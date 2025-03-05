# CodeFlow: Automating the Flow of Code with LLMs

CodeFlow is a system that automates code generation and refinement through iterative dialogue with large language models. By handling technical implementation details automatically, CodeFlow enables digital humanities scholars and social scientists to focus on their research questions while maintaining high standards of computational rigor.

## Components

- **GPT-4o Handler**: Manages communication with OpenAI's API
- **Iterative Fix Module**: Implements the core refinement loop
- **Code Handler**: Manages code execution and modification
- **Main Orchestrator**: Coordinates the overall workflow

## Usage

1. Create a `purpose` file describing your task
2. Run `python main.py`
3. The system will iteratively generate, test, and refine code until it meets the specified requirements

## Example Applications

- Sentiment analysis
- Literary text analysis
- Historical document processing
- Cultural heritage data analysis

## Requirements

- Python 3.8+
- OpenAI API key
- Additional dependencies in `requirements.txt`

## Citation

If you use CodeFlow in your research, please cite:
Marino, E.B., Bassi, D., Benitez-Baleato, J.M., & Vieira, R. (2025). CodeFlow: Automating the Flow of Code with LLMs. In Proceedings of Digital Humanities 2025, Lisbon, Portugal.