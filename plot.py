#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 14:06:38 2019

@author: christopherchen
"""
from gmplot import gmplot
from algorithm import theTSP

# Place map
gmap = gmplot.GoogleMapPlotter(42.726215, -84.488677, 13)

# coordinates in order of rescue
tsp = theTSP(40)    # initialize object
rescue_route = tsp.getList()
rescue_route_length = tsp.getWeight()

# Polygon
east_lansing_lats, east_lansing_lons = zip(*rescue_route)
gmap.plot(east_lansing_lats, east_lansing_lons, 'cornflowerblue', edge_width=10)


# Draw
gmap.draw("my_map.html")


