def rotate_image(source_image):
    from PIL import Image
    from skimage import io
    import numpy as np
    import matplotlib.pyplot as plt

    try:
        io.imsave('../image/rotate.png', source_image)
        im = Image.open('../image/rotate.png')
        plt.figure(figsize=(5, 4)), plt.axis('off')
        plt.imshow(im.rotate(90))
        plt.savefig('../image/rotate.png')
    except Exception as e:
        print('Error: {}'.format(e))