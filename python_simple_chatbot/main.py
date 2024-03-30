import pandas as pd

from services.chat_service import ChatService


class AppMain:

    def __init__(self):
        pass

    # noinspection PyMethodMayBeStatic
    def read_questions_csv(self) -> list[str]:
        questions = pd.read_csv("questions.csv")
        questions.columns = ["question"]
        return questions["question"].tolist()

    # noinspection PyMethodMayBeStatic
    def execute(self):
        questions = self.read_questions_csv()
        ChatService().get_answers_for_questions(questions)


if __name__ == '__main__':
    AppMain().execute()
