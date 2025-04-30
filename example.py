#!/usr/bin/env python

"""
Purpose: Example usage of calling discrete methods for plotting Bell Nozzle.
"""

# Standard imports
import os

# Local imports
from bell_nozzle import bell_nozzle, plot

#------------------------------------------------------
# Constants for both nozzles
#------------------------------------------------------
k 	= 1.21		# ratio of specific heats
l_percent = 60	# nozzle length percentage (60, 80, 90)

#------------------------------------------------------
# Nozzle 1: Typical Upper Stage
# Shows annotations and just shows plot (no saving to png)
#------------------------------------------------------
aratio = 25 	# Ae / At	
Rt = 40 		# {'radius_throat': 40, 'radius_exit': 210}		

# calculate rao_bell_nozzle_contour
angles, contour = bell_nozzle(k, aratio, Rt, l_percent)

# plot contour
title = 'Bell Nozzle \n [Area Ratio = ' + str(round(aratio,1)) + ', Throat Radius = ' + str(round(Rt,1)) + ']' 
ENABLE_ANNOTATIONS=True
plot(title, aratio, Rt, angles, contour, ENABLE_ANNOTATIONS)

#------------------------------------------------------
# Nozzle 2: Typical lower stage booster values
# Does not show annotations and saves to png
#------------------------------------------------------
aratio = 7   # Ae / At	
Rt = 800 	 # [your unit] Throat radius

# rao_bell_nozzle_contour
angles, contour = bell_nozzle(k, aratio, Rt, l_percent)

# plot contour
image_path = os.path.join(os.path.dirname(__file__), 'output', 'lower_stage_bell_nozzle.png')
title = 'Bell Nozzle \n [Area Ratio = ' + str(round(aratio,1)) + ', Throat Radius = ' + str(round(Rt,1)) + ']' 
ENABLE_ANNOTATIONS=False
plot(title, aratio, Rt, angles, contour, ENABLE_ANNOTATIONS, image_path)