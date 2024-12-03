import requests
import json
import argparse
import sys

with open("config.json", "r") as f:
    config = json.load(f)

ACCESS_TOKEN = config.get("ACCESS_TOKEN")
API_BASE_URL = config.get("API_BASE_URL", "https://api.surveymonkey.com/v3")

if not ACCESS_TOKEN:
    raise ValueError("Missing 'ACCESS_TOKEN' in config.json.")

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
    }


def create_survey(survey_name):
    url = f"{API_BASE_URL}/surveys"
    data = {"title": survey_name}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    survey_id = response.json()["id"]
    print(f"Survey '{survey_name}' created with ID: {survey_id}")
    return survey_id


def add_page(survey_id, page_name):
    url = f"{API_BASE_URL}/surveys/{survey_id}/pages"
    data = {"title": page_name}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    page_id = response.json()["id"]
    print(f"Page '{page_name}' added with ID: {page_id}")
    return page_id


def add_question(survey_id, page_id, question_name, question_data):
    url = f"{API_BASE_URL}/surveys/{survey_id}/pages/{page_id}/questions"
    data = {
        "headings": [{"heading": question_name}],
        "family": "single_choice",
        "subtype": "vertical",
        "answers": {"choices": [{"text": ans} for ans in question_data["Answers"]]},
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    question_id = response.json()["id"]
    print(f"Question '{question_name}' added with ID: {question_id}")
    return question_id


def create_collector(survey_id):
    url = f"{API_BASE_URL}/surveys/{survey_id}/collectors"
    data = {"type": "email", "name": "Email Collector"}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    collector_id = response.json()["id"]
    print(f"Collector created with ID: {collector_id}")
    return collector_id


def add_recipients(collector_id, email_list):
    url = f"{API_BASE_URL}/collectors/{collector_id}/recipients"
    data = {"contacts": [{"email": email} for email in email_list]}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    recipients = response.json()
    print(f"Recipients added: {len(email_list)}")
    return recipients


def send_survey(collector_id):
    url = f"{API_BASE_URL}/collectors/{collector_id}/messages"
    data = {
        "type": "invite",
        "subject": "We value your feedback",
        "body_text": "Please take our survey. Your feedback is important to us.",
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    message_id = response.json()["id"]
    print(f"Message created with ID: {message_id}")

    send_url = f"{API_BASE_URL}/collectors/{collector_id}/messages/{message_id}/send"
    send_response = requests.post(send_url, headers=headers)
    send_response.raise_for_status()
    print("Survey invitations sent to recipients.")


def main():
    parser = argparse.ArgumentParser(
        description="Create a SurveyMonkey survey from a JSON file and send it to email recipients."
    )
    parser.add_argument("json_file", help="Path to the JSON file with survey questions.")
    parser.add_argument("email_file", help="Path to the text file with email addresses.")
    args = parser.parse_args()

    try:
        with open(args.json_file, "r") as f:
            survey_data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        sys.exit(1)

    # Load email addresses from text file
    try:
        with open(args.email_file, "r") as f:
            email_list = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading email file: {e}")
        sys.exit(1)

    if len(email_list) < 2:
        print("At least 2 email addresses are required.")
        sys.exit(1)

    # Create the survey
    for survey_name, pages in survey_data.items():
        survey_id = create_survey(survey_name)
        for page_name, questions in pages.items():
            page_id = add_page(survey_id, page_name)
            for question_name, question_info in questions.items():
                add_question(survey_id, page_id, question_name, question_info)

        # Create collector and send survey
        collector_id = create_collector(survey_id)
        add_recipients(collector_id, email_list)
        send_survey(collector_id)


if __name__ == "__main__":
    main()
