import os
from langchain.memory import ConversationBufferWindowMemory
from langchain.retrievers import AmazonKnowledgeBasesRetriever
from langchain.llms.bedrock import Bedrock
from langchain.chains import ConversationalRetrievalChain

retriever = AmazonKnowledgeBasesRetriever(
    knowledge_base_id="Knowledge base ID",
    retrieval_config={"vectorSearchConfiguration": {"numberOfResults": 10}}, #Number of documents to search on Knowledge base
)

def get_llm():
        
    model_kwargs_claude =  { 
        "max_tokens_to_sample": 3000, 
        "temperature": 0, 
        "top_k": 10
    }
    
    llm = Bedrock(
        model_id="anthropic.claude-v2:1", #set the foundation model
        model_kwargs=model_kwargs_claude) #configure the properties for Claude
    
    return llm


def get_memory(): #create memory for this chat session
    
    memory = ConversationBufferWindowMemory(memory_key="chat_history", return_messages=True) #Maintains a history of previous messages
    
    return memory


def get_rag_chat_response(input_text, memory): #chat client function
    
    llm = get_llm()
    
    conversation_with_retrieval = ConversationalRetrievalChain.from_llm(llm, retriever, memory=memory, verbose=True)
    
    chat_response = conversation_with_retrieval({"question": input_text}) #pass the user message, history, and knowledge to the model
    
    return chat_response['answer']


