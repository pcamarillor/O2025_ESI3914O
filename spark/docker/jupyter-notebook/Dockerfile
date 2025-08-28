FROM spark-base:latest
LABEL author="Pablo Camarillo" email="pablo.camarillo@iteso.mx"
LABEL version="0.3"

# Install Jupyter Notebook and Python dependencies
RUN set -ex; \
    apt-get update; \
    apt-get install -y python3 python3-pip; \
    pip3 install --no-cache-dir jupyter; \
    rm -rf /var/lib/apt/lists/*

ENV PYSPARK_DRIVER_PYTHON='jupyter'
ENV PYSPARK_DRIVER_PYTHON_OPTS='notebook --no-browser --port=8888'

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]