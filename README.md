# 🚀 TaskFlow - Task Management Application

##  Overview
TaskFlow is a **web-based task management application** built with Django that allows users to create, manage, and track their tasks efficiently. The application features user authentication, task creation, deletion, and a clean, responsive interface for an optimal user experience.

---

## ✨ Features

### **User Authentication**
- **User registration**: Create an account with ease.
- **Login/logout functionality**: Secure access to your tasks.
- **Password protection**: Keep your data safe.
- **Secure session management**: Stay logged in securely.

### **Task Management**
- **Create new tasks**: Add tasks with descriptions.
- **Delete existing tasks**: Remove tasks you no longer need.
- **View all tasks**: See all your tasks in a clean, organized interface.
- **Task completion status tracking**: Mark tasks as complete or incomplete.
- **Task creation timestamps**: Track when each task was created.

### **User Interface**
- **Responsive design**: Fully mobile-friendly.
- **Bootstrap-based styling**: Modern and sleek design.
- **Interactive cards for tasks**: Visualize tasks with interactive elements.
- **User-friendly navigation**: Intuitive and easy-to-use interface.
- **Flash messages for user feedback**: Get instant feedback on actions.

---

## 🛠️ Technology Stack

- **Backend**: Django 5.1.6
- **Frontend**:
  - HTML5
  - Bootstrap 5
  - Bootstrap Icons
- **Database**: SQLite (default Django database)
- **Python**: Version 3.13.1

---

## 📂 Project Structure
```
TaskFlow/
├── manage.py
├── templates/
│   ├── base.html
│   └── registration/
│       ├── login.html
│       └── register.html
├── tasks/
│   ├── migrations/
│   │   └── __init__.py
│   ├── templates/
│   │   └── tasks/
│   │       ├── task_list.html
│   │       └── task_form.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
└── Taskflow/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## 🔒 Security Features
- CSRF protection
- User authentication required for task management
- Password hashing
- Form validation
- User-specific task isolation

---

## 🤝 Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

---

## 🌟 Future Enhancements
- Task editing functionality
- Task categories/tags
- Due dates for tasks
- Task priority levels
- Search functionality
- Task sorting options
- Email notifications
- Task sharing between users

---

## 🙏 Acknowledgments
- Django Framework
- Bootstrap
- Bootstrap Icons
- Python Community

## 📞 Contact
```
Njuguna Kelvin
njugunak349@gmail.com
```

---

## 📅 Project Status
- **Under active development**
- Last Updated: February 2025
