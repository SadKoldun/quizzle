import requests

parameters = {
    "amount": 10,
    "type": 'boolean',

}

new_response = requests.get(url='https://opentdb.com/api.php', params=parameters)
question_data = new_response.json()['results']

