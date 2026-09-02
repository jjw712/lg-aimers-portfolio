# Experiment log

원본 연구 저장소의 제출 로그와 실험 보고서를 공개 가능한 범위로 다시 정리한 대장입니다.
날짜는 제출 또는 보고서 실행 기록 기준이며, 팀 공동 점수는 개인 단독 성과와 구분합니다.
원본 데이터, OOF, 모델 가중치, 제출 ZIP과 팀원 코드는 포함하지 않습니다.

## 한눈에 보기

| 항목 | 기록 |
| --- | ---: |
| 첫 정상 Public 제출 | 793.00000 |
| 가장 큰 개인 단일 개선 | +99.53145 |
| 자체 arm 최고 | 1021.40387 |
| 독립 팀원 arm 결합 이득 | +31.99056 |
| 팀 최종 최고 | 1104.66497 |
| 아래에 기록한 제출·모델 변경 | 22건 |
| 아래에 기록한 대표 연구 스크린 | 12건 |

성과표만 남기지 않고 기각·무효화 기록도 같은 대장에 보존했습니다. 특히 `REJECT`는
아이디어가 무가치하다는 뜻이 아니라, 사전에 고정한 검증 조건에서 배포 근거가 부족했다는
뜻입니다.

상태 표기는 다음 의미입니다.

- `SUCCESS`: 실제 Public 점수 또는 사전 고정된 검증에서 개선
- `REJECT`: 정직한 전방 검증이나 효과 크기 기준을 통과하지 못함
- `SUPERSEDED`: 유효했지만 이후 더 나은 계보로 교체
- `INVALID`: 앵커·가중치·평가 설계 오류로 해당 수치를 근거에서 제외
- `CLOSED`: 같은 표현만 바꾼 재시도를 막기 위해 실험 축을 종료

## 1. 모델 및 제출 계보

| 날짜 | 실험 | 결과 | Public score | 판정 및 해석 |
| --- | --- | ---: | ---: | --- |
| 2026-08-06 | F recent CatBoost + R temporal 4-model blend | 첫 정상 코드 제출 | 793.00000 | `SUCCESS`; 이후 모든 비교의 출발점 |
| 2026-08-07 | context-v2 LightGBM을 R의 5번째 멤버로 추가 | +18.88 | 811.87621 | `SUCCESS`; 모델 다양성이 초기에는 유효 |
| 2026-08-11 | count/hand/state/context 계층 잔차 보정 | 약 +8.12 | 약 820.00000 | `SUCCESS`; 2023·2024에서 같은 방향 확인 |
| 2026-08-12 | refined 15-class F + 6번째 R 멤버 | +46.20 | 866.19746 | `SUCCESS`; route별 타깃 구조 분리가 크게 기여 |
| 2026-08-12 | call-refined 50:50 F + 7번째 R 멤버 | +15.13 | 881.32298 | `SUCCESS` |
| 2026-08-12 | pitch-type refined F + 8번째 R 멤버 | +16.19 | 897.51448 | `SUCCESS` |
| 2026-08-13 | recent-form residual correction | +6.37 | 903.88440 | `SUCCESS`; train에서 고정한 row-local 보정 |
| 2026-08-13 | current-season pitcher/batter state correction | **+99.53** | **1003.41585** | `SUCCESS`; 가장 큰 개인 단일 도약, 독립성 감사 통과 |
| 2026-08-23 | structured-OFF parallel R blend | +15.91 | 1019.32873 | `SUCCESS`; 구조가 다른 병렬 arm의 가치 확인 |
| 2026-08-24 | structured-OFF weight 0.511 고정 | +2.08 | 1021.40387 | `SUCCESS`; 이후 자체 arm 기준점 |
| 2026-08-24 | 같은 weight를 0.600으로 변경 | -4.13 | 1015.19378 | `REJECT`; 상수의 과도한 이동은 바로 악화 |
| 2026-08-24 | 자체 arm과 Minjung arm 50:50 | **+31.99** | **1053.39443** | `SUCCESS`; 독립 팀원 arm의 보완성이 가장 큰 팀 블렌드 이득 |
| 2026-08-24 | 2022 OOF analytic weight, Minjung 0.4564 | +0.20 | 1053.59248 | `SUCCESS`, 단 bootstrap 신뢰는 낮아 후속 계보로 교체 |
| 2026-08-26 | 자체 R ensemble 8→7 member pruning | +0.15 | 1053.73803 | `SUCCESS`; 복잡도 감소와 작은 점수 개선을 동시에 확보 |
| 2026-08-26 | Minjung state hard gate, T=15 | +1.00 | 1054.59276 | `SUPERSEDED`; submission-tier 개선, 엄격 월별 gate는 미달 |
| 2026-08-26 | pruning + T=20 state gate | +0.33 | 1055.07506 | `SUCCESS`; 로컬 저장소에서 완전 재현 가능한 팀 블렌드 최고 |
| 2026-08-28 | Hyerim a10bh 계보 | 팀 모델 도약 | 1070.96610 | `SUCCESS`; 최신 레짐과 상호작용 보정이 팀 계보를 확장 |
| 2026-08-28 | a10bh correction scale 0.25→0.50 | -3.93 | 1067.03954 | `REJECT`; 로컬 선호 상수가 2025 Public으로 전이되지 않음 |
| 2026-08-29 | team 1101 위 batter main, scale 0.50 | -1.44 | 1099.90590 | `REJECT`; 과대 보정 |
| 2026-08-29 | 같은 사전등록 축의 scale 0.25 | +1.12 | 1102.47038 | `SUCCESS`; 실제 점수로 곡선 방향 확인 |
| 2026-08-30 | team 1101 + Woojin 5% veteran gate | +3.31 | **1104.66497** | `SUCCESS`; 팀 최종 최고, 팀 공동 성과 |

