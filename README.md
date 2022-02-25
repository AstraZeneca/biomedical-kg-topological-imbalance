[![Maturity level-Prototype](https://img.shields.io/badge/Maturity%20Level-Prototype-red)
![Arxiv](https://img.shields.io/badge/ArXiv-2112.06567-orange.svg)](https://arxiv.org/abs/2112.06567)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pykeen)](https://img.shields.io/pypi/pyversions/pykeen)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# Biomedical KG Topological Imbalance

This repository accompanies our paper [Implications of Topological Imbalance for Representation Learning on Biomedical Knowledge Graphs](https://arxiv.org/abs/2112.06567) and enables replication of our key results.

## Installation Dependencies

The dependencies required to run the notebooks can be installed as follows:

```shell
$ pip install -r requirements.txt
```

The code relies primarily on the [PyKEEN](https://github.com/pykeen/pykeen) package, which uses [PyTorch](https://pytorch.org/) behind the scenes for gradient computation. If you are planning to retrain the models, instead of using the pretrained weight file provided as part of this repository, it would be advisable to ensure you install a GPU enabled version of PyTorch first. Details on how to do this are provided [here](https://pytorch.org/get-started/locally/).

## Citation

Please consider citing the paper for this repo if you find it useful:

```
@article{bonner2021implications,
  title={Implications of Topological Imbalance for Representation Learning on Biomedical Knowledge Graphs},
  author={Bonner, Stephen and Kirik, Ufuk and Engkvist, Ola and Tang, Jian and Barrett, Ian P},
  journal={arXiv preprint arXiv:2112.06567},
  year={2021}
}
```


**License**

- [Apache 2.0](https://github.com/AstraZeneca/awesome-drug-discovery-knowledge-graphs/blob/master/LICENSE)