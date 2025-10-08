# TODO List

## Description
TODO List is a simple web-based application that allows users to manage their tasks effectively. Users can create tasks with associated tags, track their progress, and maintain a well-organized to-do list.

## Installation
### Requirements
- Python 3.8+
- Django
- SQLite (or PostgreSQL for production)
- pip

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/todo-list.git
   cd todo-list
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   Fill in the `.env` file with necessary configurations.

5. Run database migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
- Visit `http://127.0.0.1:8000/` in your browser.
- Manage your tasks and tags from the sidebar.
-  Add, update, and delete tasks and tags as needed.

## Contributing
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them.
4. Push the changes to your fork and create a pull request.

## Authors and Acknowledgment
Developed by Kateryna

## Project Status
Active - ongoing development and improvements.
