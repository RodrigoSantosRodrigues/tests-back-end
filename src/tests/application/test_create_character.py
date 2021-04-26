import unittest

from ...domain.enum.KindEnum import KindEnum
from ...application.RpgApplication import create_character
from ...domain.mappers.StatusCodes import HTTP_OK, HTTP_BAD_REQUEST
from ...domain.mappers.Constants import Points, Messages
from .data_create import (
    request_payload_character_person, 
    request_payload_character_hero, 
    request_payload_character_fighter,
    request_payload_character_person_with_empty_field,
    request_payload_character_person_with_empty_payload,
    response_payload_character_person_with_empty_field,
    response_payload_character_person_with_empty_payload
)


class TestCreateCharacter(unittest.TestCase):

    def test_create_character_person_with_successful_return(self):
        response = create_character(request_payload_character_person)
        self.assertTrue(
            response.get('body').get('token')
        )
        self.assertTrue(
            response.get('body').get('points')
        )
        self.assertEqual(
            response.get('body').get('points'),
            Points.KINDS[KindEnum.person]
        )
        self.assertEqual(response.get('status'), HTTP_OK)

    def test_create_character_hero_with_successful_return(self):
        response = create_character(request_payload_character_hero)
        self.assertTrue(
            response.get('body').get('token')
        )
        self.assertTrue(
            response.get('body').get('points')
        )
        self.assertEqual(
            response.get('body').get('points'),
            Points.KINDS[KindEnum.hero]
        )
        self.assertEqual(response.get('status'), HTTP_OK)

    def test_create_character_fighter_with_successful_return(self):
        response = create_character(request_payload_character_fighter)
        self.assertTrue(
            response.get('body').get('token')
        )
        self.assertTrue(
            response.get('body').get('points')
        )
        self.assertEqual(
            response.get('body').get('points'),
            Points.KINDS[KindEnum.fighter]
        )
        self.assertEqual(response.get('status'), HTTP_OK)

    def test_create_character_person_with_empty_kind_field_and_error_return(self):
        response = create_character(
            request_payload_character_person_with_empty_field
        )
        self.assertEqual(response.get('status'), HTTP_BAD_REQUEST)
        self.assertEqual(
            response.get('body').get('message'),
            Messages.MISSING_FIELD_KIND
        )
        self.assertDictEqual(
            response,
            response_payload_character_person_with_empty_field
        )

    def test_create_character_person_with_empty_payload_and_error_return(self):
        response = create_character(
            request_payload_character_person_with_empty_payload
        )
        self.assertEqual(response.get('status'), HTTP_BAD_REQUEST)
        self.assertEqual(
            response.get('body').get('message'),
            Messages.MISSING_FIELD_KIND
        )
        self.assertDictEqual(
            response,
            response_payload_character_person_with_empty_payload
        )
