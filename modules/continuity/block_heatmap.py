import cv2
import numpy as np


def create_block_heatmap(
        image_path,
        blocks,
        output="results/block_heatmap.png"
):

    image = cv2.imread(image_path)

    heatmap = np.zeros(
        image.shape[:2],
        dtype=np.float32
    )


    for block in blocks:

        x = block["x"]
        y = block["y"]
        score = block["score"]


        # preenche a região com o score
        heatmap[
            y:y+32,
            x:x+32
        ] = score



    # normaliza 0-255

    heatmap = cv2.normalize(
        heatmap,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    )


    heatmap = heatmap.astype(
        np.uint8
    )


    # aplica cores

    colored = cv2.applyColorMap(
        heatmap,
        cv2.COLORMAP_JET
    )


    # mistura com imagem original

    overlay = cv2.addWeighted(
        image,
        0.6,
        colored,
        0.4,
        0
    )


    cv2.imwrite(
        output,
        overlay
    )


    return output