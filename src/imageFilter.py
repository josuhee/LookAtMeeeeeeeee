def blur_image(source_image, sigma):
    from skimage import filters, io
    try:
        io.imsave('../image/blurImage.png', filters.gaussian(source_image, sigma=sigma, multichannel=True))
    except Exception as e:
        print('Error: {}'.format(e))

