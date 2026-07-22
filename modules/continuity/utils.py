# prepara a imagem deixando ela cinza 

# importando o open cv
import cv2

# criando uma função que recebe o caminho da img
def load_image(path):

    #  função do open cv que le a img e trasnforma arquivo --> matriz de pixels
    image = cv2.imread(path)

    # verifica se a img realmente foi aberta, e se n foi, exibe uma mensagem
    if image is None:
        raise Exception("Imagem não encontrada")

    # retorna a matriz de pixels 
    return image

# criando uma função que recebe a image (veio do return)
def convert_gray(image):

    # tranforma as coes rgb em cinza com uma função do open cv
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # retorna a image cinza
    return gray