/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton interface for Bison's Yacc-like parsers in C

   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     module = 258,
     number = 259,
     token = 260,
     endmodule = 261,
     assign = 262,
     input = 263,
     output = 264,
     inout = 265,
     reg = 266,
     wire = 267,
     tri0 = 268,
     tri1 = 269,
     signed = 270,
     event = 271,
     bin = 272,
     hex = 273,
     dig = 274,
     integer = 275,
     real = 276,
     wreal = 277,
     ubin = 278,
     uhex = 279,
     udig = 280,
     domino = 281,
     and_and = 282,
     or_or = 283,
     eq3 = 284,
     eq_eq = 285,
     not_eq = 286,
     gr_eq = 287,
     sm_eq = 288,
     always = 289,
     begin = 290,
     end = 291,
     if = 292,
     else = 293,
     posedge = 294,
     negedge = 295,
     or = 296,
     wait = 297,
     emit = 298,
     string = 299,
     defparam = 300,
     parameter = 301,
     localparam = 302,
     case = 303,
     casez = 304,
     casex = 305,
     endcase = 306,
     default = 307,
     initial = 308,
     forever = 309,
     function = 310,
     endfunction = 311,
     task = 312,
     endtask = 313,
     for = 314,
     while = 315,
     backtick_define = 316,
     backtick_include = 317,
     backtick_timescale = 318,
     backtick_undef = 319,
     define = 320,
     strong1 = 321,
     strong0 = 322,
     pull1 = 323,
     pull0 = 324,
     weak1 = 325,
     weak0 = 326,
     highz1 = 327,
     highz0 = 328,
     fork = 329,
     join = 330,
     disable = 331,
     pragma = 332,
     plus_range = 333,
     minus_range = 334,
     floating = 335,
     power = 336,
     star = 337,
     generate = 338,
     endgenerate = 339,
     genvar = 340,
     force = 341,
     release = 342,
     xnor = 343,
     nand = 344,
     nor = 345,
     repeat = 346,
     supply0 = 347,
     supply1 = 348,
     newver = 349,
     arith_shift_right = 350,
     SignedLeft = 351,
     shift_right = 352,
     shift_left = 353,
     Veryequal = 354,
     noteqeq = 355,
     StarStar = 356,
     UNARY_PREC = 357
   };
#endif
/* Tokens.  */
#define module 258
#define number 259
#define token 260
#define endmodule 261
#define assign 262
#define input 263
#define output 264
#define inout 265
#define reg 266
#define wire 267
#define tri0 268
#define tri1 269
#define signed 270
#define event 271
#define bin 272
#define hex 273
#define dig 274
#define integer 275
#define real 276
#define wreal 277
#define ubin 278
#define uhex 279
#define udig 280
#define domino 281
#define and_and 282
#define or_or 283
#define eq3 284
#define eq_eq 285
#define not_eq 286
#define gr_eq 287
#define sm_eq 288
#define always 289
#define begin 290
#define end 291
#define if 292
#define else 293
#define posedge 294
#define negedge 295
#define or 296
#define wait 297
#define emit 298
#define string 299
#define defparam 300
#define parameter 301
#define localparam 302
#define case 303
#define casez 304
#define casex 305
#define endcase 306
#define default 307
#define initial 308
#define forever 309
#define function 310
#define endfunction 311
#define task 312
#define endtask 313
#define for 314
#define while 315
#define backtick_define 316
#define backtick_include 317
#define backtick_timescale 318
#define backtick_undef 319
#define define 320
#define strong1 321
#define strong0 322
#define pull1 323
#define pull0 324
#define weak1 325
#define weak0 326
#define highz1 327
#define highz0 328
#define fork 329
#define join 330
#define disable 331
#define pragma 332
#define plus_range 333
#define minus_range 334
#define floating 335
#define power 336
#define star 337
#define generate 338
#define endgenerate 339
#define genvar 340
#define force 341
#define release 342
#define xnor 343
#define nand 344
#define nor 345
#define repeat 346
#define supply0 347
#define supply1 348
#define newver 349
#define arith_shift_right 350
#define SignedLeft 351
#define shift_right 352
#define shift_left 353
#define Veryequal 354
#define noteqeq 355
#define StarStar 356
#define UNARY_PREC 357




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE yylval;

