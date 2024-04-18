import logging 

class LogGen:

    @staticmethod
    def loggen():

        logging.basicConfig(filename=".\\Logs\\automation.log")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


#format='%(asctime)s : %(levelname)s: %(message)s', datefmt= '%m %d %Y %I:%M:%S %p'
