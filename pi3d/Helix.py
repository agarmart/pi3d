from pi3d.pi3dCommon import *
from pi3d import Constants
from pi3d.Shape import Shape

class Helix(Shape):
  def __init__(self,radius=1.0, thickness=0.2, ringrots=6, sides=12, rise=1.0,
               loops=2.0, name="", x=0.0, y=0.0, z=0.0, rx=0.0, ry=0.0, rz=0.0,
               sx=1.0, sy=1.0, sz=1.0, cx=0.0, cy=0.0, cz=0.0):
    super(Helix,self).__init__(name, x, y, z, rx, ry, rz,
                                sx, sy, sz, cx, cy, cz)

    if Constants.VERBOSE:
      print "Creating Helix ...", radius, thickness, ringrots, sides

    path = []
    st = (math.pi*2)/ringrots
    hr = rise * 0.5
    for r in range(0,ringrots+1):
      path.append((radius + thickness * math.sin(r * st),
                   thickness * math.cos(r * st) - hr))
      if Constants.VERBOSE:
        print "path:",path[r][0], path[r][1]

    self.radius = radius
    self.thickness = thickness
    self.ringrots = ringrots
    self.sides = sides
    self.ttype = GL_TRIANGLES

    results = lathe(path, sides, True, rise, loops)

    self.vertices = eglfloats(results[0])
    self.normals = eglfloats(results[1])
    self.indices = eglshorts(results[2])
    self.tex_coords = eglfloats(results[3])
    self.ssize = results[4]

  def draw(self,tex=None):
    shape_draw(self, tex)
