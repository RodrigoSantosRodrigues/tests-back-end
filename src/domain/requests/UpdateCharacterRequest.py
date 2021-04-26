from pydantic import BaseModel
from ..enum.AttributeEnum import AttributeEnum
from ..enum.OperationEnum import OperationEnum


class Parameter(BaseModel):
    attribute: AttributeEnum
    points: int 

class UpdateCharacterRequest(BaseModel):
    token: str
    operation: OperationEnum
    parameters: Parameter
