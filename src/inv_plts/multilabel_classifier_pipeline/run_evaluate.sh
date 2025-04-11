#!/bin/bash

python basic_evaluate.py --model_name maxvit_t --checkpoint_path /home/ksmehrab/InvasivePlants/MultilabelPipeline/MultilabelClassifier/outputs/maxvit/ckpt_9229_S9229_invasive_maxvit_t_invasive-512_maxvit_t.t7 --output_path /home/ksmehrab/InvasivePlants/MultilabelPipeline/MultilabelClassifier/outputs/maxvit --server pda --batch_size 256 --num_workers 8