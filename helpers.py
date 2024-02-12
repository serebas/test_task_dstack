import argparse

def check_arguments(required_arguments: list) -> argparse.Namespace:
    # set arguments
    parser = argparse.ArgumentParser(description='Parser of args')    
    for argument in required_arguments:
        parser.add_argument(argument)

    # parse arguments
    try:
        received_arguments = parser.parse_args()
    except SystemExit:
        raise argparse.ArgumentError(None, "check the spelling of all arguments")
    
    # check received arguments
    for argument in required_arguments:
        argument = argument[2:].replace("-", "_") 
        if not eval(f"received_arguments.{argument}"):
            raise argparse.ArgumentError(None, f"missing required argument --{argument}")
    return received_arguments
        
        