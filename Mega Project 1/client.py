from openai import OpenAI


client = OpenAI(
    api_key="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",

)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message.content)