# RDE Area Calculator
In electropolishing, what we try to keep as an "invariant" is the current density passing through the solution.
Current density is current divided by the area of the electrode being electropolished.

In our setup, samples are taped using Kapton tape to a rotating stainless steel electrode surrounded by a teflon casing,
so the area exposed of the electrode is a polygon whose sides are the insides of these strips of tape.

This is a python module to calculate the area of these polygonal samples.

## Usage:
Starting from one corner of the exposed area of the electrode (call this point A),
measure out the distance to an adjacent corner point B, then to a corner point C (which is adjacent to B but not adjacent to A).
Then, measure the diagonal length CA.
Continue by measuring CD and DA, DE and EA, ... and so on for however many sides there are in the exposed polygon.

In an IPython shell or Jupyter notebook, run:

``` python
import area

area.area_polygon(AB, (BC, CA), (CD, DA), (DE, EA))
```

with a new tuple for each pair of sides described above, where AB, BC, CD ... are numbers representing those side lengths.

