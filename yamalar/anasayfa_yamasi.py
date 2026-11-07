"""Sürüm 13.28: yan menüye AYRI 'Ana Sayfa' öğesi (Depo / Teknik ana sayfası gibi: ön bilgi kartları + hızlı erişim).
Var olan öğeler (Excel Yükle, Kontrol Paneli, Arşiv, Kılavuz, Ayarlar) adlarıyla ve hâlleriyle kalır. ortak_dil_yamasi.py'den SONRA."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__AnaSayfaV" not in js


def bir(a, b):
    global js
    assert js.count(a) == 1, (js.count(a), a[:80]); js = js.replace(a, b)


# 1) menü: en başa Ana Sayfa
bir('__useHMS().hm&&o.splice(1,0,...o.splice(2,1));',
    '__useHMS().hm&&o.splice(1,0,...o.splice(2,1));o.unshift({id:"anasayfa",label:"Ana Sayfa",icon:__AnaIc,testId:"nav-anasayfa"});')
# 1b) Kontrol Paneli'nin simgesi ev çiziyordu; Ana Sayfa ile karışmasın diye pano simgesi (ad ve yer aynı)
bir('icon:re,testId:"nav-dashboard"', 'icon:__PanoIc,testId:"nav-dashboard"')
# 1c) açılışta Ana Sayfa (Depo / Planlama gibi): başlangıç görünümü ve açılıştaki otomatik ay yüklemeleri Ana Sayfa'da kalır
bir('activeView:"upload",activeModule:"m1",activeScope:"ashi"', 'activeView:"anasayfa",activeModule:"m1",activeScope:"ashi"')
bir('st.setActiveView&&st.setActiveView("dashboard");return}', 'st.setActiveView&&st.setActiveView("anasayfa");return}')
bir('d("dashboard"),m(`Son kay\\u0131tl\\u0131 ay otomatik', 'd("anasayfa"),m(`Son kay\\u0131tl\\u0131 ay otomatik')
# 2) görünüm
bir('"upload"===o&&(0,a().jsx)(dd,{onArchiveChange:C}),',
    '"anasayfa"===o&&(0,a().jsx)(__AnaSayfaV,{}),"upload"===o&&(0,a().jsx)(dd,{onArchiveChange:C}),')
# 3) bileşenler (menü işlevinin önüne)
kod = r'''function __PanoIc(p){return (0,a().jsx)("svg",{width:p.size||18,height:p.size||18,viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:2,strokeLinecap:"round",strokeLinejoin:"round","aria-hidden":"true",children:(0,a().jsx)("path",{d:"M3 3h7v9H3zM14 3h7v5h-7zM14 12h7v9h-7zM3 16h7v5H3z"})})}
function __AnaIc(p){return (0,a().jsx)("svg",{width:p.size||18,height:p.size||18,viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:2,strokeLinecap:"round",strokeLinejoin:"round","aria-hidden":"true",children:(0,a().jsx)("path",{d:"M3 11l9-8 9 8M5 9v12h14V9M9 21v-7h6v7"})})}
function __AnaSayfaV(){
  const git=Ge(e=>e.setActiveView),res=Ge(e=>e.results),ar=Ge(e=>e.archivedMonths)||[];
  const AY=["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"];
  const ad=ym=>{const m=/^(\d{4})-(\d{2})/.exec(String(ym||""));return m?AY[+m[2]-1]+" "+m[1]:"—"};
  const yms=ar.map(x=>x&&x.ym).filter(Boolean).sort(),son=yms[yms.length-1],yil=son?son.slice(0,4):"",yilSay=yms.filter(x=>x.slice(0,4)===yil).length;
  const kart=(b,d,alt,hedef,ok)=>__h("div",{className:"ana-kart"},__h("span",null,b),__h("b",null,d),__h("small",null,alt,hedef&&ok!==!1?__h("a",{href:"#",onClick:e=>{e.preventDefault();git(hedef)}}," ayrıntı"):null));
  const hizli=[["upload","Excel Yükle",!0],["dashboard","Kontrol Paneli",!!res],["archive","Arşiv",!0],["settings","Ayarlar",!0]];
  return __h("div",{className:"ana-sayfa","data-testid":"ana-sayfa"},
    __h("h1",{className:"ana-bas"},"Ana Sayfa"),
    __h("p",{className:"ana-alt"},son?"Kurum arşivindeki son ay: "+ad(son):"Kurum arşivinde henüz ay yok"),
    __h("div",{className:"ana-kartlar"},
      kart("Son ay",ad(son),son?"kurum arşivindeki en güncel ay":"arşiv boş","archive"),
      kart("Kurum arşivi",ar.length,"bu cihazdaki kayıtlı ay","archive"),
      kart(yil?yil+" yılı":"Yıl",yil?yilSay+" / 12":"—","ay yüklü","archive"),
      kart("Hesaplanan dönem",res?"Hazır":"Seçilmedi",res?"Kontrol Paneli'nde görüntüleniyor":"Arşiv'den ay seçin ya da Excel yükleyin",res?"dashboard":"archive")),
    __h("div",{className:"ana-hizli"},__h("h3",null,"Hızlı erişim"),__h("div",{className:"ana-git-l"},hizli.map(([k,t,ok])=>__h("button",{key:k,type:"button",className:"ana-git",disabled:!ok,onClick:()=>ok&&git(k)},t)))));
}
'''
bir('function yp(e){let{collapsed:t,onToggle:r}=e;', kod + 'function yp(e){let{collapsed:t,onToggle:r}=e;')
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode("ascii") + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html)
print("anasayfa_yamasi: ayrı Ana Sayfa öğesi + görünüm")
