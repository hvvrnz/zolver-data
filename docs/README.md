## 프로젝트 개요
학사 요람 PDF 데이터를 기반으로 비정형 데이터 → 구조화 데이터로 변환하는
데이터 파이프라인 실험 프로젝트입니다.

## 파이프라인 구성
1. PDF → Text 추출
2. Raw Text → LLM 구조화 실험
3. LLM 출력 불안정성 이슈 분석
4. Rule-based 전처리 필요성 도출
5. (개념 데모) Data Lineage 구성 방향 제시

## 주요 이슈 및 인사이트
- LLM 단독 사용 시 JSON 구조 불안정
- 대학/단과대/학과 개념 혼동 발생
- Rule-based 전처리 + LLM 보조 판단 구조가 필요함

## 향후 확장 방향
- Rule-based 전처리 규칙 고도화
- Embedding 기반 유사도 매칭을 활용한 단과대/학과 자산 자동 매핑
- 데이터 자산(Asset) 간 관계 그래프를 기반으로 한 End-to-End Data Lineage 자동화
- ex)
    PDF (page 5)
    → raw_text
    → LLM_input
    → LLM_output(JSON)
    → post_processed_json

