import scratchattach as sa

session = sa.login_by_id(r'".eJxVkMFOwzAQRP8lZwixHTt2b0VAi5A4QKnUk2U7m8ZNY5fEUVQQ_44t5dLrzO6b2f3NphEGp3rIVtluGsIOxpDdZcF34KJUakQbXqqmqFhJMRUUjGAEl6AFV5yv2OfL9XXc8P31Wz7v37ZbtcYntHnCX3PEnP3Runt7iSTBc4SqnJEccRotqabQypQubR19TgijAvNo1Sfljl4G28OPd6nZuofBGvXwDrM8-KG73W_V2MYhJBARStAC64aa2gBpCq2pEKriihEGRYMLjVJCiFca7zub4HMEQn2L1MrEB6ReSQMXYnqw3uWLMeYfcDkv4uMy_PcPD7trBA:1tCMWp:3xSHlAMCInjvKTCsT5MEV63nMgQ"', username="TurtTest") #replace with your session_id and username
cloud = session.connect_cloud("1096825275") #replace with your project id
client = cloud.requests()

@client.request
def finder(answer): #called when client receives request
    findercloud = session.connect_cloud(str(answer))
    if findercloud.logs():
        return [findercloud.logs()[0].username, findercloud.logs()[0].timestamp, findercloud.logs()[0].var, findercloud.logs()[0].value] #sends back 'pong' to the Scratch project
    else:
        return "Could not find any cloud variables in project!"

@client.request
def setter(id, varname, valueset): #called when client receives request
    settercloud = session.connect_cloud(str(id))
    if settercloud.get_var(str(varname)) == None:
        print("Fail!")
        return "That variable name could not be found! Check for a typo maybe?"
    else:
        settercloud.set_var(str(varname), str(valueset))
        print("Success!")
        print(valueset)
        return "Success!"



@client.event
def on_ready():
    print("Request handler is running")

client.start(thread=True) # thread=True is an optional argument. It makes the cloud requests handler run in a thread
