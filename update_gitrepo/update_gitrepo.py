#!/usr/bin/env python3

import json
import pytz
from datetime import datetime
import urllib.request

def iso_to_jstdt(iso_str):
    dt = None
    try:
        dt = datetime.strptime(iso_str, '%Y-%m-%dT%H:%M:%SZ')
        dt = pytz.utc.localize(dt).astimezone(pytz.timezone("Asia/Tokyo"))
    except ValueError:
        try:
            dt = datetime.strptime(iso_str, '%Y-%m-%dT%H:%M:%S')
            dt = dt.astimezone(pytz.timezone("Asia/Tokyo"))
        except ValueError:
            pass
    return dt

def jstdt_to_timestamp(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')

url='https://api.github.com/users/pandanote-info/repos'

request = urllib.request.Request(url)
try:
    with urllib.request.urlopen(request) as response:
        body = response.read()
except urllib.error.HTTPError as err:
    print(err.code)
except urllib.error.URLError as err:
    print(err.reason)

repos = json.loads(body)
for repo in repos:
    print("insert into gitrepo(name,node_id,html_url,description,updated_at,pushed_at,created_at) values('{0:s}','{1:s}','{2:s}','{3:s}','{4:s}','{5:s}','{6:s}') on duplicate key update name=values(name),html_url=values(html_url),description=values(description),updated_at=values(updated_at),pushed_at=values(pushed_at),created_at=values(created_at);".format(repo["name"],repo["node_id"],repo["html_url"],repo["description"],jstdt_to_timestamp(iso_to_jstdt(repo["updated_at"])),jstdt_to_timestamp(iso_to_jstdt(repo["pushed_at"])),jstdt_to_timestamp(iso_to_jstdt(repo["created_at"]))))
