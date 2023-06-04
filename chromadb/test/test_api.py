 Here is the updated code:

# type: ignore
import chromadb
from chromadb.api.types import QueryResult
from chromadb.config import Settings
import chromadb.server.fastapi
import pytest
import tempfile
import numpy as np
from chromadb.utils.embedding_functions import (
    DefaultEmbeddingFunction,
)


@pytest.fixture
def local_persist_api():
    return chromadb.Client(
        Settings(
            chroma_api_impl="local",
            chroma_db_impl="duckdb+parquet",
            persist_directory=tempfile.gettempdir() + "/test_server",
        )
    )


# https://docs.pytest.org/en/6.2.x/fixture.html#fixtures-can-be-requested-more-than-once-per-test-return-values-are-cached
@pytest.fixture
def local_persist_api_cache_bust():
    return chromadb.Client(
        Settings(
            chroma_api_impl="local",
            chroma_db_impl="duckdb+parquet",
            persist_directory=tempfile.gettempdir() + "/test_server",
       