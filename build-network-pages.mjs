import { copyFileSync, existsSync, mkdirSync, readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { basename, dirname, join } from 'node:path';

const official = 'https://www.misoro.kr';
const categories = [
  ['skin', '피부질환', [
    ['warts','사마귀','어느 부위에서 시작했는지, 병변의 개수와 변화, 이전 치료 이력','/skin/sama/','https://suwon.misoro.kr/warts/','수원점 공식 안내에는 병변의 위치와 범위에 따라 침·약침과 외용 한약 등을 고려하는 진료가 소개되어 있습니다.'],
    ['atopy','아토피','가려움으로 잠을 깨는지, 피부가 불편한 부위와 사용 중인 외용제','/skin/atopy/'],
    ['eczema','습진','진물·각질·갈라짐의 변화와 물일이나 제품 접촉 여부','/skin/gin/index.php'],
    ['psoriasis','건선','각질과 붉은 부위의 위치와 변화, 현재 받고 있는 치료','/skin/pangun/index.php'],
    ['dyshidrosis','한포진','손발 물집이 생기는 부위와 반복 주기, 갈라짐 여부','/skin/han/index.php','https://suwon.misoro.kr/dyshidrosis/','수원점 공식 안내에는 피부 상태를 살펴 한약·침·약침을 고려하고 필요한 경우 외용 한약이나 광선치료를 더하는 방식이 소개되어 있습니다.'],
    ['urticaria','두드러기','발진이 생긴 시간과 사라지기까지 걸린 시간, 복용약 또는 활동의 변화','/skin/doo/index.php'],
    ['hyperhidrosis','다한증','땀이 많이 나는 부위와 상황, 일상에서 불편한 순간','/skin/da/index.php'],
  ]],
  ['respiratory', '호흡기질환', [
    ['rhinitis','비염','코막힘·콧물·재채기가 반복되는 시간대와 수면 중 불편','/respiratory/b_program/','https://suwon.misoro.kr/rhinitis/','수원점 공식 안내에는 코 점막을 살핀 뒤 점막 처치·배농, 한약·침·약침 중 필요한 치료를 검토하는 과정이 소개되어 있습니다.'],
    ['sinusitis','축농증','코막힘, 콧물이 목으로 넘어가는 느낌, 이전 검사와 치료 이력','/respiratory/s_program/index.php','https://suwon.misoro.kr/sinusitis/','수원점 공식 안내에는 진찰 후 배농치료, 한약, 침 등을 검토하는 진료 과정이 소개되어 있습니다.'],
    ['otitis','중이염','귀 통증이나 먹먹함이 시작된 시점, 반복 여부, 이전 검사 결과','/respiratory/j_tong/index.php'],
  ]],
  ['general', '일반한의학', [
    ['pain','통증','불편한 부위와 시작 시점, 통증이 달라지는 자세나 활동'],
    ['weight-care','다이어트','체중 관리 목표, 생활 패턴과 현재 복용 중인 약'],
    ['seasonal-tonic','계절보약','상담을 원하는 이유, 건강 상태와 복용 중인 약'],
    ['traffic-injury','교통사고','사고 발생일, 이후 불편한 부위와 기존 검사·진료 내역'],
  ]],
];

const output = process.argv[2] || '.';
function entries(collection) {
  const folder = join('content', collection);
  return readdirSync(folder).filter(file => file.endsWith('.json')).sort().reverse().flatMap(file => {
    const id = basename(file, '.json');
    if (!/^[\p{L}\p{N}_-]+$/u.test(id) || id === 'index') throw new Error('Invalid CMS entry name: '+file);
    const entry = JSON.parse(readFileSync(join(folder,file),'utf8'));
    if (entry.published !== true || (collection === 'cases' && entry.reviewed !== true)) return [];
    for (const key of ['title','summary','body']) {
      if (typeof entry[key] !== 'string' || !entry[key].trim()) throw new Error(file+': missing '+key);
    }
    return [{...entry,id}];
  });
}
const menu = [['about/','네트워크 소개'],['branches/','지점 안내'],...categories.map(([id,label])=>['care/'+id+'/',label]),['notices/','공지'],['columns/','칼럼']];
const escape = value => value.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('"','&quot;');
const link = (url, label, cls = '') => `<a${cls ? ` class="${cls}"` : ''} href="${escape(url)}">${escape(label)}</a>`;
const panel = (title, body) => `<section class="detail-panel"><h2>${title}</h2>${body}</section>`;
const list = items => `<ul class="detail-list">${items.map(([url,label])=>`<li>${link(url,label)}</li>`).join('')}</ul>`;
const paragraphs = body => body.trim().split(/\r?\n(?:\s*\r?\n)*/).map(text=>'<p>'+escape(text)+'</p>').join('');
const relative = route => '../'.repeat(route.split('/').filter(Boolean).length);
function picture(value, alt, route) {
  if (!value) return '';
  const path = value.replace(/^\//,'');
  if (!/^media\/(?:[\p{L}\p{N} _.-]+\/)*[\p{L}\p{N} _.-]+\.(?:jpe?g|png|webp|avif)$/iu.test(path)
    || path.split('/').some(part=>part === '.' || part === '..') || !existsSync(path)) throw new Error('Invalid CMS image: '+value);
  if (output !== '.') {
    const destination = join(output,path);
    mkdirSync(dirname(destination),{recursive:true});
    copyFileSync(path,destination);
  }
  const url = relative(route)+path.split('/').map(encodeURIComponent).join('/');
  return `<img class="cms-image" src="${url}" alt="${escape(alt || '')}" loading="lazy" decoding="async">`;
}
function page(route, title, intro, body, ancestors = []) {
  const root = relative(route);
  const links = menu.filter(([,label])=>label!==title).map(([url,label])=>link(root+url+'index.html',label)).join('');
  const breadcrumbs = [['network-home.html','홈'],...ancestors].map(([url,label])=>link(root+url,label)).join('<span aria-hidden="true"> / </span>');
  const file = join(output,route,'index.html');
  mkdirSync(dirname(file),{recursive:true});
  writeFileSync(file,`<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">
<title>${escape(title)} | 미소로한의원</title><meta name="description" content="${escape(intro)}">
<link rel="stylesheet" href="${root}homepage.css"><link rel="stylesheet" href="${root}network-home.css"><link rel="stylesheet" href="${root}network-details.css"></head>
<body><a class="skip" href="#content">본문 바로가기</a><header><div class="wrap navigation">${link(root+'network-home.html','미소로한의원','brand')}
<nav class="desktop-nav" aria-label="상단 메뉴">${links}</nav><div class="header-actions">${link(root+'network-home.html#consultation','상담 문의','button')}</div>
<details class="mobile-nav"><summary>메뉴</summary><nav aria-label="모바일 메뉴">${links}</nav></details></div></header>
<main id="content"><div class="detail-heading"><div class="wrap"><nav class="breadcrumbs" aria-label="현재 위치">${breadcrumbs}<span aria-hidden="true"> / </span><span aria-current="page">${escape(title)}</span></nav>
<h1>${escape(title)}</h1><p>${escape(intro)}</p></div></div><div class="wrap detail-content">${body}</div></main>
<footer class="dark"><div class="wrap">${link(root+'network-home.html','미소로한의원 네트워크','brand')}${link(root+'branches/index.html','지점별 전화와 방문 안내')}</div></footer></body></html>`);
}

page('about/','미소로한의원 네트워크','피부·호흡기 질환과 일반한의학 진료를 안내합니다.',
  panel('진료 분야',list(categories.map(([id,name])=>['../care/'+id+'/index.html',name])))+
  panel('지역별 지점','<p>방문하기 편한 지점에서 진료 분야, 진료시간과 상담 방법을 확인하세요.</p>'+link('../branches/index.html','전체 지점 보기','button'))+
  panel('첫 방문 준비','<p>언제부터 불편했는지, 재발이나 악화가 반복되는지, 이전 진료와 복용약이 있는지 정리해 오시면 상담에 도움이 됩니다. 방문 일정은 해당 지점에 확인해 주세요.</p>'));

for (const [group, name, topics] of categories) {
  const base='care/'+group+'/';
  const categoryName=[base+'index.html', name];
  page(base,name,name+'에 해당하는 진료 안내를 살펴보세요.',panel('세부 진료 분야',list(topics.map(([id,label])=>[id+'/index.html',label]))));
  for (const [id,label,visit,path,specific,method] of topics) {
    const route=base+id+'/';
    const officialUrl=path ? official+path : '';
    page(route,label+' 진료 안내',label+' 진료를 알아보는 분을 위한 첫 방문 안내입니다.',
      panel('진료 전에 정리할 내용',`<p>${visit} 등을 정리해 주세요. 이전 검사나 진료 기록, 현재 사용하는 약이 있다면 의료진에게 알려주세요.</p>`)+
      panel('치료법과 진료 과정','<p>진찰에서 확인하는 내용과 치료 선택에 관한 안내를 확인하세요.</p>'+link('treatment/index.html',label+' 치료법 보기','button'))+
      panel('지점 안내','<p>진료 범위와 예약 가능 시간은 방문할 지점에 확인해 주세요.</p>'+link('../../../branches/index.html','지점 찾기','button outline')),[categoryName]);
    page(route+'treatment/',label+' 치료법',label+' 진료에서 확인하는 항목과 치료 선택 기준을 알아보세요.',
      panel('진찰에서 확인하는 내용',`<p>${visit} 등을 확인합니다.</p>`)+
      panel('치료 방향',`<p>${method || '진찰에서 확인한 상태와 이전 치료 이력을 토대로 가능한 진료 방법을 의료진과 상의합니다. 적용 방법과 진료 범위는 방문할 지점에 문의해 주세요.'}</p>`+
        (officialUrl ? list([[specific || officialUrl, '공식 '+label+' 진료 자료'],...(specific ? [[officialUrl,'네트워크 '+label+' 진료 안내']] : [])]) : ''))+
      panel('방문 전 확인','<p>치료 방법과 적용 여부는 진료 후 결정합니다. 상담을 원하시면 방문하실 지점을 선택해 주세요.</p>'+link('../../../../branches/index.html','지점 안내','button')),
      [categoryName,[route+'index.html',label+' 진료 안내']]);
  }
}


const branches = entries('branches').sort((left,right)=>left.title.localeCompare(right.title,'ko'));
function branchChannel(value, channel) {
  if (!value) return '';
  const url = new URL(value);
  const hosts = channel === 'kakao' ? ['pf.kakao.com'] : ['booking.naver.com','m.booking.naver.com'];
  if (url.protocol !== 'https:' || !hosts.includes(url.hostname) || url.port || url.username || url.password ||
      (channel === 'kakao' ? !/^\/_[-a-zA-Z0-9]+(?:\/chat)?\/?$/.test(url.pathname) : !/^\/booking\/\d+\/bizes\/\d+(?:\/items\/\d+)?\/?$/.test(url.pathname))) {
    throw new Error('Invalid branch '+channel+' URL: '+value);
  }
  return url.href;
}
page('branches/','지점 안내','방문하기 편한 지점을 선택해 전화와 방문 방법을 확인하세요.',
  panel('전체 지점',list(branches.map(({id,title})=>[id+'/index.html',title]))));
for (const branch of branches) {
  const {id,title,summary,body,phone,address,hours,website,image,imageAlt,kakaoUrl,naverUrl} = branch;
  const route = 'branches/'+id+'/';
  if (typeof phone !== 'string' || !/^0[\d -]{7,14}\d$/.test(phone)) throw new Error(id+': invalid branch phone');
  if (website && !/^https:\/\//.test(website)) throw new Error(id+': expected an HTTPS website');
  page(route,title,summary,
    panel('상담·예약','<div class="actions">'+link('tel:'+phone.replace(/\D/g,''),phone+' 전화하기','button')+
      (kakaoUrl ? link(branchChannel(kakaoUrl,'kakao'),'카카오톡 채널','button outline') : '')+
      (naverUrl ? link(branchChannel(naverUrl,'naver'),'네이버 예약','button outline') : '')+'</div>')+
    panel('진료시간과 오시는 길',
      picture(image,imageAlt,route)+
      (address ? paragraphs(address) : '')+(hours ? paragraphs(hours) : '<p>방문 전 최신 진료시간과 휴진일을 확인해 주세요.</p>')+
      list([[website || official,'공식 지점 안내'],['https://map.naver.com/p/search/'+encodeURIComponent('미소로한의원 '+title),'네이버 지도에서 지점 검색']]))+
    panel('첫 방문 문의',paragraphs(body)),
    [['branches/index.html','지점 안내']]);
}

const collections = [
  ['notices','공지사항','방문 전 진료시간과 지점 운영 안내를 확인하세요.'],
  ['columns','건강 칼럼','진료에 앞서 참고할 글을 모았습니다.'],
  ['programs','치료 프로그램','공개된 치료 프로그램을 확인하세요.'],
  ['cases','치료 전후 사진','게시 검토를 마친 자료가 등록되면 확인할 수 있습니다.'],
];
for (const [collection,label,description] of collections) {
  const records = entries(collection);
  let indexContent = records.length
    ? `<ul class="detail-list">${records.map(({id,title,summary})=>`<li>${link(encodeURIComponent(id)+'/index.html',title)}<p>${escape(summary)}</p></li>`).join('')}</ul>`
    : '<p>현재 공개된 게시물이 없습니다.</p>';
  if (collection === 'columns') indexContent += list([['https://bundang.misoro.kr/guide/','분당점 공식 칼럼'],['https://suwon.misoro.kr/guide/','수원점 공식 칼럼']]);
  page(collection+'/',label,description,panel('게시물',indexContent));
  for (const entry of records) {
    const {id,title,summary,body,image,imageAlt,before,beforeAlt,after,afterAlt} = entry;
    const route = collection+'/'+id+'/';
    let photos = picture(image,imageAlt,route);
    if (collection === 'cases') {
      if (!before || !after || !beforeAlt?.trim() || !afterAlt?.trim()) throw new Error(id+': before/after images and descriptions are required');
      photos = `<div class="cms-comparison"><figure>${picture(before,beforeAlt,route)}<figcaption>치료 전</figcaption></figure><figure>${picture(after,afterAlt,route)}<figcaption>치료 후</figcaption></figure></div>`;
    }
    page(route,title,summary,panel('상세 안내',photos+paragraphs(body)),[[collection+'/index.html',label]]);
  }
}

const home = readFileSync('network-home.html','utf8');
const options = branches.map(({title,phone,kakaoUrl,naverUrl})=>`<option value="${phone.replace(/\D/g,'')}" data-kakao="${escape(branchChannel(kakaoUrl,'kakao'))}" data-naver="${escape(branchChannel(naverUrl,'naver'))}">${escape(title)}</option>`).join('\n            ');
writeFileSync(join(output,'network-home.html'),home.replace(/(<!-- CMS branches -->)[\s\S]*?(<!-- end CMS branches -->)/,
  (_, start, end)=>start+'\n            '+options+'\n            '+end));
