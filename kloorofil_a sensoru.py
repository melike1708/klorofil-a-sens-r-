import random
import time

def simulate_chlorophyll_a():
    # Klorofil a konsantrasyonu 0 ile 100 µg/L arasında rastgele bir değer oluştur.
    chlorophyll_a_level = round(random.uniform(0, 100), 2)  # 0 to 100 µg/L
    return chlorophyll_a_level

try:
    while True:
        # Klorofil a için simülasyonu yap.
        simulated_chlorophyll_a = simulate_chlorophyll_a()

        # Simüle edilen klorofil a konsantrasyonunu yazdır.
        print(f"Simulated Chlorophyll A Level: {simulated_chlorophyll_a} µg/L")

        # 1 saniye bekle.
        time.sleep(1)

except KeyboardInterrupt:
    print("Simülasyon durduruldu.")
except Exception as e:
    print(f"Bir hata oluştu: {e}")
