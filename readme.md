# Usage

## Requirements

- Platform : Linux Ubuntu or Windows or Mac

- Docker installed in your computer

## Run docker containers

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

## Show services with docker compose

```bash
   $ docker compose ps

   NAME IMAGE COMMAND SERVICE CREATED STATUS PORTS
   backend_streamlit_app docker_streaming_app-backend_streamlit_app "uvicorn main:app --…" backend_streamlit_app 49 minutes ago Up 49 minutes 0.0.0.0:4000->4000/tcp, :::4000->4000/tcp
   stream_mongo_db mongo "docker-entrypoint.s…" stream_mongo_db 49 minutes ago Up 49 minutes 0.0.0.0:27017->27017/tcp, :::27017->27017/tcp
   streamlit_app docker_streaming_app-streamlit_app "streamlit run main.…" streamlit_app 49 minutes ago Up 49 minutes 0.0.0.0:8501->8501/tcp, :::8501->8501/tcp
```

You will see results like :

When you see you can access to :<br>

- Streamlit service with url : [http://localhost:8501](http://localhost:8501) (copy and paste this url on your browser)

- Backend service with url: [http://0.0.0.0:4000](http://0.0.0.0:4000) (copy and paste this url on your browser)

For more informations contact me on mtchokos@gmail.com.<br>
Enjoy and have a best day,<br>
Thanks.
