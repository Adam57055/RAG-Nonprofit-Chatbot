from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model = 'gpt-4o-mini',
  messages=[
    {
      "role", "system",
      "content": "You are an assistant tasked with locating information in the website pertaining to users' concerns",
      "content": "Use correct JSON ONLY",
    },
    {
      "role", "user",
      "content": "Who can I contact for questions?"
    },
  ]
)
