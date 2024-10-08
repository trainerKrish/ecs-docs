- git init
- git status
- git add <file-name> / git add .
- git commit -m "\<MESSAGE\>"
- git log

# Branching
- git branch - show the list of branches
- git branch <new-branch-name> - create a new branch
- git checkout <branch-name> - switch to the specified branch

# Merging
- // Switch to the target branch
- git merge <source-branch>

### Example
- git checkout main
- git merge feature


- git pull origin main
- git push origin main

# Docker commands
- docker image ls


image-pendrive
container-run the actual os.

### Build Docker image
* `docker build --tag <name-of-your-image> <Dockerfile-path>`

### Image
* `docker image ls` # list all the images
* `docker rmi <image-id-1> <image-id-2> ...` # delete one or more images

### Container
* `docker container ls` # list all the running containers
* `docker container ls -a` # list all the available containers
* `docker start <Container-id/Container-Name>` # start a stopped containers
* `docker stop <Container-id/Container-Name>` # stop a runnining containers
* `docker rm <Container-id-1/Container-Name-1> <Container-id-2/Container-Name-2> ...` # delete one or more containers

### Logs
* `docker log <Container-id/Container-Name>` # show the logs from a container


### Run a container
```
create container
 => image
 => command. (python app.py)
 ```

* `docker run <image-name>`
* `docker run -p <hostPort>:<dockerPort> <image-name>` # Attach a port
* `docker run -d <image-name>` # Create a container with Detach mode. This will return container ID as an output.
* `docker run -it <image-name>` # attach an interactive terminal
* `docker run --name <name-of-your-container> <image-name>` # Create container with custom name

### Attach a different terminal to a running container
* `docker exec -it aa2b2be8dd26 bash`

### Volume

### Network

### test