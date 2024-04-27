## Additional CPLD tools

In this repository, you will also find some (_very_ WIP) tools for writing 
CPLD code for the ATF150x range on non-Windows operating systems, using 
Yosys and the Atmel fitters under Wine. 

This is **not** currently "official" or "supported" but does _basically_ work,
at least on macOS.

Have a look at the `install.sh` script to get started - if you run it, it
will check you have the relevant prerequisites installed, and will try
to set things up for you.

If that succeeds, you should be able to use e.g:

```shell
./atf_compile_v test_cpld/toggle
```

to compile the (extremely simple!) test verilog under the `test_cpld` 
directory.