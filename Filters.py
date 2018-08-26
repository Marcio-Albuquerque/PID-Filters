#! .Python3-env/bin/python

#Program Libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

#Structure for saved files in paste
Path = ("ImagensFilters/Primeira/","ImagensFilters/Segunda/", "ImagensFilters/Terceira/")
Letters = ("A/","B/","C/")

#Variables for letter A
s = ([[3,3], [5,5], [7,7]])
N = (9,25,49)

#Variables for letter B
kernelmedian = (np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]],dtype=float)*1/16)

#Variables for letter C
kernelsize = (3,5,7)

#Declaration of the variable image
imagem = ([[0,0],[0,0],[0,0]])

    

def applyFilter(imagem, kernel, id, local):
    tempImg = cv2.filter2D(imagem, -1, kernel, cv2.BORDER_REPLICATE)
    cv2.imwrite(local + str(id) + ".png", tempImg)
    plt.cla()
    plt.clf()
    plt.hist(tempImg.ravel(),256,[0,256], facecolor='blue')
    #plt.show()
    plt.savefig(local + str(id) + "-H.png")

def applyFilterMedian(imagem, kernel, id, local):
    tempImg = cv2.medianBlur(imagem, kernel, -1)
    cv2.imwrite(local + str(id) + ".png", tempImg)
    plt.cla()
    plt.clf()
    plt.hist(tempImg.ravel(),256,[0,256], facecolor='blue')
    plt.savefig(local + str(id) + "-H.png")

for j in range(3):
    for i in range(3):
        os.makedirs(Path[j] + Letters[i], exist_ok=True)

#Read imagens
for i in range(3):
    imagem[i] = cv2.cvtColor(cv2.imread("img" + str(i+1) + ".tif"), cv2.COLOR_BGR2GRAY)
    plt.cla()
    plt.clf()
    plt.hist(imagem[i].ravel(),256,[0,256], facecolor='blue')
    plt.savefig("img" + str(i+1) + "-H.png")
 

for j in range(3): #Imagens    
    for i in range(3):# Letter A
        kernel = (np.ones(s[i], dtype=float)*1/N[i])
        id = "img" + str(j+1) + "-letraA-kernel" + str(i+1)
        applyFilter(imagem[j],kernel,id,Path[j] + Letters[0])
        
    id = "img" + str(j+1) + "-letraB-kernelmedian" 
    applyFilter(imagem[j],kernelmedian,id,Path[j] + Letters[1])
    
    for i in range(3):# Letter A
        id = "img" + str(j+1) + "-letraC-kernelSize" + str(i+1)
        applyFilterMedian(imagem[j],kernelsize[i],id,Path[j] + Letters[2])
#cv2.waitKey(0)