#hostuptime KPI monitor

##############################################################################################################################################################

#author:Sanoj

#version:V1.0

#date:16th October 2018

#use:KPI monitor creation for host uptime

#Input:Monitor name to check if already exists,APP, API key, Uptime parameter,webhook details & 3 digit account code

#Output:KPI monitor creates and print "Monitor created", If already exists it skip the steps with pop up message skipping

############################################################
#check if monitor already exists
import requests

url = "https://app.datadoghq.com/api/v1/monitor"
querystring = {"api_key": "a1e0667020c9db069874e88532473174",
               "application_key": "435032dc09c9e44138821fe4f4de424ce9a943e6"}
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "a98e3323-a047-41ad-b4fd-c6caf8887b9d"
}

response = requests.request("GET", url, headers=headers, params=querystring)
file = open("data.txt", "w+")
file.write(response.text)
file.close()

# import & initialise datadog API module

if input("Please input the KPI name to check if already exists = ") in open("data.txt").read():
    print("Monitor already exists,skipping")
else:
    from datadog import initialize, api

    # Provide app & api key of the respective Datadog account

    options = {
        'api_key': input("Please provide api key =  "),
        'app_key': input("Please provide app key =  ")
    }

    initialize(**options)

    # Create a new monitor
    options = {

        "timeout_h": 0,
        "silenced": {},
        "new_host_delay": 300,
        "renotify_interval": 0,
        "escalation_message": "",
        "thresholds": {

        }
    }

    # provide 3 digit account code, cpu parameter,message display & webhook info of the respective account

    account = input("Please enter the 3 digit account name =  ")
    tags = "IMI_" + account + "_KPI_CPU"
    webhook=input("Please provide webhook details = ")
    api.Monitor.create(
        type="metric alert",
        query="avg(last_15m):avg:system.cpu.idle{*} by {host} < 10",
        name=tags + " {{host.name}} {{host.ip}}",
        message='{{host.name}} {{host.ip}} CPU utilization is > 90%'+ '\n\n\"severity=3\" @'+webhook,
        tags=tags,
        options=options
    )

    # output

    print(" CPU Monitor Created")
       # Create a new monitor

    options = {

        "timeout_h": 0,
        "silenced": {},
        "new_host_delay": 300,
        "renotify_interval": 0,
        "escalation_message": "",
        "thresholds": {

        }
    }
    # provide 3 digit account code,parameter of free memory in percentage,display message parameter &webhook details of the respective account

    
    tags = "IMI_" + account + "_KPI_Mem"

    response = api.Monitor.create(
        type="query alert",
        query='avg(last_15m):( avg:system.mem.usable{*} by {host} / avg:system.mem.total{*} by {host} ) * 100 < 10',
        name=tags + "{{host.name}} {{host.ip}}",
        message="{{host.name}} {{host.ip}} Memory free is < 10%" +'\n\n\"severity=3\" @'+webhook,
        tags=tags,
        options=options
    )

    # output

    print(" Memory Monitor created")

          # Create a new monitor
    options = {

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

    

    tags = "IMI_" + account + "_KPI_Diskspace"
    api.Monitor.create(
        type="query alert",
        query="avg(last_1m):( avg:system.disk.free{*} by {host,device} / avg:system.disk.total{*} by {host,device} ) * 100 < 10 ",
        name=tags + "{{host.name}} {{host.ip}}",
        message='{{host.name}} {{host.ip}} disk free space < 10%' + '\n\n\"severity=3\" @'+webhook,
        tags=tags,
        options=options
    )

    # output

    print(" Disk space Monitor created")

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

tags = "IMI_"+account+"_KPI_Swap"
api.Monitor.create(
    type="query alert",
    query="avg(last_15m):( avg:system.swap.free{*} by {host} / avg:system.swap.total{*} by {host} ) * 100 < 10" ,
    name=tags+"{{host.name}} {{host.ip}}",
    message="{{host.name}} {{host.ip}} Swap free space is < 10%"+'\n\n\"severity=3\" @'+webhook,
    tags=tags,
    options=options
)

#output

print(" Swap Monitor created")

# Create a new monitor

options ={

	    "timeout_h": 0,
		"silenced": {},
	   "new_host_delay": 300,
	   "renotify_interval": 0,
	   "no_data_timeframe": 5,
		"escalation_message": "",
		"thresholds": {
			"critical": 1,
			"warning": 1,
			"ok": 1
		}
	}
# provide 3 digit account code of the respective account
tags = "IMI_"+account+"_HOST_check"
api.Monitor.create(
    type="service check",
    query="\"datadog.agent.up\".over(\"*\").by(\"host\").last(2).count_by_status()",
    name=tags+" {{host.name}} {{host.ip}}",
    message='{{host.name}} {{host.ip}} system is probably down; Please check the system  \n\n\"severity=4\" @'+webhook,
    tags=tags,
    options=options
)

#output

print(" Host check Monitor Created")

# Create a new monitor

options = {
    "timeout_h": 0,
    "silenced": {},
    "new_host_delay": 300,
    "renotify_interval": 0,
    "escalation_message": "",
    "thresholds": {

    }
}
tags = "IMI_" + account + "_KPI_uptime"

api.Monitor.create(

    type="metric alert",
    query="avg(last_15m):avg:system.uptime{*} by {host} > 8000000",
    name=tags + " {{host.name}} {{host.ip}}",
    message='{{host.name}} {{host.ip}} System has not been rebooted > 90'+'days\n\n\"severity=2\" @'+webhook,
    tags=tags,
    options=options
)

# output

print(" Uptime Monitor Created")









