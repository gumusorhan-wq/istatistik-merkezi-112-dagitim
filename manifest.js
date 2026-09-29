// Public manifest — mevcut sürüm bilgisi.
// Yeni sürüm yayınlarken bu dosyadaki version alanını güncelle. Bu dosya
// standalone HTML'e GÖMÜLMEZ; her zaman canlı sunucudan çekilir.
window.__APP_MANIFEST__ = {
  version: '1.0.08',
  released: '2026-09-29',
  notes: 'Özel Değerlendirme: her metrik artık KENDİ Matris hariç tutma kategorisiyle ayrı ayrı hesaplanıyor (ör. Nakil vakaları İstasyon Reaksiyon için hariç, Hastane Teslim için dahil olabiliyor). Yeni \'Meşguliyet\' kategorisi eklendi. \'Hariç Tutma\' sekmesi artık seçili metriklerin kategorilerini ayrı ayrı gösterir, boşsa diğer kategorilerden (Modül 4 dahil) otomatik doldurur. Seçili metrik listesinde kategori rozeti (uyarı ikonlu). Sütun arama artık aranabilir açılır kutu. Kapsamlı isimlendirme düzeltmesi: \'GKG\' öneki tüm uygulamadan (sekmeler, kartlar, Ayarlar, Kılavuz, Excel, indirilen dosya adları dahil) kaldırıldı — KKM Reaksiyon, İstasyon Reaksiyon, Kentsel Ulaşım, Kırsal Ulaşım. Modül 4\'ün kendi adı \'İstasyon İstatistik\', içindeki Hastane Teslim metriği ise kendi adını korudu.',
  downloadUrl: 'https://raw.githubusercontent.com/gumusorhan-wq/istatistik-merkezi-112-dagitim/main/112-istatistik-merkezi.html'
};
