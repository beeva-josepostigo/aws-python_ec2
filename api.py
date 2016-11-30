from bottle import route, run, request, get
from ejemplo.lib.ec2 import get_instances
from ejemplo.lib.ec2 import get_volumes
from ejemplo.lib.ec2 import get_vpcs
from ejemplo.lib.ec2 import put_tagInInstance

#Get method to obtain name of instances defined in AWS account
@get('/instances')
def instances():
    instances=get_instances()
    return instances

#Get method to obtain volumes defined in AWS account
@get('/volumes')
def volumes():
    volumes=get_volumes()
    return volumes

#Get method to obtain VPCs defined in AWS account
@get('/vpcs')
def vpcs():
    vpcs=get_vpcs()
    return vpcs

#Post method to add tag 'Name' in a instance whose name is 'AlphaGroup'
@route('/tag', method='POST')
def tag():
    username = request.json['Username']
    put_tagInInstance(username)
    return username

run(host='localhost', port=8080, debug=True, reloader=True)