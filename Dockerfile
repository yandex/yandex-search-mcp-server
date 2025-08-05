# Yandex Search API MCP Server Dockerfile
# Base image with Python 3.10
FROM python:3.10-slim as builder

# Image metadata
LABEL org.opencontainers.image.title="Yandex Search API MCP Server"
LABEL org.opencontainers.image.description="MCP server for Yandex Search API v2 with web and AI search capabilities"
LABEL org.opencontainers.image.vendor="Yandex LLC"
LABEL org.opencontainers.image.version="1.0.0"
LABEL org.opencontainers.image.licenses="Apache-2.0"

# Install dependencies
RUN pip install requests mcp[cli]

# Final image
WORKDIR /app
ENV PATH=/root/.local/bin:$PATH

# No need to copy dependencies with global installation
COPY --chown=1000:1000 server.py detail.py ./

# Environment setup
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONPATH=/app
USER 1000

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD python3 -c "import requests; requests.get('http://localhost/health')"

# Command to run the MCP server using the virtual environment
CMD ["python3", "server.py"]
