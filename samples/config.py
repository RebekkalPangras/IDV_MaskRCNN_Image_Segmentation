import os
import sys
import time
import numpy as np
import imgaug  # https://github.com/aleju/imgaug (pip3 install imgaug)

from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
from pycocotools import mask as maskUtils


# Root directory of the project
ROOT_DIR = "/content/IDV_MaskRCNN_Image_Segmentation"

# Import Mask RCNN
sys.path.append(ROOT_DIR)  # To find local version of the library
from mrcnn.config import Config
from mrcnn import model as modellib, utils

# Path to trained weights file
MICR_MODEL_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")

# Directory to save logs and model checkpoints, if not provided
# through the command line argument --logs
DEFAULT_LOGS_DIR = os.path.join(ROOT_DIR, "logs")

############################################################
#  Configurations
############################################################

class MicrConfig(Config):
    """Configuration for training on MICR.
    Derives from the base Config class and overrides some values.
    """
    # Give the configuration a recognizable name
    NAME = "micr"

    # We use a GPU with 12GB memory, which can fit two images.
    # Adjust down if you use a smaller GPU.
    IMAGES_PER_GPU = 2

    # Uncomment to train on 8 GPUs (default is 1)
    # GPU_COUNT = 8

    # Number of classes (including background)
    NUM_CLASSES = 1 + 5  # micr has 80 classes

    # Number of training steps per epoch
    #STEPS_PER_EPOCH = 100

    # Skip detections with < 90% confidence
#    DETECTION_MIN_CONFIDENCE = 0.9
