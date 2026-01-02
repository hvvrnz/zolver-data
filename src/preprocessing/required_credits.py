import re


# ============================================================================
# 0. 상수 / 패턴 (기존 그대로)
# ============================================================================

HAS_ONLY_MAJOR_REQUIRED = {"의학과", "의예과"}

college_pattern = re.compile(r'(\s?)([가-힣\s]+?대학)(\s?)')


# ============================================================================
# 1. 단과대학명 공백 정규화 (기존 로직 그대로)
# ============================================================================

def normalize_college(match):
    college = match.group(2).replace(" ", "")
    return f"{match.group(1)}{college}{match.group(3)}"


# ============================================================================
# 2. 테이블 텍스트 추출 (기존 실행 코드 → 함수화)
# ============================================================================

def extract_table_text(text):
    m = re.search(
        r'졸업에 필요한 최저 이수 학점 수.*?계 ',
        text
    )

    if not m:
        raise ValueError("TableStartNotFound")

    table_text = text[m.end():]
    table_text = re.sub(r'\s(-|0)\s', ' ', table_text)
    table_text = college_pattern.sub(normalize_college, table_text)

    return table_text


# ============================================================================
# 3. raw_nums 전처리 (로직 1도 변경 없음)
# ============================================================================

def preprocessing_raw_nums(department, raw_values):
    """
    core: 총졸업 제외한 raw_nums
    길이: 2 ~ 5
    """
    n = len(raw_values)

    general = None
    major_required = None
    major_elective = None
    double_major = None

    if n == 2:  # 전필/전선 + 전공계
        a, major_total = raw_values
        if department in HAS_ONLY_MAJOR_REQUIRED:
            major_required = a
        else:
            major_elective = a

    elif n == 3:  # 교양 + 전필 + 전공계
        general, a, major_total = raw_values
        major_required = a

    elif n == 4:  # 교양 / 전필 / 전선 / 전공계
        a, b, c, d = raw_values

        # 전필 + 전선 = 전공계
        if b + c == d:
            general = a
            major_required = b
            major_elective = c
            major_total = d

        # 2) 교양 / 전선 / 전공계 / 다전공
        else:
            general = a
            major_elective = b
            major_total = c
            double_major = d

    elif n == 5:  # 교양 / 전필 / 전선 / 전공계 / 다전공
        general, major_required, major_elective, major_total, double_major = raw_values

    else:
        raise ValueError(f"Unexpected core length: {raw_values}")

    return {
        "general": general,
        "major_required": major_required,
        "major_elective": major_elective,
        "major_total": major_total,
        "double_major": double_major,
    }


# ============================================================================
# 4. 단과대학 state 기반 전체 파싱 (로직 그대로)
# ============================================================================

def result_rows(table_text):
    tokens = table_text.split()

    result_rows = []
    current_college = None
    i = 0

    while i < len(tokens):
        token = tokens[i]

        # 단과대학
        if token.endswith("대학"):
            current_college = token
            i += 1
            continue

        # 학과
        if token.endswith("학과"):
            department = token

            raw_nums = []
            j = i + 1

            while j < len(tokens) and tokens[j].isdigit():
                raw_nums.append(int(tokens[j]))
                j += 1

            if len(raw_nums) < 2:
                raise ValueError(f"Invalid raw_nums: {department}, {raw_nums}")

            # 총졸업학점 분리
            total_credits = raw_nums[-1]
            raw_values = raw_nums[:-1]

            complete_preprocessing = preprocessing_raw_nums(department, raw_values)

            result_rows.append({
                "college": current_college,
                "department": department,
                **complete_preprocessing,
                "total_credits": total_credits,
            })

            i = j
            continue

        i += 1

    return result_rows
