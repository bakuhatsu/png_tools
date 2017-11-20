# png_tools
Python package including tools to remove watermarks or make image backgrounds transparent.

## transpPNG
Transparency is achieved by converting everything that is white to transparent (The code could easily be modified to do this based on a different color).

## removeWatermark
Watermark removal works based on the image being black and white and the watermark being a color, in this case orange.  With similar watermarks of different colors the code could be easily adapted.  

Both functions can be run on a single file or passed a list of files to loop over. 
