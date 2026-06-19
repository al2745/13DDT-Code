from anthropic import Anthropic

client = Anthropic(
    api_key="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"
)

message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "Say hello in one sentence."
        }
    ]
)

prompt = f"""
You are a fake news analyser.

Analyse the following article.

Provide:
1. Reliability score (1-100)
2. Verdict (Likely Real, Suspicious, or Likely Fake)
3. Suspicious phrases
4. Brief explanation

Article:
{article}
"""

print(message.content[0].text)

message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=300,
    messages=[
        {"role": "user", "content": prompt}
    ]
)