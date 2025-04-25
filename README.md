
# Neonmart Django Project

Welcome to the **Neonmart** Django project! This project is built using Django, with the modern **Jazzmin** theme enhancing the admin interface for a sleek, user-friendly experience. Neonmart aims to provide a seamless platform, and this repository contains everything you need to get it running.

---

## Table of Contents

- [Installation](#installation)
- [Project Setup](#project-setup)
- [Database Setup](#database-setup)
- [Admin Customization](#admin-customization)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/neonmart.git
cd neonmart
```

### 2. Set Up a Virtual Environment

We recommend creating a virtual environment to manage dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows**:

  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

### 3. Install the Required Dependencies

Install all the necessary dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## Project Setup

### 1. Database Setup

This project uses **Neon PostgreSQL** as the database. To set up the database, add the following connection string to your `.env` file:

```env
DATABASE_URL=postgresql://neondb_owner:npg_HD3fp5lkEKXM@ep-withered-fog-a1oe2q5a-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require
```

### 2. Apply Database Migrations

Run the following command to apply database migrations:

```bash
python manage.py migrate
```

### 3. Create a Superuser

To access the Django admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set the username, email, and password for the superuser.

---

## Admin Customization

The Django admin interface has been enhanced using the **Jazzmin** theme. You can further customize the admin interface in the `settings.py` file by modifying the `JAZZMIN_SETTINGS` dictionary.

Example customization:

```python
JAZZMIN_SETTINGS = {
    "site_title": "Neonmart Admin",
    "site_header": "Neonmart Admin",
    "site_brand": "Neonmart",
    "welcome_sign": "Welcome to Neonmart Admin",
    "copyright": "Neonmart © 2025",
    "theme": "default",
    "show_sidebar": True,
    "navbar": "navbar-dark navbar-primary",
    "navigation_expanded": True,
}
```

---

## Usage

### Running the Development Server

To start the development server and view the project in your browser:

```bash
python manage.py runserver
```

You can access the Django admin panel at:

```
http://127.0.0.1:8000/admin/
```

Log in using the superuser credentials you created earlier.

---

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature/your-feature-name`.
3. Commit your changes: `git commit -am 'Add some feature'`.
4. Push to your branch: `git push origin feature/your-feature-name`.
5. Open a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

