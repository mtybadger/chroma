 Here is the updated file:

from chromadb.segment import (
    SegmentImplementation,
    SegmentManager,
    MetadataReader,
    VectorReader,
)
from chromadb.config import System, get_class
from chromadb.db.system import SysDB
from overrides import override
from enum import Enum
from chromadb.types import Collection, Segment, SegmentScope
from typing import Dict, Set, Type, TypeVar
from uuid import UUID, uuid4
from collections import defaultdict
import re


class SegmentType(Enum):
    SQLITE = "urn:chroma:segment/metadata/sqlite"
    HNSW_LOCAL_MEMORY = "urn:chroma:segment/vector/hnsw-local-memory"


SEGMENT_TYPE_IMPLS = {
    SegmentType.SQLITE: "chromadb.segment.impl.sqlite.SqliteMetadataReader",
    SegmentType.HNSW_LOCAL_MEMORY: "chromadb.segment.impl.vector.local_hnsw.LocalHnswSegment",
}

PROPAGATE_METADATA = {
    SegmentType.HNSW_LOCAL_MEMORY: [r"^hnsw:.*