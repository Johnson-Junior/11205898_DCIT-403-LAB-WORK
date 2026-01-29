import random

# This class simulates the world our agent lives in
class DisasterEnvironment:
    def get_conditions(self):
        # Simulates random changes in disaster severity
        levels = ["Normal", "Warning: High Winds", "CRITICAL: FLOOD DETECTED", "Normal", "Warning: Tremors"]
        return random.choice(levels)

# Create a global instance of the environment
env = DisasterEnvironment()

import spade
import time
import asyncio
from spade.agent import Agent
from spade.behaviour import PeriodicBehaviour

class SensorAgent(Agent):
    
    # 1. Define the behavior: What does the agent do repeatedly?
    class SensingBehaviour(PeriodicBehaviour):
        async def run(self):
            # "Perceive" the environment by asking the env object
            current_condition = env.get_conditions()
            
            # Log the perception (Percept)
            print(f"[{time.ctime()}] SENSOR READING: {current_condition}")
            
            # Simple logic: If critical, alert the user (simulation of an event trigger)
            if "CRITICAL" in current_condition:
                print("!!! ALERT: DISASTER EVENT TRIGGERED !!!")

    # 2. Setup: Add the behavior when the agent starts
    async def setup(self):
        print(f"SensorAgent {self.jid} starting...")
        
        # Create the behavior to run every 3 seconds
        self.add_behaviour(self.SensingBehaviour(period=3))

async def main():
    # 
    sensor = SensorAgent("shrek@xmpp.jp", "123456")
    await sensor.start()
    
 
    print("Agent is monitoring environment...")
    await asyncio.sleep(15)
    
    await sensor.stop()
    print("Monitoring finished.")

if __name__ == "__main__":
    spade.run(main())
