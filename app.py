import os
from langchain.llms import CTransformers
from langchain import PromptTemplate, LLMChain
import chainlit as cl

local_llm = "llm/zephyr-7b-alpha.Q4_K_S.gguf"


config = {
    "max_new_token": 1024,
    "repetition_penalty": 1.1,
    "temperature": 0.5,
    "top_k": 50,
    "top_p": 0.9,
    "stream": True,
    "threads": int(os.cpu_count() / 2),
}

llm_init = CTransformers(
    model = local_llm,
    model_type = "mistral",
    lib = "avx2",
    **config
)

print(llm_init)

# query = "What is the meaning of Life?"

# result = llm_init(query)

# print(result)

template = """Question: {question}

Answer: You are helpful teacher that easily explain complex topics in easy way.
"""

@cl.on_chat_start
def main():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=llm_init, verbose=True)
    cl.user_session.set("llm_chain", llm_chain)


@cl.on_message
async def main(message: cl.Message):
    llm_chain = cl.user_session.get("llm_chain")
    res = await llm_chain.acall(message.content, callbacks=[cl.AsyncLangchainCallbackHandler()])
    await cl.Message(content=res["text"]).send()

