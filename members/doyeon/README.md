# Doyeon

## 주요 기여

- TabNet과 ResNet-MLP를 이용한 neural diversity arm 개발
- 정제된 feature를 저차원 residual MLP에 연결하고 기존 tree ensemble과 결합
- rolling OOF와 clean variant를 공유해 neural arm의 독립적 가치를 검증할 수 있게 함

## 협업 결과

- Minjung 50:50 계보에 ResNet-MLP 15%를 결합해 **1055.5282** 보고
- 이후 clean OOF 감사에서 early-stopping 및 anchor provenance 문제를 분리해 재평가
- 강한 후속 a10bh anchor 위에서는 neural arm의 2024 증분이 유지되지 않아 배포하지 않음

성공 점수와 후속 기각을 함께 기록해, 모델 자체의 가치와 특정 anchor 위 blend 가치를
구분했습니다. 실제 코드, OOF와 가중치는 포함하지 않습니다.

