
import os

##LOOPING CONDITION

while True:
    
    print('WHAT WOULD YOU LIKE TO RUN: ' , end = '')
    stm = input()
    
    if (("run" in stm) or ("start" in stm) or ("initiate" in stm) or ("initialize" in stm) or ('open' in stm) or ('execute' in stm)) and (("chrome" in stm) or ("browser" in stm)):
        os.system("chrome")
    elif (('run' in stm) or ('start' in stm) or ('initiate' in stm) or ('initialize' in stm) or ('open' in stm) or ('execute' in stm)) and (('edge' in stm) or ('msedge' in stm) or ('default browser' in stm)):
        os.system('msedge')    
    elif (('run' in stm) or ('start' in stm) or ('initiate' in stm) or ('initialize' in stm) or ('open' in stm) or ('execute' in stm)) and (('vlc' in stm) or ('player' in stm)):
        os.system('vlc')
    elif (('run' in stm) or ('start' in stm) or ('initiate' in stm) or ('initialize' in stm) or ('open' in stm) or ('execute' in stm)) and ((('media' in stm) and ('player' in stm)) or ('player' in stm) or ('wmplayer' in stm)):
        os.system('wmplayer')        
    elif (('run' in stm) or ('start' in stm) or ('initiate' in stm) or ('initialize' in stm) or ('open' in stm) or ('execute' in stm)) and (('spotify' in stm) or ('music' in stm) or ('music player' in stm)):
        os.system('spotify')
    elif (('run' in stm) or ('start' in stm) or ('initiate' in stm) or ('initialize' in stm) or ('open' in stm) or ('execute' in stm)) and (('putty' in stm)):
        os.system('putty')
    elif (('run' in stm) or ('start' in stm) or ('initiate' in stm) or ('initialize' in stm) or ('open' in stm) or ('execute' in stm)) and ('slack' in stm):
        os.system('slack')  
    elif (('run' in stm) or ('start' in stm) or ('initiate' in stm) or ('initialize' in stm) or ('open' in stm) or ('execute' in stm)) and (('texteditor' in stm) or ('editor' in stm) or ('notepad' in stm)):
        os.system('notepad')
    elif (('run' in stm) or ('start' in stm) or ('initiate' in stm) or ('initialize' in stm) or ('open' in stm) or ('execute' in stm)) and (('ide' in stm) or (('visual' in stm) and ('studio' in stm)) or ('vscode' in stm)):
        os.system('code')
    elif (('run' in stm) or ('start' in stm) or ('initiate' in stm) or ('initialize' in stm) or ('open' in stm) or ('execute' in stm)) and (('idm' in stm) or (('download' in stm) and ('manager' in stm))):
        os.system('idman')  
    elif (('run' in stm) or ('start' in stm) or ('initiate' in stm) or ('initialize' in stm) or ('open' in stm) or ('execute' in stm)) and (('zoom' in stm) or (('zoom' in stm) and ('meeting' in stm))):
        os.system('zoom')        
    elif (('run' in stm) or ('start' in stm) or ('initiate' in stm) or ('initialize' in stm) or ('open' in stm) or ('execute' in stm)) and ( ('picasa3' in stm) or ('picasa' in stm) or ( ('google' in stm) and ('picasa' in stm) ) or ( ('photo' in stm) and ('editor' in stm) ) ):
        os.system('picasa3')  
    elif (('run' in stm) or ('start' in stm) or ('initiate' in stm) or ('initialize' in stm) or ('open' in stm) or ('execute' in stm)) and ( (('oracle' in stm) and (('virtual' in stm) and ('box' in stm))  or ('vbox' in stm)) or (('virtual' in stm) and ('box' in stm))):
        os.system('virtualbox')        
    elif (('run' in stm) or ('start' in stm) or ('initiate' in stm) or ('initialize' in stm) or ('open' in stm) or ('execute' in stm)) and ((('panel' in stm) and ('cpanel' in stm)) or (('control' in stm) and ('panel' in stm))):
        os.system('control panel')      
    elif (('run' in stm) or ('start' in stm) or ('initiate' in stm) or ('initialize' in stm) or ('open' in stm) or ('execute' in stm)) and ((('settings' in stm) and ('setting' in stm)) or (('windows' in stm) and ('settings' in stm))):
        os.system('start ms-settings:')                           
    elif (('run' in stm) or ('start' in stm) or ('initiate' in stm) or ('initialize' in stm) or ('open' in stm) or ('execute' in stm)) and ((('this' in stm) and ('pc' in stm)) or (('file' in stm) and ('explorer' in stm)) or (('my' in stm) and ('computer' in stm))):
        os.system('explorer')
    elif (('run' in stm) or ('start' in stm) or ('initiate' in stm) or ('initialize' in stm) or ('open' in stm) or ('execute' in stm)) and ((('c' in stm) and ('drive' in stm)) or (('root' in stm) and ('directory' in stm))):
        os.system('explorer c:')      
    elif (('run' in stm) or ('start' in stm) or ('initiate' in stm) or ('initialize' in stm) or ('open' in stm) or ('execute' in stm)) and ((('e' in stm) and ('drive' in stm)) or (('e' in stm) and ('directory' in stm))):
        os.system('explorer e:')                 
    elif (('run' in stm) or ('start' in stm) or ('initiate' in stm) or ('initialize' in stm) or ('open' in stm) or ('execute' in stm)) and ((('f' in stm) and ('drive' in stm)) or (('f' in stm) and ('directory' in stm))):
        os.system('explorer f:')     
    elif (('run' in stm) or ('start' in stm) or ('initiate' in stm) or ('initialize' in stm) or ('open' in stm) or ('execute' in stm)) and (('calculator' in stm) or ('calc' in stm)):
        os.system('calc')              
    elif (('stop' in stm) or ('exit' in stm) or ('quit' in stm) or ('close' in stm)):
        break
    else:
        print('INVALID STATEMENT')





