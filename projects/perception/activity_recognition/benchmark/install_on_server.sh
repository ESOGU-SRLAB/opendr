#!/bin/bash

conda create --name opendr python=3.8
conda activate opendr
conda env config vars set OPENDR_HOME=$PWD
conda env config vars set PYTHONPATH=$OPENDR_HOME/src:$PYTHONPATH

# Reactivate env to let env vars take effect
conda deactivate opendr
conda activate opendr

pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 -f https://download.pytorch.org/whl/torch_stable.html
pip install pytorch_lightning==1.2.3 onnxruntime==1.3.0 opencv-python==4.5.1.48 joblib>=1.0.1 pytorch_benchmark
