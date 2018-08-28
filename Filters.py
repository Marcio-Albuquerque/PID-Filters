#! .Python3-env/bin/python

#Program Libraries
import cv2
import numpy as np

#Read imagens
imagem = cv2.imread("imgOriginal.tif", cv2.COLOR_BGR2GRAY)
#cv2.imshow("Original", imagem)
print(imagem.shape[0])

k_filter = 2 #(matrix_filters.shape[0]-1)*2

#cv2.imwrite('gray_image.png',gray_image)
 
print('Height: %d' % imagem.shape[0]) 
print('Width: %d' % imagem.shape[1]) 
#print("Largura (width): %d pixels") % (imagem.shape[1])
#print("Canais (channels): %d")      % (imagem.shape[2])

ima_aux = np.zeros((688+k_filter ,688+k_filter), dtype=int)
print (ima_aux.shape)

    
cv2.waitKey(0)