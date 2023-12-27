import sys
import os
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tinydb.db import TinyDbClient

def show_table_test():
    client = TinyDbClient("127.0.0.1", 4083)
    ret = json.loads(client.execute("show tables"))
    print(ret)

def select_test():
    client = TinyDbClient("127.0.0.1", 4083)
    ret = json.loads(client.execute("select * from A"))
    print(ret)
show_table_test()
select_test()
