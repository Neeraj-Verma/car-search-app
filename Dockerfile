# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the project files to the working directory
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the ports for FastAPI (8000) and Streamlit (8501)
EXPOSE 8000
EXPOSE 8501

# Start both FastAPI and Streamlit
CMD ["sh", "-c", "uvicorn backend:app --host 0.0.0.0 --port 8000 & streamlit run frontend.py --server.port 8501 --server.address 0.0.0.0"]
