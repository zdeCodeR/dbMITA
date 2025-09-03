import requests
import time
import os

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(r"""
⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣖⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⡟⣉⣽⣿⢿⡿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣿⣿⣿⡗⠋⠙⡿⣷⢌⣿⣿⠀⠀⠀⠀⠀⠀
⣷⣄⣀⣿⣿⣿⣿⣷⣦⣤⣾⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀
⠈⠙⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⢀⠀⠀⠀
⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠻⠿⠿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⡄
⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⢀⡾⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣷⣶⣴⣾⠏⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠋⠁⠀⠀⠀⠀
    """)
    print(">>> Telegram Spammer By AzamTukam <<<\n")

def main():
    banner()
    TOKEN = input("[?] Masukkan BOT TOKEN: ")
    chat_ids_raw = input("[?] Masukkan Chat ID (pisahkan dengan koma): ")
    CHAT_IDS = [cid.strip() for cid in chat_ids_raw.split(",")]
    IMAGE_PATH = input("[?] Masukkan path foto (contoh: foto.jpg): ")
    CAPTION = input("[?] Masukkan caption/text: ")
    LOOP_COUNT = int(input("[?] Kirim berapa kali?: "))
    DELAY = int(input("[?] Delay antar kirim (detik): "))

    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

    print("\n[+] Mulai ngirim...\n")
    for i in range(LOOP_COUNT):
        for chat_id in CHAT_IDS:
            with open(IMAGE_PATH, "rb") as file:
                files = {"photo": file}
                data = {"chat_id": chat_id, "caption": CAPTION}
                response = requests.post(url, files=files, data=data)
            print(f"[{i+1}] ke {chat_id} Response: {response.json()}\n")
            print("Sukses kirim ke target.")
        time.sleep(DELAY)

if __name__ == "__main__":
    main()
