import openai
from datetime import datetime, timedelta
import pytz

pacific_timezone = pytz.timezone("America/Los_Angeles")
current_time = datetime.now(pacific_timezone)
formatted_time = current_time.strftime("%I:%M %p")

def get_time_4_2hrs_later(time: str):
	current_time_obj = datetime.strptime(time, "%I:%M %p")
	later_time = current_time_obj + timedelta(hours = 4.2)
	
	return later_time.strftime("%I:%M %p")

#tools =[
#{
#	"name":"get_time_4_2hrs_later",
#	"description" : "Get the time 4.2 hours after the current time. Call this when someone needs to know the time 4.2 hours later",
#	"parameters" : {
#		"type" : "object",
#		"properties": {
#			"time":{
#				"type" : "string",
#				"description" : "The current time in HH:MM AM/PM format."
#			}
#		},
#		"required" : ["time"],
#		"additionalProperties" : False
#	},
#	"type" : "function"
#
#}
#]

messages = [
{"role" : "system" , "content": "You are a helpful time telling assistant. Use the tools to assist the user"},
{"role" : "user","content": "Hi can you tell me what time it will be 4.2 hours later?"}
]

response = openai.ChatCompletion.create(
model="gpt-4-0613",
messages=messages,

)
time_4_2_hours_later = get_time_4_2hrs_later(formatted_time)
print(f"The time 4.2 hours later will be: {time_4_2_hours_later}")

	
	
