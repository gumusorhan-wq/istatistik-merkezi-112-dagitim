// Public manifest — mevcut sürüm bilgisi.
// Yeni sürüm yayınlarken bu dosyadaki version alanını güncelle. Bu dosya
// standalone HTML'e GÖMÜLMEZ; her zaman canlı sunucudan çekilir.
window.__APP_MANIFEST__ = {
  version: '0.9.29',
  released: '2026-09-12',
  notes: 'Modül 5 Harita — iki düzeltme: (1) Aynı isimli mahalleler farklı ilçelerde üst üste/çok yakın konuma düşüp yanlış vaka sayısı gösterme sorunu düzeltildi — çakışan noktalar artık küçük bir daire üzerine dağıtılır (turuncu). (2) Konum bulma başarı oranı ciddi şekilde artırıldı: artık her mahalle için birden fazla sorgu biçimi sırayla denenir ve arama Manisa iliyle sınırlandırılır; ayrıca başarısız aramalar artık kalıcı olarak "bulunamadı" damgalanmıyor — bir sonraki "Haritayı Oluştur" tıklamasında yeniden denenir.',
  downloadUrl: 'https://raw.githubusercontent.com/gumusorhan-wq/istatistik-merkezi-112-dagitim/main/112-istatistik-merkezi.html'
};
