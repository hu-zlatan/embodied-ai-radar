// Embodied AI Radar — language toggle + instant search. No dependencies, no tracking.
(function () {
  var root = document.documentElement;
  function lang() { return root.classList.contains('zh') ? 'zh' : 'en'; }
  function setLang(l) {
    root.classList.toggle('zh', l === 'zh');
    root.lang = l === 'zh' ? 'zh-CN' : 'en';
    try { localStorage.setItem('lang', l); } catch (e) {}
    document.querySelectorAll('option[data-en]').forEach(function (o) { o.textContent = o.dataset[l]; });
    if (window.__radarRender) window.__radarRender();
  }
  var btn = document.getElementById('lang');
  if (btn) btn.addEventListener('click', function () { setLang(lang() === 'zh' ? 'en' : 'zh'); });
  setLang(lang());

  var q = document.getElementById('q');
  if (!q) return;
  var fTopic = document.getElementById('f-topic'), fKind = document.getElementById('f-kind'),
      fCode = document.getElementById('f-code'), out = document.getElementById('results'),
      count = document.getElementById('count'), home = document.getElementById('home-static');
  var data = null, loading = false;
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'})[c]; }); }
  function load(cb) {
    if (data) return cb();
    if (loading) return;
    loading = true;
    fetch('data/index.json').then(function (r) { return r.json(); }).then(function (j) {
      data = j;
      data.items.forEach(function (it) {
        it._s = [it.t, it.en, it.zh, it.o, (it.tg || []).join(' '), it.au, it.ab, it.a, it.id, it.pc].join(' ').toLowerCase();
      });
      cb();
    }).catch(function () { count.textContent = 'Could not load the search index.'; });
  }
  function topicChips(tp) {
    return (tp || []).map(function (t) { var n = data.topics[t]; return n ? '<a class="chip topic" href="topics/' + t + '.html">' + esc(n[lang() === 'zh' ? 1 : 0]) + '</a>' : ''; }).join('');
  }
  function card(it) {
    if (it.k === 'c') {
      var links = [];
      if (it.a) links.push('<a href="https://arxiv.org/abs/' + esc(it.a) + '">' + (lang() === 'zh' ? '论文' : 'Paper') + '</a>');
      if (it.c) links.push('<a href="' + esc(it.c) + '">' + (lang() === 'zh' ? '代码' : 'Code') + '</a>');
      if (it.p) links.push('<a href="' + esc(it.p) + '">' + (lang() === 'zh' ? '项目页' : 'Project') + '</a>');
      return '<article class="card"><div class="meta"><span class="badge">' + esc(it.ty) + '</span> ' + esc(it.y) + ' · ' + esc(it.o) + (it.h ? ' <span class="star">★</span>' : '') +
        '</div><h3><a href="' + esc(it.l) + '">' + esc(it.t) + '</a></h3><p class="take">' + esc(lang() === 'zh' ? it.zh : it.en) +
        '</p><div class="links">' + links.join(' · ') + '</div><div class="chips">' + topicChips(it.tp) + '</div></article>';
    }
    return '<article class="card feed"><div class="meta"><span class="badge">arXiv ' + esc(it.pc) + '</span> ' + esc(it.d) + (it.c ? ' <span class="badge code">code</span>' : '') +
      '</div><h3><a href="https://arxiv.org/abs/' + esc(it.id) + '">' + esc(it.t) + '</a></h3><p class="authors">' + esc(it.au) +
      '</p><div class="links"><a href="https://arxiv.org/pdf/' + esc(it.id) + '">PDF</a>' + (it.c ? ' · <a href="' + esc(it.c) + '">' + (lang() === 'zh' ? '代码' : 'Code') + '</a>' : '') +
      '</div><div class="chips">' + topicChips(it.tp) + '</div></article>';
  }
  function active() { return q.value.trim() || fTopic.value || fKind.value || fCode.checked; }
  function render() {
    if (!active()) { out.innerHTML = ''; count.textContent = ''; if (home) home.hidden = false; return; }
    load(function () {
      var terms = q.value.toLowerCase().split(/\s+/).filter(Boolean);
      var res = data.items.filter(function (it) {
        if (fTopic.value && (it.tp || []).indexOf(fTopic.value) < 0) return false;
        if (fKind.value && it.k !== fKind.value) return false;
        if (fCode.checked && !it.c) return false;
        for (var i = 0; i < terms.length; i++) if (it._s.indexOf(terms[i]) < 0) return false;
        return true;
      });
      res.sort(function (a, b) {
        if (a.k !== b.k) return a.k === 'c' ? -1 : 1;
        if (a.k === 'c') return (b.h - a.h) || (b.y - a.y);
        return a.d < b.d ? 1 : -1;
      });
      var shown = res.slice(0, 200);
      count.textContent = (lang() === 'zh' ? '找到 ' + res.length + ' 条结果' : res.length + ' results') + (res.length > 200 ? (lang() === 'zh' ? '（显示前 200 条）' : ' (showing 200)') : '');
      out.innerHTML = '<div class="cards">' + shown.map(card).join('') + '</div>';
      if (home) home.hidden = true;
    });
  }
  window.__radarRender = function () { if (q) render(); };
  var timer;
  q.addEventListener('input', function () { clearTimeout(timer); timer = setTimeout(render, 120); });
  [fTopic, fKind, fCode].forEach(function (el) { el.addEventListener('change', render); });
  var params = new URLSearchParams(location.search);
  if (params.get('q')) { q.value = params.get('q'); render(); }
  if (params.get('topic')) { fTopic.value = params.get('topic'); render(); }
})();
