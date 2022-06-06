def show_histogram(source_image):
    from matplotlib import pyplot as plt
    plt.figure(figsize=(5, 4))
    plt.hist(source_image.ravel(), bins=256)
    plt.savefig('hist.png')