Public 점수는 Brier Skill Score 계열 척도입니다. 위 표의 `약 820`은 당시 사용자 보고의
반올림값이며, 나머지는 제출 로그에 기록된 값입니다.

## 2. 대표 연구 스크린과 종료 판단

| 시기 | 가설/실험 축 | 핵심 관찰 | 상태 | 남은 지식 |
| --- | --- | --- | --- | --- |
| 2026-08-20 | TrackMan privileged-information distillation v2 | teacher 신호는 존재했지만 2022 exact blend weight=0, gain=0 | `REJECT/CLOSED` | teacher가 강해도 champion 위 순증분이 없으면 blend source가 아님 |
| 2026-08 하순 | retention shrinkage / era prior / R-only career prior | 선수 과거 평균은 일부 retention이 있어도 다음 연도 Brier로 안정 전이하지 않음 | `REJECT` | 원시 prior와 수축 prior 모두 전방 검증 필요 |
| 2026-08-26 | regime-gated multi-expert | 2024 개선확률 98.65%였지만 delta 약 -0.0000104로 최소 효과의 24% | `REJECT` | 통계적 방향성과 실용적 크기는 별개 |
| 2026-08 하순 | Season Group DRO | exact anchor에서 2023/2024 모두 악화, 2024 P(improve)=14.0% | `REJECT/CLOSED` | 연도 최악손실 최적화가 자동으로 미래 안정성을 만들지 않음 |
| 2026-08-28 | post-regime batter main effects | batter main scale 0.25만 실제 +1.12, 다수 상호작용은 배포 채널에 흡수 | `PARTIAL SUCCESS` | 타자 효과의 retention이 투수 효과보다 높았음 |
| 2026-08-30 | parallel neural blend members | 2023 양수 뒤 2024 오라클 가중치가 음수로 반전 | `REJECT/CLOSED` | 알고리즘 다양성보다 잔차 방향의 연도 전이가 중요 |
| 2026-08-30 | conditional fixed-effect arm | rolling weight=0, post-regime -5.25pt, P(improve)=13.5% | `REJECT_BOTH_LANES` | 고정효과 제거 후 공유효과만 학습하는 방식도 순증분 없음 |
| 2026-08-30 | post-regime nonlinear residual, +30pt 목표 | rolling 2024 P(improve)=42.35%, post-regime scale=0 | `REJECT_BOTH_LANES` | 큰 폭의 추가 이득을 뒷받침할 잔차 신호가 없었음 |
| 2026-08-31 | batter F→R prior | rolling pooled -0.23pt, post-regime +0.04pt/P=51.7% | `REJECT_BOTH_LANES` | 레짐을 나눠도 효과가 사실상 0 |
| 2026-08-31 | high-retention lookup stack | control보다 안정적이나 어떤 순차 단계도 사전 gate를 통과하지 못함 | `REJECT` | 약한 유효 신호를 여러 개 쌓는다고 강한 arm이 되지 않음 |
| 2026-08-31 | recent-game denominator reconstruction | raw 신호는 +13.51/+8.72pt였으나 전체 chain 뒤 2024 증분 z=0 | `REJECT/CLOSED` | 새 피처가 유효해도 강한 계보가 이미 정보를 흡수할 수 있음 |
| 2026-09 초 | joint reconstruction neural arm | 2023 proxy +7.27pt 뒤 2024 -26.81pt, post-regime weight=0 | `REJECT_BOTH_LANES` | auxiliary reconstruction도 시간 전이 실패를 해결하지 못함 |

