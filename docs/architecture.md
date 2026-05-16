# System Architecture

## Overview
The Chama Arbitrator is a RAG-based system designed for cooperative society dispute resolution.

## Sequence Diagram
1. User submits query (Sheng/Swahili/English).
2. Query Rewriter normalizes the text.
3. Query Router determines if it's financial or legal.
4. Hybrid Retriever fetches relevant bylaw sections or financial logs.
5. Reranker prioritizes the most relevant context.
6. LLM generates a neutral ruling.
7. Security Filters validate the output.
8. Response returned to User.
