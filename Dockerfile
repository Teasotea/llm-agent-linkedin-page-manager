FROM python:3.12

# Install the project into `/app`
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the project's dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Then, add the rest of the project source code and install it
# Installing separately from its dependencies allows optimal layer caching
ADD . /app

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Reset the entrypoint, don't invoke `uv`
ENTRYPOINT []

# Run the Streamlit application by default
CMD ["streamlit", "run", "app.py"]
