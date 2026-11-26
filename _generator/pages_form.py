# -*- coding: utf-8 -*-
"""예약 · 문의 · 비급여 · 약관 · 사이트맵."""
from shell import SITE, CATS, BRANCHES, esc, rel, page, cta, disclaimer, need, BRAND
from pages_hub import phead
from pages_disease import DISEASES

BRANCH_OPTS = "\n".join(
    f'            <option value="{b["slug"]}">{esc(b["name"])}</option>' for b in BRANCHES
)
DISEASE_OPTS = "\n".join(
    f'            <option value="{s}">{esc(d["name"])}</option>'
    for s, d in DISEASES.items() if not d.get("parent")
)


def booking():
    d = 1
    body = phead("예약", "Booking", "예약 신청",
                 "온라인 예약은 신청제입니다. 신청해 주시면 해당 지점에서 확인 후 확정 연락을 드립니다.", d,
                 acts=[("지점 전화번호 보기", rel(d)+"branch/", "btn-line")])
    body += f"""<section>
  <div class="wrap split">
    <div>
      <form class="form" id="bookingForm" method="post" action="#" novalidate>
        <div class="field">
          <label for="bk-branch">지점 <span class="req">필수</span></label>
          <select id="bk-branch" name="branch" required>
            <option value="">선택해 주세요</option>
{BRANCH_OPTS}
          </select>
        </div>

        <div class="field">
          <label for="bk-area">진료 영역 <span class="req">필수</span></label>
          <select id="bk-area" name="area" required>
            <option value="">선택해 주세요</option>
            <option value="respiratory">호흡기질환 (비염·축농증·중이염)</option>
            <option value="skin">피부질환 (사마귀·아토피·건선 등)</option>
            <option value="general">일반한의학 (통증·다이어트·보약·교통사고)</option>
          </select>
        </div>

        <div class="field">
          <label for="bk-date">희망 날짜 <span class="req">필수</span></label>
          <input type="date" id="bk-date" name="date" required>
          <span class="hint">지점 휴진일에는 예약이 어려울 수 있습니다.</span>
        </div>

        <div class="field">
          <label>희망 시간대 <span class="req">필수</span></label>
          <div class="radios">
            <label><input type="radio" name="slot" value="am" required> 오전</label>
            <label><input type="radio" name="slot" value="pm"> 오후</label>
            <label><input type="radio" name="slot" value="night"> 야간</label>
          </div>
        </div>

        <div class="field">
          <label for="bk-name">이름 <span class="req">필수</span></label>
          <input type="text" id="bk-name" name="name" autocomplete="name" required>
        </div>

        <div class="field">
          <label for="bk-tel">연락처 <span class="req">필수</span></label>
          <input type="tel" id="bk-tel" name="tel" inputmode="tel" autocomplete="tel"
                 placeholder="010-0000-0000" required>
          <span class="hint">확정 연락을 드릴 번호입니다.</span>
        </div>

        <div class="field">
          <label>방문 구분</label>
          <div class="radios">
            <label><input type="radio" name="visit" value="first" checked> 초진</label>
            <label><input type="radio" name="visit" value="again"> 재진</label>
          </div>
        </div>

        <div class="field">
          <label for="bk-memo">전달사항</label>
          <textarea id="bk-memo" name="memo" rows="5"
            placeholder="증상이 시작된 시점, 그동안 받으신 치료, 복용 중인 약이 있으면 적어 주세요."></textarea>
        </div>

        <div class="consent">
          <input type="checkbox" id="bk-agree" name="agree" required>
          <div>
            <label for="bk-agree" style="font-weight:600">개인정보 수집·이용에 동의합니다 <span class="req">필수</span></label>
            <p style="margin-top:4px">수집 항목: 이름, 연락처, 지점, 진료 영역, 전달사항. 목적: 예약 확인 및 안내. 보유 기간: 1년.
            자세한 내용은 <a href="../privacy/">개인정보처리방침</a>을 확인해 주세요. 동의를 거부하실 수 있으며, 이 경우 온라인 예약 신청이 제한됩니다.</p>
          </div>
        </div>

        <button type="submit" class="btn btn-cta">예약 신청하기</button>
        <p class="formnote" id="bk-note">전송 기능은 3차 작업에서 외부 폼 서비스와 연결합니다. 지금은 입력 검증만 동작합니다.</p>
      </form>
    </div>

    <aside class="side">
      <div class="sbox">
        <h3>바로 통화를 원하시면</h3>
        <p>각 지점 전화번호는 지점안내 페이지에 있습니다. 진료시간 중에는 전화가 더 빠릅니다.</p>
        <a class="btn btn-line" href="../branch/">지점 전화번호 보기</a>
      </div>
      <div class="sbox on-parchment">
        <h3>신청 후 절차</h3>
        <p>1. 신청 접수<br>2. 지점에서 확인<br>3. 확정 연락<br>4. 내원</p>
      </div>
      <div class="sbox">
        <h3>민감정보 안내</h3>
        <p>진료 영역과 전달사항에는 건강에 관한 정보가 포함될 수 있습니다. 전송 구간은 HTTPS로 보호하며, 보유 기간이 지나면 파기합니다.</p>
      </div>
    </aside>
  </div>
</section>
"""
    body += disclaimer(d)
    return page(title="예약 신청", desc="미소로한의원 온라인 예약 신청. 지점·진료 영역·희망 시간을 선택해 주세요.",
                path="/booking/", depth=d, body=body, crumb=[("예약 신청", None)])


