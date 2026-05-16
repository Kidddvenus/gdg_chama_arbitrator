# AGENTS.md - AI Agent Architecture

This document outlines the personas and responsibilities of the AI agents within the Chama Arbitrator system.

## Agent Personas

### 1. Document Grader
- **Goal**: Verify relevance of retrieved bylaw sections.
- **Behavior**: Strict, binary evaluation (relevant/irrelevant).
- **Tone**: Objective.

### 2. Query Decomposer
- **Goal**: Break down complex member complaints into atomic sub-tasks.
- **Behavior**: Analytical, identifies financial vs. legal aspects.

### 3. Adaptive Router
- **Goal**: Manage execution flow based on query complexity.
- **Behavior**: Dynamic thresholding for confidence scores.

### 4. Financial Analyst
- **Goal**: Execute calculations over CSV data.
- **Behavior**: Precision-oriented, uses code execution tools.

## Tools
- **Vector Search**: Semantic lookup in bylaws.
- **Web Search**: Fallback for external legal frameworks (Co-operative Societies Act).
- **Financial Tool**: Python interpreter for data analysis.
