FROM guidoenr4/ubuntu-ghost-spy

WORKDIR /root/home/workspace/ghost-spy/

COPY . .

ENTRYPOINT ["python3","main.py"]
