import numpy as np



def compare_blocks(block1, block2):

    """
    Mede a diferença entre dois blocos
    """

    difference = np.abs(
        block1.astype(float)
        -
        block2.astype(float)
    )


    return difference.mean()



def analyze_neighbor_difference(
        gray,
        block_size=32
):

    height, width = gray.shape


    results = []


    blocks = {}


    # primeiro salva todos os blocos

    for y in range(0, height-block_size, block_size):

        for x in range(0, width-block_size, block_size):

            blocks[(x,y)] = gray[
                y:y+block_size,
                x:x+block_size
            ]



    # compara vizinhos

    for (x,y), block in blocks.items():

        neighbors = []


        positions = [

            (x-block_size,y), # esquerda

            (x+block_size,y), # direita

            (x,y-block_size), # cima

            (x,y+block_size)  # baixo

        ]


        for pos in positions:

            if pos in blocks:

                neighbors.append(
                    blocks[pos]
                )


        if len(neighbors) > 0:


            differences = []


            for neighbor in neighbors:

                diff = compare_blocks(
                    block,
                    neighbor
                )

                differences.append(diff)



            anomaly = np.mean(
                differences
            )


            results.append({

                "x":x,

                "y":y,

                "neighbor_score":
                round(
                    float(anomaly),
                    2
                )

            })


    return results