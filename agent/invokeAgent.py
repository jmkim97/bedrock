import uuid
import boto3

client = boto3.client('bedrock-agent-runtime')


def invokeAgent(input, agent_id, agent_alias_id, session_id):
    return client.invoke_agent(
    inputText=input,
    agentId=agent_id,
    agentAliasId=agent_alias_id,
    sessionId=session_id,
    enableTrace=True
)


def get_agent_response(input_values):

    question = input_values['question']
    session_id = input_values['sessionId']

    response_text = invokeAgent(question, "Your Agent ID", "Your Agent Alias ID", session_id) # "Your Agent ID", "Your Agent Alias ID"를 생성한 Agent의 ID와 Alias ID로 변경해주세요.
    
    event_stream = response_text['completion']
    for event in event_stream:        
        if 'chunk' in event:
            data = event['chunk']['bytes'].decode("utf-8")
            return data
