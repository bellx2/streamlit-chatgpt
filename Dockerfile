FROM condaforge/miniforge3:22.11.1-4
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app
COPY app .
RUN mkdir -p ~/.streamlit/ && printf "[general]\nemail = \"\"\n"  > ~/.streamlit/credentials.toml
EXPOSE 5000
CMD ["streamlit","run","main.py","--server.port","5000"]