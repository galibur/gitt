#!/usr/bin/env python3

# Name      : Log.py
# Author    : galibur
# Version   : 0.1
# Date      : 2022-02-14
# Decription: Provide log functionality

# Get caller method
import inspect

# Colorize terminal text
from sty import fg, bg, ef, rs

class Log:

    def __init__(self):
        self.version = 0.1

        # True: show all (also debug) logs; False: do not show debug logs.
        self.debug = True

        self.log('Log initialized', 6)

        
    def log(self, message, level=0, debug=0):
        
        if debug == 1 and self.debug == False:
            return

        # Get caller class and method name:
        caller = False
        try:         
            stack = inspect.stack()
            the_class = stack[1][0].f_locals["self"].__class__.__name__
            the_method = stack[1][0].f_code.co_name

            caller = "{}.{}()".format(the_class, the_method)
        
        except Exception as e:                    
            if hasattr(e, 'message'):
                print('ERROR : ' + str(e.message))
            else:
                print('ERROR : ' + str(e))



        if level == 0:
            prefix = fg.white + "INFO  : "            

        elif level == 1:
            prefix = fg.orange + 'WARN  : '

        elif level == 2:
            prefix = fg.red + 'ERROR : '

        elif level == 3:
            prefix = fg.red + 'FATAL : '

        elif level == 4:
            prefix = fg.green + 'RESULT: '

        elif level == 5:
            prefix = fg.blue + 'TODO  : ' 

        elif level == 6:
            prefix = fg.green + 'DONE  : '               

        elif level == 7:
            prefix = fg.green + 'OK    : '

        elif level == 8:
            prefix = fg.yellow + 'ON IT : '

        else:
            prefix = fg.white + 'MISC  : '

        postfix = fg.white + ''


        #print('STATUS: ' + str(self.debug))

        if self.debug:
            print(str(prefix) + ' ' + str(caller) + ' : ' + str(message) + str(postfix))
        else:
            print(str(prefix) + ' ' + str(message) + str(postfix))
