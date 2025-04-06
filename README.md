```markdown
# Diet Plan API

![License](https://img.shields.io/github/license/niharika797/MITIHAR)
![Python](https://img.shields.io/badge/Python-100%25-blue)

## 🌟 Overview

The **Diet Plan API** is a smart, web-based application built to generate personalized diet plans tailored to individual user needs. It combines the power of modern web technologies with data science to help users achieve their nutrition goals effectively.

Built with **FastAPI** and **MongoDB**, it ensures performance, scalability, and flexibility.

---

## 🚀 Features

- 🔐 **JWT Authentication** – Secure login and registration.
- 🥗 **Smart Diet Plan Generator** – Personalized plans based on preferences and activity.
- 🍽 **Meal Planning Engine** – Meal selection based on nutritional targets.
- 📊 **Progress Tracker** – Logs weight and user progress.
- ⚡ **Fast & Async** – Powered by FastAPI, Pydantic, and asynchronous MongoDB queries.

---

## 🛠 Installation

### Prerequisites
- Python 3.8+
- MongoDB

### Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/niharika797/MITIHAR.git
cd MITIHAR

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\\Scripts\\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add environment variables
touch .env
# Add the following:
# SECRET_KEY=your-secret-key
# MONGO_URI=mongodb://localhost:27017
# DATABASE_NAME=diet_plan

# 5. Run the server
uvicorn app.main:app --reload
```

---

## 🔌 API Endpoints

### Auth
- `POST /api/v1/auth/register` – Create a new user
- `POST /api/v1/auth/login` – Authenticate user

### User
- `GET /api/v1/users/me` – Fetch logged-in user data

### Diet Plans
- `POST /api/v1/diet-plans` – Generate a diet plan
- `GET /api/v1/diet-plans/{id}` – Fetch diet plan by ID

### Meals
- `POST /api/v1/meal-plan` – Generate meal plan

### Progress
- `POST /api/v1/progress` – Log weight/progress
- `GET /api/v1/progress` – Retrieve user progress

---

## 📬 Sample Requests

```bash
# Register a new user
curl -X POST "http://localhost:8000/api/v1/auth/register" \\
     -H "Content-Type: application/json" \\
     -d '{"email": "user@example.com", "password": "securepass"}'

# Create diet plan
curl -X POST "http://localhost:8000/api/v1/diet-plans" \\
     -H "Authorization: Bearer <your_token>" \\
     -d '{"preferences": {...}, "activity_level": "moderate"}'
```

---

## 🤝 Contributing

We love contributions! 🎉

1. Fork the project  
2. Create your feature branch (`git checkout -b feat/AmazingFeature`)  
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)  
4. Push to the branch (`git push origin feat/AmazingFeature`)  
5. Open a Pull Request  

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [MongoDB](https://www.mongodb.com/)
- [Pydantic](https://docs.pydantic.dev/)

---

> Built with 💚 for healthier lives.
```
