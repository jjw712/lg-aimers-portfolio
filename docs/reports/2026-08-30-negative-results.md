# Negative results and evaluation corrections — 2026-08-30

## 목적

마감 직전에는 후보를 많이 만드는 것보다 잘못된 개선을 빠르게 무효화하는 일이 더
중요했습니다. 이날의 실험 묶음은 새 champion을 만들지 못했지만, 이후 판단을 지키는
검증 규칙을 확정했습니다.

## 대표 기각

| 축 | 관찰 | 판정 |
| --- | --- | --- |
| F specialist | 약한 과거 base 대비로는 개선처럼 보였지만 현재 계보 F 대비 악화 | `REJECT` |
| honest convex blend | 2024에 weight를 fit하고 같은 2024로 평가한 in-sample 상한 | `INVALID` |
| parallel neural members | 2023 양수였으나 2024 오라클 weight가 모두 음수 | `REJECT/CLOSED` |
| conditional fixed-effect arm | rolling weight=0, post-regime -5.25pt | `REJECT_BOTH_LANES` |
| post-regime nonlinear residual | 30pt 목표에 비해 rolling 개선확률 42.35% | `REJECT_BOTH_LANES` |

## 수정한 검증 원칙

1. 적합 연도와 평가 연도가 같으면 그 수치는 배포 이득이 아니라 oracle upper bound로 표시합니다.
2. 현재 배포 계보와 다른 약한 base를 비교 기준으로 쓰지 않습니다.
3. 일부 in-sample인 팀 OOF는 blend selection anchor로 사용하지 않습니다.
4. selection rule을 적용했다면 permutation null에서도 같은 selection을 반복합니다.
5. `gain > null`인 통계 신호와 실제 `gain > 0`인 배포 효과를 분리합니다.

## 의미

이날 통과한 신규 개인 후보는 0개였습니다. 그러나 실패 원인을 구현 문제, 평가 오염,
진짜 시간 전이 실패로 나눠 기록함으로써 같은 가설을 이름만 바꿔 반복하는 일을 막았습니다.

