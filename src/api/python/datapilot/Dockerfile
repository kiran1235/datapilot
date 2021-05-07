FROM continuumio/miniconda3:latest
WORKDIR /app
EXPOSE 3030

COPY requirements.txt /app/requirements.txt
RUN python --version && \
    conda install -c anaconda gunicorn && \
    pip install -r /app/requirements.txt

ENTRYPOINT ["sh","-c"]
CMD ["gunicorn --workers=2 --bind=0.0.0.0:3030 --reload --reload-engine auto app:app"]