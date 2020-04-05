#hostuptime KPI monitor

##############################################################################################################################################################

#author:Sanoj

#version:V1.0

#date:16th October 2018

#use:KPI monitor creation for host uptime

#Input:APP, API key, Uptime parameter,webhook details & 3 digit account code

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

# provide 3 digit account code, uptime parameter, webhook details of the respective account

account = input("Please enter the account name =  ")

tags = "IMI_"+account+"_KPI_uptime"

api.Monitor.create(
    
    type="metric alert",
    query="avg(last_15m):avg:system.uptime{*} by {host} >" + input("Please provide the uptime value parameter = "),
    name=tags+" {{host.name}} {{host.ip}}",
    message='{{host.name}} {{host.ip}} System has not been rebooted >' + input("Please provide the uptime parameter in display message in days = ") + 'days\n\n\"severity=2\" @'+input("Please provide webhook info = "),
    tags=tags,
    options=options
)

#output

print("Monitor Created")
