import googleapiclient.discovery
from pprint import pprint
from googleapiclient import discovery
from google.oauth2 import service_account
from oauth2client.client import GoogleCredentials
import logging
import json
from flask import jsonify

# service account details

PROJECT_ID = 'cloud-migration-solution'
region='us-central1'
filter_zone = ("name:" + region + "*")
credentials = GoogleCredentials.get_application_default()
service = discovery.build('compute', 'v1', credentials=credentials, cache_discovery=False)


                                                      
def get_list_of_zones():
   try:
        zones_request = service.zones().list(project=PROJECT_ID,filter=filter_zone)
        zones_response = zones_request.execute()
        # print(response)
        return json.dumps(zones_response["items"])
   except:
      return json.dumps({"ERROR":1,"description":"not found"})


def get_list_of_instances(PROJECT_ID,filter_zone):
        print ("Function is executing")
        zones_request = service.zones().list(project=PROJECT_ID,filter=filter_zone)
        zones_response = zones_request.execute()
        items = zones_response["items"]
        instance_list=[]
        for item in items:
            zone = item['description']  
            request=service.instances().list(project=PROJECT_ID,zone=zone)
            try: 
              response=request.execute()
              for instance in response['items']:
                inst_status = instance['status']
                inst_name = instance['name']
                inst_zone = zone 
                instance_list.append({"name":inst_name,"zone":inst_zone,"status":inst_status})
            except:
              pass  
        return instance_list

                                                  

def start_instanse(zone,instance_name):
    try:
        start_request=service.instances().start(project=PROJECT_ID,zone=zone,instance=instance_name)
        start_response=start_request.execute()
        return json.dumps(start_response["items"])
    except:
        return json.dumps({"code":1,"description":"not found"})


def stop_instance(zone,instance_name):
    try:
        stop_request=service.instances().stop(project=PROJECT_ID,zone=zone,instance=instance_name)
        stop_response=stop_request.execute()
        return json.dumps(stop_response["items"])
    except:
        return json.dumps({"code":1,"description":"not found"})








