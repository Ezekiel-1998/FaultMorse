# FaultMorse
An Automated Controlled-channel Attack via Longest Recurring Sequence


# Searching the LRS
# convert hex file to decimal file
python convert2int.py hex_file dec_file_output

# generate suffix array
python sa.py dec_file sa_file_output

# build rank array and height array
python get_rank_height.py dec_file sa_file rank_file_output height_file_output

# find pattern
python find_repeat.py height_file sa_file dec_file THRES_NUM

# hyper parameters:
THRES_NUM: can be a number a little bit larger than 512, or 1024, etc. This is an arg for find_repeat.py
THRES_LEN: pattern length. Currently hardcoded in find_repeat.py

# usage of shell script for batch process:
sh script_new.sh /path/to/tracefile THRES_NUM

# remaining work:
to be optimize: stage 2 searching in find_repeat.py, should be able to achieve O(n) scanning


