#! .Python3-env/bin/python

#Program Libraries
import cv2

#Read imagens
imagem = cv2.imread("imgOriginal.tif", cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", imagem)

#cv2.imwrite('gray_image.png',gray_image)
 
#print "Altura (height): %d pixels" % (imagem.shape[0])
#print "Largura (width): %d pixels" % (imagem.shape[1])
#print "Canais (channels): %d"      % (imagem.shape[2])
    
cv2.waitKey(0)