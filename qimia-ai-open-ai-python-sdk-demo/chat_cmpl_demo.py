from oai_client import client

key_values = {
    "use_cache": False,  # Use embedded cache for session
}

completion = client.chat.completions.create(
    model="vicuna",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "What are the basics of programming?"}
    ],
    extra_body={"key_values": key_values}
)

print(completion.model_dump_json(indent=4))
