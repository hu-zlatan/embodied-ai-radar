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

  // BibTeX copy buttons (cards are static HTML; the <pre> stays selectable without JS).
  document.addEventListener('click', function (ev) {
    var b = ev.target.closest && ev.target.closest('button.copy');
    if (!b) return;
    var pre = b.parentNode.querySelector('pre');
    if (!pre || !navigator.clipboard) return;
    navigator.clipboard.writeText(pre.textContent).then(function () {
      var old = b.innerHTML;
      b.textContent = lang() === 'zh' ? '已复制 ✓' : 'Copied ✓';
      setTimeout(function () { b.innerHTML = old; }, 1500);
    });
  });

  var q = document.getElementById('q');
  if (!q) return;
  var fTopic = document.getElementById('f-topic'), fKind = document.getElementById('f-kind'),
      fCode = document.getElementById('f-code'), fSort = document.getElementById('f-sort'), fEmb = document.getElementById('f-emb'), fVen = document.getElementById('f-venue'), out = document.getElementById('results'),
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
        it._s = [it.t, it.en, it.zh, it.o, (it.tg || []).join(' '), it.au, it.ab, it.a, it.id, it.pc, it.v].join(' ').toLowerCase();
      });
      cb();
    }).catch(function () { count.textContent = 'Could not load the search index.'; });
  }
  function topicChips(tp) {
    return (tp || []).map(function (t) { var n = data.topics[t]; return n ? '<a class="chip topic" href="topics/' + t + '.html">' + esc(n[lang() === 'zh' ? 1 : 0]) + '</a>' : ''; }).join('');
  }
  function embChips(em) {
    return (em || []).map(function (m) { var n = (data.emb || {})[m]; return n ? '<span class="chip emb">' + esc(n[lang() === 'zh' ? 1 : 0]) + '</span>' : ''; }).join('');
  }
  function card(it) {
    if (it.k === 'c') {
      var links = [];
      if (it.a) links.push('<a href="https://arxiv.org/abs/' + esc(it.a) + '">' + (lang() === 'zh' ? '论文' : 'Paper') + '</a>');
      if (it.c) links.push('<a href="' + esc(it.c) + '">' + (lang() === 'zh' ? '代码' : 'Code') + '</a>');
      if (it.p) links.push('<a href="' + esc(it.p) + '">' + (lang() === 'zh' ? '项目页' : 'Project') + '</a>');
      links.push('<a class="perma" href="e/' + esc(it.id) + '.html">' + (lang() === 'zh' ? '详情' : 'Details') + '</a>');
      return '<article class="card"><div class="meta"><span class="badge">' + esc(it.ty) + '</span> ' + esc(it.y) + ' · ' + esc(it.o) + (it.v ? ' <span class="badge venue">' + esc(it.v) + '</span>' : '') + (it.h ? ' <span class="star">★</span>' : '') +
        '</div><h3><a href="' + esc(it.l) + '">' + esc(it.t) + '</a></h3><p class="take">' + esc(lang() === 'zh' ? it.zh : it.en) +
        '</p><div class="links">' + links.join(' · ') + (it.s != null ? ' <span class="gh" title="GitHub stars">★ ' + (it.s >= 1000 ? (it.s / 1000).toFixed(1).replace(/\.0$/, '') + 'k' : it.s) + '</span>' : '') + '</div><div class="chips">' + topicChips(it.tp) + embChips(it.em) + '</div></article>';
    }
    return '<article class="card feed"><div class="meta"><span class="badge">arXiv ' + esc(it.pc) + '</span> ' + esc(it.d) + (it.c ? ' <span class="badge code">code</span>' : '') + (it.v ? ' <span class="badge venue">' + esc(it.v) + '</span>' : '') +
      '</div><h3><a href="https://arxiv.org/abs/' + esc(it.id) + '">' + esc(it.t) + '</a></h3><p class="authors">' + esc(it.au) +
      '</p><div class="links"><a href="https://arxiv.org/pdf/' + esc(it.id) + '">PDF</a>' + (it.c ? ' · <a href="' + esc(it.c) + '">' + (lang() === 'zh' ? '代码' : 'Code') + '</a>' + (it.s != null ? ' <span class="gh" title="GitHub stars">★ ' + (it.s >= 1000 ? (it.s / 1000).toFixed(1).replace(/\.0$/, '') + 'k' : it.s) + '</span>' : '') : '') +
      (it.pj ? ' · <a href="' + esc(it.pj) + '">' + (lang() === 'zh' ? '项目页' : 'Project') + '</a>' : '') +
      '</div><div class="chips">' + topicChips(it.tp) + embChips(it.em) + '</div></article>';
  }
  function active() { return q.value.trim() || fTopic.value || (fEmb && fEmb.value) || (fVen && fVen.value) || fKind.value || fCode.checked || (fSort && fSort.value); }
  function syncUrl() {
    // Keep the address bar shareable: ?q=…&topic=…&robot=…&src=…&code=1 (lang is kept if present).
    try {
      var u = new URLSearchParams(location.search), set = function (k, v) { if (v) u.set(k, v); else u.delete(k); };
      set('q', q.value.trim()); set('topic', fTopic.value); set('robot', fEmb ? fEmb.value : ''); set('venue', fVen ? fVen.value : '');
      set('src', fKind.value); set('code', fCode.checked ? '1' : ''); set('sort', fSort ? fSort.value : '');
      var s = u.toString();
      history.replaceState(null, '', location.pathname + (s ? '?' + s : '') + location.hash);
    } catch (e) {}
  }
  function render() {
    syncUrl();
    if (!active()) { out.innerHTML = ''; count.textContent = ''; if (home) home.hidden = false; return; }
    load(function () {
      var terms = q.value.toLowerCase().split(/\s+/).filter(Boolean);
      var res = data.items.filter(function (it) {
        if (fTopic.value && (it.tp || []).indexOf(fTopic.value) < 0) return false;
        if (fEmb && fEmb.value && (it.em || []).indexOf(fEmb.value) < 0) return false;
        if (fVen && fVen.value && !(it.v && (fVen.value === '*' || it.v === fVen.value || String(it.v).indexOf(fVen.value + ' ') === 0))) return false;
        if (fKind.value && it.k !== fKind.value) return false;
        if (fCode.checked && !it.c) return false;
        for (var i = 0; i < terms.length; i++) if (it._s.indexOf(terms[i]) < 0) return false;
        return true;
      });
      var mode = fSort ? fSort.value : '';
      res.sort(function (a, b) {
        if (mode === 'stars') { var sa = a.s == null ? -1 : a.s, sb = b.s == null ? -1 : b.s; if (sa !== sb) return sb - sa; }
        if (mode === 'new') { var da = a.d || String(a.y), db = b.d || String(b.y); if (da !== db) return da < db ? 1 : -1; }
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
  [fTopic, fEmb, fVen, fKind, fCode, fSort].filter(Boolean).forEach(function (el) { el.addEventListener('change', render); });
  var params = new URLSearchParams(location.search);
  if (params.get('q')) { q.value = params.get('q'); render(); }
  if (params.get('topic')) { fTopic.value = params.get('topic'); render(); }
  if (params.get('robot') && fEmb) { fEmb.value = params.get('robot'); render(); }
  if (params.get('venue') && fVen) { fVen.value = params.get('venue'); render(); }
  if (params.get('src')) { fKind.value = params.get('src'); render(); }
  if (params.get('code') === '1') { fCode.checked = true; render(); }
  if (params.get('sort') && fSort) { fSort.value = params.get('sort'); render(); }
})();
