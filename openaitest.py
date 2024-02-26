import os
import openai
from apikeys import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Write a email to the biss for my resignation\n",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response["choices"][0]["text"])

"""
{
  "id": "cmpl-8Ah78IEam8nKwcPVchVVbMXikQL0Q",
  "object": "text_completion",
  "created": 1697559702,
  "model": "gpt-3.5-turbo-instruct",
  "choices": [
    {
      "text": "\n\nSubject: Resignation from my position at [Company Name]\n\nDear [BISS Name],\n\nI am writing this email to inform you of my decision to resign from my position at [Company Name]. It has been a privilege to be a part of such a dynamic and innovative organization for the past [period of employment].\n\nAfter much consideration, I have accepted another opportunity that aligns more with my personal and professional goals. While I am sad to leave such a great team and company, I believe this is the right decision for me at this point in my career.\n\nI want to take this opportunity to extend my gratitude to the entire team at [Company Name]. I have learned so much from each and every one of my colleagues during my time here. I am grateful for the support, guidance, and mentorship provided by my managers and colleagues, which has helped me grow both personally and professionally.\n\nIn order to ensure a smooth transition, I am willing to assist in any way possible during my remaining time here. I will complete all of my current tasks and projects and will be available to train my successor if needed. I am open to discuss my ongoing projects with my colleagues and provide any necessary information that will facilitate the smooth transition of my responsibilities.\n\nPlease consider this email as my",
      "index": 0,
      "logprobs": null,
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 11,
    "completion_tokens": 256,
    "total_tokens": 267
  }
}
"""