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
                'modelArn': 'arn:aws:bedrock:us-west-2::foundation-model/anthropic.claude-3-5-sonnet-20240620-v1:0',
                'retrievalConfiguration': {
                    'vectorSearchConfiguration': {
                        'numberOfResults': 100,
                        'overrideSearchType': 'HYBRID' # Knowledge base의 Vector database가 OpenSearch 일 때만 overrideSearchType을 HYBRID로 세팅 할 수 있습니다.
                        }
                    }
                }
            }
        )


def get_rag_response(question):

    # "Your knowledge base ID"를 생성한 Knowledge base의 ID로 변경해주세요.
    response_text = retrieveAndGenerate(question, "Your knowledge base ID")["output"]["text"]

    return response_text