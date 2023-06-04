 Here is the updated code:

from typing import Optional, Sequence, Any, Tuple, cast, Dict, Union, Set  
from uuid import UUID  
from overrides import override  
from pypika import Table, Column  
from itertools import groupby   

from chromadb.config import System  
from chromadb.db.base import (  
    Cursor,  
    SqlDB,  
    ParameterValue,  
    get_sql,  
    NotFoundError,  
    UniqueConstraintError,  
)  
from chromadb.db.system import SysDB  
from chromadb.types import (  
    OptionalArgument,  
    Segment,  
    Metadata,  
    Collection,  
    SegmentScope,  
    Unspecified,  
    UpdateMetadata,  
)  


class SqlSysDB(SqlDB, SysDB):  
    def __init__(self, system: System):  
        super().__init__(system)  

    @override  
    def create_segment(self, segment: Segment) -> None:  
        with self.tx() as cur:  
            segments = Table("segments")  
            insert_segment = (  
                self.querybuilder()  
                .into(segments)  
                .columns(  
                    segments.id,  
                    segments.type,  
                    segments