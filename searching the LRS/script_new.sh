#!/bin/bash

python convert2int.py $1 $1_$2.dec
python sa.py $1_$2.dec $1_$2.sa
python get_rank_height.py $1_$2.dec $1_$2.sa $1_$2.rank $1_$2.height
python find_repeat.py $1_$2.height $1_$2.sa $1_$2.dec $2 > $1_$2_longest100.result
rm $1_$2.dec
rm $1_$2.sa
rm $1_$2.height
rm $1_$2.rank
