## AWS deploying

1 - init eb
eb init -p python-3.6 erpSysv2 --region sa-east-1

2 - set ssh
eb init
eb init, run it again with the --interactive


3 - Create an environment and deploy your application to it with eb create:
eb create erp-lpc


## testing
eb open
eb ssh erp-lpc


## updating
eb deploy


## instance

ec2-user@ec2-18-231-2-128.sa-east-1.compute.amazonaws.com
ec2-18-231-2-128.sa-east-1.compute.amazonaws.com
