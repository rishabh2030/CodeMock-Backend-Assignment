# Running Django Project 💻
---
### Prerequisite
- Python 3.8 or latest t installed locally.
### Env Method
For this method, you need to have PostgreSQL installed and running locally. Additionally, you have to configure the database in the `.env ` file.
1. Create a virtual environment to isolate our package dependencies locally:
    ` # Create a virtual environment to isolate our package dependencies locally`
    `python3 -m venv env`
2. Activate the env:
    `env\Scripts\activate or mac/linux source env/bin/activate `
3. Then run this command for install all dependencies:
    `pip install -r requirements.txt`
4. Run the project by this command:
    `python manage.py runserver`
---
### Docker

For this method, you need to have Docker installed locally. If you haven't installed it yet, please download Docker Desktop from [here](https://www.docker.com/products/docker-desktop/).

1. Build the container using the following command:
    `docker-compose up --build`
    This command will create the container on your local Docker environment.
2. Optionally, the project will automatically start running at localhost:8008. If not, run the following command:
    `docker-compose up`

---
### Important Links
- Postman API Documentation [here](https://www.postman.com/telecoms-geoscientist-33370767/workspace/codemock-backend-assignment/collection/23160347-c9f3f3b5-5a9f-4ac3-afa0-f1b07f814f8c)
- Documentation [here](https://docs.google.com/document/d/1b7yIVTT3cCaQrIHPUCU0L0j0Vj-Qckv-vxU1jUL9Y1w/edit?usp=sharing)
