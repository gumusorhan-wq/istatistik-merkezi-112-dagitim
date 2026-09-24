// Public manifest — mevcut sürüm bilgisi.
// Yeni sürüm yayınlarken bu dosyadaki version alanını güncelle. Bu dosya
// standalone HTML'e GÖMÜLMEZ; her zaman canlı sunucudan çekilir.
window.__APP_MANIFEST__ = {
  version: '1.0.06',
  released: '2026-09-24',
  notes: 'Modül 5\'e "Özel Değerlendirme" sekmesi eklendi: Excel\'in TÜM sütun başlıkları (tanınan/tanınmayan hepsi) metrik olarak seçilebilir; sayısal sütunlarda Toplam+Ortalama, metin/kod sütunlarında Dolu Satır Sayısı + Dağılım (Değer Sayıları) sunulur. Kimlik/kod/tarih/koordinat alanları (Ekip No, Plaka, Protokol vb.) toplanabilir metrik havuzundan hariç tutuldu. Hastane Teslim eşik aşımı listesine Nakledilen Hastane eklendi. ICD-10/Akıllı Bileklik listelerinden ve GKG16\'dan İstasyon Açıklaması/KM/Saatte KM kaldırıldı. Harita: istasyon/hastane/dış kurum ambulans lokasyon katmanları, halka/nokta hover paneli, üst üste binen işaretçiler otomatik ayrılıyor. Excel\'de Dağılım metrikleri artık ayrı, tam (kesilmemiş) sayfalarda.',
  downloadUrl: 'https://raw.githubusercontent.com/gumusorhan-wq/istatistik-merkezi-112-dagitim/main/112-istatistik-merkezi.html'
};
