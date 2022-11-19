from PIL import Image
import random
from filmgrainer.imgbuffers import GrayBuffer

_GaussPower = 60 

def _makeNoise(width, height, power):
    buffer = GrayBuffer.fromZeros(width, height)

    for y in range(0, height):
        for x in range(0, width):
            rn = random.gauss(128, power)
            if rn < 0:
                i = 0
            elif rn > 255:
                i = 255
            else:
                i = int(rn)
            buffer.setGray(x, y, i)
    return buffer


def grainGen(width, height, grain_size, power, seed = 1):
    # A grain_size of 1 means the noise buffer will be made 1:1
    # A grain_size of 2 means the noise buffer will be resampled 1:2
    noise_width = int(width / grain_size)
    noise_height = int(height / grain_size)
    print("Making gaussian noise buffer, width: %d, height: %d, grain-size: %s, seed: %d" % (noise_width, noise_height, str(grain_size), seed))
    random.seed(seed)
    buffer = _makeNoise(noise_width, noise_height, power)
    img = buffer.toImg()

    # Resample
    if grain_size != 1.0:
        img = img.resize((width, height), resample = Image.LANCZOS)

    return img


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 6:
        out_file = sys.argv[1]
        width = int(sys.argv[2])
        height = int(sys.argv[3])
        grain_size = float(sys.argv[4])
        power = float(sys.argv[5])
        out = grainGen(width, height, grain_size, power)
        out.save(sys.argv[1])

