# Student Management System

A simple Django application for managing student records, calculating grades, and displaying student details.

## Features

- **Student Registration**: Register new students with their details.
- **Grade Calculation**: Calculate grades based on student records from a CSV file.
- **User Authentication**: Users can register, log in, and log out.
- **Navigation Links**: Easy navigation for logging in, registering, and submitting student details.

## Technologies Used

- **Django**: Web framework for building the application.
- **Python**: Programming language used.
- **Pandas**: Library for data manipulation and analysis (used for handling CSV files).
- **Chardet**: Library for detecting file encoding (used for reading CSV files).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
Create a virtual environment:

python -m venv myenv
Activate the virtual environment:

On Windows:
.\myenv\Scripts\activate
On macOS/Linux:
source myenv/bin/activate
Install the required packages:


pip install -r requirements.txt
Run database migrations:

python manage.py migrate
Start the development server:

python manage.py runserver

Open your web browser and navigate to:
http://127.0.0.1:8000/
