```
➜  ~ whoami
박태영 (코징) — 백엔드 개발자, Java · Spring
```

실무에서 막혔던 문제를 끝까지 파고든 다음 [블로그](https://qkrxodud.github.io/tech-blog/)에 정리합니다.
급하게 고치고 넘어가면 다음에 같은 자리에서 또 막히더라고요. 그래서 "왜 그렇게 동작하는지"까지 보고 넘어가려고 합니다.

요즘은 Claude Code로 에이전트 여러 개를 묶어 개인 프로젝트를 만들고 있습니다.

```
➜  ~ cat stack.txt
lang      Java, Python
backend   Spring Boot, JPA, MyBatis, WebFlux
data      MySQL, Redis, Kafka, Elasticsearch
infra     Docker, Kubernetes, GitHub Actions
etc       Flutter, Next.js, Firebase
```

### `$ ls projects/`

운영 중인 것

- [BTC 레이더](https://btctiming.co.kr) — 비트코인 시장 지표 25가지를 매일 모아 한 화면에 보여 줍니다. Python으로 스냅샷을 만들어 정적 사이트로 배포하기 때문에 따로 띄워 둔 서버가 없습니다.
- [또렷](https://qkrxodud.github.io/easy-read/) — 웹 페이지에 책갈피와 형광펜을 남기는 크롬 익스텐션
- [내용](https://naeyong.co.kr) — 내용증명, 차용증 같은 문서를 단계별로 작성해 줍니다. 입력한 내용은 브라우저 밖으로 나가지 않습니다.

만들고 있는 것

- [running](https://github.com/qkrxodud/running) — 러닝 크루 앱. 서버가 GPS 트랙을 검증해서 완주 여부와 순위를 확정합니다. 헥사고날 구조의 Spring Boot(Java 25) + Flutter. 트랙 정제와 순위 계산은 순수 함수로 빼서 골든 테스트 175개로 묶어 뒀고, 버그가 나오면 회귀 테스트부터 추가합니다.
- [interview-connect](https://github.com/qkrxodud/interview-connect) — 면접을 먼저 본 사람과 준비하는 사람을 이어 주는 서비스. Spring Boot + Next.js, TDD로 진행 중입니다.

<details>
<summary>예전 것들</summary>

- [trading_bot](https://github.com/qkrxodud/trading_bot) — 업비트 이동평균 교차 자동매매. WebFlux, Telegram 알림
- [UserRefundCalculator](https://github.com/qkrxodud/UserRefundCalculator) — 환급금 조회 API, 외부 스크래핑 연동
- [pharmacy](https://github.com/qkrxodud/pharmacy) — 위치 기반 약국 추천. 카카오 지도 API, Redis 캐싱, Spock

</details>

### `$ ls -lt posts/ | head -5`

- [SimpleDateFormat 동시성 문제부터 불변 객체까지](https://qkrxodud.github.io/tech-blog/posts/simpledateformat-thread-safety/)
- [Spring Session Redis에서 중복 로그인이 막히지 않는 원인 (SessionRegistry)](https://qkrxodud.github.io/tech-blog/posts/spring-session-registry-redis/)
- [MySQL DATETIME과 TIMESTAMP](https://qkrxodud.github.io/tech-blog/posts/mysql-datetime-timestamp/)
- [데드락의 네 가지 조건과 해결 전략](https://qkrxodud.github.io/tech-blog/posts/deadlock/)
- [ElasticSearch를 도입하게 된 이유](https://qkrxodud.github.io/tech-blog/posts/es-intro/)

더 보기 → [qkrxodud.github.io/tech-blog](https://qkrxodud.github.io/tech-blog/)

### `$ contact`

[qkrxodud00@gmail.com](mailto:qkrxodud00@gmail.com) · [LinkedIn](https://url.kr/o8rerj) · [Blog](https://qkrxodud.github.io/tech-blog/)
