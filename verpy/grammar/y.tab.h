/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

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

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    module = 258,                  /* module  */
    number = 259,                  /* number  */
    token = 260,                   /* token  */
    endmodule = 261,               /* endmodule  */
    assign = 262,                  /* assign  */
    input = 263,                   /* input  */
    output = 264,                  /* output  */
    inout = 265,                   /* inout  */
    reg = 266,                     /* reg  */
    wire = 267,                    /* wire  */
    logic = 268,                   /* logic  */
    tri0 = 269,                    /* tri0  */
    tri1 = 270,                    /* tri1  */
    signed = 271,                  /* signed  */
    event = 272,                   /* event  */
    bin = 273,                     /* bin  */
    hex = 274,                     /* hex  */
    dig = 275,                     /* dig  */
    integer = 276,                 /* integer  */
    int = 277,                     /* int  */
    real = 278,                    /* real  */
    wreal = 279,                   /* wreal  */
    ubin = 280,                    /* ubin  */
    uhex = 281,                    /* uhex  */
    udig = 282,                    /* udig  */
    domino = 283,                  /* domino  */
    and_and = 284,                 /* and_and  */
    or_or = 285,                   /* or_or  */
    eq3 = 286,                     /* eq3  */
    eq_eq = 287,                   /* eq_eq  */
    not_eq = 288,                  /* not_eq  */
    gr_eq = 289,                   /* gr_eq  */
    sm_eq = 290,                   /* sm_eq  */
    always = 291,                  /* always  */
    begin = 292,                   /* begin  */
    end = 293,                     /* end  */
    if = 294,                      /* if  */
    else = 295,                    /* else  */
    posedge = 296,                 /* posedge  */
    negedge = 297,                 /* negedge  */
    or = 298,                      /* or  */
    wait = 299,                    /* wait  */
    emit = 300,                    /* emit  */
    string = 301,                  /* string  */
    defparam = 302,                /* defparam  */
    parameter = 303,               /* parameter  */
    localparam = 304,              /* localparam  */
    case = 305,                    /* case  */
    casez = 306,                   /* casez  */
    casex = 307,                   /* casex  */
    endcase = 308,                 /* endcase  */
    default = 309,                 /* default  */
    initial = 310,                 /* initial  */
    forever = 311,                 /* forever  */
    function = 312,                /* function  */
    endfunction = 313,             /* endfunction  */
    task = 314,                    /* task  */
    endtask = 315,                 /* endtask  */
    for = 316,                     /* for  */
    while = 317,                   /* while  */
    backtick_define = 318,         /* backtick_define  */
    backtick_include = 319,        /* backtick_include  */
    backtick_timescale = 320,      /* backtick_timescale  */
    backtick_undef = 321,          /* backtick_undef  */
    define = 322,                  /* define  */
    strong1 = 323,                 /* strong1  */
    strong0 = 324,                 /* strong0  */
    pull1 = 325,                   /* pull1  */
    pull0 = 326,                   /* pull0  */
    weak1 = 327,                   /* weak1  */
    weak0 = 328,                   /* weak0  */
    highz1 = 329,                  /* highz1  */
    highz0 = 330,                  /* highz0  */
    fork = 331,                    /* fork  */
    join = 332,                    /* join  */
    disable = 333,                 /* disable  */
    pragma1 = 334,                 /* pragma1  */
    pragma2 = 335,                 /* pragma2  */
    plus_range = 336,              /* plus_range  */
    minus_range = 337,             /* minus_range  */
    plus_plus = 338,               /* plus_plus  */
    floating = 339,                /* floating  */
    power = 340,                   /* power  */
    star = 341,                    /* star  */
    generate = 342,                /* generate  */
    endgenerate = 343,             /* endgenerate  */
    genvar = 344,                  /* genvar  */
    force = 345,                   /* force  */
    release = 346,                 /* release  */
    xnor = 347,                    /* xnor  */
    nand = 348,                    /* nand  */
    nor = 349,                     /* nor  */
    repeat = 350,                  /* repeat  */
    supply0 = 351,                 /* supply0  */
    supply1 = 352,                 /* supply1  */
    newver = 353,                  /* newver  */
    return = 354,                  /* return  */
    always_comb = 355,             /* always_comb  */
    always_ff = 356,               /* always_ff  */
    enum = 357,                    /* enum  */
    typedef = 358,                 /* typedef  */
    assert = 359,                  /* assert  */
    struct = 360,                  /* struct  */
    packed = 361,                  /* packed  */
    bit = 362,                     /* bit  */
    automatic = 363,               /* automatic  */
    shift_left = 364,              /* shift_left  */
    shift_right = 365,             /* shift_right  */
    SignedLeft = 366,              /* SignedLeft  */
    arith_shift_right = 367,       /* arith_shift_right  */
    noteqeq = 368,                 /* noteqeq  */
    Veryequal = 369,               /* Veryequal  */
    StarStar = 370,                /* StarStar  */
    UNARY_PREC = 371               /* UNARY_PREC  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif
/* Token kinds.  */
#define YYEMPTY -2
#define YYEOF 0
#define YYerror 256
#define YYUNDEF 257
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
#define logic 268
#define tri0 269
#define tri1 270
#define signed 271
#define event 272
#define bin 273
#define hex 274
#define dig 275
#define integer 276
#define int 277
#define real 278
#define wreal 279
#define ubin 280
#define uhex 281
#define udig 282
#define domino 283
#define and_and 284
#define or_or 285
#define eq3 286
#define eq_eq 287
#define not_eq 288
#define gr_eq 289
#define sm_eq 290
#define always 291
#define begin 292
#define end 293
#define if 294
#define else 295
#define posedge 296
#define negedge 297
#define or 298
#define wait 299
#define emit 300
#define string 301
#define defparam 302
#define parameter 303
#define localparam 304
#define case 305
#define casez 306
#define casex 307
#define endcase 308
#define default 309
#define initial 310
#define forever 311
#define function 312
#define endfunction 313
#define task 314
#define endtask 315
#define for 316
#define while 317
#define backtick_define 318
#define backtick_include 319
#define backtick_timescale 320
#define backtick_undef 321
#define define 322
#define strong1 323
#define strong0 324
#define pull1 325
#define pull0 326
#define weak1 327
#define weak0 328
#define highz1 329
#define highz0 330
#define fork 331
#define join 332
#define disable 333
#define pragma1 334
#define pragma2 335
#define plus_range 336
#define minus_range 337
#define plus_plus 338
#define floating 339
#define power 340
#define star 341
#define generate 342
#define endgenerate 343
#define genvar 344
#define force 345
#define release 346
#define xnor 347
#define nand 348
#define nor 349
#define repeat 350
#define supply0 351
#define supply1 352
#define newver 353
#define return 354
#define always_comb 355
#define always_ff 356
#define enum 357
#define typedef 358
#define assert 359
#define struct 360
#define packed 361
#define bit 362
#define automatic 363
#define shift_left 364
#define shift_right 365
#define SignedLeft 366
#define arith_shift_right 367
#define noteqeq 368
#define Veryequal 369
#define StarStar 370
#define UNARY_PREC 371

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
