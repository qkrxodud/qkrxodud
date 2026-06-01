# 박태영 (Taeyoung Park)

**Backend Developer** | 안정적이고 확장 가능한 서버를 고민하는 개발자

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://url.kr/o8rerj)
[![Tech Blog](https://img.shields.io/badge/Tech_Blog-000000?style=flat-square&logo=notion&logoColor=white)](https://www.coby-blog.co.kr/)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:qkrxodud00@gmail.com)

---

## 👨‍💻 About Me

안녕하세요! **대규모 트래픽 환경에서 안정적인 백엔드 시스템을 설계하고 운영**하는 것에 즐거움을 느끼는 개발자입니다.

- 🔧 **주력 기술**: Java, Spring Boot, JPA — 견고한 도메인 설계와 테스트 가능한 구조를 지향합니다.
- ⚡ **강점**: 성능 최적화와 분산 시스템 — Kafka, Redis, 분산 락을 활용한 동시성 제어에 관심이 많습니다.
- 🔬 **깊게 파고드는 것**: JVM 내부 동작, 동시성(JMM·synchronized·가상 스레드), 트랜잭션 & DB 성능
- 📝 **일하는 방식**: 실무에서 마주친 문제를 직접 분석하고 해결한 뒤, [기술 블로그](https://www.coby-blog.co.kr/)에 정리하며 팀과 공유합니다.
- 💡 **개발 철학**: *"동작하는 깨끗한 코드"* — 읽기 좋은 코드, 테스트 가능한 설계, 지속적인 개선

---

## 🛠 Tech Stack

**Language & Framework**

![Java](https://img.shields.io/badge/Java-007396?style=flat-square&logo=openjdk&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white)
![Spring Data JPA](https://img.shields.io/badge/Spring_Data_JPA-6DB33F?style=flat-square&logo=spring&logoColor=white)
![MyBatis](https://img.shields.io/badge/MyBatis-DC382D?style=flat-square&logo=&logoColor=white)

**Database & Cache**

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)

**Message Queue**

![Apache Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white)

**Infra & DevOps**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)

**Tools & Collaboration**

![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)
![IntelliJ IDEA](https://img.shields.io/badge/IntelliJ_IDEA-000000?style=flat-square&logo=intellijidea&logoColor=white)
![Notion](https://img.shields.io/badge/Notion-000000?style=flat-square&logo=notion&logoColor=white)

---

## 💪 핵심 역량

| 분야 | 설명 |
| --- | --- |
| **성능 최적화** | 실행 계획(EXPLAIN) 분석, 인덱스 설계, 쿼리 튜닝을 통한 응답 속도 개선 |
| **분산 시스템** | Kafka 기반 이벤트 처리, Redis · Redisson 분산 락을 활용한 동시성 제어 |
| **동시성 & JVM** | JMM, `synchronized`, 가상 스레드 등 내부 동작 이해를 바탕으로 한 설계 |
| **품질 & 협업** | TDD 적용, 코드 리뷰 문화 정착, 가독성 높은 기술 문서 작성 |

---

## 🚀 Projects

### [Trading Bot](https://github.com/qkrxodud/trading_bot) `완료 ✅`
**실시간 암호화폐 자동매매 시스템** — 5/20 이동평균선 교차 전략 기반 트레이딩 봇

- 업비트 API 연동으로 실시간 시세 수집 및 골든크로스/데드크로스 자동 감지
- Spring WebFlux 기반 비동기 처리로 효율적인 API 호출
- 클린 아키텍처 적용 (Domain–Infrastructure 분리)
- 텔레그램 봇 연동 실시간 매매 신호 알림 / JUnit 5 기반 TDD
- `BigDecimal`로 금융 계산 정확성 확보, Fake 객체 활용 단위 테스트

**Tech** · Spring Boot 3.5.6 · Java 21 · WebFlux · JPA · H2 · Telegram API

---

### [User Refund Calculator](https://github.com/qkrxodud/UserRefundCalculator) `완료 ✅`
**유저 환급금 조회 서비스** — 회원 인증부터 결정세액 조회까지의 API 서버

- 회원 가입 / 로그인 인증 API 설계
- 외부 데이터 스크래핑 API 연동 및 결정세액 조회 로직 구현
- 계층 분리를 고려한 도메인 중심 구조

**Tech** · Spring Boot 3.3.0 · Java 17 · JPA · H2 · JUnit 5 · Gradle

---

### [Pharmacy Management System](https://github.com/qkrxodud/pharmacy) `완료 ✅`
**약국 길찾기 서비스** — 위치 기반 가까운 약국 추천 및 경로 안내

- 카카오 주소 검색 / 지도 API 연동
- Haversine 알고리즘 기반 최단거리 약국 추천
- Redis 캐싱을 통한 응답 속도 개선
- 공공 데이터 API 활용 및 데이터 정제, Docker 컨테이너 환경 구축
- Spock 프레임워크 기반 BDD 스타일 테스트

**Tech** · Spring Boot · JPA · Redis · Docker · Kakao API · Spock

---

## 📝 Recent Blog Posts

실무 경험과 학습 내용을 [기술 블로그](https://www.coby-blog.co.kr/)에 꾸준히 정리하고 있습니다.

- [실무에서 잘못 사용하고 있던 Transaction](https://www.coby-blog.co.kr/108db2e0-c45e-8012-89d5-ce76a9bc1ad6)
- [Garbage Collection 튜닝](https://www.coby-blog.co.kr/c2b3527e-9868-4a14-b4e0-378e626d68fc)
- [DBCP (Database Connection Pool) 이해하기](https://www.coby-blog.co.kr/8a8ec26b-2675-442f-b7b2-893a33227627)

---

## 📊 GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=qkrxodud&show_icons=true&theme=default&hide_border=true&count_private=true" alt="GitHub Stats" height="165" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=qkrxodud&layout=compact&theme=default&hide_border=true" alt="Top Languages" height="165" />
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com/?user=qkrxodud&theme=default&hide_border=true" alt="GitHub Streak" />
</p>

---

## 📫 Contact

협업 제안이나 기술 이야기는 언제든 환영합니다!

- **Email** · qkrxodud00@gmail.com
- **LinkedIn** · [linkedin.com/in/taeyoung-park](https://url.kr/o8rerj)
- **Tech Blog** · [coby-blog.co.kr](https://www.coby-blog.co.kr/)

---

<div align="center">

*"Clean code that works" — 동작하는 깨끗한 코드를 작성하기 위해 노력합니다.*

</div>
