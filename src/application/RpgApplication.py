from pydantic import ValidationError

from ..infra.RpgRepository import RpgRepository
from ..domain.requests.CreateCharacterRequest import CreateCharacterRequest
from ..domain.requests.UpdateCharacterRequest import UpdateCharacterRequest
from ..domain.mappers.Constants import Points, Messages
from ..domain.mappers.StatusCodes import HTTP_OK, HTTP_BAD_REQUEST
from ..domain.enum.OperationEnum import OperationEnum
from ..domain.utils import custom_reponse

repository = RpgRepository()

def create_character(payload: dict):
    try:
        payload_validated = CreateCharacterRequest(**payload).dict()
    except ValidationError:
        return custom_reponse({
                'message': Messages.MISSING_FIELD_KIND
            },
            HTTP_BAD_REQUEST
        )
    return custom_reponse({
                'token': 'eyJ0eXAiOiJKhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxIiwwianRp',
                'points': Points.KINDS[payload_validated.get('kind')]
            },
            HTTP_OK
        )

def update_character(payload: dict):
    try:
        payload_validated = UpdateCharacterRequest(**payload).dict()
    except ValidationError as error:
        print("error", error)
        return custom_reponse({
                'message': str(error)
            },
            HTTP_BAD_REQUEST
        )

    character = repository.get_character(payload_validated.get('token'))
    if not character:
        return custom_reponse({"message": "Not found"}, HTTP_BAD_REQUEST)

    points = payload_validated.get('parameters').get('points')
    parameter = payload_validated.get('parameters').get('attribute')

    if payload_validated.get('operation') == OperationEnum.addPoint:
        if character.get('points') >= points:
            character[parameter] = character.get('points') + points
            character['points'] = character.get('points') - points
            repository.update_character(character)

    if payload_validated.get('operation') == OperationEnum.removePoint:
        if character.get('points') >= points:
            character[parameter] = character.get('points') - points
            character['points'] = character.get('points') + points
            repository.update_character(character)

    if payload_validated.get('operation') == OperationEnum.end:
        if character.get('points') > 0:
            return custom_reponse({"message": Messages.FAIL}, HTTP_BAD_REQUEST)

    return custom_reponse({
                'token': payload_validated.get('token'),
                'message': Messages.SUCCESS
            },
            HTTP_OK
        )
