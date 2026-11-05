// Embodied AI Radar — language toggle + instant search. No dependencies, no tracking.
(function () {
  var root = document.documentElement;
  function lang() { return root.classList.contains('zh') ? 'zh' : 'en'; }
  function setLang(l) {
    root.classList.toggle('zh', l === 'zh');
    root.lang = l === 'zh' ? 'zh-CN' : 'en';
    try { localStorage.setItem('lang', l); } catch (e) {}
    document.querySelectorAll('option[data-en]').forEach(function (o) { o.textContent = o.dataset[l]; });
    document.querySelectorAll('input[data-en]').forEach(function (o) { o.placeholder = o.dataset[l]; });
    if (window.__radarRender) window.__radarRender();
  }
  var btn = document.getElementById('lang');
  if (btn) btn.addEventListener('click', function () { setLang(lang() === 'zh' ? 'en' : 'zh'); });
  setLang(lang());

  // Filter box on long venue pages: ?q=&topic=&code=1 keeps a filtered view shareable.
  var vf = document.getElementById('vf');
  if (vf) {
    var vq = document.getElementById('vf-q'), vt = document.getElementById('vf-t'), vc = document.getElementById('vf-c'), vn = document.getElementById('vf-n'), vh = document.getElementById('vf-h'), vk = document.getElementById('vf-k');
    var vcards = Array.prototype.slice.call(document.querySelectorAll('.cards .card'));
    var vtext = vcards.map(function (c) {
      var h = c.querySelector('h3'), a = c.querySelector('.authors');
      return ((h ? h.textContent : '') + ' ' + (a ? a.textContent : '')).toLowerCase();
    });
    var vm = document.getElementById('vf-m'), my = null;
    var vapply = function () {
      var q = vq.value.trim().toLowerCase(), t = vt.value, code = vc.checked, honor = vh && vh.checked, k = vk ? vk.value : '', shown = new Set();
      vcards.forEach(function (c, i) {
        var ok = (!q || vtext[i].indexOf(q) >= 0) && (!t || (' ' + c.dataset.t + ' ').indexOf(' ' + t + ' ') >= 0) && (!k || (' ' + c.dataset.k + ' ').indexOf(' ' + k + ' ') >= 0) && (!code || c.dataset.c) && (!honor || c.dataset.h) && (!(vm && vm.checked) || my.has(c.dataset.id));
        c.hidden = !ok;
        if (ok) shown.add(c.dataset.id || i);
      });
      vn.textContent = shown.size + ' / ' + new Set(vcards.map(function (c, i) { return c.dataset.id || i; })).size;
      Array.prototype.forEach.call(document.querySelectorAll('.pg-sess'), function (b) { b.hidden = !b.querySelector('.card:not([hidden])'); });
      var u = new URLSearchParams();
      if (q) u.set('q', vq.value.trim());
      if (t) u.set('topic', t);
      if (k) u.set('theme', k);
      if (code) u.set('code', '1');
      if (honor) u.set('honor', '1');
      if (vm && vm.checked) u.set('mine', '1');
      try { history.replaceState(null, '', (u.toString() ? '?' + u : location.pathname) + location.hash); } catch (e) {}
    };
    var vp = new URLSearchParams(location.search);
    vq.value = vp.get('q') || '';
    vt.value = vp.get('topic') || '';
    if (vk) vk.value = vp.get('theme') || '';
    vc.checked = vp.get('code') === '1';
    if (vh) vh.checked = vp.get('honor') === '1';
    if (vm) my = mySchedule(vf, vm, vp, vcards, function () { vapply(); });
    if (vm) sessionClock();
    [vq, vt, vc].concat(vh ? [vh] : []).concat(vk ? [vk] : []).concat(vm ? [vm] : []).forEach(function (el) { el.addEventListener(el === vq ? 'input' : 'change', vapply); });
    vapply();
  }

  // Program guide: 'Now / Next' bar and session times in the viewer's own time zone, both from data-when (UTC).
  // The bar shows only before and during the conference. Listed times stay in venue time; a line is added for remote viewers.
  function sessionClock() {
    var bar = document.getElementById('pg-now');
    function bi(en, zh) { return '<span lang="en">' + en + '</span><span lang="zh">' + zh + '</span>'; }
    function utc(s) { var m = /^(\d{4})(\d\d)(\d\d)T(\d\d)(\d\d)/.exec(s || ''); return m ? new Date(Date.UTC(+m[1], m[2] - 1, +m[3], +m[4], +m[5])) : null; }
    var list = [];
    document.querySelectorAll('.pg-sess').forEach(function (b) {
      var w = (b.dataset.when || '').split('/'), s = utc(w[0]), e = utc(w[1]);
      if (s && e) list.push({ b: b, s: s, e: e });
    });
    if (!bar || !list.length) return;
    list.sort(function (x, y) { return x.s - y.s; });
    function fmt(d, loc, day) {
      var o = { hour: '2-digit', minute: '2-digit', hour12: false };
      if (day) { o.weekday = 'short'; o.month = 'numeric'; o.day = 'numeric'; }
      try { return d.toLocaleString(loc, o); } catch (e) { return d.toISOString().slice(0, 16).replace('T', ' ') + ' UTC'; }
    }
    if (list[0].s.getTimezoneOffset() !== 360) {  // venue is UTC-6 in November
      list.forEach(function (x) {
        var p = document.createElement('p');
        p.className = 'pg-local';
        p.innerHTML = bi('Your time: ' + fmt(x.s, 'en-US', true) + '–' + fmt(x.e, 'en-US'), '你的时间：' + fmt(x.s, 'zh-CN', true) + '–' + fmt(x.e, 'zh-CN'));
        x.b.querySelector('p.muted').after(p);
      });
    }
    function name(x) { return '<a href="#' + x.b.querySelector('h3').id + '">' + x.b.querySelector('h3').innerHTML + '</a>'; }
    function until(ms) {
      var m = Math.max(1, Math.ceil(ms / 60000)), h = Math.round(m / 60), d = Math.round(m / 1440);
      if (m < 60) return bi('in ' + m + ' min', m + ' 分钟后');
      if (m < 2880) return bi('in ' + h + ' h', h + ' 小时后');
      return bi('in ' + d + ' days', d + ' 天后');
    }
    function tick() {
      var now = new Date(), on = list.filter(function (x) { return x.s <= now && now < x.e; }), later = list.filter(function (x) { return x.s > now; });
      var next = later.filter(function (x) { return +x.s === +later[0].s; }), html = '';
      if (on.length) html += '<p><b>' + bi('Now', '正在进行') + '</b> ' + on.map(name).join(' · ') + '</p>';
      if (next.length) html += '<p><b>' + bi('Next', '接下来') + '</b> ' + until(next[0].s - now) + ': ' + next.map(name).join(' · ') + '</p>';
      bar.innerHTML = html;
      bar.hidden = !html;
    }
    tick();
    setInterval(tick, 60000);
  }

  // Program guide: a personal schedule. ☆ on a card saves it in this browser; the panel lists saved papers
  // by session, with a share link (?my=id,id), plain text and a calendar file. Nothing leaves the browser.
  function mySchedule(vf, vm, params, cards, refilter) {
    var key = 'my:' + vf.dataset.store, panel = document.getElementById('pg-my'), mem = new Set();
    function bi(en, zh) { return '<span lang="en">' + en + '</span><span lang="zh">' + zh + '</span>'; }
    function esc(s) { var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }
    function save() { try { localStorage.setItem(key, Array.from(mem).join(',')); } catch (e) {} }
    try { (localStorage.getItem(key) || '').split(',').filter(Boolean).forEach(function (i) { mem.add(i); }); } catch (e) {}
    var known = new Set(cards.map(function (c) { return c.dataset.id; }));
    var shared = (params.get('my') || '').split(',').filter(function (i) { return known.has(i) && !mem.has(i); });
    shared.forEach(function (i) { mem.add(i); });
    if (shared.length) save();
    vm.checked = params.get('mine') === '1';
    function sessions() {  // sessions in page order, each with its saved papers
      var out = [];
      document.querySelectorAll('.pg-sess').forEach(function (b) {
        var ps = [];
        b.querySelectorAll('.card[data-id]').forEach(function (c) {
          if (!mem.has(c.dataset.id)) return;
          var pb = c.querySelector('.badge[href^="#s-P"]');
          ps.push({ title: c.querySelector('h3').textContent, url: c.querySelector('h3 a').href, no: pb ? pb.textContent.split('#').pop().trim() : '' });
        });
        if (ps.length) out.push({ b: b, ps: ps });
      });
      return out;
    }
    function asText(list) {
      return list.map(function (s) {
        var h = s.b.querySelector('h3').cloneNode(true), other = lang() === 'zh' ? 'en' : 'zh';
        h.querySelectorAll('[lang="' + other + '"]').forEach(function (e) { e.remove(); });
        return h.textContent.replace(/\s+/g, ' ').trim() + ' — ' + s.b.querySelector('p.muted').textContent + '\n' +
          s.ps.map(function (p) { return '  - ' + (s.b.dataset.kind === 'poster' && p.no ? '#' + p.no + ' ' : '') + p.title + ' ' + p.url; }).join('\n');
      }).join('\n\n');
    }
    function icsEsc(s) { return s.replace(/\\/g, '\\\\').replace(/([,;])/g, '\\$1').replace(/\n/g, '\\n'); }
    function fold(l) { var o = []; while (l.length > 70) { o.push(l.slice(0, 70)); l = ' ' + l.slice(70); } o.push(l); return o.join('\r\n'); }
    function ics(list) {
      var name = panel.dataset.name, stamp = new Date().toISOString().replace(/[-:]|\.\d+/g, '');
      var lines = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//Embodied AI Radar//Program guide//EN', 'CALSCALE:GREGORIAN'];
      list.forEach(function (s) {
        var w = s.b.dataset.when.split('/'), k = s.b.dataset.kind;
        if (w.length !== 2) return;
        var summary = name + ' ' + (k === 'poster' ? 'Poster session ' : k === 'oral' ? 'Oral ' : 'Spotlight ') + s.b.dataset.sid + (k === 'poster' ? '' : ': ' + s.b.dataset.name);
        var desc = s.ps.map(function (p) { return (k === 'poster' && p.no ? '#' + p.no + ' ' : '') + p.title; }).join('\n');
        lines.push('BEGIN:VEVENT', 'UID:' + s.b.dataset.sid + '-' + w[0] + '@embodied-ai-radar', 'DTSTAMP:' + stamp, 'DTSTART:' + w[0], 'DTEND:' + w[1],
          fold('SUMMARY:' + icsEsc(summary)), fold('LOCATION:' + icsEsc(s.b.dataset.place)), fold('DESCRIPTION:' + icsEsc(desc)), 'END:VEVENT');
      });
      lines.push('END:VCALENDAR');
      return lines.join('\r\n') + '\r\n';
    }
    function link() { return location.origin + location.pathname + '?my=' + Array.from(mem).join(','); }
    function render() {
      document.querySelectorAll('.pg-save').forEach(function (b) {
        var on = mem.has(b.dataset.id);
        b.setAttribute('aria-pressed', on);
        b.innerHTML = on ? '★ ' + bi('Saved', '已保存') : '☆ ' + bi('Save', '保存');
      });
      panel.hidden = !mem.size;
      if (!mem.size) { panel.innerHTML = ''; if (vm.checked) vm.checked = false; return; }
      var list = sessions();
      panel.innerHTML = '<details open><summary>' + bi('My schedule', '我的日程') + ' (' + mem.size + ')</summary>' +
        (shared.length ? '<p class="muted">' + bi('Added ' + shared.length + ' from the shared link.', '已从分享链接添加 ' + shared.length + ' 篇。') + '</p>' : '') +
        list.map(function (s) {
          return '<h4>' + s.b.querySelector('h3').innerHTML + '</h4><p class="muted">' + esc(s.b.querySelector('p.muted').textContent) + '</p><ul>' + s.ps.map(function (p) {
            return '<li>' + (s.b.dataset.kind === 'poster' && p.no ? '<b>#' + esc(p.no) + '</b> ' : '') + '<a href="' + esc(p.url) + '" rel="noopener">' + esc(p.title) + '</a></li>';
          }).join('') + '</ul>';
        }).join('') +
        '<div class="pg-acts"><button type="button" data-a="link">' + bi('Copy share link', '复制分享链接') + '</button><button type="button" data-a="text">' + bi('Copy as text', '复制为文本') + '</button><button type="button" data-a="ics">' + bi('Calendar file (.ics)', '日历文件 (.ics)') + '</button><button type="button" data-a="clear">' + bi('Clear', '清空') + '</button></div></details>';
    }
    cards.forEach(function (c) {
      var b = document.createElement('button');
      b.type = 'button'; b.className = 'pg-save'; b.dataset.id = c.dataset.id;
      c.querySelector('.meta').appendChild(b);
    });
    document.addEventListener('click', function (ev) {
      var b = ev.target.closest && ev.target.closest('.pg-save');
      if (b) {
        if (mem.has(b.dataset.id)) mem.delete(b.dataset.id); else mem.add(b.dataset.id);
        shared = []; save(); render(); refilter();
        return;
      }
      var a = ev.target.closest && ev.target.closest('#pg-my button[data-a]');
      if (!a) return;
      var act = a.dataset.a, list = sessions();
      if (act === 'clear') {
        if (!confirm(lang() === 'zh' ? '清空我的日程？' : 'Clear your schedule?')) return;
        mem.clear(); shared = []; save(); render(); refilter();
      } else if (act === 'ics') {
        var u = URL.createObjectURL(new Blob([ics(list)], { type: 'text/calendar;charset=utf-8' })), l = document.createElement('a');
        l.href = u; l.download = vf.dataset.store + '-my-schedule.ics'; document.body.appendChild(l); l.click(); l.remove();
        setTimeout(function () { URL.revokeObjectURL(u); }, 1000);
      } else if (navigator.clipboard) {
        navigator.clipboard.writeText(act === 'link' ? link() : asText(list)).then(function () {
          var old = a.innerHTML;
          a.textContent = lang() === 'zh' ? '已复制 ✓' : 'Copied ✓';
          setTimeout(function () { a.innerHTML = old; }, 1500);
        });
      }
    });
    render();
    return mem;
  }

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
  function venueBadge(v) {  // links to venues/<slug>.html when the build made a page for this venue+year
    if (!v) return '';
    var m = /^(.+?) ((?:19|20)\d\d)\b/.exec(String(v).trim()), k = m ? m[1] + ' ' + m[2] : null;
    var slug = k && data && data.venues ? data.venues[k] : null;
    return slug ? ' <a class="badge venue" href="venues/' + esc(slug) + '.html">' + esc(v) + '</a>' : ' <span class="badge venue">' + esc(v) + '</span>';
  }
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
  // Chinese query expansion: feed papers are English-only, so common Chinese terms are
  // mapped to English substrings (matched against the lowercased index text). A Chinese
  // token without spaces ("人形机器人强化学习") is split greedily into known terms, each ANDed.
  var ZH = {
    '具身智能': ['embodied'], '具身': ['embodied'], '机器人': ['robot'],
    '机械臂': [' arm', 'manipulator'], '操作': ['manipulat'], '操控': ['manipulat'],
    '灵巧手': ['dexter', ' hand'], '灵巧操作': ['dexter'], '灵巧': ['dexter'], '抓取': ['grasp'],
    '视触觉': ['visuotactile', 'visual-tactile', 'visuo-tactile'], '触觉': ['tactile', 'touch'],
    '人形机器人': ['humanoid'], '人形': ['humanoid'], '四足': ['quadruped', 'legged'], '足式': ['legged'],
    '运动控制': ['locomotion'], '步态': ['gait', 'locomotion'], '跑酷': ['parkour'], '全身控制': ['whole-body', 'whole body'],
    '双臂': ['bimanual', 'dual-arm'], '移动操作': ['mobile manipulation'], '导航': ['navigat'],
    '视觉语言导航': ['vision-and-language navigation', 'vision-language navigation', 'vln'],
    '世界动作模型': ['world action model', ' wam'], '世界模型': ['world model'], '视频生成': ['video generation'],
    '扩散策略': ['diffusion polic'], '扩散': ['diffusion'], '流匹配': ['flow matching', 'flow-matching'],
    '离线强化学习': ['offline rl', 'offline reinforcement'], '强化学习': ['reinforcement', ' rl'],
    '模仿学习': ['imitation', 'behavior cloning', 'behaviour cloning'], '行为克隆': ['behavior cloning', 'behaviour cloning'],
    '大语言模型': ['llm', 'language model'], '大模型': ['llm', 'language model', 'foundation model'],
    '基础模型': ['foundation model'], '视觉语言模型': ['vlm', 'vision-language model', 'vision language model'],
    '视觉语言动作': ['vla', 'vision-language-action'], '多模态': ['multimodal', 'multi-modal'],
    '虚实迁移': ['sim-to-real', 'sim2real'], '仿真': ['simulat'], '数据集': ['dataset'], '基准': ['benchmark'],
    '评测': ['benchmark', 'evaluat'], '遥操作': ['teleop'], '运动规划': ['motion planning'], '路径规划': ['path planning'],
    '轨迹优化': ['trajectory optimization'], '轨迹': ['trajector'], '模型预测控制': ['mpc', 'model predictive'],
    '安全': ['safe'], '点云': ['point cloud'], '三维重建': ['3d reconstruction', 'reconstruct'], '重建': ['reconstruct'],
    '建图': ['mapping'], '定位': ['locali'], '位姿估计': ['pose estimation'], '位姿': ['pose'], '深度估计': ['depth estimation'],
    '分割': ['segment'], '检测': ['detect'], '标定': ['calibrat'], '自动驾驶': ['driving', 'autonomous vehicle'],
    '无人机': ['drone', 'uav', 'aerial', 'quadrotor'], '水下': ['underwater'], '软体': ['soft robot'],
    '人机交互': ['human-robot interaction', 'hri'], '多机器人': ['multi-robot'], '泛化': ['generaliz'], '零样本': ['zero-shot'],
    '推理': ['reasoning'], '规划': ['plan'], '视频': ['video'], '语言': ['language'], '开源': ['open-source', 'open source'],
    '低成本': ['low-cost', 'low cost'], '硬件': ['hardware'], '传感器': ['sensor'], '力控': ['force control', 'impedance'],
    '阻抗控制': ['impedance'], '预训练': ['pretrain', 'pre-train'], '后训练': ['post-train'], '微调': ['fine-tun'],
    '跨具身': ['cross-embodiment'], '长时程': ['long-horizon'], '可变形': ['deformable'], '布料': ['cloth'],
    '装配': ['assembl'], '倒水': ['pour'], '家务': ['household'], '里程计': ['odometry'], '激光雷达': ['lidar'], '综述': ['survey']
  };
  var ZH_KEYS = Object.keys(ZH).sort(function (a, b) { return b.length - a.length; });
  var CJK = /[㐀-鿿]/, GENERIC = ['机器人', '具身', '具身智能'];
  // Returns a list of groups; an item matches when, for every group, it contains any string in it.
  function queryGroups(text) {
    var groups = [];
    text.toLowerCase().split(/\s+/).filter(Boolean).forEach(function (t) {
      if (!CJK.test(t)) { groups.push([t]); return; }
      if (ZH[t]) { groups.push([t].concat(ZH[t])); return; }
      var found = [], i = 0;
      while (i < t.length) {
        var k = null;
        for (var j = 0; j < ZH_KEYS.length; j++) if (t.substr(i, ZH_KEYS[j].length) === ZH_KEYS[j]) { k = ZH_KEYS[j]; break; }
        if (k) { found.push([k].concat(ZH[k])); i += k.length; } else i++;
      }
      // Generic words ("机器人", "具身") only narrow results when nothing more specific was typed.
      var specific = found.filter(function (g) { return GENERIC.indexOf(g[0]) < 0; });
      if (specific.length) found = specific;
      if (found.length) groups = groups.concat(found); else groups.push([t]);
    });
    return groups;
  }
  window.__radarQueryGroups = queryGroups;
  function topicChips(tp) {
    return (tp || []).map(function (t) { var n = data.topics[t]; return n ? '<a class="chip topic" href="topics/' + t + '.html">' + esc(n[lang() === 'zh' ? 1 : 0]) + '</a>' : ''; }).join('');
  }
  function embChips(em) {
    return (em || []).map(function (m) { var n = (data.emb || {})[m]; return n ? '<span class="chip emb">' + esc(n[lang() === 'zh' ? 1 : 0]) + '</span>' : ''; }).join('');
  }
  function hfLink(id, u) {
    return u ? ' · <a class="hf" href="https://huggingface.co/papers/' + esc(id) + '" title="Upvotes on Hugging Face Daily Papers">▲ ' + esc(u) + ' HF</a>' : '';
  }
  function card(it) {
    if (it.k === 'c') {
      var links = [];
      if (it.a) links.push('<a href="https://arxiv.org/abs/' + esc(it.a) + '">' + (lang() === 'zh' ? '论文' : 'Paper') + '</a>');
      if (it.c) links.push('<a href="' + esc(it.c) + '">' + (lang() === 'zh' ? '代码' : 'Code') + '</a>');
      if (it.p) links.push('<a href="' + esc(it.p) + '">' + (lang() === 'zh' ? '项目页' : 'Project') + '</a>');
      links.push('<a class="perma" href="e/' + esc(it.id) + '.html">' + (lang() === 'zh' ? '详情' : 'Details') + '</a>');
      if (it.u && it.a) links.push(hfLink(it.a, it.u).slice(3));
      return '<article class="card"><div class="meta"><span class="badge">' + esc(it.ty) + '</span> ' + esc(it.y) + ' · ' + esc(it.o) + venueBadge(it.v) + (it.h ? ' <span class="star">★</span>' : '') +
        '</div><h3><a href="' + esc(it.l) + '">' + esc(it.t) + '</a></h3><p class="take">' + esc(lang() === 'zh' ? it.zh : it.en) +
        '</p><div class="links">' + links.join(' · ') + (it.s != null ? ' <span class="gh" title="GitHub stars">★ ' + (it.s >= 1000 ? (it.s / 1000).toFixed(1).replace(/\.0$/, '') + 'k' : it.s) + '</span>' : '') + '</div><div class="chips">' + topicChips(it.tp) + embChips(it.em) + '</div></article>';
    }
    return '<article class="card feed"><div class="meta"><span class="badge">arXiv ' + esc(it.pc) + '</span> ' + esc(it.d) + (it.c ? ' <span class="badge code">code</span>' : '') + venueBadge(it.v) +
      '</div><h3><a href="https://arxiv.org/abs/' + esc(it.id) + '">' + esc(it.t) + '</a></h3><p class="authors">' + esc(it.au) +
      '</p><div class="links"><a href="https://arxiv.org/pdf/' + esc(it.id) + '">PDF</a>' + (it.c ? ' · <a href="' + esc(it.c) + '">' + (lang() === 'zh' ? '代码' : 'Code') + '</a>' + (it.s != null ? ' <span class="gh" title="GitHub stars">★ ' + (it.s >= 1000 ? (it.s / 1000).toFixed(1).replace(/\.0$/, '') + 'k' : it.s) + '</span>' : '') : '') +
      (it.pj ? ' · <a href="' + esc(it.pj) + '">' + (lang() === 'zh' ? '项目页' : 'Project') + '</a>' : '') + hfLink(it.id, it.u) +
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
      var groups = queryGroups(q.value);
      var res = data.items.filter(function (it) {
        if (fTopic.value && (it.tp || []).indexOf(fTopic.value) < 0) return false;
        if (fEmb && fEmb.value && (it.em || []).indexOf(fEmb.value) < 0) return false;
        if (fVen && fVen.value && !(it.v && (fVen.value === '*' || it.v === fVen.value || String(it.v).indexOf(fVen.value + ' ') === 0))) return false;
        if (fKind.value && it.k !== fKind.value) return false;
        if (fCode.checked && !it.c) return false;
        for (var i = 0; i < groups.length; i++) {
          var g = groups[i], hit = false;
          for (var j = 0; j < g.length && !hit; j++) hit = it._s.indexOf(g[j]) >= 0;
          if (!hit) return false;
        }
        return true;
      });
      var mode = fSort ? fSort.value : '';
      res.sort(function (a, b) {
        if (mode === 'stars') { var sa = a.s == null ? -1 : a.s, sb = b.s == null ? -1 : b.s; if (sa !== sb) return sb - sa; }
        if (mode === 'hf') { var ua = a.u || 0, ub = b.u || 0; if (ua !== ub) return ub - ua; }
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
