 Here is the updated code:

import pytest
import hypothesis.strategies as st
from hypothesis import given, settings
from chromadb.api import API
import chromadb.test.property.strategies as strategies
import chromadb.test.property.invariants as invariants

collection_st = st.shared(strategies.collections(with_hnsw_params=True), key="coll")


@given(collection=collection_st, embeddings=strategies.recordsets(collection_st))
@settings(deadline=None)
def test_add(
    api: API, collection: strategies.Collection, embeddings: strategies.RecordSet
):
    api.reset()

    coll = api.create_collection(
        name=collection.name,
        metadata=collection.metadata,
        embedding_function=collection.embedding_function,
    )
    coll.add(**embeddings)

    embeddings = invariants.wrap_all(embeddings)
    invariants.count(coll, embeddings)
    n_results = max(1, (len(embeddings["ids"]) // 10))
    invariants.ann_accuracy(
        coll,
        embeddings,
        n_results=n_results,
        embedding_