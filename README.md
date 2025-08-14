# SmartPickr

SmartPickr is a tiny, modular **Streamlit** app that walks a user through a short rating flow and then shows **personalized recommendations** (currently mocked with anime titles). It’s organized with lightweight MVC-style modules (controllers, views, and a simple context manager) and ships with **Docker** and an example **n8n** workflow for automation.

---

## What this project is about

* **Interactive recommendations demo**: a guided “like / dislike” flow followed by a recommendations screen.
* **Context-based workflow**: the UI advances through four contexts: `INITIAL_RATING → LOADING → RECOMMENDATIONS → COMPLETE`.
* **Clean, modular structure**: controllers handle logic, views render UI, and a context manager orchestrates state via `st.session_state`.
* **Drop-in deployment**: run locally with Python, or spin up with Docker Compose (plus an n8n instance on port 5678).

---

## Run it from scratch (local)

### Prerequisites

* **Python 3.11** (see `.python-version`)
* Optional but recommended: **uv** package manager (faster installs). You can also use `pip`.

### 1) Clone and enter the project

```bash
git clone <your-repo-url>.git
cd SmartPickr/SmartPickr
```

### 2A) Install with `uv` (recommended)

```bash
pip install uv
uv sync              # creates .venv and installs deps from pyproject.toml
```

### 2B) …or install with `pip`

```bash
python -m venv .venv
# Linux/Mac
source .venv/bin/activate
# Windows (PowerShell)
# .venv\Scripts\Activate.ps1

pip install -U pip
pip install -e .      # optional if you add a pyproject build system
pip install streamlit streamlit-product-card
```

### 3) Run the app

From the `SmartPickr/SmartPickr` directory:

```bash
# default port 8501
streamlit run src/smartpickr/main.py
# or, choose a custom port:
# streamlit run src/smartpickr/main.py --server.port 8502
```

Now open: [http://localhost:8501](http://localhost:8501)

> Tip: If you used `uv sync`, you can also run:
>
> ```bash
> uv run streamlit run src/smartpickr/main.py
> ```

---

## Run it with Docker (one command)

### Prerequisites

* **Docker** and **Docker Compose**

### 1) Build & start

From the `SmartPickr/SmartPickr` directory:

```bash
docker compose -f docker/docker-compose.yml up --build
```

### 2) What you’ll get

* **SmartPickr (Streamlit)** on [http://localhost:8501](http://localhost:8501)
* **n8n** on [http://localhost:5678](http://localhost:5678) (started with a tunnel; import the sample workflow at `n8n/content_recommendation_wf.json` if you want to integrate automations)

To stop:

```bash
docker compose -f docker/docker-compose.yml down
```

---

## Project structure

```
SmartPickr/
└── SmartPickr/
    ├── docker/
    │   ├── Dockerfile.smartpickr     # Python 3.11-slim + uv; exposes port 8501
    │   └── docker-compose.yml         # n8n (5678) + Streamlit app (8501)
    ├── n8n/
    │   └── content_recommendation_wf.json
    ├── src/smartpickr/
    │   ├── main.py
    │   ├── context/
    │   │   ├── manager.py
    │   │   ├── rating/
    │   │   │   ├── controller.py
    │   │   │   └── handler.py
    │   │   └── recommendations/
    │   │       ├── controller.py
    │   │       ├── handler.py
    │   │       └── views/loading.py
    │   ├── model/anime.py
    │   └── shared/
    │       ├── base_controller.py
    │       └── views/
    │           ├── base.py
    │           └── anime.py
    ├── pyproject.toml                 # deps: streamlit, streamlit-product-card
    └── .python-version                # 3.11
```

---

## Configuration

* **Ports**: Streamlit defaults to `8501`; change via `--server.port` or `PORT` env in Dockerfile.
* **Environment variables**: none required by default.
* **n8n**: optional. Import the JSON in `n8n/` to your n8n instance and wire it to the app if you want automations.

---

## Troubleshooting

* **Black page or import errors**: make sure you run from the `SmartPickr/SmartPickr` folder so relative imports in `src/smartpickr` resolve.
* **Port already in use**: run Streamlit on a different port: `--server.port 8502`.
* **Docker build is slow**: it installs `uv` and syncs deps; subsequent builds are cached.

---
