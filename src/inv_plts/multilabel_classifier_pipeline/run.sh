#!/bin/bash

python train.py --lr 1e-4 --lr_warmup 50 --model maxvit_t --batch-size 128 --epoch 100 --output_path "/home/ksmehrab/InvasivePlants/MultilabelPipeline/MultilabelClassifier/outputs/maxvit" --seed 9229 --dataset invasive-512 --optimizer AdamW --decay 0.1 --name invasive_maxvit_t --loss_type WBCE --cosine_annealing --num_workers 8 --wandb --server pda
