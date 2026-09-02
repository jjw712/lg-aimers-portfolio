# Complementary team blending — 2026-08-24

## 배경

자체 arm의 당시 최고 Public score는 1021.40387이었습니다. Minjung이 독립적으로 개발한
모델은 단독 약 1010이었으므로 단독 점수만 보면 자체 arm보다 약했습니다. 하지만 서로
다른 feature branch와 state 처리 구조를 사용했기 때문에 잔차 보완 가능성을 OOF로
검사했습니다.

## 방법

- 팀원 예측은 `row_id, probability` 인터페이스로 정렬했습니다.
- 50:50을 먼저 하나의 고정 후보로 평가했습니다.
- 이후 leakage-controlled 2022 OOF에서 analytic convex weight를 한 번 적합했습니다.
- 추론 시 두 모델의 frozen prediction을 행 단위로 결합했습니다.

## 결과

| 구성 | Public score | 직전 대비 |
| --- | ---: | ---: |
| 자체 structured-OFF arm | 1021.40387 | - |
| 자체 + Minjung 50:50 | 1053.39443 | **+31.99056** |
| Minjung weight 0.45641368 | **1053.59248** | +0.19805 |

후속으로 자체 ensemble을 8개에서 7개로 줄이고, 2022에서 고정한 current-state gate를
결합해 저장소 재현 계보는 1055.07506까지 개선됐습니다.

## 배운 점

- 단독 점수가 낮은 모델도 기존 모델이 틀리는 행에서 다르면 강한 blend source가 됩니다.
- 팀 협업의 공용 산출물은 거대한 모델 파일보다 정직한 OOF와 provenance였습니다.
- 작은 analytic-weight 이득은 불확실성이 커서, 50:50의 큰 구조적 이득과 구분해 해석했습니다.

이 보고서의 팀 점수는 공동 성과이며, Minjung의 모델 구현을 포트폴리오 작성자의 단독
작업으로 주장하지 않습니다.

