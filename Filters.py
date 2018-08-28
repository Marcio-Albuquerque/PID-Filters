#! .Python3-env/bin/python

#Program Libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageFont #dynamic import
import os

#Structure for saved files in paste
Path = ("ImagensFilters/1/","ImagensFilters/2/", "ImagensFilters/3/","ImagensFilters/4/")
Letters = ("A/","B/","C/")

#Variables for letter A
s = ([[3,3], [5,5], [7,7]])
N = (9,25,49)

#Variables for letter B
kernelmedian = (np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]],dtype=float)*1/16)

#Variables for letter C
kernelsize = (3,5,7)

#Declaration of the variable image
imagem = ([[0,0],[0,0],[0,0],[0,0]])    

def applyFilter(imagem, kernel, id, local):
    tempImg = cv2.filter2D(imagem, -1, kernel, cv2.BORDER_REPLICATE)
    cv2.imwrite(local + str(id) + ".png", tempImg)
    plt.cla()
    plt.clf()
    plt.xlabel('Intensidade', fontsize=18)
    plt.ylabel('Quantidade de pixel', fontsize=16)
    plt.hist(tempImg.ravel(),256,[0,256], fc='k', ec='k')
    #plt.show()
    plt.savefig(local + str(id) + "-H.png")

def applyFilterMedian(imagem, kernel, id, local):
    tempImg = cv2.medianBlur(imagem, kernel, -1)
    cv2.imwrite(local + str(id) + ".png", tempImg)
    plt.cla()
    plt.clf()
    plt.xlabel('Intensidade', fontsize=18)
    plt.ylabel('Quantidade de pixel', fontsize=16)
    plt.hist(tempImg.ravel(),256,[0,256], fc='k', ec='k')
    plt.savefig(local + str(id) + "-H.png")

os.makedirs("Input/", exist_ok=True)
for j in range(4):
    for i in range(3):
        os.makedirs(Path[j] + Letters[i], exist_ok=True)

##Convert imagens
#Firt image
cv2.imwrite("Input/img1.png",cv2.imread("Original/022.png")) 

#Second image
img2 = Image.open("Original/cameraman_sp.gif")
img2.save("Input/img2.png",'png', optimize=True, quality=100)

#Third image
img3 = Image.open("Original/medfilt2.gif")
img3.save("Input/img3.png",'png', optimize=True, quality=100)

#Fourth image
cv2.imwrite("Input/img4.png",cv2.imread("Original/SaltAndPepperNoise.jpg")) 

#Read imagens
for i in range(4):
    imagem[i] = cv2.cvtColor(cv2.imread("Input/img" + str(i+1) + ".png"), cv2.COLOR_BGR2GRAY)
    plt.cla()
    plt.clf()
    plt.hist(imagem[i].ravel(),256,[0,256], fc='k', ec='k')
    plt.xlabel('Intensidade', fontsize=18)
    plt.ylabel('Quantidade de pixel', fontsize=16)
    plt.savefig("Input/img" + str(i+1) + "-H.png")


for j in range(4): #Imagens    
    for i in range(3):# Letter A
        kernel = (np.ones(s[i], dtype=float)*1/N[i])
        id = "img" + str(j+1) + "-letraA-kernel" + str(i+1)
        applyFilter(imagem[j],kernel,id,Path[j] + Letters[0])
        
    # Letter B
    id = "img" + str(j+1) + "-letraB-kernelmedian" 
    applyFilter(imagem[j],kernelmedian,id,Path[j] + Letters[1])
    
    for i in range(3):# Letter C
        id = "img" + str(j+1) + "-letraC-kernelSize" + str(i+1)
        applyFilterMedian(imagem[j],kernelsize[i],id,Path[j] + Letters[2])
