from typing import Dict, Any
from openai.types.chat import ChatCompletion

from oai_client import client

key_values: Dict[str, Any] = {
    "use_cache": False,  # Use embedded cache for session
}

completion: ChatCompletion = client.chat.completions.create(
    model="vicuna",
    messages=[
        {"role": "system", "content": "You are a title generator. Generate a title for the content from Human"},
        {"role": "user", "content": "For Real Madrid, last season couldn’t have gone much better. En route to "
                                    "becoming the Turkish Airlines EuroLeague champion for an 11th time, which came "
                                    "in Chus Mateo's first year as head coach, the team showed the Real Madrid DNA "
                                    "that has often been associated with the club's soccer team in recent years. "
                                    "Time and time again, particularly in the playoffs, Los Blancos defied the odds "
                                    "by returning from the dead to grab a big victory. Heading into Year Two under "
                                    "Coach Mateo, the goal will be what it always is at Real: to lift the EuroLeague "
                                    "title once again."}
    ],
    stop=["Title Generator:"],
    extra_body={"key_values": key_values}
)

print(completion.model_dump_json(indent=4))
