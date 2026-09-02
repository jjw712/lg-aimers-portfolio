# Documentation

이 디렉터리는 프로젝트의 결과뿐 아니라 검증 방법, 실패 과정과 협업 방식을 함께 설명합니다.

## 먼저 읽을 문서

1. [전체 실험 대장](experiment_log.md)
   - 날짜별 가설, Public 점수 변화, 성공·기각·무효화·종료 판단
2. [검증 전략](validation_strategy.md)
   - rolling-origin split, frozen weight, 행 독립성 감사
3. [실험 회고](experiment_summary.md)
   - 프로젝트 전체에서 반복해서 확인된 핵심 교훈
4. [대표 사례 보고서](reports/README.md)
   - 큰 성공 2건과 평가 오류·실패를 정리한 사례 1건
5. [팀 협업 구조](../members/README.md)
   - 구성원별 역할, OOF 중심 협업 인터페이스, 공개 범위

## 공개본의 범위

문서는 원본 내부 실험 보고서를 요약하지만 다음 자산은 포함하지 않습니다.

- 대회 데이터와 파생 데이터
- 팀원 소스 코드와 비공개 feature pipeline
- OOF·test prediction·선수별 lookup
- 모델 가중치, final bundle과 제출 ZIP

포함된 코드는 합성 데이터에서 검증 가능한 temporal split, Brier blend와 행 독립성 감사의
최소 재구성본입니다.

