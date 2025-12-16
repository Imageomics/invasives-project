#!/bin/bash

export CUDA_VISIBLE_DEVICES=0

python src/inv_plts/multilabel_classification/basic_evaluate.py --model_name maxvit_t --checkpoint_path /home/ksmehrab/InvasivePlants/MultilabelPipeline/MultilabelClassifier/outputs/maxvit/ckpt_9229_S9229_invasive_maxvit_t_invasive-512_maxvit_t.t7 --output_path /home/ksmehrab/InvasivePlants/MultilabelPipeline/MultilabelClassifier/outputs/maxvit --server pda --batch_size 256 --num_workers 8

python src/inv_plts/multilabel_classification/basic_evaluate.py --model_name vit_b_16 --checkpoint_path /home/ksmehrab/InvasivePlants/MultilabelPipeline/MultilabelClassifier/outputs/vitb/ckpt_9229_S9229_invasive_vitb_invasive-512_vit_b_16.t7 --output_path /home/ksmehrab/InvasivePlants/MultilabelPipeline/MultilabelClassifier/outputs/vitb --server pda --batch_size 256 --num_workers 8

python src/inv_plts/multilabel_classification/basic_evaluate.py --model_name cvt_13 --checkpoint_path /home/ksmehrab/InvasivePlants/MultilabelPipeline/MultilabelClassifier/outputs/cvt_13/ckpt_9229_S9229_invasive_cvt_13_invasive-512_cvt_13.t7 --output_path /home/ksmehrab/InvasivePlants/MultilabelPipeline/MultilabelClassifier/outputs/cvt_13 --server pda --batch_size 256 --num_workers 8

python src/inv_plts/multilabel_classification/basic_evaluate.py --model_name convnext_base --checkpoint_path /home/ksmehrab/InvasivePlants/MultilabelPipeline/MultilabelClassifier/outputs/convnext_base/ckpt_9229_S9229_invasive_convnext_base_invasive-512_convnext_base.t7 --output_path /home/ksmehrab/InvasivePlants/MultilabelPipeline/MultilabelClassifier/outputs/convnext_base --server pda --batch_size 256 --num_workers 8

python src/inv_plts/multilabel_classification/basic_evaluate.py --model_name resnext50_32x4d --checkpoint_path /home/ksmehrab/InvasivePlants/MultilabelPipeline/MultilabelClassifier/outputs/resnext/ckpt_9229_S9229_invasive_resnext_invasive-512_resnext50_32x4d.t7 --output_path /home/ksmehrab/InvasivePlants/MultilabelPipeline/MultilabelClassifier/outputs/resnext --server pda --batch_size 256 --num_workers 8

python src/inv_plts/multilabel_classification/basic_evaluate.py --model_name resnet50 --checkpoint_path /home/ksmehrab/InvasivePlants/MultilabelPipeline/MultilabelClassifier/outputs/resnet50/ckpt_9229_S9229_invasive_resnet50_invasive-512_resnet50.t7 --output_path /home/ksmehrab/InvasivePlants/MultilabelPipeline/MultilabelClassifier/outputs/resnet50 --server pda --batch_size 256 --num_workers 8