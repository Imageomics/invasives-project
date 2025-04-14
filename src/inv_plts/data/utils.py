from datasets import load_dataset, Dataset

def load_hf_dataset(sampling_type="full", leaf_view="both", cache_dir="~/.cache/huggingface/datasets") -> Dataset:
    """_summary_

    Args:
        sampling_type (str, optional): The type of sampling ('opportunistic', 'systematic', 'full'). Defaults to "full".
        leaf_view (str, optional): The view of the leaf ('dorsal', 'ventral', 'both'). Defaults to "both".
        cache_dir (str, optional): The cache directory to download and store dataset files. Defaults to "~/.cache/huggingface/datasets".

    Returns:
        Dataset: _description_
    """
    return load_dataset("imageomics/invasive_plants_hawaii", name=sampling_type, split=leaf_view, cache_dir=cache_dir)
