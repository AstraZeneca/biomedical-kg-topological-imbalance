# Biomedical KG Topological Imbalance

![Maturity level-1](https://img.shields.io/badge/Maturity%20Level-ML--1-yellow)
[![Arxiv](https://img.shields.io/badge/ArXiv-2112.06567-orange.svg)](https://arxiv.org/abs/2112.06567)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pykeen)](https://img.shields.io/pypi/pyversions/pykeen)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

<p align="center">
  <img width="800" src="https://github.com/AstraZeneca/biomedical-kg-topological-imbalance/raw/master/result.png">
</p>

This repository accompanies our paper [Implications of Topological Imbalance for Representation Learning on Biomedical Knowledge Graphs](https://academic.oup.com/bib/advance-article-abstract/doi/10.1093/bib/bbac279/6649936) and enables replication of the key results.

## Notebooks

This repository contains four jupyter notebooks which replicate the key results and figures from the manuscript. The notebooks are:

- [`target_prediction.ipynb`](target_prediction.ipynb): This notebook replicates the primary finding of the work and shows how the degree of genes in Hetionet correlates with their predicted score for association with various diseases.
- [`trivial_relations.ipynb`](trivial_relations.ipynb): This notebook explores how the presence of other relationship types between a given gene-disease pair can influence the score of the associates relationship.
- [`other_models.ipynb`](other_models.ipynb): The notebook explores the entity degree to predicted score across three other models: DistMult, RotatE and TransH.
- [`other_tasks.ipynb`](other_tasks.ipynb): The notebook explores the entity degree to predicted score across three other tasks: Drug Repositioning, Protein-Protein Interaction and Drug-Target Interaction.

## Installation Dependencies

The dependencies required to run the notebooks can be installed as follows:

```shell
$ pip install -r requirements.txt
```

The code relies primarily on the [PyKEEN](https://github.com/pykeen/pykeen) package, which uses [PyTorch](https://pytorch.org/) behind the scenes for gradient computation. If you are planning to retrain the models, instead of using the pretrained weight file provided as part of this repository, it would be advisable to ensure you install a GPU enabled version of PyTorch first. Details on how to do this are provided [here](https://pytorch.org/get-started/locally/).

## Model

A pretrained version of the [TransE](https://proceedings.neurips.cc/paper/2013/file/1cecc7a77928ca8133fa24680a88d2f9-Paper.pdf) model is provided in the `artifacts` directory. This version is automatically used in the notebooks.

Due to the size of weight files for the other models used in the study, they were unable to be included in main repository. However, the files are available for download as part of the release of the repository [here](https://github.com/AstraZeneca/biomedical-kg-topological-imbalance/releases/tag/0.2.0). Once the files have been downloaded, please place them in the `artifacts` directory if you wish to use them.

Note that the code is provided to retrain any of the models in the `train.py` file in the `src` directory.

## Citation

Please consider citing the paper for this repo if you find it useful:

```
@article{bonner2022implications,
    author = {Bonner, Stephen and Kirik, Ufuk and Engkvist, Ola and Tang, Jian and Barrett, Ian P},
    title = {Implications of topological imbalance for representation learning on biomedical knowledge graphs},
    journal = {Briefings in Bioinformatics},
    year = {2022},
    month = {07},
    doi = {10.1093/bib/bbac279},
}
```

**License**

- [Apache 2.0](https://github.com/AstraZeneca/awesome-drug-discovery-knowledge-graphs/blob/master/LICENSE)
