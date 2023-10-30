import cv2
imagem = cv2.imread('corshow.png')
cv2.imshow('Imagem original: ', imagem)
for y in range(0, imagem.shape[0], 1): #percorre linhas
 for x in range(0, imagem.shape[1], 1): #percorre colunas
     imagem[y, x] = (255,(x*y+1)%256,255)
     #imagem[y:y+1, x: x+10] = (125,125,125)

cv2.imshow("Imagem modificada: ", imagem)
cv2.waitKey(0)
