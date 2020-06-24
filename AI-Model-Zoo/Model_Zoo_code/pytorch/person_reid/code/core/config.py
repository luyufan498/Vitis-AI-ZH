# Copyright 2019 Xilinx Inc.
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


# encoding: utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import yaml
from easydict import EasyDict as edict

__C = edict()
opt = __C
__C.seed = 0

__C.dataset = edict()
__C.dataset.name = 'market1501'
__C.dataset.num_classes = 751

__C.aug = edict()
__C.aug.resize_size = [256, 128]
__C.aug.color_jitter = False
__C.aug.random_erasing = False
__C.aug.random_mirror = True
__C.aug.pad = 10
__C.aug.random_crop = True

__C.test = edict()
__C.test.batch_size = 128
__C.test.load_path = False

__C.network = edict()
__C.network.depth = 50
__C.network.name = 'Baseline'
__C.network.last_stride = 1
__C.network.gpus = "0"
__C.network.workers = 8


def update_config(config_file):
    exp_config = None
    with open(config_file) as f:
        exp_config = edict(yaml.load(f, Loader=yaml.FullLoader))
        for k, v in exp_config.items():
            if k in __C:
                if isinstance(v, dict):
                    for vk, vv in v.items():
                        __C[k][vk] = vv
                else:
                    __C[k] = v
            else:
                raise ValueError("key must exist in configs.py")