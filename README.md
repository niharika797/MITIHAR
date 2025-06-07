
# Diet Plan API

![Python](https://img.shields.io/badge/Python-100%25-blue)

## 🌟 Overview

The AI-based diet recommender system **MITIHAR** is a smart application built to generate personalized diet plans tailored to individual user needs according to their dietry preferences and health needs.


---

## 🚀 Features

- 🥗 **Smart Diet Plan Generator** – Personalized plans based on preferences and activity levels
- 🍽 **Meal Planning Engine** – Meal selection based on nutritional targets.
- 📊 **Progress Tracker** – Synced with GoogleFit API to track your daily progess.
- 🥗 **Dynamic adjustment** - The app adjusts the extra calories in the diet plan just on uploading a picture.
- 🍽 **Meal Authentication** - Prompts user to upload picture of food consumed for better authentication.
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
source venv/bin/activate        # On Windows: venv\Scripts\activate

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

### Register a new user
```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
     -H "Content-Type: application/json" \
     -d '{"email": "user@example.com", "password": "securepass"}'
```

### Create diet plan
```bash
curl -X POST "http://localhost:8000/api/v1/diet-plans" \
     -H "Authorization: Bearer <your_token>" \
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

Licensed under the MIT License.

---

## 🙏 Acknowledgements

- FastAPI  
- MongoDB  
- Pydantic  

Built with 💚 for healthier lives.
