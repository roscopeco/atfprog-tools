#!/bin/sh

echo "\x1b[1;37mATF150x Programmer Toolchain Installation\x1b[0m"
echo "\x1b[0;37mCopyright ©2024 The Really Old-School Company Limited\x1b[0m"
echo

ROOT=$(dirname $(readlink -f $0))
if [ ! -w $ROOT ]; then
    echo "\x1b[1;31mThe installation directory is not writeable; Cannot continue.\x1b[0m"
    echo "\x1b[0;31m(ensure $ROOT is a writeable directory)\x1b[0m"
    exit 1
fi

PYTHON=$(command -v python)
[ -z $PYTHON ] && PYTHON=$(command -v python3)
if [ -z $PYTHON ]; then
    echo "\x1b[1;31mA system python is required to install; Please install it and try again.\x1b[0m"
    echo "\x1b[0;31m(try 'brew install python' or 'sudo apt-get install python')\x1b[0m"
    exit 1
fi

INNOEX=$(command -v innoextract)
if [ -z $INNOEX ]; then
    echo "\x1b[1;31minnoextract is required to install; Please install it and try again.\x1b[0m"
    echo "\x1b[0;31m(try 'brew install innoextract' or 'sudo apt-get install innoextract')\x1b[0m"
    exit 1
fi

CURL=$(command -v curl)
if [ -z $CURL ]; then
    echo "\x1b[1;31mcurl is required to install; Please install it and try again.\x1b[0m"
    echo "\x1b[0;31m(try 'brew install curl' or 'sudo apt-get install curl')\x1b[0m"
    exit 1
fi

UNZIP=$(command -v unzip)
if [ -z $UNZIP ]; then
    echo "\x1b[1;31munzip is required to install; Please install it and try again.\x1b[0m"
    echo "\x1b[0;31m(try 'brew install unzip' or 'sudo apt-get install unzip')\x1b[0m"
    exit 1
fi

YOSYS=$(command -v yosys)
if [ -z $YOSYS ]; then
    echo "\x1b[1;31myosys is required for verilog support; Please install it and try again.\x1b[0m"
    echo "\x1b[0;31m(https://github.com/YosysHQ/oss-cad-suite-build/releases)\x1b[0m"
    exit 1
fi

WINE=$(command -v wine)
if [ -z $WINE ]; then
    echo "\x1b[1;31mwine is required for Microchip fitters; Please install it and try again.\x1b[0m"
    echo "\x1b[0;31m(try 'brew install wine' or 'sudo apt-get install wine')\x1b[0m"
    exit 1
fi

echo "\x1b[0;37mFound Curl         : \x1b[1;32m$CURL\x1b[0m"
echo "\x1b[0;37mFound Python       : \x1b[1;32m$PYTHON\x1b[0m"
echo "\x1b[0;37mFound Innoextract  : \x1b[1;32m$INNOEX\x1b[0m"
echo "\x1b[0;37mFound Unzip        : \x1b[1;32m$UNZIP\x1b[0m"
echo "\x1b[0;37mFound Yosys        : \x1b[1;32m$YOSYS\x1b[0m"
echo "\x1b[0;37mFound Wine         : \x1b[1;32m$WINE\x1b[0m"
echo

if [ $# -ne 0 ]; then
    PROCHIP_INSTALLER=$(readlink -f $1)
fi
if [ ! -z $PROCHIP_INSTALLER ]; then
    if [ ! -f $PROCHIP_INSTALLER ]; then
        echo "\x1b[1;31mERROR: ProChip5 installer file $PROCHIP_INSTALLER not found. Will attempt download.\x1b[0m" 
        PROCHIP_INSTALLER=""
    else
        echo "\x1b[1;32m    • \x1b[1;37mUsing ProChip5 installer file $PROCHIP_INSTALLER\x1b[0m" 
    fi
fi
if [ -z $PROCHIP_INSTALLER ]; then
    echo "\x1b[0;34m    🛜  \x1b[1;37mDownloading ProChip5.0.1...\x1b[0m"

    PROCHIP_INSTALLER=`mktemp`
    $CURL -L --fail --progress-bar -o $PROCHIP_INSTALLER http://ww1.microchip.com/downloads/en/DeviceDoc/ProChip5.0.1.zip
    curl_exit=$?
    if [ $curl_exit != 0 ]; then
        echo "\x1b[1;31mERROR: Unable to download ProChip5 installer files. Please download from:\x1b[0m" 
        echo
        echo "\x1b[0;31m    https://www.microchip.com/prochiplicensing/#/\x1b[0m"
        echo
        echo "\x1b[1;31mand the restart this installer, passing the path to the downloaded zip file."
        rm -rf $PROCHIP_INSTALLER
        exit 2
    fi
    DELETE_PCINST=1
fi

echo -n "\x1b[A\r\x1b[2K\r"
echo "\x1b[0;34m    💾 \x1b[1;37mInstalling... \x1b[0;37mThis may take a little while...\x1b[0m"
echo "\x1b[0;34m        • \x1b[1;36mInstalling Microchip fitters...\x1b[0m"


TEMP_DIR=`mktemp -d`
if [ ! -d $TEMP_DIR ]; then
    echo "\x1b[1;31mCould not create a temporary directory!\x1b[0m"
    echo "\x1b[0;31m(Check there is enough free space and the temporary directory is writeable)\x1b[0m"
    exit 3
fi

VEND_DIR=$ROOT/.vendor/microchip

$UNZIP -qq -d $TEMP_DIR $PROCHIP_INSTALLER
$INNOEX -s -d $TEMP_DIR -I app/Prochip/pldfit/aprim.lib -I app/Prochip/pldfit/atmel.std -I app/Prochip/pldfit/fit1502.exe -I app/Prochip/pldfit/fit1504.exe -I app/Prochip/pldfit/fit1508.exe $TEMP_DIR/ProChip5_setup.exe

mkdir -p $VEND_DIR

cp $TEMP_DIR/app/Prochip/pldfit/* $VEND_DIR
cp $VEND_DIR/fit1502.exe $VEND_DIR/find1502.exe
cp $VEND_DIR/fit1504.exe $VEND_DIR/find1504.exe
cp $VEND_DIR/fit1508.exe $VEND_DIR/find1508.exe

if [ ! -z $DELETE_PCINST ]; then
    rm -rf $PROCHIP_INSTALLER
fi
rm -rf $TEMP_DIR

echo "\x1b[0;34m        • \x1b[1;36mCreating python environment...\x1b[0m"
$PYTHON -m venv .venv

echo "\x1b[0;34m        • \x1b[1;36mInstalling Python requirements...\x1b[0m"
source .venv/bin/activate
pip -q -q -q install -r requirements.txt
deactivate

echo
echo "\x1b[0;32m    ✅ \x1b[1;37mInstallation complete!\x1b[0m"
echo
echo
exit 0
