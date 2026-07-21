import cv2


def load_image(path):

    image = cv2.imread(path)

    if image is None:
        raise Exception("Imagem não encontrada")

    return image



def convert_gray(image):

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    return gray