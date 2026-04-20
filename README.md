# 🚀 Hola Mundo DevOps — CI/CD con GitHub Actions

Pipeline completo: **Código → Test → Docker Hub → Render.com**

```
git push → GitHub Actions → Test → Build imagen → Push Docker Hub → Deploy Render
```

---

## 📁 Estructura del proyecto

```
hola-mundo-app/
├── .github/
│   └── workflows/
│       └── ci-cd.yml        ← Pipeline CI/CD completo
├── app.py                   ← Aplicación Flask
├── requirements.txt         ← Dependencias Python
├── Dockerfile               ← Imagen Docker
├── render.yaml              ← Config de Render.com
└── README.md
```

---

## ⚙️ CONFIGURACIÓN INICIAL (hacer una sola vez)

### 1️⃣ Subir el proyecto a GitHub

```bash
git init
git add .
git commit -m "feat: hola mundo devops con CI/CD"
git remote add origin https://github.com/TU_USUARIO/hola-mundo-devops.git
git push -u origin main
```

### 2️⃣ Obtener las API Keys necesarias

#### Docker Hub Token
1. Ir a https://hub.docker.com → Account Settings → Security
2. Click **New Access Token**
3. Nombre: `github-actions`, Permisos: **Read, Write, Delete**
4. Copiar el token generado

#### Render.com API Key + Service ID
1. Ir a https://dashboard.render.com → Account Settings → API Keys
2. Click **Create API Key** → copiar la key
3. Crear el servicio web en Render (conectar repo de GitHub)
4. En la URL del servicio copiar el **Service ID** (formato: `srv-xxxxxxxxxxxx`)

### 3️⃣ Agregar Secrets en GitHub

Ir a: **GitHub repo → Settings → Secrets and variables → Actions → New repository secret**

| Secret Name            | Valor                              |
|------------------------|------------------------------------|
| `DOCKERHUB_USERNAME`   | Tu usuario de Docker Hub           |
| `DOCKERHUB_TOKEN`      | Token generado en Docker Hub       |
| `RENDER_API_KEY`       | API Key de Render.com              |
| `RENDER_SERVICE_ID`    | ID del servicio (srv-xxxxxxxxxxxx) |

---

## 🔄 Cómo funciona el pipeline

```
┌─────────────┐     push a main     ┌──────────────────────────────────────────┐
│  git push   │ ──────────────────► │           GitHub Actions                 │
└─────────────┘                     │                                          │
                                    │  Job 1: TEST                             │
                                    │  ├── Setup Python 3.11                   │
                                    │  ├── pip install requirements.txt        │
                                    │  └── curl /health → ✅                   │
                                    │           ↓ (si tests pasan)             │
                                    │  Job 2: DOCKER                           │
                                    │  ├── Login Docker Hub                    │
                                    │  ├── Build imagen (amd64 + arm64)        │
                                    │  └── Push → :latest + :sha-xxxxx         │
                                    │           ↓ (si imagen fue publicada)    │
                                    │  Job 3: DEPLOY                           │
                                    │  └── POST /deploys → Render.com ✅       │
                                    └──────────────────────────────────────────┘
```

### Los 3 jobs del workflow

| Job | Nombre | Condición |
|-----|--------|-----------|
| `test` | 🧪 Test Application | Siempre (push y PR) |
| `docker` | 🐳 Build & Push Docker Hub | Solo push a main + test pasó |
| `deploy` | 🚀 Deploy a Render.com | Solo push a main + imagen publicada |

---

## 🧪 Probar el pipeline

```bash
# Hacer cualquier cambio y pushear
echo "# cambio" >> README.md
git add . && git commit -m "test: trigger CI/CD pipeline"
git push

# Ver el pipeline corriendo en:
# https://github.com/TU_USUARIO/hola-mundo-devops/actions
```

---

## 🔍 Verificar resultados

- **GitHub Actions:** https://github.com/TU_USUARIO/hola-mundo-devops/actions
- **Docker Hub:** https://hub.docker.com/r/TU_USUARIO/hola-mundo-devops
- **App en producción:** https://hola-mundo-devops.onrender.com

---

## 📊 Ciclo DevOps completado

| Fase | Herramienta | Estado |
|------|-------------|--------|
| Código | Python + Flask | ✅ |
| Control de versiones | GitHub | ✅ |
| CI/CD | GitHub Actions | ✅ |
| Contenedor | Docker | ✅ |
| Registry | Docker Hub | ✅ |
| Producción | Render.com | ✅ |
# cambio
