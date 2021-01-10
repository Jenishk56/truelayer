# Pokemon API

- Covering the API(As expected) with automation and easier way to start the app.

# Description
I have created an app which provides the API for pokemon description in Shakespear's way. Tried to make it easier to use. Also, the framework is structured in a way that it could be scaled in future for multiple use.

Also, Have provided the Dockerfile and Makefile to make life more easier. Dockerfile build the image with code + necessary packages and Makefile to run those docker image with only one click.

I have covered the testcases ofcourse considering the TDD way of working. Covered only the mandatory test case considering the timeline of the project.

# How to Run ?
- Clone the project
  
  ```git clone https://github.com/Jenishk56/truelayer.git```
- Start the app
  
  ```make start```
- Run Unit test
  
  ```Keep the server running on one tab```
  
  ```make test``` 

- I have made the port static `5000` for now. Go to browser and try `http://localhost:5000/pokemon/charizard/`

# About API

While running the API, It would show the output something like 

```
{
  "description": "Charizard flies 'round the sky in search of powerful opponents. 't breathes fire of such most wondrous heat yond 't melts aught. However,  't nev'r turns its fiery breath on any opponent weaker than itself.",
  "name": "charizard"
}
```

- As per Pokemon api, for one pokemon name, there are many description available for english langaguge itself. I am <b>randomly picking</b> any of these and providing in output. The same output I am passing on Shakespear API and throwing that as a result of my pokemon API.

# What i could have improved

As per given timeline, i tried to implement the best i can. If i would have more time, I would be happy to implement follow parts.
  - Authentication in front of the Main API.
  - Auto deployment using Jenkins or equivalant tools for the API build, package and deployment.
  - Deployment on Kubernetes with scalable configuration through Helm chart / Weave flux.
  - Could have cover more testcases for more worse scenarios.
  
