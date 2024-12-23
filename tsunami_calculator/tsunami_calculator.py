import math

def tsunami_speed(depth: float) -> float:
    """Dalga hızını hesaplar."""
    g = 9.81  # Yerçekimi ivmesi (m/s^2)
    return math.sqrt(g * depth)

def arrival_time(distance: float, speed: float) -> float:
    """Tsunaminin kıyıya ulaşma süresini hesaplar."""
    if speed == 0:
        raise ValueError("Dalga hızı sıfır olamaz.")
    return distance / speed

def tsunami_wave_height(magnitude: float) -> float:
    """Deprem büyüklüğüne göre tahmini dalga yüksekliğini hesaplar."""
    k = 1.5  # Denge faktörü
    return k * 10 ** (0.5 * magnitude - 3)

def tsunami_wavelength(speed: float, period: float = 1800) -> float:
    """Tsunami dalga boyunu hesaplar."""
    return speed * period

def tsunami_energy(height: float, wavelength: float, width: float = 100000) -> float:
    """Tsunami dalgasının enerjisini hesaplar."""
    rho = 1025  # Su yoğunluğu (kg/m³)
    g = 9.81  # Yerçekimi ivmesi (m/s²)
    return 0.5 * rho * g * height**2 * wavelength * width

def test_scenario(depth, distance, magnitude):
    """Belirli bir senaryoyu çalıştır ve sonuçları yazdır."""
    speed = tsunami_speed(depth)
    time = arrival_time(distance * 1000, speed)  # km -> m dönüşümü
    height = tsunami_wave_height(magnitude)
    wavelength = tsunami_wavelength(speed)
    energy = tsunami_energy(height, wavelength)

    print(f"\n🌊 **Senaryo:** Derinlik={depth}m, Mesafe={distance}km, Büyüklük={magnitude}")
    print(f"Tsunami Dalga Hızı: {speed:.2f} m/s")
    print(f"Kıyıya Ulaşma Süresi: {time / 60:.2f} dakika")
    print(f"Tahmini Tsunami Dalga Yüksekliği: {height:.2f} metre")
    print(f"Tsunami Dalga Boyu: {wavelength:.2f} metre")
    print(f"Tsunami Enerjisi: {energy:.2e} Joule")

def main():
    try:
        # Kullanıcıya ön tanımlı senaryoları çalıştırmak isteyip istemediğini sorma
        run_predefined_scenarios = input("Ön tanımlı tsunami senaryolarını çalıştırmak ister misiniz? (E/H): ").strip().lower()
        if run_predefined_scenarios == 'e':
            print("📌 **Ön Tanımlı Tsunami Senaryoları Çalıştırılıyor...**")
            # 1️⃣ Hint Okyanusu - 2004 Depremi
            test_scenario(depth=4000, distance=100, magnitude=9.1)
            # 2️⃣ Japonya - 2011 Tohoku Depremi
            test_scenario(depth=6000, distance=70, magnitude=9.0)

        print("\n📌 **Şimdi kendi verilerinizi girerek hesaplama yapabilirsiniz!**\n")

        # Kullanıcıdan veri alma
        depth = float(input("Okyanus derinliğini (metre cinsinden) girin: "))
        distance = float(input("Deprem merkez üssü ile kıyı arasındaki mesafeyi (km cinsinden) girin: "))
        magnitude = float(input("Depremin büyüklüğünü (Mw cinsinden) girin: "))

        # Negatif değer kontrolü
        if depth <= 0 or distance <= 0 or magnitude <= 0:
            raise ValueError("Derinlik, mesafe ve büyüklük pozitif olmalıdır.")

        # Birimleri çevirme
        distance *= 1000  # km'yi metreye çevirme

        # Hesaplamalar
        speed = tsunami_speed(depth)
        time = arrival_time(distance, speed)
        height = tsunami_wave_height(magnitude)
        wavelength = tsunami_wavelength(speed)
        energy = tsunami_energy(height, wavelength)

        # Sonuçları ekrana yazdırma
        print(f"\n🔹 **Sizin Girdiğiniz Veriler İçin Sonuçlar:**")
        print(f"Tsunami Dalga Hızı: {speed:.2f} m/s")
        print(f"Kıyıya Ulaşma Süresi: {time / 60:.2f} dakika")
        print(f"Tahmini Tsunami Dalga Yüksekliği: {height:.2f} metre")
        print(f"Tsunami Dalga Boyu: {wavelength:.2f} metre")
        print(f"Tsunami Enerjisi: {energy:.2e} Joule")

    except OSError:
        print("Giriş/Çıkış hatası: Bu ortamda input fonksiyonu desteklenmiyor.")
    except ValueError as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    main()
