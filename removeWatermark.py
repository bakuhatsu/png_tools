###################################
# 3/31/2016                       #
# Sven Nelson                     #
# Remove watermarks from image    #
# backgrounds (using png)         #
###################################

## Function takes a filename of a PNG with orange watermark and removes the watermark
def removeWatermark( file ):
   "Takes a png file and converts the orange background to white."
   from PIL import Image
   import os
   
   img = Image.open(file)
   img = img.convert("RGBA")
   datas = img.getdata()
   
   newData = []
   for item in datas:
       if item[0] > 240 and item[1] < 255 and item[2] < 255:
           newData.append((255, 255, 255, 255))
       elif item[0] < 90 and item[0] > 0 and item[1] < 50 and item[1] > 0 and item[2] < 10:
           newData.append((0, 0, 0, 255))
       else:
           newData.append(item)
   img.putdata(newData)
   img.save(file[:-4] + "_transp.png", "PNG")
   print( "Saved: "+ file[:-4] + "_transp.png")
   os.remove(file)
   return;
   
## Function to do removeWatermark for multiple files (loop)
def rmWatermarks( ):
   "Takes multiple png file and converts the white background to transparent."
   import Tkinter,tkFileDialog
   import os
   # set up your Tk Frame and whatnot here...
   
   root = Tkinter.Tk()
   #os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
   root.update()
   files = tkFileDialog.askopenfilenames(parent=root,title='Choose file or files')
   files = root.tk.splitlist(files)
   root.destroy()
   
   for file in files:
       removeWatermark( file )
   print( "Process complete!")






