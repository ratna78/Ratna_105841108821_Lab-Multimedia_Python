import tkinter as tk
from PIL import Image, ImageTk

# Membuat jendela utama
root = tk.Tk()
root.title("Multimedia Application")

# Menjalankan loop acara Tkinter
root.mainloop()

image = Image.open('contoh.jpg')
photo = ImageTk.PhotoImage(image)

# Membuat label untuk menampilkan gambar
label = tk.Label(root, image=photo)
label.pack()
