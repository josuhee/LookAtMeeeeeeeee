def rotate_image(source_image):
    from PIL import Image
    from skimage import io
    import matplotlib.pyplot as plt

    try:
        io.imsave('../image/rotate.png', source_image)
        im = Image.open('../image/rotate.png')

        plt.figure(figsize=(5, 4)), plt.axis('off')
        plt.imshow(im.rotate(90))

        plt.savefig('../image/rotate.png')
    except Exception as e:
        print('Error: {}'.format(e))

def scaling_image(source_image):
    from PIL import Image
    from skimage import io
    import matplotlib.pyplot as plt
    try:
        io.imsave('../image/scaling.png', source_image)
        im = Image.open('../image/scaling.png')

        size0 = im.size[0], im.size[1]
        size1 = (2, 0.1)
        im_size1 = im.resize((round(size0[0] * size1[0]), round(size0[1] * size1[1])))

        plt.imshow(im_size1)
        plt.savefig('../image/scaling.png')
    except Exception as e:
        print('Error: {}'.format(e))

def flip_image_left(source_image):
    from PIL import Image
    from skimage import io
    import matplotlib.pyplot as plt
    try:
        io.imsave('../image/flip_left_right.png', source_image)
        im = Image.open('../image/flip_left_right.png')

        im_flip_left_right = im.transpose(Image.FLIP_LEFT_RIGHT)

        plt.imshow(im_flip_left_right)
        plt.savefig('../image/flip_left_right.png')
    except Exception as e:
        print('Error: {}'.format(e))

def flip_image_top(source_image):
    from PIL import Image
    from skimage import io
    import matplotlib.pyplot as plt
    try:
        io.imsave('../image/flip_top_bottom.png', source_image)
        im = Image.open('../image/flip_top_bottom.png')

        im_flip_top_bottom = im.transpose(Image.FLIP_TOP_BOTTOM)

        plt.imshow(im_flip_top_bottom)
        plt.savefig('../image/flip_top_bottom.png')
    except Exception as e:
        print('Error: {}'.format(e))