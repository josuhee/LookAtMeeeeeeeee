def show_histogram(source_image):
    from matplotlib import pyplot as plt
    plt.figure(figsize=(5, 4))
    plt.hist(source_image.ravel(), bins=256)
    plt.savefig('../image/hist.png')

def invert_image(source_image, a_max):
    from skimage.color import rgb2gray
    import matplotlib.pyplot as plt
    gray_image = rgb2gray(source_image)
    im_invert = a_max - gray_image

    plt.figure(figsize=(5, 4)), plt.axis('off')
    plt.imshow(im_invert, cmap='gray', vmin=0, vmax=1)
    plt.savefig('../image/invert.png')

def convert_grayscale(source_image):
    from skimage.color import rgb2gray
    import matplotlib.pyplot as plt
    gray_image = rgb2gray(source_image)

    plt.figure(figsize=(5, 4)), plt.axis('off')
    plt.imshow(gray_image, cmap='gray', vmin=0, vmax=1)
    plt.savefig('../image/gray.png')