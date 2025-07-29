# CodeFlow Setup Guide

This guide will help you set up CodeFlow on your local machine for digital humanities and computational social science research.

## Prerequisites

### 1. Python Environment
- **Python 3.8 or higher** is required
- Check your version: `python --version`
- If needed, download from [python.org](https://www.python.org/downloads/)

### 2. OpenAI API Access
- Create an account at [OpenAI](https://platform.openai.com/)
- Generate an API key from your dashboard
- Ensure you have sufficient credits for GPT-4o usage

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/erikbranmarino/CodeFlow.git
cd CodeFlow
```

### 2. Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv codeflow_env

# Activate it
# On Windows:
codeflow_env\Scripts\activate
# On macOS/Linux:
source codeflow_env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure OpenAI API Key

#### Option A: Environment Variable (Recommended)
```bash
# On Windows:
set OPENAI_API_KEY=your-api-key-here

# On macOS/Linux:
export OPENAI_API_KEY="your-api-key-here"
```

#### Option B: Modify gpt4o_handler.py
Edit `gpt4o_handler.py` and replace:
```python
openai.api_key = os.getenv("OPENAI_API_KEY")
```
with:
```python
openai.api_key = "your-api-key-here"
```

⚠️ **Security Warning:** Never commit API keys to version control!

## Verification

### Test Installation
```bash
python -c "import openai; print('OpenAI library installed correctly')"
```

### Test API Connection
Create a test file `test_api.py`:
```python
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use cheaper model for testing
        messages=[{"role": "user", "content": "Hello!"}],
        max_tokens=10
    )
    print("API connection successful!")
except Exception as e:
    print(f"API connection failed: {e}")
```

Run: `python test_api.py`

## First Run

### 1. Create Your Purpose File
Create a file named `purpose` in the CodeFlow directory:
```text
Task: Simple Text Processing
Requirements:
1. Read a text file
2. Count words and sentences
3. Print basic statistics

This is a test task to verify CodeFlow is working.
```

### 2. Create Initial Script
Create a simple `script.py`:
```python
# This is a placeholder script that will be improved by CodeFlow
print("Hello, CodeFlow!")
```

### 3. Run CodeFlow
```bash
python main.py
```

You should see:
```
Iteration 1...
Code execution in progress...
Code output:
Hello, CodeFlow!
Code is not compliant with the purpose or has generated errors. Requesting corrections.
...
```

## Troubleshooting

### Common Issues

#### 1. Import Errors
```bash
ModuleNotFoundError: No module named 'openai'
```
**Solution:** Ensure virtual environment is activated and run `pip install -r requirements.txt`

#### 2. API Key Errors
```bash
Authentication Error: No API key provided
```
**Solution:** Check your API key is correctly set in environment variables

#### 3. Rate Limit Errors
```bash
Rate limit exceeded
```
**Solution:** 
- Check your OpenAI usage limits
- Add delays between API calls if needed
- Consider upgrading your OpenAI plan

#### 4. Execution Permissions
```bash
Permission denied when running script
```
**Solution:** Ensure Python has permission to create/modify files in the directory

### Getting Help

1. **Check the logs:** CodeFlow prints detailed information about each iteration
2. **Examine temp_script.py:** This shows what code is being executed
3. **Review error messages:** GPT-4o provides specific error descriptions
4. **Validate your purpose file:** Ensure requirements are clear and achievable

## Advanced Configuration

### Using Different Models
Modify `gpt4o_handler.py` to use different OpenAI models:
```python
response = openai.ChatCompletion.create(
    model="gpt-4",  # or "gpt-3.5-turbo" for lower cost
    messages=[...],
    max_tokens=1500
)
```

### Adjusting Iteration Limits
Modify `iterative_fix.py`:
```python
for i in range(20):  # Increase from 10 to 20 iterations
```

### Custom Execution Environment
Modify `code_handler.py` to use specific Python interpreters:
```python
result = subprocess.run(
    ["/path/to/specific/python", "temp_script.py"],
    capture_output=True,
    text=True
)
```

## Next Steps

1. **Review Examples:** Check the `examples/` directory for sample purpose files
2. **Start Small:** Begin with simple tasks to understand the workflow
3. **Iterate:** Refine your purpose descriptions based on results
4. **Scale Up:** Gradually increase complexity as you become comfortable

Happy researching with CodeFlow! 🚀