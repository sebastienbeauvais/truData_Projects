import platform
import subprocess

from StoreItems import #...
from Coupon import #...
from Basket import #...
  

def clear_screen():
    """clears terminal screen before starting"""

    # Clear command as function of OS
    command = "cls" if platform.system().lower() == "windows" else "clear"

    # Action
    return subprocess.call(command) == 0

def main():
    # do something

if __name__ == "__main__":
    main() 

            