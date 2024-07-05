import psutil
import logging

logging.basicConfig(filename= '/Users/sasidharambatipudi/Devops/pyhton_project/cpu_monitor.log',level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

#function to monitor CPU usage
def monitor_cpu(threshold,interval):
    """
    Monitors the CPU usage of the local machine.

    Parameters:
    threshold (int): The CPU usage percentage threshold to trigger an alert.
    interval (int): The interval in seconds to wait between checks.
    """

    logging.info("Monitoring CPU usage....")

    try:
        while True:
            # Get the CPU utilisation percentae with the interval of 1sec
            cpu_usage = psutil.cpu_percent(interval = interval)

            #check if the usage is grater than treshold
            if(cpu_usage>threshold):
                logging.warning(f"ALERT! CPU usage exceeds threshold: {cpu_usage}%") 

            else:
                logging.info(f"CPU usage is {cpu_usage}%")
                
    #catches the user inturruption Exception
    except KeyboardInterrupt:
        logging.error("User inturrupted.Exiting..!")

    #catches general exception if any  
    except Exception as e:
        logging.error(f"Error occured..!{e}")




threshold = 20  #set threshold value
interval = 1  #set interval value

monitor_cpu(threshold,interval)