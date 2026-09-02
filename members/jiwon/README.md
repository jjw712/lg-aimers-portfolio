# Jiwon

## 역할

- 초기 routed CatBoost/LightGBM ensemble과 rolling-origin 검증 체계 구축
- current-season pitcher/batter state 복원 및 row-local residual correction
- structured-OFF 병렬 arm, exact convex blend, member pruning과 state gate 통합
- singleton/batch/shuffle/add-remove 행 독립성 감사와 실험 보고서 관리

## 대표 결과

- current-season state correction: 903.88440 → **1003.41585**
- 자체 structured-OFF 계보: **1021.40387**
- Minjung OOF와 analytic blend: **1053.59248**
- pruned own arm + Minjung state gate의 재현 가능한 계보: **1055.07506**

팀 최종 1104.66497은 아래 구성원들의 후속 모델링이 더해진 공동 성과입니다.

## 공개 범위

이 포트폴리오에는 일반화 가능한 검증·블렌딩·감사 코드만 재구성했습니다. 대회 원본
feature pipeline, 선수별 통계, 팀원 자산과 제출물은 포함하지 않습니다.

