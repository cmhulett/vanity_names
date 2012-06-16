A short script for replacing city names with vanity citiy names in multiple binary data files with txt extensions. The data files have a fixed width of 346 bytes. 3MA_TEST.txt is a sample data file with a few records.

The format for the vanity_names csv I used is:
"Vanity City Name", census_tract, file_id, state_abbreviation

State was used to build the path to the files, file_id is a 3 digit code used to differentiate georgraphical regions as they are separeted from the data provider, and census_tracts are a way of separating geographical locations for determining if they are in the city area or not.

In my case vanity_names.csv was a very sort list so it was stored in memory and looped against the record but for larger comparisons to avoid O(n^2) it should be broken down into smaller chunks by area so only the possible matches by census_tract are compared.