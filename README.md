# LLM Template


## Installation

We assume you have python (at least 3.10) and pip are installed on your machine.
All commands should be executed from the root of the repository.

Next, ensure that `poetry` is installed, see [documentation](https://python-poetry.org/docs/)

```bash
pip install poetry
```

You can install the dependencies via:

```bash
poetry install
```

You can execute a command in the project's environment via:

```bash
poetry run <cmd> 
```

For example, you can check your installation worked via:

```bash
poetry run pytest
```

Or run a development server via:

```bash
poetry run streamlit run dashboards/simple_chat.py --server.port=8501
```

## Dependencies

### Pytest

Pytest is a test framework, see [pytest docs](https://docs.pytest.org/)

### Pandas

This is for handling dataframes/tables in memory: loading csvs, data wrangling,
etc.

Here is a [cheatsheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
Google/chatbots can probably accomplish the same. 

### Streamlit

This is building UIs, see [streamlit docs](https://docs.streamlit.io/)

You can start a development server via:

```bash
poetry run streamlit run <path_to_dashboard>
```

### OpenAI

This is an easy way to get started with llms, see (documentation)[https://platform.openai.com/docs/api-reference]

Note this repository assumes you have an OpenAI API key set as an environment variable.

For example, if you're on a Mac, the following may work:

```bash
echo export OPENAI_API_KEY=<key> >> ~/.zprofile
```

or if you're using bash:

```bash
echo export OPENAI_API_KEY=<key> >> ~/.profile
```

see [here](https://platform.openai.com/account/api-keys) for generating API keys.

### LangChain

LangChain is a llm app framework. See their (documentation)[https://python.langchain.com/docs]

LangChain's advantages are:

1. Making llm's "interchangeable". E.g. Use Llama2 instead of gpt-3.5-turbo without
having to change your prompt engineering code.
1. Out-of-the-box agents/prompts/etc. as well as tools (e.g. google search etc.)


## Chroma

Chroma is an easy, open source, in-memory vector database. This allows for easy in-memory
semantic search, see
[documenation](https://python.langchain.com/docs/integrations/vectorstores/chroma)
for how to use it with langchain.


### General Notes

Put your code that will be used throughout different prototypes inside of 
the llm folder. Make sure to always use "absolute imports":

Good:
```python
from llm.dumbest_llm import DumbestLLM
```

Bad:
```python
from .dumbest_llm import DumbestLLM
```

Transitioning from javascript to python modules is notoriously fraught. Do it
the python way, don't try to force javascript practices.


