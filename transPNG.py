###################################
# 3/28/2016                       #
# Sven Nelson                     #
# Convert PNG white background    #
# to transparent                  #
###################################

## Function takes a filename of a PNG and makes background transparent
def removeBackground( file ):
   "Takes a png file and converts the white background to transparent."
   from PIL import Image
   import os
   
   img = Image.open(file)
   img = img.convert("RGBA")
   datas = img.getdata()
   
   newData = []
   for item in datas:
       if item[0] == 255 and item[1] == 255 and item[2] == 255:
           newData.append((255, 255, 255, 0))
       else:
           newData.append(item)
   img.putdata(newData)
   img.save(file[:-4] + "_transp.png", "PNG")
   print( "Saved: "+ file[:-4] + "_transp.png")
   os.remove(file)
   return;
   
## Function to do removeBackground for multiple files (loop)
def rmBackgrounds( ):
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
       removeBackground( file )
   print( "Process complete!")
