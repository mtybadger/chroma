 Here is the updated file:

from typing import Optional, Union, Sequence, Dict, Mapping, List
from typing_extensions import Literal, TypedDict, TypeVar
from uuid import UUID
from enum import Enum

Metadata = Mapping[str, Union[str, int, float]]
UpdateMetadata = Mapping[str, Union[int, float, str, None]]

# Namespaced Names are mechanically just strings, but we use this type to indicate that
# the intent is for the value to be globally unique and semantically meaningful.
NamespacedName = str


class ScalarEncoding(Enum):
    FLOAT32 = "FLOAT32"
    INT32 = "INT32"


class SegmentScope(Enum):
    VECTOR = "VECTOR"
    METADATA = "METADATA"


class Collection(TypedDict):
    id: UUID
    name: str
    topic: str
    metadata: Optional[Metadata]


class Segment(TypedDict):
    id: UUID
    type: NamespacedName
    scope: SegmentScope
    # If a segment has a topic, it implies that this segment is a consumer of the topic
    # and indexes the contents of the topic.
    topic: Optional[str]