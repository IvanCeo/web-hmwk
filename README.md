# 🛒 Simple E-commerce Frontend + FastAPI Backend

Проект представляет собой простой шаблон веб-приложения с HTML+CSS фронтендом и backend на **FastAPI**. Он разделён на два микросервиса: **orders-service** и **products-service**.

---

## 📁 Структура проекта

backend/                     ← FastAPI backend
│   └── orders-service/
│   └── products-service/
│       └── services/
│           └── db_query.py
│           └── product_services.py
│       ├── main.py
│       └── product_schema.py
├── images
│   └── ...
├── index.html               ← HTML-шаблоны
└── styles.css               ← Статические файлы CSS

---
