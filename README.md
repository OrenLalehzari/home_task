---------------------------------
Home Task
---------------------------------



How to run
====================
run docker image. for example:

docker build -t syte_home_task .
docker run -p 8080:8080 syte_home_task serve



API
====================

Health
=============
URL:
    /health

Method:
    GET

URL Params:
    None

Response:
    {"health": "Ok"}
    

Predict
=============
URL:
    /predict

Method:
    POST

URL Params:
    None

Data Params:
    Required: 
        image_file=[Image]
        
Response:
    array of strings. for example:
    ["n04479046, trench_coat, 0.20388673", "n02667093, abaya, 0.07812133", "n03680355, Loafer, 0.073182926"]