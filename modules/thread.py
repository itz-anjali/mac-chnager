import threading
import time

# Pehla kaam: Game Download
def download_game():
    print("📥 Game download shuru...")
    time.sleep(3)  # Maan lo 3 second lag rahe hain
    print("✅ Game download complete!")

# Dusra kaam: Music Play
def play_music():
    for i in range(3):
        print("🎵 Music chal raha hai...")
        time.sleep(1) # Har 1 second baad beat bajti hai

# --- Main Program ---

# Do alag threads (workers) banaye
thread1 = threading.Thread(target=download_game)
thread2 = threading.Thread(target=play_music)

# Dono ko start kiya
thread1.start()
thread2.start()

# wait karte hain dono ke khatam hone ka
thread1.join()
thread2.join()

print("🎉 Sab kaam khatam!")