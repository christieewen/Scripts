I recently had to upgrade from Python 2.7.x to 2.7.y so I downloaded the tar ball, followed the README then upgraded the virtualenv.
I also need to update the virtualenv in my project directory.

First install dependencies
sudo apt-get install build-essential
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

$wget https://www.python.org/ftp/python/2.7.8/Python-2.7.8.tar.xz | tar xf
$./configure
$./make
$sudo make install
$sudo pip install virtualenv --upgrade


REFERENCES
Follow these directions using apt-get instead of installing the hard way:
http://askubuntu.com/questions/101591/how-do-I-install-python-2-7-2-on-ubuntu

http://askubuntu.com/questions/50870/how-do-i-update-virtualenv

Using different python version with virtualenv
http://stackoverflow.com/questions/1534210/use-different-python-version-with-virtualenv

