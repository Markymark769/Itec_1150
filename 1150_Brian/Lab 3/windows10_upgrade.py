"""
Name: Mark Porraz
Date: 7/1/2024
Program: windows10 upgrade.py


 - at least 1 GHz, 64-bit processor with 2 cores
 - at least 4 GB of memory
 - at least 64 GB of storage space
 - a motherboard with a TPM chip
 - a motherboard with UEFI Secure Boot firmware currently installed with Windows 10 at version 2004 or greater

"""
# def main():
#     processor, cores, memory, storage, TPM_chip, UEFI, secure_boot, ver = input()
#     total = processing(processor, cores, memory, storage, TPM_chip, UEFI, secure_boot, ver)
# def inputs():
#     processor = input('What is your current processor speed?')
#     cores = input('what is the number of cores do you have?')
#     memory = input('What is the amount of memory you have on your computer?')
#     storage = input('What is the amount of storage you have on your computer?')
#     TPM_chip = input('Do you have a TPM chip?')
#     UEFI = input('Do you have a have a UEFI motherboard?')
#     secure_boot = input('Do you have a Secure Boot enabled?')
#     ver = input('What version of Windows are you currently running? ')
#     return processor, cores, memory , storage, TPM_chip, UEFI, secure_boot, ver
#
#
# def processing(processor, cores, memory, storage, TPM_chip, UEFI, secure_boot, ver):
#     memory >= 2 and speed >= 1.6 and os.lower() in ['windows 8', 'windows xp', 'windows 7']
#     return total
#
# def outputs():

# version 2
# this version asks:
#- How much RAM in GB does your system have?
#- What is the GHz clock speed of your processor?
#- What version of Windows are you currently running?


def upgrade(memory, speed, os):
    return memory >= 2 and speed >= 1.6 and os.lower() in ['windows 8', 'windows xp', 'windows 7']


mem = int(input('How much RAM in GB does your system have? '))
clock = float(input('What is the GHz clock speed of your processor? '))
ver = input('What version of Windows are you currently running? ')
if upgrade(mem, clock, ver):
    print('You can upgrade to Windows 10!')
else:
    print('Sorry, you cannot upgrade.')
