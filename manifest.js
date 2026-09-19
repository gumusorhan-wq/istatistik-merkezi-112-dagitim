// Public manifest — mevcut sürüm bilgisi.
// Yeni sürüm yayınlarken bu dosyadaki version alanını güncelle. Bu dosya
// standalone HTML'e GÖMÜLMEZ; her zaman canlı sunucudan çekilir.
window.__APP_MANIFEST__ = {
  version: '1.0.01',
  released: '2026-09-20',
  notes: 'v1.0 — Kapsamlı filtreleme ve arayüz güncellemesi: Modül 5 (İstasyon Performans, İstasyon Değerlendirme, Mahalle Dağılımı, Ekip Dağılımı), GKG 15/16/17/20 + Hastane Teslim (İstasyon Bazlı + Eşik Aşımı), ICD-10 (İstasyon Bazlı + Girilmeyen Vakalar), Akıllı Bileklik (İstasyon Bazlı + Takılmayan Hastalar) ve Vaka Kapatma (İstasyon Bazlı, 24/72/Diğer, Kapatılmayan Vaka) sekmelerinin tümüne arama/filtreleme eklendi — hepsi ilgili sekme butonlarıyla aynı satırda, sağa yaslı. Modül 2/4 "Genel" sekmesindeki gereksiz özet kartları kaldırıldı. Vaka Kapatma "Diğer" kategorisi artık sadece 72 saatten uzun sürede KAPANMIŞ vakaları içeriyor (kapatılmamış vakalar ayrı takip ediliyor). Ana panele ICD-10 ve Akıllı Bileklik kartları eklendi, kart taşma/hizalama sorunları düzeltildi.',
  downloadUrl: 'https://raw.githubusercontent.com/gumusorhan-wq/istatistik-merkezi-112-dagitim/main/112-istatistik-merkezi.html'
};
