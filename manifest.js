// Public manifest — mevcut sürüm bilgisi.
// Yeni sürüm yayınlarken bu dosyadaki version alanını güncelle. Bu dosya
// standalone HTML'e GÖMÜLMEZ; her zaman canlı sunucudan çekilir.
window.__APP_MANIFEST__ = {
  version: '1.0.02',
  released: '2026-09-21',
  notes: 'KRİTİK veri doğruluğu düzeltmesi: Excel\'de bazı "doluluk" kolonlarında (özellikle Akıllı Bileklik No) gerçek veri girilmemiş satırlar tamamen boş bırakılmak yerine tek bir "-" (tire) karakteriyle dolduruluyordu. Sistem bunu yanlışlıkla "dolu" (kullanılmış) sayıyordu — bu yüzden Temmuz 2026 gibi hiç Akıllı Bileklik kullanılmayan aylarda bile bazı istasyonlarda sahte "kullanılmış" sayıları görünüyordu. Artık sadece tire(ler)den oluşan değerler de boş sayılıyor. Gerçek Temmuz/Ağustos 2026 verisiyle doğrulandı: Temmuz artık doğru şekilde 0 gösteriyor, Ağustos\'ta sadece gerçek bileklik kodları (1920→0 ve 8471→6415 gibi) sayılıyor. Aynı koruma ICD-10 doluluk kontrolüne ve Vaka Kapatma "kapalı mı?" kontrolüne de önlem amaçlı eklendi.',
  downloadUrl: 'https://raw.githubusercontent.com/gumusorhan-wq/istatistik-merkezi-112-dagitim/main/112-istatistik-merkezi.html'
};
