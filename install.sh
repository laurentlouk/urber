docker build -t urber/urber-app .
docker run --name my-urber-app -p 8000:8000 -d urber/urber-app