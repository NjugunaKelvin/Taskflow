# TaskFlow - Task Management Application

## Overview
TaskFlow is a web-based task management application built with Django that allows users to create, manage, and track their tasks. The application features user authentication, task creation, deletion, and a clean, responsive interface.

## Features
- User Authentication
  - User registration
  - Login/logout functionality
  - Password protection
  - Secure session management

- Task Management
  - Create new tasks
  - Delete existing tasks
  - View all tasks in a clean interface
  - Task completion status tracking
  - Task creation timestamps

- User Interface
  - Responsive design (mobile-friendly)
  - Bootstrap-based styling
  - Interactive cards for tasks
  - User-friendly navigation
  - Flash messages for user feedback

## Technology Stack
- **Backend**: Django 5.1.6
- **Frontend**: 
  - HTML5
  - Bootstrap 5
  - Bootstrap Icons
- **Database**: SQLite (default Django database)
- **Python**: Version 3.13.1

## Project Structure
Copy
Insert

TaskFlow/ ├── manage.py ├── templates/ │ ├── base.html │ └── registration/ │ ├── login.html │ └── register.html ├── tasks/ │ ├── migrations/ │ ├── templates/ │ │ └── tasks/ │ │ ├── task_list.html │ │ └── task_form.html │ ├── init.py │ ├── admin.py │ ├── apps.py │ ├── models.py │ ├── urls.py │ └── views.py └── Taskflow/ ├── init.py ├── settings.py ├── urls.py └── wsgi.py


## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd TaskFlow
Copy
Insert

Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Copy
Insert

Install required packages:
pip install django
Copy
Insert

Apply migrations:
python manage.py makemigrations
python manage.py migrate
Copy
Insert

Create a superuser (admin):
python manage.py createsuperuser
Copy
Insert

Run the development server:
python manage.py runserver
Copy
Insert

Access the application at http://127.0.0.1:8000
Usage
User Registration
Navigate to the registration page
Create a new account with username and password
Automatic login after successful registration
Task Management
Login to your account
View your task dashboard
Create new tasks using the "Add New Task" button
Delete tasks using the delete button on each task card
View task details including creation time
Authentication
Login: /login/
Register: /register/
Logout: /logout/
Models
Task Model
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
Copy
Insert

Security Features
CSRF protection
User authentication required for task management
Password hashing
Form validation
User-specific task isolation
Contributing
Fork the repository
Create a new branch
Make your changes
Submit a pull request
Future Enhancements
Task editing functionality
Task categories/tags
Due dates for tasks
Task priority levels
Search functionality
Task sorting options
Email notifications
Task sharing between users
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Django Framework
Bootstrap
Bootstrap Icons
Python Community
Contact
[Your Name/Contact Information]

Project Status
Under active development

Last Updated: February 2025
