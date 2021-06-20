import logging
import os
from datetime import datetime


def main():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

    unreachable_lst = []
    data = []
    now = datetime.now()
    datetime_now = now.strftime("%d/%m/%Y, %H:%M")

    if os.path.exists('env_info.txt'):
        with open('env_info.txt', 'r') as f:
            data = f.readlines()
    else:
        logging.warning("File not found: env_info.txt")

    if os.path.exists('unreachable.txt'):
        logging.info("File with unreachable hosts list was found")
        with open('unreachable.txt', 'r') as f:
            unreachable_lst = f.readlines()
            logging.info(f"Unreachable list: {unreachable_lst}")

    with open('report.html', 'w') as f:
        # Insert header
        f.write(f"<h1>Report date time: {datetime_now}</h1>")
        for line in data:
            f.write("<p>%s</p>" % line.replace('\n', ' '))
            if line.startswith("\n"):
                f.write("<br>")

        if len(unreachable_lst) > 0:
            f.write("<h2 style='color:red'>Unreachable Hosts:</h2>")
            for u in unreachable_lst:
                f.write("<p>%s</p>" % u.replace('\n', ' '))

    logging.info("Python script finished")
    

if __name__ == '__main__':
    main()
