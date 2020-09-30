from locust import HttpUser, task, between, constant
from locust_plugins.csvreader import CSVReader
from pathlib import Path
import hashlib
import hmac
import base64
import logging
import time
# replace with your csv file if you want have dynamic data
user_reader = CSVReader(Path(__file__).parent / "../data/sample_data.csv")

class QuickstartUser(HttpUser):
    #Can be tweaked as per your requirement
    wait_time = constant(0.9)

    @task()
    def your_api_name(self):
        my_user = next(user_reader)
        resp = self.client.get(
            "/<YOUR_API_PATH>",
            name="/<YOUR_API_NAME>",
            headers={
                # If any headers
            },
        )

        if(resp.ok != True):
            print(resp.content)