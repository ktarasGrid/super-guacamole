'''
    Task 2: Create a script that uses the Survey Monkey (https://www.surveymonkey.com) service, creates a survey.

    PREREQUISITES:

    Sign up at https://www.surveymonkey.com 
    Create a draft application at https://developer.surveymonkey.com   
    No need to deploy your application. It's just for testing. Do not forget to set permissions for your application.
    After creating a draft application you will obtain an ACCESS_TOKEN which is needed to do API requests from your script.

    REQUIREMENTS: 

    The script should accept a JSON file with questions for the survey and a text file with a list of email addresses.
    The structure of a JSON file with questions:

{

   "Survey_Name": {

      "Page_Name": {

          "Question1_Name": {

              "Description" : "Description of question",

              "Answers" : [

                  "Answer1",

                  "Answer2",

                  "Answer3"

              ]

          },

          "Question2_Name": {

              "Description" : "Description of question",

              "Answers" : [

                  "Answer1",

                  "Answer2",

                  "Answer3"

              ]

          }

          . . .

      }

   }}

iii.     There should be at least 3 questions and 2 recipients.
'''

#preparation
def main():
    pass


if __name__ == "__main__":
    main()