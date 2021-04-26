from ...domain.mappers.StatusCodes import HTTP_OK, HTTP_BAD_REQUEST
from ...domain.mappers.Constants import Messages


request_payload_character = {
    "token": "xxxxxxx",
    "operation": "addPoint",
    "parameters": {
        "attribute": "f",
        "points": 1
    }
}

request_payload_character_hero_with_end_operation_points_error = {
    "token": "xxxxxxx",
    "operation": "end",
    "parameters": {
        "attribute": "a",
        "points": 1
    }
}

request_payload_character_with_remove_points = {
    "token": "xxxxxxx",
    "operation": "removePoint",
    "parameters": {
        "attribute": "f",
        "points": 1
    }
}

response_payload_character = {
    "status": HTTP_OK,
    "body": {
        "message": Messages.SUCCESS,
        "token": "xxxxxxx"
    }
}

data_repository_get_hero_created = {
    "kind": "Hero",
    "points": 4,
    "token": "xxxxxx",
    "f": 1,
    "h": 0,
    "r": 0,
    "a": 0,
    "pdf": 0,
}

data_repository_update_hero_created = {
    "kind": "Hero",
    "points": 3,
    "token": "xxxxxx",
    "f": 1,
    "h": 0,
    "r": 1,
    "a": 0,
    "pdf": 0,
}
