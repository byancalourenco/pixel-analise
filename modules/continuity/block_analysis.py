import cv2
import numpy as np



def analyze_blocks(gray, block_size=32):

    height, width = gray.shape


    blocks = []

    scores = []


    for y in range(0, height-block_size, block_size):

        for x in range(0, width-block_size, block_size):


            block = gray[
                y:y+block_size,
                x:x+block_size
            ]


            # diferença entre pixels vizinhos

            horizontal = np.abs(
                np.diff(
                    block.astype(float),
                    axis=1
                )
            )


            vertical = np.abs(
                np.diff(
                    block.astype(float),
                    axis=0
                )
            )


            score = (
                horizontal.mean()
                +
                vertical.mean()
            ) / 2



            blocks.append({
                "x":x,
                "y":y,
                "score":round(float(score),2)
            })


            scores.append(score)



    return blocks, scores