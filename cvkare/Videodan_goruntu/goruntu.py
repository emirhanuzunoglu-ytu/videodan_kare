import cv2
import os


cap = cv2.VideoCapture("Photos/video11.mp4")  # Videoyu aç
frame_number = 0  # Kaçıncı karede olduğumuzu takip etmek için

while True:  
    ret, frame = cap.read()  # Kareyi oku
    if not ret:  # Eğer video bittiyse döngüden çık
        break  

    filename = f"frames/frame_{frame_number:04d}.jpg"  # Dosya ismi oluştur
    cv2.imwrite(filename, frame)  # Kareyi kaydet
    frame_number += 1  # Bir sonraki kareye geç



# Kaydedilen karelerin olduğu klasörü göster
save_path = "frames"
print(f"Karelerin kaydedildiği dizin: {os.path.abspath(save_path)}")

# Eğer klasör yoksa oluştur
if not os.path.exists(save_path):
    print("Dizin bulunamadı, oluşturuluyor...")
    os.makedirs(save_path)

cap.release()  # Videoyu kapat
cv2.destroyAllWindows()  # Pencereyi kapat
