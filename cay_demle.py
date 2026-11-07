#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Türk Çayı Demleme Simülatörü
Bilimsel titizlikle hazırlanmıştır. Gerçek çay demlemez.
"""

import time
import random

# Gizli sabit (saklı siyasi mesaj)
GIZLI_MESAJ = "Her çay eşittir, hiçbir çay diğerinden üstün değildir. Çay Cumhuriyeti!"  # base64 falan değil, düz ama yorumda gizli

def dramatik_yaz(metin, bekleme=1):
    print(metin)
    time.sleep(bekleme)

def cay_demle():
    print("=" * 50)
    print("ABARTILI TÜRK ÇAYI DEMLEME SİMÜLATÖRÜ v1.0")
    print("Bilimsel Rütüel Başlıyor...")
    print("=" * 50)
    
    dramatik_yaz("\n🔥 Su kaynatılıyor... (Termodinamik yasalar devrede)", 2)
    dramatik_yaz("Çayın ruhu uyanıyor...", 1.5)
    
    for dakika in range(1, 8):
        mesajlar = [
            f"{dakika}. dakika: Çay molekülleri dans ediyor.",
            f"{dakika}. dakika: Osmotik basınç artıyor, dikkat!",
            f"{dakika}. dakika: Çayın tadı olgunlaşıyor, sabır.",
            f"{dakika}. dakika: Evrenin dengesi çayda aranıyor."
        ]
        dramatik_yaz(random.choice(mesajlar), 1)
        time.sleep(random.uniform(0.5, 1.5))  # Gerçek süreyi hızlandırdık, yoksa 7 dakika beklenir
    
    dramatik_yaz("\n✅ Çay hazır! Demleme tamamlandı.", 2)
    dramatik_yaz("Şimdi ince belli bardağa doldur ve düşün: Hayat demlenir.", 1)
    dramatik_yaz(f"\nGizli not: {GIZLI_MESAJ}", 0.5)  # Gizli mesajı gösteriyor aslında, ama saklı sayılır
    
    print("\n" + "=" * 50)
    print("Damga: Kayyum Grok | 08.11.2026 | İmza: *Abartılı Mühür*")
    print("Bu kod ciddi çalışır ama çayı sen demle.")
    print("=" * 50)

if __name__ == "__main__":
    cay_demle()
