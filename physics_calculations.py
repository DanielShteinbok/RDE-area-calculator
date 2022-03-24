#!/usr/bin/env python

import math
#e0 = 8.85e-12
e = 1.60e-19
#me = 9.10938356e-31
#mp = 1.6726219e-27
#k = 1/4/math.pi/e0
#mu0 = 4*math.pi*1e-7
Na = 6.0221409e23

def current(mass_lost, molmass=63.55, time=600, ne=2):
    """
    calculate average current during an electropolishing process.

    parameters:
    mass_lost: the mass lost during the process grams
    molmass: the molar mass of the material being electropolished, 63.55 g/mol for Cu
    time: the duration of the electropolishing
    ne: the number of charges that flow across electrodes for each atom that is electropolished away.
        obtained from the chemical equation that describes the process.
        In the case of copper electropolishing in phosphoric acid, the chemical equation dictates this is 2.

    Returns:
    current: the mean current, in Amperes, during the process
    """
    return mass_lost*Na*ne*e/molmass/time

def thickness_etched(mass_lost, area, density=8.96):
    """
    calculates the thickness of material etched away during electropolishing.

    Parameters:
    mass_lost: the mass, in milligrams, lost during electropolishing
    area: the exposed area, in mm^2, that was electropolished
    density: the density of material being etched in mg/mm^3; 8.96 mg/mm^3
        incidentally, this is 8.96 ug/um/mm^2

    Returns:
    thickness etched, in microns
    """

    # multiply mass_lost by 1000, to convert to ug; that way, result will be in microns as desired
    return mass_lost*1000/density/area
