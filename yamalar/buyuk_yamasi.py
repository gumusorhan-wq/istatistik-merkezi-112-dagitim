"""Sürüm 12.39: çok büyük dönem seçimi (ör. tüm istasyonlar × 10 ay ≈ 140 bin vaka) tarayıcıyı çökertmesin.
- Hesaplamadan önce bellek boşaltılır (önceki dönem önbellekleri silinir), büyük seçimde önbellekte en çok 1 sonuç tutulur.
- 60 binden çok vaka varsa önce bilgi/onay: süre uyarısı; 200 binden çoksa hesaplanmaz (daha az ay ya da istasyon seçilmeli)."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
def bir(a, b):
    global js
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)
bir('let R;if(!ist.length&&R1)R=R1;else{ilerleme(`${rows.length.toLocaleString("tr-TR")} vaka hesaplanıyor…`);await new Promise(r=>setTimeout(r,30));R=Qu(rows,B.cols,S)}',
    'let R;if(!ist.length&&R1)R=R1;else{const __n=rows.length;'
    'if(__n>200000)throw new Error(`${__n.toLocaleString("tr-TR")} vaka tek seferde hesaplanamayacak kadar çok (tarayıcı belleği yetmez). Daha az ay ya da istasyon seçin (en çok 200.000 vaka).`);'
    'if(__n>60000){for(const[kk,PP]of[...__DN_ONB.entries()])if(PP!==T)__DN_ONB.delete(kk);'
    'if(!window.confirm(`${__n.toLocaleString("tr-TR")} vaka hesaplanacak. Bu büyüklükte hesaplama tarayıcıda 1–3 dakika sürebilir; tarayıcı \\"Sayfa yanıt vermiyor\\" derse \\"Bekle\\"ye basın.\\n\\nDevam edilsin mi?`))throw new Error("Hesaplama iptal edildi")}'
    'ilerleme(`${__n.toLocaleString("tr-TR")} vaka hesaplanıyor…`);await new Promise(r=>setTimeout(r,30));R=Qu(rows,B.cols,S)}')
bir('__DN_ONB.set(k,P);while(__DN_ONB.size>4)__DN_ONB.delete(__DN_ONB.keys().next().value);',
    '__DN_ONB.set(k,P);const __enCok=P.rows&&P.rows.length>60000?1:4;while(__DN_ONB.size>__enCok)__DN_ONB.delete(__DN_ONB.keys().next().value);')
# çok aylı seçimde ayları yüklemeden önce eski dönem önbelleklerini bırak (bellek)
bir('else{const il=K&&K.aktif()?await K.hedefIl():null,yerel=new Set(',
    'else{if(L.length>=4)for(const[kk,PP]of[...__DN_ONB.entries()])if(PP!==T)__DN_ONB.delete(kk);const il=K&&K.aktif()?await K.hedefIl():null,yerel=new Set(')
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("BUYUK_OK")
