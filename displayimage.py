from PIL import Image
from pathlib import Path
from mayavi import mlab
import numpy as np


def main():
    '''
    Displays a 3D point cloud
    Version 1.1 - Cyndi Cavanaugh
    '''
    s = np.random.rand(20, 20, 20)
    volume = mlab.pipeline.volume(mlab.pipeline.scalar_field(s), vmin=0, vmax=0.8)

    mlab.draw()
    mlab.savefig('output.png')
    img = Image.open('output.png')
    img.show()


if __name__ == "__main__":
    print("Running main()")
    main()
