# 112 İstatistik Merkezi — Stok Takip Entegrasyon Sözleşmesi

Sürüm 1 · 25.10.2026 · Uygulama sürümü v1.0.27 ve sonrası

Bu belge, 112 İstatistik Merkezi'nin Stok Takip içine gömülerek il bazlı **Kurum Arşivi** ile çalışması için Stok Takip tarafında yapılması gerekenleri tanımlar. Uygulama tarafı hazırdır; Stok Takip yalnızca aşağıdaki `window.__IM112_HOST` nesnesini sağlar ve sunucu tarafını kurar.

## 1. Genel yapı

- Uygulama tek HTML dosyasıdır; bütün hesaplamalar kullanıcının tarayıcısında yapılır. Sunucu yalnızca **ay paketlerini saklar** ve **yetki kontrolü** yapar.
- Her il ayrı bir depodur. Kullanıcı yalnızca kendi ilinin deposunu görür; süper admin tüm illeri görür.
- Kurum Arşivi modunda Google Drive, ekip parolası ve paket şifrelemesi **kullanılmaz**. Erişimi Stok Takip'in oturum ve yetki sistemi korur.
- `window.__IM112_HOST` tanımlı değilse uygulama eskisi gibi Ortak Arşiv (Google Drive) ile çalışır.

## 2. Roller

| Rol (`rol`) | Görme | Yükleme | Silme | İl seçimi |
|---|---|---|---|---|
| `kullanici` | Kendi ili | — | — | — |
| `il_admin` | Kendi ili | Kendi iline | Kendi ilinden | — |
| `super_admin` | Tüm iller | Her ile | Her ilden | Var (açılır liste) |

Uygulama bu kuralları arayüzde uygular, ancak **asıl kontrol sunucuda yapılmalıdır**: her yükleme ve silme isteğinde oturumdaki kullanıcının rolü ve ili sunucuda yeniden doğrulanmalıdır.

## 3. Sayfaya gömme

Uygulamayı yükleyen Stok Takip sayfası, uygulama betiğinden **önce** şunları tanımlar:

```html
<script>
  window.__IM112_YUKLEYICI = 1;          // gömülü mod: güncelleme uyarısı çıkmaz
  window.__IM112_HOST = { /* bölüm 4 */ };
</script>
<!-- ardından 112-istatistik-merkezi.html içeriği / iframe -->
```

## 4. `window.__IM112_HOST` sözleşmesi

Bütün fonksiyonlar `Promise` döndürür. İl adları büyük harf ve Türkçe karakterli yazılır (`"MANİSA"`, `"İZMİR"`), GVA Excel'indeki "Şehir" sütunuyla aynı olmalıdır.

```js
window.__IM112_HOST = {
  surum: 1,

  // Oturumdaki kullanıcı
  kullanici: async () => ({
    id: "123",                 // Stok Takip kullanıcı kimliği
    ad: "Ayşe Yılmaz",         // ekranda ve "Yükleyen" sütununda görünür
    rol: "il_admin",           // "kullanici" | "il_admin" | "super_admin"
    il: "MANİSA"               // kullanıcının bağlı olduğu il
  }),

  // Yalnızca super_admin için çağrılır: seçilebilecek iller
  iller: async () => ["AMASYA", "MANİSA", "İZMİR"],

  arsiv: {
    // İlin deposundaki aylar
    listele: async (il) => [
      { ym: "2026-09", boyut: 11743210, guncelleme: "2026-10-10T08:15:00Z", yukleyen: "Ayşe Yılmaz" }
    ],
    // Ay paketini ham bayt olarak döndürür (ArrayBuffer veya Uint8Array)
    indir: async (il, ym) => arrayBuffer,
    // Ay paketini kaydeder; aynı il+ay varsa üzerine yazar
    yukle: async (il, ym, veri /* Uint8Array */, meta) => {},
    // Ayı depodan siler
    sil: async (il, ym) => {}
  },

  // İsteğe bağlı: yükleme sonrası özet ve brifing Excel dosyaları
  ozetYukle: async (il, ym, dosyaAdi, blob) => {}
};
```

Kurallar:

- `guncelleme` her yüklemede değişmelidir (ISO tarih önerilir). Uygulama bir ayı yalnızca bu değer değiştiğinde yeniden indirir.
- Hata durumunda fonksiyon `Error` fırlatmalıdır; mesajı kullanıcıya gösterilir (örn. `throw new Error("Yetkiniz yok")`).
- `meta` alanı: `{ dosya, satir, surum, schema }` — kayıt için bilgi amaçlıdır.
- `ozetYukle` tanımlı değilse özet dosyaları gönderilmez.

