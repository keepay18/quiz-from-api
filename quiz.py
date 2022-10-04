import requests
import html


class Question:
    def __init__(self, category, question_str, correct_answer_flag):
        self.category = category
        self.question_str = question_str
        self.correct_answer_flag = correct_answer_flag


class Quiz:
    def __init__(self, num_of_questions):
        self.api_url = f"https://opentdb.com/api.php?amount={str(num_of_questions)}&difficulty=easy&type=boolean"
        self.num_of_questions = num_of_questions
        self.questions_list = []
        self.loadQuestions(num_of_questions)

    def loadQuestions(self, num_of_questions):
        response = requests.get(self.api_url)
        if response.ok:
            data = response.json()
            results = data["results"]

            for question in results:
                category = question["category"]
                question_type = question["type"]
                difficulty = question["difficulty"]
                question_str = html.unescape(question["question"])
                print(question_str)
                correct_answer_flag = question["correct_answer"].lower() in [
                    'true', '1', 'yes']

                q_obj = Question(category, question_str, correct_answer_flag)
                self.questions_list.append(q_obj)

    def startQuiz(self):
        print("\nWelcome to Quiz!!!")
        num_correct_user_answers = 0
        n = 1
        num_of_questions = len(self.questions_list)

        while (n < num_of_questions + 1):
            question = self.questions_list[n - 1]
            print("Question number " + str(n) + ":", question.question_str)

            answer = input("Give correct answer as y/n:")
            answer_bool = False
            if answer == "y":
                answer_bool = True

            if answer_bool == question.correct_answer_flag:
                print("Correct!")
                num_correct_user_answers += 1
            else:
                print("Not correct!")

            n += 1

        print("Number of correct answers:", num_correct_user_answers,
              "from", len(self.questions_list), "questions")


quiz = Quiz(10)
quiz.startQuiz()
