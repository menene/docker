
# FastAPI App en Docker

Servidor simple de FastAPI.

## 📂 Estructura del Proyecto

```
fastapi-app/
├── Dockerfile
└── main.py
```

### 🚀 Requisitos

- Docker instalado en tu sistema.

---

## 🐳 Construcción de la Imagen

Ejecuta el siguiente comando para crear la imagen:
```bash
docker build -t fastapi-app .
```

---

## 🚀 Ejecución del Contenedor

Inicia el contenedor con el siguiente comando:
```bash
docker run -d -p 8000:8000 --name my-fastapi-app fastapi-app
```

### 💡 Explicación:
- `-d`: Ejecuta el contenedor en segundo plano (desacoplado).
- `-p 8000:8000`: Mapea el puerto 8000 del host al contenedor.
- `--name my-fastapi-app`: Asigna un nombre al contenedor.
- `fastapi-app`: Nombre de la imagen.

---

## 🌐 Probar la Aplicación

Para verificar que el servidor está funcionando, abre tu navegador:
```bash
http://localhost:8000/ping
```

**Resultado esperado:**
```
{"message": "pong"}
```

---

## 🛑 Detener el Contenedor
```bash
docker stop my-fastapi-app
```

## ❌ Eliminar el Contenedor
```bash
docker rm my-fastapi-app
```

## 🗑️ Eliminar la Imagen
```bash
docker rmi fastapi-app
```

---

## 📝 Notas

- Asegúrate de que el puerto 8000 no esté en uso antes de ejecutar el contenedor.
- Puedes cambiar el puerto del host modificando el parámetro `-p` en el comando de ejecución.
