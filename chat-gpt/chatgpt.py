import openai
openai.api_key = "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"

prompt = "Hello, can you help me with something?"
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=60,
    n=1,
    stop=None,
    temperature=0.5,
)
message = response.choices[0].text.strip()
print(message)