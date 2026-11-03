"""README에 들어가는 SVG를 생성한다. 색상은 tech-blog 다크 테마 CSS 변수와 같다.

    python3 scripts/build_svg.py
"""
import math
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"


def oklch(l, c, h):
    a, b = c * math.cos(math.radians(h)), c * math.sin(math.radians(h))
    l_, m_, s_ = (l + 0.3963377774 * a + 0.2158037573 * b) ** 3, \
                 (l - 0.1055613458 * a - 0.0638541728 * b) ** 3, \
                 (l - 0.0894841775 * a - 1.2914855480 * b) ** 3
    rgb = (4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_,
           -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_,
           -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_)

    def gamma(x):
        x = min(max(x, 0), 1)
        return 12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055

    return "#" + "".join(f"{round(gamma(x) * 255):02x}" for x in rgb)


BG = "#0f1412"
CARD = "#151b18"
GRID = "#161d1a"
LINE = "#2a322e"
INK = "#e6ebe8"
BODY = "#c3ccc7"
MUTED = "#98a29c"
FAINT = "#6f7a74"
STATUS_BG = "#080b0a"
ACCENT = oklch(0.72, 0.14, 155)
SHADOW = oklch(0.4, 0.09, 155)

MONO = "'JetBrains Mono','SFMono-Regular',Menlo,Consolas,monospace"
SANS = "'IBM Plex Sans KR','Apple SD Gothic Neo','Noto Sans KR','Malgun Gothic',sans-serif"
W = 840


def svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}">\n{body}\n</svg>\n')


def text(x, y, s, size=13, fill=BODY, font=SANS, weight=400, anchor="start"):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>')


def spans(x, y, parts, size=13, font=MONO):
    inner = "".join(f'<tspan fill="{c}">{escape(s)}</tspan>' for s, c in parts)
    return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" xml:space="preserve">{inner}</text>'


def grid(w, h):
    return (f'<defs><pattern id="g" width="24" height="24" patternUnits="userSpaceOnUse">'
            f'<path d="M24 0H0V24" fill="none" stroke="{GRID}" stroke-width="1"/></pattern></defs>'
            f'<rect width="{w}" height="{h}" fill="{BG}"/><rect width="{w}" height="{h}" fill="url(#g)"/>')


def header():
    h = 318
    b = [grid(W, h),
         f'<rect x="0.5" y="0.5" width="{W - 1}" height="{h - 1}" rx="10" fill="{BG}" stroke="{INK}" stroke-opacity=".55"/>',
         f'<path d="M1 38H{W - 1}" stroke="{INK}" stroke-opacity=".35"/>']
    for i, c in enumerate(["#ff5f57", "#febc2e", "#28c840"]):
        b.append(f'<circle cx="{20 + i * 19}" cy="19" r="6" fill="{c}"/>')
    b.append(text(W / 2, 24, "~/qkrxodud — zsh", 12, MUTED, MONO, anchor="middle"))
    b.append(spans(34, 76, [("➜ ", ACCENT), ("~/qkrxodud ", MUTED), ("git:(", FAINT), ("main", ACCENT), (")", FAINT)]))
    b.append(text(34, 114, "박태영 · 코징", 28, INK, SANS, 700))
    b.append(text(34, 144, "// Java, Spring, 데이터베이스를 파고드는 백엔드 개발자", 13, MUTED, MONO))
    b.append(f'<rect x="34.5" y="164.5" width="{W - 69}" height="38" rx="6" fill="none" '
             f'stroke="{LINE}" stroke-dasharray="4 4"/>')
    b.append(f'<circle cx="54" cy="184" r="4" fill="{ACCENT}"/>')
    b.append(spans(68, 188, [("블로그 글 ", MUTED), ("231", INK), ("편  ·  연재 ", MUTED), ("18", INK),
                             ("종  ·  ", MUTED), ("2022", INK), ("년부터 기록 중", MUTED)], 13, SANS))
    b.append(spans(34, 236, [("$ ", ACCENT), ("cat stack.txt", INK)]))
    rows = [("backend", "Java · Spring Boot · JPA · MyBatis · WebFlux"),
            ("data", "MySQL · Redis · Kafka · Elasticsearch"),
            ("infra", "Docker · Kubernetes · GitHub Actions")]
    for i, (k, v) in enumerate(rows):
        b.append(spans(34, 262 + i * 20, [(f"{k:<9}", FAINT), (v, BODY)], 12.5))
    return svg(W, h, "\n".join(b))


