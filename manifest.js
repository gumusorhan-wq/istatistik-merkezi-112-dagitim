// Public manifest — mevcut sürüm bilgisi.
// Yeni sürüm yayınlarken bu dosyadaki version alanını güncelle. Bu dosya
// standalone HTML'e GÖMÜLMEZ; her zaman canlı sunucudan çekilir.
window.__APP_MANIFEST__ = {
  version: '0.9.32',
  released: '2026-09-12',
  notes: 'Modül 5 Harita tamamen yeniden yapıldı: artık dış harita/konum servislerine (OpenStreetMap, CARTO, Esri, Nominatim) HİÇ bağımlı değil — bu servisler sık sık erişimi kesiyordu (403, "API KEY REQUIRED" vb.). Bunun yerine Manisa\'nın 17 ilçesini şematik olarak gösteren, tamamen bu bilgisayarda anında oluşan bir SVG harita kullanılıyor. Konum bulma beklemesi kalktı, sekme açılır açılmaz veya ay/kapsam değiştirildiğinde anında güncelleniyor. Bundle boyutu da küçüldü (Leaflet kaldırıldı).',
  downloadUrl: 'https://raw.githubusercontent.com/gumusorhan-wq/istatistik-merkezi-112-dagitim/main/112-istatistik-merkezi.html'
};
