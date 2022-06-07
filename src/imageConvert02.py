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

def warp_image_row(source_image):
    import numpy as np
    from skimage import io
    import math
    import matplotlib.pyplot as plt
    from PIL import Image

    try:
        io.imsave('../image/warp_rows.png', source_image)
        im = Image.open('../image/warp_rows.png').convert("L")
        im = np.array(im)
        rows, cols = im.shape[0], im.shape[1]
        img_output = np.zeros((rows, cols))

        for i in range(rows):
            for j in range(cols):
                offset_y = int(40.0 * math.sin(2 * 3.14 * j / 180))
                if i + offset_y < rows:
                    img_output[i, j] = im[(i + offset_y) % rows, j]
                else:
                    img_output[i, j] = 0

        plt.imshow(img_output)
        plt.savefig('../image/warp_rows.png')
    except Exception as e:
        print('Error: {}'.format(e))

def warp_image_col(source_image):
    import numpy as np
    from skimage import io
    import math
    import matplotlib.pyplot as plt
    from PIL import Image

    try:
        io.imsave('../image/warp_cols.png', source_image)
        im = Image.open('../image/warp_cols.png').convert("L")
        im = np.array(im)
        rows, cols = im.shape[0], im.shape[1]
        img_output = np.zeros((rows, cols))

        for i in range(rows):
            for j in range(cols):
                offset_x = int(40.0 * math.sin(2 * 3.14 * i / 180))  # 40 부분을 바꿀 수 있음
                if j + offset_x < rows:
                    img_output[i, j] = im[i, (j + offset_x) % cols]
                else:
                    img_output[i, j] = 0

        plt.imshow(img_output)
        plt.savefig('../image/warp_cols.png')
    except Exception as e:
        print('Error: {}'.format(e))