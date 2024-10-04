import uuid
import boto3

client = boto3.client('bedrock-agent-runtime')

session_id=str(uuid.uuid1())

def invokeAgent(input, agent_id, agent_alias_id):
    return client.invoke_agent(
    inputText=input,
    agentId=agent_id,
    agentAliasId=agent_alias_id,
    sessionId=session_id,
    enableTrace=False
)


def get_agent_response(question):

    # "Your Agent ID"를 생성한 Agent의 ID로 변경하고, "Your Agent Alias ID"를 생성한 Agent의 Alias ID로 변경해주세요.
    response_text = invokeAgent(question, "Your Agent ID", "Your Agent Alias ID")

    event_stream = response_text['completion']
    for event in event_stream:
        if 'chunk' in event:
            data = event['chunk']['bytes'].decode("utf-8")

            return data