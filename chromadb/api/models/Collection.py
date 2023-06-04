 Here is the updated code:

from typing import TYPE_CHECKING, Optional, Tuple, cast, List  
from pydantic import BaseModel, PrivateAttr
from uuid import UUID
import chromadb.utils.embedding_functions as ef  

from chromadb.api.types import (
    CollectionMetadata,
    Embedding,
    Include,
    Metadata,
    Document,
    Where,
    IDs,
    EmbeddingFunction,
    GetResult,
    QueryResult,
    ID,
    OneOrMany,
    WhereDocument,
    maybe_cast_one_to_many,
    validate_ids,
    validate_include,
    validate_metadatas,
    validate_where,
    validate_where_document,
    validate_n_results,
    validate_embeddings,
)
import logging

logger = logging.getLogger(__name__)  

if TYPE_CHECKING:
    from chromadb.api import API


class Collection(BaseModel):
    name: str
    id: UUID
    metadata: Optional[CollectionMetadata] = None
    _client: "API" = PrivateAttr()
    _embedding_function: Optional[EmbeddingFunction] = PrivateAttr()

    def __init__(
        self,
        client: "API",
        name