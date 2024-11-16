#function call to extract_data()

import openai 
import json

def extract_data(grad_note):
	instruction = f"""
	You're a helpful assistant that identifies and generalizes the groups of people/communities mentioned in the user's gratitude note, along with a description of the said group's contribution. For the given gratitude note, identify and extract key groups, generalize them (e.g "Academic Counselors"), and provide a concise description of their contribution
	
	Input:"{gratitude_note}"
	

	The output should have each group's name and their description on a separate line, formatted like:
	[Group Name]: [Generalized summary of what they contributed]

	{{
		"groups":[
			{{
				"group_name":"string",
				"description":"string"
			}}
		]
	}}

	Example:
	Input: "Having a community that appreciates my interests and my intellectual outputs is really important for my sense of self worth, especially seeing other people also wrangling with difficult ideas along with me. This also extends to the community that opened up to me during academic conferences."
	JSON output:
	{{
	   "groups":[
		{{
			"group_name": "Academic Advisors in STEM",
			"description": "for purposefully guiding students in their academic pursuits and self-confidence."
		}},
		{{
			"group_name": "Scientific Research Communities",
			"description": "for fostering an environment of collaboration and learning to motivate aspiring researchers."
		}}
	   ]
	}}
	
	Now process this gratitude note:
	{grad_note}
	"""

	
	response = openai.ChatCompletion.create(
	   model="gpt-4",
	   messages=[
		{"role":"system","content":"You are a helpful assistant that identifies groups and summarizes their contributions."},
		{"role":"user","content":instruction}
	   ],
	)	
	
	try:
		result = response['choices'][0]['message']['content']
		data = json.loads(result)
		return data
	except Exception as e:
		print(f"Error processing: {e}")
		return None
	

if __name__ == "__main__":
	gratitude_note = "The working experience with my advisor is the best I've ever experienced so far. She's such an energetic person with great passion and enthusiasm in exploring science, leading me to think, to dig, and to solve. She's optimistic about life and caring about everyone in our group. She helps me a lot not only in my academic career but also in blending into the US. l'm so lucky to meet her. Love her soooooo much!!"
	data = extract_data(gratitude_note)
	print(json.dumps(data,indent=4))	
