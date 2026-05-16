class DocumentGrader:
    """
    Quality check agent verifying if a retrieved rule actually applies to the dispute.
    """
    async def grade(self, query: str, document: str) -> bool:
        # Implementation to verify relevance
        pass
