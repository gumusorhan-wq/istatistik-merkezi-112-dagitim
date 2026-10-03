// Public manifest — mevcut sürüm bilgisi.
// Yeni sürüm yayınlarken bu dosyadaki version alanını güncelle. Bu dosya
// standalone HTML'e GÖMÜLMEZ; her zaman canlı sunucudan çekilir.
window.__APP_MANIFEST__ = {
  version: '1.0.12',
  released: '2026-10-03',
  notes: 'ARŞİV ÇÖKME SORUNU GİDERİLDİ: Arşivdeki ay sayısı arttıkça yaşanan çökmeler düzeltildi. Ayların ham verileri artık ayrı saklanıyor ve yalnızca gerektiğinde, tek ay olarak yükleniyor; mevcut arşiviniz ilk açılışta otomatik ve güvenli şekilde yeni düzene taşınır. Yerel Dosya Deposu, Tam Yedek ve Arşiv dışa aktarma artık parça parça yazılıyor; yedek yükleme ve birleştirme büyük dosyaları da açabiliyor, Tam Yedek Yükle artık önce yedeği yazıp sonra fazla ayları siliyor (bozuk dosyada mevcut veri korunur). Analitik/oturum kaydı betiği (PostHog) kaldırıldı. Özel Değerlendirme: Komuta Reaksiyon sütunu artık tanınıyor (Eşik Aşım Oranı ≤120 sn) ve hariç tutma ayarları Modül 5 listelerini kullanıyor. Modül 5 > İstasyon Bazlı Değerlendirme: yeni \'Aylar Arası Kıyaslama\' Excel çıktısı. ÖNEMLİ: Güncellemeden sonra eski sürümü (1.0.09) kullanmayın; yeni sürümle bir Tam Yedek alın.',
  downloadUrl: 'https://raw.githubusercontent.com/gumusorhan-wq/istatistik-merkezi-112-dagitim/main/112-istatistik-merkezi.html'
};
