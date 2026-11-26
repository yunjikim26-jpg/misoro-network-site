const menu = document.querySelector('.mobile-nav');
const branch = document.querySelector('#branch');
const call = document.querySelector('#call-branch');
const statusMessage = document.querySelector('.branch-status');
const branchChannels = ['kakao','naver'].map(key => ({key, link: document.querySelector('#'+key+'-branch')}));
const quickLinks = document.querySelectorAll('[data-quick]');

menu.addEventListener('click', (event) => {
  if (!event.target.closest('a')) return;
  menu.open = false;
  menu.querySelector('summary').focus();
});

menu.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape' || !menu.open) return;
  menu.open = false;
  menu.querySelector('summary').focus();
});

function updateBranch() {
  const number = branch.value;
  const option = branch.selectedOptions[0];
  const channels = option?.dataset || {};
  const destinations = {...channels, phone: number ? 'tel:'+number : ''};
  for (const {key, link} of branchChannels) {
    const url = destinations[key];
    link.hidden = !url;
    if (url) link.href = url;
    else link.removeAttribute('href');
  }
  for (const link of quickLinks) {
    const url = destinations[link.dataset.quick];
    link.href = url || '#branch';
    link.dataset.direct = String(Boolean(url));
  }
  call.hidden = !number;
  if (!number) {
    call.removeAttribute('href');
    statusMessage.textContent = '상담할 지점을 선택하면 전화번호가 표시됩니다.';
    return;
  }

  const formatted = number.replace(/^(02|0\d{2})(\d{3,4})(\d{4})$/, '$1-$2-$3');
  const name = option.textContent;
  call.href = 'tel:' + number;
  call.textContent = name + ' 전화하기';
  statusMessage.textContent = name + ' ' + formatted;
}

branch.addEventListener('change', updateBranch);
for (const link of quickLinks) link.addEventListener('click', () => {
  if (link.dataset.direct === 'true') return;
  const channel = link.dataset.quick === 'kakao' ? '카카오톡' : '네이버 예약';
  if (branch.value && link.dataset.quick !== 'phone') {
    statusMessage.textContent = '이 지점은 '+channel+' 링크가 아직 연결되지 않았습니다. 전화 문의를 이용해 주세요.';
  }
  branch.focus();
});
updateBranch();

const consultation = document.querySelector('.consultation-online');
const formUrl = consultation.dataset.formUrl.trim();
if (/^https:\/\/(?:forms\.gle\/[a-zA-Z0-9]+|docs\.google\.com\/forms\/d\/e\/[a-zA-Z0-9_-]+\/viewform)(?:\?[^#\s]*)?$/.test(formUrl)) {
  const formLink = consultation.querySelector('.consultation-form-link');
  formLink.href = formUrl;
  formLink.hidden = false;
  consultation.querySelector('.consultation-preview').hidden = true;
}
