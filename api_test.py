# -*- coding=utf-8 -*-
import urllib2
import json
import sys
import getopt

sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('UTF-8')

#api_host = 'http://api.alhelp.net/'
api_host = 'http://localhost:8850/'
apis = {
		'add_single_message': {
			'need_token': True,
			'method': 'POST',
			'url': 'v1/im/message/single/516',
			'data': {
				'mime_type': 0,
				'content': 'haha'
			}
		},
		'add_group_message': {
			'need_token': True,
			'method': 'POST',
			'url': 'v1/im/message/group/29',
			'data': {
				'mime_type': 0,
				'content': '一条大于十个字的消息会被哈哈'
			}
		},
		'get_no_read_msg': {
			'need_token': True,
			'url': 'v1/im/message/no_read',
			'method': 'GET',
			'data': None
		},
		'get_no_read_msg_total': {
			'need_token': True,
			'url': 'v1/im/message/no_read_total',
			'method': 'GET',
			'data': None
		},
		'mark_read_msg': {
			'need_token': True,
			'url': 'v1/im/message/mark_read/single/516',
			'method': 'PUT',
			'data': None
		},
		'get_single_history': {
			'need_token': True,
			'method': 'GET',
			'url': 'v1/im/message/history/single/516',
			'data': None
		},
		'get_group_history': {
			'need_token': True,
			'method': 'GET',
			'url': 'v1/im/message/history/group/29',
			'data': None
		},
		'get_rct_contacts': {
			'need_token': True,
			'method': 'GET',
			'url': 'v1/im/message/rct_contacts',
			'data': None
		},
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
		'get_group': {
			'need_token': True,
			'method': 'GET',
			'url': 'v1/im/group/16',
			'data': None
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
			'need_token': True,
			'method': 'GET',
			'url': 'v1/im/groups?p=1&ps=2',
			'data': {
				'filters': {
					'name': '我们的群'
				}
			}	
		},
		'get_demand_collaborate': {
			'need_token': True,
			'method': 'GET',
			'url': 'v1/demands/collaborates/4834?page=1',
			'data': None
		},
		'get_talk_by_id': {
			'need_token': True,
			'method': 'GET',
			'url': 'v1/talks/50'
		},
		'get_follows': {
			'need_token': True,
			'method': 'GET',
			'url' : 'v1/follow/15034',
			'data': None
		},
		'get_someone_talks_list': {
			'need_token': True,
			'method': 'GET',
			'url': 'v1/talks/list/14257',
			'data': None
		},
		'get_master_talks': {
			'need_token': False,
			'method': 'GET',
			'url': 'v1/talks/list/master/page/1',
			'data': None
		},
		'get_follows_talks': {
			'need_token': True,
			'method': 'GET',
			'url': 'v1/talks/list/follow',
			'data': None
		},
		'get_all_talks': {
			'need_token': True,
			'method': 'GET',
			'url': 'v1/talks/list',
			'data': {
				'community_id': '2'
			}
		},
		'set_talk_top': {
			'need_token': True,
			'method': 'PUT',
			'url': 'v1/talks/1/top',
			'data': None
		},
		'unset_talk_top': {
			'need_token': True,
			'method': 'PUT',
			'url': 'v1/talks/1/top_off',
			'data': None
		},
		'set_talk_hot': {
			'need_token': True,
			'method': 'PUT',
			'url': 'v1/talks/1/hot',
			'data': None
		},
		'unset_talk_hot': {
			'need_token': True,
			'method': 'PUT',
			'url': 'v1/talks/1/hot_off',
			'data': None
		},
		'set_talk_ann': {
			'need_token': True,
			'method': 'PUT',
			'url': 'v1/talks/1/ann',
			'data': None
		},
		'unset_talk_ann': {
			'need_token': True,
			'method': 'PUT',
			'url': 'v1/talks/1/ann_off',
			'data': None
		},
		'gen_order': {
			'need_token': True,
			'method': 'POST',
			'url': 'v1/order',
			'data': {
				'address_id': '13',
				'items': [
					{
						'business_id': '5262',
						'goods': [
							{
								'type': 'book',
								'id': '321',
								'quantity': 10			
							},
							{
								'type': 'book',
								'id': '322',
								'quantity': 5			
							}
						],
						'shipping_template_id': '0',
						'shipping_price': '0.00',
						'remark': '给卖家的留言'
					},
					{
						'business_id': '5131',
						'goods': [
							{
								'type': 'book',
								'id': '151',
								'quantity': 2			
							}
						],
						'shipping_template_id': '0',
						'shipping_price': '0.00',
						'remark': '给卖家的留言'
					}
				]
			}
		},
		'pay_order': {
			'need_token': True,
			'url': 'v1/order/pay/remain',
			'method': 'PUT',
			'data': {
				'order_ids': [570, 594]
			}
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
	


