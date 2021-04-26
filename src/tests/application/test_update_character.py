import unittest
from unittest.mock import patch

from ...application.RpgApplication import update_character
from ...domain.mappers.StatusCodes import HTTP_OK, HTTP_BAD_REQUEST
from ...domain.mappers.Constants import Messages
from .data_update import (
    request_payload_character,
    request_payload_character_hero_with_end_operation_points_error,
    request_payload_character_with_remove_points,
    response_payload_character,
    data_repository_get_hero_created,
    data_repository_update_hero_created
)


class TestUpdateCharactere(unittest.TestCase):

    @patch("src.application.RpgApplication.repository")
    def test_update_charactere_hero_with_sucessfull_return(
            self,
            mock_repository
        ):
        mock_repository.get_character.return_value = data_repository_get_hero_created
        mock_repository.update_character.return_value = data_repository_update_hero_created
        response = update_character(request_payload_character)
        self.assertEqual(response.get("status"), HTTP_OK)
        self.assertEqual(
            response.get('body').get('token'),
            response_payload_character.get('body').get('token')
        )
        self.assertDictEqual(response, response_payload_character)
        self.assertEqual(mock_repository.get_character.call_count, 1)
        self.assertEqual(mock_repository.update_character.call_count, 1)

    @patch("src.application.RpgApplication.repository")
    def test_update_character_hero_with_end_operation_and_return_error(
            self,
            mock_repository
        ):
        mock_repository.get_character.return_value = data_repository_update_hero_created
        response = update_character(
            request_payload_character_hero_with_end_operation_points_error
        )
        self.assertEqual(response.get('status'), HTTP_BAD_REQUEST)
        self.assertEqual(response.get('body').get('message'), Messages.FAIL)
        self.assertEqual(mock_repository.get_character.call_count, 1)
        self.assertEqual(mock_repository.update_character.call_count, 0)

    @patch("src.application.RpgApplication.repository")
    def test_update_character_hero_with_removepoints_operation_sucessfull_return(
            self,
            mock_repository
        ):
        mock_repository.get_character.return_value = data_repository_get_hero_created
        mock_repository.update_character.return_value = data_repository_update_hero_created
        response = update_character(
            request_payload_character_with_remove_points
        )
        self.assertEqual(response.get('status'), HTTP_OK)
        self.assertEqual(response.get('body').get('message'), Messages.SUCCESS)
        self.assertEqual(mock_repository.get_character.call_count, 1)
        self.assertEqual(mock_repository.update_character.call_count, 1)
