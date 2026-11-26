# -*- coding: utf-8 -*-
"""허브 페이지(진료 영역 3군 · 지점 · 소식 · 소개)와 지점 상세."""
import json, pathlib
from shell import (SITE, CATS, BRANCHES, B_BY_SLUG, esc, rel, page, branch_card,
                   cta, disclaimer, need, tel_link, ORIGIN, BRAND)
from pages_disease import DISEASES

ROOT = pathlib.Path(__file__).parent


def phead(num, en, h1, lede, depth, acts=None):
    r = rel(depth)
    acts = acts or [("예약하기", f"{r}booking/", "btn-cta"),
                    ("비용·상담 문의", f"{r}contact/", "btn-line")]
    a = "".join(f'<a class="btn {c}" href="{u}">{esc(t)}</a>' for t, u, c in acts)
    return f"""<section class="phead">
  <div class="wrap">
    <div class="seclabel"><span class="num">{esc(num)}</span><span class="en">{esc(en)}</span></div>
    <h1>{esc(h1)}</h1>
    <p class="plede">{esc(lede)}</p>
    <div class="pacts">{a}</div>
  </div>
</section>
"""


def lcards(items, depth):
    r = rel(depth)
    out = []
    for name, url, note in items:
        out.append(f"""      <a class="lcard" href="{r}{url.lstrip('/')}">
        <h3>{esc(name)}</h3>
        <p>{esc(note)}</p>
        <span class="go">자세히 보기 →</span>
      </a>""")
    return '    <div class="cardgrid rv">\n' + "\n".join(out) + "\n    </div>"


# ================================================================ 진료 영역 허브
CAT_HUB = {
    "respiratory": {
        "h1": "코와 귀는 이어져 있습니다",
        "lede": "비염·축농증·중이염은 서로 떨어진 질환이 아닙니다. 미소로는 호흡기 점막을 하나로 놓고 봅니다.",
        "intro": [
            "코로 들어온 자극은 코 점막에서 멈추지 않습니다. 부비동으로 번지면 축농증이 되고, 이관을 타고 올라가면 중이염이 됩니다. 하나를 가라앉혀도 나머지 조건이 남아 있으면 되풀이되는 이유입니다.",
            "미소로는 세 질환을 각각의 진료로 나누지 않고, 점막의 상태와 그 상태를 만드는 전신 조건을 함께 봅니다. 초진에서 어느 지점부터 정리할지를 먼저 정합니다.",
        ],
        "slugs": ["rhinitis", "sinusitis", "otitis"],
        "extra": [("치료 프로그램", "/respiratory/program/", "호흡기 진료에서 사용하는 처치와 한약 구성을 정리했습니다."),
                  ("치료 과정·기간·비용", "/respiratory/process/", "초진부터 생활 관리까지의 흐름과 비용 안내 방식입니다.")],
    },
    "skin": {
        "h1": "겉이 아니라, 반복되는 조건을 봅니다",
        "lede": "바르는 동안에만 가라앉는다면, 피부가 그렇게 반응하는 조건이 그대로 남아 있다는 뜻입니다.",
        "intro": [
            "피부 질환은 증상이 눈에 보이기 때문에 겉을 다루는 치료에 집중하기 쉽습니다. 그런데 같은 자극에도 어떤 날은 괜찮고 어떤 날은 올라온다면, 피부 바깥이 아니라 안쪽 조건이 달라진 것입니다.",
            "미소로는 병변에 대한 처치와 함께 수면·소화·체력·스트레스처럼 반응의 문턱을 좌우하는 조건을 같이 봅니다. 사용 중인 외용제가 있으면 임의로 끊지 마시고 알려 주세요.",
        ],
        "slugs": ["wart", "atopy", "eczema", "psoriasis", "pompholyx", "urticaria", "hyperhidrosis"],
        "extra": [("치료 과정·기간·비용", "/skin/process/", "초진부터 생활 관리까지의 흐름과 비용 안내 방식입니다.")],
    },
    "general": {
        "h1": "가까운 곳에서, 이어서 관리합니다",
        "lede": "통증과 체력, 교통사고 후의 몸 상태까지. 생활 반경 안에서 계속 볼 수 있는 진료입니다.",
        "intro": [
            "한의원을 찾는 이유가 늘 특정 질환만은 아닙니다. 오래 앉아 생긴 허리 통증, 환절기마다 떨어지는 체력, 사고 뒤에 남은 뻐근함처럼 생활에서 생긴 문제가 더 많습니다.",
            "이런 진료는 한 번에 끝나지 않고 이어서 봐야 합니다. 미소로가 지점 네트워크로 운영되는 이유 중 하나입니다.",
        ],
        "slugs": ["pain", "diet", "tonic", "accident"],
        "extra": [],
    },
}


