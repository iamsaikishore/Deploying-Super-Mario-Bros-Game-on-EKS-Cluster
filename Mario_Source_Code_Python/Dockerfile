# Base image for Python 3.7
FROM python:3.7-slim

RUN apt-get update && apt-get install -y xvfb

# Set working directory within the container
WORKDIR /app

# Copy game files into the container
COPY . /app

# Install required dependencies
RUN pip install -r requirements.txt

# Expose port 8080 (adjust if your game uses a different port)
EXPOSE 8080

# Start virtual display before game
ENTRYPOINT ["xvfb-run", "--auto-servernum"]

# Set the command to start the game
CMD ["python", "main.py"]

