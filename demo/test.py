from modules.configEmail import EMailInstrument as emi
import os
from modules.most_new_log import NewLog

if __name__ == '__main__':
    send = emi.get_email()
    send.send_email()