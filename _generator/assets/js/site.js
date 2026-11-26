(function(){
  "use strict";

  /* 모바일 메뉴 */
  var burger = document.querySelector('.burger');
  var mnav = document.getElementById('mnav');
  burger.addEventListener('click', function(){
    var open = burger.getAttribute('aria-expanded') === 'true';
    burger.setAttribute('aria-expanded', String(!open));
    burger.setAttribute('aria-label', open ? '메뉴 열기' : '메뉴 닫기');
    mnav.dataset.open = String(!open);
  });

  /* 지점 선택 드롭다운 */
  var bs = document.getElementById('branchsel');
  var bsBtn = bs.querySelector('button');
  function closeBS(){ bs.dataset.open = 'false'; bsBtn.setAttribute('aria-expanded','false'); }
  bsBtn.addEventListener('click', function(e){
    e.stopPropagation();
    var open = bs.dataset.open === 'true';
    bs.dataset.open = String(!open);
    bsBtn.setAttribute('aria-expanded', String(!open));
  });
  document.addEventListener('click', function(e){ if(!bs.contains(e.target)) closeBS(); });
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape') closeBS(); });

  /* 증상 필터 */
  var filterBtns = document.querySelectorAll('.filters button');
  var chips = document.querySelectorAll('#chips .chip');
  filterBtns.forEach(function(btn){
    btn.addEventListener('click', function(){
      var f = btn.dataset.filter;
      filterBtns.forEach(function(b){ b.setAttribute('aria-pressed', String(b === btn)); });
      chips.forEach(function(c){ c.hidden = !(f === 'all' || c.dataset.cat === f); });
    });
  });

  /* 등장 모션 */
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var rv = document.querySelectorAll('.rv');
  if (reduce || !('IntersectionObserver' in window)) {
    rv.forEach(function(el){ el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    rv.forEach(function(el, i){ el.style.transitionDelay = (Math.min(i % 5, 4) * 60) + 'ms'; io.observe(el); });
  }
})();

/* ---- 칼럼 목록 필터 (2차) ---- */
(function(){
  "use strict";
  var btns = document.querySelectorAll('[data-colfilter]');
  if (!btns.length) return;
  var cards = document.querySelectorAll('#collist .col');
  btns.forEach(function(btn){
    btn.addEventListener('click', function(){
      var f = btn.dataset.colfilter;
      btns.forEach(function(b){ b.setAttribute('aria-pressed', String(b === btn)); });
      cards.forEach(function(c){ c.hidden = !(f === 'all' || c.dataset.cat === f); });
    });
  });
})();

/* ---- 폼 입력 검증 (3차에서 외부 폼 서비스와 연결) ---- */
(function(){
  "use strict";
  ['bookingForm','contactForm'].forEach(function(id){
    var f = document.getElementById(id);
    if (!f) return;
    f.addEventListener('submit', function(e){
      e.preventDefault();
      var note = f.querySelector('.formnote');
      if (!f.checkValidity()) {
        var bad = f.querySelector(':invalid');
        if (bad) bad.focus();
        if (note) note.textContent = '필수 항목을 채워 주세요.';
        return;
      }
      if (note) note.textContent = '입력 검증을 통과했습니다. 실제 전송은 3차 작업에서 연결합니다.';
    });
  });
})();
