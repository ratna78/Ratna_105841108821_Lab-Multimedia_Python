from PIL import Image, ImageFilter
from pydub import AudioSegment

image = Image.open('contoh.jpg')

cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('cropped_result.jpg')

print("Gambar telah dipotong dan disimpan sebagai cropped_result.jpg")

resized_image = cropped_image.resize((100, 100))
resized_image.save('resized_result.jpg')

print("Gambar telah diubah ukuran dan disimpan sebagai resized_result.jpg")

filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('filtered_result.jpg')

print("Gambar telah difilter dan disimpan sebagai filtered_result.jpg")

audio = AudioSegment.from_file('Imagine Dragons.mp3')

audio.export('result.mp3', format='mp3')
print("File audio telah disimpan  sebagai result.mp3")

clipped_audio = audio[:10000]
clipped_audio.export('clipped_result.mp3', format='mp3')
print("Audio telah dipotong dan disimpan sebagai clipped_result.mp3")

print(f"Durasi asli: {len(audio) / 1000} detik")
print(f"Durasi hasil pemotongan: {len(clipped_audio) / 1000} detik")

combined_audio = audio + clipped_audio
combined_audio.export('combined_result.mp3', format='mp3')
print("Audio telah digabungkan dan disimpan sebagai combined_result.mp3")

audio.export('result.wav', format='wav')
print("File audio telah disimpan sebagai resul.wav")

louder_audio = audio + 10
louder_audio.export('louder_result.mp3', format='mp3')
print("Audio telah diperbesar volumenya dan disimpan sebagai louder_result.mp3")