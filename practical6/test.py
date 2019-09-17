import agentframework

jack = agentframework.Agent()

for i in range(10**10):
    jack.move()
    print(jack)