# reliefconnection

Relief Connection is an webapp that helps emergency services staff to plot a path between different people (represented by points on a map) in the aftermath of a disaster using a greedy algorithm that solves the traveling salesman problem. Our algorithm directly connects two points in a straight line on our map, however this could be useful for some disaster recovery situations, such as a situation like Hurricane Maria where people who were stranded were rescued by helicopter search crews.

## Demonstration
Our demonstration shows a route that connects fourty different points inside of a rectangular area that roughly captures MSU (excluding Farms), and part of East Lansing north of Grand River. The fourty points in our list was randomly generated using Python 3's random library. Specifically, random.uniform() allowed us to create random floating point numbers inbetween specific ranges. Our route was created by a Python implementation of a greedy solution to the traveling salesman problem that took in the randomly generated list of points as its input. Finally, we also created a plot program that took in the created list by our algorithm program and plotted it using gmplot, a library that takes latitude and longitude pairs (represented by tuples of floating point numbers) then plots and overlays the plotted route to a html file.

## Technologies Used

The technologies used to create this webapp include Python 3, gmplot, and HTML/CSS.

## Contributers

The contributers to this project are Brandon Hu, Chris Chan, Juston Ko, and
Naveen Sabharwal.
