
banner ='''\033[92m                                                                       
                                                                        
 ##   ##  #######  ##   ##  #######  #######  #######  #######  ######  
 ##  ##            ##   ##       ##       ##       ##       ##       ## 
 #####    ####     #######  ######   ##   ##  #######  #######  ##   ## 
 ##  ##   ##            ##  ##   ##  ##   ##  ##   ##  ##  ##   ##   ## 
 ##   ##  #######  #######  #######  #######  ##   ##  ##   ##  ######  
                                                                                                                             

########  #######  ####### ########  #######  ####### 
   ##                         ##                   ##     \033[91m bY \033[92m
   ##     ####     #######    ##     ####     #######       \033[91m ADITHYA \033[92m
   ##     ##            ##    ##     ##       ##  ##  
   ##     #######  #######    ##     #######  ##   ## 
\033[93m
Press Any Key to Test Your Keyboard...
Press ESC to Exit ! \033[34m

                                                     '''

import keyboard
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def key_tester():
    clear()
    print(banner)

    while True:
        try:
            key_event = keyboard.read_event()
            
            if key_event.event_type == keyboard.KEY_DOWN:
                key_name = key_event.name
                clear()
                print(banner)
                print(f"You pressed the key: \033[91m {key_name.upper()}")

                if key_name == 'esc':
                    break

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    key_tester()
