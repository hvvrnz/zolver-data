### Issue: 학과 구조화 시 단과대학명이 잘리는 현상 발생

PDF -> 텍스트 변환 과정에서 단과대학 이름이 줄바꿈 단위로 분리되어 
LLM이 "인문사회융합대학"을 "인문", "사회", "융합", "대학"처럼 독립된 섹션으로 오판하는 문제가 발생

#### 예시 입력:
{raw_text} : 졸업에 필요한 최저 이수 학점 수\n대학\n학과\n교양\n전공\n다전공\n학생\n졸업이수\n학점\n전필\n전선\n계\n디자인\n대학\n산업디자인학과\n35\n14\n58\n72\n40\n132\n실내디자인학과\n35\n13\n56\n69\n40\n132\n패션디자인학과\n35\n2\n70\n72\n40\n132\n시각영상디자인학과\ ...


#### 예시 출력 문제:
 {
      "college_name": "산업디자인학과",
      "departments": [
        {
          "department_name": "",
          "credits": {
            "general_education": 58,
            "major_required": 14,
            "major_elective": 0,
            "major_total": 72,
            "double_major": 40,
            "graduation_total": 132
          }
        },
        {
          "department_name": "실내디자인학과",
          "credits": {
            "general_education": 56,

        또는

        
      "college_name": "인문",
      "departments": [
        {
          "department_name": "경영학과",
          "credits": {

#### 원인:
1. PDF 텍스트 추출 시 개행 단위 분리
2. LLM이 복합명사를 줄 단위로 오해하는 패턴 오류

#### 해결 방향:
1. pdf -> text 추출 후 미리 문자열 정제: 줄바꿈 제거 및 단과대 명칭 수동 복원 (진행중)
2. 프롬프트에 "단과대학 이름은 공백 없이 하나의 문자열..."이라는 규칙 추가 (완료)
3. JSON 후처리에서 검증 로직 적용(예정)

