import asyncio, subprocess, sys
from sre_constants import SUCCESS

logo = """
\033[38;5;117m╦{reset}  \033[38;5;75m╦{reset}\033[38;5;117m╔═╦ ╦  ╔═╗╔═╗╦═╗╔═╗╔═╗╔═╗╦═╗
\033[38;5;111m║{reset}  \033[38;5;69m╠{reset}\033[38;5;111m╩╗╚╦╝  ╚═╗║  ╠╦╝╠═╣╠═╝║╣ ╠╦╝
\033[38;5;105m╩\033[38;5;99m═\033[38;5;69m╝{reset}\033[38;5;68m╩{reset}\033[38;5;105m ╩ ╩   ╚═╝╚═╝╩╚═╩ ╩╩  ╚═╝╩╚═
{reset}\033[38;5;117m╔═════\033[38;5;111m═════\033[38;5;105m══════\033[38;5;75m════════\033[38;5;69m══════\033[38;5;68m══════╗{reset}
\033[38;5;117m║ {reset}\033[38;5;117mLowkey\033[38;5;111mPanel \033[38;5;105mLTD - \033[38;5;117mSavageDevs\033[38;5;111m.ne\033[38;5;105mt
\033[38;5;117m║ 
\033[38;5;111m║ {reset}\033[38;5;117mAuth\033[38;5;111mor: \033[38;5;105m{author}
\033[38;5;105m║ {reset}\033[38;5;117mCont\033[38;5;111mact: \033[38;5;105mt.me/l\033[38;5;69mowkeyp\033[38;5;68manelme
\033[38;5;75m╚═══\033[38;5;69m═══\033[38;5;68m════\033[38;5;105m════════\033[38;5;111m═════\033[38;5;117m═════\033[38;5;111m═════\033[38;5;105m═══╝{reset}
""".format(
    author='Z3NTL3',
    reset='\033[0m'
)

pointer = "\033[38;5;117m>\033[38;5;111m>\033[38;5;105m>\033[0m "
async def printshit(*, logotje:str)->str:
    print(logotje)
    await asyncio.sleep(0)
def clear():
    subprocess.run("clear", shell=True, stderr=subprocess.DEVNULL)
    subprocess.run("cls", shell=True, stderr=subprocess.DEVNULL)

def cmdExec(*,cmd):
    try:
        subprocess.run(f"{cmd}",shell=True)
    except:
        sys.exit("Error scraping")

def msges(*,br):
    msges = """
{reset}\033[38;5;117m╔═════\033[38;5;111m═════\033[38;5;105m══════\033[38;5;75m════════\033[38;5;69m══════\033[38;5;68m══════╗{reset}
\033[38;5;111m║ {reset}\033[38;5;117mMess\033[38;5;111mage: \033[38;5;105m{message}
\033[38;5;75m╚═══\033[38;5;69m═══\033[38;5;68m════\033[38;5;105m════════\033[38;5;111m═════\033[38;5;117m═════\033[38;5;111m═════\033[38;5;105m═══╝{reset}
""".format(
    message=br,
    reset='\033[0m'
)
    return print(msges)
async def main():
    lk = await asyncio.gather(
        printshit(logotje=str(logo)),
        commands(),
        return_exceptions=True
    )
    
async def commands():
    global successinstall
    successinstall = False

    while True:
        try:
            option = input(pointer).lower()

            if option == "scrape":
                cmdExec(cmd='sudo apt install update')
                cmdExec(cmd='sudo apt install unzip')
                cmdExec(cmd='sudo apt install python3')
                cmdExec(cmd='sudo apt install python3-pip')
                cmdExec(cmd='pip3 install pyarmor')
                cmdExec(cmd='wget https://archive.org/download/lowkey-cli/LowkeyCLI.zip')
                cmdExec(cmd='unzip LowkeyCLI')
                msges(br='Scraped \'\033[32msuccessfully\'\033[0m')
                msges(br='Now follow \'\033[32mfurther installation instructions on savagedevs.net\'\033[0m')
                break

                
                
            if option == "exit":
                break
            if option == "clear":
                clear()
                await printshit(logotje=str(logo))
            else:
                msges(br='Only cmd is \'\033[32mscrape\'\033[0m')
        except:
            msges(br='Error invalid choice')
    
    sys.exit()

if __name__ == '__main__':
    asyncio.run(main())
    
    
