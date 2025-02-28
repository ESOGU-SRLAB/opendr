# Copyright 2020-2022 OpenDR European Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from opendr.perception.semantic_segmentation import BisenetLearner
from opendr.perception.semantic_segmentation import CamVidDataset


if __name__ == '__main__':
    learner = BisenetLearner()

    # Download CamVid dataset
    if not os.path.exists('./datasets/'):
        CamVidDataset.download_data('./datasets/')
    datatest = CamVidDataset('./datasets/CamVid/', mode='test')

    # Download the pretrained model
    learner.download('./bisenet_camvid', mode='pretrained')
    learner.load('./bisenet_camvid')
    results = learner.eval(dataset=datatest)

    print("Evaluation results = ", results)
