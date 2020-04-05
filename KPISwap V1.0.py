#SWAP KPI monitor

##############################################################################################################################################################

#author:Sanoj

#version:V1.0

#date:16th October 2018

#use:KPI monitor creation for swap usage

#Input:APP, API key ,swap parameter,webhook details& 3 digit account code

#Output:KPI monitor creates and print "Monitor created"

################################################################################################################################################################

#import & initialise datadog API module

from datadog import initialize, api

#Provide app & api key of the respective Datadog account


options = {
    'api_key': input ("Please provide api key =  "),
    'app_key': input ("Please provide app key =  ")
}

initialize(**options)

# Create a new monitor
options ={

	    "timeout_h": 0,
		"silenced": {},
	   "new_host_delay": 300,
	   "renotify_interval": 0,
		"escalation_message": "",
		"thresholds": {
			
		}
	}
#provide 3 digit account code,swap parameter,display message parameter & webhook details of the respective account

account = input("Please enter the account name =  ")

tags = "IMI_"+account+"_KPI-Swap"
api.Monitor.create(
    type="query alert",
    query="avg(last_15m):( avg:system.swap.free{*} by {host} / avg:system.swap.total{*} by {host} ) * 100 <" + input("Please provide free swap parameter = "),
    name=tags+"{{host.name}} {{host.ip}}",
    message="{{host.name}} {{host.ip}} Swap free space is <" +input("Please provide free swap parameter in display message = ")+'%\n\n\"severity=3\" @'+input("Please provide webhook info = "),
    tags=tags,
    options=options
)

#output

print("Monitor creatd")
