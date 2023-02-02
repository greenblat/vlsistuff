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
    real = 277,                    /* real  */
    wreal = 278,                   /* wreal  */
    ubin = 279,                    /* ubin  */
    uhex = 280,                    /* uhex  */
    udig = 281,                    /* udig  */
    domino = 282,                  /* domino  */
    and_and = 283,                 /* and_and  */
    or_or = 284,                   /* or_or  */
    eq3 = 285,                     /* eq3  */
    eq_eq = 286,                   /* eq_eq  */
    not_eq = 287,                  /* not_eq  */
    gr_eq = 288,                   /* gr_eq  */
    sm_eq = 289,                   /* sm_eq  */
    always = 290,                  /* always  */
    begin = 291,                   /* begin  */
    end = 292,                     /* end  */
    if = 293,                      /* if  */
    else = 294,                    /* else  */
    posedge = 295,                 /* posedge  */
    negedge = 296,                 /* negedge  */
    or = 297,                      /* or  */
    wait = 298,                    /* wait  */
    emit = 299,                    /* emit  */
    string = 300,                  /* string  */
    defparam = 301,                /* defparam  */
    parameter = 302,               /* parameter  */
    localparam = 303,              /* localparam  */
    case = 304,                    /* case  */
    casez = 305,                   /* casez  */
    casex = 306,                   /* casex  */
    endcase = 307,                 /* endcase  */
    default = 308,                 /* default  */
    initial = 309,                 /* initial  */
    forever = 310,                 /* forever  */
    function = 311,                /* function  */
    endfunction = 312,             /* endfunction  */
    task = 313,                    /* task  */
    endtask = 314,                 /* endtask  */
    for = 315,                     /* for  */
    while = 316,                   /* while  */
    backtick_define = 317,         /* backtick_define  */
    backtick_include = 318,        /* backtick_include  */
    backtick_timescale = 319,      /* backtick_timescale  */
    backtick_undef = 320,          /* backtick_undef  */
    define = 321,                  /* define  */
    strong1 = 322,                 /* strong1  */
    strong0 = 323,                 /* strong0  */
    pull1 = 324,                   /* pull1  */
    pull0 = 325,                   /* pull0  */
    weak1 = 326,                   /* weak1  */
    weak0 = 327,                   /* weak0  */
    highz1 = 328,                  /* highz1  */
    highz0 = 329,                  /* highz0  */
    fork = 330,                    /* fork  */
    join = 331,                    /* join  */
    disable = 332,                 /* disable  */
    pragma1 = 333,                 /* pragma1  */
    pragma2 = 334,                 /* pragma2  */
    plus_range = 335,              /* plus_range  */
    minus_range = 336,             /* minus_range  */
    floating = 337,                /* floating  */
    power = 338,                   /* power  */
    star = 339,                    /* star  */
    generate = 340,                /* generate  */
    endgenerate = 341,             /* endgenerate  */
    genvar = 342,                  /* genvar  */
    force = 343,                   /* force  */
    release = 344,                 /* release  */
    xnor = 345,                    /* xnor  */
    nand = 346,                    /* nand  */
    nor = 347,                     /* nor  */
    repeat = 348,                  /* repeat  */
    supply0 = 349,                 /* supply0  */
    supply1 = 350,                 /* supply1  */
    newver = 351,                  /* newver  */
    return = 352,                  /* return  */
    always_comb = 353,             /* always_comb  */
    enum = 354,                    /* enum  */
    typedef = 355,                 /* typedef  */
    shift_left = 356,              /* shift_left  */
    shift_right = 357,             /* shift_right  */
    SignedLeft = 358,              /* SignedLeft  */
    arith_shift_right = 359,       /* arith_shift_right  */
    noteqeq = 360,                 /* noteqeq  */
    Veryequal = 361,               /* Veryequal  */
    StarStar = 362,                /* StarStar  */
    UNARY_PREC = 363               /* UNARY_PREC  */
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
#define real 277
#define wreal 278
#define ubin 279
#define uhex 280
#define udig 281
#define domino 282
#define and_and 283
#define or_or 284
#define eq3 285
#define eq_eq 286
#define not_eq 287
#define gr_eq 288
#define sm_eq 289
#define always 290
#define begin 291
#define end 292
#define if 293
#define else 294
#define posedge 295
#define negedge 296
#define or 297
#define wait 298
#define emit 299
#define string 300
#define defparam 301
#define parameter 302
#define localparam 303
#define case 304
#define casez 305
#define casex 306
#define endcase 307
#define default 308
#define initial 309
#define forever 310
#define function 311
#define endfunction 312
#define task 313
#define endtask 314
#define for 315
#define while 316
#define backtick_define 317
#define backtick_include 318
#define backtick_timescale 319
#define backtick_undef 320
#define define 321
#define strong1 322
#define strong0 323
#define pull1 324
#define pull0 325
#define weak1 326
#define weak0 327
#define highz1 328
#define highz0 329
#define fork 330
#define join 331
#define disable 332
#define pragma1 333
#define pragma2 334
#define plus_range 335
#define minus_range 336
#define floating 337
#define power 338
#define star 339
#define generate 340
#define endgenerate 341
#define genvar 342
#define force 343
#define release 344
#define xnor 345
#define nand 346
#define nor 347
#define repeat 348
#define supply0 349
#define supply1 350
#define newver 351
#define return 352
#define always_comb 353
#define enum 354
#define typedef 355
#define shift_left 356
#define shift_right 357
#define SignedLeft 358
#define arith_shift_right 359
#define noteqeq 360
#define Veryequal 361
#define StarStar 362
#define UNARY_PREC 363

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
