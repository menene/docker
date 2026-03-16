# Docker

Material de introducción a Docker — presentación interactiva y ejemplos funcionales listos para correr.

## Contenido

```
.
├── presentation.html   # Presentación reveal.js
├── index.html          # Landing page
└── examples/
    ├── js/             # Node.js HTTP nativo
    ├── express/        # Node.js + Express
    ├── fastapi/        # Python + FastAPI
    ├── nginx/          # NGINX sitio estático
    ├── multicontainer/ # React + FastAPI + SQLite
    ├── devenv/         # Express + PostgreSQL + Adminer + NGINX
    ├── docuwiki/       # DokuWiki
    ├── libreoffice/    # LibreOffice (browser)
    ├── doom/           # DOOM
    ├── jellyfin/       # Jellyfin media server
    ├── kali-linux/     # Kali Linux (KasmVNC)
    └── bitwarden/      # Vaultwarden (Bitwarden self-hosted)
```

## Ver la presentación

Abrí `index.html` en el browser o servila con cualquier servidor estático:

```bash
npx serve .
```

## Correr los ejemplos

Cada carpeta dentro de `examples/` es independiente. La mayoría solo necesita:

```bash
cd examples/<nombre>
docker compose up
```

Los que tienen `Dockerfile` requieren build:

```bash
docker compose up --build
```

### Requisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Mac / Windows)
- Docker Engine + Docker Compose (Linux)

---

## Ejemplos

### `js`
Servidor Node.js puro sin dependencias externas. Demuestra puertos y bind mounts.
```bash
cd examples/js
docker build -t my-app .
docker run -p 3000:3000 my-app
# con volumen:
docker run -p 3000:3000 -v .:/app my-app
```

### `express`
Servidor Express básico. Responde `pong` en `/ping`.
```bash
cd examples/express
docker build -t express-app .
docker run -p 3000:3000 express-app
```

### `fastapi`
API REST con FastAPI. Responde `{"message":"pong"}` en `/ping`.
```bash
cd examples/fastapi
docker build -t fastapi-app .
docker run -p 8000:8000 fastapi-app
```

### `nginx`
Sitio estático servido por NGINX. El contenido de `./site` se monta como volumen.
```bash
cd examples/nginx
docker compose up
# → http://localhost:8080
```

### `multicontainer`
Tres servicios orquestados con Docker Compose: un seeder SQLite (one-shot), un backend FastAPI y un frontend React que muestra equipos de LaLiga.
```bash
cd examples/multicontainer
docker compose up --build
# → http://localhost:5173
```

### `devenv`
Entorno de desarrollo completo: backend Express, frontend HTML, PostgreSQL, Adminer y NGINX como proxy inverso.
```bash
cd examples/devenv
docker compose up --build
# frontend → http://localhost:8180
# adminer  → http://localhost:8081
```

### `docuwiki`
Wiki personal corriendo desde una imagen de Docker Hub, sin Dockerfile.
```bash
cd examples/docuwiki
docker compose up
# → http://localhost:8097
```

### `libreoffice`
LibreOffice completo accesible desde el browser vía KasmVNC.
```bash
cd examples/libreoffice
docker compose up
# → http://localhost:3000
```

### `doom`
DOOM corriendo en un contenedor.
```bash
cd examples/doom
docker compose up
# → http://localhost:8880
```

### `jellyfin`
Servidor de medios self-hosted. Montá tus carpetas de películas y series en `./media/movies` y `./media/shows`.
```bash
cd examples/jellyfin
mkdir -p media/movies media/shows
docker compose up
# → http://localhost:8096
```

### `kali-linux`
Kali Linux con escritorio completo accesible desde el browser vía KasmVNC.
```bash
cd examples/kali-linux
docker compose up
# → http://localhost:3000
```

### `bitwarden`
Gestor de contraseñas self-hosted (Vaultwarden, compatible con clientes Bitwarden).
```bash
cd examples/bitwarden
docker compose up
# → http://localhost:8080
```

---

## Versión anterior

La primera versión de esta presentación está disponible en la rama [`v1`](https://github.com/menene/docker/tree/v1).

---

Erick Marroquin · [@menene](https://github.com/menene) · marzo 2026
