import configparser
config = configparser.ConfigParser()
config.read('dwh.cfg')

ARN_ROLE=config.get("IAM_ROLE","ARN")
print(ARN_ROLE)