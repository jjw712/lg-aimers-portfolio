# Hyerim

## 주요 기여

- 최신 시즌에 맞춘 pitcher/batter interaction과 post-regime residual correction 탐색
- 투수별 좌우타 상성, 2-strike sensitivity, count leverage, TrackMan pitch tendency 등
  여러 row-local lookup channel을 팀 계보에 통합
- 상위 팀 anchor와 OOF 성격에 대한 공유 문서 제공

## 협업 결과

- a10bh 팀 계보: **1070.96610**
- 후속 post-regime correction을 포함한 mf1101 계보: 약 **1101.35**
- 2023/2024 diagnostic OOF 일부가 correction fit에 사용됐다는 제한을 명시해,
  후속 blend 판정에서는 held-out anchor를 사용하도록 개선

실제 correction table, 모델, OOF와 제출 파일은 포함하지 않습니다.

