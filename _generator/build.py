# -*- coding: utf-8 -*-
"""전체 사이트 빌드. 출력: ../site/"""
import pathlib, shutil, sys, datetime
sys.path.insert(0, str(pathlib.Path(__file__).parent))

from shell import SITE, BRANCHES, CATS, ORIGIN, rel, page, cta, disclaimer, esc, branch_section
import pages_disease as PD
import pages_hub as PH
import pages_static as PS
import pages_form as PF

SRC = pathlib.Path(__file__).parent
OUT = SRC.parent / "site"


def write(path, html):
    """path: '/about/' 또는 '/' → 디렉터리 + index.html"""
    p = OUT / path.strip("/")
    p.mkdir(parents=True, exist_ok=True)
    (p / "index.html").write_text(html, encoding="utf-8")
    return path


def build_home():
    """메인 페이지 — 1차에서 확정된 구조를 그대로 유지하되 공용 셸로 재구성."""
    d = 0
    r = ""
    chips = []
    order = ["rhinitis", "sinusitis", "otitis", "wart", "atopy", "eczema", "psoriasis",
             "pompholyx", "urticaria", "hyperhidrosis", "pain", "diet", "tonic", "accident"]
    for s in order:
        x = PD.DISEASES[s]
        chips.append(f'<a class="chip" data-cat="{x["cat"]}" href="{x["path"].lstrip("/")}">'
                     f'<span class="dot"></span>{esc(x["name"])}</a>')

    areas = []
    for key, slugs, note in [
        ("respiratory", ["rhinitis", "sinusitis", "otitis"],
         "코막힘과 재채기가 계절마다 되풀이될 때, 약을 끊으면 돌아오는 증상을 다시 봅니다."),
        ("skin", ["wart", "atopy", "eczema", "psoriasis", "pompholyx", "urticaria", "hyperhidrosis"],
         "겉으로 드러나는 증상만이 아니라, 그 증상이 반복되는 몸의 조건을 함께 봅니다."),
        ("general", ["pain", "diet", "tonic", "accident"],
         "통증과 체력, 교통사고 후의 몸 상태까지. 가까운 지점에서 이어서 관리하실 수 있습니다."),
    ]:
        cat = CATS[key]
        lis = "".join(f'<li>{esc(PD.DISEASES[s]["name"])}</li>' for s in slugs)
        areas.append(f"""      <article class="area rv" data-cat="{key}">
        <span class="bar"></span>
        <h3>{esc(cat['label'])}</h3>
        <p>{esc(note)}</p>
        <ul>{lis}</ul>
        <a class="btn-ghost" href="{cat['url'].lstrip('/')}">{esc(cat['label'])} 보기 <span class="arw">→</span></a>
      </article>""")

    cols = []
    for c in PS.COLUMNS[:4]:
        cols.append(f"""          <a class="col rv" href="news/column/">
            <div class="ph thumb">
              <svg class="ph-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><rect x="3" y="4" width="18" height="14" rx="2"/><path d="M3 15l4.5-4 3.5 3 3-2.5L21 16"/></svg>
              <span class="ph-t">썸네일 800 × 450</span>
            </div>
            <div class="col-body">
              <span class="tag" data-cat="{c['cat']}">{esc(c['tag'])}</span>
              <h3>{esc(c['t'])}</h3>
              <p class="by">{esc(c['by'])} · {esc(c['d'])}</p>
            </div>
          </a>""")

    notices = "".join(
        f'<li><a href="news/notice/"><h3>{esc(n["t"])}</h3><span class="d">{esc(n["d"])}</span></a></li>'
        for n in PS.NOTICES[:3]
    )

    body = f"""<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">전국 9개 지점 한의원 네트워크</span>
      <h1>한 사람의 원장이,<br><span class="thin">끝까지.</span></h1>
      <p class="hero-sub">호흡기와 피부를 면역이라는 한 기준으로 봅니다. 초진부터 마무리까지 한 원장이 맡기 때문에, 올 때마다 처음부터 설명하지 않으셔도 됩니다.</p>
      <div class="hero-acts">
        <a class="btn btn-cta" href="booking/">예약하기</a>
        <a class="btn btn-line" href="#finder">증상으로 찾아보기</a>
      </div>

      <dl class="hero-facts">
        <div><dt>진료 영역</dt><dd>호흡기 · 피부 · 일반한의학</dd></div>
        <div><dt>진료 방식</dt><dd>1:1 전담 진료</dd></div>
        <div><dt>지점</dt><dd>전국 9개</dd></div>
      </dl>
    </div>

    <figure class="hero-vis">
      <img src="assets/img/consultation.webp"
           srcset="assets/img/consultation-660.webp 660w, assets/img/consultation.webp 1320w"
           sizes="(min-width:1024px) 46vw, 100vw"
           width="1320" height="880"
           alt="진료실에서 원장이 환자와 마주 앉아 상담하는 모습" fetchpriority="high" decoding="async">
      <figcaption class="tagline">
        <strong>바른치료 다른치료</strong>
        <span>미소로한의원</span>
      </figcaption>
    </figure>
  </div>
</section>

<section class="finder" id="finder">
  <div class="wrap">
    <div class="sechead">
      <div class="seclabel"><span class="num">01</span><span class="en">Find by symptom</span></div>
      <div class="finder-head">
        <div>
          <h2 class="h1">어떤 증상으로 오셨나요?</h2>
          <p class="lede" style="margin-top:8px">증상을 고르시면 치료 과정과 기간, 가까운 지점까지 한 화면에서 확인하실 수 있습니다.</p>
        </div>
      </div>
    </div>

    <div class="filters" role="group" aria-label="진료 영역 필터">
      <button type="button" data-filter="all" aria-pressed="true">전체 14</button>
      <button type="button" data-filter="respiratory" aria-pressed="false">호흡기 3</button>
      <button type="button" data-filter="skin" aria-pressed="false">피부 7</button>
      <button type="button" data-filter="general" aria-pressed="false">일반한의학 4</button>
    </div>

    <div class="chips" id="chips">
      {''.join(chips)}
    </div>

    <div class="legend">
      <span><i style="background:var(--tag-respiratory)"></i>호흡기질환</span>
      <span><i style="background:var(--tag-skin)"></i>피부질환</span>
      <span><i style="background:var(--tag-general)"></i>일반한의학</span>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sechead rv" style="margin-bottom:var(--s-xl)">
      <div class="seclabel"><span class="num">02</span><span class="en">Clinics</span></div>
      <h2 class="h1">세 갈래의 진료</h2>
    </div>

    <div class="areas">
{''.join(areas)}
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sechead rv" style="margin-bottom:var(--s-xxl)">
      <div class="seclabel"><span class="num">03</span><span class="en">Principles</span></div>
      <h2 class="h1">미소로가 일하는 방식</h2>
    </div>

    <div class="principles">
      <article class="principle rv">
        <h3>한 원장이<br>끝까지 맡습니다</h3>
        <p>초진부터 마무리까지 같은 원장이 진료합니다. 방문할 때마다 경과를 처음부터 설명하실 필요가 없고, 치료 방향이 중간에 바뀌지 않습니다.</p>
      </article>
      <article class="principle rv">
        <h3>호흡기와 피부를<br>한 기준으로 봅니다</h3>
        <p>다른 곳에서는 각기 다른 진료실로 나뉘는 두 영역을, 미소로는 면역이라는 하나의 관점에서 함께 살핍니다.</p>
      </article>
      <article class="principle rv">
        <h3>진료실 밖의<br>생활까지 봅니다</h3>
        <p>치료만으로 끝내지 않고 식사·수면·환경까지 함께 점검합니다. 반복되는 조건을 그대로 두면 같은 자리로 돌아오기 때문입니다.</p>
      </article>
    </div>
  </div>
</section>

<section class="tile-dark">
  <div class="wrap">
    <div class="sechead rv" style="margin-bottom:var(--s-xxl)">
      <div class="seclabel"><span class="num">04</span><span class="en">Process</span></div>
      <h2 class="h1">처음 오시면 이렇게 진행됩니다</h2>
    </div>

    <div class="journey">
      <article class="step rv"><span class="ln"></span><div class="n">STEP 1</div><h3>초진 상담</h3><p>증상이 시작된 시점과 그동안 받으신 치료를 충분히 듣습니다.</p></article>
      <article class="step rv"><span class="ln"></span><div class="n">STEP 2</div><h3>검사·진단</h3><p>체질과 현재 상태를 확인해 원인을 어디에서 찾을지 정합니다.</p></article>
      <article class="step rv"><span class="ln"></span><div class="n">STEP 3</div><h3>치료 계획</h3><p>예상되는 과정과 기간, 비용을 먼저 안내해 드립니다.</p></article>
      <article class="step rv"><span class="ln"></span><div class="n">STEP 4</div><h3>치료</h3><p>같은 원장이 경과를 보며 계획을 조정해 나갑니다.</p></article>
      <article class="step rv"><span class="ln"></span><div class="n">STEP 5</div><h3>생활 관리</h3><p>치료가 끝난 뒤의 식사·환경 관리까지 함께 정리합니다.</p></article>
    </div>

    <p class="small" style="margin-top:var(--s-xl)">{esc(SITE['disclaimerShort'])}</p>
  </div>
</section>

{branch_section(0)}

<section class="alt">
  <div class="wrap">
    <div class="news-grid">
      <div>
        <div class="sechead rv" style="margin-bottom:var(--s-lg)">
          <div class="seclabel"><span class="num">06</span><span class="en">Column</span></div>
          <div class="finder-head">
            <h2 class="h1">건강칼럼</h2>
            <a class="btn-ghost" href="news/column/">전체 보기 <span class="arw">→</span></a>
          </div>
        </div>

        <div class="cols">
{''.join(cols)}
        </div>
        <p class="small" style="margin-top:var(--s-md)"><span class="devnote">샘플</span> 칼럼 4건은 레이아웃 확인용 더미입니다.</p>
      </div>

      <div>
        <div class="sechead rv" style="margin-bottom:var(--s-lg)">
          <div class="seclabel"><span class="num">07</span><span class="en">Notice</span></div>
          <div class="finder-head">
            <h2 class="h1">공지사항</h2>
            <a class="btn-ghost" href="news/notice/">전체 <span class="arw">→</span></a>
          </div>
        </div>

        <ul class="notices rv">{notices}</ul>
        <p class="small" style="margin-top:var(--s-md)"><span class="devnote">샘플</span> 공지 3건은 더미입니다.</p>
      </div>
    </div>
  </div>
</section>

{cta(0)}
{disclaimer(0)}
"""
    ld = {
        "@context": "https://schema.org", "@type": "MedicalOrganization",
        "name": SITE["brand"]["name"], "url": ORIGIN + "/",
        "department": [
            {k: v for k, v in {
                "@type": "MedicalClinic",
                "name": f"{SITE['brand']['name']} {b['name']}",
                "url": f"{ORIGIN}/branch/{b['slug']}/",
                "telephone": b["tel"],
                "address": ({"@type": "PostalAddress", "streetAddress": b["address"],
                             "addressCountry": "KR"} if b["address"] else None),
            }.items() if v} for b in BRANCHES
        ],
    }
    return page(title="미소로한의원 — 호흡기·피부 한방치료 네트워크",
                desc="비염·축농증·중이염 등 호흡기질환과 사마귀·아토피·건선 등 피부질환을 면역이라는 한 기준으로 봅니다. 1:1 전담 진료, 전국 9개 지점 미소로한의원.",
                path="/", depth=0, body=body, ld=[ld])


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copytree(SRC / "assets", OUT / "assets")

    built = []
    built.append(write("/", build_home()))

    # 소개
    built.append(write("/about/", PS.about_hub()))
    built.append(write("/about/story/", PS.about_story()))
    built.append(write("/about/principle/", PS.about_principle()))
    built.append(write("/about/principle/one-to-one/", PS.about_one_to_one()))
    built.append(write("/about/principle/immunity/", PS.about_immunity()))
    built.append(write("/about/doctors/", PS.about_doctors()))
    built.append(write("/about/facility/", PS.about_facility()))

    # 진료 영역 허브
    for key in ("respiratory", "skin", "general"):
        built.append(write(CATS[key]["url"], PH.build_cat_hub(key)))

    # 질환 상세 14 + 하위
    for slug, d in PD.DISEASES.items():
        built.append(write(d["path"], PD.build(slug, d)))

    built.append(write("/respiratory/program/", PS.respiratory_program()))
    built.append(write("/respiratory/process/", PS.process_page("respiratory")))
    built.append(write("/skin/process/", PS.process_page("skin")))

    # 지점
    built.append(write("/branch/", PH.build_branch_hub()))
    for b in BRANCHES:
        built.append(write(f"/branch/{b['slug']}/", PH.build_branch(b)))

    # 소식
    built.append(write("/news/", PS.news_hub()))
    built.append(write("/news/notice/", PS.news_notice()))
    built.append(write("/news/column/", PS.news_column()))
    built.append(write("/news/faq/", PS.news_faq()))

    # 폼·약관
    built.append(write("/booking/", PF.booking()))
    built.append(write("/contact/", PF.contact()))
    built.append(write("/pricing/", PF.pricing()))
    built.append(write("/privacy/", PF.privacy()))
    built.append(write("/terms/", PF.terms()))

    # 사이트맵 페이지
    tree = [
        ("네트워크 소개", [
            ("네트워크 소개", "/about/", []),
            ("미소로 이야기", "/about/story/", []),
            ("진료 원칙", "/about/principle/", [
                ("1:1 전담 진료", "/about/principle/one-to-one/"),
                ("면역 관점의 통합 진료", "/about/principle/immunity/")]),
            ("의료진", "/about/doctors/", []),
            ("진료 환경", "/about/facility/", []),
        ]),
        ("호흡기질환", [
            ("호흡기질환", "/respiratory/", []),
            ("비염", "/respiratory/rhinitis/", [
                ("알레르기성 비염", "/respiratory/rhinitis/allergic/"),
                ("만성 비염·비후성 비염", "/respiratory/rhinitis/chronic/"),
                ("소아 비염", "/respiratory/rhinitis/child/")]),
            ("축농증", "/respiratory/sinusitis/", []),
            ("중이염", "/respiratory/otitis/", []),
            ("치료 프로그램", "/respiratory/program/", []),
            ("치료 과정·기간·비용", "/respiratory/process/", []),
        ]),
        ("피부질환", [
            ("피부질환", "/skin/", []),
            ("사마귀", "/skin/wart/", []),
            ("아토피", "/skin/atopy/", []),
            ("습진", "/skin/eczema/", []),
            ("건선", "/skin/psoriasis/", []),
            ("한포진", "/skin/pompholyx/", []),
            ("두드러기", "/skin/urticaria/", []),
            ("다한증", "/skin/hyperhidrosis/", []),
            ("치료 과정·기간·비용", "/skin/process/", []),
        ]),
        ("일반한의학", [
            ("일반한의학", "/general/", []),
            ("통증·추나", "/general/pain/", []),
            ("다이어트", "/general/diet/", []),
            ("계절보약", "/general/tonic/", []),
            ("교통사고 후유증", "/general/accident/", [
                ("자동차보험 적용 안내", "/general/accident/insurance/")]),
        ]),
        ("지점안내", [("지점안내", "/branch/", [])] +
            [(b["name"], f"/branch/{b['slug']}/", []) for b in BRANCHES]),
        ("소식 · 안내", [
            ("소식", "/news/", []),
            ("공지사항", "/news/notice/", []),
            ("건강칼럼", "/news/column/", []),
            ("자주 묻는 질문", "/news/faq/", []),
            ("예약 신청", "/booking/", []),
            ("비용·상담 문의", "/contact/", []),
            ("비급여 진료비 안내", "/pricing/", []),
            ("개인정보처리방침", "/privacy/", []),
            ("이용약관", "/terms/", []),
        ]),
    ]
    built.append(write("/sitemap/", PF.sitemap_page(tree)))

    # sitemap.xml / robots.txt
    today = datetime.date.today().isoformat()
    urls = "\n".join(
        f"  <url><loc>{ORIGIN}{p}</loc><lastmod>{today}</lastmod></url>" for p in sorted(set(built))
    )
    (OUT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n',
        encoding="utf-8")
    from shell import DEMO
    if DEMO.get("enabled"):
        # 실습 사이트: 검색엔진·AI 크롤러 전면 차단.
        # 실제 misoro.kr 과 중복 콘텐츠로 경쟁하지 않도록 반드시 유지하세요.
        (OUT / "robots.txt").write_text(
            "# 마케팅 교육 실습용 사이트입니다. 색인을 허용하지 않습니다.\n"
            "User-agent: *\nDisallow: /\n", encoding="utf-8")
    else:
        (OUT / "robots.txt").write_text(
            f"User-agent: *\nAllow: /\n\nSitemap: {ORIGIN}/sitemap.xml\n", encoding="utf-8")
    # GitHub Pages: Jekyll 처리 비활성화
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    print(f"페이지 {len(built)}개 생성 → {OUT}")
    return built


if __name__ == "__main__":
    main()
