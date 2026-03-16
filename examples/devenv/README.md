
# Full-Stack App en Docker

Aplicación simple con un backend en Express, frontend en HTML, base de datos PostgreSQL, Adminer y NGINX como proxy.

## 📂 Estructura del Proyecto

```
full-stack-app/
├── backend/
├── frontend/
├── nginx/
└── docker-compose.yml
```

### 🚀 Requisitos

- Docker y Docker Compose instalados.

---

## 🐳 Construcción y Ejecución

Construir y levantar todos los servicios:
```bash
docker-compose up --build -d
```

Verificar el estado de los servicios:
```bash
docker ps
```

---

## 🌐 Acceso a los Servicios

- **Frontend:** [http://localhost:8180](http://localhost:8180)
- **API (Backend):** [http://localhost:3003/api](http://localhost:3003/api)
- **Adminer:** [http://localhost:8081](http://localhost:8081)

---

## 🛑 Detener todos los servicios
```bash
docker-compose down
```

---

## 📝 Notas

- Asegúrate de que los puertos 80, 8080 y 8081 estén libres.
- Puedes acceder a la base de datos desde Adminer usando:
  - **Servidor:** db
  - **Usuario:** user
  - **Contraseña:** password
  - **Base de datos:** demo_db
