 Here is the updated code:

import os
import pickle
import time
from typing import Dict, List, Optional, Set, Tuple, Union, cast

from chromadb.api.types import Embeddings, IndexMetadata
import hnswlib
from chromadb.config import Settings
from chromadb.db.index import Index
from chromadb.errors import (
    InvalidDimensionException,
)
import logging
import re
from uuid import UUID
import multiprocessing

logger = logging.getLogger(__name__)


valid_params = {
    "hnsw:space": r"^(l2|cosine|ip)$",
    "hnsw:construction_ef": r"^\d+$",
    "hnsw:search_ef": r"^\d+$",
    "hnsw:M": r"^\d+$",
    "hnsw:num_threads": r"^\d+$",
    "hnsw:resize_factor": r"^\d+(\.\d+)?$",
}

DEFAULT_CAPACITY = 1000


class HnswParams:
    space: str
    construction_ef: int
    search_ef: int
    M: