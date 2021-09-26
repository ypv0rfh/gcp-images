# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.7-slim

# Copy local code to the container image.
ENV APP_HOME /app
ENV PYTHONUNBUFFERED TRUE

WORKDIR $APP_HOME
COPY . .

# Install production dependencies.
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org functions-framework
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# Run the web service on container startup.
CMD exec functions-framework --target=fx_rates --signature-type=event
