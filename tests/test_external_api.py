# pytest tests/test_external_api.py
import json
from unittest.mock import patch
from src.external_api import get_convert, get_exchange_rate

transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": 8221.37,
            "currency": {
                "name": "RUB",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }


def test_get_convert_with():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = 8221.37
        assert get_convert(transaction) == 8221.37
        mock_get.assert_called_once_with('https://apilayer.com/exchangerates_data-api'), {base}, {symbols}

# @patch('src.github.requests.get')
# def test_get_user_info(mocked_get):
#     mocked_get.return_value.status_code = 200
#     mocked_get.return_value.json.return_value = {'login': 'test_user', 'public_repos': 10}
#     result = get_user_info('test_user')
#     assert result == (True, {'login': 'test_user', 'public_repos': 10})
#
# @patch('src.github.requests.get')
# def test_get_user_info_invalid(mocked_get):
#     mocked_get.return_value.json.return_value = {'message': 'Not Found'}
#     result = get_user_info('non_existent_user')
#     assert result == (False, {})
#
# @patch('src.github.requests.get')
# def test_get_user_repos(mocked_get):
#     mocked_get.return_value.status_code = 200
#     mocked_get.return_value.json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]
#     result = get_user_repos('test_user')
#     assert result == (True, ['repo1', 'repo2'])
#
# @patch('src.github.requests.get')
# def test_get_user_repos_invalid(mocked_get):
#     mocked_get.return_value.status_code = 404
#     mocked_get.return_value.json.return_value = {'message': 'Not Found'}
#     result = get_user_repos('non_existent_user')
#     assert result == (False, [])
#
# @patch('src.github.get_user_info')
# @patch('src.github.get_user_repos')
# def test_get_github_users(mock_get_user_repos, mock_get_user_info):
#     mock_get_user_info.return_value = (True, {'login': 'user1', 'public_repos': 2})
#     mock_get_user_repos.return_value = (True, ['repo1', 'repo2'])
#     expected_result = [{'login': 'user1', 'public_repos': 2, 'repositories': ['repo1', 'repo2']}]
#     result = get_github_users(['user1'])
#     assert result == json.dumps(expected_result)
#
# @patch('src.github.get_user_info')
# @patch('src.github.get_user_repos')
# def test_get_github_users_negative(mock_get_user_repos, mock_get_user_info):
#     mock_get_user_info.return_value = (False, {})
#     mock_get_user_repos.return_value = (False, [])
#     result = get_github_users(['non_existent_user'])
#     assert result == None