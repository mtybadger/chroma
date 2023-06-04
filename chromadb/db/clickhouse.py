 Here is the updated code:

# type: ignore  
from chromadb.api.types import (  
    Documents,  
    Embeddings,  
    IDs,  
    Metadatas,  
    Where,  
    WhereDocument,  
)  
from chromadb.db import DB  
from chromadb.db.index.hnswlib import Hnswlib, delete_all_indexes  
import uuid  
import json  
from typing import Optional, Sequence, List, Tuple, cast  
import clickhouse_connect  
from clickhouse_connect.driver.client import Client  
from clickhouse_connect import common  
import logging  
from uuid import UUID  
from chromadb.config import System  
from overrides import override  
import numpy.typing as npt  
from chromadb.api.types import Metadata  

logger = logging.getLogger(__name__)  

COLLECTION_TABLE_SCHEMA = [{"uuid": "UUID"}, {"name": "String"}, {"metadata": "String"}]  

EMBEDDING_TABLE_SCHEMA = [  
    {"collection_uuid": "UUID"},  
    {"uuid": "UUID"},  
    {"embedding": "Array(Float64)"},  
    {"document