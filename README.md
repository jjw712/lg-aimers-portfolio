# Temporal Probability Forecasting for Pitch Control

LG Aimers 야구 투구 데이터에서 다음 투구의 제구 성공 확률을 예측하며 구축한
검증·앙상블·추론 감사 방법을 공개 가능한 형태로 정리한 포트폴리오 저장소입니다.

원본 대회 데이터, 팀원 코드, 선수별 lookup, OOF 예측, 모델 가중치와 제출 파일은
포함하지 않습니다. 포함된 테스트는 전부 합성 데이터만 사용합니다.

## 문제 정의

- 목표: 투구 직전 정보로 이진 사건의 발생 확률 예측
- 평가: Brier Score 기반 확률 예측 품질
- 핵심 난점: 미래 시즌으로의 분포 이동과 확률 보정 변화
- 추론 제약: 한 평가 행의 예측이 다른 평가 행의 존재·순서에 의존하면 안 됨

## 핵심 기여

1. **Rolling-origin validation**
   - 검증 시즌 `Y`에 대해 `season < Y`만 학습에 사용합니다.
   - 랜덤 분할이 숨길 수 있는 연도 간 전이 실패를 직접 측정합니다.
2. **Brier-optimal convex blending**
   - OOF 예측만으로 비음수·합 1 제약의 앙상블 가중치를 적합합니다.
   - 가중치는 이후 시즌에 고정해 사후 재튜닝을 막습니다.
3. **Row-independent inference audit**
   - singleton, batch size, shuffle, 행 추가·제거 조건에서 같은 행의 예측이
     동일한지 자동 검증합니다.
4. **실패를 포함한 실험 관리**
   - 단독 점수뿐 아니라 잔차 보완성, 시간 전이, 안정성을 기준으로 후보를 종료했습니다.
5. **OOF 중심 팀 협업**
   - 팀원의 모델 파일을 한 저장소에 합치기보다 `row_id, probability` 형식의 OOF와
     예측 계보를 공유해 서로 다른 arm을 독립적으로 검증하고 결합했습니다.

## 결과

수치는 원본 저장소의 제출·실험 기록을 바탕으로 하며 역할 범위를 구분합니다.

| 단계 | Public score | 기여 범위 |
| --- | ---: | --- |
| 첫 정상 제출 | 793.00000 | 초기 routed ensemble |
| current-season state 도입 | 1003.41585 | 개인 모델링·행 독립성 감사 |
| 자체 structured-off 개선 | 1021.40387 | 개인 모델링·검증 |
| 보완적 팀원 모델과 OOF 블렌딩 | 1053.59248 | 블렌딩 설계·통합 |
| 팀 veteran-gate 계보 | 1104.66497 | 팀 전체 성과 |
| 팀 최종 기록 | 1126.23661 | 팀 전체 성과 |

점수 차이는 대회의 공식 Brier Skill Score 척도이며 정확도 퍼센트가 아닙니다.
최종 순위는 165위로 상위 약 15%입니다. 이 저장소의 실험 기록은 2026-08-31까지이며,
그 이후의 팀 제출 계보는 포함하지 않습니다.
팀 최종 점수를 개인 단독 성과로 주장하지 않습니다.

## 공개 코드

```text
src/pitch_control/
  metrics.py       Brier Score와 대회형 skill score
  temporal.py      rolling-origin 분할
  blending.py      convex probability blend
  invariance.py    행 독립성 동적 감사
tests/              합성 데이터 단위 테스트
docs/
  experiment_log.md 날짜·가설·성공/실패가 포함된 실험 대장
  reports/          공개용으로 다시 쓴 대표 사례 보고서
members/            팀원별 역할과 협업 산출물 요약 README
```

## 실행

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m pytest -q
```

## 설계 원칙

```text
공식 과거 데이터
    -> season < Y 학습
    -> Y년 OOF 예측
    -> Brier/안정성/보완성 평가
    -> 동결된 모델·가중치
    -> 행 독립성 감사
    -> 배포 후보
```

## 협업 방식

팀원은 서로 다른 모델 계열을 독립 arm으로 개발하고, 시간순 OOF와 재현 정보를 공유했습니다.
통합 단계에서는 단독 점수보다 기존 앵커의 잔차를 보완하는지 확인했고, 실제 배포 계보에
얹은 뒤 남는 순증분을 다시 측정했습니다. 팀원별 기여와 공개 범위는
[members/README.md](members/README.md)에 정리했습니다.

보다 자세한 내용은 [문서 인덱스](docs/README.md),
[전체 실험 대장](docs/experiment_log.md), [검증 전략](docs/validation_strategy.md),
[대표 사례 보고서](docs/reports/README.md), [공개 전 점검표](PUBLICATION_CHECKLIST.md)를
참고하세요.

## 공개 범위

이 저장소는 포트폴리오용 최소 재구성본입니다. 대회 원본 저장소의 경로와 내부 구현을
그대로 복제하지 않았으며, 데이터와 팀 공동 자산은 공개하지 않습니다.
