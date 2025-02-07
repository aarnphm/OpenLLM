from typing import List, Literal, Tuple

from .merger import Merger
DEFAULT_TYPE_SPECIFIC_MERGE_STRATEGIES: List[Tuple[type, Literal['append', 'merge', 'union']]] = ...
always_merger: Merger = ...
merge_or_raise: Merger = ...
conservative_merger: Merger = ...
