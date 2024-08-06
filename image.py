from PIL import Image

# Memuat gambar
image = Image.open('contoh.jpg')

# Menyimpan gambar
image.save('result.jpg')

print("Gambar telah diproses dan disimpan sebagai result.jpg")
