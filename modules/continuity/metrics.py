import numpy as np



def horizontal_difference(gray):

    """
    Compara cada pixel com o pixel da direita
    """

    diff = np.abs(
        gray[:,1:].astype(float)
        -
        gray[:,:-1].astype(float)
    )

    return diff



def vertical_difference(gray):

    """
    Compara cada pixel com o pixel abaixo
    """

    diff = np.abs(
        gray[1:,:].astype(float)
        -
        gray[:-1,:].astype(float)
    )

    return diff



def diagonal_difference(gray):

    """
    Compara pixels diagonais
    """

    diff = np.abs(
        gray[1:,1:].astype(float)
        -
        gray[:-1,:-1].astype(float)
    )

    return diff



def create_continuity_map(gray):

    horizontal = horizontal_difference(gray)

    vertical = vertical_difference(gray)

    diagonal = diagonal_difference(gray)


    # ajusta tamanhos
    h = horizontal[:-1,:]

    v = vertical[:,:-1]


    continuity = (
        h +
        v +
        diagonal
    ) / 3


    return continuity



def calculate_continuity_score(map):

    """
    Retorna percentual de descontinuidade
    """

    mean_value = np.mean(map)


    score = (
        mean_value / 255
    ) * 100


    return round(float(score),2)