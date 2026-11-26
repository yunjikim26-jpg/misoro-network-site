# -*- coding: utf-8 -*-
"""소개 · 소식 · 폼 · 약관 등 나머지 페이지."""
from shell import (SITE, CATS, BRANCHES, esc, rel, page, cta, disclaimer,
                   need, branch_section, BRAND)
from pages_hub import phead, lcards
from pages_disease import DISEASES

COLUMNS = [
    {"t": "환절기마다 비염이 되풀이될 때 먼저 확인할 것", "cat": "respiratory", "tag": "비염", "by": "분당점", "d": "2026.11.18"},
    {"t": "아이 아토피, 보습제만으로 부족하다고 느껴질 때", "cat": "skin", "tag": "아토피", "by": "수원점", "d": "2026.11.11"},
    {"t": "손에 물집이 반복될 때 생활에서 점검할 것들", "cat": "skin", "tag": "한포진", "by": "대전점", "d": "2026.11.04"},
    {"t": "교통사고 후 며칠 지나 통증이 올라오는 이유", "cat": "general", "tag": "교통사고", "by": "평택점", "d": "2026.10.28"},
    {"t": "축농증과 비염은 어떻게 다른가", "cat": "respiratory", "tag": "축농증", "by": "전주점", "d": "2026.10.21"},
    {"t": "건선 관리에서 겨울에 신경 쓸 것", "cat": "skin", "tag": "건선", "by": "안산점", "d": "2026.10.14"},
]

NOTICES = [
    {"t": "12월 진료시간 변경 안내 (대전점)", "d": "2026.11.20"},
    {"t": "홈페이지 개편 안내", "d": "2026.11.15"},
    {"t": "연말연시 휴진 일정 안내", "d": "2026.11.03"},
    {"t": "추석 연휴 진료 안내", "d": "2026.09.22"},
]

FAQS = [
    ("예약 없이 가도 되나요?", "지점에 따라 다릅니다. 예약제로 운영하는 지점이 있어, 방문 전 전화나 온라인으로 신청해 주시는 편이 대기 없이 진료받으실 수 있습니다."),
    ("예약은 바로 확정되나요?", "온라인 예약은 신청제입니다. 신청해 주시면 해당 지점에서 확인 후 확정 연락을 드립니다."),
    ("건강보험이 적용되나요?", "침·뜸 등 급여 항목은 적용되고, 한약을 비롯한 비급여 항목은 적용되지 않습니다. 비급여 진료비 안내 페이지에서 항목별 금액을 확인하실 수 있습니다."),
    ("다른 지점에서 받던 진료를 이어갈 수 있나요?", "가능합니다. 이전에 진료받으신 지점과 시기를 알려 주시면 그에 맞춰 진료합니다."),
    ("복용 중인 약이 있어도 되나요?", "반드시 알려 주세요. 상호작용을 확인한 뒤 처방 여부와 구성을 결정합니다. 기존 처방을 임의로 중단하지 마세요."),
    ("아이도 진료받을 수 있나요?", "연령과 체중에 맞춰 처방과 처치를 조정합니다. 아이의 나이와 증상을 알려 주시면 가능한 범위를 먼저 안내해 드립니다."),
    ("주차할 수 있나요?", "지점마다 다릅니다. 각 지점 페이지의 오시는 길에서 확인하실 수 있습니다."),
    ("교통사고 보험 처리가 되나요?", "자동차보험 적용이 가능합니다. 보험사 접수번호를 준비해 주세요. 자세한 절차는 자동차보험 적용 안내 페이지에 있습니다."),
]


