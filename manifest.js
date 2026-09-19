// Public manifest — mevcut sürüm bilgisi.
// Yeni sürüm yayınlarken bu dosyadaki version alanını güncelle. Bu dosya
// standalone HTML'e GÖMÜLMEZ; her zaman canlı sunucudan çekilir.
window.__APP_MANIFEST__ = {
  version: '0.9.45',
  released: '2026-09-19',
  notes: 'Modül 2 ve Modül 4\'ün "Genel" sekmesindeki üstteki özet kartları (Toplam Vaka / Hastane Teslim % / Vaka Kapatma %) kaldırıldı. ICD-10 sekmesine Akıllı Bileklik ile birebir aynı yapıda iki alt sekme eklendi: "İstasyon Bazlı" (doluluk tablosu) ve "Girilmeyen Vakalar" (İstasyon, Vaka Tarihi, KKM Protokol, Ekip Şefi, Sonuç, İstasyon Açıklaması detay listesi), Excel çıktısına da ayrı bir sayfa olarak yansıdı.',
  downloadUrl: 'https://raw.githubusercontent.com/gumusorhan-wq/istatistik-merkezi-112-dagitim/main/112-istatistik-merkezi.html'
};
