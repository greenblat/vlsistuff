


src/synlib_tables.c : llbin/synlib_tables.py
	llbin/table2c.py synlib_tables
	/bin/cp tables.c src/synlib_tables.c


synlib_lexer :  src/synlib_tables.c
	gcc src/synlib_tables.c src/nlexer.c -o synlib_lexer


src/vhdl_tables.c : llbin/vhdl_tables.py
	llbin/table2c.py vhdl_tables
	/bin/cp tables.c src/vhdl_tables.c

vhdl_lexer :  src/vhdl_tables.c
	gcc src/vhdl_tables.c src/nlexer.c -o vhdl_lexer