# ================================================================ 소개
def about_hub():
    d = 1
    items = [
        ("미소로 이야기", "/about/story/", "어떻게 시작했고 무엇을 기준으로 삼는지."),
        ("진료 원칙", "/about/principle/", "1:1 전담 진료와 면역 관점의 통합 진료."),
        ("의료진", "/about/doctors/", "지점별 대표원장 안내."),
        ("진료 환경", "/about/facility/", "진료실과 대기 공간, 접근성."),
    ]
    body = phead("네트워크 소개", "About", "한 곳에서 보고, 한 원장이 끝까지 맡습니다",
                 "지점이 각자 움직이면 진료가 달라집니다. 미소로는 같은 기준을 공유하는 네트워크입니다.", d)
    body += f"""<section>
  <div class="wrap">
    <div class="prose rv" style="margin-bottom:var(--s-xxl)">
      <p>미소로한의원은 호흡기질환과 피부질환을 면역이라는 하나의 관점에서 보는 한의원 네트워크입니다. 전국 9개 지점이 같은 브랜드로 운영되며, 각 지점은 독립된 대표원장이 진료를 맡습니다.</p>
      <p>네트워크로 운영하는 이유는 두 가지입니다. 하나는 같은 진료 기준을 공유하기 위해서이고, 다른 하나는 환자가 생활 반경 안에서 진료를 이어갈 수 있게 하기 위해서입니다. 이사를 가거나 통원이 어려워져도 가까운 지점에서 계속 보실 수 있습니다.</p>
    </div>
    <div class="sechead rv" style="margin-bottom:var(--s-xl)">
      <div class="seclabel"><span class="num">01</span><span class="en">Sections</span></div>
      <h2 class="h1">더 알아보기</h2>
    </div>
{lcards(items, d)}
  </div>
</section>
"""
    body += branch_section(d, title="전국 9개 지점", num="02", alt=True)
    body += cta(d) + disclaimer(d)
    return page(title="네트워크 소개", desc="미소로한의원 네트워크 소개. 1:1 전담 진료와 면역 관점의 통합 진료.",
                path="/about/", depth=d, body=body, active="/about/",
                crumb=[("네트워크 소개", None)])


def about_story():
    d = 2
    body = phead("네트워크 소개", "Story", "되풀이되지 않게 하는 것",
                 "증상을 빨리 누르는 일은 어렵지 않습니다. 어려운 것은 같은 자리로 돌아오지 않게 하는 일입니다.", d)
    body += """<section>
  <div class="wrap split">
    <div class="prose rv">
      <p>한의원을 찾는 분들의 이야기에는 공통점이 있습니다. 약을 쓰는 동안에는 괜찮다가 끊으면 돌아온다는 것, 그리고 그 과정을 여러 해 반복해 왔다는 것입니다.</p>
      <h2>증상과 조건을 나눠 봅니다</h2>
      <p>코막힘이 있으면 코를 뚫고, 가려우면 가려움을 가라앉히는 것이 치료의 한 축입니다. 다만 그것만으로 끝내면, 같은 증상이 같은 조건에서 다시 올라옵니다. 미소로는 증상에 대한 처치와 함께 그 증상이 되풀이되는 조건을 함께 봅니다.</p>
      <p>조건은 사람마다 다릅니다. 수면이 부족한 경우, 소화가 약해 회복이 더딘 경우, 찬 기운에 유독 민감한 경우가 서로 다른 처방으로 이어집니다. 초진에서 이 구분을 먼저 하는 이유입니다.</p>
      <h2>한 원장이 끝까지 봅니다</h2>
      <p>조건을 보는 진료는 한 번에 끝나지 않습니다. 경과를 보며 조정해 나가야 하는데, 담당이 바뀌면 그 흐름이 끊깁니다. 미소로가 전 지점에서 1:1 전담 진료를 운영하는 것은 이 때문입니다.</p>
      <h2>호흡기와 피부를 함께 봅니다</h2>
      <p>많은 곳에서 코 질환과 피부 질환은 서로 다른 진료실로 나뉩니다. 한의학에서는 두 영역이 면역이라는 공통의 틀 안에서 설명됩니다. 미소로가 두 질환군을 한 고집에서 보는 이유입니다.</p>
      <p class="small">치료 경과는 개인의 체질·증상·경과에 따라 다를 수 있으며, 정확한 상태는 내원 진료 후 안내해 드립니다.</p>
    </div>
    <aside class="side">
      <div class="sbox">
        <h3>진료 원칙 보기</h3>
        <p>1:1 전담 진료와 면역 관점의 통합 진료를 더 자세히 정리했습니다.</p>
        <a class="btn btn-line" href="../principle/">진료 원칙</a>
      </div>
    </aside>
  </div>
</section>
"""
    body += cta(d) + disclaimer(d)
    return page(title="미소로 이야기", desc="미소로한의원이 증상과 조건을 함께 보는 이유.",
                path="/about/story/", depth=d, body=body, active="/about/",
                crumb=[("네트워크 소개", "/about/"), ("미소로 이야기", None)])