def contact():
    d = 1
    body = phead("문의", "Contact", "비용·상담 문의",
                 "궁금한 점을 남겨 주시면 영업일 기준으로 연락드립니다.", d,
                 acts=[("바로 예약하기", rel(d)+"booking/", "btn-cta")])
    body += f"""<section>
  <div class="wrap split">
    <div>
      <form class="form" id="contactForm" method="post" action="#" novalidate>
        <div class="field">
          <label for="ct-name">이름 <span class="req">필수</span></label>
          <input type="text" id="ct-name" name="name" autocomplete="name" required>
        </div>
        <div class="field">
          <label for="ct-tel">연락처 <span class="req">필수</span></label>
          <input type="tel" id="ct-tel" name="tel" inputmode="tel" autocomplete="tel"
                 placeholder="010-0000-0000" required>
        </div>
        <div class="field">
          <label for="ct-branch">문의할 지점</label>
          <select id="ct-branch" name="branch">
            <option value="">선택 안 함</option>
{BRANCH_OPTS}
          </select>
        </div>
        <div class="field">
          <label for="ct-disease">관심 질환</label>
          <select id="ct-disease" name="disease">
            <option value="">선택 안 함</option>
{DISEASE_OPTS}
          </select>
        </div>
        <div class="field">
          <label for="ct-body">문의 내용 <span class="req">필수</span></label>
          <textarea id="ct-body" name="message" rows="7" required
            placeholder="증상과 경과, 그동안 받으신 치료를 적어 주시면 더 정확히 안내해 드릴 수 있습니다."></textarea>
        </div>
        <div class="consent">
          <input type="checkbox" id="ct-agree" name="agree" required>
          <div>
            <label for="ct-agree" style="font-weight:600">개인정보 수집·이용에 동의합니다 <span class="req">필수</span></label>
            <p style="margin-top:4px">수집 항목: 이름, 연락처, 지점, 관심 질환, 문의 내용. 목적: 문의 답변. 보유 기간: 1년.
            자세한 내용은 <a href="../privacy/">개인정보처리방침</a>을 확인해 주세요.</p>
          </div>
        </div>
        <button type="submit" class="btn btn-cta">문의 보내기</button>
        <p class="formnote" id="ct-note">전송 기능은 3차 작업에서 외부 폼 서비스와 연결합니다. 지금은 입력 검증만 동작합니다.</p>
      </form>
    </div>

    <aside class="side">
      <div class="sbox">
        <h3>자주 묻는 질문</h3>
        <p>예약·보험·진료에 대한 질문을 모아 두었습니다. 먼저 확인해 보세요.</p>
        <a class="btn btn-line" href="../news/faq/">자주 묻는 질문</a>
      </div>
      <div class="sbox on-parchment">
        <h3>비용이 궁금하시면</h3>
        <p>비급여 항목별 금액은 안내 페이지에 고지되어 있습니다. 총액은 진료 후 안내해 드립니다.</p>
        <a class="btn btn-line" href="../pricing/">비급여 진료비 안내</a>
      </div>
    </aside>
  </div>
</section>
"""
    body += disclaimer(d)
    return page(title="비용·상담 문의", desc="미소로한의원 비용 및 진료 상담 문의.",
                path="/contact/", depth=d, body=body, crumb=[("비용·상담 문의", None)])


