# Back-end-Development-Capstone

Aplicación Django Capstone - Python Rockers Band Website

## Descripción del Proyecto

Aplicación web Django completa que presenta una banda musical con páginas de Inicio, Canciones, Fotos y Conciertos. Incluye panel de administración y diálogos modales.

## Environment Setup

- **Python version**: 3.9.x
- **Virtual environment**: `backend-capstone-venv`
- **Framework**: Django 6.0.x
- **Database**: SQLite

### Setup Instructions

```bash
# Clone the repository
git clone https://github.com/cristhus100/Back-end-Development-Capstone.git
cd Back-end-Development-Capstone

# Create virtual environment
python3 -m venv backend-capstone-venv
source backend-capstone-venv/bin/activate

# Create from template
bin/setup.sh

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver 0.0.0.0:8080
```

### Pages

- `/` - Home page
- `/songs/` - Songs list with lyrics modals
- `/photos/` - Band photos
- `/concerts/` - Upcoming concerts
- `/admin/` - Django admin interface
