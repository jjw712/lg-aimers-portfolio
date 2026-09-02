# Minjung

## 주요 기여

- 자체 baseline 위에 current-season state branch를 둔 독립 CatBoost ensemble 개발
- 2022/2023/2024 OOF를 공용 `row_id, probability` 형식으로 공유
- 기존 자체 arm과 다른 오류 패턴을 제공해 팀 병렬 블렌드의 핵심 source 역할

## 협업 결과

- 자체 arm 1021.40387 + Minjung arm 50:50: **1053.39443** (`+31.99056`)
- 2022 OOF analytic weight 0.45641368: **1053.59248**
- 이후 pruning과 current-state gate를 결합한 재현 계보: **1055.07506**

실제 모델 코드, OOF와 번들은 이 공개용 저장소에 포함하지 않습니다.

