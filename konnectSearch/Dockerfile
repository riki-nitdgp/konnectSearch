FROM python:3.9.19-slim-bullseye

RUN apt-get update && apt-get install -y curl && apt-get clean

WORKDIR /usr/src/konnectSearch

COPY requirements.txt .

RUN pip3 install -r requirements.txt


COPY . .

# RUN chmod +x run_service.sh
#
# EXPOSE 8002
# EXPOSE 80

# CMD ["bash", "run_service.sh"]