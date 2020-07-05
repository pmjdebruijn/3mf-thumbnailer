#!/usr/bin/python3

THUMBNAIL_FILENAME = 'Metadata/thumbnail.png'

import sys
import zipfile

zip = zipfile.ZipFile(sys.argv[1], 'r')

if THUMBNAIL_FILENAME in zip.namelist():
  thumbnail = zip.read(THUMBNAIL_FILENAME, '')
  f = open(sys.argv[2], 'wb')
  f.write(thumbnail)
  f.close()

