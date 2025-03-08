import cv2
import os


cap = cv2.VideoCapture("video/video11.mp4")

# FPS değerini al (videonun saniyede kaç kare olduğunu öğren)
fps = int(cap.get(cv2.CAP_PROP_FPS))
print(f"Video FPS: {fps}") 

# Kaç saniyede bir kare alacağımızı belirle
interval = 2  # Her 1 saniyede bir kare almak için
frame_interval = fps * interval  # Örneğin: 30 FPS * 1 saniye = 30. Yani her 30. kareyi kaydet

# Çıktı klasörünü oluştur
output_folder = "frames"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

frame_number = 0  # Videodaki toplam kare numarası
saved_frames = 0  # Kaydedilen kare sayısı

while True:
    ret, frame = cap.read()  # Kareyi oku
    if not ret:
        break  # Video bittiyse döngüyü durdur

    # Eğer şu anki kare numarası belirlenen aralığa denk geliyorsa kaydet
    if frame_number % frame_interval == 0:
        filename = f"{output_folder}/frame_{saved_frames:04d}.jpg"
        cv2.imwrite(filename, frame)  # Kareyi kaydet
        print(f"Kare kaydedildi: {filename}")
        saved_frames += 1

    frame_number += 1  # Bir sonraki kareye geç

cap.release()
cv2.destroyAllWindows()
print(f"Toplam kaydedilen kare sayısı: {saved_frames}")
