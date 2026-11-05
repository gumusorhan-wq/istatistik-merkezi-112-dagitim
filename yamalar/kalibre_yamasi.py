"""Sürüm 12.41: Tahmini varış denemesi (önce "Süre karşılaştırma raporu"). Ambulans tahmini = çıkış payı + yol süresi × oran,
Kentsel/Kırsal ayrı (kurum ayarı 05.11.2026: Kentsel 3,5 dk + %80, Kırsal 4,5 dk + %75; rapordan tarayıcıda denenebilir). Rota kutusu ve Tahmini Varış listesi bu tahmini kullanır. Ayın vakalarında rota motorunun tahmini süresi ile
Excel'deki gerçek ulaşım süresi karşılaştırılır (Kentsel/Kırsal × tahmini yol km aralığı): medyan gerçek/tahmini süre,
oran (gerçek ÷ tahmini) medyanı ve çeyrekleri, gerçek km ÷ tahmini km. Yalnız toplu sayılar; kişi/protokol yok.
Amaç: tahmini süreye uygulanacak düzeltme katsayısını veriyle belirlemek. Kentsel ve Kırsal Ulaşım bloklarında düğme (rapor ikisini birlikte gösterir); yalnız Genel Admin ve İl Admini görür (/api/im112/durum "yonetici"); Sayfa Excel'e girmez (pencere sayfa içeriğinin dışında)."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__tvsKalibre" not in js
def bir(a, b):
    global js
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)

FN = r'''
window.__TVS_KAT_VAR={"Kentsel":{pay:210,oran:.8},"Kırsal":{pay:270,oran:.75}};
window.__tvsBolge=function(v){const s=String(v||"").toLocaleLowerCase("tr");return s.includes("kır")||s.includes("kir")?"Kırsal":"Kentsel"};
window.__tvsKat=function(){const D=window.__TVS_KAT_VAR,R={"Kentsel":{...D["Kentsel"]},"Kırsal":{...D["Kırsal"]}};try{const o=JSON.parse(localStorage.getItem("im112_tvs_kat2")||"null");if(o)for(const b of["Kentsel","Kırsal"]){const x=o[b];x&&isFinite(x.pay)&&isFinite(x.oran)&&x.oran>0&&(R[b]={pay:+x.pay,oran:+x.oran})}}catch(e){}return R};
window.__tvsAmb=function(yolSn,bolge){const K=window.__tvsKat()[window.__tvsBolge(bolge)];return Math.round(K.pay+K.oran*yolSn)};
(function(){let n=0;const t=()=>{const K=window.__IM112_KURUM;if(!K||!K.aktif||!K.aktif()){++n<20&&setTimeout(t,1500);return}K.oturum().then(k=>{window.__tvsYon=!!k&&(k.yonetici===!0||k.rol==="super_admin")}).catch(()=>{++n<20&&setTimeout(t,3000)})};setTimeout(t,1200)})();
window.__tvsKalibre=async function(){
  if(window.__tvsYon!==true)return;
  const ID="__tvsKalKutu";try{document.getElementById(ID)&&document.getElementById(ID).remove()}catch(e){}
  const kutu=document.createElement("div");kutu.id=ID;kutu.setAttribute("data-testid","tvs-kalibre-rapor");
  kutu.style.cssText="position:fixed;inset:0;z-index:5000;background:rgba(0,0,0,.45);display:flex;align-items:flex-start;justify-content:center;padding:40px 12px;overflow:auto";
  const ic=document.createElement("div");ic.style.cssText="background:#fff;color:#0f172a;border-radius:12px;max-width:980px;width:100%;padding:18px 20px;font:13px/1.5 system-ui,sans-serif;box-shadow:0 20px 50px rgba(0,0,0,.35)";
  kutu.appendChild(ic);kutu.addEventListener("click",e=>{e.target===kutu&&kutu.remove()});document.body.appendChild(kutu);
  const yaz=h=>{ic.innerHTML=h},kapatBtn=`<button type="button" data-testid="tvs-kalibre-kapat" style="padding:5px 12px;border-radius:6px;border:1px solid #cbd5e1;background:#fff;cursor:pointer">Kapat</button>`;
  const bagla=()=>{const k=ic.querySelector("[data-testid=tvs-kalibre-kapat]");k&&(k.onclick=()=>kutu.remove())};
  yaz("<b>Tahmini varış denemesi</b><div style='margin-top:8px;color:#64748b'>Vakalar hazırlanıyor…</div>");
  try{
    const st=Ge.getState(),R=st.parsedRows,t=st.cols;if(!Array.isArray(R)||!R.length||!t)throw new Error("Açık ayın vaka satırları yok (önce bir ay açın).");
    const sn=v=>{if(v==null||v==="")return null;if(typeof v==="number")return v>0&&v<1?Math.round(v*86400):v;const s=String(v).trim(),m=s.match(/^(\d+):(\d{1,2}):(\d{1,2})$/);if(m)return 3600*m[1]+60*m[2]+ +m[3];const n=Number(s.replace(",","."));return isFinite(n)?n:null},
      sayi=v=>{if(v==null||v==="")return null;if(typeof v==="number")return v;const s=String(v).trim(),n=Number(/,\d+$/.test(s)?s.replace(/\./g,"").replace(",","."):s);return isFinite(n)?n:null},
      saat=v=>{if(v==null||v==="")return null;if(v instanceof Date)return v.getHours();if(typeof v==="number")return v>=0&&v<1?Math.floor(v*24+1e-9)%24:null;const m=String(v).trim().match(/(\d{1,2})[:.](\d{2})/);return m&&+m[1]<24?+m[1]:null},
      tip=v=>{const s=String(v||"").toLocaleLowerCase("tr");return s.includes("kent")?"Kentsel":s.includes("kır")||s.includes("kir")?"Kırsal":null};
    const gor=new Set,satir=[];
    for(const r of R){const pr=String(Hu(r,t.protokol)||"").trim(),ist=String(Hu(r,t.istasyon)||"").trim();if(!pr||!ist||gor.has(pr))continue;
      try{if(typeof xe==="function"&&!xe(ist,"ashi"))continue}catch(e){}
      const g=sn(Hu(r,t.ulasimSn)),b=tip(Hu(r,t.bolgeTipi));if(!b||g==null||g<30||g>7200)continue;
      const c=sayi(Hu(r,t.cikisKm)),v=sayi(Hu(r,t.varisKm)),gk=c!=null&&v!=null&&v-c>0&&v-c<300?v-c:null;
      gor.add(pr);satir.push({protokol:pr,istasyon:ist,kisaStasyon:ist,__g:g,__b:b,__gk:gk,__s:saat(Hu(r,t.cagriSaati))})}
    if(!satir.length)throw new Error("Ulaşım süresi ve Kentsel/Kırsal bilgisi olan vaka bulunamadı.");
    const ENC=5000,adim=Math.max(1,Math.ceil(satir.length/ENC)),orn=satir.filter((x,i)=>i%adim===0);
    yaz(`<b>Tahmini varış denemesi</b><div style='margin-top:8px;color:#64748b'>${orn.length.toLocaleString("tr-TR")} vaka için yol süresi hesaplanıyor… (bir-iki dakika sürebilir)</div>`);
    const H=await window.__tvsHesapla(orn,[]);if(H.ozet.hata&&!H.sonuc.size)throw new Error(H.ozet.hata);
    const V=[];let yak=0,sup=0;
    for(const[e,v]of H.sonuc){if(v.vk!=="Excel"){yak++;continue}const y=v.yol!=null?v.yol:v.sn;if(y==null||v.km==null)continue;
      if(e.__gk!=null&&v.km>2&&e.__gk/v.km<.5){sup++;continue}V.push({g:e.__g,y,km:v.km,b:e.__b,s:e.__s})}
    const BAND=[[0,2],[2,5],[5,10],[10,20],[20,40],[40,1e9]],bEt=b=>b[1]>1e8?`${b[0]}+ km`:`${b[0]}–${b[1]} km`,
      med=a=>{if(!a.length)return null;const s=a.slice().sort((x,y)=>x-y),h=(s.length-1)/2;return(s[Math.floor(h)]+s[Math.ceil(h)])/2},
      dk=x=>x==null?"–":(x/60).toFixed(1).replace(".",","),ay=st.currentMonth||"";
    const ciz=()=>{
      const K=window.__tvsKat(),amb=(y,b)=>K[b].pay+K[b].oran*y,sat=[],tsv=[["Bölge","Yol mesafesi","Vaka","Gerçek (dk)","Eski tahmin: normal araç (dk)","Yeni tahmin: ambulans (dk)","Fark gerçek−yeni (dk)","Yeni tahmin ±2 dk içinde"]];
      const satirYap=(hedef,bt,et,a,kalin)=>{const f=med(a.map(x=>x.g-amb(x.y,x.b))),is=Math.round(100*a.filter(x=>Math.abs(x.g-amb(x.y,x.b))<=120).length/a.length),
          row=[bt,et,a.length,dk(med(a.map(x=>x.g))),dk(med(a.map(x=>x.y))),dk(med(a.map(x=>amb(x.y,x.b)))),(f>0?"+":"")+dk(f),"%"+is];
        tsv.push(row);hedef.push(`<tr style="${kalin?"font-weight:700;background:#eef6f7":""}">${row.map((c,i)=>`<td style="padding:5px 8px;border-bottom:1px solid #e2e8f0;text-align:${i<2?"left":"right"};${i===5?"font-weight:700;color:#0f766e":""}">${typeof c==="number"?c.toLocaleString("tr-TR"):c}</td>`).join("")}</tr>`)};
      for(const bt of["Kentsel","Kırsal"]){const A=V.filter(x=>x.b===bt);for(const b of[null,...BAND]){const a=b?A.filter(x=>x.km>=b[0]&&x.km<b[1]):A;if(a.length<(b?10:1))continue;satirYap(sat,bt,b?bEt(b):"TÜMÜ",a,!b)}}
      const DIL=[["07–10 (sabah trafiği)",h=>h>=7&&h<10],["10–16 (gündüz)",h=>h>=10&&h<16],["16–20 (akşam trafiği)",h=>h>=16&&h<20],["20–07 (gece)",h=>h>=20||h<7]],sat2=[];
      tsv.push([]);tsv.push(["Bölge","Saat dilimi","Vaka","Gerçek (dk)","Eski tahmin (dk)","Yeni tahmin (dk)","Fark (dk)","±2 dk içinde"]);
      for(const bt of["Kentsel","Kırsal"]){const A=V.filter(x=>x.b===bt&&x.s!=null);for(const[ad,f]of DIL){const a=A.filter(x=>f(x.s));a.length>=10&&satirYap(sat2,bt,ad,a,!1)}}
      const bas=tsv[0].map((c,i)=>`<th style="padding:6px 8px;text-align:${i<2?"left":"right"};font-size:11.5px;color:#475569;border-bottom:2px solid #17a2a8">${c}</th>`).join(""),metin=tsv.map(r=>r.join("\t")).join("\n");
      yaz(`<div style="display:flex;align-items:center;gap:10px;margin-bottom:8px"><b style="font-size:15px">⏱ Tahmini varış denemesi</b><span style="color:#64748b">${ay}${window.__donemAktif&&window.__donemAktif()?" (seçili dönem)":""}</span><span style="flex:1"></span><button type="button" data-testid="tvs-kalibre-kopyala" style="padding:5px 12px;border-radius:6px;border:1px solid #17a2a8;background:#17a2a8;color:#fff;cursor:pointer;font-weight:600">Tabloyu kopyala</button>${kapatBtn}</div>
      <div style="background:#f1f5f9;border-radius:8px;padding:10px 12px;margin-bottom:10px;color:#334155">
        <div><b>Gerçek:</b> ambulansın vakaya ulaşma süresi (Excel). <b>Eski tahmin:</b> rota motorunun normal araçla yol süresi. <b>Yeni tahmin:</b> çıkış payı + yol süresinin belli bir oranı.</div>
        <div style="margin-top:4px"><b>Fark</b> 0'a yakınsa ve <b>±2 dk içinde</b> yüzdesi yüksekse formül iyi demektir. Fark artıysa tahmin kısa kalıyor, eksiyse uzun.</div>
        ${["Kentsel","Kırsal"].map(b=>`<div style="margin-top:8px;display:flex;gap:12px;align-items:center;flex-wrap:wrap"><b style="min-width:110px">Formül · ${b}:</b>
          <label>Çıkış payı <input data-testid="tvs-kat-pay-${b==="Kentsel"?"kentsel":"kirsal"}" type="number" step="0.5" min="0" max="15" value="${K[b].pay/60}" style="width:64px;padding:3px 6px;border:1px solid #cbd5e1;border-radius:6px"> dk</label>
          <span>+ yol süresinin</span><label><input data-testid="tvs-kat-oran-${b==="Kentsel"?"kentsel":"kirsal"}" type="number" step="5" min="30" max="200" value="${Math.round(K[b].oran*100)}" style="width:64px;padding:3px 6px;border:1px solid #cbd5e1;border-radius:6px"> %'si</label></div>`).join("")}
        <div style="margin-top:8px;display:flex;gap:10px"><button type="button" data-testid="tvs-kat-uygula" style="padding:4px 12px;border-radius:6px;border:1px solid #0f766e;background:#0f766e;color:#fff;cursor:pointer;font-weight:600">Uygula</button>
          <button type="button" data-testid="tvs-kat-varsayilan" style="padding:4px 10px;border-radius:6px;border:1px solid #cbd5e1;background:#fff;cursor:pointer">Kurum ayarı (Kentsel 3,5 dk + %80 · Kırsal 4,5 dk + %75)</button></div>
        <div style="margin-top:4px;font-size:11.5px;color:#64748b">Kurum ayarı herkes için geçerlidir (05.11.2026 kararı, Ekim 2026 verisiyle). Buradan yaptığınız değişiklik yalnız bu tarayıcıda denemedir; haritadaki rota kutusu ve Tahmini Varış listesi de bunu kullanır.</div></div>
      <div style="font-weight:700;margin:4px 0 4px">Mesafeye göre</div><div style="overflow:auto"><table style="border-collapse:collapse;width:100%;font-size:12.5px"><thead><tr>${bas}</tr></thead><tbody>${sat.join("")}</tbody></table></div>
      <div style="font-weight:700;margin:14px 0 2px">Saat dilimine göre <span style="font-weight:400;color:#64748b;font-size:12px">(çağrı saatine göre; tüm mesafeler — aynı formül her dilimde tutuyor mu?)</span></div>
      ${sat2.length?`<div style="overflow:auto"><table style="border-collapse:collapse;width:100%;font-size:12.5px"><thead><tr>${bas.replace(">Yol mesafesi<",">Saat dilimi<")}</tr></thead><tbody>${sat2.join("")}</tbody></table></div>`:`<div style="color:#64748b">Çağrı saati okunamadı.</div>`}
      <div style="color:#64748b;font-size:12px;margin-top:10px">Kullanılan: ${V.length.toLocaleString("tr-TR")} vaka${adim>1?` (${satir.length.toLocaleString("tr-TR")} vakadan her ${adim}. vaka örneklendi)`:""} · vaka konumu Excel'de olmadığı için dışarıda: ${yak.toLocaleString("tr-TR")} · konumu şüpheli (araç sayacına göre gidilen yol hesaplanan yolun yarısından az): ${sup.toLocaleString("tr-TR")} · tahmini hesaplanamayan: ${(H.eksik||[]).length.toLocaleString("tr-TR")}. Aralık satırlarında en az 10 vaka aranır. Tabloda kişi ya da protokol bilgisi yoktur.</div>
      ${(H.eksik||[]).length?(()=>{const N=new Map,I=new Map;for(const x of H.eksik){const n=x.neden||"bilinmiyor";N.set(n,(N.get(n)||0)+1);/istasyon/.test(n)&&I.set(x.e.istasyon,(I.get(x.e.istasyon)||0)+1)}
        const li=[...N].sort((a,b)=>b[1]-a[1]).map(([n,k])=>`<li>${n}: <b>${k.toLocaleString("tr-TR")}</b></li>`).join(""),
          ist=[...I].sort((a,b)=>b[1]-a[1]).slice(0,15).map(([n,k])=>`${String(n).replace(/[<>&]/g,"")} (${k})`).join(" · ");
        return`<details data-testid="tvs-eksik-dokum" style="margin-top:8px;font-size:12px;color:#334155"><summary style="cursor:pointer;font-weight:600">Tahmini hesaplanamayan vakaların nedenleri</summary><ul style="margin:6px 0 0 18px">${li}</ul>${ist?`<div style="margin-top:4px">Konumu bulunamayan istasyonlar (vaka sayısı): ${ist}</div>`:""}</details>`})():""}`);
      bagla();
      ic.querySelector("[data-testid=tvs-kalibre-kopyala]").onclick=async ev=>{try{await navigator.clipboard.writeText(metin);ev.target.textContent="Kopyalandı ✓"}catch(e){ev.target.textContent="Kopyalanamadı"}};
      const kaydet=o=>{try{o?localStorage.setItem("im112_tvs_kat2",JSON.stringify(o)):localStorage.removeItem("im112_tvs_kat2")}catch(e){}ciz()};
      ic.querySelector("[data-testid=tvs-kat-uygula]").onclick=()=>{const o={};for(const[b,k]of[["Kentsel","kentsel"],["Kırsal","kirsal"]]){const p=Number(String(ic.querySelector(`[data-testid=tvs-kat-pay-${k}]`).value).replace(",",".")),r=Number(ic.querySelector(`[data-testid=tvs-kat-oran-${k}]`).value);if(!(p>=0&&p<=15&&r>=30&&r<=200))return;o[b]={pay:Math.round(p*60),oran:r/100}}kaydet(o)};
      ic.querySelector("[data-testid=tvs-kat-varsayilan]").onclick=()=>kaydet(null)};
    ciz();
  }catch(err){yaz(`<b>Tahmini varış denemesi</b><div style="margin-top:8px;color:#b91c1c">${String(err&&err.message||err)}</div><div style="margin-top:12px">${kapatBtn}</div>`);bagla()}
};
'''
bir('window.__rotaCiz=async function(el){', FN.strip() + '\nwindow.__rotaCiz=async function(el){')
bir('c=null==sn?null:{sn:Math.round(sn),km:null==km?null:Math.round(km/100)/10}',
    'c=null==sn?null:{yol:Math.round(sn),km:null==km?null:Math.round(km/100)/10}')
bir('const IST=__tvsIstasyonlar(),S=__tvsSatir(),G=new Map;',
    'const IST=__tvsIstasyonlar(),S=__tvsSatir(),G=new Map,AMB=(e,y)=>window.__tvsAmb?window.__tvsAmb(y,e.__b||((S&&S.P.get(e.protokol))||{}).bt):y;')
bir('const c=__TVS_ON.get(ck);c?(sonuc.set(e,{...c,...ek}),ozet.hesap++)','const c=__TVS_ON.get(ck);c?(sonuc.set(e,{...c,sn:AMB(e,c.yol),...ek}),ozet.hesap++)')
bir('for(const[e,ek]of g.get(bk))c?(sonuc.set(e,{...c,...ek}),ozet.hesap++)','for(const[e,ek]of g.get(bk))c?(sonuc.set(e,{...c,sn:AMB(e,c.yol),...ek}),ozet.hesap++)')
bir('pr&&!P.has(pr)&&P.set(pr,{v,s,il,mh});','pr&&!P.has(pr)&&P.set(pr,{v,s,il,mh,bt:Hu(r,t.bolgeTipi)});')
bir('Tahmini süre: <b>${Math.max(1,Math.round(rt.duration/60))} dk</b></div><div style="color:#6b7280;font-size:11px">Normal araç hızıyla tahmin (ambulans değil) · ',
    'Normal araç: ${Math.max(1,Math.round(rt.duration/60))} dk · Ambulans tahmini${__rbt?" ("+__rbt+")":""}: <b>${Math.max(1,Math.round((window.__tvsAmb?window.__tvsAmb(rt.duration,__rbt):rt.duration)/60))} dk</b></div><div style="color:#6b7280;font-size:11px">Ambulans tahmini = çıkış payı + yol süresinin oranı (Kentsel/Kırsal ayrı, gerçek ulaşım sürelerinden) · ')
bir('const __ist=s=>/ASH[İI]|[İI]STASYON/i.test(String(s||"")),__vk=s=>/^Vaka/.test(String(s||"")),',
    'const __ist=s=>/ASH[İI]|[İI]STASYON/i.test(String(s||"")),__vk=s=>/^Vaka/.test(String(s||"")),__rbt=(()=>{try{const m=/\\((\\d+)\\)/.exec(String((/^Vaka/.test(A.ad||"")?A.ad:B.ad)||""));const S=m&&__tvsSatir();const b=S&&(S.P.get(m[1])||{}).bt;return b?window.__tvsBolge(b):""}catch(e){return""}})(),')
bir('"station"===d&&(0,a().jsx)(Cd,{value:p.q,onChange:p.setQ,',
    'window.__IM112_HOST&&window.__tvsYon===!0&&(0,a().jsx)("button",{type:"button",className:"btn btn-ghost","data-testid":"tvs-kalibre",title:"Ayın vakalarında (Kentsel ve Kırsal) tahmini yol süresini gerçek ulaşım süresiyle karşılaştırır",style:{fontSize:11.5,padding:"4px 10px"},onClick:()=>window.__tvsKalibre(),children:"⏱ Tahmini varış denemesi"}),"station"===d&&(0,a().jsx)(Cd,{value:p.q,onChange:p.setQ,')
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("KALIBRE_OK")
