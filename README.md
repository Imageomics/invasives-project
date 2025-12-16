# Invasives Species Biocontrol Quantification
Repository for the invasive species biocontrol quantification project as part of the AI &amp; Ecology Course field component in HI. The data associated with this project is available on Hugging Face: [Imageomics/invasive_plants_hawaii](https://huggingface.co/datasets/imageomics/invasive_plants_hawaii).

## Abstract
Invasive species are non-native organisms to an ecosystem that cause economic, environmental, and/or human harm. A soapbush (Clidemia Hirta) is such an invasive species forming dense thickets smothering other native plant life in Hawaii. Several biocontrols were released to control the spread of the soapbush, but quantifying the effect of such a release is difficult due to time consuming manual inspection. To alleviate these efforts, we collected a dataset of individual leaves from Clidemia Hirta bushes which were then photographed and labeled according to their damage type. We implemented baselines for automatic damage classification, detection, and segmentation for individual leaves.

## Environment Setup
Install [uv](https://docs.astral.sh/uv/) if not already done, and run the following command:
```
uv sync
```

## Classification Baseline
The classification baseline results can be found in `src/inv_plts/multilabel_classification`.

### Training
To train a classification baseline model run the following command `uv run python -m inv_plts.multilabel_classification.train --model resnet50`
More information on command line arguments can be found in `src/inv_plts/multilabel_classification.config.py`
More examples of these commands can be found in `scripts/train_classifiers.sh`

### Evaluation
To evaluate a classification baseline model run the following command `uv run python -m inv_plts.multilabel_classification.basic_evaluate --model resnet50`
More information on command line arguments can be found in `src/inv_plts/multilabel_classification.basic_evalute.py`
More examples of these commands can be found in `scripts/evaluate_classifiers.sh`

### Models
We report classification results for the following models: [ViT](https://arxiv.org/abs/2010.11929), [Resnet](https://arxiv.org/abs/1512.03385), [ConvNext](https://arxiv.org/abs/2201.03545), [CvT](https://arxiv.org/abs/2103.15808), [MaxViT](https://arxiv.org/abs/2204.01697)

## Faster R-CNN baseline
The [Faster R-CNN](https://arxiv.org/abs/1506.01497) baseline can be ran with the following notebook: `notebooks/rcnn_baseline/FasterRCNN_pipeline.ipynb`. The training and test splits are also given in `data/rcnn_cropped_annotations_[test,train].csv`. The archived images used to produce these results is available in the [images](https://huggingface.co/datasets/imageomics/invasive_plants_hawaii/tree/main/images) folder of our HuggingFace Repository (filename : `rcnn_images.zip`). 

## Zero-shot Segmentation using Molmo and SAM2 
The code for running [Molmo](https://arxiv.org/abs/2409.17146) and [SAM2](https://arxiv.org/abs/2408.00714) are in the corresponding notebooks in this directory: `notebooks/zero_shot_segmentation_pipeline`. Some example image names used for the qualitative analysis is provided in `data/sample_images.csv`. First, we need to run the molmo notebook `notebooks/zero_shot_segmentation_pipeline/run_molmo.ipynb` to generate points. Then, we need to run the sam2 notebook `notebooks/zero_shot_segmentation_pipeline/run_sam2_and_visualize.ipynb` to generate segmentation masks and visualize on images. 

## Leaf Reconstruction

The code for our Leaf Reconstruction baseline is available in the `scripts/leaf_reconstruction`. It contains the code to reproduce the results shown in our report (`scripts/leaf_reconstruction/get_absolute_error.py`), as well as the code to compute the ground truth damage ratio (`scripts/leaf_reconstruction/damage_calculation_ground_truth.py`). The code for testing HerbiEstim on a set of images can be found in the original repository of the authors [here](https://github.com/ZihuiWang1/HerbiEstim). The archived images used to produce our results is available in the [images](https://huggingface.co/datasets/imageomics/invasive_plants_hawaii/tree/main/images) folder of our HuggingFace Repository (filename : `Dataset_Leaf_Reconstruction.zip`). 

## Acknowledgement

This work was supported by both the [Imageomics Institute](https://imageomics.org) and the [AI and Biodiversity Change (ABC) Global Center](https://abcresearchcenter.org/). The Imageomics Institute is funded by the US National Science Foundation's Harnessing the Data Revolution (HDR) program under [Award #2118240](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2118240) (Imageomics: A New Frontier of Biological Information Powered by Knowledge-Guided Machine Learning). The ABC Global Center is funded by the US National Science Foundation under [Award No. 2330423](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2330423&HistoricalAwards=false) and Natural Sciences and Engineering Research Council of Canada under [Award No. 585136](https://www.nserc-crsng.gc.ca/ase-oro/Details-Detailles_eng.asp?id=782440). This code draws on research funded by the Social Sciences and Humanities Research Council. Any opinions, findings, conclusions, or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation, the Natural Sciences and Engineering Research Council of Canada, or the Social Sciences and Humanities Research Council.

We acknowledge the support of the [U.S. Forest Service](https://www.fs.usda.gov/), more specifically the researchers associated with the [Pacific Southwest Research Station](https://research.fs.usda.gov/psw) (Institute of Pacific Islands Forestry), for their support and collaboration in this research. Data collection and protocols were notably done in close collaboration with Dr. Ellyn Bitume, a research entomologist for the U.S. Forest Service. We also acknowledge the support of the [National Ecological Observatory Network](https://www.neonscience.org/) (NEON), a program sponsored by the U.S. National Science Foundation (NSF) and operated under cooperative agreement by Battelle. We especially thank the team associated with the [Pu'u Maka'ala Natural Area Reserve](https://www.neonscience.org/field-sites/puum), for helping us with logistics and equipment.

## Citation
Our code (this repository):
```
@software{invasive_species_code,
  author = {David Carlyn and Catherine Villeneuve and Kazi Sajeed Mehrab and Leonardo Viotti},
  title = {Invasives Species Biocontrol Quantification},
  version = {v1.0.0},
  year = {2025}
}
```

The dataset:
```
@dataset{invasive_plants_hawaii_dataset,
  author = {David Edward Carlyn and Catherine Villeneuve and Leonardo Viotti and Kazi Sajeed Mehrab
            and Ellyn Bitume and Chuck Stewart and Leanna House},
  title = {Hawaii Leaf Damage Dataset},
  year = {2025},
  url = {https://huggingface.co/datasets/imageomics/invasive_plants_hawaii},
  publisher = {Hugging Face}
}

```