def pricing():
    d = 1
    rows = "\n".join(
        f'<tr><th scope="row">{esc(n)}</th><td>{need("금액 확인 필요")}</td><td>{esc(note)}</td></tr>'
        for n, note in [
            ("한약 (첩약)", "처방 구성과 일수에 따라 다름"),
            ("약침", "부위와 횟수에 따라 다름"),
            ("추나요법 (비급여분)", "급여 적용 횟수 초과 시"),
            ("공진단·경옥고", "용량에 따라 다름"),
            ("비염 처치", "처치 종류에 따라 다름"),
            ("피부 처치", "부위와 범위에 따라 다름"),
            ("제증명 수수료", "진단서·소견서 등"),
        ]
    )
    body = phead("안내", "Pricing", "비급여 진료비 안내",
                 "의료법 제45조에 따라 비급여 진료비용을 고지합니다.", d)
    body += f"""<section>
  <div class="wrap">
    <div class="callout rv" style="margin-bottom:var(--s-xxl)">
      <h3>지점별로 금액이 다를 수 있습니다</h3>
      <p>비급여 진료비는 각 지점이 자율적으로 정합니다. 아래는 공통 항목이며, 실제 금액은 지점 페이지 또는 내원 시 확인하실 수 있습니다.</p>
    </div>
    <div class="tbl-wrap rv"><table class="tbl">
      <caption>최종 고지일 [확인 필요] · 금액은 변경될 수 있습니다.</caption>
      <thead><tr><th scope="col">항목</th><th scope="col">금액</th><th scope="col">비고</th></tr></thead>
      <tbody>{rows}</tbody>
    </table></div>
    <div class="prose rv" style="margin-top:var(--s-xxl)">
      <h2>건강보험이 적용되는 항목</h2>
      <p>침, 뜸, 부항 등은 건강보험이 적용됩니다. 일부 추나요법도 연간 횟수 제한 안에서 적용됩니다. 본인부담금은 내원 시 안내해 드립니다.</p>
      <h2>자동차보험</h2>
      <p>교통사고로 인한 진료는 자동차보험이 적용됩니다. 보험사 접수번호가 필요합니다. 자세한 절차는 <a href="../general/accident/insurance/">자동차보험 적용 안내</a>를 참고해 주세요.</p>
    </div>
  </div>
</section>
"""
    body += cta(d) + disclaimer(d)
    return page(title="비급여 진료비 안내", desc="미소로한의원 비급여 진료비용 고지. 의료법 제45조에 따른 안내입니다.",
                path="/pricing/", depth=d, body=body, crumb=[("비급여 진료비 안내", None)])


def privacy():
    d = 1
    body = phead("안내", "Privacy", "개인정보처리방침",
                 "미소로한의원이 수집하는 개인정보와 그 처리 방식입니다.", d, acts=[])
    body += """<section>
  <div class="wrap">
    <div class="callout rv" style="margin-bottom:var(--s-xxl)">
      <h3>법무 검토 필요</h3>
      <p>아래는 구조 확인용 초안입니다. 실제 게시 전에 지점별 개인정보보호책임자, 위탁 업체, 보유 기간을 확정하고 법무 검토를 받아야 합니다.</p>
    </div>
    <div class="prose rv">
      <h2>1. 수집하는 개인정보</h2>
      <ul>
        <li>예약 신청: 이름, 연락처, 지점, 진료 영역, 희망 일시, 전달사항</li>
        <li>상담 문의: 이름, 연락처, 지점, 관심 질환, 문의 내용</li>
        <li>자동 수집: 접속 기록, 쿠키, 브라우저 정보</li>
      </ul>
      <h2>2. 민감정보 처리</h2>
      <p>진료 영역, 관심 질환, 전달사항에는 건강에 관한 정보가 포함될 수 있습니다. 이는 「개인정보 보호법」 제23조의 민감정보에 해당하며, 별도 동의를 받아 수집합니다.</p>
      <h2>3. 이용 목적</h2>
      <p>예약 확인과 안내, 문의 답변, 진료 준비 목적으로만 이용합니다.</p>
      <h2>4. 보유 및 이용 기간</h2>
      <p>수집일로부터 1년간 보유한 뒤 지체 없이 파기합니다. 다만 관계 법령에서 보존을 요구하는 경우 해당 기간을 따릅니다. 진료기록은 「의료법」 제22조 및 시행규칙에 따라 별도로 보존합니다.</p>
      <h2>5. 제3자 제공</h2>
      <p>이용자의 동의 없이 제3자에게 제공하지 않습니다. 다만 법령에 근거가 있는 경우는 예외로 합니다.</p>
      <h2>6. 처리 위탁</h2>
      <p>예약·문의 접수를 위해 외부 폼 서비스를 이용하는 경우, 수탁자와 위탁 업무 내용을 이 항목에 공개합니다. [수탁자 확정 필요]</p>
      <h2>7. 파기 절차</h2>
      <p>보유 기간이 지나거나 처리 목적이 달성된 개인정보는 지체 없이 파기합니다. 전자적 파일은 복구할 수 없는 방법으로 삭제합니다.</p>
      <h2>8. 이용자의 권리</h2>
      <p>개인정보 열람, 정정, 삭제, 처리정지를 요구하실 수 있습니다. 아래 연락처로 요청해 주세요.</p>
      <h2>9. 안전성 확보 조치</h2>
      <p>전송 구간 암호화(HTTPS), 저장 시 암호화, 접근 권한 관리, 접근 기록 보관을 적용합니다.</p>
      <h2>10. 개인정보 보호책임자</h2>
      <p>[성명·직책·연락처 확정 필요]</p>
      <h2>11. 고지 의무</h2>
      <p>이 방침의 내용이 변경되는 경우 시행 7일 전부터 홈페이지에 공지합니다.</p>
      <p class="small">시행일: [확정 필요]</p>
    </div>
  </div>
</section>
"""
    return page(title="개인정보처리방침", desc="미소로한의원 개인정보처리방침.",
                path="/privacy/", depth=d, body=body, crumb=[("개인정보처리방침", None)])


