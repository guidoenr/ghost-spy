FROM guidoenr4/ubuntu-gostpy

WORKDIR /root/home/workspace/ghost-spy/

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3","main.py"]