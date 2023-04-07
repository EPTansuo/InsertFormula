#/usr/bin/python
import sys
import os
import time
import json
import pyperclip
import mathpix
import imageproc
import subprocess
import multiprocessing
from pynput import keyboard 
from shutil import copyfile



def runXournalpp(filename):
    xournalpp_proc = subprocess.Popen(["xournalpp",filename+".xopp"])
    return xournalpp_proc

def mathpixAPI(filename):
    r = mathpix.latex({
        'src': mathpix.image_uri(filename+".jpg"),
        'ocr':['math','text'],
        'formats': ['latex_styled'],
        'format_options': {
            'text': { 'transforms': ['rm_spaces', 'rm_newlines']},
            'latex_styled': {'transforms': ['rm_spaces']}
        }
    })
    print(json.dumps(r, indent=4, sort_keys=True))
    latex_str = r['latex_styled']
    print(latex_str)
    pyperclip.copy("\n$$\n"+latex_str+"\n$$\n")



def onHotKeyPressed(filename,xournalpp_proc):
    print("Press Ctrl+S")
    time.sleep(0.4)
    xournalpp_proc.terminate()
    os.system("xournalpp "+filename+".xopp "+"-i " +
              filename+".png")
    imageproc.proc(filename)
    mathpixAPI_p = multiprocessing.Process(target=mathpixAPI,args=(filename,))
    mathpixAPI_p.start()
    exit(0)

def main() -> int:
    print("hello")
    print("app_id:"+os.getenv("APP_ID"))
    print("app_key:"+os.getenv("APP_KEY"))
    time_str = time.strftime("%Y%m%d%H%M%S")
    filename = "./out_files/"+time_str
    copyfile("note.xopp",filename+".xopp")
    
    xournalpp_proc = runXournalpp(filename); 

    with keyboard.GlobalHotKeys({
        '<ctrl>+s':lambda: onHotKeyPressed(filename,xournalpp_proc)}) as h:
        h.join()

    time.sleep(2);
    print("run over")
    return 0

if __name__ == '__main__':
    sys.exit(main())
