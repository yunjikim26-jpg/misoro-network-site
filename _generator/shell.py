# -*- coding: utf-8 -*-
"""공용 셸: head / 헤더 / 푸터 / 모바일바 / 공통 블록."""
import json, pathlib, html

ROOT = pathlib.Path(__file__).parent
SITE = json.loads((ROOT / "data" / "site.json").read_text(encoding="utf-8"))
BRAND = SITE["brand"]
NAV = SITE["nav"]
BRANCHES = SITE["branches"]
CATS = SITE["categories"]
B_BY_SLUG = {b["slug"]: b for b in BRANCHES}

ORIGIN = BRAND["origin"]
DEMO = SITE.get("demo", {"enabled": False})


def esc(s):
    return html.escape(s or "", quote=True)


def rel(depth):
    """루트 기준 상대 경로 접두사. depth=0 → '', 1 → '../' ..."""
    return "../" * depth


def tel_link(t):
    return "tel:" + t.replace(" ", "") if t else None


def need(text="확인 필요"):
    return f'<span class="devnote">{esc(text)}</span>'


# ---------------------------------------------------------------- head
def head(*, title, desc, path, depth, extra_ld=None, og_type="website"):
    r = rel(depth)
    full_title = title if BRAND["name"] in title else f"{title} – {BRAND['name']}"
    canonical = ORIGIN + path
    ld = extra_ld or []
    robots_meta = ('<meta name="robots" content="noindex, nofollow, noarchive, nosnippet">\n'
                   '<meta name="googlebot" content="noindex, nofollow">\n') if DEMO.get("enabled") else ""
    ld_html = "\n".join(
        f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld
    )
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{robots_meta}<title>{esc(full_title)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{esc(canonical)}">
<meta property="og:locale" content="ko_KR">
<meta property="og:site_name" content="{esc(BRAND['name'])}">
<link rel="canonical" href="{esc(canonical)}">
<!-- DESIGN.md 준수: Apple 기기에서는 system-ui가 실제 SF Pro로 해석됩니다.
     그 외 플랫폼은 Inter(라틴) + Noto Sans KR(한글)로 대체합니다. -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Noto+Sans+KR:wght@300;400;600;700&display=swap">
<link rel="stylesheet" href="{r}assets/css/site.css">
{ld_html}
</head>
<body>
<a class="skip" href="#main">본문 바로가기</a>
"""


# ---------------------------------------------------------------- 헤더
def header(depth, active=None):
    r = rel(depth)
    gnb, mnav = [], []
    for item in NAV:
        cur = ' aria-current="page"' if active and item["url"].startswith(active) else ""
        href = r + item["url"].lstrip("/")
        gnb.append(f'<a href="{href}"{cur}>{esc(item["label"])}</a>')
        mnav.append(f'<li><a href="{href}"{cur}>{esc(item["label"])}</a></li>')

    bmenu, mbranch = [], []
    for b in BRANCHES:
        href = f'{r}branch/{b["slug"]}/'
        t = b["tel"] or "준비 중"
        bmenu.append(
            f'<a role="menuitem" href="{href}">{esc(b["name"])} <span class="tel">{esc(t)}</span></a>'
        )
        mbranch.append(f'<a href="{href}">{esc(b["name"])}</a>')

    demobar = ""
    if DEMO.get("enabled") and DEMO.get("banner", True):
        demobar = (f'<div class="demobar" role="note">'
                   f'<strong>{esc(DEMO["label"])}</strong> '
                   f'<span>{esc(DEMO["note"])}</span> '
                   f'<a href="{esc(DEMO["officialUrl"])}" rel="noopener nofollow">공식 홈페이지 바로가기</a>'
                   f'</div>\n')

    return f"""{demobar}<header class="hdr">
  <div class="hdr-in">
    <a class="logo" href="{r if r else "/"}" aria-label="{esc(BRAND['name'])} 홈">
      <img src="{r}assets/img/logo-wordmark.png" alt="{esc(BRAND['name'])}" width="213" height="36">
    </a>

    <nav class="gnb" aria-label="주요 메뉴">
      {''.join(gnb)}
    </nav>

    <div class="hdr-right">
      <div class="branchsel" id="branchsel" data-open="false">
        <button type="button" aria-expanded="false" aria-controls="branchmenu">
          지점 선택
          <svg class="caret" width="12" height="12" viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M3 4.5L6 7.5L9 4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
        <div class="branchmenu" id="branchmenu" role="menu">
          {''.join(bmenu)}
        </div>
      </div>

      <a class="btn btn-cta" href="{r}booking/">예약하기</a>

      <button class="burger" type="button" aria-expanded="false" aria-controls="mnav" aria-label="메뉴 열기">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>

  <nav class="mnav" id="mnav" data-open="false" aria-label="모바일 메뉴">
    <ul>
      {''.join(mnav)}
    </ul>
    <div class="mnav-sub">
      <a href="{r}booking/">예약하기</a>
      <a href="{r}contact/">비용·상담 문의</a>
      <a href="{r}pricing/">비급여 진료비 안내</a>
      <p style="margin:var(--s-lg) 0 6px;font-size:12px;font-weight:600;letter-spacing:-0.12px;color:var(--ink)">지점 바로가기</p>
      {''.join(mbranch)}
    </div>
  </nav>
</header>

<main id="main">
"""


# ---------------------------------------------------------------- 브레드크럼
def crumbs(depth, items):
    """items: [(label, url|None)] — 마지막은 url=None"""
    r = rel(depth)
    out = ['<li><a href="%s">홈</a></li>' % (r if r else "/")]
    for label, url in items:
        if url:
            out.append(f'<li><a href="{r}{url.lstrip("/")}">{esc(label)}</a></li>')
        else:
            out.append(f'<li><span aria-current="page">{esc(label)}</span></li>')
    return f'<nav class="crumb" aria-label="현재 위치"><div class="wrap"><ol>{"".join(out)}</ol></div></nav>'


# ---------------------------------------------------------------- 지점 카드
def branch_card(b, depth, reveal=True):
    r = rel(depth)
    rv = " rv" if reveal else ""
    badge = (
        '<span class="badge night">야간진료</span>'
        if b["night"]
        else f'<span class="badge">{esc(b["line"] or b["region"])}</span>'
    )
    addr = esc(b["address"]) if b["address"] else need("주소 확인 필요")
    meta = []
    if b["station"]:
        meta.append(f'<span>{esc(b["station"])} <b>{esc(b["walk"] or "")}</b></span>')
    if b["parking"]:
        meta.append(f'<span>{esc(b["parking"])}</span>')
    if not meta:
        meta.append(need("진료시간·교통 확인 필요"))
    if b["tel"]:
        left = f'<a class="tel" href="{tel_link(b["tel"])}">{esc(b["tel"])}</a>'
    else:
        left = f'<a class="tel" href="{r}branch/{b["slug"]}/">지점 정보</a>'
    return f"""      <article class="bcard{rv}">
        <div class="bcard-top"><h3><a href="{r}branch/{b['slug']}/">{esc(b['name'])}</a></h3>{badge}</div>
        <p class="addr">{addr}</p>
        <div class="meta">{''.join(meta)}</div>
        <div class="bcard-acts">{left}<a class="bk" href="{r}booking/?branch={b['slug']}">예약</a></div>
      </article>"""


def branch_section(depth, title="가까운 지점에서 상담받으세요", num="05", alt=False):
    r = rel(depth)
    cards = "\n".join(branch_card(b, depth) for b in BRANCHES)
    cls = ' class="alt"' if alt else ""
    return f"""<section{cls}>
  <div class="wrap">
    <div class="sechead rv" style="margin-bottom:var(--s-xl)">
      <div class="seclabel"><span class="num">{num}</span><span class="en">Network</span></div>
      <div class="finder-head">
        <div>
          <h2 class="h1">{esc(title)}</h2>
          <p class="lede" style="margin-top:8px">이사를 가셔도, 통원이 어려워지셔도 가까운 지점에서 진료를 이어가실 수 있습니다.</p>
        </div>
        <a class="btn btn-line" href="{r}branch/">전체 9개 지점 보기</a>
      </div>
    </div>
    <div class="brails">
{cards}
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------- CTA / 고지 / 푸터
def cta(depth, heading=None, sub=None):
    r = rel(depth)
    heading = heading or "증상을 설명해 주시면<br>가장 가까운 지점으로 안내해 드립니다"
    sub = sub or "예약은 신청제로 운영됩니다. 신청해 주시면 해당 지점에서 확정 연락을 드립니다."
    return f"""<section class="cta">
  <div class="wrap">
    <h2>{heading}</h2>
    <p>{esc(sub)}</p>
    <div class="cta-acts">
      <a class="btn btn-cta" href="{r}booking/">예약 신청하기</a>
      <a class="btn btn-line" href="{r}contact/">비용·상담 문의</a>
    </div>
  </div>
</section>
"""


def disclaimer(depth):
    r = rel(depth)
    return f"""<div class="disclaimer">
  <div class="wrap">
    <p>{esc(SITE['disclaimerLong'])} 비급여 진료비는 <a href="{r}pricing/">비급여 진료비 안내</a> 페이지에서 확인하실 수 있습니다.</p>
  </div>
</div>
"""


def footer(depth):
    r = rel(depth)
    lines = []
    for b in BRANCHES:
        a = esc(b["address"]) if b["address"] else "[주소 확인 필요]"
        t = esc(b["tel"]) if b["tel"] else "[전화번호 확인 필요]"
        lines.append(f"<p><b>{esc(b['name'])}</b> {a} · {t}</p>")
    return f"""</main>

<footer class="ftr">
  <div class="wrap">
    <div class="ftr-top">
      <div>
        <img class="ftr-logo" src="{r}assets/img/logo-stacked.png" alt="{esc(BRAND['name'])}" width="150" height="80">
        <p class="ftr-tag">{esc(BRAND['tagline'])}</p>
      </div>

      <div class="ftr-links">
        <div>
          <h4>진료</h4>
          <ul>
            <li><a href="{r}respiratory/">호흡기질환</a></li>
            <li><a href="{r}skin/">피부질환</a></li>
            <li><a href="{r}general/">일반한의학</a></li>
          </ul>
        </div>
        <div>
          <h4>미소로</h4>
          <ul>
            <li><a href="{r}about/">네트워크 소개</a></li>
            <li><a href="{r}about/doctors/">의료진</a></li>
            <li><a href="{r}branch/">지점안내</a></li>
          </ul>
        </div>
        <div>
          <h4>소식</h4>
          <ul>
            <li><a href="{r}news/notice/">공지사항</a></li>
            <li><a href="{r}news/column/">건강칼럼</a></li>
            <li><a href="{r}news/faq/">자주 묻는 질문</a></li>
          </ul>
        </div>
        <div>
          <h4>문의</h4>
          <ul>
            <li><a href="{r}booking/">예약하기</a></li>
            <li><a href="{r}contact/">비용·상담 문의</a></li>
            <li><a href="{r}pricing/">비급여 진료비 안내</a></li>
          </ul>
        </div>
      </div>
    </div>

    <div class="ftr-bot">
      <div class="ftr-branches">
        {''.join(lines)}
      </div>

      <div class="ftr-legal">
        <span>지점별 사업자등록번호·대표자명 [확인 필요]</span>
        <a href="{r}privacy/">개인정보처리방침</a>
        <a href="{r}terms/">이용약관</a>
        <a href="{r}sitemap/">사이트맵</a>
        <span>&copy; {esc(BRAND['name'])}</span>
      </div>
    </div>
  </div>
</footer>

<nav class="mbar" aria-label="빠른 연결">
  <a href="{r}branch/">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M5 4h3l2 5-2.5 1.5a11 11 0 0 0 5 5L14 13l5 2v3a2 2 0 0 1-2 2A15 15 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg>
    전화상담
  </a>
  <a href="{r}contact/">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><path d="M21 11.5a8.4 8.4 0 0 1-9 8.3L7 21l1.2-3A8.3 8.3 0 1 1 21 11.5z"/></svg>
    카카오톡
  </a>
  <a class="book" href="{r}booking/">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>
    예약하기
  </a>
</nav>

<script src="{r}assets/js/site.js"></script>
</body>
</html>
"""


def page(*, title, desc, path, depth, body, active=None, ld=None, crumb=None):
    out = [head(title=title, desc=desc, path=path, depth=depth, extra_ld=ld)]
    out.append(header(depth, active))
    if crumb:
        out.append(crumbs(depth, crumb))
    out.append(body)
    out.append(footer(depth))
    return "".join(out)
