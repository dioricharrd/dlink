import random
import time
from playwright.sync_api import sync_playwright


def run_automation(target_url, total_loops):
  with sync_playwright() as p:
    for i in range(1, total_loops + 1):
      print(f"\n[*] Siklus {i} dari {total_loops} dimulai...")

      # Buka browser (headless=False agar jendela Chrome terlihat)
      browser = p.chromium.launch(headless=False)
      context = browser.new_context()
      page = context.new_page()

      try:
        # 1. Buka link web dari input user
        page.goto(target_url)
        print(f"[SUKSES] Berhasil membuka halaman: {target_url}")

        # 2. Stay/diam selama rentang waktu acak (10 - 30 detik)
        stay_duration = random.randint(10, 30)
        print(f"[*] Menahan sesi selama {stay_duration} detik...")
        time.sleep(stay_duration)

      except Exception as e:
        print(f"[ERROR] Terjadi kendala pada siklus {i}: {e}")

      finally:
        # 3. Tutup browser sepenuhnya
        browser.close()
        print(f"[SUKSES] Sesi {i} ditutup.")

      # Jeda singkat antar perulangan
      if i < total_loops:
        cooldown = random.randint(3, 6)
        print(f"[*] Jeda {cooldown} detik sebelum siklus berikutnya...")
        time.sleep(cooldown)


if __name__ == "__main__":
  print("=" * 45)
  print("   TERMINAL PLAYWRIGHT AUTOMATION BOT")
  print("=" * 45)

  # User memasukkan link web interaktif
  target_url = input("Masukkan link web yang dituju: ").strip()

  # Validasi otomatis jika user lupa menuliskan https://
  if not target_url.startswith(("http://", "https://")):
    target_url = "https://" + target_url

  # User memasukkan jumlah loop
  try:
    total_loops = int(input("Masukkan jumlah pengulangan (loop): "))
  except ValueError:
    total_loops = 1
    print("[!] Input tidak valid, otomatis diset ke 1 loop.")

  print(f"\n[INFO] Menjalankan bot untuk target: {target_url}")
  print(f"[INFO] Total perulangan: {total_loops} kali\n")

  # Eksekusi fungsi utama
  run_automation(target_url, total_loops)