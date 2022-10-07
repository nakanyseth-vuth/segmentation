import os
import re
from pathlib import Path
from typing import List, Union, Dict

from bilstm_tokenizer import tokenize_sentences_bilstm, tokenize_sentences_bilstm_pos
from segmentation.intents.intents import *

from segmentation.models import Intent
from segmentation.stores.process import sentences, segment, entity, pos

if __name__ == '__main__':
    schoolMajor()
    # fileName = "Bus"

    # Pe edit ah nis edit ah ler pg and brab tv tha ah na intent ah na, kom oy error klang,
    # doch សុខលាភ -> សុខ លាភ since they are first name all, add space between them
    # " សុខលាភ "
    # And dont forget to mer error list pg and recheck everything
