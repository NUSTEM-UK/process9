"""Process images containing Diamond 9 data samples.

Uses Tesseract (on a Mac: brew install tesseract) and PyTesseract
(sudo pip install pytesseract.)

Proof-of-concept for processing captured images into (eventually) coded CSV
data sets for onward analysis in SPSS. Part of the research efforts
supporting and drawing lessons from Think Physics, http://thinkphysics.org.

Jonathan Sanderson, Northumbria University, Newcastle, UK.
This initial test version: 2016-09-07
"""

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
