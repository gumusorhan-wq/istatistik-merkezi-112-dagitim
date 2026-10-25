(()=>{const q=new URLSearchParams(location.search),rol=q.get('rol'),il=q.get('il'),ad=q.get('ad')||rol;if(!rol)return;
const P=(p,x)=>'/api/'+p+'?'+new URLSearchParams({rol,kil:il,ad,...x});
window.__IM112_YUKLEYICI=1;
window.__IM112_HOST={surum:1,
 kullanici:async()=>({id:ad,ad,rol,il}),
 iller:async()=>['MANİSA','AMASYA','İZMİR'],
 ozetYukle:async(i,ym,dosya,blob)=>{const r=await fetch(P('ozet',{il:i,ym,dosya}),{method:'POST',body:blob});(window.__ozet=window.__ozet||[]).push(dosya)},
 arsiv:{
  listele:async i=>(await fetch(P('listele',{il:i}))).json(),
  indir:async(i,ym)=>{const r=await fetch(P('indir',{il:i,ym}));if(!r.ok)throw new Error('indirilemedi');return r.arrayBuffer()},
  yukle:async(i,ym,u8,meta)=>{const r=await fetch(P('yukle',{il:i,ym}),{method:'POST',body:u8});if(!r.ok)throw new Error((await r.json()).hata)},
  sil:async(i,ym)=>{const r=await fetch(P('sil',{il:i,ym}),{method:'POST'});if(!r.ok)throw new Error((await r.json()).hata)}}}})();
