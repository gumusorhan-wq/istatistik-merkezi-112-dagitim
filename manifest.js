// Public manifest — mevcut sürüm bilgisi.
// Yeni sürüm yayınlarken bu dosyadaki version alanını güncelle. Bu dosya
// standalone HTML'e GÖMÜLMEZ; her zaman canlı sunucudan çekilir.
window.__APP_MANIFEST__ = {
  version: '1.0.09',
  released: '2026-10-03',
  notes: 'KRİTİK VERİ HATASI DÜZELTMESİ: Özel Değerlendirme\'de birden fazla ay birleştirildiğinde, aynı sütun başlığının farklı aylarda farklı Excel harfine denk gelmesi (ör. \'Hastane Teslim Süresi\' Mayıs\'ta CN, Ocak\'ta CM) yüzünden bir ayın verisi BAŞKA bir aydaki TAMAMEN FARKLI bir sütunla (ör. Meşguliyet Süresi) karışabiliyordu — artık veriler harfe değil sütun başlığının METNİNE göre saklanıyor, bu sorun kökten çözüldü. Hastane Teslim Süresi hesaplaması artık diğer modüllerle birebir aynı: sadece Sonuç="Nakil-Hastaneye" vakaları sayılıyor, mükerrer (Protokol+Ekip+İstasyon) kayıtlar TÜM metriklerde tekilleştiriliyor. GKG15/16/17/20 hesaplamaları artık Dashboard\'daki (Modül 2) resmi kaynakla aynı Matris listesini kullanıyor. \'Genel Toplam\' kategorisi artık yanlışlıkla diğer kategorilerden otomatik doldurulmuyor (ve önceki hatalı doldurma otomatik temizleniyor). Arşiv: eski aylar artık arka planda otomatik yeniden hesaplanıyor (tek tek açmaya gerek yok), satır sayısı uyuşmazlığı ve Özel Değerlendirme için eksik sütun bilgisi artık görünür uyarılarla işaretleniyor, Dışa Aktar artık hata mesajını gösteriyor. Aylar Arası Karşılaştırma\'ya ORTALAMA sütunu (Toplam Vaka\'da toplam da) eklendi. Ayrıca: Özel Değerlendirme\'de Oran(%) ve otomatik Eşik Aşım Oranı metrikleri, sütun/eşik filtreleri, Hariç Tutma sekmesi, kapsamlı isimlendirme ve arayüz iyileştirmeleri.',
  downloadUrl: 'https://raw.githubusercontent.com/gumusorhan-wq/istatistik-merkezi-112-dagitim/main/112-istatistik-merkezi.html'
};
