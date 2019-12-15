import boto3

from moto import mock_ec2_instance_connect

pubkey = """ssh-rsa
AAAAB3NzaC1yc2EAAAADAQABAAABAQDV5+voluw2zmzqpqCAqtsyoP01TQ8Ydx1eS1yD6wUsHcPqMIqpo57YxiC8XPwrdeKQ6GG6MC3bHsgXoPypGP0LyixbiuLTU31DnnqorcHt4bWs6rQa7dK2pCCflz2fhYRt5ZjqSNsAKivIbqkH66JozN0SySIka3kEV79GdB0BicioKeEJlCwM9vvxafyzjWf/z8E0lh4ni3vkLpIVJ0t5l+Qd9QMJrT6Is0SCQPVagTYZoi8+fWDoGsBa8vyRwDjEzBl28ZplKh9tSyDkRIYszWTpmK8qHiqjLYZBfAxXjGJbEYL1iig4ZxvbYzKEiKSBi1ZMW9iWjHfZDZuxXAmB
example
"""


@mock_ec2_instance_connect
def test_send_ssh_public_key():
    client = boto3.client("ec2-instance-connect")
    fake_response = {
        "RequestId": "example-2a47-4c91-9700-e37e85162cb6",
        "Success": True,
        "ResponseMetadata": {
            "HTTPStatusCode": 200,
            "HTTPHeaders": {"server": "amazon.com"},
            "RetryAttempts": 0,
        },
    }

    response = client.send_ssh_public_key(
        InstanceId="i-abcdefg12345",
        InstanceOSUser="ec2-user",
        SSHPublicKey=pubkey,
        AvailabilityZone="us-east-1a",
    )

    assert response == fake_response
