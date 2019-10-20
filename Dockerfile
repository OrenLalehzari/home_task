# Dockerfile

FROM python:3.6

RUN pip install absl-py==0.8.1 aiohttp==3.5.4 aiofiles==0.4.0 aiohttp-jinja2==1.1.1 astor==0.8.0 async-timeout==3.0.1 attrs==19.3.0 chardet==3.0.4 Click==7.0 gast==0.2.2 google-pasta==0.1.7 grpcio==1.24.1 h5py==2.10.0 idna==2.8 idna-ssl==1.1.0 Jinja2==2.10.3 Keras==2.3.1 Keras-Applications==1.0.8 Keras-Preprocessing==1.1.0 Markdown==3.1.1 MarkupSafe==1.1.1 multidict==4.5.2 numpy==1.17.3 opt-einsum==3.1.0 Pillow==6.2.0 protobuf==3.10.0 PyYAML==5.1.2 scipy==1.3.1 six==1.12.0 tensorboard==2.0.0 tensorflow==2.0.0 tensorflow-estimator==2.0.0 termcolor==1.1.0 typing-extensions==3.7.4 Werkzeug==0.16.0 wrapt==1.11.2 yarl==1.3.0

COPY . /syte_task
WORKDIR syte_task

COPY ./docker-scripts/serve /bin/serve
RUN chmod +x /bin/serve

EXPOSE 8080

ENTRYPOINT ["/bin/serve"]