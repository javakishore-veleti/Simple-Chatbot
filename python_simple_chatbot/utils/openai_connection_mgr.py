import openai
import os

from openai import OpenAI

global openai_client
openai_client: OpenAI = None


class OpenAiConnectionManager:

    @staticmethod
    def get_or_initialize_openai() -> OpenAI:
        if "MY_OPENAPI_KEY" not in os.environ:
            raise "Environment Variable MY_OPENAPI_KEY Not Found"

        global openai_client
        if openai_client is not None:
            return openai_client

        openai.api_key = os.environ["MY_OPENAPI_KEY"]

        openai_client = OpenAI(api_key=os.environ["MY_OPENAPI_KEY"])
        return openai_client
