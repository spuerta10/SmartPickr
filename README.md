# SmartPickr 🎯

SmartPickr es un sistema inteligente de recomendaciones de anime que combina una interfaz web interactiva con agentes de inteligencia artificial para ofrecer recomendaciones personalizadas basadas en tus gustos.

## 🎌 ¿Qué es SmartPickr?

SmartPickr es una aplicación que te ayuda a descubrir nuevos animes basándose en tus preferencias. El sistema funciona de la siguiente manera:

1. **Te presenta animes para calificar**: Muestra una serie de animes populares para que los califiques con "Me gusta" o "No me gusta"
2. **Analiza tus gustos**: Utiliza agentes de IA (powered by n8n) para entender tus preferencias basándose en tus calificaciones
3. **Genera recomendaciones personalizadas**: Te sugiere animes que podrían gustarte basándose en el análisis de tus gustos
4. **Muestra resultados detallados**: Presenta las recomendaciones con información completa de cada anime

## 🚀 Características principales

* **Interfaz intuitiva**: Una aplicación web simple y fácil de usar construida con Streamlit
* **IA inteligente**: Agentes de n8n que analizan patrones en tus calificaciones para hacer recomendaciones precisas
* **Flujo guiado**: Te lleva paso a paso desde la calificación inicial hasta las recomendaciones de los animes
* **Arquitectura modular**: Código bien organizado siguiendo patrones MVC para fácil mantenimiento
* **Despliegue sencillo**: Funciona tanto localmente con Python como con Docker
* **Generador de datos**: Herramienta incluida para importar tu lista personal de MyAnimeList

## 🔄 Cómo funciona el flujo

El sistema maneja cuatro estados principales:

1. **INITIAL_RATING**: Calificas una selección de animes
2. **LOADING**: Los agentes de IA procesan tus calificaciones  
3. **RECOMMENDATIONS**: Se muestran las recomendaciones personalizadas
4. **COMPLETE**: Resumen final de la sesión

## 🤖 Integración con n8n

El proyecto incluye un workflow completo de n8n que maneja la lógica de recomendaciones mediante tres agentes especializados:

- **Anime Recommendations Agent**: Analiza tus calificaciones y selecciona animes compatibles con tus preferencias
- **Recommendations Analyzer Agent**: Revisa y valida la calidad de las recomendaciones
- **Description Improver Agent**: Mejora las descripciones de los animes recomendados

## 📊 Generador de datos personalizado

Incluye una herramienta que te permite:
- Importar tu lista personal de MyAnimeList (formato XML)
- Generar una base de datos personalizada con tus animes
- Crear archivos de configuración listos para usar

---

## 🛠️ Instalación y ejecución local

### Prerrequisitos

* **Python 3.11+** (ver archivo `.python-version`)
* **uv** (recomendado) - gestor de paquetes más rápido que pip
* Alternativamente: **pip** estándar de Python

### Opción 1: Instalación rápida con uv (recomendada)

```bash
# 1. Clona el repositorio
git clone https://github.com/spuerta10/SmartPickr.git
cd SmartPickr

# 2. Instala uv si no lo tienes
pip install uv

# 3. Instala dependencias y crea entorno virtual automáticamente
uv sync

# 4. Ejecuta la aplicación
uv run streamlit run src/smartpickr/main.py
```

### Opción 2: Instalación tradicional con pip

```bash
# 1. Clona el repositorio
git clone https://github.com/spuerta10/SmartPickr.git
cd SmartPickr

# 2. Crea entorno virtual
python -m venv .venv

# 3. Activa el entorno virtual
# En Windows (PowerShell):
.venv\Scripts\Activate.ps1
# En Linux/Mac:
# source .venv/bin/activate

# 4. Actualiza pip e instala dependencias
pip install -U pip
pip install streamlit streamlit-product-card

# 5. Ejecuta la aplicación
streamlit run src/smartpickr/main.py
```

### 🌐 Accede a la aplicación

