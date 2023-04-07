#/bin/bash
#
#
workdir="/home/han/Disk/Document/PROJECT/Python/InsertFormula"
source "$workdir/myenv/bin/activate"

#echo "Error: you have to config the app_id and app_key!"
#exit 1
#APP_ID="your app id"
#APP_KEY="your app key"


cd $workdir

if [ ! -d "out_files" ]; then
	mkdir "out_files"
fi


python main.py



