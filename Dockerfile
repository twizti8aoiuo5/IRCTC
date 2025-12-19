FROM python:3.9-slim

# Install only the necessary Chromium packages
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir flask selenium

COPY . .

# Set Render port
ENV PORT=10000
EXPOSE 10000

CMD ["python", "app.py"]
