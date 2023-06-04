 Here is the updated code:

from typing import Optional, cast
from chromadb.api import API
from chromadb.config import System
from chromadb.api.types import (
    Documents,
    Embeddings,
    EmbeddingFunction,
    IDs,
    Include,
    Metadatas,
    Where,
    WhereDocument,
    GetResult,
    QueryResult,
    CollectionMetadata,
)
import chromadb.utils.embedding_functions as ef
import pandas as pd
import requests
import json
from typing import Sequence
from chromadb.api.models.Collection import Collection
import chromadb.errors as errors
from uuid import UUID
from chromadb.telemetry import Telemetry
from overrides import override


class FastAPI(API):
    def __init__(self, system: System):
        super().__init__(system)
        url_prefix = "https" if system.settings.chroma_server_ssl_enabled else "http"
        system.settings.require("chroma_server_host")
        system.settings.require("chroma_server_http_port")
        self._api_url = f"{url_prefix}://{system.settings.chroma_server_host