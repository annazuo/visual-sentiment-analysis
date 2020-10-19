# Cross-Media Learning for Image Sentiment Analysis in the Wild

This repo contains the PyTorch-converted models for visual sentiment analysis trained on the
[T4SA](http://t4sa.it) (Twitter for Sentiment Analysis) dataset presented in \[1\].

## Usage Example
```sh
python predict.py images_list.txt --model vgg19_finetuned_all --batch_size 64 > predictions.csv
```
The output file contains three columns representing the probability of each image belonging respectively to the *negative*, *neutral*, and *positive* classes in this order.

## Converting the original Caffe models

Already converted models are available here: TODO.

We adopted [MMdnn](https://github.com/microsoft/MMdnn) to convert caffe models to PyTorch.
We recommend using the pre-built Docker image:
```
docker pull mmdnn/mmdnn:cpu.small
```

First, download the original models available from [http://t4sa.it] and extract them following this
folder structure:
```
original-models
├── hybrid_finetuned_all
│   ├── deploy.prototxt
│   ├── mean.binaryproto
│   ├── snapshot_iter_34560.caffemodel
│   └── ...
├── hybrid_finetuned_fc6+
│   ├── <same as above>
│   └── ...
├── vgg19_finetuned_all
│   ├── <same as above>
│   └── ...
└── vgg19_finetuned_fc6+
    ├── <same as above>
    └── ...
```

Then, run `convert_models.sh`:

```sh
docker run --rm -it -v $(pwd):/workspace -w /workspace mmdnn/mmdnn:cpu.small bash ./convert_models.sh
```
