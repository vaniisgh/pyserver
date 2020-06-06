## use your venv

- whatever you follow

### **Test using Python**

```bash
# Install Required Packages
pip install -r requirements.txt
# Run Server
python3 server.py &
# Manually Test
curl -i localhost:5000/
curl -i localhost:5000/test/request
```

### **Using Docker Compose to setup jenkins**

```bash
# Start containerized service on Docker for the jenkis
docker-compose up -d
```
it's at localhost 8080

If you have installed Jenkins using Docker and you are not able to find the password using the command :

```bash

$ sudo cat /Users/Shared/Jenkins/Home/secrets/initialAdminPassword
Then do following steps :

Type in your command prompt : docker ps
Find the running containerID
Type docker exec -it <containerID> bash
Type cd /var/jenkins_home/secrets
Type cat initialAdminPassword
```



then run the tests file by adding pipeline to the jenkins instance host :) 

you should see that the jenkis is posting results back 