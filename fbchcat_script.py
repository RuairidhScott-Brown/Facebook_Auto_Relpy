
from fbchat import log, Client
from fbchat.models import*
import pickle
import random

with open("session_data.txt","rb") as f:
    session = pickle.load(f)

class EchoBot(Client):
    def onMessage(self, mid, author_id, message_object, thread_id, thread_type, ts, metadata, msg, **kwargs):
        emotion_list = ['YES','SMILE']
        list = random.choice(emotion_list)

        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        print(author_id)
        print(message_object)
        print(thread_type)
        print(thread_id)
        print(self)
        print(mid)
        print(ts)
        print(metadata)
        print(msg)
        if thread_type.name == "GROUP" and (author_id == mum or author_id == dad):
            if list == 'YES':
                client.reactToMessage(mid, MessageReaction.YES)
            if list =='SMILE':
                client.reactToMessage(mid, MessageReaction.SMILE)



        if author_id == self.uid:
            self.send(Message(text = 'yo yo yo yo yo yo yo'), thread_id = client.uid, thread_type = ThreadType.USER)
            print("111111111111")
        if message_object.text == "testing":
            print("222222222222")
        if thread_type.name == "USER":
            print("333333333333")



client = EchoBot("<email>", "<password>", session_cookies = session)
message_id = client.send(Message(text='message'), thread_id=client.uid, thread_type=ThreadType.USER)
print(message_id)
client.reactToMessage(message_id, MessageReaction.LOVE)
user1 = client.searchForUsers('Roderick Brown ')
user2 = client.searchForUsers('Sue Scott')
dad =user1[0]
mum =user2[0]
print("User's main url: {}".format(mum.url))
print("User's main url: {}".format(dad.url))
client.send(Message(text='facebook auto reply is running'), thread_id = client.uid, thread_type = ThreadType.USER)
client.listen()
