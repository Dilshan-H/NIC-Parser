import calendar
import re
from datetime import datetime

def id_2_bday(nic):
    
    """
    Parse standard identity card numbers (NIC numbers) in Sri Lanka and return
    Gender, Birthday of the NIC holder.
    - Old NIC pattern >> 861473487V
    - New NIC pattern >> 198614703487
    """
    
    validIds = re.findall(r"\d{9}[vVxX]|\d{12}", nic)

    if len(validIds) == 0:
        return("No valid NIC numbers found!")
    else:
        for nic in validIds:
            nicType = 'NEW' if len(nic) == 12 else 'OLD'
            try:
                if nicType == 'NEW':
                    dateTag = int(nic[4:7])
                    gender = 'Male' if dateTag < 500 else 'Female'
                    if not calendar.isleap(int(nic[:4])) and dateTag > 59:
                        dateTag -= 1
                    if gender == 'Male':
                        birthday = datetime.strptime(f'{dateTag},{nic[:4]}','%j,%Y')
                    elif gender == 'Female':
                        birthday = datetime.strptime(f'{dateTag - 500},{nic[:4]}','%j,%Y')
                    return(nicType, gender, str(birthday.date()))
                else:
                    dateTag = int(nic[2:5])
                    gender = 'Male' if dateTag < 500 else 'Female'
                    if not calendar.isleap(int(nic[:4])) and dateTag > 59:
                        dateTag -= 1
                    if gender == 'Male':
                        birthday = datetime.strptime(f'{dateTag},{"19" + nic[:2]}','%j,%Y')
                    elif gender == 'Female':
                        birthday = datetime.strptime(f'{dateTag - 500},{"19" + nic[:2]}','%j,%Y')
                    return(nicType, gender, str(birthday.date()))
            except:
                return("Error occurred while processing the NIC number.\nCheck the ID number again!\n---- Ex:861473487V OR 198614703487 ----")

if __name__ == '__main__':
    nic = input("Enter NIC/ID number: ")
    print(id_2_bday(nic))
