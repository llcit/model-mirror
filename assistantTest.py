import os
import time
from openai import OpenAI

APIKEY = os.environ['OPENAI_API_KEY']

client = OpenAI(api_key=APIKEY)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Israel Baline had a difficult childhood. His family had to leave Russia when he was very young. They had been discriminated against because they were Jewish. They decided to immigrate to America. When Israel and his family came to New York City, they arrived at Ellis Island. Israels life was not easy. His family was poor. When he was young, he worked very hard delivering newspapers to help his family. When Israel grew up, he decided to do what he liked best. He was a singer. He changed his name to Irving Berlin. He sang in small cafés in New York. Then, he became very popular. Irving not only sang, he also wrote songs. His music was played all over the world. His songs were so admired that he was invited to visit the President of the U.S. He also created musical plays. They were performed on Broadway, where New Yorks most famous theaters are located. Irving became wealthy, but he was never greedy. He composed “God Bless America,” a very well known song. He donated the money he earned from it to the Girl Scouts and Boy Scouts. Another song he wrote is “White Christmas.” You may have heard it playing in December. These songs helped Americans during World War II. They gave people hope for victory. Irving deeply loved America. He also loved New York City. He lived and worked there his whole life. It was a long life, too. He lived to be 101 years old! We can be proud of Irving. His life shows how important it is to work hard and do what you do best."
)

run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id='asst_A2LrxIWZht5Gf2rqCqv5CZ4d'
)

while True:
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    if any(msg.role == 'assistant' for msg in messages):
        break
    time.sleep(10)

for msg in messages:
    print(msg.content)
