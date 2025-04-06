def calculate_bmi(height: float, weight: float) -> float:
    height_m = height / 100
    return weight / (height_m ** 2)

def calculate_bmr(gender: str, weight: float, height: float, age: int) -> float:
    if gender == 'male':
        return 66.5 + (13.75 * weight) + (5.003 * height) - (6.75 * age)
    else:
        return 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)

def calculate_tdee(bmr: float, activity_level: str) -> float:
    multipliers = {
        'S': 1.2, 'LA': 1.375,
        'MA': 1.55, 'VA': 1.725, 'SA': 1.9
    }
    return bmr * multipliers[activity_level]

def calculate_macronutrients(tdee: float, meal_plan_type: str, health_condition: str = None):
    if meal_plan_type == 'Healthy':
        protein = (tdee * 0.2) / 4
        carbs = (tdee * 0.55) / 4
    else:
        if health_condition == 'Controlled':
            protein = (tdee * 0.25) / 4
            carbs = (tdee * 0.45) / 4
        else:
            protein = (tdee * 0.3) / 4
            carbs = (tdee * 0.4) / 4
    
    fiber = (tdee * 14) / 1000
    fat=(tdee*0.25)/9
    return protein, carbs, fiber,fat