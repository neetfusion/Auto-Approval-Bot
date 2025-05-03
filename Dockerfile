# Use a specific version of Python (3.10.8 in this case)
FROM python:3.10.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install the dependencies from requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the entire contents of your app into the container
COPY . /app

# Set the environment variable to prevent Python from buffering output (useful for logging)
ENV PYTHONUNBUFFERED 1

# Run the bot with the appropriate command (assuming your entry point is bot.py)
CMD ["python3", "bot.py"]
