FROM python:slim

RUN pip install uv

WORKDIR /app
COPY README.md pyproject.toml requirements.lock ./
RUN uv pip install --no-cache --system -r requirements.lock

COPY src .
CMD streamlit run hasu_stamina_calc/app.py --server.port 8080