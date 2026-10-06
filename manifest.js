// Public manifest — mevcut sürüm bilgisi.
// Yeni sürüm yayınlarken bu dosyadaki version alanını güncelle. Bu dosya
// standalone HTML'e GÖMÜLMEZ; her zaman canlı sunucudan çekilir.
window.__APP_MANIFEST__ = {
  version: '1.0.15',
  released: '2026-10-06',
  notes: 'DÜZELTME: Özel Değerlendirme\'de arşiv aylarında sütunlar artık her ay için başlık adına göre bulunuyor (değer/eşik filtresi, metrikler, ortak vaka). Sütun yeri aydan aya değiştiğinde filtrelenen sayıların eksik çıkması (ör. Sevk Edilen İl - il dışı) giderildi. Değer filtresi listesi artık seçili tüm aylardaki değerleri gösteriyor. Başlıklarda büyük/küçük harf ve boşluk farkları önemsenmiyor; başlık bilgisi olmayan eski arşiv aylarında sütun haritası kullanılıyor.',
  downloadUrl: 'https://raw.githubusercontent.com/gumusorhan-wq/istatistik-merkezi-112-dagitim/main/112-istatistik-merkezi.html'
};
