// Merkezi Matris + Filtreleme Kuralları — settingsSyncChecker.js tarafından okunur.
// Bu dosya standalone HTML'e GÖMÜLMEZ; her zaman canlı sunucudan (bu repodan) çekilir.
// Yeni sürüm yayınlarken: Ayarlar > Dışa Aktar (.json) -> bu dosyanın içeriğini güncelle.
window.__SETTINGS_MANIFEST__ = {
  "magic": "huser-112-settings-sync",
  "schema": 1,
  "settingsVersion": 1,
  "exportedAt": "2026-09-09T00:10:17.159Z",
  "notes": "Merkez tarafından 9.09.2026 tarihinde güncellendi.",
  "matrix": {
    "1": {
      "genelToplam": {},
      "gkg16": {},
      "gkg17": {},
      "gkg20": {}
    },
    "2": {
      "genelToplam": {},
      "gkg15": {},
      "gkg16": {},
      "gkg17": {},
      "gkg20": {}
    },
    "3": {
      "genelToplam": {},
      "gkg09": {},
      "gkg15": {},
      "gkg16": {},
      "gkg17": {},
      "gkg20": {}
    },
    "4": {
      "genelToplam": {},
      "gkg15": {},
      "gkg16": {},
      "gkg17": {},
      "gkg20": {},
      "hastaneTeslim": {},
      "vakaKapatma": {},
      "icd10": {
        "sağlık tedbirleri": {
          "asılsız ihbar": true,
          "başka araçla nakil": true,
          "diğer": true,
          "ex - morga nakil": true,
          "ex - yerinde bırakıldı": true,
          "görev iptali": true,
          "nakil - eve": true,
          "nakil - hastaneler arası": true,
          "nakil - hastaneye": true,
          "nakil - red": true,
          "nakil - tıbbi tetkik için": true,
          "olay yerinde bekleme": true,
          "yaralı yok": true,
          "yerinde müdahale": true,
          "nakil - diğer": true
        },
        "protokol": {
          "asılsız ihbar": true,
          "başka araçla nakil": true,
          "diğer": true,
          "ex - morga nakil": true,
          "ex - yerinde bırakıldı": true,
          "görev iptali": true,
          "nakil - eve": true,
          "nakil - hastaneler arası": true,
          "nakil - hastaneye": true,
          "nakil - red": true,
          "nakil - tıbbi tetkik için": true,
          "olay yerinde bekleme": true,
          "yaralı yok": true,
          "yerinde müdahale": true,
          "nakil - diğer": true
        },
        "diğer": {
          "asılsız ihbar": true,
          "başka araçla nakil": true,
          "diğer": true,
          "görev iptali": true,
          "olay yerinde bekleme": true,
          "yaralı yok": true
        },
        "diğer kazalar": {
          "asılsız ihbar": true,
          "başka araçla nakil": true,
          "diğer": true,
          "görev iptali": true,
          "olay yerinde bekleme": true,
          "yaralı yok": true
        },
        "intihar": {
          "asılsız ihbar": true,
          "başka araçla nakil": true,
          "diğer": true,
          "görev iptali": true,
          "olay yerinde bekleme": true,
          "yaralı yok": true
        },
        "iş kazası": {
          "asılsız ihbar": true,
          "başka araçla nakil": true,
          "diğer": true,
          "görev iptali": true,
          "olay yerinde bekleme": true,
          "yaralı yok": true
        },
        "medikal": {
          "asılsız ihbar": true,
          "başka araçla nakil": true,
          "diğer": true,
          "görev iptali": true,
          "olay yerinde bekleme": true,
          "yaralı yok": true
        },
        "nakil": {
          "asılsız ihbar": true,
          "başka araçla nakil": true,
          "diğer": true,
          "görev iptali": true,
          "olay yerinde bekleme": true,
          "yaralı yok": true
        },
        "trafik kazası": {
          "asılsız ihbar": true,
          "başka araçla nakil": true,
          "diğer": true,
          "görev iptali": true,
          "olay yerinde bekleme": true,
          "yaralı yok": true
        },
        "yangın": {
          "asılsız ihbar": true,
          "başka araçla nakil": true,
          "diğer": true,
          "görev iptali": true,
          "olay yerinde bekleme": true,
          "yaralı yok": true
        },
        "yaralama": {
          "asılsız ihbar": true,
          "başka araçla nakil": true,
          "diğer": true,
          "görev iptali": true,
          "olay yerinde bekleme": true,
          "yaralı yok": true
        }
      }
    },
    "5": {
      "genelToplam": {},
      "gkg15": {},
      "gkg16": {},
      "gkg17": {},
      "gkg20": {},
      "hastaneTeslim": {},
      "vakaKapatma": {},
      "icd10": {},
      "istasyonDegerlendirme": {}
    }
  },
  "filters": {
    "m1ExcludedReasons": [
      "protokol",
      "sağlık tedbirleri"
    ],
    "m1ExcludedResults": [
      "nakil - eve",
      "nakil - hastaneler arası",
      "nakil - tıbbi tetkik için",
      "nakil - diğer",
      "olay yerinde bekleme",
      "diğer",
      "görev iptali"
    ],
    "m2ExcludedReasons": [
      "protokol",
      "sağlık tedbirleri"
    ],
    "m2ExcludedResults": [
      "nakil - eve",
      "nakil - hastaneler arası",
      "nakil - tıbbi tetkik için",
      "nakil - diğer",
      "olay yerinde bekleme",
      "diğer",
      "görev iptali"
    ],
    "m3ExcludedReasons": [
      "protokol",
      "sağlık tedbirleri"
    ],
    "m3ExcludedResults": [
      "nakil - eve",
      "nakil - hastaneler arası",
      "nakil - tıbbi tetkik için",
      "nakil - diğer",
      "olay yerinde bekleme",
      "diğer",
      "görev iptali"
    ],
    "gorenExcludedReasons1516": [
      "protokol",
      "sağlık tedbirleri",
      "nakil"
    ],
    "gorenExcludedReasons1720": [
      "protokol",
      "sağlık tedbirleri"
    ],
    "gorenIncludedResults": [
      "nakil - hastaneye",
      "yerinde müdahale",
      "ex - yerinde bırakıldı",
      "nakil - red",
      "başka araçla nakil",
      "asılsız ihbar",
      "yaralı yok"
    ]
  }
};
