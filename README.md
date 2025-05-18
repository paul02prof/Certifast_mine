# Certifast

Certifast is a Django-based certification reference system that allows users to browse, search, and add certifications. The application features a modern UI built with Tailwind CSS and offers a clean way to manage certification information.

## Features

- Modern, responsive UI using Tailwind CSS
- Certification management (add, view certifications)
- Dynamic modals for adding related items (categories, institutions, prerequisites, languages)
- AJAX form submissions for smooth user experience

## Tech Stack

- Python 3.x
- Django 5.x
- Tailwind CSS
- SQLite (default database)

## Installation

### Prerequisites

- Python 3.8 or higher
- Node.js and npm (for Tailwind CSS)

### Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/certifast.git
   cd certifast
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Tailwind CSS dependencies**

   ```bash
   cd theme
   npm install
   ```

5. **Build Tailwind CSS**

   ```bash
   npm run build
   ```

6. **Apply database migrations**

   ```bash
   cd ..  # Return to project root
   python manage.py migrate
   ```

7. **Create a superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**

   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   
   Open your browser and navigate to http://127.0.0.1:8000

## Project Structure

- `certification/` - Main app for managing certifications
- `templates/` - HTML templates
- `static/` - Static assets
- `theme/` - Tailwind CSS configuration
- `templates/components/` - Reusable UI components

## Contribution Guidelines

We welcome contributions to Certifast! Please follow these steps to contribute:

### 1. Set Up Development Environment

- Fork the repository on GitHub
- Clone your fork locally
- Set up the project following the installation instructions above
- Create a new branch for your feature/bugfix:
  ```bash
  git checkout -b feature/your-feature-name
  ```

### 2. Make Your Changes

- Follow the code style of the project
- Write clean, maintainable code
- Include comments where necessary
- Update or add tests as needed

### 3. Test Your Changes

- Run existing tests:
  ```bash
  python manage.py test
  ```
- Manually test your feature in the browser
- Ensure your changes don't break existing functionality

### 4. Create a Pull Request

- Push your changes to your fork
- Create a Pull Request from your branch to the main repository
- Provide a clear description of the changes
- Reference any related issues

### 5. Code Review

- Wait for project maintainers to review your changes
- Be open to feedback and make requested changes
- Respond to comments in a timely manner

### Coding Standards

- Follow PEP 8 style guide for Python code
- Use class-based views
