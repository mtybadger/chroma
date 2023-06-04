 Here is the updated code:

import json
import time
from uuid import UUID
from typing import List, Optional, Sequence, cast
from chromadb import __version__
import chromadb.errors as errors
from chromadb.api import API
from chromadb.db import DB
from chromadb.api.types import (
    Documents,
    EmbeddingFunction,
    Embeddings,
    GetResult,
    IDs,
    Include,
    Metadata,
    Metadatas,
    QueryResult,
    Where,
    WhereDocument,
    CollectionMetadata,
)
from chromadb.api.models.Collection import Collection
from chromadb.config import System
import chromadb.utils.embedding_functions as ef
import re

from chromadb.telemetry import Telemetry
from chromadb.telemetry.events import CollectionAddEvent, CollectionDeleteEvent
from overrides import override
import pandas as pd


# mimics s3 bucket requirements for naming
def check_index_name(index_name: str) -> None:
    msg = (
        "Expected collection name that "
        "(1) contains 3-63 characters, "
        "(2) starts and ends with an alphanumeric character, "
        "(3