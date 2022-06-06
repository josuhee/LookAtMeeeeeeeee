def blur_image(source_image, sigma):
    from skimage import filters, io
    try:
        io.imsave('../image/blurImage.png', filters.gaussian(source_image, sigma=sigma, multichannel=True))
    except Exception as e:
        print('Error: {}'.format(e))

def smooth_image(source_image):
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    try:
        gray = cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)
        smoothing_mask = np.array([[1 / 16, 1 / 8, 1 / 16], [1 / 8, 1 / 4, 1 / 8], [1 / 16, 1 / 8, 1 / 16]])
        smoothing_out = cv2.filter2D(gray, -1, smoothing_mask)

        plt.figure(figsize=(5, 4)), plt.axis('off')
        plt.imshow(smoothing_out)
        plt.savefig('../image/smooth.png')
    except Exception as e:
        print('Error: {}'.format(e))