from pydantic import BaseModel

from ..enum.KindEnum import KindEnum


class CharacterModel(BaseModel):
    kind: KindEnum
    token: str
    points: int
    f: int = None
    h: int = None
    r: int = None
    a: int = None
    pdf: int = None
