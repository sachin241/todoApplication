# Django Taskboard

A server-rendered Django todo application with PostgreSQL, filtering, FullCalendar, and Excel import/export.

## Setup (SQLite, ready to run)

1. Copy `.env.example` to `.env` and set a secure `SECRET_KEY`. The default `DATABASE_ENGINE=sqlite` stores local data in `db.sqlite3`; no database server is needed.

2. Create and activate a virtual environment, then install dependencies:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

3. Apply migrations and run the server:

   ```powershell
   python manage.py migrate
   python manage.py runserver
   ```

Open `http://127.0.0.1:8000/`. Use `python manage.py createsuperuser` to access `/admin/`.

## Switching to PostgreSQL later

1. Create a PostgreSQL database and user, for example:

   ```sql
   CREATE USER todo_user WITH PASSWORD 'your-postgresql-password';
   CREATE DATABASE todo_db OWNER todo_user;
   ```

2. Set `DATABASE_ENGINE=postgresql` plus the `DB_*` values in `.env`, then run `python manage.py migrate` again.

## Deploy to Render with Neon

The root `render.yaml` installs dependencies, collects static assets, applies migrations, and runs Gunicorn. Create a Neon database, copy its `DATABASE_URL` connection string (with `sslmode=require`), then set it as the `DATABASE_URL` secret when creating the Render Blueprint. See the deployment steps provided with this project for the full sequence.

The production service uses PostgreSQL whenever `DATABASE_URL` is set. Do not commit `.env`, `db.sqlite3`, or a Neon connection string.

## Excel format

Exports use the required column order: `Title`, `Description`, `Status`, `Priority`, `Due Date`, `Created At`. Imports expect the same headers. Status must be `Pending`, `In Progress`, or `Completed`; priority must be `Low`, `Medium`, or `High`. Due dates accept Excel dates, `YYYY-MM-DD`, `DD/MM/YYYY`, or `MM/DD/YYYY`.
