from collections import deque
from flask import Flask
from flask_restful import Resource, Api
import datetime
import threading
import time
import psutil as psutil

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


class ServerMem(Resource):
    def get(self):
        ret = list(mem_history)
        # to allow external access to the endpoint you need to add 'Access-Control-Allow-Origin': '*' to the headers
        return ret, 200, {'Access-Control-Allow-Origin': '*'}


app = Flask(__name__)
api = Api(app)
database = []
api.add_resource(ServerMem, '/mem', endpoint="statistics", methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)
