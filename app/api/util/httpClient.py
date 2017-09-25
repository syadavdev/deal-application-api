import http.client, urllib.request
import urllib, requests
from flask import Response
import json

from froodapp.exception.ApiException import ApiException

HTTP_SCHEME = 'http://'

def jsonHttpRequest(serverName, endPoint, dictionary, headerParams, port="80", verb='POST'):
	resp = None
	headers = {'Content-Type':'application/json', 'Accept':'application/json'}

	for key, value in headerParams.items():
		headers[key] = value

	try:
		conn = http.client.HTTPConnection(serverName, port)
		print(json.dumps(dictionary))
		conn.request(verb, endPoint, json.dumps(dictionary), headers)
		response = conn.getresponse()

		if response.status >= 200 and response.status < 210:
			resp = response.read()
			print(resp)
			return resp.decode('UTF-8')

		if response.status >= 400 and response.status <= 450:
			resp = response.read()
			raise ApiException(response.status, response.reason, resp.decode('UTF-8'))

		if response.status >= 500:
			raise ApiException(response.status, response.reason,response.read().decode('UTF-8'))

		return response

	except Exception as e:
		raise e

def httpGET(serverName, endPoint, query, headerParams, port="80"):
	resp = None
	headers = {'Accept':'application/json'}

	for key, value in headerParams.items():
		headers[key] = value

	try:
		#conn = http.client.HTTPConnection(serverName, port)
		if query is not None and bool(query):
			endPoint = endPoint + '?' + urllib.parse.urlencode(query)

		url = HTTP_SCHEME + serverName + ":" + port + endPoint
		#conn.request("GET", endPoint, query, headers)
		print(url)
		response = requests.request('GET', url,headers=headers)
		print(response.status_code)
		if response.status_code >= 200 and response.status_code <= 210:
			print(response.json())
			return response.json()

		if response.status_code >= 400 and response.status_code <= 450:
			raise ApiException(response.status_code, response.reason, response.text)

		return response

	except Exception as e:
		raise e

def httpDelete(url, headers):
	try:
		r = requests.delete(HTTP_SCHEME + url, headers=headers)
		if r.status_code >= 400 and r.status_code <= 450:
			resp = Response(r.iter_content(chunk_size=10 * 1024), content_type=r.headers['Content-Type'])
			raise ApiException(r.status_code, r.reason, resp.data.decode('utf-8'))
		return Response(r.iter_content(chunk_size=10 * 1024), content_type=r.headers['Content-Type']).data.decode('utf-8')
	except Exception as e:
		raise e

def download_file(server_name, file_uri):
	try:
		r = requests.get(server_name+file_uri, stream=True)
		return Response(r.iter_content(chunk_size=10*1024), content_type=r.headers['Content-Type'])
	except Exception as e:
		raise e

def download_with_post(server_name, uri, data, headers, port=80, verb='POST'):
	try:
		r = requests.post(server_name+uri, data=data, headers=headers)
		return Response(r.iter_content(chunk_size=10 * 1024), content_type=r.headers['Content-Type'])
	except Exception as e:
		raise e

def get_secure_server_url(is_secure, server_name):
	if is_secure:
		return "https://"+server_name
	return "http://"+server_name