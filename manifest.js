// Public manifest — mevcut sürüm bilgisi.
// Yeni sürüm yayınlarken bu dosyadaki version alanını güncelle. Bu dosya
// standalone HTML'e GÖMÜLMEZ; her zaman canlı sunucudan çekilir.
window.__APP_MANIFEST__ = {
  version: '0.9.27',
  released: '2026-09-12',
  notes: '"İndir" düğmeleri düzeltildi. GitHub\'ın ham dosya sunucusu .html dosyalarını güvenlik nedeniyle her zaman düz metin olarak gönderiyordu; bu yüzden "İndir"e basınca dosya inmek yerine kaynak kodu ekrana dökülüyordu. Artık dosya JS ile indirilip gerçek bir indirme penceresi tetikleniyor (Güncelleme bildirimi, Ayarlar > HTML Olarak İndir ve Ayarlar > Güncelleme Kontrolü Yap sonucundaki tüm indirme düğmeleri için geçerli).',
  downloadUrl: 'https://raw.githubusercontent.com/gumusorhan-wq/istatistik-merkezi-112-dagitim/main/112-istatistik-merkezi.html'
};
