#Disk space KPI monitor

##############################################################################################################################################################

#author:Sanoj

#version:V1.0

#date:16th October 2018

#use:KPI monitor creation for disk usage

#Input:APP, API key,free disk space parameter,webhook details & 3 digit account code

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
			"critical": 10
		}
	}
# provide 3 digit account code,diskspace parameter,display message parameter,webhook of the respective account

account = input("Please enter the account name =  ")

tags = "IMI_"+account+"_KPI_Diskspace"
api.Monitor.create(
    type="query alert",
    query="avg(last_1m):( avg:system.disk.free{*} by {host,device} / avg:system.disk.total{*} by {host,device} ) * 100 < " + input("Please provide free disk space parameter = " ),
    name=tags+"{{host.name}} {{host.ip}}",
    message='{{host.name}} {{host.ip}} disk free space <' +  input("Please provide free disk space in display message = ")+ '%\n\n\"severity=3\"  @'+input("Please provide webhook details = "),
    tags=tags,
    options=options
)

#output

print("Monitor created")
