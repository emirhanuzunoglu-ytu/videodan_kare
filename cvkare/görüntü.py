import cv2
import os

# Karelerin kaydedileceği dizini tanımla
save_path = "frames"

# Eğer klasör yoksa oluştur
if not os.path.exists(save_path):
    os.makedirs(save_path)

cap = cv2.VideoCapture("video/video11.mp4")  # Videoyu aç
frame_number = 0  # Kaçıncı karede olduğumuzu takip etmek için

while True:
    ret, frame = cap.read()  # Kareyi oku
    if not ret:  # Eğer video bittiyse döngüden çık
        break

    filename = os.path.join(save_path, f"frame_{frame_number:04d}.jpg")  # Dosya ismi oluştur
    cv2.imwrite(filename, frame)  # Kareyi kaydet
    frame_number += 1  # Bir sonraki kareye geç

cap.release()  # Videoyu kapat
cv2.destroyAllWindows()  # Pencereyi kapat

print(f"Karelerin kaydedildiği dizin: {os.path.abspath(save_path)}")
