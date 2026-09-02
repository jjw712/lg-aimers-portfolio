# Woojin

## 주요 기여

- TrackMan release/context와 current-season state를 결합한 독립 CatBoost arm 개발
- strict rolling OOF와 veteran-pitcher 구간에서의 보완 신호 공유
- 강한 팀 anchor에 작은 고정 가중치로 적용하는 gated blend 제안

## 협업 결과

- 독립 모델 Public: **1016.7228**
- `game_type=R`이면서 충분한 pitcher history가 있는 행에만 Woojin arm 5% 적용
- 팀 1101 계보 대비 **+3.315**, 팀 최종 최고 **1104.66497**

gate 임계값과 가중치는 결과를 본 뒤 재탐색하지 않았으며, 실제 모델·OOF·제출 ZIP은
이 공개용 저장소에 포함하지 않습니다.

