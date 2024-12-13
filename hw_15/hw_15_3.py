def get_user_data():
    print("Заполните информацию для резюме:")
    name = input("Имя: ")
    age = input("Возраст: ")
    profession = input("Профессия: ")
    experience = input("Опыт работы: ")
    skills = input("Навыки (через запятую): ")
    return {
        "Имя": name,
        "Возраст": age,
        "Профессия": profession,
        "Опыт работы": experience,
        "Навыки": skills,
    }

def display_resume(data):
    print("\nВаше резюме:")
    print(f"Имя: {data['Имя']}")
    print(f"Возраст: {data['Возраст']}")
    print(f"Профессия: {data['Профессия']}")
    print(f"Опыт работы: {data['Опыт работы']}")
    print(f"Навыки: {data['Навыки']}")

def main():
    user_data = get_user_data()
    display_resume(user_data)

if __name__ == "__main__":
    main()
