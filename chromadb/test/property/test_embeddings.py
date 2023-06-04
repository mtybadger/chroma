 Here is the updated code:

import pytest
import logging
import hypothesis.strategies as st
from typing import Set
from dataclasses import dataclass
from chromadb.api.types import Include
import chromadb.errors as errors
from chromadb.api import API
from chromadb.api.models.Collection import Collection
import chromadb.test.property.strategies as strategies
from hypothesis.stateful import (
    Bundle,
    RuleBasedStateMachine,
    rule,
    initialize,
    precondition,
    consumes,
    run_state_machine_as_test,
    multiple,
    invariant,
)
from collections import defaultdict
import chromadb.test.property.invariants as invariants
import numpy as np


traces = defaultdict(lambda: 0)


def trace(key):
    global traces
    traces[key] += 1


def print_traces():
    global traces
    for key, value in traces.items():
        print(f"{key}: {value}")


dtype_shared_st = st.shared(st.sampled_from(strategies.float_types), key="dtype")
dimension_shared_st = st.shared(
    st.integers(