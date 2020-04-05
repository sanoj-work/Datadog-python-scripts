#CPU KPI monitor

##############################################################################################################################################################

#author:Sanoj

#version:V1.0

#date:16th October 2018

#use:KPI monitor creation for CPU usage

#Input:APP, API key,cpu parameter,webhok details & 3 digit account code

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

# provide 3 digit account code, cpu parameter,message display & webhook info of the respective account

account = input("Please enter the account name =  ")
tags = "IMI_"+account+"_KPI_CPU"
api.Monitor.create(
    type="metric alert",
    query="avg(last_15m):avg:system.cpu.idle{*} by {host} <" + input("Please provide the threshold parameter of free cpu = "),
    name=tags+" {{host.name}} {{host.ip}}",
    message='{{host.name}} {{host.ip}} CPU utilization is > ' + input("Please provide the threshold parameter in display message = ")+'%\n\n\"severity=3\" @' + input("Please provide webhook information = "),
    tags=tags,
    options=options
)

#output

print("Monitor Created")
