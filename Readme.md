
## Setup

1. Clone the repo and create a virtualenv:
   python -m venv venv
   venv\Scripts\activate  (Windows)

2. Install dependencies:
   pip install -r requirements.txt

3. Create a PostgreSQL database named `healthcare_db`.

4. Create a `.env` file (see `.env.example`) with your DB credentials and a secret key.

5. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

6. Start the server:
   python manage.py runserver

## API Endpoints

### Auth
- POST /api/auth/register/ - Register a new user (name, email, password)
- POST /api/auth/login/ - Login, returns JWT access & refresh tokens

### Patients (auth required)
- POST /api/patients/ - Add patient
- GET /api/patients/ - List patients created by logged-in user
- GET /api/patients/<id>/ - Patient detail
- PUT /api/patients/<id>/ - Update patient
- DELETE /api/patients/<id>/ - Delete patient

### Doctors (auth required)
- POST /api/doctors/ - Add doctor
- GET /api/doctors/ - List all doctors
- GET /api/doctors/<id>/ - Doctor detail
- PUT /api/doctors/<id>/ - Update doctor
- DELETE /api/doctors/<id>/ - Delete doctor

### Mappings (auth required)
- POST /api/mappings/ - Assign doctor to patient
- GET /api/mappings/ - List all mappings
- GET /api/mappings/<id>/ - Mapping detail
- DELETE /api/mappings/<id>/ - Remove mapping

## Auth Usage

After login, include the access token in headers for protected routes:
Authorization: Bearer <access_token>