from collections import deque
from flask import Flask
import datetime
import threading
import time
import psutil as psutil
from jsonpickle import json

app = Flask(__name__)
mem_history = deque(maxlen=60)


def record_mem():
    while True:
        if len(mem_history) == 60:
            mem_history.pop()
        date = datetime.datetime.now()
        date = int(date.timestamp())
        mem_history.append({'date': date, 'memory_usage': psutil.virtual_memory().percent})
        time.sleep(10)


t = threading.Thread(target=record_mem)
t.daemon = True
t.start()


@app.route("/mem", methods=['GET'])
def get_memory_history():
    history = list(mem_history)
    # to allow external access to the endpoint you need to add 'Access-Control-Allow-Origin': '*' to the headers
    return json.dumps(history), 200, {'Access-Control-Allow-Origin': '*'}


if __name__ == '__main__':
    app.run(debug=True)
