 Here is the updated code:

from chromadb.api.types import Documents, EmbeddingFunction, Embeddings  
from pathlib import Path
import os
import tarfile
import requests
from typing import Any, Dict, List, cast
import numpy as np
import numpy.typing as npt
import importlib
from typing import Optional

try:
    from chromadb.is_thin_client import is_thin_client
except ImportError:
    is_thin_client = False


class SentenceTransformerEmbeddingFunction(EmbeddingFunction):
    # Since we do dynamic imports we have to type this as Any
    models: Dict[str, Any] = {}  

    # If you have a beefier machine, try "gtr-t5-large".
    # for a full list of options: https://huggingface.co/sentence-transformers, https://www.sbert.net/docs/pretrained_models.html
    def __init__(self, model_name: str = "all-MiniLM-L6-v2", device: str = "cpu"):
        if model_name not in self.models:
            try:
                from sentence_transformers import SentenceTransformer
            except ImportError:
               