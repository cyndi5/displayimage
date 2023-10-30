from PIL import Image
import argparse
from pathlib import Path
from mayavi import mlab
import numpy as np


def main():
    '''
    Displays a 3D point cloud
    Version 1.1 - Cyndi Cavanaugh
    '''
    parser = argparse.ArgumentParser(description='Point cloud.')
    parser.add_argument(
        "--threed",
        required=True,
        default=None,
        type=str,
        help="path to file with 3d info")
    parser.add_argument(
        "--image",
        required=True,
        default=None,
        type=str,
        help="path to image")
    args = parser.parse_args()
    image_path = Path(args.image)
    threed_path = Path(args.threed)
    print(f'image_path={image_path} threed_path={threed_path}')
    image = Image.open(image_path)
    threed = Image.open(threed_path)
    image.show()
    image_converted = image.convert('L')
    image_data = np.asarray(image_converted.getdata()).reshape(image_converted.size)
    threed.show()
    threed_converted = threed.convert('L')
    threed_data = np.asarray(threed_converted.getdata()).reshape(threed_converted.size)

    s = np.random.rand(20, 20, 20)
    volume = mlab.pipeline.volume(mlab.pipeline.scalar_field(threed_data), vmin=0, vmax=0.8)

    mlab.draw()
    mlab.savefig('output.png')
    point = Image.open('output.png')
    point.show()


if __name__ == "__main__":
    print("Running main()")
    main()