def build_cat_hub(key):
    cat = CATS[key]
    c = CAT_HUB[key]
    depth = 1
    r = rel(depth)
    items = [(DISEASES[s]["name"], DISEASES[s]["path"], DISEASES[s]["lead"]) for s in c["slugs"]]
    extra = [(n, u, d) for n, u, d in c["extra"]]
    intro = "\n".join(f"      <p>{esc(p)}</p>" for p in c["intro"])

    body = phead("진료 영역", cat["en"], c["h1"], c["lede"], depth)
    body += f"""<section>
  <div class="wrap">
    <div class="prose rv" style="margin-bottom:var(--s-xxl)">
{intro}
    </div>
    <div class="sechead rv" style="margin-bottom:var(--s-xl)">
      <div class="seclabel"><span class="num">01</span><span class="en">Clinics</span></div>
      <h2 class="h1">{esc(cat['label'])} 진료</h2>
    </div>
{lcards(items, depth)}
  </div>
</section>
"""
    if extra:
        body += f"""<section class="alt">
  <div class="wrap">
    <div class="sechead rv" style="margin-bottom:var(--s-xl)">
      <div class="seclabel"><span class="num">02</span><span class="en">More</span></div>
      <h2 class="h1">함께 보기</h2>
    </div>
{lcards(extra, depth)}
  </div>
</section>
"""
    from shell import branch_section
    body += branch_section(depth, num="03")
    body += cta(depth) + disclaimer(depth)

    return page(title=f"{cat['label']} 한방치료", desc=c["lede"], path=cat["url"],
                depth=depth, body=body, active=cat["url"],
                crumb=[(cat["label"], None)])


# ================================================================ 지점 상세
def branch_ld(b):
    d = {
        "@context": "https://schema.org",
        "@type": "MedicalClinic",
        "name": f"{BRAND['name']} {b['name']}",
        "url": f"{ORIGIN}/branch/{b['slug']}/",
    }
    if b["tel"]:
        d["telephone"] = b["tel"]
    if b["address"]:
        d["address"] = {"@type": "PostalAddress", "streetAddress": b["address"], "addressCountry": "KR"}
    return d


