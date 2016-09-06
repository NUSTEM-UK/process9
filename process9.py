# Uses Tesseract (brew install tesseract, on a Mac)
# and PyTesseract (sudo pip install pytesseract)

import os
import glob
import PIL
import pytesseract

for infile in glob.glob("*.jpg"):
  file, ext = os.path.splitext(infile)
  print file
  # im = Image.open(infile)
  print pytesseract.image_to_string(PIL.Image.open(infile))
  print "###############"