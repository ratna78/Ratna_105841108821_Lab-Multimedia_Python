from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips
from moviepy.editor import vfx
import tkinter as tk
from PIL import Image, ImageTk


# Memuat file video
video = VideoFileClip('satumenit.mp4')

# Menyimpan file video
video.write_videofile('result.mp4')

short_video = video.subclip(0, 10)  # Mendapatkan 10 detik pertama
short_video.write_videofile('short_result.mp4')

combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('combined_result.mp4')

reversed_video = short_video.fx(vfx.time_mirror)  # Membalikkan video
reversed_video.write_videofile('reversed_result.mp4')

sped_up_video = short_video.fx(vfx.speedx, 2)  # Mempercepat video 2x
sped_up_video.write_videofile('sped_up_result.mp4')

root = tk.Tk()
root.title("Multimedia Application")

# Menjalankan loop acara Tkinter
root.mainloop()

image = Image.open('contoh.jpg')
photo = ImageTk.PhotoImage(image)

# Membuat label untuk menampilkan gambar
label = tk.Label(root, image=photo)
label.pack()
