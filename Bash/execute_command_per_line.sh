if [ $# -ne 2 ]
then
   echo "Usage: execute_command_per_line command filename"
   exit 1
fi

command=$1
filename=$2

while read line
do
   $command $line
done < $filename
