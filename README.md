# Amazon Bedrock Workshop 수정 버전
Amazon Bedrock Workshop에서 사용하는 VectorDatabase를 FAISS에서 Knowledge Base로 변경
- 출처 : https://catalog.workshops.aws/building-with-amazon-bedrock/en-US


# 확인 필요 사항
- AWS IAM Role or Credentail Setting required. (region check!)

- Amazon Bedrock Model access required.


# Install library
- pip3 install -r ./setup/requirements.txt -U


# streamlit 실행 명령어
- streamlit run rag_app.py --server.port 8080
- streamlit run rag_chatbot_app.py --server.port 8080
