class RAGPipeline:
    """
    Main orchestration layer linking retrieved documents to LLM contexts.
    """
    def __init__(self, retriever, reranker, llm):
        self.retriever = retriever
        self.reranker = reranker
        self.llm = llm

    async def run(self, query: str):
        # 1. Rewrite query
        # 2. Route query
        # 3. Retrieve & Rerank
        # 4. Generate response
        pass
