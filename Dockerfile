FROM python:3-alpine

RUN apk add --no-cache git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-vickytorresburgos.git

WORKDIR /ajedrez-2024-vickytorresburgos

RUN pip install -r requirements.txt

CMD ["sh", "-c", "coverage run -m unittest && coverage report -m && python -m game.cli"]

# docker buildx build -t ajedrez-2024-torres .

# docker run -i ajedrez-2024-torres