# Usage

## Requirements

- Platform : Linux Ubuntu or Windows or Mac

- Docker installed in your computer

# Steps

## 1. Run docker containers

```bash
   $ docker compose up -d

   [+] Running 3/4
   ⠴ Network docker_streaming_app_network_app Created                                   11.5s
   ✔ Container backend_streamlit_app           Start...                                   6.9s
   ✔ Container stream_mongo_db                 Started                                    7.1s
   ✔ Container streamlit_app                   Started                                    8.4s
```

Docker will be run three services :

- mongodb service

- streamlit service

- backend service

## 2.Show services with docker compose

```bash
   $ docker compose ps
```

You can access to :<br>

- Streamlit service with url : [http://localhost:8501](http://localhost:8501) (copy and paste this url on your browser after step 1)

- Backend service with url: [http://0.0.0.0:4000](http://0.0.0.0:4000) (copy and paste this url on your browser after step 2)

For more informations contact me on mtchokos@gmail.com.<br>
Enjoy and have a best day,<br>
Thanks.
