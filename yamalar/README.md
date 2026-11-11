# İstatistik dağıtım yamaları (stoktakip-entegrasyon)

`112-istatistik-merkezi.html`, 6666b34 tabanına aşağıdaki yamalar **bu sırayla** uygulanarak üretilir
(her biri `python3 <yama>.py <html>`; `ozet_yamasi.py` ve `donem_ozet_yamasi.py` yanlarındaki `.js` dosyalarını okur):

donem → geri → oturum → brans → kart → buyuk → nakil → istdeg_harita → ilkac → yil_ac → rota_yon → kalibre → altbilgi → yol_uzak → ozet → donem_ozet → yil_tum → ist_liste → ozet_hazir → turgos_secici → teknik_brifing → ortak_dil → anasayfa → ambulans_ay → harita_coklu → istasyon_konum → harita_protokol → harita_kutu → istasyon_katman → sunum_istasyon → ihbar_veren → esik_sola → arsiv_serit

`dogrula.js` (Aşama 2): jsdom ile aylık sonuçların birleşimini (`__ozetBirlestir`) tam hesapla alan alan karşılaştırır.
Gerçek veri bu klasöre konmaz.
