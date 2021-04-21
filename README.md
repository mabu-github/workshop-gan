# Workshop GAN

## AWS

Provision an EC2 instance with the latest "Deep Learning Ubuntu" AMI. The instance type "g4dn.xlarge" is recommended 
as it uses the cost-efficient NVIDIA T4 graphics cards.

## SSH Access to AWS Instance

Preparation

```
ssh_credentials=workshop.pem
ec2_instance=ec2-<IP>.eu-central-1.compute.amazonaws.com
ec2_portforwarding=8888
```

Restrict permissions to credentials

```
chmod 400 "$ssh_credentials"
```

Connect

```
ssh -i "$ssh_credentials" ubuntu@"$ec2_instance"
ssh -i "$ssh_credentials" -L "$ec2_portforwarding:localhost:$ec2_portforwarding" ubuntu@"$ec2_instance"
```