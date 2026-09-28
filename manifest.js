// Public manifest — mevcut sürüm bilgisi.
// Yeni sürüm yayınlarken bu dosyadaki version alanını güncelle. Bu dosya
// standalone HTML'e GÖMÜLMEZ; her zaman canlı sunucudan çekilir.
window.__APP_MANIFEST__ = {
  version: '1.0.07',
  released: '2026-09-28',
  notes: 'Özel Değerlendirme: Excel sütunlarından dinamik metrik seçimi geliştirildi — kimlik/kod/tarih alanları hariç tutuldu ("Ulaşım sn" süre sütunları hatalı hariç tutuluyordu, düzeltildi). Yeni FİLTRE: herhangi bir sütun+değer seçilip (ör. Kentsel/Kırsal = Kırsal) tüm metrikler sadece o vakalar üzerinden hesaplanır; filtre değerleri sol taraftaki seçili istasyonlara göre gelir. Başlık/filtre/indirme butonları tek satırda, Excel/Ay Ay/Toplu butonlarında anında açılan açıklama balonu. TOPLAM/ORTALAMA satırı hizası düzeltildi (tüm tablolarda). Hastane Teslim listesinde Nakledilen/Sevk Eden Hastane, harita lokasyon katmanları ve v1.0.06 içeriği dahil.',
  downloadUrl: 'https://raw.githubusercontent.com/gumusorhan-wq/istatistik-merkezi-112-dagitim/main/112-istatistik-merkezi.html'
};
