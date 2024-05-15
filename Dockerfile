# Choose our version of Python
FROM python:3.10.1

# Set up a working directory
WORKDIR /code

# Copy just the requirements into the working directory so it gets cached by itself
COPY ./requirements.txt /code/requirements.txt

# Install the dependencies from the requirements file
RUN pip install --no-cache-dir  -r /code/requirements.txt

# Copy the code into the working directory
COPY ./app /code/app

WORKDIR /code/app

# Expose port to access API endpoint
EXPOSE 8030

# Tell uvicorn to start spin up our code, which will be running inside the container now
CMD ["uvicorn", "serve_prices:app", "--host", "0.0.0.0", "--port", "8030"]