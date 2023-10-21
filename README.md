# Zephyr 7B Local LLM using Langchain and Chainlit

This is simple chat interface much like chatGPT. Download [Zephyr-7B-alpha-GGUF](https://huggingface.co/TheBloke/zephyr-7B-alpha-GGUF) from huggingface. We are using langchain, ctransformers, chainlit python package to develop our app.

Just clone the repo, and run

`pip install -r ./requirements.txt`

adjust the path of local llm in `app.py`

`local_llm = "llm/zephyr-7b-alpha.Q4_K_S.gguf"`

you can also adjust or modify template for better result.

and finally run below command to open the chat interface run by the Chainlit

`chainlit run app.py -w`

you should see your app running at localhost:8000

---

Contact at - [linkedin](https://www.linkedin.com/in/sanjay-ojha-34984355/)