Una vez ejecutada, abre tu navegador en: [http://localhost:8501](http://localhost:8501)

> **Tip**: Puedes cambiar el puerto usando: `streamlit run src/smartpickr/main.py --server.port 8502`

---

## 🐳 Ejecución con Docker (todo incluido)

La forma más fácil de probar SmartPickr con todas sus funcionalidades es usando Docker, que incluye tanto la aplicación como el servidor n8n con los agentes de IA.

### Prerrequisitos

* **Docker** y **Docker Compose** instalados en tu sistema

### Ejecución en un comando

```bash
# Desde la carpeta del proyecto
docker compose -f docker/docker-compose.yml up --build
```

### 🎯 Lo que obtienes

* **SmartPickr (aplicación web)**: disponible en [http://localhost:8501](http://localhost:8501)
* **n8n (servidor de agentes IA)**: disponible en [http://localhost:5678](http://localhost:5678)

### 🔧 Configuración del workflow n8n

1. Accede a n8n en [http://localhost:5678](http://localhost:5678)
2. Importa el workflow desde `n8n/content_recommendation_wf.json`
3. El workflow se activará automáticamente para procesar las recomendaciones

### Detener los servicios

```bash
docker compose -f docker/docker-compose.yml down
```

---

## 📁 Estructura del proyecto

```
SmartPickr/
├── 📄 README.md                      # Documentación del proyecto
├── 📄 pyproject.toml                 # Dependencias de Python
├── 📄 uv.lock                        # Lock file para dependencias
├── 🐳 docker/                        # Configuración de Docker
│   ├── Dockerfile.smartpickr         # Imagen Python 3.11 + uv
│   └── docker-compose.yml            # n8n (5678) + Streamlit (8501)
├── 🤖 n8n/                          # Workflows de agentes IA
│   ├── content_recommendation_wf.json # Workflow principal
│   └── prompts/                      # Prompts para cada agente
│       ├── anime_recommendations_agent.txt
│       ├── description_improver_agent.txt
│       └── recommendations_analyzer_agent.txt
├── 📊 src/
│   ├── data_generator/               # Herramientas para generar datos
│   │   ├── data_generator.py         # Script principal
│   │   ├── title_extractor.py        # Extractor de títulos
│   │   ├── requirements.txt          # Dependencias específicas
│   │   └── in/                       # Archivos de entrada (XML de MAL)
│   └── smartpickr/                   # Aplicación principal
│       ├── main.py                   # Punto de entrada
│       ├── context/                  # Gestión de estados
│       │   ├── manager.py            # Gestor de contexto
│       │   ├── rating/               # Módulo de calificaciones
│       │   │   ├── controller.py
│       │   │   └── handler.py
│       │   └── recommendations/      # Módulo de recomendaciones
│       │       ├── controller.py
│       │       ├── handler.py
│       │       └── views/
│       │           ├── loading.py    # Vista de carga
│       │           └── sumary.py     # Vista de resumen
│       ├── model/                    # Modelos de datos
│       │   └── anime.py              # Modelo Anime
│       └── shared/                   # Componentes compartidos
│           ├── base_controller.py    # Controlador base
│           └── views/                # Vistas compartidas
│               ├── base.py
│               └── anime.py
└── 🏗️ terraform/                    # Infraestructura como código
    ├── main.tf                       # Configuración principal
    ├── provider.tf                   # Proveedores
    ├── variables.tf                  # Variables
    ├── terraform.tfvars             # Valores de variables
    └── scripts/
        └── setup_db.sh              # Script de configuración DB
```

---

## 🎮 Uso de la aplicación

### Paso 1: Calificación inicial
- La aplicación te mostrará una selección de animes populares
- Califica cada uno con "👍 Me gusta" o "👎 No me gusta"
- Tus calificaciones serán la base para las recomendaciones

### Paso 2: Procesamiento IA
- Los agentes de n8n analizan tus gustos
- Se procesan patrones en tus calificaciones
- Se seleccionan animes compatibles con tus preferencias

### Paso 3: Recomendaciones personalizadas
- Recibes una lista de animes recomendados
- Cada recomendación incluye:
  - Título y descripción mejorada
  - Número de temporadas y episodios
  - Géneros principales
  - Imagen representativa

### Paso 4: Resumen final
- Revisión de toda tu sesión
- Posibilidad de exportar resultados
- Opción para comenzar una nueva sesión

---

## 🛠️ Generador de datos personalizado

El proyecto incluye herramientas para personalizar tu experiencia con tus propios animes:

### Importar desde MyAnimeList

```bash
# Navegar al generador de datos
cd src/data_generator

# Instalar dependencias específicas
pip install -r requirements.txt

# Colocar tu archivo XML exportado de MAL en la carpeta 'in/'
# Ejecutar el generador
python data_generator.py
```

### Lo que hace el generador

1. **Lee tu lista personal**: Importa el XML exportado desde MyAnimeList
2. **Enriquece los datos**: Obtiene información detallada usando la API de MAL
3. **Genera archivos**: Crea `mock_animes.json` y `mock_animes.txt`
4. **Calcula estadísticas**: Añade información realista de temporadas y episodios

---

## ⚙️ Configuración avanzada

### Variables de entorno

```bash
# Puerto de Streamlit (opcional)
PORT=8501

# Configuración de n8n (opcional)
N8N_PORT=5678
N8N_WEBHOOK_URL=http://localhost:5678/webhook/recommendations
```

### Personalización de puertos

```bash
# Cambiar puerto de Streamlit
streamlit run src/smartpickr/main.py --server.port 8502

# En Docker (editar docker-compose.yml)
ports:
  - "8502:8501"  # puerto_host:puerto_contenedor
```

### Configuración de agentes IA

Los prompts de los agentes están en `n8n/prompts/` y se pueden personalizar:

- **anime_recommendations_agent.txt**: Lógica principal de recomendaciones
- **recommendations_analyzer_agent.txt**: Validación y análisis de calidad
- **description_improver_agent.txt**: Mejora de descripciones

---

## 🚀 Despliegue en producción

### Con Terraform (infraestructura en la nube)

```bash
cd terraform

# Inicializar Terraform
terraform init

# Planificar despliegue
terraform plan

# Aplicar infraestructura
terraform apply
```

### Consideraciones de producción

- **Base de datos**: Configurar PostgreSQL para persistencia
- **Escalabilidad**: Usar contenedores con orquestadores (K8s, Docker Swarm)
- **Monitoreo**: Implementar logging y métricas
- **Seguridad**: Configurar HTTPS y autenticación

---

## 🐛 Solución de problemas

### Problemas comunes

| Problema | Causa | Solución |
|----------|-------|----------|
| Página en blanco | Imports incorrectos | Ejecutar desde la carpeta raíz del proyecto |
| Puerto ocupado | Otro servicio usa el puerto 8501 | Usar `--server.port 8502` |
| Docker lento | Primera construcción | Las siguientes serán más rápidas (cache) |
| n8n no conecta | Workflow no importado | Importar `content_recommendation_wf.json` |
| Error de dependencias | Entorno no configurado | Ejecutar `uv sync` o instalar con pip |

### Logs útiles

```bash
# Logs de Docker Compose
docker compose -f docker/docker-compose.yml logs

# Logs específicos de un servicio
docker compose -f docker/docker-compose.yml logs smartpickr
docker compose -f docker/docker-compose.yml logs n8n

# Verificar puertos en uso (Windows)
netstat -an | findstr :8501
netstat -an | findstr :5678
```

---

