from langchain.memory import ConversationBufferWindowMemory
from langchain_community.retrievers import AmazonKnowledgeBasesRetriever
from langchain.chains import ConversationalRetrievalChain
from langchain_aws.chat_models.bedrock import ChatBedrock

retriever = AmazonKnowledgeBasesRetriever(
  knowledge_base_id="Your knowledge base ID", # "Your knowledge base ID"를 생성한 Knowledge base의 ID로 변경해주세요.
  retrieval_config={
    "vectorSearchConfiguration": {
      "numberOfResults": 100,
      "overrideSearchType": "HYBRID" # Knowledge base의 Vector database가 OpenSearch 일 때만 overrideSearchType을 HYBRID로 세팅 할 수 있습니다.
      }
    }
  )

def get_llm():

    llm = ChatBedrock(model_id="anthropic.claude-3-5-sonnet-20240620-v1:0", model_kwargs={"max_tokens": 3000, "temperature": 0.0, "top_k": 35, "top_p": 1})

    return llm


def get_memory(): # Create memory for this chat session

    memory = ConversationBufferWindowMemory(memory_key="chat_history", return_messages=True) # Maintains a history of previous messages

    return memory


def get_rag_chat_response(input_text, memory): #chat client function

    llm = get_llm()

    conversation_with_retrieval = ConversationalRetrievalChain.from_llm(llm, retriever, memory=memory, verbose=True)

    chat_response = conversation_with_retrieval({"question": input_text}) # Pass the user message, history, and knowledge to the model

    return chat_response['answer']
