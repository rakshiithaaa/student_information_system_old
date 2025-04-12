# Use the official Python 3.9 image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir flask mysql-connector-python

# Set Flask environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV FLASK_ENV=production  # Set Flask to production mode

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["flask", "run"]
