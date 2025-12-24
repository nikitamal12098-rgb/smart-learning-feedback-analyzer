# Smart Learning Feedback Analyzer

## 📌 Description
Smart Learning Feedback Analyzer is an NLP-based system for analyzing student feedback,
essays, and course reviews. The project helps educators understand student sentiment,
identify recurring problems, and gain actionable insights from textual feedback.

One of the key features of the system is **automatic generation of structured reports
for instructors**, which summarize sentiment distribution, key topics, and common issues
highlighted by students.

---

## 🎯 Project Goals
- Analyze textual feedback from students using NLP techniques
- Detect overall and per-topic sentiment
- Identify recurring problem areas and frequently mentioned topics
- Automatically generate clear, instructor-friendly reports
- Support multiple languages (English and Russian)
- Provide results in a format suitable for web deployment

---

## ⚙️ Installation

### Prerequisites
- Python 3.8 or higher
- pip

### Setup
```bash
git clone https://github.com/nikitamal12098-rgb/smart-learning-feedback-analyzer.git
cd smart-learning-feedback-analyzer
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt 
```
## 🚀 Usage  
  
### Basic Usage Example  
```python
from src.main import analyze_feedback

result = analyze_feedback("data/sample.csv")
print(result)
```  
  
### What the System Produces  

- Overall sentiment statistics

- Key recurring topics in student feedback

- Frequently mentioned issues and complaints

- Automatically generated instructor report (Markdown / HTML)  
  
## 🗂 Current Project Structure  
The project currently uses the following structure:  
```graphql .
├── src/                 # Source code (will be extended)
│   └── __init__.py
├── tests/               # Unit tests
│   └── __init__.py
├── data/                # Input and sample data
├── docs/                # Additional documentation
├── scripts/             # Utility scripts
├── .github/
│   └── workflows/       # CI/CD pipelines
├── README.md
├── requirements.txt
└── .gitignore
```  
  
📌 As the project develops, new modules will be added to the src/ directory.
This structure will be updated accordingly at the final stage of the project.
  
# 🧪 Testing  
Run tests locally using:  
```bash 
pytest
```  
Run tests with coverage:  
```bash 
pytest --cov=src tests/
```  
  
## 🔁 CI/CD  
  
- The project uses GitHub Actions for:  

- automated testing and code quality checks

- scheduled feedback analysis

- automatic report generation

- deployment of generated reports  

Details of CI/CD workflows will be documented as they are added.  
  
## 👤 Author  
  
GotLib
