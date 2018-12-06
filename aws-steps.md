## AWS deploying

1 - init eb
eb init -p python-3.6 erpSys --region sa-east-1

2 - set ssh
eb init

3 - Create an environment and deploy your application to it with eb create:
eb create erp-lpc


## testing
eb open

## updating
eb deploy
