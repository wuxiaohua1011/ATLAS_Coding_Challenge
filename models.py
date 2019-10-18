from typing import List,Tuple
from pydantic import BaseModel, FilePath

class Segment(BaseModel):
    id: int
    data_file_name: FilePath = None
    segment_name: str
    indices: List[int]
    type: str = "Layout"
    type_class: Tuple[str, int] = None
    intersection: int = 0
    plane_equation: Tuple[List[float], float] = None
    vertices: List[List[float]] = None

