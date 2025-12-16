#!/bin/bash

export CUDA_VISIBLE_DEVICES=1

which python 
nvidia-smi

# maxvit_t
python src/inv_plts/multilabel_classification/train.py --lr 1e-4 --lr_warmup 50 --model maxvit_t --batch-size 128 --epoch 100 --output_path "/home/ksmehrab/InvasivePlants/MultilabelPipeline/MultilabelClassifier/outputs/maxvit" --seed 9229 --dataset invasive-512 --optimizer AdamW --decay 0.1 --name invasive_maxvit_t --loss_type WBCE --cosine_annealing --num_workers 8 --wandb --server pda

# vit_b_16
python src/inv_plts/multilabel_classification/train.py --lr 1e-4 --lr_warmup 50 --model vit_b_16 --batch-size 128 --epoch 100 --output_path "/home/ksmehrab/InvasivePlants/MultilabelPipeline/MultilabelClassifier/outputs/vitb" --seed 9229 --dataset invasive-512 --optimizer AdamW --decay 0.1 --name invasive_vitb --loss_type WBCE --cosine_annealing --num_workers 8 --wandb --server pda

# cvt_13
python src/inv_plts/multilabel_classification/train.py --lr 1e-4 --lr_warmup 50 --model cvt_13 --batch-size 128 --epoch 100 --output_path "/home/ksmehrab/InvasivePlants/MultilabelPipeline/MultilabelClassifier/outputs/cvt_13" --seed 9229 --dataset invasive-512 --optimizer AdamW --decay 0.1 --name invasive_cvt_13 --loss_type WBCE --cosine_annealing --num_workers 8 --wandb --server pda

# convnext_base
python src/inv_plts/multilabel_classification/train.py --lr 1e-4 --lr_warmup 5 --model convnext_base --batch-size 128 --epoch 100 --output_path /home/ksmehrab/InvasivePlants/MultilabelPipeline/MultilabelClassifier/outputs/convnext_base --seed 9229 --dataset invasive-512 --optimizer AdamW --decay 0.1 --name invasive_convnext_base --loss_type WBCE --wandb --cosine_annealing --num_workers 8 --server pda

# resnext50_32x4d
python src/inv_plts/multilabel_classification/train.py --lr 1e-4 --lr_warmup 5 --model resnext50_32x4d --batch-size 128 --epoch 100 --output_path /home/ksmehrab/InvasivePlants/MultilabelPipeline/MultilabelClassifier/outputs/resnext --seed 9229 --dataset invasive-512 --optimizer AdamW --decay 0.1 --name invasive_resnext --loss_type WBCE --wandb --cosine_annealing --num_workers 8 --server pda

# resnet50
python src/inv_plts/multilabel_classification/train.py --lr 1e-4 --lr_warmup 5 --model resnet50 --batch-size 128 --epoch 100 --output_path /home/ksmehrab/InvasivePlants/MultilabelPipeline/MultilabelClassifier/outputs/resnet50 --seed 9229 --dataset invasive-512 --optimizer AdamW --decay 0.1 --name invasive_resnet50 --loss_type WBCE --wandb --cosine_annealing --num_workers 8 --server pda