def about_principle():
    d = 2
    items = [
        ("1:1 전담 진료", "/about/principle/one-to-one/", "초진부터 마무리까지 한 원장이 맡는 구조."),
        ("면역 관점의 통합 진료", "/about/principle/immunity/", "호흡기와 피부를 한 기준으로 보는 관점."),
    ]
    body = phead("네트워크 소개", "Principles", "두 가지 원칙",
                 "미소로의 진료는 이 두 가지 위에서 설계됩니다.", d)
    body += f"""<section>
  <div class="wrap">
{lcards(items, d)}
  </div>
</section>
"""
    body += cta(d) + disclaimer(d)
    return page(title="진료 원칙", desc="미소로한의원의 두 가지 진료 원칙.",
                path="/about/principle/", depth=d, body=body, active="/about/",
                crumb=[("네트워크 소개", "/about/"), ("진료 원칙", None)])


def about_one_to_one():
    d = 3
    body = phead("진료 원칙", "One to one", "같은 원장이, 처음부터 끝까지",
                 "올 때마다 경과를 처음부터 설명하지 않으셔도 됩니다.", d)
    body += """<section>
  <div class="wrap">
    <div class="prose rv">
      <p>미소로는 전 지점에서 한 원장이 한 환자를 전담합니다. 초진에서 세운 치료 방향이 중간에 바뀌지 않고, 경과를 기록한 사람이 다음 진료도 맡습니다.</p>
      <h2>왜 전담인가</h2>
      <p>조건을 보는 진료는 변화를 읽는 일입니다. 지난번보다 나아졌는지, 어떤 상황에서 다시 올라왔는지를 비교해야 다음 처방을 조정할 수 있습니다. 담당이 바뀌면 이 비교가 기록에만 의존하게 되고, 기록에 남지 않는 미묘한 변화는 놓치게 됩니다.</p>
      <h2>환자 입장에서 달라지는 것</h2>
      <ul>
        <li>방문할 때마다 처음부터 설명하지 않아도 됩니다</li>
        <li>치료 방향이 중간에 바뀌지 않습니다</li>
        <li>경과에 대한 판단 기준이 일관됩니다</li>
        <li>질문할 상대가 분명합니다</li>
      </ul>
      <h2>지점을 옮길 때</h2>
      <p>이사나 전근으로 다른 지점으로 옮기셔야 할 때는, 이전 지점의 진료 내용을 공유받아 이어갑니다. 옮기실 계획이 있으면 미리 말씀해 주세요.</p>
    </div>
  </div>
</section>
"""
    body += cta(d) + disclaimer(d)
    return page(title="1:1 전담 진료", desc="초진부터 마무리까지 한 원장이 맡는 미소로한의원의 진료 구조.",
                path="/about/principle/one-to-one/", depth=d, body=body, active="/about/",
                crumb=[("네트워크 소개", "/about/"), ("진료 원칙", "/about/principle/"), ("1:1 전담 진료", None)])


def about_immunity():
    d = 3
    body = phead("진료 원칙", "Immunity", "호흡기와 피부를 한 기준으로",
                 "다른 곳에선 각기 다른 진료실로 가는 두 질환을, 미소로는 면역이라는 하나의 관점에서 봅니다.", d)
    body += """<section>
  <div class="wrap">
    <div class="prose rv">
      <p>비염과 아토피는 겉으로 보면 전혀 다른 질환입니다. 하나는 코에서, 다른 하나는 피부에서 나타납니다. 그런데 두 증상을 함께 가진 분이 적지 않고, 한쪽이 심해질 때 다른 쪽도 같이 심해지는 경우를 자주 봅니다.</p>
      <h2>공통의 틀</h2>
      <p>코 점막과 피부는 모두 바깥과 맞닿는 경계면입니다. 외부 자극을 가장 먼저 받고, 그 자극에 어떻게 반응할지를 결정하는 체계가 겹칩니다. 한의학에서 두 영역을 함께 설명해 온 이유입니다.</p>
      <p>미소로는 이 관점에서 두 질환군을 한 진료 안에 둡니다. 코 증상으로 오신 분에게 피부 상태를 묻고, 피부로 오신 분에게 호흡기 증상을 확인하는 것이 형식적인 절차가 아닌 이유입니다.</p>
      <h2>실제 진료에서</h2>
      <ul>
        <li>초진 문진에서 두 영역의 증상을 모두 확인합니다</li>
        <li>한쪽을 치료하는 동안 다른 쪽의 변화도 함께 기록합니다</li>
        <li>처방 구성에 두 영역의 상태를 함께 반영합니다</li>
      </ul>
      <p class="small">치료 경과는 개인의 체질·증상·경과에 따라 다를 수 있으며, 정확한 상태는 내원 진료 후 안내해 드립니다.</p>
    </div>
  </div>
</section>
"""
    body += cta(d) + disclaimer(d)
    return page(title="면역 관점의 통합 진료", desc="호흡기와 피부를 하나의 관점에서 보는 미소로한의원의 진료 기준.",
                path="/about/principle/immunity/", depth=d, body=body, active="/about/",
                crumb=[("네트워크 소개", "/about/"), ("진료 원칙", "/about/principle/"), ("면역 관점의 통합 진료", None)])


