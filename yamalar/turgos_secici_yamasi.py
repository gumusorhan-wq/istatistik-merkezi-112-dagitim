"""Sürüm 12.50: (1) TÜR-GÖS çeyrek/ay seçimi tarayıcı açılır listesi yerine ortak ay ızgarası (yıllar açılır/kapanır).
(2) Çok aylı dönem açıkken TÜR-GÖS'te dönemin son ayı birleşik sonuçtan değil, o ayın kendisinden alınır (önceden 10 ayın toplamı görünebiliyordu).
(3) Çok aylı dönemde sunucuda hazır özeti olan ay doğrudan sunucudan alınır; cihazdaki tam veri okunmaz (bekleme kısalır).
ozet_hazir_yamasi.py'den SONRA."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "sks-izgara" not in js
def bir(a, b):
    global js
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)

# (2) dönem açıkken cm için birleşik sonuç kullanılmasın
bir('let T = ym === cm && results ? (results[sc] || results.ashi) : await __SUNUM.ayKapsam(ym, sc, cm ? { ym: cm, results } : null);',
    'const __dn = !!window.__DONEM; let T = ym === cm && results && !__dn ? (results[sc] || results.ashi) : await __SUNUM.ayKapsam(ym, sc, cm && !__dn ? { ym: cm, results } : null);')

# (1) ızgara seçici
bir('[ac, setAc] = R.useState(""), [busy, setBusy] = R.useState(!1);',
    '[ac, setAc] = R.useState(""), [busy, setBusy] = R.useState(!1), [izAc, setIzAc] = R.useState(!1), [izY, setIzY] = R.useState(null);')
eski_sel = ('mod === "3ay" ? E("select", { className: "input", value: q, onChange: e => setQ(e.target.value), "data-testid": "sks-ceyrek", style: { fontSize: 12.5, padding: "6px 10px", maxWidth: 260 } }, ceyrekler.map(x => E("option", { key: x, value: x }, qAd(x))))\n'
            '          : E("select", { className: "input", value: ay, onChange: e => setAy(e.target.value), "data-testid": "sks-ay", style: { fontSize: 12.5, padding: "6px 10px", maxWidth: 200 } }, [...tumAy].reverse().map(x => E("option", { key: x, value: x }, Du(x)))),')
yeni_sel = '__izgara(),'
bir(eski_sel, yeni_sel)

izgara = r'''
  const __AYK = ["Oca", "Şub", "Mar", "Nis", "May", "Haz", "Tem", "Ağu", "Eyl", "Eki", "Kas", "Ara"], __QK = ["Oca–Mar", "Nis–Haz", "Tem–Eyl", "Eki–Ara"];
  const __izgara = () => {
    const yillar = [...new Set(tumAy.map(x => x.slice(0, 4)))].sort().reverse(), secY = (mod === "3ay" ? q : ay || "").slice(0, 4);
    const acik = izY || new Set([secY || yillar[0]]);
    const hucre = (k, etiket, var_, secili, sec) => E("button", { key: k, type: "button", disabled: !var_, onClick: () => { sec(); setIzAc(!1) }, "data-testid": "sks-izgara-" + k,
      style: { fontSize: 12.5, padding: "7px 4px", borderRadius: 8, cursor: var_ ? "pointer" : "default", border: "1px solid " + (secili ? "var(--turquoise, #17a2a8)" : "var(--border-subtle, rgba(148,163,184,.35))"),
        background: secili ? "var(--turquoise, #17a2a8)" : "transparent", color: secili ? "#fff" : var_ ? "var(--text-primary)" : "var(--text-muted)", opacity: var_ ? 1 : .45, fontWeight: secili ? 700 : 500 } }, etiket);
    const yazi = mod === "3ay" ? (q ? qAd(q) : "Çeyrek seçin") : (ay ? Du(ay) : "Ay seçin");
    return E("div", { style: { position: "relative" } },
      E("button", { type: "button", className: "input", onClick: () => setIzAc(!izAc), "data-testid": mod === "3ay" ? "sks-ceyrek" : "sks-ay",
        style: { fontSize: 12.5, padding: "6px 12px", cursor: "pointer", display: "flex", alignItems: "center", gap: 6, whiteSpace: "nowrap", fontWeight: 600 } }, "📅 " + yazi + " ▾"),
      izAc && E("div", { onClick: () => setIzAc(!1), style: { position: "fixed", inset: 0, zIndex: 1999 } }),
      izAc && E("div", { "data-testid": "sks-izgara", style: { position: "absolute", right: 0, top: "calc(100% + 6px)", zIndex: 2000, width: 300, padding: 12, borderRadius: 12, background: "var(--bg-card, #fff)", border: "1px solid var(--border-subtle, rgba(148,163,184,.35))", boxShadow: "0 10px 30px rgba(0,0,0,.18)" } },
        yillar.map(y => { const ac = acik.has(y);
          return E("div", { key: y, style: { marginBottom: ac ? 10 : 4 } },
            E("button", { type: "button", "data-testid": "sks-izgara-yil-" + y, onClick: () => { const b = new Set(acik); b.has(y) ? b.delete(y) : b.add(y); setIzY(b) },
              style: { fontSize: 13, fontWeight: 700, background: "transparent", border: 0, cursor: "pointer", color: "var(--text-primary)", padding: "2px 0", marginBottom: 6 } }, (ac ? "▾ " : "▸ ") + y),
            ac && E("div", { style: { display: "grid", gridTemplateColumns: mod === "3ay" ? "repeat(2,1fr)" : "repeat(4,1fr)", gap: 6 } },
              mod === "3ay" ? [1, 2, 3, 4].map(n => { const k = y + "-Q" + n; return hucre(k, n + ". çeyrek · " + __QK[n - 1], ceyrekler.includes(k), q === k, () => setQ(k)) })
                : __AYK.map((t, i) => { const k = y + "-" + String(i + 1).padStart(2, "0"); return hucre(k, t, tumAy.includes(k), ay === k, () => setAy(k)) })))
        })))
  };
'''
a = '  const yms = mod === "ay" ? (ay ? [ay] : []) : qAylar(q);'
bir(a, izgara + a)

# (3) hazır özet varsa önce sunucudan
bir('for(let i=0;i<L.length;i++){const ym=L[i],f=uzak.get(ym);let R=null;ilerleme(`${Du(ym)} özeti hazırlanıyor (${i+1}/${L.length})…`);\n    try{const r=',
    'for(let i=0;i<L.length;i++){const ym=L[i],f=uzak.get(ym);let R=null;ilerleme(`${Du(ym)} özeti hazırlanıyor (${i+1}/${L.length})…`);\n'
    '    if(f&&f.ozetHazir)try{const p=await __ORT.paketAc(new Uint8Array(await H.arsiv.indir(il,ym,{ozet:!0})));if(p&&p.ym===ym&&51===p.schema&&__ozGecerli(p.results,p.fp,matFp)){R=p.results;cols=cols||p.cols;ah=ah||p.allHeaders;satir+=p.rawRowCount||0}}catch(e){console.warn("[özet] hazır sunucu özeti alınamadı",ym,e)}\n'
    '    if(!R)try{const r=')
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("TURGOS_SECICI_OK")
