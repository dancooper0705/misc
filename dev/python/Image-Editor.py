import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def main():
    img = mpimg.imread('1200.png')
    data = rgb2gray(img)
    print('shape: ' + str(data.shape))
    print(data)
    plt.imshow(data, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
    plt.show()

if __name__ == "__main__":
    main()
