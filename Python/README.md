I recently had to upgrade from Python 2.7.x to 2.7.y so I downloaded the tar ball, followed the README then upgraded the virtualenv.
I also need to update the virtualenv in my project directory.
$curl https://www.python.org/ftp/python/2.7.8/Python-2.7.8.tar.xz | tar xf
$./configure
$./make
$sudo make install
$sudo pip install virtualenv --upgrade
