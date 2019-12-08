import numpy as np
from PIL import Image

def main():
    with open("input") as f:
        image = np.array(list(map(int, f.read())))
    # 100 capas
    image = np.reshape(image, (-1, 25*6))
    zeros = np.sum(image[:,] == 0, axis=1)
    layer = np.argmin(zeros)
    output = np.sum(image[layer] == 1)*np.sum(image[layer] == 2)
    print(f"Output: {output}")
    final = np.ones((25*6), dtype=np.int32)
    final *= 2
    for i in range(25*6):
        x = np.where(image[:,i] != 2)
        final[i] = image[x,i][0][0]

    im = Image.new("1", (25,6))
    for j in range(6):
        for i in range(25):
            im.putpixel((i,j), int(final[i+j*25]))
    im.save("out.png")

main()