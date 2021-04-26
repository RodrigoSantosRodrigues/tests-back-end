from pydantic import BaseModel

from ..enum.KindEnum import KindEnum


class CreateCharacterRequest(BaseModel):
    kind: KindEnum
