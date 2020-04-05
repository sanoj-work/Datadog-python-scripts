#CPU KPI monitor Editor

##############################################################################################################################################################

#author:Sanoj

#version:V1.0

#date:16th October 2018

#use:KPI monitor editor

#Input:APP, API key,new paramter,webhook details,monitor ID 

#Output:KPI monitor update with new values and print "Monitor updated"

################################################################################################################################################################

# Import datadog module and initialise API


from datadog import initialize,  api

#input APP & API key of the respective datadog account

options = {
    'api_key': input ("Please provide api key =  "),
    'app_key': input ("Please provide app key =  ")
}

initialize(**options)

#update the existing monitor with new parameters

api.Monitor.update(
    id= input ("Please provide monitor ID = "),
    query='avg(last_15m):avg:system.cpu.idle{*} by {host} < ' + input("Please provide new parameter value of free cpu required to edit = "),
    message= '{{host.name}} {{host.ip}} CPU utilization is > '+ input("Please provide the parameter value in display message = " )+ '%\n\n\"severity=3\" @'+input("Please provide webhook info = ")
                    )
#output

print("Monitor updated")



