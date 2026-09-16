// Public manifest — mevcut sürüm bilgisi.
// Yeni sürüm yayınlarken bu dosyadaki version alanını güncelle. Bu dosya
// standalone HTML'e GÖMÜLMEZ; her zaman canlı sunucudan çekilir.
window.__APP_MANIFEST__ = {
  version: '0.9.40',
  released: '2026-09-16',
  notes: 'Arşiv: Matris (Modül × Kombinasyon hariç tutmaları) güncellendiğinde, arşivdeki eski aylar artık otomatik yeniden hesaplanıyor. Önceden yalnızca hesaplama mantığı (kod) değiştiğinde otomatik güncelleme tetikleniyordu — Matris içeriği değiştiğinde bu hiç yakalanmıyordu. Her arşivlenen aya artık kullanılan Matris\'in bir "parmak izi" de kaydediliyor; ay açıldığında güncel Matris ile karşılaştırılıp farklıysa (ham veri varsa) sessizce yeniden hesaplanıyor.',
  downloadUrl: 'https://raw.githubusercontent.com/gumusorhan-wq/istatistik-merkezi-112-dagitim/main/112-istatistik-merkezi.html'
};
