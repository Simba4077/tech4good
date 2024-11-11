import openai
from datetime import datetime
import pytz
pacific_timezone = pytz.timezone("America/Los_Angeles")
current_time = datetime.now(pacific_timezone)
formatted_time = current_time.strftime("%I:%M %p")
response = openai.ChatCompletion.create(
	model= "gpt-4",
	messages= [
	 {
		"role":"system",
		"content":"You are a helpful assistant that always provides the specific answer to time-related questions without disclaimers or explanations."
	
 	 },
	 {
		"role":"user",
		"content": "What is the current time in the Pacific timezone?"
	 },
	 {
		"role":"assistant",
		"content":f"The current time is {current_time} in the Pacific timezone"
 	 },
	 {
		"role":"user",
		"content":"What time will it be when I add 1.75 hours to the current time?"
	 },
 	 {
		"role":"assistant",
		"content":"The time after adding 1.75 hours will be {current_time} + 1.75 hours"
	 }
	]
)
print(response['choices'][0]['message']['content'])
#print(response.choices[0].message.content)

