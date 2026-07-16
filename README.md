<div align="center">

# 박태영 · Taeyoung Park

### Backend Developer

**견고한 도메인 설계**로 서버를 만들고, **AI 에이전트 하네스**로 개발 프로세스까지 설계합니다.

[![Tech Blog](https://img.shields.io/badge/Tech_Blog-000000?style=flat-square&logo=notion&logoColor=white)](https://www.coby-blog.co.kr/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://url.kr/o8rerj)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:qkrxodud00@gmail.com)

</div>

---

## 👋 한 줄 소개

> **"동작하는 깨끗한 코드"** — 대규모 트래픽 환경에서 **안정적으로 확장되는 백엔드**를 설계하고, 문제를 직접 분석해 **실제 서비스로 배포**하는 개발자입니다.

- 🔧 **주력** — Java · Spring Boot · JPA. 테스트 가능한 구조와 견고한 도메인 모델을 지향합니다.
- ⚡ **강점** — Kafka · Redis · 분산 락 기반의 **동시성 제어**와 **성능 최적화**.
- 🤖 **차별점** — **Claude Code 기반 멀티 에이전트 하네스**를 직접 설계해, 기획→도메인→구현→테스트→QA 파이프라인을 자동화하며 개발합니다.
- 📝 **일하는 방식** — 실무에서 마주친 문제를 파고들어 해결하고, [기술 블로그](https://www.coby-blog.co.kr/)에 정리해 팀과 공유합니다.

---

## 🚀 최신 프로젝트

> 최근 작업일수록 위에 배치했습니다. 각 프로젝트의 **핵심 도전 과제**를 굵게 표시했습니다.

### 🟢 [BTC Timing](https://btctiming.co.kr) — 비트코인 지표 대시보드 `서비스 운영 중`

> **배경** — 비트코인 시장을 판단하려면 RSI·MVRV·SOPR·펀딩비 등 수십 개 지표를 매일 흩어진 곳에서 확인해야 합니다. 이걸 한 화면에 모으고 자동화했습니다.

- **25개+ 온체인·파생·거시 지표를 매일 자동 수집·분석**하는 무료 대시보드 → 실제 도메인(`btctiming.co.kr`)으로 운영
- Python 스냅샷 파이프라인으로 데이터 수집 → 정적 사이트 배포 (실시간 부하 없이 안정적 서빙)
- 한국어 / 영어 다국어(i18n), SEO 최적화, Firebase 연동
- 지표별 상세 해설 페이지 20종 + 매수 타이밍 스코어링

**Tech** · Python · Firebase · GitHub Pages · i18n

---

### 🏃 [Running Crew](https://github.com/qkrxodud/running) — 러닝크루 앱 `개발 중`

> **배경** — 러닝 크루가 함께 뛰고, 코스를 완주하고, 순위·기록을 겨루는 모바일 앱. 서버가 GPS 트랙을 검증하고 순위를 확정합니다.

- **6인 AI 에이전트 하네스(기획·도메인·백엔드·Flutter·테스트·QA)를 설계해 팀 개발 프로세스를 자동화** — 실행 회차마다 감사 추적 보존
- **헥사고날 아키텍처** 기반 Spring Boot 서버 (Java 25) + Flutter 클라이언트
- 트랙 정제·완주 판정·순위 산정을 **순수 함수 + 골든 테스트 175케이스**로 검증
- **회귀 레지스트리** 운영 — 모든 버그를 영구 장부에 기록하고 red→green 테스트로 재발 방지
- 업로드 멱등 파이프라인, `AFTER_COMMIT` 자동 확정, 마감 스케줄러

**Tech** · Spring Boot 3.5+ · Java 25 · Hexagonal · Flutter · JWT · Kakao API

---

### 🧑‍💼 [Interview Connect](https://github.com/qkrxodud/interview-connect) — 면접 경험 연결 플랫폼 `개발 중`

> **배경** — 잡플래닛이 '회사 정보'를 다룬다면, 이 서비스는 **면접 경험자와 구직자를 사람 단위로 연결**하는 것이 핵심 차별점입니다.

- **TDD 파이프라인(설계→테스트→구현→리뷰)을 에이전트 팀으로 자동화** — product-analyst가 비즈니스 룰을 먼저 검증
- 비로그인 후기 공개로 SEO 유입 확보 + Q&A 답변 블러로 회원 전환 유도 (제품 설계 관점 반영)
- 4단계·16주 로드맵을 주차별 실행 계획·기술 부채 트래커로 관리
- Spring Boot 백엔드 + Next.js 프론트엔드

**Tech** · Spring Boot · Next.js · TDD · Docker

---

## 🧭 나의 개발 성격

| 이런 개발자입니다 | 근거 |
| --- | --- |
| **끝까지 파고든다** | JVM 내부 동작, JMM·`synchronized`·가상 스레드, 트랜잭션·DB 성능을 원리부터 이해하고 [블로그](https://www.coby-blog.co.kr/)에 정리 |
| **품질을 시스템으로 만든다** | TDD·골든 테스트·회귀 레지스트리 등 "재발하지 않는 구조"를 설계 |
| **프로세스도 설계 대상이다** | AI 에이전트 하네스로 기획·구현·QA 파이프라인 자체를 엔지니어링 |
| **실제로 배포한다** | 데모에서 끝내지 않고 도메인 붙여 운영( `btctiming.co.kr` )하고, 가족·주변의 실제 문제를 서비스로 해결 |
| **읽는 사람을 배려한다** | 도메인 배경을 짧게 설명하고, 문서·코드 모두 가독성을 최우선 |

---

## 🛠 Tech Stack

**Backend**

![Java](https://img.shields.io/badge/Java-007396?style=flat-square&logo=openjdk&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white)
![Spring Data JPA](https://img.shields.io/badge/Spring_Data_JPA-6DB33F?style=flat-square&logo=spring&logoColor=white)
![MyBatis](https://img.shields.io/badge/MyBatis-DC382D?style=flat-square&logo=&logoColor=white)

**Database & Cache · Messaging**

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Apache_Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white)

**Infra & DevOps**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)

**Client & Etc**

![Flutter](https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=black)

---

## 💪 핵심 역량

| 분야 | 설명 |
| --- | --- |
| **성능 최적화** | 실행 계획(EXPLAIN) 분석, 인덱스 설계, 쿼리 튜닝을 통한 응답 속도 개선 |
| **분산 시스템** | Kafka 기반 이벤트 처리, Redis·Redisson 분산 락을 활용한 동시성 제어 |
| **동시성 & JVM** | JMM, `synchronized`, 가상 스레드 등 내부 동작 이해 기반의 설계 |
| **테스트 & 품질** | TDD·골든 테스트·회귀 레지스트리로 재발 없는 품질 체계 구축 |
| **AI 하네스 엔지니어링** | 멀티 에이전트로 기획→구현→QA 개발 파이프라인 자동화 |

---

## 📝 이전 프로젝트

<details>
<summary><b>펼쳐서 보기</b> — Trading Bot · User Refund Calculator · Pharmacy</summary>

<br>

**[Trading Bot](https://github.com/qkrxodud/trading_bot)** — 실시간 암호화폐 자동매매 시스템
5/20 이동평균 교차 전략, 업비트 API 연동, Spring WebFlux 비동기 처리, 클린 아키텍처, `BigDecimal` 금융 정확성, TDD.
`Spring Boot 3.5.6 · Java 21 · WebFlux · Telegram API`

**[User Refund Calculator](https://github.com/qkrxodud/UserRefundCalculator)** — 유저 환급금 조회 서비스
회원 인증 API, 외부 스크래핑 연동, 결정세액 조회, 도메인 중심 계층 분리.
`Spring Boot 3.3.0 · Java 17 · JPA · JUnit 5`

**[Pharmacy](https://github.com/qkrxodud/pharmacy)** — 위치 기반 약국 추천 서비스
Haversine 최단거리 추천, 카카오 지도 API, Redis 캐싱, 공공데이터 정제, Spock BDD 테스트, Docker.
`Spring Boot · JPA · Redis · Docker · Kakao API`

</details>

---

## ✍️ Recent Blog Posts

실무 경험과 학습을 [기술 블로그](https://www.coby-blog.co.kr/)에 꾸준히 정리합니다.

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

<div align="center">

**협업 제안이나 기술 이야기는 언제든 환영합니다.**

📧 qkrxodud00@gmail.com · 💼 [LinkedIn](https://url.kr/o8rerj) · 📝 [Tech Blog](https://www.coby-blog.co.kr/)

<br>

*"Clean code that works" — 동작하는 깨끗한 코드를 위해 노력합니다.*

</div>
