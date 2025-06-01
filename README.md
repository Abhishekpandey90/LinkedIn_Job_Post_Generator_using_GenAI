# LinkedIn Job Post Generator using GenAI

This project is a **LinkedIn Job Post Generator** powered by **Generative AI**. It provides a streamlined interface for users to generate customized, professional job descriptions suitable for LinkedIn using the power of modern AI models.

## ✨ Features

- Django-powered web application for job description generation.
- Integration with Google Generative AI APIs.
- Form-based UI to input job details (e.g., role, company, location).
- Output displays dynamically generated professional job descriptions.
- Portable and self-contained with Python virtual environment support.

## 🚀 Technologies Used

- Python 3.11+
- Django Framework
- Google Generative AI (Gemini)
- HTML/CSS Templates
- SQLite (for basic storage)

## 📁 Project Structure

```
- LinkedIn_JobD/
  - LinkedIn_JobD/
    - env/
      - pyvenv.cfg
      - Include/
      - Lib/
        - site-packages/
          - distutils-precedence.pth
          - google_auth_httplib2.py
          - google_generativeai-0.8.4-py3.12-nspkg.pth
          - numpy-2.2.3-cp311-cp311-win_amd64.whl
          - scipy-1.15.2-cp311-cp311-win_amd64.whl
          - threadpoolctl.py
          - typing_extensions.py
          - annotated_types/
            - py.typed
            - test_cases.py
            - __init__.py
            - __pycache__/
              - test_cases.cpython-311.pyc
              - __init__.cpython-311.pyc
          - annotated_types-0.7.0.dist-info/
            - INSTALLER
            - METADATA
            - RECORD
            - WHEEL
            - licenses/
              - LICENSE
          - anyio/
            - from_thread.py
            - lowlevel.py
            - py.typed
            - pytest_plugin.py
            - to_interpreter.py
            - to_process.py
            - to_thread.py
            - __init__.py
            - abc/
              - _eventloop.py
              - _resources.py
              - _sockets.py
              - _streams.py
              - _subprocesses.py
              - _tasks.py
              - _testing.py
              - __init__.py
              - __pycache__/
                - _eventloop.cpython-311.pyc
                - _resources.cpython-311.pyc
                - _sockets.cpython-311.pyc
                - _streams.cpython-31...
```

## ⚙️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/Abhishekpandey90/LinkedIn_Job_Post_Generator_using_GenAI.git
cd LinkedIn_Job_Post_Generator_using_GenAI

# (Optional) Create and activate virtual environment
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the server
python manage.py runserver
```

## 📌 Usage

1. Open `http://127.0.0.1:8000/` in your browser.
2. Fill in job details in the form.
3. Submit to receive a generated job description.
4. Copy and use the output on LinkedIn or other platforms.

## 🤖 AI Integration

This project uses Google Generative AI (Gemini) to generate professional-grade job posts based on user input.

## 🧾 License

This project is licensed under the MIT License.

---

Created by **Abhishek Pandey**. Contributions are welcome! 🚀
