# Production Chama Arbitrator

An AI-powered arbitration system designed to resolve disputes within Kenyan Chamas (informal cooperative societies).

## Features
- **Multilingual Support**: Handles Sheng, Swahili, and English queries.
- **Bylaw RAG**: Retrieval-Augmented Generation based on uploaded chama bylaws.
- **Financial Analysis**: Automated parsing and calculation of M-Pesa statements and financial ledgers.
- **Neutral Arbitration**: AI agents designed to maintain an unyielding, neutral tone.
- **Privacy First**: Robust content filtering for sensitive financial data.

## Project Structure
Refer to [architecture.md](docs/architecture.md) for a detailed breakdown of the system.

## Setup
1. Clone the repository.
2. Install dependencies: `pip install .`
3. Set up environment variables in `.env`.
4. Run with Docker: `docker-compose up`

## Development
See [CLAUDE.md](CLAUDE.md) for development workflows and coding standards.
