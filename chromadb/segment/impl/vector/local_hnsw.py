 Here is my proposed solution:

from overrides import override  
from typing import Optional, Sequence, Dict, Set, List, Callable, Union, cast
from uuid import UUID
from chromadb.segment import VectorReader
from chromadb.ingest import Consumer
from chromadb.config import Component, System, Settings
from chromadb.types import (
    EmbeddingRecord,
    VectorEmbeddingRecord,
    VectorQuery,
    VectorQueryResult,
    SeqId,
    Segment,
    Metadata,
    Operation,
    Vector,
)
from chromadb.errors import InvalidDimensionException
import re
import multiprocessing
import hnswlib
from threading import Lock
import logging

logger = logging.getLogger(__name__)  

DEFAULT_CAPACITY = 1000  

Validator = Callable[[Union[str, int, float]], bool]  

param_validators: Dict[str, Validator] = {
    "hnsw:space": lambda p: bool(re.match(r"^(l2|cosine|ip)$", str(p))),
    "hnsw:construction_ef": lambda p: isinstance(p, int),
    "hnsw:search_ef": lambda p: isinstance(