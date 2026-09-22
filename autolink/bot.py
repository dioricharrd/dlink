import random
import time
from playwright.sync_api import sync_playwright


def run_automation(target_url, total_loops):
  with sync_playwright() as p:
    for i in range(1, total_loops + 1):
      print(f"\n[*] Siklus {i} dari {total_loops} dimulai...")

      browser = p.chromium.launch(
        headless=True,
        args=["--no-sandbox", "--disable-dev-shm-usage"],
      )
      context = browser.new_context(
        user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
      )
      page = context.new_page()

      try:
        page.goto(target_url, wait_until="domcontentloaded", timeout=60000)
        print(f"[SUKSES] Berhasil membuka halaman: {target_url}")

        stay_duration = random.randint(1, 20)
        print(f"[*] Menahan sesi selama {stay_duration} detik...")
        time.sleep(stay_duration)

      except Exception as e:
        print(f"[ERROR] Terjadi kendala pada siklus {i}: {e}")

      finally:
        # 3. Tutup browser sepenuhnya
        browser.close()
        print(f"[SUKSES] Sesi {i} ditutup.")

      if i < total_loops:
        cooldown = 3
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