from ...domain.mappers.StatusCodes import HTTP_BAD_REQUEST
from ...domain.mappers.Constants import Messages


request_payload_character_person = {
    "kind": "Person"
}

request_payload_character_hero = {
    "kind": "Hero"
}

request_payload_character_fighter = {
    "kind": "Fighter"
}

request_payload_character_person_with_empty_field = {
    "kind": ""
}

request_payload_character_person_with_empty_payload = {}

response_payload_character_person_with_empty_field = {
    "status": HTTP_BAD_REQUEST,
    "body": {
        "message": Messages.MISSING_FIELD_KIND
    }
}

response_payload_character_person_with_empty_payload = {
    "status": HTTP_BAD_REQUEST,
    "body": {
        "message": Messages.MISSING_FIELD_KIND
    }
}
