#Memory KPI monitor

##############################################################################################################################################################

#author:Sanoj

#version:V1.0

#date:16th October 2018

#use:KPI monitor creation for Memory usage

#Input:APP, API key, free memory paramter,webhook details & 3 digit account code

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
# provide 3 digit account code,parameter of free memory in percentage,display message parameter &webhook details of the respective account

account = input("Please enter the 3 DIGIT account name =  ")
tags = "IMI_"+account+"_KPI-Mem"


response=api.Monitor.create(
    type="query alert",
    query='avg(last_15m):( avg:system.mem.usable{*} by {host} / avg:system.mem.total{*} by {host} ) * 100 <'  + input("Please provide the threshold parameter of free memory = "),
    name=tags+"{{host.name}} {{host.ip}}",
    message="{{host.name}} {{host.ip}} Memory free is < "+ input("Please provide the threshold parameter in display message = ") + '%\n\n\"severity=3\" @' + input("Please provide webhook info = "),
    tags=tags,
    options=options
)
    
   

#output

print("Monitor created")
