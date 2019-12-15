import boto
from moto.core import BaseBackend, BaseModel


class FakeEc2InstanceConnect(BaseModel):

    def __init__(self):
        pass


class Ec2InstanceConnectBackend(BaseBackend):
    def __init__(self, region=None):
        self.region = region


ec2_instance_connect_backends = {}
for region in boto.ec2.regions():
    ec2_instance_connect_backends[region.name] = Ec2InstanceConnectBackend()
