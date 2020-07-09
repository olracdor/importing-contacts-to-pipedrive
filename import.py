import requests
import sys
import json
import csv

print sys.path[0]
with open(sys.path[0] + '/import.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        
        if line_count > 0:
            data = {
                    "name": row[2],
                    "phone": [
                        {
                            "label": "Work",
                            "value": row[4]
                        },
                        {
                            "label": "Mobile",
                            "value": row[3]
                        }
                    ],
                    "email": [
                        {
                            "label": "Work",
                            "value": row[5]
                        },
                        {
                            "label": "Home",
                            "value": row[6]
                        },
                        {
                            "label": "Other",
                            "value": row[7]
                        }
                    ]
                }
            print json.dumps(data)
            headers = {"Accept": "application/json",
                "Content-Type": "application/json"}
            url = "https://api.pipedrive.com/v1/persons/"+ row[1] +"?api_token=<TOKEN>"
            print "Sending request to " + url
            resp = requests.put(url, data=json.dumps(data), headers=headers)
            print resp
            if resp.status_code == 404:
                url = "https://api.pipedrive.com/v1/persons?api_token=<TOKEN>"
                print "Sending request to " + url
                resp = requests.post(url, data=json.dumps(data), headers=headers)
                print resp

        line_count += 1
        

