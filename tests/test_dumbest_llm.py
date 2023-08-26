from llm.dumbest_llm import DumbestLLM


def test_dumbest_llm_responds():
    llm = DumbestLLM()
    input = 'Who are you?'
    expected_output = "I am the dumbest chatbot in the world"
    actual_output = llm.chat(input)
    assert expected_output == actual_output
