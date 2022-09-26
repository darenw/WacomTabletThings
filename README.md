# WacomTabletThings
Command line scripts to fix or deal with Wacom drawing tablet issues


# Two Monitors and One Wacom Tablet

**wacom-one-monitor.py:**   run this to map the tablet's area to only the left of two monitors. 

Without this, tablet's area with 16:9 (?) ratio will by default map to the
whole area of two monitors side by side, 32:9, and circles, nice neat square grids of 
points, tic-tac-toe games will come out distorted, twice as wide as intended. 
That is bothersome for most artists!   

This script is a simple fix for that. It's hard-code for the Intuos Pro
and for monitors with 1920x1080 resolution.  
Someday I may generalize it, or you can submit a fix.

# Other Things

Other command line tools or GUI tools relating to the Wacom Intuos Pro may
appear here someday. 
