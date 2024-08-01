import logging
import os
from typing import Dict

import torch
from omegaconf import OmegaConf
from tqdm import tqdm

from . import util

log = logging.getLogger(__name__)


def run(cfg: Dict):
    log.info("Load datasets...")

    print(cfg)
