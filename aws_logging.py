import logging

from docker.models.containers import Container
from cloudwatch import cloudwatch

def logging_to_aws(
        container: Container,
        log_group: str,
        log_stream: str,
        access_id: str,
        access_key: str,
        region: str
):
    #set logger
    logger = logging.getLogger('test_task')
    formatter = logging.Formatter('%(message)s')
    handler = cloudwatch.CloudwatchHandler(
        log_group=log_group,
        log_stream=log_stream,
        access_id=access_id,
        access_key=access_key,
        region=region
        )
    handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    
    # start logging
    print('Start logging...')
    for line in container.logs(stream=True, follow=True):
        log_line = line.decode("utf-8").strip()
        print(log_line)
        logger.info(log_line)