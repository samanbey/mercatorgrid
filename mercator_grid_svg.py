from math import *

def y(fi):
    return -log(tan(radians(fi/2 + 45)))

svg = '<svg xmlns="http://www.w3.org/2000/svg" height="400" width="400" viewBox="-3.141 -3.141 6.283 6.283">\n'
svg += '<g stroke="blue" stroke-width=".001">\n'

fi1 = float(input('Southernmost latitude in degrees (e.g. -85): '))
fi2 = float(input('Northernmost latitude in degrees (e.g. 85): '))
step = float(input('Grid density in degrees (e.g. 10): '))

fi = fi1
while fi <= fi2:
    yy = y(fi)
    xx = radians(180)
    svg += '<line x1="%.6f" y1="%.6f" x2="%.6f" y2="%.6f"/>\n' % (-xx, yy, xx, yy)
    fi += step

la = -180
while la <= 180:
    y1 = y(fi1)
    y2 = y(fi2)
    xx = radians(la)
    svg += '<line x1="%.6f" y1="%.6f" x2="%.6f" y2="%.6f"/>\n' % (xx, y1, xx, y2)
    la += step

svg += '</g>\n'

svg += "</svg>\n"

with open("mercator_grid.svg","w") as f:
    f.write(svg)
