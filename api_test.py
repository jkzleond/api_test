# -*- coding=utf-8 -*-
import urllib2
import json
import sys
import getopt

api_host = 'http://localhost:8850/'
apis = {
        'add_group': {
            'need_token': True,
				'method': 'POST',
            'url': 'v1/im/group',
				'data': {
        				'name': '我们的群',
        				'image': 'http://api.alhelp.net'
				}
          		},
			'delete_group': {
				'need_token': True,
				'method': 'DELETE',
				'url': 'v1/im/group/22',
				'data': None
			},
			'modify_group': {
				'need_token': True,
				'method': 'PUT',
				'url': 'v1/im/group/22',
				'data': {
					'name': '修改过的'
				}
			},
			'add_group_member': {
				'need_token': False,
				'method': 'POST',
				'url': 'v1/im/group/22/member',
				'data': {
					'member_ids': [130, 131] 
				}
			},
			'delete_group_member': {
				'need_token': False,
				'method': 'DELETE',
				'url': 'v1/im/group/22/member',
				'data': {
					'member_ids': [131]
				}
			},
			'get_groups': {
				'need_token': False,
				'method': 'GET',
				'url': 'v1/im/groups?p=1&ps=2',
				'data': {
					'filters': {
						'name': '修改过的'
					}
				}	
			},
			'get_demand_collaborate': {
				'need_token': True,
				'method': 'GET',
				'url': 'v1/demands/collaborates/4834?page=1',
				'data': None
			},
			'get_follows': {
				'need_token': True,
				'method': 'GET',
				'url' : 'v1/follow',
				'data': None
			},
			'get_someone_talks_list': {
				'need_token': True,
				'method': 'GET',
				'url': 'v1/talks/list/14257',
				'data': None
			}
        	}

token_url = 'http://localhost:8850/v1/tokens'
credential = json.dumps({
	'passwordCredentials': {
		'username': 'jkzleond', 
		'password': '19831123'
	}
})

def api_request(api_name):
	try:
		api_config = apis[api_name]
	except KeyError as e:
		print 'api ' + api_name + ' is not defined\n'
		exit()

	need_token = api_config['need_token']
	api_url = api_host + api_config['url']
	api_data = json.dumps(api_config['data'])
	api_method 	= api_config['method']
	
	api_req = urllib2.Request(api_url, data=api_data)
	api_req.get_method = lambda: api_method	

	if need_token is True:
		token_req = urllib2.Request(token_url, data=credential)
		token_res = urllib2.urlopen(token_req)
		token = json.loads(token_res.read())
		api_req.add_header('X-Auth-Token', token['data']['X-Subject-Token'])

	api_res = urllib2.urlopen(api_req)
	return api_res.read()

def api_list():
	for api_name in apis.keys():
		print api_name

def usage():
	print 'usage:'
	print '-n api name you want to test'

if __name__ == '__main__':
	opt, argv = getopt.getopt(sys.argv[1:], 'n:l')
	if len(opt) == 0:
		usage()
	for key, value in opt:
		if key == '-n':
			print api_request(value).decode('raw_unicode_escape')
		elif key == '-l':
			api_list()
		else:
			usage()
			exit()
	