def about_doctors():
    d = 2
    r = rel(d)
    rows = "\n".join(
        f'<tr><th scope="row"><a href="{r}branch/{b["slug"]}/#doctor">{esc(b["name"])}</a></th>'
        f'<td>{need("원장 정보 확인 필요")}</td>'
        f'<td class="num">{esc(b["tel"]) if b["tel"] else need("확인 필요")}</td></tr>'
        for b in BRANCHES
    )
    body = phead("네트워크 소개", "Doctors", "지점별 대표원장",
                 "각 지점은 독립된 대표원장이 진료를 맡습니다.", d)
    body += f"""<section>
  <div class="wrap">
    <div class="callout rv" style="margin-bottom:var(--s-xxl)">
      <h3>표기 기준</h3>
      <p>의료법 제56조 제2항 9호에 따라 법적 근거가 있는 자격·명칭만 표기할 수 있습니다. 성명, 성별, 면허의 종류, 그리고 검증 가능한 약력만 게재하며, 사진은 서면 동의를 받은 경우에만 사용합니다.</p>
    </div>
    <div class="tbl-wrap rv"><table class="tbl">
      <thead><tr><th scope="col">지점</th><th scope="col">대표원장</th><th scope="col">전화</th></tr></thead>
      <tbody>{rows}</tbody>
    </table></div>
  </div>
</section>
"""
    body += cta(d) + disclaimer(d)
    return page(title="의료진", desc="미소로한의원 지점별 대표원장 안내.",
                path="/about/doctors/", depth=d, body=body, active="/about/",
                crumb=[("네트워크 소개", "/about/"), ("의료진", None)])


def about_facility():
    d = 2
    body = phead("네트워크 소개", "Facility", "진료 환경",
                 "지점마다 규모는 다르지만, 갖춰야 할 기준은 같습니다.", d)
    body += """<section>
  <div class="wrap">
    <div class="cardgrid rv">
      <div class="lcard"><h3>상담실</h3><p>초진 상담이 충분히 이뤄질 수 있는 독립 공간을 둡니다.</p></div>
      <div class="lcard"><h3>진료실</h3><p>처치와 진료가 분리된 구조로, 대기 시간을 줄입니다.</p></div>
      <div class="lcard"><h3>접근성</h3><p>지하철역 인근과 주차 가능 여부를 지점 페이지에 표기합니다.</p></div>
    </div>
    <div class="callout rv" style="margin-top:var(--s-xxl)">
      <h3>사진 자료 확인 필요</h3>
      <p>전 지점 동일 구도 3종(건물 외관·데스크·진료실) 촬영 후 교체합니다. 지점마다 구도가 다르면 네트워크로 읽히지 않습니다.</p>
    </div>
  </div>
</section>
"""
    body += cta(d) + disclaimer(d)
    return page(title="진료 환경", desc="미소로한의원의 진료 환경 안내.",
                path="/about/facility/", depth=d, body=body, active="/about/",
                crumb=[("네트워크 소개", "/about/"), ("진료 환경", None)])


