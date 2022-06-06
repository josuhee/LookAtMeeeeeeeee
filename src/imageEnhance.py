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