def prompt(cmd, comment):
    parts = [("$ ", ACCENT), (cmd, INK)]
    if comment:
        parts.append((f"  # {comment}", FAINT))
    return svg(W, 40, f'<rect width="{W}" height="40" rx="6" fill="{BG}"/>' + spans(16, 25, parts))


CW, CH = 268, 214


def card(name, sub, lines, tags, badge=None):
    b = [f'<rect x="5" y="5" width="{CW - 6}" height="{CH - 6}" rx="8" fill="{SHADOW}"/>',
         f'<rect x="1" y="1" width="{CW - 6}" height="{CH - 6}" rx="8" fill="{CARD}" stroke="{INK}" stroke-width="1.2"/>',
         spans(20, 38, [(name, INK), (" ↗", ACCENT)], 17, SANS).replace("<text ", '<text font-weight="700" ', 1),
         text(20, 62, escape(sub), 11.5, ACCENT, SANS, 600)]
    if badge:
        b.append(f'<rect x="{CW - 78}" y="22" width="58" height="20" rx="10" fill="none" stroke="{ACCENT}" stroke-opacity=".6"/>')
        b.append(text(CW - 49, 36, escape(badge), 11, ACCENT, SANS, 500, "middle"))
    for i, ln in enumerate(lines):
        b.append(text(20, 92 + i * 21, escape(ln), 12.5, BODY))
    x = 20
    for t in tags:
        tw = round(sum(11 if ord(ch) > 0x3000 else 7 for ch in t) + 16)
        b.append(f'<rect x="{x + 0.5}" y="{CH - 43.5}" width="{tw}" height="22" rx="11" fill="none" stroke="{LINE}" stroke-width="1.2"/>')
        b.append(text(x + tw / 2, CH - 29, escape(t), 11, MUTED, MONO, anchor="middle"))
        x += tw + 6
    return svg(CW, CH, "\n".join(b))


def posts(items):
    row = 66
    h = 52 + row * len(items) + 10
    b = [f'<rect x="0.5" y="0.5" width="{W - 1}" height="{h - 1}" rx="8" fill="{BG}" stroke="{LINE}"/>',
         spans(20, 32, [("$ ", ACCENT), ("ls -lt posts/ | head -5", INK), ("  # 최근 글", FAINT)])]
    for i, (_, date, cat, title) in enumerate(items):
        y = 52 + i * row
        b.append(spans(20, y + 20, [(cat, ACCENT), (f"  {date}", FAINT)], 12))
        b.append(text(20, y + 45, escape(title), 17, INK, SANS, 600))
        if i < len(items) - 1:
            b.append(f'<path d="M20 {y + row - 4}H{W - 20}" stroke="{LINE}" stroke-dasharray="3 4"/>')
    return svg(W, h, "\n".join(b))


def categories(groups):
    rows = max(len(items) for _, items in groups)
    h = 92 + rows * 26 + 14
    col = (W - 40) / len(groups)
    b = [f'<rect x="0.5" y="0.5" width="{W - 1}" height="{h - 1}" rx="8" fill="{BG}" stroke="{LINE}"/>',
         spans(20, 32, [("$ ", ACCENT), ("ls -l categories/", INK), ("  # 주제별 글 수", FAINT)])]
    for i, (title, items) in enumerate(groups):
        x = 20 + i * col
        b.append(text(x, 70, escape(title), 11.5, ACCENT, MONO, 600))
        for j, (name, n) in enumerate(items):
            y = 98 + j * 26
            b.append(text(x, y, escape(name), 13.5, BODY))
            b.append(text(x + col - 28, y, str(n), 13, FAINT, MONO, anchor="end"))
    return svg(W, h, "\n".join(b))


def status():
    h = 34
    b = [f'<rect width="{W}" height="{h}" rx="6" fill="{STATUS_BG}" stroke="{LINE}"/>',
         f'<circle cx="18" cy="17" r="4" fill="{ACCENT}"/>',
         spans(30, 21, [("main", INK), ("   231 posts", MUTED), ("   UTF-8", MUTED), ("   LF", MUTED)], 12),
         text(W - 16, 21, "© 2026 코징", 12, MUTED, MONO, anchor="end")]
    return svg(W, h, "\n".join(b))