# ================================================================ 치료 과정 공통
def process_page(cat_key):
    d = 2
    cat = CATS[cat_key]
    body = phead(cat["label"], "Process", "처음 오시면 이렇게 진행됩니다",
                 "초진부터 생활 관리까지의 흐름과, 비용을 안내하는 방식입니다.", d)
    body += f"""<section>
  <div class="wrap">
    <ol class="steps rv" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr))">
      <li><h3>초진 상담</h3><p>증상이 시작된 시점과 그동안 받으신 치료를 충분히 듣습니다.</p></li>
      <li><h3>검사·진단</h3><p>체질과 현재 상태를 확인해 원인을 어디에서 찾을지 정합니다.</p></li>
      <li><h3>치료 계획</h3><p>예상되는 과정과 기간, 비용을 먼저 안내해 드립니다.</p></li>
      <li><h3>치료</h3><p>같은 원장이 경과를 보며 계획을 조정해 나갑니다.</p></li>
      <li><h3>생활 관리</h3><p>치료가 끝난 뒤의 식사·환경 관리까지 함께 정리합니다.</p></li>
    </ol>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="sechead rv" style="margin-bottom:var(--s-xl)">
      <div class="seclabel"><span class="num">02</span><span class="en">Cost</span></div>
      <h2 class="h1">비용은 이렇게 안내합니다</h2>
    </div>
    <div class="prose rv">
      <p>치료 구성이 사람마다 다르기 때문에, 상태를 보지 않고 총액을 말씀드리기는 어렵습니다. 초진에서 상태를 확인한 뒤 예상되는 과정과 비용을 먼저 안내하고, 동의하신 범위에서 진행합니다.</p>
      <ul>
        <li>침·뜸 등 급여 항목은 건강보험이 적용됩니다</li>
        <li>한약을 비롯한 비급여 항목은 보험이 적용되지 않습니다</li>
        <li>비급여 항목별 금액은 비급여 진료비 안내 페이지에 고지되어 있습니다</li>
        <li>치료 중 구성이 바뀌면 변경 전에 다시 안내해 드립니다</li>
      </ul>
      <p class="small">{esc(SITE['disclaimerShort'])}</p>
    </div>
    <div class="pacts rv"><a class="btn btn-cta" href="../../pricing/">비급여 진료비 안내</a></div>
  </div>
</section>
"""
    body += cta(d) + disclaimer(d)
    return page(title=f"{cat['label']} 치료 과정·기간·비용",
                desc=f"미소로한의원 {cat['label']} 진료의 흐름과 비용 안내 방식입니다.",
                path=f"{cat['url']}process/", depth=d, body=body, active=cat["url"],
                crumb=[(cat["label"], cat["url"]), ("치료 과정·기간·비용", None)])


def respiratory_program():
    d = 2
    body = phead("호흡기질환", "Program", "호흡기 치료 프로그램",
                 "처치와 한약을 어떻게 구성하는지 정리했습니다.", d)
    body += """<section>
  <div class="wrap">
    <div class="prose rv">
      <p>호흡기 진료는 코 점막에 직접 작용하는 처치와, 전신 상태를 조정하는 한약을 함께 씁니다. 두 축의 비중은 증상의 정도와 경과 기간, 연령에 따라 달라집니다.</p>
      <h2>처치</h2>
      <p>코 점막의 부종과 분비 상태에 따라 처치 방법과 강도를 정합니다. 아이는 부담을 덜 느끼는 방식으로 조정합니다.</p>
      <h2>한약</h2>
      <p>찬 기운에 민감한 경우, 열감과 함께 코막힘이 심한 경우, 체력 저하와 함께 오래 끄는 경우에 각각 다른 처방을 씁니다. 복용 중인 약이 있으면 상호작용을 확인한 뒤 구성합니다.</p>
      <h2>생활 관리</h2>
      <p>실내 습도와 온도, 수면 시간, 자극 요인 회피 등 증상이 되풀이되는 조건을 함께 정리합니다. 치료만으로 끝내지 않는 이유입니다.</p>
    </div>
    <div class="callout rv" style="margin-top:var(--s-xxl)">
      <h3>프로그램 명칭 확인 필요</h3>
      <p>실제 운영 중인 치료 프로그램의 명칭과 구성을 받아 교체합니다. 명칭에 효과를 단정하는 표현이 들어가면 의료법 제56조 제2항 8호에 걸릴 수 있어 검토가 필요합니다.</p>
    </div>
  </div>
</section>
"""
    body += cta(d) + disclaimer(d)
    return page(title="호흡기 치료 프로그램", desc="미소로한의원 호흡기 진료의 처치와 한약 구성.",
                path="/respiratory/program/", depth=d, body=body, active="/respiratory/",
                crumb=[("호흡기질환", "/respiratory/"), ("치료 프로그램", None)])


