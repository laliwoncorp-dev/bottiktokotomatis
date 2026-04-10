import os
import random
from moviepy.editor import ColorClip, TextClip, CompositeVideoClip
from gtts import gTTS

def buat_video_otomatis():
    # 1. Daftar Konten (Bisa kamu tambah sebanyak mungkin)
    quotes = [
        "Disiplin adalah jembatan antara cita-cita dan pencapaian.",
        "Jangan menunggu kesempatan, ciptakanlah.",
        "Kerja keras mengalahkan bakat ketika bakat tidak bekerja keras.",
        "Masa depanmu ditentukan oleh apa yang kamu lakukan hari ini."
    ]
    
    warna_latar = [(20, 20, 20), (0, 51, 102), (102, 0, 0), (0, 102, 51)]
    
    # 2. Pilih secara acak
    teks = random.choice(quotes)
    warna = random.choice(warna_latar)
    
    print(f"Memproses video dengan teks: {teks}")

    # 3. Buat Suara (TTS)
    tts = gTTS(teks, lang='id')
    tts.save("audio.mp3")
    
    # 4. Buat Video (Sederhana dulu agar cepat di GitHub Actions)
    # Ukuran TikTok 1080x1920
    bg = ColorClip(size=(1080, 1920), color=warna).set_duration(7)
    
    txt = TextClip(teks, fontsize=70, color='white', font='Arial-Bold', 
                   method='caption', size=(900, None), align='center')
    txt = txt.set_position('center').set_duration(7)
    
    video = CompositeVideoClip([bg, txt])
    
    # 5. Export
    video.write_videofile("hasil_video.mp4", fps=24, codec="libx264")
    print("Video berhasil dibuat!")

if __name__ == "__main__":
    buat_video_otomatis()
