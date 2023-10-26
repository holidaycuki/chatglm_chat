import zhipuai
from custom_chatglm import CustomChatGLM

zhipuai.api_key = "0b20d86d815e7efbd97c00dbe133a2dd.d3WKOidakB3rkoqh"

llm = CustomChatGLM()

llm("介绍一下玻璃杯的材质")


