#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 14:06:38 2019

@author: christopherchen
"""
from gmplot import gmplot

# Place map
gmap = gmplot.GoogleMapPlotter(42.726215, -84.488677, 13)

#coordinates in order of rescue
rescue_route = [
    (37.771269, -122.511015),
    (37.773495, -122.464830),
    (38.7713, -123.5110),
    (38.7735, -125.4648)
    ]

# Polygon
east_lansing_lats, east_lansing_lons = zip(*rescue_route)
gmap.plot(east_lansing_lats, east_lansing_lons, 'cornflowerblue', edge_width=10)


# Draw
gmap.draw("my_map.html")


