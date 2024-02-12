import docker

client = docker.from_env()

def run_container(image: str, bash_command: str):
    #start container
    container = client.containers.run(
        image=image,
        command=bash_command,
        stderr=True,
        detach=True
    )
    return container