def build_branch(b):
    r = rel(2)
    if b["slug"] == "bundang":
        doc_block = f"""<div class="docgrid rv">
      <figure class="docphoto">
        <img src="{r}assets/img/doctor-portrait.webp"
             srcset="{r}assets/img/doctor-portrait-360.webp 360w, {r}assets/img/doctor-portrait.webp 720w"
             sizes="(min-width:768px) 260px, 100vw" width="720" height="720" loading="lazy" decoding="async"
             alt="미소로한의원 분당점 대표원장 프로필 사진">
        <figcaption>분당점 대표원장</figcaption>
      </figure>
      <div class="prose">
        <h3 style="margin-top:0">초진부터 마무리까지 한 원장이 맡습니다</h3>
        <p>방문하실 때마다 경과를 처음부터 설명하지 않으셔도 되고, 치료 방향이 중간에 바뀌지 않습니다.</p>
        <p>성명과 약력은 {need("확인 후 게재")}. 의료법 제56조 제2항 9호에 따라 법적 근거가 있는 자격·면허만 표기하며, 성명·면허 종류·검증 가능한 약력만 받아 게재합니다.</p>
      </div>
    </div>"""
    else:
        doc_block = f"""<div class="callout rv">
      <h3>원장 정보 {need()}</h3>
      <p>의료법 제56조 제2항 9호에 따라 법적 근거가 있는 자격·면허만 표기할 수 있습니다. 성명, 면허 종류, 검증 가능한 약력만 받아 게재합니다. 사진은 서면 동의 후 사용합니다.</p>
    </div>"""
    depth = 2
    r = rel(depth)

    # 진료시간표
    if b["hours"]:
        rows = "\n".join(
            f'<tr><th scope="row">{esc(h["day"])}</th>'
            f'<td class="num">{esc(h["open"])}{" – " + esc(h["close"]) if h["close"] else ""}</td>'
            f'<td>{esc(h["note"])}</td></tr>'
            for h in b["hours"]
        )
        hours_html = f"""<div class="tbl-wrap"><table class="tbl">
  <caption>진료시간은 변경될 수 있습니다. 방문 전 전화로 확인해 주세요.</caption>
  <thead><tr><th scope="col">요일</th><th scope="col">진료시간</th><th scope="col">비고</th></tr></thead>
  <tbody>{rows}</tbody>
</table></div>"""
    else:
        hours_html = f"""<div class="callout">
  <h3>진료시간 {need()}</h3>
  <p>이 지점의 진료시간은 아직 확정되지 않았습니다. 전화로 문의해 주세요.</p>
</div>"""

    addr_block = []
    if b["address"]:
        addr_block.append(f'<p><strong>도로명</strong> {esc(b["address"])}</p>')
    else:
        addr_block.append(f"<p><strong>도로명</strong> {need('주소 확인 필요')}</p>")
    if b["addressJibun"]:
        addr_block.append(f'<p><strong>지번</strong> {esc(b["addressJibun"])}</p>')
    if b["station"]:
        addr_block.append(f'<p><strong>지하철</strong> {esc(b["station"])} {esc(b["walk"] or "")}</p>')
    if b["parking"]:
        addr_block.append(f'<p><strong>주차</strong> {esc(b["parking"])}</p>')
    if b["tel"]:
        addr_block.append(f'<p><strong>전화</strong> <a href="{tel_link(b["tel"])}">{esc(b["tel"])}</a></p>')
    else:
        addr_block.append(f"<p><strong>전화</strong> {need('전화번호 확인 필요')}</p>")

    others = "\n".join(
        branch_card(x, depth) for x in BRANCHES if x["slug"] != b["slug"]
    )

    lede = (f'{esc(b["station"])} {esc(b["walk"] or "")}. ' if b["station"] else "") + \
        "초진부터 마무리까지 한 원장이 맡습니다."

    body = f"""<section class="phead">
  <div class="wrap">
    <div class="seclabel"><span class="num">지점안내</span><span class="en">{esc(b['slug'].upper())}</span></div>
    <h1>{esc(BRAND['name'])} {esc(b['name'])}</h1>
    <p class="plede">{lede}</p>
    <div class="pacts">
      {'<a class="btn btn-cta" href="%s">전화걸기 %s</a>' % (tel_link(b['tel']), esc(b['tel'])) if b['tel'] else ''}
      <a class="btn btn-line" href="{r}booking/?branch={b['slug']}">예약 신청</a>
    </div>
  </div>
</section>

<section id="visit">
  <div class="wrap split">
    <div>
      <div class="sechead" style="margin-bottom:var(--s-xl)">
        <div class="seclabel"><span class="num">01</span><span class="en">Hours</span></div>
        <h2 class="h1">진료시간</h2>
      </div>
      {hours_html}

      <div class="sechead" style="margin-top:var(--s-section);margin-bottom:var(--s-xl)">
        <div class="seclabel"><span class="num">02</span><span class="en">Directions</span></div>
        <h2 class="h1">오시는 길</h2>
      </div>
      <div class="mapbox" style="margin-bottom:var(--s-lg)">
        <span class="ph-t">지도 임베드 자리</span>
        <span class="ph-d">네이버/카카오 지도 iframe · 길찾기 링크<br>좌표 확정 후 삽입</span>
      </div>
      <div class="prose">{''.join(addr_block)}</div>
    </div>

    <aside class="side">
      <div class="sbox">
        <h3>{esc(b['name'])} 예약</h3>
        <p>예약은 신청제로 운영됩니다. 신청해 주시면 지점에서 확정 연락을 드립니다.</p>
        <a class="btn btn-cta" href="{r}booking/?branch={b['slug']}">예약 신청하기</a>
      </div>
      <div class="sbox">
        <h3>진료 영역</h3>
        <p>호흡기질환 · 피부질환 · 일반한의학</p>
        <a class="btn btn-line" href="{r}respiratory/">호흡기질환 보기</a>
      </div>
    </aside>
  </div>
</section>

<section id="doctor" class="alt">
  <div class="wrap">
    <div class="sechead rv" style="margin-bottom:var(--s-xl)">
      <div class="seclabel"><span class="num">03</span><span class="en">Doctor</span></div>
      <h2 class="h1">{esc(b['name'])} 원장</h2>
    </div>
    {doc_block}
  </div>
</section>

<section id="notice">
  <div class="wrap">
    <div class="sechead rv" style="margin-bottom:var(--s-xl)">
      <div class="seclabel"><span class="num">04</span><span class="en">Notice</span></div>
      <div class="finder-head">
        <h2 class="h1">{esc(b['name'])} 공지</h2>
        <a class="btn-ghost" href="{r}news/notice/">전체 공지 <span class="arw">→</span></a>
      </div>
    </div>
    <div class="callout rv">
      <h3>등록된 공지가 없습니다</h3>
      <p>휴진·진료시간 변경 등 지점 공지는 관리자에서 지점 계정으로 등록합니다. (3차 작업)</p>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sechead rv" style="margin-bottom:var(--s-xl)">
      <div class="seclabel"><span class="num">05</span><span class="en">Network</span></div>
      <h2 class="h1">다른 지점</h2>
    </div>
    <div class="brails">
{others}
    </div>
  </div>
</section>
"""
    body += cta(depth) + disclaimer(depth)

    return page(
        title=f"{BRAND['name']} {b['name']}",
        desc=f"{b['name']} 진료시간·오시는 길·예약 안내. " + (b["address"] or ""),
        path=f"/branch/{b['slug']}/",
        depth=depth, body=body, active="/branch/",
        ld=[branch_ld(b)],
        crumb=[("지점안내", "/branch/"), (b["name"], None)],
    )


