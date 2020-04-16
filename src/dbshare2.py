#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, requests, json, time

file_path = sys.argv[1]
db_token = sys.argv[2]
db_folder = sys.argv[3]

timestamp = time.strftime('%Y%m%d%H%M%S')

token = 'Bearer ' + db_token
file_name = os.path.basename(file_path)
file_ts = timestamp + "_" + file_name


def upload(file):
	url = "https://content.dropboxapi.com/2/files/upload"

	headers = {
	    "Authorization": token,
	    "Content-Type": "application/octet-stream",
	    "Dropbox-API-Arg": "{\"path\":\"/" + db_folder + "/" + file_ts + "\",\"mode\":{\".tag\":\"add\"},\"autorename\":true,\"mute\":false}"
	}

	data = open(file_path, "rb").read()

	r = requests.post(url, headers=headers, data=data)
	json_data = r.text
	parsed_json = json.loads(json_data)
	return parsed_json['path_lower']


def get_link(file):
	headers = {'Authorization': token,'Content-Type': 'application/json'}
	payload = {'path': file}

	r = requests.post("https://api.dropboxapi.com/2/sharing/create_shared_link_with_settings", json=payload, headers=headers)
	json_data = r.text
	parsed_json = json.loads(json_data)
	url_preview = parsed_json['url']
	url_download = url_preview.replace("dl=0", "dl=1")

	try:
		return url_download
	except:
		return parsed_json['error']['shared_link_already_exists']['metadata']['url']


uploaded = upload(file)
url = get_link(uploaded)

sys.stdout.write(url)