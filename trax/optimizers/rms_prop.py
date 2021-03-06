# coding=utf-8
# Copyright 2020 The Trax Authors.
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

"""RMSProp optimizer class."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from trax.math import numpy as np
from trax.optimizers import base as opt_base


class RMSProp(opt_base.Optimizer):
  """RMSProp optimizer."""

  def __init__(self, learning_rate, gamma=0.9, eps=1e-8):  # pylint: disable=useless-super-delegation
    super(RMSProp, self).__init__(
        learning_rate=learning_rate,
        gamma=gamma,
        eps=eps,
    )

  def init(self, params):
    return np.ones_like(params)

  def update(self, step, grads, weights, avg_sq_grad, opt_params):
    del step
    learning_rate = opt_params['learning_rate']
    gamma = opt_params['gamma']
    eps = opt_params['eps']
    avg_sq_grad = avg_sq_grad * gamma + grads**2 * (1. - gamma)
    weights = weights - (learning_rate * grads /
                         (np.sqrt(avg_sq_grad) + eps)).astype(weights.dtype)
    return weights, avg_sq_grad
