// Public manifest — mevcut sürüm bilgisi.
// Yeni sürüm yayınlarken bu dosyadaki version alanını güncelle. Bu dosya
// standalone HTML'e GÖMÜLMEZ; her zaman canlı sunucudan çekilir.
window.__APP_MANIFEST__ = {
  version: '0.9.34',
  released: '2026-09-13',
  notes: 'Modül 5 Harita — konum bulma tamamen yeniden tasarlandı: artık her mahalle (700+) değil, sadece İLÇE merkezleri (tipik 15-20 tane) internetten bulunuyor — bu yüzden saniyeler içinde bitiyor (önceden 15-50 dakika sürebiliyordu) ve "eksik" mahalle kalmıyor. Her ilçenin mahalleleri, o ilçenin gerçek konumunun etrafına otomatik ve düzgün şekilde dağıtılıyor (konum ilçe hassasiyetindedir, tam adres değildir).',
  downloadUrl: 'https://raw.githubusercontent.com/gumusorhan-wq/istatistik-merkezi-112-dagitim/main/112-istatistik-merkezi.html'
};
