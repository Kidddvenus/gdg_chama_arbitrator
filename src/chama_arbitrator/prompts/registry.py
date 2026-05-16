from typing import Optional

from .templates import (
    ARBITRATOR_SYSTEM_PROMPT,
    DOCUMENT_GRADER_PROMPT,
    FINANCIAL_ANALYST_TOOL_PROMPT,
    INPUT_GUARDRAIL_PROMPT,
    OUTPUT_FILTER_PROMPT,
    QUERY_REWRITER_PROMPT,
    QUERY_ROUTER_PROMPT,
    SHENG_NORMALIZER_PROMPT,
    VECTOR_SEARCH_TOOL_PROMPT,
)


class PromptRegistry:
    """
    Version-controlled prompt repository handling dynamic context updates.
    """

    def __init__(self):
        self.prompts = {
            "arbitrator_system": ARBITRATOR_SYSTEM_PROMPT,
            "sheng_normalizer": SHENG_NORMALIZER_PROMPT,
            "query_rewriter": QUERY_REWRITER_PROMPT,
            "query_router": QUERY_ROUTER_PROMPT,
            "vector_search_tool": VECTOR_SEARCH_TOOL_PROMPT,
            "financial_analyst_tool": FINANCIAL_ANALYST_TOOL_PROMPT,
            "input_guardrail": INPUT_GUARDRAIL_PROMPT,
            "document_grader": DOCUMENT_GRADER_PROMPT,
            "output_filter": OUTPUT_FILTER_PROMPT,
        }

    def get_prompt(self, name: str, version: str = "latest") -> Optional[str]:
        """Return the prompt text for a named prompt."""
        return self.prompts.get(name)
