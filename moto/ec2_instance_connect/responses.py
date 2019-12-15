import json
from moto.core.responses import BaseResponse


class Ec2InstanceConnectResponse(BaseResponse):

    def send_ssh_public_key(self):
        return json.dumps(
            {
                'RequestId': '',
                'Success': True
            }
        )
