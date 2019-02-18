import cv2

img = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)  #grayscale fonksiyonu ile direk gri yapabilirsiniz ya da hiçbir şey yapmadan direk orjinal resmi kullanabilirsiniz.
img2 = cv2.imread('img1.jpg')   #resmi bulunduğunuz klasörden çekme. 
cv2.imshow('result', img)       #resmi ekrana bastırma işlemi
cv2.imshow('result2', img2)

cv2.waitKey(0)      #klavyeden bir input bekler.
cv2.destroyAllWindows()     #Bir tuşa basıldığında tüm pencereleri kapatır

