"""Sürüm 13.12 (HUSER ortak dil, kararlar madde 15 ve 17):
(1) window.confirm → ortak onay penceresi (await window.__onay). Onay gerektiren 21 işlem; zaman uyumlu işleyiciler async yapılır.
(2) window.alert → ortak bilgi penceresi (beklemeyen; mesaj 112 düzeninde görünür).
(3) Düz <select> kutuları ortak seçim düğmesi + paneline dönüşür. Asıl kutu gizli kalır; seçim yerel değer yazıcısıyla
    kutuya yazılıp 'change' tetiklenir → React onChange aynen çalışır. React seçimi kodla değiştirince düğme güncellenir.
Pencere görünümü 112 kit onayla/bildir ile aynı: koyu örtü, mavi (silmede kırmızı) başlık, Vazgeç / Evet; Enter = evet (silmede değil), Esc = vazgeç.
teknik_brifing_yamasi.py'den SONRA."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__ortakDil" not in js


def bir(a, b, n=1):
    global js
    assert js.count(a) == n, (js.count(a), a[:90]); js = js.replace(a, b)


# (1) zaman uyumlu onay işleyicileri async olur
for a in ['onClick:()=>{var e,t;const r=null===(e=Ee.find(e=>e.id===y))',
          'onClick:()=>{window.confirm("Seçili istasyonlar',
          'onClick:()=>{window.confirm(`"${e.ad}" silinsin mi?`)',
          'onClick:()=>{window.confirm("Tablo varsayılan 45 branşa',
          'onClick:()=>{window.confirm("Bu cihazda yönetici bölümü',
          'onClick:()=>{window.confirm("Eşikler varsayılan']:
    bir(a, a.replace('onClick:()=>', 'onClick:async()=>'))
bir('function __ilDegistir(h) {', 'async function __ilDegistir(h) {')
bir('onChange: x => { const h = x.target.value; __ilDegistir(h) || setIl(il) }',
    'onChange: async x => { const h = x.target.value; (await __ilDegistir(h)) || setIl(il) }')
bir('const sil = f => window.confirm(', 'const sil = async f => window.confirm(')
bir('window.confirm(', 'await window.__onay(', 21)

# (2)+(3) ortak pencereler ve seçim paneli — paketin başına
on = r'''/* HUSER 13.12 — ortak dil: onay / bilgi pencereleri ve tek seçim paneli */
(function __ortakDil(){
  if (window.__onay) return;
  var css = document.createElement("style");
  css.textContent = ".hod-ort{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:2147483000;display:flex;align-items:center;justify-content:center;padding:16px}"
   + ".hod-kut{background:#fff;max-width:448px;width:100%;box-shadow:0 20px 50px rgba(0,0,0,.3);font-family:'IBM Plex Sans',-apple-system,'Segoe UI',sans-serif}"
   + ".hod-bas{padding:14px 20px;color:#fff;background:#0055a4;font-size:16px;font-weight:700}.hod-bas.k{background:#dc2626}"
   + ".hod-gov{padding:20px;font-size:14px;color:#334155;white-space:pre-line;line-height:1.6;max-height:60vh;overflow:auto}"
   + ".hod-alt{padding:12px 20px;background:#f8fafc;border-top:1px solid #e2e8f0;display:flex;justify-content:flex-end;gap:8px}"
   + ".hod-alt button{font:inherit;font-size:12px;font-weight:600;padding:6px 12px;cursor:pointer;border:1px solid #cbd5e1;background:#fff;color:#334155;border-radius:0}"
   + ".hod-alt button.a{background:#0055a4;border-color:#0055a4;color:#fff}.hod-alt button.a:hover{background:#004080}.hod-alt button.k{background:#dc2626;border-color:#dc2626;color:#fff}"
   + ".hod-sbtn{display:inline-flex!important;align-items:center;justify-content:space-between;gap:8px;cursor:pointer;text-align:left;min-width:0}"
   + ".hod-sbtn>span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;min-width:0}.hod-sbtn>i{font-style:normal;font-size:10px;opacity:.7;flex:none}"
   + ".hod-sbtn:disabled{opacity:.6;cursor:not-allowed}.hod-sbtn.acik{border-color:#0055a4!important;box-shadow:0 0 0 2px rgba(0,85,164,.25)!important}"
   + ".hod-pop{position:fixed;z-index:2147482000;background:var(--bg-card,#fff);color:var(--text-primary,#0f172a);border:1px solid var(--border-subtle,#cbd5e1);border-radius:12px;box-shadow:0 12px 32px rgba(15,23,42,.25);padding:8px;display:flex;flex-direction:column;gap:6px;overflow:auto;font-size:13px}"
   + ".hod-pop input{width:100%;box-sizing:border-box;height:34px;padding:0 10px;border:1px solid var(--border-subtle,#cbd5e1);background:transparent;color:inherit;font:inherit;outline:none}"
   + ".hod-lis{border:1px solid var(--border-subtle,#e2e8f0)}.hod-lis button{display:flex;align-items:center;gap:9px;width:100%;text-align:left;padding:7px 10px;border:0;border-bottom:1px solid var(--border-subtle,#e2e8f0);background:transparent;color:inherit;font:inherit;font-size:12.5px;cursor:pointer;line-height:1.3}"
   + ".hod-lis button:last-child{border-bottom:0}.hod-lis button:hover,.hod-lis button:focus{background:var(--bg-hover,#f1f5f9);outline:none}.hod-lis button:disabled{opacity:.45;cursor:not-allowed}"
   + ".hod-lis button i{width:13px;height:13px;border-radius:50%;border:1px solid #94a3b8;flex:none}.hod-lis button.sec{font-weight:700;color:#0055a4}.hod-lis button.sec i{background:#0055a4;border-color:#0055a4;box-shadow:inset 0 0 0 2px #fff}";
  (document.head || document.documentElement).appendChild(css);
  var TEH = /sil|kaldır|sıfırla|geri alınamaz|SİL|KALDIR|SIFIRLA|TÜM/;
  function pencere(metin, onayMi) {
    return new Promise(function (coz) {
      var teh = onayMi && TEH.test(String(metin || "")), o = document.createElement("div");
      o.className = "hod-ort"; o.setAttribute("data-testid", onayMi ? "onay-pencere" : "bilgi-pencere");
      o.innerHTML = '<div class="hod-kut" role="alertdialog" aria-modal="true"><div class="hod-bas' + (teh ? " k" : "") + '"></div><div class="hod-gov"></div><div class="hod-alt"></div></div>';
      o.querySelector(".hod-bas").textContent = onayMi ? (teh ? "Dikkat" : "Onay") : "Bilgi";
      o.querySelector(".hod-gov").textContent = String(metin == null ? "" : metin);
      var alt = o.querySelector(".hod-alt");
      function dug(y, c, v, t) { var b = document.createElement("button"); b.type = "button"; b.className = c; b.textContent = y; b.setAttribute("data-testid", t); b.onclick = function () { bit(v) }; alt.appendChild(b); return b }
      function tus(e) { if (e.key === "Escape") { e.preventDefault(); e.stopPropagation(); bit(!onayMi) } else if (e.key === "Enter" && !teh) { e.preventDefault(); e.stopPropagation(); bit(!0) } }
      function bit(v) { document.removeEventListener("keydown", tus, !0); o.remove(); coz(v) }
      var odak;
      if (onayMi) { var h = dug("Vazgeç", "", !1, "onay-hayir"), ev = dug(teh ? "Evet, devam et" : "Evet", teh ? "k" : "a", !0, "onay-evet"); odak = teh ? h : ev }
      else odak = dug("Tamam", "a", !0, "bilgi-tamam");
      if (onayMi) o.addEventListener("mousedown", function (e) { if (e.target === o) bit(!1) });
      document.addEventListener("keydown", tus, !0);
      document.body.appendChild(o); setTimeout(function () { odak.focus() }, 0);
    });
  }
  window.__onay = function (m) { return pencere(m, !0) };
  window.__bildir = function (m) { return pencere(m, !1) };
  window.alert = function (m) { pencere(m, !1) };

  /* tek seçim paneli */
  var SP = HTMLSelectElement.prototype, OP = HTMLOptionElement.prototype,
      dV = Object.getOwnPropertyDescriptor(SP, "value"), dI = Object.getOwnPropertyDescriptor(SP, "selectedIndex"), dS = Object.getOwnPropertyDescriptor(OP, "selected");
  var acik = null;
  function kapat() { if (acik) { acik.pop.remove(); acik.btn.classList.remove("acik"); acik = null } }
  function boya(sel) { var b = sel.__hodBtn; if (!b) return; var o = sel.options[dI.get.call(sel)]; b.firstChild.textContent = o ? o.text : "—"; b.title = o ? o.text : ""; b.disabled = sel.disabled }
  function sonra(sel) { if (sel && sel.__hodBtn && !sel.__hodBekle) { sel.__hodBekle = 1; Promise.resolve().then(function () { sel.__hodBekle = 0; boya(sel) }) } }
  Object.defineProperty(SP, "value", { configurable: !0, enumerable: dV.enumerable, get: dV.get, set: function (v) { dV.set.call(this, v); sonra(this) } });
  Object.defineProperty(SP, "selectedIndex", { configurable: !0, enumerable: dI.enumerable, get: dI.get, set: function (v) { dI.set.call(this, v); sonra(this) } });
  Object.defineProperty(OP, "selected", { configurable: !0, enumerable: dS.enumerable, get: dS.get, set: function (v) { dS.set.call(this, v); sonra(this.parentNode && this.parentNode.tagName === "SELECT" ? this.parentNode : this.closest && this.closest("select")) } });
  var katla = function (v) { return String(v || "").toLocaleLowerCase("tr-TR") };
  function ac(sel, btn) {
    kapat();
    var ops = Array.prototype.slice.call(sel.options), cok = ops.length > 12, pop = document.createElement("div"), si = dI.get.call(sel);
    pop.className = "hod-pop"; pop.setAttribute("data-testid", "secim-panel");
    var h = (cok ? '<input type="search" placeholder="Ara…" autocomplete="off">' : "") + '<div class="hod-lis"></div>';
    pop.innerHTML = h; var lis = pop.querySelector(".hod-lis");
    ops.forEach(function (o, i) { var b = document.createElement("button"); b.type = "button"; b.setAttribute("data-i", i); b.className = i === si ? "sec" : ""; b.disabled = o.disabled; b.setAttribute("data-ara", katla(o.text)); b.innerHTML = "<i></i><span></span>"; b.lastChild.textContent = o.text; lis.appendChild(b) });
    document.body.appendChild(pop); acik = { pop: pop, btn: btn }; btn.classList.add("acik");
    var r = btn.getBoundingClientRect(), w = Math.min(Math.max(r.width, 220), 440, innerWidth - 16);
    pop.style.width = w + "px"; pop.style.left = Math.max(8, Math.min(r.left, innerWidth - w - 8)) + "px";
    var alt = innerHeight - r.bottom - 12, ust = r.top - 12;
    if (alt < 240 && ust > alt) { pop.style.bottom = (innerHeight - r.top + 4) + "px"; pop.style.maxHeight = Math.min(420, ust) + "px" }
    else { pop.style.top = (r.bottom + 4) + "px"; pop.style.maxHeight = Math.min(420, Math.max(160, alt)) + "px" }
    function sec(i) {
      kapat(); btn.focus(); if (i === dI.get.call(sel)) return;
      dV.set.call(sel, ops[i].value); boya(sel);
      sel.dispatchEvent(new Event("input", { bubbles: !0 })); sel.dispatchEvent(new Event("change", { bubbles: !0 }));
    }
    pop.addEventListener("mousedown", function (e) { e.stopPropagation() });
    pop.addEventListener("click", function (e) { var b = e.target.closest("[data-i]"); if (b && !b.disabled) sec(+b.getAttribute("data-i")) });
    var ara = pop.querySelector("input");
    pop.addEventListener("keydown", function (e) {
      var g = Array.prototype.filter.call(lis.querySelectorAll("[data-i]"), function (x) { return x.style.display !== "none" && !x.disabled }), k = g.indexOf(document.activeElement);
      if (e.key === "ArrowDown" || e.key === "ArrowUp") { e.preventDefault(); var n = g[Math.max(0, Math.min(g.length - 1, k + (e.key === "ArrowDown" ? 1 : -1)))]; n && n.focus() }
      else if (e.key === "Enter" && e.target === ara) { e.preventDefault(); g.length && sec(+g[0].getAttribute("data-i")) }
      else if (e.key === "Escape") { e.preventDefault(); e.stopPropagation(); kapat(); btn.focus() }
    });
    if (ara) { ara.addEventListener("input", function () { var q = katla(ara.value).trim(); lis.querySelectorAll("[data-i]").forEach(function (x) { x.style.display = !q || x.getAttribute("data-ara").indexOf(q) >= 0 ? "" : "none" }) }); ara.focus() }
    else { var x = lis.querySelector(".sec") || lis.querySelector("[data-i]"); if (x) { x.focus(); x.scrollIntoView({ block: "nearest" }) } }
  }
  function kur(sel) {
    if (sel.__hodBtn || sel.multiple || sel.hasAttribute("data-duz")) return;
    var b = document.createElement("button"); b.type = "button";
    b.className = (sel.className || "") + " hod-sbtn"; b.style.cssText = sel.style.cssText;
    var t = sel.getAttribute("data-testid"); if (t) b.setAttribute("data-testid", t + "-dugme");
    b.innerHTML = "<span></span><i>▾</i>";
    sel.__hodBtn = b; sel.style.display = "none"; sel.insertAdjacentElement("afterend", b); boya(sel);
    b.addEventListener("mousedown", function (e) { e.stopPropagation() });
    b.addEventListener("click", function () { if (acik && acik.btn === b) kapat(); else ac(sel, b) });
    new MutationObserver(function () { boya(sel) }).observe(sel, { childList: !0, subtree: !0, characterData: !0, attributes: !0, attributeFilter: ["disabled"] });
  }
  function tara(k) { if (k.tagName === "SELECT") kur(k); else if (k.querySelectorAll) k.querySelectorAll("select").forEach(kur) }
  function temizle(k) { if (k.tagName === "SELECT") { if (k.__hodBtn && !k.isConnected) { k.__hodBtn.remove() } } else if (k.querySelectorAll) k.querySelectorAll("select").forEach(temizle) }
  function basla() {
    tara(document.body);
    new MutationObserver(function (ms) { ms.forEach(function (m) { m.addedNodes.forEach(function (n) { n.nodeType === 1 && tara(n) }); m.removedNodes.forEach(function (n) { n.nodeType === 1 && temizle(n) }) }) }).observe(document.body, { childList: !0, subtree: !0 });
    document.addEventListener("mousedown", kapat);
    document.addEventListener("scroll", function (e) { if (acik && !acik.pop.contains(e.target)) kapat() }, !0);
    addEventListener("resize", kapat);
  }
  document.body ? basla() : document.addEventListener("DOMContentLoaded", basla);
})();
'''
js = on + js

yeni = base64.b64encode(js.encode("utf-8")).decode("ascii")
html = html[:m.start(1)] + yeni + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html)
print("ortak_dil_yamasi: confirm 21 → __onay, alert → __bildir, select → ortak panel")
