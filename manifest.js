// Public manifest — mevcut sürüm bilgisi.
// Yeni sürüm yayınlarken bu dosyadaki version alanını güncelle. Bu dosya
// standalone HTML'e GÖMÜLMEZ; her zaman canlı sunucudan çekilir.
window.__APP_MANIFEST__ = {
  version: '0.9.40',
  released: '2026-09-15',
  notes: 'Büyük güncelleme paketi: (1) KKM Protokol tekilleştirme — aynı protokol+ekip+istasyona sahip satırlar artık tüm modüllerde (ICD-10 ve Vaka Kapatma dahil) tek vaka sayılıyor. (2) Modül 4 Vaka Kapatma tamamen yenilendi: 24 Saat/72 Saat/Diğer süre analizi, istasyon bazlı özet + TOPLAM satırı, kapatılmamış vakalar listesi, tümü Excel\'e de yansıyor. (3) Çağrı ve kapatma saatleri artık ayrı saat kolonlarıyla birleştirilip doğru hesaplanıyor (önceden sadece tarih kullanılıyordu). (4) Modül 5 Harita: gerçek Excel koordinatları kullanılıyor (geocoding yok), tam ekran inceleme, mahalle/ilçe arama ile odaklanma, Standart/Uydu geçişi. (5) Ana panelde "Tüm Ekipler" (ASHİ+Dış Kurum birleşik) seçeneği eklendi, Genel Toplam artık seçime göre değişiyor. (6) Mahalle/ilçe adları standart hale getirildi (Mah./Mh. ekleri temizlendi, büyük harf). (7) Arşiv artık sürüm güncellemelerinde otomatik yeniden hesaplanıyor. (8) Sessiz/istenmeyen yedek indirme sorunu düzeltildi; güvenli "tarayıcılar arası birleştirme" eklendi. (9) Çeşitli arayüz sadeleştirmeleri.',
  downloadUrl: 'https://raw.githubusercontent.com/gumusorhan-wq/istatistik-merkezi-112-dagitim/main/112-istatistik-merkezi.html'
};
