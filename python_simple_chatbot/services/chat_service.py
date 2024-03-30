from utils.openai_connection_mgr import OpenAiConnectionManager
import openai


class ChatService:

    def __init__(self):
        pass

    # noinspection PyMethodMayBeStatic
    def ask_openai_chatbot(self, question: str):
        openai_client = OpenAiConnectionManager.get_or_initialize_openai()

        chat_response = openai_client.chat.completions.create(
            messages=[{
                "role": "user",
                "content": question
            }],
            model="gpt-3.5-turbo"
        )

        chat_response_str = chat_response.choices[0].message.content.strip()
        return chat_response_str

    # noinspection PyMethodMayBeStatic
    def get_answers_for_questions(self, questions: list[str]):

        for a_question in questions:
            chat_response_str = self.ask_openai_chatbot(a_question)
            print(f"For Question [{a_question}] Chat Response is [{chat_response_str}]")

