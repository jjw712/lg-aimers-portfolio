# Team collaboration

이 디렉터리는 팀 협업 구조와 역할을 설명하는 포트폴리오용 인덱스입니다. 실제 팀원 코드,
OOF, 모델, lookup, 제출 ZIP은 포함하지 않습니다. 각 README는 원본 저장소의 제출 계보와
팀 공유 기록을 요약한 것이며 팀 최종 점수는 공동 성과로 표기합니다.

## 협업 인터페이스

```text
독립 arm 개발
  -> rolling-origin OOF (`row_id`, `probability`)
  -> anchor 정렬 및 provenance 확인
  -> 단독 성능 + 잔차 보완성 측정
  -> frozen blend/gate
  -> 행 독립성 감사
  -> 팀 후보
```

| 구성원 | 주요 기여 축 | 대표 결과 |
| --- | --- | --- |
| [Jiwon](jiwon/README.md) | baseline, temporal validation, state/structured arm, blend·감사 | 자체 1021.40, 팀 OOF blend 1053.59 |
| [Minjung](minjung/README.md) | 독립 CatBoost/state arm과 OOF 공유 | 결합 시 +31.99, 후속 gate 계보 1055.08 |
| [Hyerim](hyerim/README.md) | post-regime interaction correction과 팀 상위 계보 | a10bh 1070.97, mf1101 계보 |
| [Doyeon](doyeon/README.md) | TabNet/ResNet-MLP neural diversity arm | mj50 + ResNet 15%로 1055.53 보고 |
| [Woojin](woojin/README.md) | 독립 TrackMan/current-state arm과 veteran gate | 팀 최종 1104.66 |

## 협업에서 중요했던 것

- 모델 소유권은 각 작성자에게 두고, 통합에는 최소한의 예측 인터페이스를 사용했습니다.
- held-out OOF와 in-sample diagnostic prediction을 구분했습니다.
- 팀원이 만든 모델의 결과를 개인 단독 성과로 표현하지 않았습니다.
- 강한 팀 앵커 뒤에서도 순증분이 남는지를 별도로 확인했습니다.

