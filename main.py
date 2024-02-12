import argparse
import docker
import botocore

from aws_logging import logging_to_aws
from container import run_container
from helpers import check_arguments

required_arguments = [
    '--docker-image',
    '--bash-command',
    '--aws-cloudwatch-group',
    '--aws-cloudwatch-stream',
    '--aws-access-key-id',
    '--aws-secret-access-key',
    '--aws-region',
]

def main():
    # get arguments
    arguments = check_arguments(required_arguments=required_arguments)

    # start container
    container = run_container(image=arguments.docker_image, bash_command=arguments.bash_command)

    # handle the output logs
    logging_to_aws(
        container=container,
        log_group=arguments.aws_cloudwatch_group,
        log_stream=arguments.aws_cloudwatch_stream,
        access_id=arguments.aws_access_key_id,
        access_key=arguments.aws_secret_access_key,
        region=arguments.aws_region
    )

if __name__ == "__main__":
    try:
        main()
        print("Stop logging!")
    except argparse.ArgumentError as e:
        print(f"Error in command line arguments: {e}")
    except docker.errors.DockerException as e:
        print(f"Error when starting container: {e}")
    except botocore.exceptions.BotoCoreError as e:
        print(f"Connection error: {e}. Probably provided invalid credentials")
    except KeyboardInterrupt:
        print("Logging interrupted!")