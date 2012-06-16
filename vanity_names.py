import os
import csv
from progressbar import ProgressBar
from stat import *


def chunked(file, chunk_size):
    return iter(lambda: file.read(chunk_size), '')

#replace C:\\cities\\vanity_names.csv with your own path
reader = csv.reader( open("C:\\cities\\vanity_names.csv","rb") )
reader.next()

#store all vanity name records in a list
vanity_names = []
for line in reader:
    vanity_names.append( line )

#Lists areas before processing, states = [] stores folders for dirs needed to check
#set working_dir to the root folder for the data files
print "Processing vanity city names for the following areas:"
states = ['MI\\', 'WI\\', 'FL\\']
working_dir = "C:\\working_dir\\"

#set used to store only 1 file per match
found_files = set()
for state in states:
    text_file = [file for file in os.listdir( working_dir + state ) if file.lower().endswith( ".txt" )]
    for file in text_file:
            for vanity_name_record in vanity_names:
                    if file[:3] == vanity_name_record[2]:
                            found_files.add( working_dir + state + file )

#Count up total bytes for progress bar
total_bytes = 0
running_bytes = 0
for file in found_files:
    print file
    st = os.stat( file )
    total_bytes += st[ST_SIZE]

progress = ProgressBar(maxval=total_bytes).start()

#loop through data files found that require processing
#create new file, copy records unless a vanity name census_tract is found,
#then write the adjusted line to the file with new city name
#delete old file after processing
for file in found_files:
    os.rename( file, file+"~" )
    src = open( file + "~", "rb" )
    dest = open( file, "wb" )
    for line in chunked(src, 346):
        running_bytes += 346
        progress.update(running_bytes)
        match = "0"
        s_line = str( line )
        for vanity_name_record in vanity_names:
            #census_tracts are on 14:20 in 346 record format
            if s_line[14:20] == vanity_name_record[1]:
                match = vanity_name_record[0]
                break
        if match == "0":
            dest.write( s_line )
        else:
            #city starts at 141 and goes for 24 in 346 format
            dest.write( s_line[:140] + match.ljust(24) + s_line[164:] )
    src.close()
    dest.close()
    os.remove( file + "~" )
