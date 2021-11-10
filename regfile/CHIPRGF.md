
# CHIPRGF app

this app intended to produce all register files documentation under the same the same roof.

## activation

chiprgf.py base.regfile  $DIR1/rgf1.regfile  $DIR2/rgf2.regfile $DIR3/rgf3.regfile


first param must be the global config file. after that all regfiles in a chip. Notice if some of them have multiple instances, this will be treated in global config file.

Notice that running this script produces actual regfile files, but we use only MD files to create top level document.  

Depending on Your flow, these local produced files can be used or discraded (in case they are already produced by designers elsewhere).

## global config file
here we call it base.regfile, but any other name is fine.

it is simple: here example:

`rgf plug_rgf   base=0x10000 instance=plug_rgf1`
`rgf plug_rgf   base=0x20000 instance=plug_rgf2`
`rgf nex_b_rgf  base=0x30000 instance=nex_rgf`

If the rgf is used once, no need to add instance name. Base is a must.   I can, but it is dangerous for me to compute the base by myself, for example by concating the regfiles.

There is full example in examples directory.


questions:  greenblat@mac.com



