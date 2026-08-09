Unicorn setup:
uvicorn app:app --host 127.0.0.1 --port 8000

Tcpdump:
tcpdump -i lo -nn 'tcp port 8000'
