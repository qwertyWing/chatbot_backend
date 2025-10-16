from langchain.memory import ConversationBufferMemory

def make_memory():
    return ConversationBufferMemory(return_messages=True)
