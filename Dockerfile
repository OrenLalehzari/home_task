# Dockerfile

FROM python:3.6

RUN pip install absl-py==0.8.1 aiohttp==3.6.2 aiohttp-jinja2==1.2.0 astor==0.8.0 async-timeout==3.0.1 atomicwrites==1.3.0 attrs==19.3.0 chardet==3.0.4 gast==0.2.2 google-pasta==0.1.7 grpcio==1.24.1 h5py==2.10.0 idna==2.8 idna-ssl==1.1.0 importlib-metadata==0.23 Jinja2==2.10.3 Keras==2.3.1 Keras-Applications==1.0.8 Keras-Preprocessing==1.1.0 Markdown==3.1.1 MarkupSafe==1.1.1 more-itertools==7.2.0 multidict==4.5.2 numpy==1.17.3 opt-einsum==3.1.0 packaging==19.2 Pillow==6.2.1 pluggy==0.13.0 protobuf==3.10.0 py==1.8.0 pyparsing==2.4.2 pytest==5.2.1 pytest-aiohttp==0.3.0 PyYAML==5.1.2 scipy==1.3.1 six==1.12.0 tensorboard==2.0.0 tensorflow==2.0.0 tensorflow-estimator==2.0.1 termcolor==1.1.0 typing-extensions==3.7.4 wcwidth==0.1.7 Werkzeug==0.16.0 wrapt==1.11.2 yarl==1.3.0 zipp==0.6.0

COPY . /syte_task
WORKDIR syte_task

COPY ./docker-scripts/serve /bin/serve
RUN chmod +x /bin/serve

EXPOSE 8080

ENTRYPOINT ["/bin/serve"]