def terms():
    d = 1
    body = phead("안내", "Terms", "이용약관", "홈페이지 이용에 관한 약관입니다.", d, acts=[])
    body += """<section>
  <div class="wrap">
    <div class="callout rv" style="margin-bottom:var(--s-xxl)">
      <h3>법무 검토 필요</h3>
      <p>아래는 구조 확인용 초안입니다. 실제 게시 전에 법무 검토를 받아야 합니다.</p>
    </div>
    <div class="prose rv">
      <h2>제1조 (목적)</h2>
      <p>이 약관은 미소로한의원이 운영하는 홈페이지의 이용 조건과 절차, 이용자와 운영자의 권리·의무를 정함을 목적으로 합니다.</p>
      <h2>제2조 (서비스의 내용)</h2>
      <p>홈페이지는 진료 정보 제공, 예약 신청 접수, 상담 문의 접수를 제공합니다. 온라인 예약은 신청 접수이며, 지점의 확인 연락으로 확정됩니다.</p>
      <h2>제3조 (의료 정보의 성격)</h2>
      <p>홈페이지에 게시된 의료 정보는 일반적인 안내이며, 개별 환자에 대한 진단이나 처방을 대신하지 않습니다. 정확한 상태와 치료 계획은 내원 진료를 통해 확인하셔야 합니다.</p>
      <h2>제4조 (이용자의 의무)</h2>
      <p>이용자는 신청 시 사실에 부합하는 정보를 제공해야 합니다. 허위 정보로 인한 불이익은 이용자가 부담합니다.</p>
      <h2>제5조 (게시물의 관리)</h2>
      <p>운영자는 법령을 위반하거나 타인의 권리를 침해하는 게시물을 사전 통지 없이 삭제할 수 있습니다.</p>
      <h2>제6조 (면책)</h2>
      <p>천재지변, 통신 장애 등 운영자의 책임 없는 사유로 서비스가 중단된 경우 책임을 지지 않습니다.</p>
      <h2>제7조 (약관의 변경)</h2>
      <p>약관이 변경되는 경우 시행 7일 전부터 홈페이지에 공지합니다.</p>
      <p class="small">시행일: [확정 필요]</p>
    </div>
  </div>
</section>
"""
    return page(title="이용약관", desc="미소로한의원 홈페이지 이용약관.",
                path="/terms/", depth=d, body=body, crumb=[("이용약관", None)])


def sitemap_page(tree):
    d = 1
    cols = []
    for title, links in tree:
        items = []
        for label, url, subs in links:
            sub_html = ""
            if subs:
                sub_html = "<ul>" + "".join(
                    f'<li><a href="../{u.lstrip("/")}">{esc(l)}</a></li>' for l, u in subs
                ) + "</ul>"
            items.append(f'<li><a href="../{url.lstrip("/")}">{esc(label)}</a>{sub_html}</li>')
        cols.append(f'<div><h2>{esc(title)}</h2><ul>{"".join(items)}</ul></div>')
    body = phead("안내", "Sitemap", "사이트맵", "전체 페이지 구조입니다.", d, acts=[])
    body += f"""<section>
  <div class="wrap">
    <div class="smap rv">{''.join(cols)}</div>
  </div>
</section>
"""
    return page(title="사이트맵", desc="미소로한의원 홈페이지 전체 구조.",
                path="/sitemap/", depth=d, body=body, crumb=[("사이트맵", None)])
