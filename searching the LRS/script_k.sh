#!/bin/bash

python convert2int.py ../../experiment/Trace$1.txt tmp/dec$1_$2.out
python sa.py tmp/dec$1_$2.out tmp/sa$1_$2.out
python get_rank_height.py tmp/dec$1_$2.out tmp/sa$1_$2.out tmp/rank$1_$2.out tmp/height$1_$2.out
python find_repeat.py tmp/height$1_$2.out tmp/sa$1_$2.out tmp/dec$1_$2.out $2 > ../../experiment/log_$2_trace$1_lenv
