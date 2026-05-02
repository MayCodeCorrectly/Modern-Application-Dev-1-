import logging

logging.basicConfig(level = logging.INFO, filename= "log.log", filemode="w")

# hierarchy
logging.info("INFO")
logging.debug("debug")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
