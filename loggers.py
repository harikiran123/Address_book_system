import logging

logging.basicConfig(
    filename="address_book.log", 
    level=logging.DEBUG,          
    format="%(asctime)s - %(levelname)s - %(message)s",  
    datefmt="%Y-%m-%d %H:%M:%S"  
)
logger = logging.getLogger(__name__)
