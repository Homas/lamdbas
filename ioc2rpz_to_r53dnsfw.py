#(c) Vadim Pavlov
#2023-01-12
#lambda function to import ioc2rpz community feeds to AWS Route 53 DNS Firewall domain lists
#
#
# This lambda functon requires the following permissions:
# - route53resolver:ImportFirewallDomains (all objects or just the domain lists provisioned below)
# - s3:GetObject (all object or the objects listed below)
#
#
import boto3
import os

feeds = [
#['s3 object', 'domains list id']

#free tier
['s3://ioc2rpz-public-feeds-free/adultfree.ioc2rpz','PUT_DOMAIN_LIST_ID_HERE'],                     # large feed
['s3://ioc2rpz-public-feeds-free/blox-ukraine-russia-conflict.ioc2rpz','PUT_DOMAIN_LIST_ID_HERE'],
['s3://ioc2rpz-public-feeds-free/rescure-domains.ioc2rpz','PUT_DOMAIN_LIST_ID_HERE'],
['s3://ioc2rpz-public-feeds-free/local.ioc2rpz','PUT_DOMAIN_LIST_ID_HERE'],

#core tier
#['s3://ioc2rpz-public-feeds-core/doh.ioc2rpz','PUT_DOMAIN_LIST_ID_HERE'],
#['s3://ioc2rpz-public-feeds-core/notracking.ioc2rpz','PUT_DOMAIN_LIST_ID_HERE'],                    # large feed
#['s3://ioc2rpz-public-feeds-core/notracking-dead.ioc2rpz','PUT_DOMAIN_LIST_ID_HERE'],               # large feed

#essentials tier
#['s3://ioc2rpz-public-feeds-essentials/oisd-basic.ioc2rpz','PUT_DOMAIN_LIST_ID_HERE'],
#['s3://ioc2rpz-public-feeds-essentials/blocklist-malicious.ioc2rpz','PUT_DOMAIN_LIST_ID_HERE'],     # large feed
#['s3://ioc2rpz-public-feeds-essentials/hblock.ioc2rpz','PUT_DOMAIN_LIST_ID_HERE'],                  # large feed
#['s3://ioc2rpz-public-feeds-essentials/malicious.ioc2rpz','PUT_DOMAIN_LIST_ID_HERE'],               # large feed

#standard tier
#['s3://ioc2rpz-public-feeds-standard/urlhaus.ioc2rpz','PUT_DOMAIN_LIST_ID_HERE'],
#['s3://ioc2rpz-public-feeds-standard/bforeai.ioc2rpz','PUT_DOMAIN_LIST_ID_HERE'],                   # large feed
#['s3://ioc2rpz-public-feeds-standard/oisd-full.ioc2rpz','PUT_DOMAIN_LIST_ID_HERE'],                 # large feed
#['s3://ioc2rpz-public-feeds-standard/dga-360.ioc2rpz','PUT_DOMAIN_LIST_ID_HERE'],                   # large feed
#['s3://ioc2rpz-public-feeds-standard/phishtank.ioc2rpz','PUT_DOMAIN_LIST_ID_HERE'],

]

r53 = boto3.client('route53resolver')

def lambda_handler(event, context):

    for feed in feeds:
        try:
# https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ImportFirewallDomains.html
            r53r=r53.import_firewall_domains(
                FirewallDomainListId=feed[1],
                Operation='REPLACE',
                DomainFileUrl=feed[0]
            )
        except Exception as e:
            print("Import failed (..):", e)

    
    return {
        'statusCode': 200,
        'body': 'Life is good'
    }
