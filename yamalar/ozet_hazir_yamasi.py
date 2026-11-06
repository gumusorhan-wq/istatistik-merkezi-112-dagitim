"""Sürüm 12.45: çok aylı dönemde ay özeti bu cihazdaki (aynı kurum paketinden, güncel uygulamayla hesaplanmış) sonuçtan alınınca da,
sunucuda bu paket için hazır özet yoksa (liste: ozetHazir false) yetkili kullanıcı onu sunucuya yazar. Önceden yalnız
ay baştan hesaplanınca yazılıyordu; cihazında ayı tutan yönetici dönemi seçse de diğer kullanıcılar için özet oluşmuyordu.
ist_liste_yamasi.py'den SONRA."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__ozYerelYaz" not in js
a = 'if(r&&__ozGecerli(r.results,r.matrixFingerprint,matFp)&&(!f||r.kurumMod===(f.guncelleme||null)||r.kaynak!=="kurum")){R=r.results;cols=cols||r.cols;ah=ah||r.allHeaders;satir+=r.rawRowCount||(r.rows||[]).length}}catch(e){}'
b = ('if(r&&__ozGecerli(r.results,r.matrixFingerprint,matFp)&&(!f||r.kurumMod===(f.guncelleme||null)||r.kaynak!=="kurum")){R=r.results;cols=cols||r.cols;ah=ah||r.allHeaders;satir+=r.rawRowCount||(r.rows||[]).length;'
     'if(yaz&&f&&f.paket&&f.ozetHazir===false&&r.kaynak==="kurum"&&r.kurumMod===(f.guncelleme||null)){const __ozYerelYaz=1;try{await H.arsiv.ozetYaz(il,ym,{results:__ozKopya(R),fp:matFp,paket:f.paket});yazilan++;f.ozetHazir=!0}catch(e){console.warn("[özet] sunucuya yazılamadı",ym,e)}}}}catch(e){}')
assert js.count(a) == 1, js.count(a)
js = js.replace(a, b)
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("OZET_HAZIR_OK")
