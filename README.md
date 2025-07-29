# CodeFlow: Automating the Flow of Code with LLMs

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![OpenAI](https://img.shields.io/badge/Powered%20by-OpenAI-black.svg)](https://openai.com/)

CodeFlow is a research tool that automates code generation and refinement through iterative dialogue with large language models (LLMs). By handling technical implementation details automatically, CodeFlow enables digital humanities scholars and social scientists to focus on their research questions while maintaining high standards of computational rigor.

## 🎯 Overview

Researchers increasingly rely on computational methods for analyzing large-scale textual data. However, implementing these methods often requires programming skills that may lie outside their core expertise. CodeFlow addresses this challenge by providing:

- **Automated code generation** from natural language research goals
- **Iterative refinement** through automatic debugging cycles  
- **Zero manual intervention** in the debug-fix loop
- **Research-focused interface** for non-programmers

## 🏗️ Architecture

CodeFlow comprises seven integrated components:

```
purpose.txt → main.py → iterative_fix.py ↔ gpt4o_handler.py
                            ↓
                    code_handler.py ↔ script.py ↔ temp_script.py
```

### Components

| Component | Function |
|-----------|----------|
| **purpose.txt** | Research goals in natural language |
| **main.py** | Main orchestrator coordinating workflow |
| **iterative_fix.py** | Core refinement loop (max 10 iterations) |
| **gpt4o_handler.py** | LLM communication and code extraction |
| **code_handler.py** | Safe code execution and error capture |
| **script.py** | Target file that gets iteratively improved |
| **temp_script.py** | Temporary execution sandbox |

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- OpenAI API key

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/erikbranmarino/CodeFlow.git
cd CodeFlow
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set your OpenAI API key:**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

### Usage

1. **Create a purpose file** describing your research task:
```text
Task: Sentiment Analysis
Dataset: amazon_cells_labelled.txt, imdb_labelled.txt, yelp_labelled.txt
Requirements:
1. Fine-tune BERT model for binary classification
2. Target accuracy: > 90%
3. Generate performance metrics
4. Implement cross-validation
```

2. **Run CodeFlow:**
```bash
python main.py
```

3. **Watch the automated process:**
```
Iteration 1...
Code execution in progress...
Code errors: ModuleNotFoundError: No module named 'transformers'
Requesting corrections from GPT-4o...
Code updated and saved at iteration 1.

Iteration 2...
Code is compliant with the purpose and has no errors. Process completed.
```

## 📊 Performance

CodeFlow was evaluated on sentiment analysis benchmarks with automated implementation achieving:

- **Accuracy:** 95%
- **Precision:** 92% 
- **Recall:** 98%
- **F1 Score:** 95%

The system successfully automated:
- ✅ Data preprocessing and cleaning
- ✅ Model architecture configuration
- ✅ Training parameter optimization  
- ✅ Performance evaluation with metrics

## 💡 Use Cases

### Digital Humanities
- Literary text sentiment analysis
- Historical document processing
- Cultural artifact computational analysis
- Corpus linguistic analysis

### Computational Social Sciences
- Social media sentiment tracking
- Survey response analysis
- Political discourse analysis
- Cultural trend identification

## 🔧 Example Purpose Files

### Sentiment Analysis
```text
Task: Sentiment Analysis
Dataset: reviews.csv
Requirements:
1. Use BERT-based model
2. Handle multiple languages
3. Generate confusion matrix
4. Target F1-score: > 0.90
```

### Web Scraping
```text
Task: Web Scraping
Website: https://example.com/articles
Requirements:
1. Extract article titles and content
2. Handle pagination automatically
3. Save to structured CSV format
4. Implement rate limiting
```

## ⚠️ Limitations

- **Creative Problem-Solving:** May not match human creativity for novel research questions
- **LLM Reliability:** Users should validate outputs for research-critical applications
- **Security:** Potential for generating code with vulnerabilities
- **Technical Knowledge:** Basic programming literacy still beneficial
- **Scope:** Some tasks require manual intervention (dependency installation, domain-specific requirements)

## 🔮 Future Directions

- **Multi-LLM Support:** Integration with open-source models
- **Digital Humanities Specialization:** Corpus analysis, stylometry, network analysis
- **Direct Device Integration:** Platform connecting to researchers' local machines
- **Enhanced Error Handling:** More sophisticated automation patterns
- **Security Improvements:** Better vulnerability detection

## 📚 Citation

If you use CodeFlow in your research, please cite:

```bibtex
@article{marino2025codeflow,
  title={CodeFlow: Automating the Flow of Code with LLMs},
  author={Marino, Erik Bran and Bassi, Davide and Benitez-Baleato, Jesus M and Vieira, Renata},
  journal={Digital Humanities Conference},
  year={2025},
  location={Lisbon, Portugal}
}
```

## 👥 Authors

- **Erik Bran Marino** - University of Évora, HYBRIDS Project
- **Davide Bassi** - University of Santiago de Compostela  
- **Jesus M Benitez-Baleato** - University of Santiago de Compostela
- **Renata Vieira** - University of Évora

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request.

## 📞 Contact

- **Erik Bran Marino:** erik.marino@uevora.pt
- **Project:** [HYBRIDS Marie Skłodowska-Curie Actions](https://hybridsproject.eu/)

---

**CodeFlow** - *Democratizing computational research for digital humanities scholars worldwide.*