# ================================================================ 지점 허브
def build_branch_hub():
    depth = 1
    cards = "\n".join(branch_card(b, depth) for b in BRANCHES)
    rows = "\n".join(
        f'<tr><th scope="row"><a href="{rel(depth)}branch/{b["slug"]}/">{esc(b["name"])}</a></th>'
        f'<td>{esc(b["address"]) if b["address"] else need("확인 필요")}</td>'
        f'<td class="num">{esc(b["tel"]) if b["tel"] else need("확인 필요")}</td>'
        f'<td>{"야간진료" if b["night"] else "—"}</td></tr>'
        for b in BRANCHES
    )
    body = phead("지점안내", "Network", "전국 9개 지점",
                 "가까운 지점에서 같은 기준으로 진료받으실 수 있습니다. 이사를 가셔도 진료를 이어가실 수 있습니다.", depth)
    body += f"""<section>
  <div class="wrap">
    <div class="mapbox rv" style="margin-bottom:var(--s-xxl)">
      <span class="ph-t">전국 지점 지도</span>
      <span class="ph-d">9개 지점 핀 · 클릭 시 지점 카드 확장<br>좌표 확정 후 삽입</span>
    </div>
    <div class="brails">
{cards}
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sechead rv" style="margin-bottom:var(--s-xl)">
      <div class="seclabel"><span class="num">02</span><span class="en">All branches</span></div>
      <h2 class="h1">한눈에 보기</h2>
    </div>
    <div class="tbl-wrap rv"><table class="tbl">
      <caption>진료시간과 주소는 변경될 수 있습니다. 방문 전 전화로 확인해 주세요.</caption>
      <thead><tr><th scope="col">지점</th><th scope="col">주소</th><th scope="col">전화</th><th scope="col">야간진료</th></tr></thead>
      <tbody>{rows}</tbody>
    </table></div>
  </div>
</section>
"""
    body += cta(depth) + disclaimer(depth)
    return page(title="지점안내", desc="미소로한의원 전국 9개 지점의 주소·전화·진료시간 안내입니다.",
                path="/branch/", depth=depth, body=body, active="/branch/",
                crumb=[("지점안내", None)])
