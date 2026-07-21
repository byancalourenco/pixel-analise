import numpy as np



def normalize(value, max_value):

    score = (value / max_value) * 100

    if score > 100:
        score = 100

    return score



def calculate_pixel_fraud_score(
        block_scores,
        neighbor_scores
):

    """
    Junta as duas análises:
    - continuidade interna
    - comparação com vizinhos
    """


    if len(block_scores) == 0:
        return 0



    max_block = max(block_scores)


    max_neighbor = max(
        [
            x["neighbor_score"]
            for x in neighbor_scores
        ]
    ) if neighbor_scores else 0



    # transforma em 0-100

    block_score = normalize(
        max_block,
        50
    )


    neighbor_score = normalize(
        max_neighbor,
        100
    )



    # pesos

    final_score = (

        block_score * 0.4

        +

        neighbor_score * 0.6

    )


    return round(
        float(final_score),
        2
    )



def classify_score(score):


    if score >= 75:

        return "Alta suspeita"


    elif score >= 45:

        return "Média suspeita"


    else:

        return "Baixa suspeita"