# ================================================================ 소식
def news_hub():
    d = 1
    items = [
        ("공지사항", "/news/notice/", "진료시간 변경, 휴진 일정 등 안내."),
        ("건강칼럼", "/news/column/", "각 지점 원장이 쓰는 질환별 칼럼."),
        ("자주 묻는 질문", "/news/faq/", "예약·보험·진료에 대한 질문 모음."),
    ]
    body = phead("소식", "News", "미소로 소식", "공지와 칼럼, 자주 묻는 질문을 모았습니다.", d)
    body += f"""<section>
  <div class="wrap">
{lcards(items, d)}
  </div>
</section>
"""
    body += cta(d) + disclaimer(d)
    return page(title="소식", desc="미소로한의원 공지사항·건강칼럼·자주 묻는 질문.",
                path="/news/", depth=d, body=body, active="/news/",
                crumb=[("소식", None)])


def news_notice():
    d = 2
    rows = "\n".join(
        f'<li><a href="#"><h3>{esc(n["t"])}</h3><span class="d">{esc(n["d"])}</span></a></li>'
        for n in NOTICES
    )
    body = phead("소식", "Notice", "공지사항", "진료시간 변경과 휴진 일정을 안내해 드립니다.", d)
    body += f"""<section>
  <div class="wrap">
    <ul class="list rv">
{rows}
    </ul>
    <p class="small" style="margin-top:var(--s-md)"><span class="devnote">샘플</span> 공지 {len(NOTICES)}건은 레이아웃 확인용 더미입니다. 3차 작업에서 관리자와 연결합니다.</p>
  </div>
</section>
"""
    body += cta(d) + disclaimer(d)
    return page(title="공지사항", desc="미소로한의원 공지사항.",
                path="/news/notice/", depth=d, body=body, active="/news/",
                crumb=[("소식", "/news/"), ("공지사항", None)])


def news_column():
    d = 2
    cards = []
    for c in COLUMNS:
        cards.append(f"""      <a class="col" data-cat="{c['cat']}" href="#">
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
    body = phead("소식", "Column", "건강칼럼",
                 "각 지점 원장이 직접 쓰는 질환별 칼럼입니다.", d)
    body += f"""<section>
  <div class="wrap">
    <div class="filters" role="group" aria-label="진료 영역 필터">
      <button type="button" data-colfilter="all" aria-pressed="true">전체</button>
      <button type="button" data-colfilter="respiratory" aria-pressed="false">호흡기</button>
      <button type="button" data-colfilter="skin" aria-pressed="false">피부</button>
      <button type="button" data-colfilter="general" aria-pressed="false">일반한의학</button>
    </div>
    <div class="cols" id="collist" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr))">
{''.join(cards)}
    </div>
    <p class="small" style="margin-top:var(--s-md)"><span class="devnote">샘플</span> 칼럼 {len(COLUMNS)}건은 레이아웃 확인용 더미입니다. 3차 작업에서 관리자와 연결합니다.</p>
  </div>
</section>
"""
    body += cta(d) + disclaimer(d)
    return page(title="건강칼럼", desc="미소로한의원 각 지점 원장이 쓰는 건강칼럼.",
                path="/news/column/", depth=d, body=body, active="/news/",
                crumb=[("소식", "/news/"), ("건강칼럼", None)])


def news_faq():
    d = 2
    items = "\n".join(
        f"""    <details>
      <summary>{esc(q)}<span class="ic" aria-hidden="true"></span></summary>
      <div class="ans"><p>{esc(a)}</p></div>
    </details>""" for q, a in FAQS
    )
    ld = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS],
    }
    body = phead("소식", "FAQ", "자주 묻는 질문", "예약·보험·진료에 대해 많이 주시는 질문을 모았습니다.", d)
    body += f"""<section>
  <div class="wrap">
    <div class="faq rv">
{items}
    </div>
  </div>
</section>
"""
    body += cta(d) + disclaimer(d)
    return page(title="자주 묻는 질문", desc="미소로한의원 예약·보험·진료 관련 자주 묻는 질문.",
                path="/news/faq/", depth=d, body=body, active="/news/", ld=[ld],
                crumb=[("소식", "/news/"), ("자주 묻는 질문", None)])
