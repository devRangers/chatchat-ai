import os
import argparse
import numpy as np
from omegaconf import OmegaConf, DictConfig
import logging
import torch

from harm_chat_detector import seed_everything, run

log = logging.getLogger(__name__)


def main(cfg):

    seed_everything(cfg.base.seed)
    torch.backends.cudnn.benchmark = True

    run(cfg)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Training script for harm_chat_detector"
    )
    parser.add_argument(
        "--config",
        type=str,
        default="configs/train.yaml",
        help="Path to the train config file",
    )
    args = parser.parse_args()

    cfg = OmegaConf.load(args.config)

    main(cfg)
