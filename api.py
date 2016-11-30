from bottle import route, run, request, get
from ejemplo.lib.ec2 import get_instances
from ejemplo.lib.ec2 import get_volumes
from ejemplo.lib.ec2 import get_vpcs
from ejemplo.lib.ec2 import put_tagInInstance

@get('/instances')
def instances():
    instances=get_instances()
    return instances

@get('/volumes')
def volumes():
    volumes=get_volumes()
    return volumes

@get('/vpcs')
def vpcs():
    vpcs=get_vpcs()
    return vpcs

# @post('/login')
@route('/tag', method='POST')
def tag():
    username = request.json['Username']
    put_tagInInstance(username)
    # res= HTTPResponse(status=503,body="{}".format(username))
    return username

run(host='localhost', port=8080, debug=True, reloader=True)