정확한 날짜가 원본 결과에 남지 않은 항목은 억지로 일자를 만들지 않고 `8월 하순` 또는
`9월 초`로 표시했습니다.

## 3. 무효화하거나 다시 계산한 결과

실패뿐 아니라 평가 설계가 틀린 결과도 별도로 보존했습니다.

- `mf1101`의 2023/2024 OOF는 일부 또는 전체가 보정 적합에 사용돼, 그 위의 블렌드
  자기평가는 실제 이득보다 크게 부풀 수 있었습니다. 이후 판정 앵커를 held-out 계보로 분리했습니다.
- 2024에 가중치를 적합하고 같은 2024로 평가한 convex blend 결과는 `INVALID` 처리했습니다.
- regime-gated confirmation에서 폐기된 development weight를 읽은 최초 결과는 무효화하고,
  frozen prediction과 canonical report SHA-256을 고정해 순수 산술로 다시 계산했습니다.
- 점수가 약한 구형 base를 현재 champion처럼 사용한 F specialist 평가는 재계산 후 기각했습니다.

이 기록은 실수를 숨기지 않고, 잘못된 결론이 다음 실험으로 전파되지 않게 만든 과정입니다.

## 4. 실험 운영 규칙의 변화

1. `season < Y`만 쓰는 rolling-origin 검증과 `early2024 → late2024` post-regime 검증을 분리했습니다.
2. 후보 단독 개선, champion 위 blend 순증분, 실제 배포 채널 뒤 순증분을 서로 다른 질문으로 봤습니다.
3. 가중치·gate·scale은 source 기간에서 고정하고 target 결과를 본 뒤 바꾸지 않았습니다.
4. selection-aware permutation/null과 pitcher-cluster bootstrap을 사용했습니다.
5. anchor, OOF provenance, frozen weight, artifact SHA-256을 결과와 함께 기록했습니다.
6. 제출 전 singleton/batch/shuffle/add-remove 불변성과 test 기반 집계 부재를 감사했습니다.

## 5. 읽을 만한 사례

- [current-season state breakthrough](reports/2026-08-13-current-state-breakthrough.md)
- [complementary team blending](reports/2026-08-24-complementary-team-blend.md)
- [negative results and corrections](reports/2026-08-30-negative-results.md)
