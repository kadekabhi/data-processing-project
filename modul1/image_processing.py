from PIL import Image
import cv2

# dummy image

try:
    img = Image.new('RGB', (200,100), color = 'red')
    img.save('Untitled.png')
except ImportError:
    print("Pillow tidak terinstall. silahkan install dengan 'pip install pillow'.")

try:
    image = cv2.imread('Untitled.png')
    if image is None:
        raise FileNotFoundError
    print("Ukuran gambar (tinggi, lebar, channel):", image.shape)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("ukuran gambar grayscale:", gray_image.shape)
    edges = cv2.Canny(gray_image, 100, 200)
    cv2.imwrite('Untitled_grayscale.png', gray_image)
    cv2.imwrite('Untitled_tepi.png', edges)
    print("\nGambar grayscale dan tepi berhasil disimpan.")

except FileNotFoundError:
    print("Pastikan file 'Untitled.png' ada di direktori yang sama.")
except cv2.error as e:
    print(f"Terjadi kesalahan openCV: {e}")