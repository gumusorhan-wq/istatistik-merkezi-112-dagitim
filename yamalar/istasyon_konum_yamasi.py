"""Sürüm 13.57: İstasyon harita konumu — HUSER Yönetim › İstasyonlar'da girilen konum (host window.__IM112_KONUM =
[{ad, enlem, boylam}]) Excel'deki "İstasyonun Enlemi/Boylamı"nın önüne geçer: vaka kayıtlarındaki istasyon noktası,
istasyon ortalama konumu (haritadaki istasyon işareti) ve rota/tahmini süre hesabı. Eşleme: birim kodu (4–7 hane) ya da
"İLÇE N" anahtarı (ör. "MANİSA AHMETLİ 1 NOLU ACİL SAĞLIK HİZMETLERİ İSTASYONU" = "AHMETLİ 1 NOLU ASHİ")."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__ikBul" not in js
def bir(a, b):
    global js
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)

YARDIMCI = r'''(function(){function N(s){s=String(s||"").toLocaleUpperCase("tr-TR");const k=(s.match(/\((\d{4,7})\)/)||s.match(/(?:^|\s)(\d{4,7})\s*$/)||[])[1]||"";
const t=s.replace(/\(.*?\)/g," ").replace(/(?:^|\s)\d{4,7}(?=\s|$)/g," ");let a="";const r=/([A-ZÇĞİÖŞÜ]+)\s+(\d{1,2})(?=\s|$)/g;let x;while((x=r.exec(t)))a=x[1]+" "+x[2];
return{kod:k,ad:a||t.replace(/\s+/g," ").trim()}}
window.__ikBul=function(ad){try{const L=window.__IM112_KONUM;if(!L||!L.length||!ad)return null;let M=window.__IKM;if(!M||M.src!==L){M={src:L,kod:new Map,ad:new Map};
for(const y of L){const n=N(y.ad),o={lat:+y.enlem,lon:+y.boylam};if(!(o.lat>=35&&o.lat<=43&&o.lon>=25&&o.lon<=45))continue;n.kod&&M.kod.set(n.kod,o);n.ad&&M.ad.set(n.ad,o)}window.__IKM=M}
const n=N(ad);return(n.kod&&M.kod.get(n.kod))||(n.ad&&M.ad.get(n.ad))||null}catch(e){return null}}})();
'''
js = YARDIMCI + js
# 1) vaka kaydındaki istasyon noktası (ilat/ilon)
bir('const y=t.istasyonEnlem?me(Hu(pe,t.istasyonEnlem)):null,x=t.istasyonBoylam?me(Hu(pe,t.istasyonBoylam)):null;',
    'const __o=window.__ikBul&&window.__ikBul(Hu(pe,t.istasyon)),y=__o?__o.lat:t.istasyonEnlem?me(Hu(pe,t.istasyonEnlem)):null,x=__o?__o.lon:t.istasyonBoylam?me(Hu(pe,t.istasyonBoylam)):null;')
# 2) istasyon ortalama konumu
bir('s=t.istasyonEnlem?__tvsNokta(Hu(r,t.istasyonEnlem),Hu(r,t.istasyonBoylam)):null,',
    's=(window.__ikBul&&window.__ikBul(ist))||(t.istasyonEnlem?__tvsNokta(Hu(r,t.istasyonEnlem),Hu(r,t.istasyonBoylam)):null),')
# 3) rota / tahmini süre: önce Yönetim'deki konum
bir('let s=null,sk="";k&&k.ilat&&(s=__tvsNokta(k.ilat,k.ilon))&&(sk="Excel");',
    'let s=null,sk="";(s=window.__ikBul&&window.__ikBul(e.istasyon))&&(sk="Yönetim");!s&&k&&k.ilat&&(s=__tvsNokta(k.ilat,k.ilon))&&(sk="Excel");')

html = html.replace(m.group(1), base64.b64encode(js.encode("utf-8")).decode("ascii"), 1)
open(p, "w", encoding="utf-8").write(html)
print("istasyon konum yaması uygulandı")
