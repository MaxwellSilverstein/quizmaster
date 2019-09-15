import exifread
#tried to look at the tags of the TIFF file. turns out there are not a lot in each frame
# Open image file for reading (binary mode)
f = open('Lepton_Capture_2.tiff', 'rb')

# Return Exif tags
tags = exifread.process_file(f)

# Print the tag/ value pairs
for tag in tags.keys():
    #if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
    print("Key: %s, value %s" % (tag, tags[tag]))