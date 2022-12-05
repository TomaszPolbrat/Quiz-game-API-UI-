import requests  # ask API for information

question_api = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")  # question for API's data
question_data = question_api.json()["results"]  # gets only result data from all data
question_category = question_data[0]["category"]    # gets category data from results data
