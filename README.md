# Little ATF150x Programmer Board
## Software utilities

### What

This repository contains the official standard programmer software and utilities 
for the Little ATF150x Programmer Board.

![Picture of The Little ATF150x Programmer](https://github.com/roscopeco/atfprog-tools/raw/main/images/board.jpeg)

This is a plug-and-play USB-connected programmer and breakout board for
Atmel (Microchip) ATF150{2,4,8}{AS,ASV} CPLDs, featuring:

* Support for JED, SVF or XSVF files
* Support for both PLCC44 and 84 packages on-board
* Ability to drive ICSP via the JTAG headers (single-device only - chains **not** currently supported)
* Ability to erase JTAG-locked and secured devices

The board is **now available** on the on the [rosco_m68k store](https://store.rosco-m68k.com/products/little-atf-programmer) 🥳

### Software Installation

Prerequisites:

* Recent macOS, Linux or Windows operating system
* Working Python (3.9+) installation
  * Recent macOS and Linux will likely have this by default
  * If not, it can be installed with your package manager
  * Windows users can download from https://www.python.org/downloads/windows
  * `python` and `pip` should be in your `PATH` for easiest installation experience

> **Note**: on some systems, your `python` may instead be named `python3`, with `pip`
> being similarly named `pip3`. As long as Python is version 3.9 or higher 
> (as reported by `python3 --version`) it should work just fine.

#### Latest release

With a Python environment that meets these requirements, installation
is as simple as:

```shell
pip install little-atf-programmer
```

> **Note**: on Windows, when installing you may receive a message from pip
> warning that the installed binaries are not in your `PATH`. If you see this,
> for easier installation you may wish to add the directory in the warning
> to your `PATH` by editing in
> `Control Panel / System / Advanced / Environment Variables.`

#### From source

Developers and project collaborators may wish to install from source. 

To do this, clone the project from GitHub (or grab a source tarball).

Then either run `python src/atfu.py` or install with pip if you like:

```shell
pip install .
```

If you're hacking on the code, you'll probably want to install it `--editable`.

### Usage

#### General arguments

General command line arguments look like this:

```
atfu [-h] [--version] [-q] [-v] [-t] {program,erase,check,programmer} ...

Little ATF150x Programmer Board Utility

positional arguments:
  {scan,program,erase,check,verify,programmer}
    scan                Scan for ATF150x devices
    program             Program an ATF150x device
    erase               Erase an ATF150x device
    check               Check if an ATF150x device is blank
    verify              Verify an ATF150x device
    programmer          Little ATF150x Programmer Board device functions

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -q, --quiet           Silence almost all output
  -v, --verbose         Allow additional output
  -t, --trace           Enable debugging output (can be noisy!)
```

#### Device scan mode

This mode is used to scan the connected ATF CPLD, and try to autodetect the specific
type of the chip.

By default, the first detected programmer will be used. This can be changed
with the `-p` option.

The `-n` option can be used to obtain unadorned output. This can be useful for
passing to other commands, or to `atfu` itself if you want to work with whatever
device is detected, e.g.

```shell
atfu program -d $(atfu scan -n) my_file.jed
```

Usage: 

```
atfu scan [-h] [-n] [-p PROGRAMMER]

options:
  -h, --help            show this help message and exit
  -n, --plain           Plain output, only the unadorned device name, no newline
  -p PROGRAMMER, --programmer PROGRAMMER
                        Programmer device (default: <detected>)
```
#### Program mode

This mode is used to program JEDEC, SVF or XSVF files to an ATF150x device.

By default, the first detected programmer will be used. This can be changed
with the `-p` option.

If you have problems programming, try erasing first with the `-e` option,
or force-erasing with the `-f` option, which can be useful when you have a
JTAG-locked or secured device.

```
atfu program [-h] [-e] [-f] [-d {ATF1502,ATF1504,ATF1508}] [-p PROGRAMMER] filename [filename ...]

positional arguments:
  filename              .jed, .svf or .xsvf file(s) to program

options:
  -h, --help            show this help message and exit
  -e, --erase           Erase before programming
  -f, --force           Force-erase before programming (implies -e)
  -d {ATF1502AS,ATF1504AS,ATF1508AS,ATF1502ASV,ATF1504ASV,ATF1508ASV}, --device {ATF1502AS,ATF1504AS,ATF1508AS,ATF1502ASV,ATF1504ASV,ATF1508ASV}
                        Device to program (default: ATF1502AS)
  -p PROGRAMMER, --programmer PROGRAMMER
                        Programmer device (default: <detected>)
```

#### Erase mode

This mode is used to erase an ATF150x device, and can also be used to 
force erase JTAG-locked or secured devices.

By default, the first detected programmer will be used. This can be changed
with the `-p` option.

> **Note** that the force mode might be... _stressful_ for your device, 
> so try a regular erase first :)

```
atfu erase [-h] [-f] [-p PROGRAMMER] [-d {ATF1502,ATF1504,ATF1508}]

options:
  -h, --help            show this help message and exit
  -f, --force           Force erase
  -p PROGRAMMER, --programmer PROGRAMMER
                        Programmer device (default: <detected>)
  -d {ATF1502AS,ATF1504AS,ATF1508AS,ATF1502ASV,ATF1504ASV,ATF1508ASV}, --device {ATF1502AS,ATF1504AS,ATF1508AS,ATF1502ASV,ATF1504ASV,ATF1508ASV}
                        Device to erase (default: ATF1502AS)
```

#### Check mode

This mode is used to determine whether an ATF150x device is blank.

By default, the first detected programmer will be used. This can be changed
with the `-p` option.

```
atfu check [-h] [-p PROGRAMMER] [-d {ATF1502,ATF1504,ATF1508}]

options:
  -h, --help            show this help message and exit
  -p PROGRAMMER, --programmer PROGRAMMER
                        Programmer device (default: <detected>)
  -d {ATF1502AS,ATF1504AS,ATF1508AS,ATF1502ASV,ATF1504ASV,ATF1508ASV}, --device {ATF1502AS,ATF1504AS,ATF1508AS,ATF1502ASV,ATF1504ASV,ATF1508ASV}
                        Device to check (default: ATF1502AS)
```

#### Verify mode

This mode is used to verify the contents of an ATF150x device against a JESD3-C (.jed) file.

By default, the first detected programmer will be used. This can be changed
with the `-p` option.

**Verification cannot be performed against SVF or XSVF files**. The expectation for those is that
verification would be encoded into the vectors themselves.

```
atfu verify [-h] [-d {ATF1502,ATF1504,ATF1508,ATF1502AS,ATF1504AS,ATF1508AS,ATF1502ASV,ATF1504ASV,ATF1508ASV}] [-p PROGRAMMER] filename [filename ...]

positional arguments:
  filename              .jed file(s) to verify against

options:
  -h, --help            show this help message and exit
  -d {ATF1502,ATF1504,ATF1508,ATF1502AS,ATF1504AS,ATF1508AS,ATF1502ASV,ATF1504ASV,ATF1508ASV}, --device {ATF1502,ATF1504,ATF1508,ATF1502AS,ATF1504AS,ATF1508AS,ATF1502ASV,ATF1504ASV,ATF1508ASV}
                        Device to verify (default: ATF1502AS)
  -p PROGRAMMER, --programmer PROGRAMMER
                        Programmer device (default: <detected>)
```

#### Programmer mode

This mode can be used to list detected programmer boards, and query them.

```
atfu programmer [-h] {list,query} ...

positional arguments:
  {list,query}

options:
  -h, --help    show this help message and exit


atfu programmer list [-h] [--plain]

Functions for listing connected programmers

options:
  -h, --help   show this help message and exit
  -n, --plain  Display a plain list of device paths
```

### Copyright

Copyright ©2024 [The Really Old-School Company Limited](https://rosco_m68k.com).

Portions Copyright (C) 2019-2020 whitequark@whitequark.org

Portions Copyright (c) 2015 Marcelo Roberto Jimenez <marcelo.jimenez (at) gmail (dot) com>

Portions Copyright 2008, SoftPLC Corporation  http://softplc.com [Dick Hollenbeck dick@softplc.com]

Mostly MIT License, portions under other licenses - see LICENSE.md & source code comments.


