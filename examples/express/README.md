
# Express App en Docker

Servidor simple de Express.

## 📂 Estructura del Proyecto

```
express-app/
├── Dockerfile
└── app.js
```

### 🚀 Requisitos

- Docker instalado en tu sistema.

---

## 🐳 Construcción de la Imagen

Ejecuta el siguiente comando para crear la imagen:
```bash
docker build -t express-app .
```

---

## 🚀 Ejecución del Contenedor

Inicia el contenedor con el siguiente comando:
```bash
docker run -d -p 3000:3000 --name my-express-app express-app
```

### 💡 Explicación:
- `-d`: Ejecuta el contenedor en segundo plano (desacoplado).
- `-p 3000:3000`: Mapea el puerto 3000 del host al contenedor.
- `--name my-express-app`: Asigna un nombre al contenedor.
- `express-app`: Nombre de la imagen.

---

## 🌐 Probar la Aplicación

Para verificar que el servidor está funcionando, abre tu navegador:
```bash
http://localhost:3000/ping
```

**Resultado esperado:**
```
pong
```

---

## 🛑 Detener el Contenedor
```bash
docker stop my-express-app
```

## ❌ Eliminar el Contenedor
```bash
docker rm my-express-app
```

## 🗑️ Eliminar la Imagen
```bash
docker rmi express-app
```

---

## 📝 Notas

- Asegúrate de que el puerto 3000 no esté en uso antes de ejecutar el contenedor.
- Puedes cambiar el puerto del host modificando el parámetro `-p` en el comando de ejecución.
