"""
* DEMO-0 --- a simple example demonstrating the construction
*   of 2-d. geometry and user-defined mesh-size constraints.
*
* These examples call to JIGSAW via its api.-lib. interface.
*
* Writes "case_0x.vtk" files on output for vis. in PARAVIEW.
*
"""

import os
import sys
import numpy as np
import jigsawpy


def render1d(src_path, dst_path):

    mesh = jigsawpy.jigsaw_msh_t()
    jigsawpy.loadmsh(src_path, mesh)

    jigsawpy.savevtk1d("{}-1d.vtk".format(dst_path), mesh)

    jigsawpy.savevtk("{}.vtk".format(dst_path), mesh)

    return

if __name__ == "__main__":
    render1d(sys.argv[1], sys.argv[2])

