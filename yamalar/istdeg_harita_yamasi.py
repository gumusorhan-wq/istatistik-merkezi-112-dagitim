"""Sürüm 12.40:
- Modül 5 › İstasyon Değerlendirme tablosunun altında seçili (aramayla süzülmüş) istasyonların TOPLAM / ORTALAMA satırı
  (vaka, nakil, KM toplam; günlük ortalamalar ortalama; vaka başına meşguliyet/KM ağırlıklı).
- Modül 5 › Harita: mahalle/ilçe seçilince (öneri listesi ya da Enter) haritada yalnız o mahallenin/ilçenin vakaları kalır;
  sol altta "Yalnız: … — Tümünü göster" kutusu; arama kutusu boşaltılınca da tümü geri gelir."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__IDTOP" not in js
def bir(a, b):
    global js
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)

# --- İstasyon Değerlendirme toplam satırı
bir('function ph(e){let{rows:t,hasMesguliyetKolonu:r}=e;',
    'function __IDTOP(r,fz,st){if(!r||r.length<2)return null;const S=k=>r.reduce((e,t)=>e+(Number(t[k])||0),0),O=k=>Math.round(S(k)/r.length*10)/10,tv=S("toplamVaka"),km=Math.round(10*S("toplamKm"))/10,'
    'vm=tv?Math.round(r.reduce((e,t)=>e+(Number(t.vakaBasinaMesg)||0)*(Number(t.toplamVaka)||0),0)/tv):0,vk=tv?Math.round(km/tv*10)/10:0,'
    'td=(c,x)=>(0,a().jsx)("td",{style:{...st(x),fontWeight:700,whiteSpace:x?"normal":"nowrap",borderTop:"2px solid rgba(23,162,168,0.5)"},children:c});'
    'return(0,a().jsx)("tfoot",{children:(0,a().jsxs)("tr",{"data-testid":"istasyon-degerlendirme-toplam",style:{position:"sticky",bottom:0,background:"var(--bg-card)"},children:['
    'td(["TOPLAM / ORTALAMA (",r.length," istasyon)"],!0),td("",!0),td(tv.toLocaleString("tr-TR")),td(O("gunlukOrtVaka").toLocaleString("tr-TR")),'
    'td(S("hstArasi").toLocaleString("tr-TR")),td(O("gunlukOrtNakil").toLocaleString("tr-TR")),td(fz(O("gunlukOrtMesg"))),td(fz(vm)),'
    'td([km.toLocaleString("tr-TR")," km"]),td([O("gunlukOrtKm").toLocaleString("tr-TR")," km"]),td([vk.toLocaleString("tr-TR")," km"])]})})}'
    'function ph(e){let{rows:t,hasMesguliyetKolonu:r}=e;')
bir('(null!==(s=e.vakaBasinaKm)&&void 0!==s?s:0).toLocaleString("tr-TR")," km"]})]},e.istasyon)})})]})})]})}function mh(){',
    '(null!==(s=e.vakaBasinaKm)&&void 0!==s?s:0).toLocaleString("tr-TR")," km"]})]},e.istasyon)})}),__IDTOP(n.filtered,i,mh)]})})]})}function mh(){')

# --- Harita: seçilen mahalle/ilçe süzgeci
bir('function oh(e){let{vakaKoordinatlari:t}=e;',
    'function oh(e){let{vakaKoordinatlari:__t0}=e;const[__mf,__smf]=(0,s().useState)(null),t=(0,s().useMemo)(()=>__mf&&__t0?__t0.filter(__mf.f):__t0,[__t0,__mf]);')
bir('C=(0,s().useMemo)(()=>{const e=new Map;for(const r of t||[]){', 'C=(0,s().useMemo)(()=>{const e=new Map;for(const r of __t0||[]){')
bir('lon:e.lons.reduce((e,t)=>e+t,0)/e.lons.length}))},[t]);function M(e)', 'lon:e.lons.reduce((e,t)=>e+t,0)/e.lons.length}))},[__t0]);function M(e)')
bir('const a=(t||[]).filter(e=>M(e.mahalle).includes(n)||M(e.ilce).includes(n));if(a.length)if(x(!1),T(!1),',
    'const __p=e=>M(e.mahalle).includes(n)||M(e.ilce).includes(n),a=(__t0||[]).filter(__p);if(a.length)if(__smf({f:__p,ad:k.trim()}),x(!1),T(!1),')
bir('onClick:()=>(e=>{const t=i.current;t&&(t.setView([e.lat,e.lon],16),w(`${e.mahalle} (${e.ilce})`),T(!1),x(!1))})(e)',
    'onClick:()=>(e=>{const t=i.current;__smf({f:r=>r.ilce===e.ilce&&r.mahalle===e.mahalle,ad:`${e.mahalle} (${e.ilce})`});t&&(t.setView([e.lat,e.lon],16),w(`${e.mahalle} (${e.ilce})`),T(!1),x(!1))})(e)')
bir('onChange:e=>{w(e.target.value),x(!1),T(e.target.value.trim().length>0)}',
    'onChange:e=>{w(e.target.value),x(!1),T(e.target.value.trim().length>0),e.target.value.trim()||__smf(null)}')
bir('children:"E\\u015fle\\u015fen mahalle/il\\xe7e bulunamad\\u0131."}),',
    'children:"E\\u015fle\\u015fen mahalle/il\\xe7e bulunamad\\u0131."}),__mf&&(0,a().jsxs)("div",{"data-testid":"m5-harita-suzgec",style:{position:"absolute",bottom:24,left:10,zIndex:1e3,display:"flex",alignItems:"center",gap:8,background:"rgba(15,42,68,0.92)",color:"#fff",fontSize:12,padding:"6px 10px",borderRadius:8,border:"1px solid rgba(255,255,255,0.25)"},children:[(0,a().jsxs)("span",{children:["Yaln\\u0131z: ",(0,a().jsx)("b",{children:__mf.ad})," \\u2014 ",(t||[]).length.toLocaleString("tr-TR")," vaka"]}),(0,a().jsx)("button",{type:"button","data-testid":"m5-harita-suzgec-kaldir",onClick:()=>{__smf(null),w("")},style:{background:"rgba(23,162,168,0.85)",color:"#fff",border:"none",borderRadius:6,padding:"3px 8px",cursor:"pointer",fontSize:11},children:"\\u2716 T\\xfcm\\xfcn\\xfc g\\xf6ster"})]}),')
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("ISTDEG_HARITA_OK")
