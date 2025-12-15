# Data Pipeline Log 기반 분석 데모

## 목적
본 디렉토리는 데이터 파이프라인 처리 과정에서 발생한
실제 이슈들을 기반으로,
로그 관점에서 input/output 흐름을 추적하고
Data Asset 및 Data Lineage로 확장하는 사고 과정을 정리합니다.

## 파이프라인 개요
PDF → Text → LLM 구조화(JSON) → 테이블 적재

## 로그 관점 해석
각 처리 단계는 다음과 같은 로그 정보를 생성한다고 가정합니다.
- job_name
- input_asset
- output_asset
- status
- 품질 이슈 유형

이를 통해 데이터 흐름과 문제 발생 지점을 추적합니다.

## 관련 이슈 문서
- college_name_issue.md
- llm_result_issue.md
