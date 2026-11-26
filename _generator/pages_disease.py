# -*- coding: utf-8 -*-
"""질환 상세 페이지 — 7섹션 고정 템플릿 (14개 전부 동일 구조)."""
import json, pathlib
from shell import (SITE, CATS, BRANCHES, esc, rel, page, branch_card,
                   cta, disclaimer, need)

ROOT = pathlib.Path(__file__).parent
DISEASES = {}
for f in ("diseases_respiratory.json", "diseases_skin.json", "diseases_general.json"):
    DISEASES.update(json.loads((ROOT / "data" / f).read_text(encoding="utf-8")))

CHECK_ICON = ('<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" '
              'aria-hidden="true"><path d="M4 10.5l4 4 8-9" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def faq_ld(d):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q["q"],
             "acceptedAnswer": {"@type": "Answer", "text": q["a"]}}
            for q in d["faq"]
        ],
    }


def build(slug, d):
    depth = d["path"].strip("/").count("/") + 1
    r = rel(depth)
    cat = CATS[d["cat"]]

    # ---- 브레드크럼
    crumb = [(cat["label"], cat["url"])]
    if d.get("parent"):
        crumb.append((d["parent"]["name"], d["parent"]["path"]))
    crumb.append((d["name"], None))

    # ---- 01 히어로
    hero = f"""<section class="phead">
  <div class="wrap">
    <div class="seclabel"><span class="num">{esc(cat['label'])}</span><span class="en">{esc(cat['en'])}</span></div>
    <h1>{esc(d['lead'])}</h1>
    <p class="plede">{esc(d['sub'])}</p>
    <div class="pacts">
      <a class="btn btn-cta" href="{r}booking/">예약하기</a>
      <a class="btn btn-line" href="#branches">가까운 지점 보기</a>
    </div>
  </div>
</section>
"""

    # ---- 02 증상 체크 + 목차(사이드)
    checks = "\n".join(
        f'      <li>{CHECK_ICON}<span>{esc(c)}</span></li>' for c in d["checks"]
    )
    toc_items = [
        ("왜 되풀이되는가", "#why"),
        ("미소로의 치료 접근", "#approach"),
        ("과정·기간·비용", "#process"),
        ("자주 묻는 질문", "#faq"),
        ("가까운 지점", "#branches"),
    ]
    toc = "\n".join(f'<li><a href="{u}">{esc(t)}</a></li>' for t, u in toc_items)

    kids = ""
    if d.get("children"):
        items = "\n".join(
            f'<li><a href="{r}{DISEASES[c]["path"].lstrip("/")}">{esc(DISEASES[c]["name"])}</a></li>'
            for c in d["children"]
        )
        kids = f"""      <div class="sbox">
        <h3>세부 유형</h3>
        <ul class="toc" style="background:none;border:0;padding:0">{items}</ul>
      </div>"""

    sec_check = f"""<section id="check">
  <div class="wrap split">
    <div>
      <div class="sechead" style="margin-bottom:var(--s-xl)">
        <div class="seclabel"><span class="num">01</span><span class="en">Symptoms</span></div>
        <h2 class="h1">혹시 이런 상황이신가요?</h2>
      </div>
      <ul class="checks">
{checks}
      </ul>
      <p class="small" style="margin-top:var(--s-md)">해당하는 항목이 있다면 진료 때 말씀해 주세요. 이 목록은 자가 진단이 아니며, 점수나 결과를 알려드리지 않습니다.</p>
    </div>
    <aside class="side">
      <div class="toc">
        <h3>이 페이지에서</h3>
        <ul>{toc}</ul>
      </div>
{kids}
      <div class="sbox">
        <h3>{esc(d['name'])} 상담</h3>
        <p>증상과 그동안 받으신 치료를 알려 주시면, 가까운 지점에서 상담해 드립니다.</p>
        <a class="btn btn-cta" href="{r}booking/">예약하기</a>
      </div>
    </aside>
  </div>
</section>
"""

    # ---- 03 왜 되풀이되는가
    why_p = "\n".join(f"      <p>{esc(p)}</p>" for p in d["why"])
    sec_why = f"""<section id="why" class="alt">
  <div class="wrap">
    <div class="sechead rv" style="margin-bottom:var(--s-xl)">
      <div class="seclabel"><span class="num">02</span><span class="en">Why</span></div>
      <h2 class="h1">왜 되풀이되는가</h2>
    </div>
    <div class="prose rv">
{why_p}
    </div>
  </div>
</section>
"""

    # ---- 04 치료 접근
    steps = "\n".join(
        f"""      <li>
        <h3>{esc(s['h'])}</h3>
        <p>{esc(s['p'])}</p>
      </li>""" for s in d["approach"]
    )
    # 호흡기 계열에는 실제 진료 사진을 넣습니다
    care_photo = ""
    if d["cat"] == "respiratory":
        care_photo = f"""    <figure class="figure rv" style="max-width:720px;margin-bottom:var(--s-xl)">
      <img src="{r}assets/img/respiratory-care.webp"
           srcset="{r}assets/img/respiratory-care-660.webp 660w, {r}assets/img/respiratory-care.webp 1320w"
           sizes="(min-width:768px) 720px, 100vw" width="1320" height="880" loading="lazy" decoding="async"
           alt="원장이 비경으로 코 점막 상태를 확인하는 진료 장면">
      <figcaption>초진에서 코 점막의 부종과 분비 상태를 직접 확인합니다.</figcaption>
    </figure>
"""

    sec_app = f"""<section id="approach">
  <div class="wrap">
    <div class="sechead rv" style="margin-bottom:var(--s-xl)">
      <div class="seclabel"><span class="num">03</span><span class="en">Approach</span></div>
      <h2 class="h1">미소로는 이렇게 봅니다</h2>
    </div>
{care_photo}    <ol class="steps rv">
{steps}
    </ol>
  </div>
</section>
"""

    # ---- 05 과정·기간·비용
    proc_url = {"respiratory": "respiratory/process/", "skin": "skin/process/"}.get(d["cat"])
    proc_link = (f'<a class="btn btn-line" href="{r}{proc_url}">치료 과정 자세히 보기</a>'
                 if proc_url else "")
    sec_proc = f"""<section id="process" class="tile-dark">
  <div class="wrap">
    <div class="sechead rv" style="margin-bottom:var(--s-xl)">
      <div class="seclabel"><span class="num">04</span><span class="en">Process</span></div>
      <h2 class="h1">얼마나 걸리고 얼마나 드나요</h2>
    </div>
    <div class="prose rv" style="max-width:46em">
      <p style="color:var(--body-on-dark)">{esc(d['processNote'])}</p>
      <p style="color:var(--body-muted)">{esc(SITE['disclaimerShort'])}</p>
    </div>
    <div class="pacts rv">
      <a class="btn btn-cta" href="{r}pricing/">비급여 진료비 안내</a>
      {proc_link}
    </div>
  </div>
</section>
"""

    # ---- 06 FAQ
    faqs = "\n".join(
        f"""    <details>
      <summary>{esc(q['q'])}<span class="ic" aria-hidden="true"></span></summary>
      <div class="ans"><p>{esc(q['a'])}</p></div>
    </details>""" for q in d["faq"]
    )
    sec_faq = f"""<section id="faq" class="alt">
  <div class="wrap">
    <div class="sechead rv" style="margin-bottom:var(--s-xl)">
      <div class="seclabel"><span class="num">05</span><span class="en">FAQ</span></div>
      <h2 class="h1">자주 묻는 질문</h2>
    </div>
    <div class="faq rv">
{faqs}
    </div>
  </div>
</section>
"""

    # ---- 07 지점 선택
    cards = "\n".join(branch_card(b, depth) for b in BRANCHES)
    rel_links = ""
    if d.get("related"):
        items = "\n".join(
            f'<a class="chip" data-cat="{DISEASES[s]["cat"]}" href="{r}{DISEASES[s]["path"].lstrip("/")}">'
            f'<span class="dot"></span>{esc(DISEASES[s]["name"])}</a>'
            for s in d["related"] if s in DISEASES
        )
        rel_links = f"""    <div style="margin-top:var(--s-xxl)">
      <h3 class="h2" style="margin-bottom:var(--s-md)">함께 보는 질환</h3>
      <div class="chips" style="grid-template-columns:repeat(auto-fit,minmax(180px,1fr))">{items}</div>
    </div>"""

    sec_branch = f"""<section id="branches">
  <div class="wrap">
    <div class="sechead rv" style="margin-bottom:var(--s-xl)">
      <div class="seclabel"><span class="num">06</span><span class="en">Network</span></div>
      <div class="finder-head">
        <div>
          <h2 class="h1">가까운 지점에서 상담받으세요</h2>
          <p class="lede" style="margin-top:8px">{esc(d['name'])} 진료는 전국 9개 지점에서 동일한 기준으로 진행합니다.</p>
        </div>
        <a class="btn btn-line" href="{r}branch/">전체 지점 보기</a>
      </div>
    </div>
    <div class="brails">
{cards}
    </div>
{rel_links}
  </div>
</section>
"""

    body = hero + sec_check + sec_why + sec_app + sec_proc + sec_faq + sec_branch \
        + cta(depth) + disclaimer(depth)

    return page(
        title=d["title"],
        desc=d["desc"],
        path=d["path"],
        depth=depth,
        body=body,
        active=cat["url"],
        ld=[faq_ld(d)],
        crumb=crumb,
    )
