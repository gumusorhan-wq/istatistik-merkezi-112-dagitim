// Public manifest — mevcut sürüm bilgisi.
// Yeni sürüm yayınlarken bu dosyadaki version alanını güncelle. Bu dosya
// standalone HTML'e GÖMÜLMEZ; her zaman canlı sunucudan çekilir.
window.__APP_MANIFEST__ = {
  version: '0.9.25',
  released: '2026-09-11',
  notes: 'Güncelleme kontrolü artık önce standart fetch() ile deniyor, başarısız olursa eski <script> yöntemine düşüyor. Bazı kurumsal ağ/güvenlik yazılımları dinamik <script src=...> isteklerini engelleyip normal fetch isteklerine izin verebiliyor — bu değişiklik, "sunucudan sürüm bilgisi alınamadı" hatasını bu tür ağlarda çözmeyi amaçlıyor. Aynı düzeltme Matris/Filtre senkron kontrolüne de uygulandı.',
  downloadUrl: 'https://raw.githubusercontent.com/gumusorhan-wq/istatistik-merkezi-112-dagitim/main/112-istatistik-merkezi.html'
};
