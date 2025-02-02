import requests

parameters = {
    "amount":10,
    "type":'boolean'
}

questions_json = requests.get("https://opentdb.com/api.php", params=parameters)
# questions_json.raise_for_status()

if questions_json.status_code == 200 :


    question_data = dict(questions_json.json())

    question_data = question_data['results']

else :
    question_data = [
        {"type": "boolean",
         "difficulty": "easy",
         "category": "Science: Computers",
         "question": "The logo for Snapchat is a Bell.",
         "correct_answer": "False",
         "incorrect_answers": ["True"]},

        {"type": "boolean", "difficulty": "easy",
         "category": "Science: Computers",
         "question": "The Windows ME operating system was released in the year 2000.",
         "correct_answer": "True",
         "incorrect_answers": ["False"]},

        {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
         "question": "In most programming languages, the operator ++ is equivalent to the statement &quot;+= 1&quot;.",
         "correct_answer": "True", "incorrect_answers": ["False"]},
        {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
         "question": "The Python programming language gets its name from the British comedy group &quot;Monty Python.&quot;",
         "correct_answer": "True", "incorrect_answers": ["False"]},
        {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
         "question": "Linux was first created as an alternative to Windows XP.", "correct_answer": "False",
         "incorrect_answers": ["True"]}, {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
                                          "question": "Pointers were not used in the original C programming language; they were added later on in C++.",
                                          "correct_answer": "False", "incorrect_answers": ["True"]},
        {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
         "question": "Time on Computers is measured via the EPOX System.", "correct_answer": "False",
         "incorrect_answers": ["True"]}, {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
                                          "question": "&quot;HTML&quot; stands for Hypertext Markup Language.",
                                          "correct_answer": "True", "incorrect_answers": ["False"]},
        {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
         "question": "Ada Lovelace is often considered the first computer programmer.", "correct_answer": "True",
         "incorrect_answers": ["False"]}, {"type": "boolean", "difficulty": "easy", "category": "Science: Computers",
                                           "question": "Linus Torvalds created Linux and Git.",
                                           "correct_answer": "True",
                                           "incorrect_answers": ["False"]}]
