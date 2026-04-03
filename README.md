# Simple AgenticAI

This project is a simple agentic AI application with a Streamlit-based UI for interacting with LLMs (Large Language Models).

## Features
- Streamlit web interface for user interaction
- Modular code structure
- Requirements file for easy environment setup

## Project Structure
```
UI/
    app_LLM.py   # Main Streamlit app for LLM interaction
    app.py       # Additional app logic
requirements.txt
.gitignore
```

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Setup
1. Clone the repository:
   ```
   git clone https://github.com/AspirantSathish/Simple_AgenticAI.git
   ```
2. Navigate to the project directory:
   ```
   cd Simple_AgenticAI
   ```
3. (Optional) Create and activate a virtual environment:
   ```
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On Unix or MacOS
   source .venv/bin/activate
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running the App
To start the Streamlit app:
```
streamlit run UI/app_LLM.py
```

## License
This project is licensed under the MIT License.
