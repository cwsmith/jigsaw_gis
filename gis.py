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
import numpy as np
import jigsawpy


def gis(src_path, dst_path):

    opts = jigsawpy.jigsaw_jig_t()
    geom = jigsawpy.jigsaw_msh_t()
    mesh = jigsawpy.jigsaw_msh_t()
    hfun = jigsawpy.jigsaw_msh_t()

#------------------------------------ define JIGSAW geometry

    geom.mshID = "euclidean-mesh"
    geom.ndims = +2
    jigsawpy.loadmsh("mesh.msh", geom)
    jigsawpy.loadmsh("mesh-HFUN.msh", hfun)
    

#------------------------------------ build mesh via JIGSAW!

    print("Call libJIGSAW: gis")

    opts.verbosity = +1
    opts.hfun_scal = "absolute"
    opts.hfun_hmax = float("inf")
    opts.hfun_hmin = float(0.0)

    opts.mesh_dims = +2                 # 2-dim. simplexes

    opts.optm_qlim = +.9375

    opts.geom_feat = True
    opts.geom_eta1 = float(+5.0)
    opts.geom_eta2 = float(+5.0)

    jigsawpy.lib.jigsaw(opts, geom, mesh, hfun=hfun)

    scr2 = jigsawpy.triscr2(            # "quality" metric
        mesh.point["coord"],
        mesh.tria3["index"])

    print("Saving gis.vtk file.")

    jigsawpy.savevtk(os.path.join(
        dst_path, "gis.vtk"), mesh)

    return

if __name__ == "__main__":
    gis("", "./")

