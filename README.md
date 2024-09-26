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

create container
 => image
 => command. (python app.py)

### Build Docker image
* `docker build --tag <name-of-your-image> <Dockerfile-path>`

### Image
* `docker image ls` # list all the images

### Container
* `docker container ls` # list all the running containers
* `docker container ls -a` # list all the available containers

### Logs
* `docker log <Container-id/Container-Name>` # show the logs from a container