## 5. Paket biçimi

- İlk 9 bayt `IM112ZIP1`, devamı gzip ile sıkıştırılmış JSON.
- İçerik: ayın GVA satırları, kolon eşlemesi, hesaplanmış sonuçlar ve branş atamaları.
- Hasta adı/soyadı, T.C. kimlik, telefon, ihbar eden ve bileklik numarası paketlenmeden önce `*` ile maskelenir; açıklama alanlarındaki isimler gizlenir. Yine de paket **sağlık verisi** içerir.
- Boyut: Manisa için ay başına yaklaşık 11–12 MB (14.000 satır); il başına yılda yaklaşık 150 MB.
- Sunucu paketi açmak zorunda değildir; olduğu gibi saklayıp geri vermesi yeterlidir.

## 6. Önerilen sunucu uç noktaları

Stok Takip kendi API'sini istediği gibi kurabilir; host nesnesi bu uçlara `fetch` ile bağlanır. Örnek:

| İşlem | Uç nokta | Yetki |
|---|---|---|
| Liste | `GET /api/im112/{il}/aylar` | Oturum + (il = kullanıcı ili veya super_admin) |
| İndir | `GET /api/im112/{il}/aylar/{ym}` | Aynı |
| Yükle | `PUT /api/im112/{il}/aylar/{ym}` (gövde: ikili, en fazla ~40 MB) | il_admin (kendi ili) veya super_admin |
| Sil | `DELETE /api/im112/{il}/aylar/{ym}` | il_admin (kendi ili) veya super_admin |
| Özet | `PUT /api/im112/{il}/ozet/{ym}/{dosya}` | Yükleme yetkisi |
| İller | `GET /api/im112/iller` | super_admin |

Veritabanı tarafında bir tablo yeterlidir: `il, ym, veri (blob veya dosya yolu), boyut, guncelleme, yukleyen_id` — `(il, ym)` benzersiz.

## 7. Uygulama tarafında hazır olanlar

- **Kurum Arşivi paneli** (Arşiv sayfası): ilin ayları, boyut, güncelleme, yükleyen; il admini/süper admin için "Yükle" ve "Sil"; süper admin için il seçimi.
- **Açılışta eşitleme:** ilin yeni veya güncellenmiş ayları otomatik iner; süper admin il değiştirince eski ilin ayları cihazdan kaldırılır.
- **İl kontrolü:** Yüklenen ayın ili ("Şehir" sütunu) depo iliyle aynı değilse yükleme reddedilir.
- **İl bazlı hesaplama:** İl içi/dışı sevk ayrımı, istasyon adı kısaltma ve il dışı branş değerlendirmesi verinin iline göre yapılır; il içi anahtar kelimeleri Ayarlar'da il bazında düzenlenir.

## 8. KVKK ve güvenlik

- Bağlantı yalnızca HTTPS; uçlar oturumsuz erişime kapalı.
- Yükleme, indirme ve silme işlemleri kullanıcı, il, ay ve zaman bilgisiyle kayıt altına alınmalı.
- Saklama süresi ve silme politikası kurum tarafından belirlenmeli; süper admin silme yetkisine sahiptir.
- Paketler şifresiz saklandığı için sunucu diski ve yedekleri kurum içi güvenlik kurallarına tabi olmalı.

## 9. Dosyalar ve güncel tutma

- Bu entegrasyon sürümü GitHub deposunda ayrı **`stoktakip-entegrasyon`** dalında tutulur; canlı site (`main`) bundan etkilenmez.
- Dalda: `112-istatistik-merkezi.html` (Kurum Arşivi destekli sürüm), bu belge ve `test/` klasöründe sahte host (`mock-host.js`) ile sahte sunucu (`mock-srv.py`).
- Canlı sistemde yapılan her değişiklik aynı kaynaktan iki ayrı derlemeyle üretilir; her yayında `main` ve `stoktakip-entegrasyon` birlikte güncellenir.

## 10. Test

Uygulama deposunda sahte bir host ile test edildi: Manisa il admini yükledi; Manisa kullanıcısı ayı otomatik indirdi ve yükleme/silme düğmesi görmedi; Amasya il admini kendi ilini yükledi, Manisa deposuna yükleme denemesi reddedildi; süper admin il değiştirip eşitledi ve sildi. Stok Takip geliştiricisi aynı senaryolarla kendi sunucusunu doğrulayabilir.
