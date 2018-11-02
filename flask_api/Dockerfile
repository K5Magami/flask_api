FROM python:3.7

ARG project_dir=/app/

# ADD requirements.txt $project_dir
# ADD app/reply.py $project_dir

WORKDIR $project_dir

RUN pip install flask
# RUN pip install -r requirements.txt

CMD ["python", "reply.py"]