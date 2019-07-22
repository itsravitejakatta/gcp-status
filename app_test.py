#!/usr/bin/python

from util import gcp
PROJECT_ID = "cloud-migration-solution"
region = "us-central1"
filter_zone = ("name:" + region + "*")  

gcp.get_list_of_instances(PROJECT_ID,filter_zone)