CARDS = {
    "ttoryeot": ("또렷", "읽은 것이 사라지지 않는 브라우저",
                 ["다시 볼 페이지는 책갈피로,", "중요한 구절은 형광펜으로 남기는", "크롬 익스텐션. 가입 없이", "온디바이스로 동작합니다."],
                 ["Chrome Ext", "온디바이스"], None),
    "naeyong": ("내용", "문서 작성 마법사",
                ["내용증명, 차용증, 합의서 같은", "문서를 질문 몇 개에 답하면", "격식 갖춰 완성해 줍니다. 입력은", "브라우저 밖으로 나가지 않습니다."],
                ["문서 자동화", "클라이언트 처리"], None),
    "btc": ("BTC 레이더", "비트코인 투자 타이밍 지표",
            ["RSI, MVRV-Z, SOPR, 공포탐욕지수,", "펀딩비 등 시장 지표 25개 이상을", "매일 모아 한 화면에 보여 주는", "대시보드. Claude Code와 함께 설계."],
            ["Spring Boot", "헥사고날"], None),
    "running": ("running", "러닝 크루 앱",
                ["GPS 트랙을 서버에서 검증해", "완주 여부와 순위를 확정합니다.", "트랙 정제·순위 계산은 순수 함수,", "골든 테스트 175케이스."],
                ["Java 25", "Flutter"], "개발 중"),
    "interview": ("interview-connect", "면접 경험 연결 플랫폼",
                  ["면접을 먼저 본 사람과", "준비하는 사람을 이어 줍니다.", "설계→테스트→구현 순서의 TDD."],
                  ["Spring", "Next.js"], "개발 중"),
    "techblog": ("tech-blog", "코징의 개발탐방",
                 ["지금 이 블로그의 저장소입니다.", "Java, Spring, DB, 아키텍처 글", "231편과 연재 18종. 댓글은", "GitHub Discussions로 받습니다."],
                 ["GitHub Pages", "giscus"], "공개"),
}

CATEGORIES = [
    ("언어 & 백엔드", [("Spring", 48), ("Spring JPA", 36), ("Java · JVM", 27),
                    ("알고리즘", 11), ("객체지향 · 설계", 8), ("테스트", 3)]),
    ("데이터 & 인프라", [("Database", 15), ("Elasticsearch", 10), ("Kafka", 7),
                     ("AI 협업 개발", 6), ("네트워크 · HTTP", 5), ("인프라 · 컨테이너", 3)]),
    ("책 & 기록", [("클린 코드 with Java", 16), ("Clean Code", 11), ("도메인 주도 개발 시작하기", 10),
                 ("만들면서 배우는 클린 아키텍처", 8), ("회고", 6), ("Git · 협업", 1)]),
]

POSTS = [
    ("simpledateformat", "2026.10.23", "Java · JVM", "SimpleDateFormat 동시성 문제부터 불변 객체까지"),
    ("session-registry", "2026.10.17", "Spring", "Spring Session Redis에서 중복 로그인이 막히지 않는 원인"),
    ("datetime", "2026.10.09", "Database", "MySQL DATETIME과 TIMESTAMP"),
    ("deadlock", "2026.10.05", "Java · JVM", "데드락의 네 가지 조건과 해결 전략"),
    ("es-intro", "2026.08.30", "Elasticsearch", "ElasticSearch를 도입하게 된 이유"),
]

PROMPTS = {
    "projects": ("ls projects/", "직접 만들어 운영하고 있는 서비스"),
    "repos": ("ls repos/", "만들고 있는 것"),
}


def main():
    OUT.mkdir(exist_ok=True)
    files = {"header.svg": header(), "status.svg": status()}
    files |= {f"section-{k}.svg": prompt(*v) for k, v in PROMPTS.items()}
    files |= {f"card-{k}.svg": card(*v) for k, v in CARDS.items()}
    files["posts.svg"] = posts(POSTS)
    files["categories.svg"] = categories(CATEGORIES)
    for name, body in files.items():
        (OUT / name).write_text(body, encoding="utf-8")
    print(f"{len(files)} files -> {OUT}")


if __name__ == "__main__":
    main()
