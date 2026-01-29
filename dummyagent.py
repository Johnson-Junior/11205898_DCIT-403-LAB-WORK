import spade
import asyncio

class DummyAgent(spade.agent.Agent):
    async def setup(self):
        print("Hello World! I'm agent {}".format(str(self.jid)))

async def main():
    # 1. Enter the password you created on the website below
    # 2. We use your new JID: shrek@xmpp.jp
    dummy = DummyAgent("shrek@xmpp.jp", "123456")
    
    await dummy.start()
    print("Agent is starting...")
    
    # Wait to ensure the message prints before the script ends
    await asyncio.sleep(5)
    await dummy.stop()

if __name__ == "__main__":
    spade.run(main())