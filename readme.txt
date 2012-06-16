A short script for replacing city names with vanity citiy names in a variety of binary data files with txt extensions. The data files have a fixed width of 346 bytes. 3MA_TEST.txt is a sample data file with a few records.

The format for the vanity_names csv I used is:
"<Vanity City Name>", census_tract, file_id, state

State was used to build the path to the files, file_id is a 3 digit code used to differentiate georgraphical regions as they are separeted from the data provider, and census_tracts are a way of separating geographical locations for determining if they are in the city area or not.