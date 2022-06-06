# 흑백 사진 lower contrast 이미지 이용
def enhance_by_histequal(source_image):
    from skimage import exposure
    from matplotlib import pyplot as plt
    try:
        im_equalization = exposure.equalize_hist(source_image)
        plt.figure(figsize=(5, 4)), plt.axis('off')
        plt.imshow(im_equalization)
        plt.savefig('../image/enhance_hist_equal.png')
    except Exception as e:
        print('Error: {}'.format(e))

def enhance_by_gammacorrect(source_image):
    import cv2
    import numpy as np
    from skimage import io
    import matplotlib.pyplot as plt

    # g: gamma 값 변경 대략 0.5 ~ 2.2
    try:
        io.imsave('../image/enhance_gamma_correct.png', source_image)
        g = 0.5
        img = cv2.imread("../image/enhance_gamma_correct.png")
        out = img.copy()
        out = img.astype(np.float)
        out = ((out / 255) ** (1 / g)) * 255
        out = out.astype(np.uint8)
        plt.figure(figsize=(5, 4)), plt.axis('off')
        plt.imshow(out)
        plt.savefig('../image/enhance_gamma_correct.png')
    except Exception as e:
        print('Error: {}'.format(e))