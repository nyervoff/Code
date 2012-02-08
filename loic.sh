#!/bin/bash
#
# This script installs, updates and runs LOIC on Linux.
#
# Supported distributions:
# * Ubuntu / Debian
# * Fedora
# * openSUSE
#
# Usage: bash install_loic.bash

###COLOURS###

txt_bld=$(tput bold)
bld_red=${txt_bld}$(tput setaf 1)
col_rst=$(tput sgr0)

###GLOBALS###

GIT_REPO=https://github.com/NewEraCracker/LOIC.git
GIT_BRANCH=master

###FUNCTIONS###

ensure_git() #Checks if git is installed, Tries to install it if not
{
type -P git &>/dev/null ||
{
echo -e "${bld_red}Git not found! Attempting to install...${col_rst}"
if [ -f /etc/SuSE-release ] ; then
sudo zypper install git
elif [ -f /etc/lsb-release ] ; then
sudo apt-get install git
elif [ -f /etc/fedora-release ] ; then
sudo yum install git
elif [ -f /etc/debian_version ] ; then
sudo apt-get install git
fi
}
}

is_loic_git()
{
[[ -d .git ]] && grep -q LOIC .git/config
}

is_loic() {
is_loic_git ||
{
[[ -d LOIC ]] && cd LOIC && is_loic_git
}
}

get_loic() {
ensure_git
if ! is_loic ; then
git init
git clone $GIT_REPO -b $GIT_BRANCH
fi
}

compile_loic() {
get_loic
if ! is_loic ; then
echo -e "${bld_red}Error: You are not in a LOIC repository.${col_rst}"
exit 1
else
if [ -f /etc/SuSE-release ] ; then
echo -e "${bld_red}mono-basic, mono-devel, monodevelop and mono-tools not found! Attempting to install...${col_rst}"
sudo zypper install mono-basic mono-devel monodevelop mono-tools
elif [ -f /etc/lsb-release ] ; then
echo -e "${bld_red}monodevelop and liblog4net-cil-dev not found! Attempting to install...${col_rst}"
sudo apt-get install monodevelop liblog4net-cil-dev
elif [ -f /etc/fedora-release ] ; then
echo -e "${bld_red}mono-basic, mono-devel, monodevelop and mono-tools not found! Attempting to install...${col_rst}"
su -c "yum -y install mono-basic mono-devel monodevelop mono-tools"
elif [ -f /etc/debian_version ] ; then
echo -e "${bld_red}monodevelop and liblog4net-cil-dev not found! Attempting to install...${col_rst}"
sudo apt-get install monodevelop liblog4net-cil-dev

fi
fi
mdtool build
}

run_loic() {
is_loic
if [[ ! -e bin/Debug/LOIC.exe ]] ; then
compile_loic
fi
type -P mono &>/dev/null ||
{
echo -e "${bld_red}mono-runtime not found! Attempting to install...${col_rst}"
if [ -f /etc/SuSE-release ] ; then
sudo yum install mono-runtime
elif [ -f /etc/lsb-release ] ; then
sudo apt-get install mono-runtime
elif [ -f /etc/fedora-release ] ; then
su -c "yum -y install mono-core"
elif [ -f /etc/debian_version ] ; then
sudo apt-get install mono-runtime
fi
}
mono bin/Debug/LOIC.exe
}

update_loic() {
ensure_git
if is_loic ; then
git pull --rebase
compile_loic
else
echo -e "${bld_red}Error: You are not in a LOIC repository.${col_rst}"
fi
}

case $1 in
install)
compile_loic
;;
update)
update_loic
;;
run)
run_loic
;;
*)
echo "Usage: $0 "
;;
esac

