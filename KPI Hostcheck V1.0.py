#hostcheckKPI monitor

##############################################################################################################################################################

#author:Sanoj

#version:V1.0

#date:16th October 2018

#use:KPI monitor creation for host connectivity check

#Input:APP, API key & 3 digit account code

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
	   "no_data_timeframe": input("Please input no data time frame in minutes = "),
		"escalation_message": "",
		"thresholds": {
			"critical": 1,
			"warning": 1,
			"ok": 1
		}
	}
# provide 3 digit account code of the respective account

account = input("Please enter the account name =  ")
tags = "IMI_"+account+"_HOST_check"
api.Monitor.create(
    type="service check",
    query="\"datadog.agent.up\".over(\"*\").by(\"host\").last(2).count_by_status()",
    name=tags+" {{host.name}} {{host.ip}}",
    message='{{host.name}} {{host.ip}} system is probably down; Please check the system  \n\n\"severity=4\"  @'+ input("Please provide webhook info = "),
    tags=tags,
    options=options
)

#output

print("Monitor Created")
