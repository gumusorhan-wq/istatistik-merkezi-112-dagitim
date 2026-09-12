// Public manifest — mevcut sürüm bilgisi.
// Yeni sürüm yayınlarken bu dosyadaki version alanını güncelle. Bu dosya
// standalone HTML'e GÖMÜLMEZ; her zaman canlı sunucudan çekilir.
window.__APP_MANIFEST__ = {
  version: '0.9.30',
  released: '2026-09-12',
  notes: 'Modül 5 Harita: Chrome\'da "Access blocked / App is not following the tile usage policy" hatası düzeltildi. OpenStreetMap\'in kendi resmi sunucuları, uygulama içinden yapılan yoğun kullanımı politika ihlali sayıp engelliyordu (Safari\'de tesadüfen çalışıyordu). Harita alt yapısı artık bu tür kullanım için uygun, ücretsiz bir alternatif olan CARTO harita karolarına geçirildi — tüm tarayıcılarda çalışması gerekir. (Not: Mahalle isimlerindeki "Mah./Mh." gibi ek farklılıkları zaten önceden birleştiriliyordu, harita da bu birleşik veriyi kullanıyor.)',
  downloadUrl: 'https://raw.githubusercontent.com/gumusorhan-wq/istatistik-merkezi-112-dagitim/main/112-istatistik-merkezi.html'
};
