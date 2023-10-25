import openai as op



op.organization = "dsada"
op.api_key = "sdsda"

#system dowolona wiadomosc
#asystent odpowiada
#klient input

open_position = "Senior Developer"
messages = [
    {
        "role": "system",
        "content": f"You are HR assistant which can check the CV candidate are able for {open_position}"
    },
    {
        "role": "user",
        "content": "Candidate's CV text: "
    }
]

chat_completion = op.ChatCompletion.create(
    model="",
    messages=messages
)

response: str = chat_completion.choices[0].message.content