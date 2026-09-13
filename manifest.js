// Public manifest — mevcut sürüm bilgisi.
// Yeni sürüm yayınlarken bu dosyadaki version alanını güncelle. Bu dosya
// standalone HTML'e GÖMÜLMEZ; her zaman canlı sunucudan çekilir.
window.__APP_MANIFEST__ = {
  version: '0.9.35',
  released: '2026-09-13',
  notes: 'Modül 5 Harita: kullanıcı isteği üzerine ilçe-merkezli yaklaşık gösterimden GERÇEK mahalle bazlı konuma geri dönüldü — her mahalle kendi gerçek konumunda gösteriliyor (ör. Yunusemre Muradiye Mahallesi kendi yerinde). Bunun için konum bulma yeniden mahalle başına ~1-4 saniye sürüyor. Ayrıca birbirine çok yakın mahalleler artık Leaflet.markercluster ile sayı rozetli gruplar halinde gösteriliyor — tıklanınca veya yakınlaşınca otomatik ayrı ayrı görünürler (görsel karmaşayı azaltır).',
  downloadUrl: 'https://raw.githubusercontent.com/gumusorhan-wq/istatistik-merkezi-112-dagitim/main/112-istatistik-merkezi.html'
};
