from openai import OpenAI
from datetime import datetime
client = OpenAI()

today_date = datetime.now().strftime("%m/%d/%Y")

response = client.chat.completions.create(
        model = "gpt-4o-mini-2024-07-18",
        messages=[
                {
                        "role":"system",
                        "content":"You are a helpful assistant that extracts the date of the next Saturday from today in mm/dd/yyyy JSON form."
                },

                {
                        "role" : "user",
                        "content": f"The current date is {today_date}.What is the date of the next upcoming Saturday from today's date. Please respond only with JSON in this format: {{\"date\": \"mm/dd/yyyy\"}}"

                }
        ]
                    
)
print(response.choices[0].message.content)
