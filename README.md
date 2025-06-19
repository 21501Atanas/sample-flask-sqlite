
🌟 Описание

Този проект демонстрира контейнеризация на лесно разширима уеб система с две услуги:

Backend: Flask REST API с вграден SQLite файл за съхранение на задачи и категории.

Frontend: Лек статичен интерфейс на HTML/CSS/JS, сервиращ се от Nginx.

Използвайки Docker Compose, системата е напълно самостоятелна и може да се стартира, мащабира и развива без инсталация на допълнителни зависимости.

🚀 Бързо стартиране

Клонирай репозитория

git clone https://github.com/your-username/sample-flask-sqlite.git
cd sample-flask-sqlite

Инициализирай базата данни

mkdir -p data
sqlite3 data/database.db < /dev/null

Създава се празен SQLite файл, монтиран като том в контейнера.

Стартирай контейнерите

docker-compose up --build -d

--build гарантира използването на последните промени.

-d стартира услугите в заден план.

Достъп

Интерфейс: http://localhost:8080

API:      http://localhost:5000/api/items

🛠 Функционалности

Backend API

GET /api/items: Връща списък със задачи, включително:

id

name

created_at

categories

POST /api/items: Създава нова задача. Примерен payload:

{
  "name": "Напиши документация",
  "categories": ["Work", "Docs"]
}

Frontend UI

Изобразява всички задачи и техните категории.

Форма за добавяне на нова задача с категории, разделени със запетая.

Автоматично обновяване на списъка след добавяне.

📁 Структура на проекта

sample-flask-sqlite/
├── backend/        # Flask API + Dockerfile
├── frontend/       # HTML/CSS/JS клиент + Dockerfile
├── data/      # Том за SQLite (database.db)
├── docker-compose.yml
└── README.md

⚙️ Технологии

Python 3.10, Flask, Flask-SQLAlchemy

SQLite 3

HTML5, CSS3, Vanilla JavaScript

Nginx (alpine)

Docker, Docker Compose

🔄 Разширения и идеи

Превключване на DB: Използвай PostgreSQL/MySQL чрез нов контейнер.

Аутентикация: Добави JWT или OAuth2 за сигурен достъп.

Тестове и CI: Настрой GitHub Actions за автоматични тестове и билдове.

Production: Деплой в Kubernetes или Docker Swarm с Load Balancer.

