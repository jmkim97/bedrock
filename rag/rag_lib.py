import os
import boto3

client = boto3.client('bedrock-agent-runtime')

def retrieveAndGenerate(input, kbId):
    return client.retrieve_and_generate(
        input={
            'text': input
        },
        retrieveAndGenerateConfiguration={
            'type': 'KNOWLEDGE_BASE',
            'knowledgeBaseConfiguration': {
                'knowledgeBaseId': kbId,
                'modelArn': 'arn:aws:bedrock:us-west-2::foundation-model/anthropic.claude-v2:1'
                }
            }
        )


def get_rag_response(question): #rag client function

    response_text = retrieveAndGenerate(question, "Knowledge base ID")["output"]["text"]

    return response_text



