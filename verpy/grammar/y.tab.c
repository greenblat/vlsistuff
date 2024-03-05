/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison implementation for Yacc-like parsers in C

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

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output, and Bison version.  */
#define YYBISON 30802

/* Bison version string.  */
#define YYBISON_VERSION "3.8.2"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1





# ifndef YY_CAST
#  ifdef __cplusplus
#   define YY_CAST(Type, Val) static_cast<Type> (Val)
#   define YY_REINTERPRET_CAST(Type, Val) reinterpret_cast<Type> (Val)
#  else
#   define YY_CAST(Type, Val) ((Type) (Val))
#   define YY_REINTERPRET_CAST(Type, Val) ((Type) (Val))
#  endif
# endif
# ifndef YY_NULLPTR
#  if defined __cplusplus
#   if 201103L <= __cplusplus
#    define YY_NULLPTR nullptr
#   else
#    define YY_NULLPTR 0
#   endif
#  else
#   define YY_NULLPTR ((void*)0)
#  endif
# endif

/* Use api.header.include to #include this header
   instead of duplicating it here.  */
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
    floating = 338,                /* floating  */
    power = 339,                   /* power  */
    star = 340,                    /* star  */
    generate = 341,                /* generate  */
    endgenerate = 342,             /* endgenerate  */
    genvar = 343,                  /* genvar  */
    force = 344,                   /* force  */
    release = 345,                 /* release  */
    xnor = 346,                    /* xnor  */
    nand = 347,                    /* nand  */
    nor = 348,                     /* nor  */
    repeat = 349,                  /* repeat  */
    supply0 = 350,                 /* supply0  */
    supply1 = 351,                 /* supply1  */
    newver = 352,                  /* newver  */
    return = 353,                  /* return  */
    always_comb = 354,             /* always_comb  */
    always_ff = 355,               /* always_ff  */
    enum = 356,                    /* enum  */
    typedef = 357,                 /* typedef  */
    assert = 358,                  /* assert  */
    shift_left = 359,              /* shift_left  */
    shift_right = 360,             /* shift_right  */
    SignedLeft = 361,              /* SignedLeft  */
    arith_shift_right = 362,       /* arith_shift_right  */
    noteqeq = 363,                 /* noteqeq  */
    Veryequal = 364,               /* Veryequal  */
    StarStar = 365,                /* StarStar  */
    UNARY_PREC = 366               /* UNARY_PREC  */
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
#define floating 338
#define power 339
#define star 340
#define generate 341
#define endgenerate 342
#define genvar 343
#define force 344
#define release 345
#define xnor 346
#define nand 347
#define nor 348
#define repeat 349
#define supply0 350
#define supply1 351
#define newver 352
#define return 353
#define always_comb 354
#define always_ff 355
#define enum 356
#define typedef 357
#define assert 358
#define shift_left 359
#define shift_right 360
#define SignedLeft 361
#define arith_shift_right 362
#define noteqeq 363
#define Veryequal 364
#define StarStar 365
#define UNARY_PREC 366

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
/* Symbol kind.  */
enum yysymbol_kind_t
{
  YYSYMBOL_YYEMPTY = -2,
  YYSYMBOL_YYEOF = 0,                      /* "end of file"  */
  YYSYMBOL_YYerror = 1,                    /* error  */
  YYSYMBOL_YYUNDEF = 2,                    /* "invalid token"  */
  YYSYMBOL_module = 3,                     /* module  */
  YYSYMBOL_number = 4,                     /* number  */
  YYSYMBOL_token = 5,                      /* token  */
  YYSYMBOL_endmodule = 6,                  /* endmodule  */
  YYSYMBOL_assign = 7,                     /* assign  */
  YYSYMBOL_input = 8,                      /* input  */
  YYSYMBOL_output = 9,                     /* output  */
  YYSYMBOL_inout = 10,                     /* inout  */
  YYSYMBOL_reg = 11,                       /* reg  */
  YYSYMBOL_wire = 12,                      /* wire  */
  YYSYMBOL_logic = 13,                     /* logic  */
  YYSYMBOL_tri0 = 14,                      /* tri0  */
  YYSYMBOL_tri1 = 15,                      /* tri1  */
  YYSYMBOL_signed = 16,                    /* signed  */
  YYSYMBOL_event = 17,                     /* event  */
  YYSYMBOL_bin = 18,                       /* bin  */
  YYSYMBOL_hex = 19,                       /* hex  */
  YYSYMBOL_dig = 20,                       /* dig  */
  YYSYMBOL_integer = 21,                   /* integer  */
  YYSYMBOL_int = 22,                       /* int  */
  YYSYMBOL_real = 23,                      /* real  */
  YYSYMBOL_wreal = 24,                     /* wreal  */
  YYSYMBOL_ubin = 25,                      /* ubin  */
  YYSYMBOL_uhex = 26,                      /* uhex  */
  YYSYMBOL_udig = 27,                      /* udig  */
  YYSYMBOL_domino = 28,                    /* domino  */
  YYSYMBOL_and_and = 29,                   /* and_and  */
  YYSYMBOL_or_or = 30,                     /* or_or  */
  YYSYMBOL_eq3 = 31,                       /* eq3  */
  YYSYMBOL_eq_eq = 32,                     /* eq_eq  */
  YYSYMBOL_not_eq = 33,                    /* not_eq  */
  YYSYMBOL_gr_eq = 34,                     /* gr_eq  */
  YYSYMBOL_sm_eq = 35,                     /* sm_eq  */
  YYSYMBOL_always = 36,                    /* always  */
  YYSYMBOL_begin = 37,                     /* begin  */
  YYSYMBOL_end = 38,                       /* end  */
  YYSYMBOL_if = 39,                        /* if  */
  YYSYMBOL_else = 40,                      /* else  */
  YYSYMBOL_posedge = 41,                   /* posedge  */
  YYSYMBOL_negedge = 42,                   /* negedge  */
  YYSYMBOL_or = 43,                        /* or  */
  YYSYMBOL_wait = 44,                      /* wait  */
  YYSYMBOL_emit = 45,                      /* emit  */
  YYSYMBOL_string = 46,                    /* string  */
  YYSYMBOL_defparam = 47,                  /* defparam  */
  YYSYMBOL_parameter = 48,                 /* parameter  */
  YYSYMBOL_localparam = 49,                /* localparam  */
  YYSYMBOL_case = 50,                      /* case  */
  YYSYMBOL_casez = 51,                     /* casez  */
  YYSYMBOL_casex = 52,                     /* casex  */
  YYSYMBOL_endcase = 53,                   /* endcase  */
  YYSYMBOL_default = 54,                   /* default  */
  YYSYMBOL_initial = 55,                   /* initial  */
  YYSYMBOL_forever = 56,                   /* forever  */
  YYSYMBOL_function = 57,                  /* function  */
  YYSYMBOL_endfunction = 58,               /* endfunction  */
  YYSYMBOL_task = 59,                      /* task  */
  YYSYMBOL_endtask = 60,                   /* endtask  */
  YYSYMBOL_for = 61,                       /* for  */
  YYSYMBOL_while = 62,                     /* while  */
  YYSYMBOL_backtick_define = 63,           /* backtick_define  */
  YYSYMBOL_backtick_include = 64,          /* backtick_include  */
  YYSYMBOL_backtick_timescale = 65,        /* backtick_timescale  */
  YYSYMBOL_backtick_undef = 66,            /* backtick_undef  */
  YYSYMBOL_define = 67,                    /* define  */
  YYSYMBOL_strong1 = 68,                   /* strong1  */
  YYSYMBOL_strong0 = 69,                   /* strong0  */
  YYSYMBOL_pull1 = 70,                     /* pull1  */
  YYSYMBOL_pull0 = 71,                     /* pull0  */
  YYSYMBOL_weak1 = 72,                     /* weak1  */
  YYSYMBOL_weak0 = 73,                     /* weak0  */
  YYSYMBOL_highz1 = 74,                    /* highz1  */
  YYSYMBOL_highz0 = 75,                    /* highz0  */
  YYSYMBOL_fork = 76,                      /* fork  */
  YYSYMBOL_join = 77,                      /* join  */
  YYSYMBOL_disable = 78,                   /* disable  */
  YYSYMBOL_pragma1 = 79,                   /* pragma1  */
  YYSYMBOL_pragma2 = 80,                   /* pragma2  */
  YYSYMBOL_plus_range = 81,                /* plus_range  */
  YYSYMBOL_minus_range = 82,               /* minus_range  */
  YYSYMBOL_floating = 83,                  /* floating  */
  YYSYMBOL_power = 84,                     /* power  */
  YYSYMBOL_star = 85,                      /* star  */
  YYSYMBOL_generate = 86,                  /* generate  */
  YYSYMBOL_endgenerate = 87,               /* endgenerate  */
  YYSYMBOL_genvar = 88,                    /* genvar  */
  YYSYMBOL_force = 89,                     /* force  */
  YYSYMBOL_release = 90,                   /* release  */
  YYSYMBOL_xnor = 91,                      /* xnor  */
  YYSYMBOL_nand = 92,                      /* nand  */
  YYSYMBOL_nor = 93,                       /* nor  */
  YYSYMBOL_repeat = 94,                    /* repeat  */
  YYSYMBOL_supply0 = 95,                   /* supply0  */
  YYSYMBOL_supply1 = 96,                   /* supply1  */
  YYSYMBOL_newver = 97,                    /* newver  */
  YYSYMBOL_return = 98,                    /* return  */
  YYSYMBOL_always_comb = 99,               /* always_comb  */
  YYSYMBOL_always_ff = 100,                /* always_ff  */
  YYSYMBOL_enum = 101,                     /* enum  */
  YYSYMBOL_typedef = 102,                  /* typedef  */
  YYSYMBOL_assert = 103,                   /* assert  */
  YYSYMBOL_104_ = 104,                     /* '?'  */
  YYSYMBOL_105_ = 105,                     /* ':'  */
  YYSYMBOL_106_ = 106,                     /* '|'  */
  YYSYMBOL_107_ = 107,                     /* '^'  */
  YYSYMBOL_108_ = 108,                     /* '&'  */
  YYSYMBOL_shift_left = 109,               /* shift_left  */
  YYSYMBOL_shift_right = 110,              /* shift_right  */
  YYSYMBOL_SignedLeft = 111,               /* SignedLeft  */
  YYSYMBOL_arith_shift_right = 112,        /* arith_shift_right  */
  YYSYMBOL_113_ = 113,                     /* '<'  */
  YYSYMBOL_114_ = 114,                     /* '>'  */
  YYSYMBOL_115_ = 115,                     /* '+'  */
  YYSYMBOL_116_ = 116,                     /* '-'  */
  YYSYMBOL_noteqeq = 117,                  /* noteqeq  */
  YYSYMBOL_Veryequal = 118,                /* Veryequal  */
  YYSYMBOL_119_ = 119,                     /* '*'  */
  YYSYMBOL_120_ = 120,                     /* '/'  */
  YYSYMBOL_121_ = 121,                     /* '%'  */
  YYSYMBOL_StarStar = 122,                 /* StarStar  */
  YYSYMBOL_UNARY_PREC = 123,               /* UNARY_PREC  */
  YYSYMBOL_124_ = 124,                     /* '#'  */
  YYSYMBOL_125_ = 125,                     /* '('  */
  YYSYMBOL_126_ = 126,                     /* ')'  */
  YYSYMBOL_127_ = 127,                     /* ';'  */
  YYSYMBOL_128_ = 128,                     /* ','  */
  YYSYMBOL_129_ = 129,                     /* '='  */
  YYSYMBOL_130_ = 130,                     /* '{'  */
  YYSYMBOL_131_ = 131,                     /* '}'  */
  YYSYMBOL_132_ = 132,                     /* '.'  */
  YYSYMBOL_133_ = 133,                     /* '['  */
  YYSYMBOL_134_ = 134,                     /* ']'  */
  YYSYMBOL_135_ = 135,                     /* '@'  */
  YYSYMBOL_136_ = 136,                     /* '!'  */
  YYSYMBOL_137_ = 137,                     /* '~'  */
  YYSYMBOL_YYACCEPT = 138,                 /* $accept  */
  YYSYMBOL_Main = 139,                     /* Main  */
  YYSYMBOL_Mains = 140,                    /* Mains  */
  YYSYMBOL_MainItem = 141,                 /* MainItem  */
  YYSYMBOL_Module = 142,                   /* Module  */
  YYSYMBOL_Hparams = 143,                  /* Hparams  */
  YYSYMBOL_Header = 144,                   /* Header  */
  YYSYMBOL_Header_list = 145,              /* Header_list  */
  YYSYMBOL_Header_item = 146,              /* Header_item  */
  YYSYMBOL_Module_stuffs = 147,            /* Module_stuffs  */
  YYSYMBOL_Mstuff = 148,                   /* Mstuff  */
  YYSYMBOL_Define = 149,                   /* Define  */
  YYSYMBOL_Initial = 150,                  /* Initial  */
  YYSYMBOL_OneDef = 151,                   /* OneDef  */
  YYSYMBOL_ManyDefs = 152,                 /* ManyDefs  */
  YYSYMBOL_Definition = 153,               /* Definition  */
  YYSYMBOL_Assign = 154,                   /* Assign  */
  YYSYMBOL_StrengthDef = 155,              /* StrengthDef  */
  YYSYMBOL_Strength = 156,                 /* Strength  */
  YYSYMBOL_WidthInt = 157,                 /* WidthInt  */
  YYSYMBOL_Function = 158,                 /* Function  */
  YYSYMBOL_Task = 159,                     /* Task  */
  YYSYMBOL_Mem_defs = 160,                 /* Mem_defs  */
  YYSYMBOL_Mem_def = 161,                  /* Mem_def  */
  YYSYMBOL_Parameter = 162,                /* Parameter  */
  YYSYMBOL_Localparam = 163,               /* Localparam  */
  YYSYMBOL_Defparam = 164,                 /* Defparam  */
  YYSYMBOL_Pairs = 165,                    /* Pairs  */
  YYSYMBOL_Pair = 166,                     /* Pair  */
  YYSYMBOL_head_params = 167,              /* head_params  */
  YYSYMBOL_head_param = 168,               /* head_param  */
  YYSYMBOL_Instance = 169,                 /* Instance  */
  YYSYMBOL_Conns_list = 170,               /* Conns_list  */
  YYSYMBOL_Connection = 171,               /* Connection  */
  YYSYMBOL_AssignParams = 172,             /* AssignParams  */
  YYSYMBOL_Prms_list = 173,                /* Prms_list  */
  YYSYMBOL_PrmAssign = 174,                /* PrmAssign  */
  YYSYMBOL_InstParams = 175,               /* InstParams  */
  YYSYMBOL_Always = 176,                   /* Always  */
  YYSYMBOL_Generate = 177,                 /* Generate  */
  YYSYMBOL_GenStatements = 178,            /* GenStatements  */
  YYSYMBOL_GenStatement = 179,             /* GenStatement  */
  YYSYMBOL_GenFor_statement = 180,         /* GenFor_statement  */
  YYSYMBOL_When = 181,                     /* When  */
  YYSYMBOL_Or_coma = 182,                  /* Or_coma  */
  YYSYMBOL_When_items = 183,               /* When_items  */
  YYSYMBOL_When_item = 184,                /* When_item  */
  YYSYMBOL_Statement = 185,                /* Statement  */
  YYSYMBOL_pragma_stuffs = 186,            /* pragma_stuffs  */
  YYSYMBOL_pragma_item = 187,              /* pragma_item  */
  YYSYMBOL_Pragma = 188,                   /* Pragma  */
  YYSYMBOL_For_statement = 189,            /* For_statement  */
  YYSYMBOL_Repeat_statement = 190,         /* Repeat_statement  */
  YYSYMBOL_While_statement = 191,          /* While_statement  */
  YYSYMBOL_Soft_assigns = 192,             /* Soft_assigns  */
  YYSYMBOL_Soft_assign = 193,              /* Soft_assign  */
  YYSYMBOL_Cases = 194,                    /* Cases  */
  YYSYMBOL_GenCases = 195,                 /* GenCases  */
  YYSYMBOL_Case = 196,                     /* Case  */
  YYSYMBOL_GenCase = 197,                  /* GenCase  */
  YYSYMBOL_Default = 198,                  /* Default  */
  YYSYMBOL_GenDefault = 199,               /* GenDefault  */
  YYSYMBOL_Exprs = 200,                    /* Exprs  */
  YYSYMBOL_Statements = 201,               /* Statements  */
  YYSYMBOL_LSH = 202,                      /* LSH  */
  YYSYMBOL_Tokens_list = 203,              /* Tokens_list  */
  YYSYMBOL_Width = 204,                    /* Width  */
  YYSYMBOL_BusBit = 205,                   /* BusBit  */
  YYSYMBOL_ExtDir = 206,                   /* ExtDir  */
  YYSYMBOL_IntDir = 207,                   /* IntDir  */
  YYSYMBOL_CurlyList = 208,                /* CurlyList  */
  YYSYMBOL_CurlyItems = 209,               /* CurlyItems  */
  YYSYMBOL_CurlyItem = 210,                /* CurlyItem  */
  YYSYMBOL_Literal = 211,                  /* Literal  */
  YYSYMBOL_Expr = 212                      /* Expr  */
};
typedef enum yysymbol_kind_t yysymbol_kind_t;




#ifdef short
# undef short
#endif

/* On compilers that do not define __PTRDIFF_MAX__ etc., make sure
   <limits.h> and (if available) <stdint.h> are included
   so that the code can choose integer types of a good width.  */

#ifndef __PTRDIFF_MAX__
# include <limits.h> /* INFRINGES ON USER NAME SPACE */
# if defined __STDC_VERSION__ && 199901 <= __STDC_VERSION__
#  include <stdint.h> /* INFRINGES ON USER NAME SPACE */
#  define YY_STDINT_H
# endif
#endif

/* Narrow types that promote to a signed type and that can represent a
   signed or unsigned integer of at least N bits.  In tables they can
   save space and decrease cache pressure.  Promoting to a signed type
   helps avoid bugs in integer arithmetic.  */

#ifdef __INT_LEAST8_MAX__
typedef __INT_LEAST8_TYPE__ yytype_int8;
#elif defined YY_STDINT_H
typedef int_least8_t yytype_int8;
#else
typedef signed char yytype_int8;
#endif

#ifdef __INT_LEAST16_MAX__
typedef __INT_LEAST16_TYPE__ yytype_int16;
#elif defined YY_STDINT_H
typedef int_least16_t yytype_int16;
#else
typedef short yytype_int16;
#endif

/* Work around bug in HP-UX 11.23, which defines these macros
   incorrectly for preprocessor constants.  This workaround can likely
   be removed in 2023, as HPE has promised support for HP-UX 11.23
   (aka HP-UX 11i v2) only through the end of 2022; see Table 2 of
   <https://h20195.www2.hpe.com/V2/getpdf.aspx/4AA4-7673ENW.pdf>.  */
#ifdef __hpux
# undef UINT_LEAST8_MAX
# undef UINT_LEAST16_MAX
# define UINT_LEAST8_MAX 255
# define UINT_LEAST16_MAX 65535
#endif

#if defined __UINT_LEAST8_MAX__ && __UINT_LEAST8_MAX__ <= __INT_MAX__
typedef __UINT_LEAST8_TYPE__ yytype_uint8;
#elif (!defined __UINT_LEAST8_MAX__ && defined YY_STDINT_H \
       && UINT_LEAST8_MAX <= INT_MAX)
typedef uint_least8_t yytype_uint8;
#elif !defined __UINT_LEAST8_MAX__ && UCHAR_MAX <= INT_MAX
typedef unsigned char yytype_uint8;
#else
typedef short yytype_uint8;
#endif

#if defined __UINT_LEAST16_MAX__ && __UINT_LEAST16_MAX__ <= __INT_MAX__
typedef __UINT_LEAST16_TYPE__ yytype_uint16;
#elif (!defined __UINT_LEAST16_MAX__ && defined YY_STDINT_H \
       && UINT_LEAST16_MAX <= INT_MAX)
typedef uint_least16_t yytype_uint16;
#elif !defined __UINT_LEAST16_MAX__ && USHRT_MAX <= INT_MAX
typedef unsigned short yytype_uint16;
#else
typedef int yytype_uint16;
#endif

#ifndef YYPTRDIFF_T
# if defined __PTRDIFF_TYPE__ && defined __PTRDIFF_MAX__
#  define YYPTRDIFF_T __PTRDIFF_TYPE__
#  define YYPTRDIFF_MAXIMUM __PTRDIFF_MAX__
# elif defined PTRDIFF_MAX
#  ifndef ptrdiff_t
#   include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  endif
#  define YYPTRDIFF_T ptrdiff_t
#  define YYPTRDIFF_MAXIMUM PTRDIFF_MAX
# else
#  define YYPTRDIFF_T long
#  define YYPTRDIFF_MAXIMUM LONG_MAX
# endif
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif defined __STDC_VERSION__ && 199901 <= __STDC_VERSION__
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned
# endif
#endif

#define YYSIZE_MAXIMUM                                  \
  YY_CAST (YYPTRDIFF_T,                                 \
           (YYPTRDIFF_MAXIMUM < YY_CAST (YYSIZE_T, -1)  \
            ? YYPTRDIFF_MAXIMUM                         \
            : YY_CAST (YYSIZE_T, -1)))

#define YYSIZEOF(X) YY_CAST (YYPTRDIFF_T, sizeof (X))


/* Stored state numbers (used for stacks). */
typedef yytype_int16 yy_state_t;

/* State numbers in computations.  */
typedef int yy_state_fast_t;

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(Msgid) dgettext ("bison-runtime", Msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(Msgid) Msgid
# endif
#endif


#ifndef YY_ATTRIBUTE_PURE
# if defined __GNUC__ && 2 < __GNUC__ + (96 <= __GNUC_MINOR__)
#  define YY_ATTRIBUTE_PURE __attribute__ ((__pure__))
# else
#  define YY_ATTRIBUTE_PURE
# endif
#endif

#ifndef YY_ATTRIBUTE_UNUSED
# if defined __GNUC__ && 2 < __GNUC__ + (7 <= __GNUC_MINOR__)
#  define YY_ATTRIBUTE_UNUSED __attribute__ ((__unused__))
# else
#  define YY_ATTRIBUTE_UNUSED
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YY_USE(E) ((void) (E))
#else
# define YY_USE(E) /* empty */
#endif

/* Suppress an incorrect diagnostic about yylval being uninitialized.  */
#if defined __GNUC__ && ! defined __ICC && 406 <= __GNUC__ * 100 + __GNUC_MINOR__
# if __GNUC__ * 100 + __GNUC_MINOR__ < 407
#  define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN                           \
    _Pragma ("GCC diagnostic push")                                     \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")
# else
#  define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN                           \
    _Pragma ("GCC diagnostic push")                                     \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")              \
    _Pragma ("GCC diagnostic ignored \"-Wmaybe-uninitialized\"")
# endif
# define YY_IGNORE_MAYBE_UNINITIALIZED_END      \
    _Pragma ("GCC diagnostic pop")
#else
# define YY_INITIAL_VALUE(Value) Value
#endif
#ifndef YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_END
#endif
#ifndef YY_INITIAL_VALUE
# define YY_INITIAL_VALUE(Value) /* Nothing. */
#endif

#if defined __cplusplus && defined __GNUC__ && ! defined __ICC && 6 <= __GNUC__
# define YY_IGNORE_USELESS_CAST_BEGIN                          \
    _Pragma ("GCC diagnostic push")                            \
    _Pragma ("GCC diagnostic ignored \"-Wuseless-cast\"")
# define YY_IGNORE_USELESS_CAST_END            \
    _Pragma ("GCC diagnostic pop")
#endif
#ifndef YY_IGNORE_USELESS_CAST_BEGIN
# define YY_IGNORE_USELESS_CAST_BEGIN
# define YY_IGNORE_USELESS_CAST_END
#endif


#define YY_ASSERT(E) ((void) (0 && (E)))

#if !defined yyoverflow

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined EXIT_SUCCESS
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
      /* Use EXIT_SUCCESS as a witness for stdlib.h.  */
#     ifndef EXIT_SUCCESS
#      define EXIT_SUCCESS 0
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's 'empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (0)
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined EXIT_SUCCESS \
       && ! ((defined YYMALLOC || defined malloc) \
             && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef EXIT_SUCCESS
#    define EXIT_SUCCESS 0
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined EXIT_SUCCESS
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined EXIT_SUCCESS
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* !defined yyoverflow */

#if (! defined yyoverflow \
     && (! defined __cplusplus \
         || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yy_state_t yyss_alloc;
  YYSTYPE yyvs_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (YYSIZEOF (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (YYSIZEOF (yy_state_t) + YYSIZEOF (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

# define YYCOPY_NEEDED 1

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)                           \
    do                                                                  \
      {                                                                 \
        YYPTRDIFF_T yynewbytes;                                         \
        YYCOPY (&yyptr->Stack_alloc, Stack, yysize);                    \
        Stack = &yyptr->Stack_alloc;                                    \
        yynewbytes = yystacksize * YYSIZEOF (*Stack) + YYSTACK_GAP_MAXIMUM; \
        yyptr += yynewbytes / YYSIZEOF (*yyptr);                        \
      }                                                                 \
    while (0)

#endif

#if defined YYCOPY_NEEDED && YYCOPY_NEEDED
/* Copy COUNT objects from SRC to DST.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(Dst, Src, Count) \
      __builtin_memcpy (Dst, Src, YY_CAST (YYSIZE_T, (Count)) * sizeof (*(Src)))
#  else
#   define YYCOPY(Dst, Src, Count)              \
      do                                        \
        {                                       \
          YYPTRDIFF_T yyi;                      \
          for (yyi = 0; yyi < (Count); yyi++)   \
            (Dst)[yyi] = (Src)[yyi];            \
        }                                       \
      while (0)
#  endif
# endif
#endif /* !YYCOPY_NEEDED */

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  12
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   5639

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  138
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  75
/* YYNRULES -- Number of rules.  */
#define YYNRULES  375
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  857

/* YYMAXUTOK -- Last valid token kind.  */
#define YYMAXUTOK   366


/* YYTRANSLATE(TOKEN-NUM) -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex, with out-of-bounds checking.  */
#define YYTRANSLATE(YYX)                                \
  (0 <= (YYX) && (YYX) <= YYMAXUTOK                     \
   ? YY_CAST (yysymbol_kind_t, yytranslate[YYX])        \
   : YYSYMBOL_YYUNDEF)

/* YYTRANSLATE[TOKEN-NUM] -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   136,     2,   124,     2,   121,   108,     2,
     125,   126,   119,   115,   128,   116,   132,   120,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,   105,   127,
     113,   129,   114,   104,   135,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,   133,     2,   134,   107,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   130,   106,   131,   137,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    52,    53,    54,
      55,    56,    57,    58,    59,    60,    61,    62,    63,    64,
      65,    66,    67,    68,    69,    70,    71,    72,    73,    74,
      75,    76,    77,    78,    79,    80,    81,    82,    83,    84,
      85,    86,    87,    88,    89,    90,    91,    92,    93,    94,
      95,    96,    97,    98,    99,   100,   101,   102,   103,   109,
     110,   111,   112,   117,   118,   122,   123
};

#if YYDEBUG
/* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_int16 yyrline[] =
{
       0,    46,    46,    47,    47,    48,    48,    50,    51,    52,
      54,    54,    55,    55,    55,    56,    56,    58,    58,    58,
      59,    60,    61,    62,    62,    62,    66,    66,    69,    70,
      71,    72,    73,    74,    75,    76,    77,    78,    79,    80,
      81,    82,    86,    86,    86,    86,    86,    87,    88,    88,
      89,    89,    91,    92,    93,    94,    95,    96,    97,    98,
      99,   100,   101,   102,   103,   104,   105,   106,   107,   108,
     112,   113,   114,   115,   118,   119,   119,   119,   119,   119,
     119,   119,   119,   120,   120,   122,   123,   124,   125,   126,
     127,   128,   129,   130,   133,   134,   135,   136,   139,   139,
     141,   142,   143,   144,   145,   146,   147,   148,   149,   150,
     151,   152,   153,   157,   158,   159,   160,   161,   163,   163,
     163,   164,   166,   166,   167,   169,   169,   171,   172,   173,
     174,   178,   179,   180,   181,   182,   183,   184,   185,   186,
     187,   188,   189,   190,   198,   198,   199,   199,   199,   199,
     201,   201,   201,   201,   202,   202,   203,   203,   204,   204,
     204,   204,   204,   204,   207,   207,   207,   207,   210,   212,
     212,   215,   216,   217,   218,   219,   220,   221,   222,   223,
     224,   225,   226,   227,   228,   229,   230,   231,   232,   237,
     242,   242,   242,   242,   243,   243,   244,   244,   245,   245,
     245,   250,   251,   252,   253,   254,   255,   256,   257,   258,
     259,   260,   261,   262,   263,   264,   265,   266,   267,   268,
     269,   270,   271,   272,   273,   274,   275,   276,   277,   278,
     279,   280,   281,   282,   283,   284,   285,   286,   287,   288,
     289,   290,   294,   294,   295,   295,   297,   300,   301,   303,
     304,   305,   305,   306,   307,   307,   308,   308,   309,   309,
     310,   310,   311,   311,   312,   312,   314,   314,   315,   315,
     318,   318,   318,   318,   318,   318,   320,   320,   322,   322,
     322,   323,   325,   325,   325,   325,   325,   325,   325,   325,
     325,   325,   325,   325,   327,   327,   327,   327,   327,   327,
     327,   327,   327,   327,   327,   327,   327,   329,   330,   330,
     332,   333,   334,   339,   340,   341,   342,   342,   342,   342,
     342,   342,   346,   347,   348,   349,   350,   351,   352,   352,
     352,   352,   352,   352,   353,   354,   355,   356,   357,   358,
     359,   360,   361,   362,   363,   364,   365,   366,   367,   368,
     369,   370,   371,   372,   373,   374,   375,   376,   377,   378,
     379,   380,   381,   382,   383,   384,   385,   386,   387,   388,
     389,   390,   391,   392,   393,   394
};
#endif

/** Accessing symbol of state STATE.  */
#define YY_ACCESSING_SYMBOL(State) YY_CAST (yysymbol_kind_t, yystos[State])

#if YYDEBUG || 0
/* The user-facing name of the symbol whose (internal) number is
   YYSYMBOL.  No bounds checking.  */
static const char *yysymbol_name (yysymbol_kind_t yysymbol) YY_ATTRIBUTE_UNUSED;

/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "\"end of file\"", "error", "\"invalid token\"", "module", "number",
  "token", "endmodule", "assign", "input", "output", "inout", "reg",
  "wire", "logic", "tri0", "tri1", "signed", "event", "bin", "hex", "dig",
  "integer", "int", "real", "wreal", "ubin", "uhex", "udig", "domino",
  "and_and", "or_or", "eq3", "eq_eq", "not_eq", "gr_eq", "sm_eq", "always",
  "begin", "end", "if", "else", "posedge", "negedge", "or", "wait", "emit",
  "string", "defparam", "parameter", "localparam", "case", "casez",
  "casex", "endcase", "default", "initial", "forever", "function",
  "endfunction", "task", "endtask", "for", "while", "backtick_define",
  "backtick_include", "backtick_timescale", "backtick_undef", "define",
  "strong1", "strong0", "pull1", "pull0", "weak1", "weak0", "highz1",
  "highz0", "fork", "join", "disable", "pragma1", "pragma2", "plus_range",
  "minus_range", "floating", "power", "star", "generate", "endgenerate",
  "genvar", "force", "release", "xnor", "nand", "nor", "repeat", "supply0",
  "supply1", "newver", "return", "always_comb", "always_ff", "enum",
  "typedef", "assert", "'?'", "':'", "'|'", "'^'", "'&'", "shift_left",
  "shift_right", "SignedLeft", "arith_shift_right", "'<'", "'>'", "'+'",
  "'-'", "noteqeq", "Veryequal", "'*'", "'/'", "'%'", "StarStar",
  "UNARY_PREC", "'#'", "'('", "')'", "';'", "','", "'='", "'{'", "'}'",
  "'.'", "'['", "']'", "'@'", "'!'", "'~'", "$accept", "Main", "Mains",
  "MainItem", "Module", "Hparams", "Header", "Header_list", "Header_item",
  "Module_stuffs", "Mstuff", "Define", "Initial", "OneDef", "ManyDefs",
  "Definition", "Assign", "StrengthDef", "Strength", "WidthInt",
  "Function", "Task", "Mem_defs", "Mem_def", "Parameter", "Localparam",
  "Defparam", "Pairs", "Pair", "head_params", "head_param", "Instance",
  "Conns_list", "Connection", "AssignParams", "Prms_list", "PrmAssign",
  "InstParams", "Always", "Generate", "GenStatements", "GenStatement",
  "GenFor_statement", "When", "Or_coma", "When_items", "When_item",
  "Statement", "pragma_stuffs", "pragma_item", "Pragma", "For_statement",
  "Repeat_statement", "While_statement", "Soft_assigns", "Soft_assign",
  "Cases", "GenCases", "Case", "GenCase", "Default", "GenDefault", "Exprs",
  "Statements", "LSH", "Tokens_list", "Width", "BusBit", "ExtDir",
  "IntDir", "CurlyList", "CurlyItems", "CurlyItem", "Literal", "Expr", YY_NULLPTR
};

static const char *
yysymbol_name (yysymbol_kind_t yysymbol)
{
  return yytname[yysymbol];
}
#endif

#define YYPACT_NINF (-503)

#define yypact_value_is_default(Yyn) \
  ((Yyn) == YYPACT_NINF)

#define YYTABLE_NINF (-217)

#define yytable_value_is_error(Yyn) \
  0

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
static const yytype_int16 yypact[] =
{
      93,    14,   224,    89,    93,  -503,  -503,  -503,   293,   106,
    1746,  -503,  -503,  -503,   -27,    70,  -503,   -54,  4182,    29,
    -503,   -64,  -503,  -503,  -503,  -503,  -503,  -503,  -503,    47,
    -503,  1746,  1746,  1746,  1746,  1746,  1746,  1746,  1746,  1352,
    1746,  1746,  -503,  5450,    54,  -503,   313,   432,   206,   138,
      80,  -503,    15,  4278,    76,  -503,    63,   236,   256,  -503,
    -503,  -503,  -503,   275,  -503,  -503,  2693,    65,   355,    33,
       7,  2693,    34,   386,    58,  4662,  -503,  -503,  -503,  -503,
    2693,   272,   312,   415,  4278,  -503,  -503,  -503,  -503,  -503,
    -503,  -503,  -503,  -503,  -503,  -503,  -503,  -503,    10,    17,
     429,  1746,  1746,  -503,   318,  1746,  -503,  -503,  -503,  -503,
    -503,  -503,  -503,  4661,   325,   265,  -503,  3137,  -503,  -503,
    1746,  1746,  1746,  1746,  1746,  1746,  1746,  1746,  1746,  1746,
    1746,  1746,  1746,  1746,  1746,  1746,  1746,  1746,  1746,  1746,
    1746,  1746,  1746,  1746,  1746,  1746,   333,    42,   464,  -503,
     167,  -503,  -503,  -503,  -503,   460,  -503,  -503,  -503,  -503,
    -503,   365,   336,   366,   494,  1746,    43,   497,   133,   102,
    1746,   502,   318,   134,   512,    59,    35,   211,  -503,   385,
    -503,  -503,  -503,   397,   391,   175,    35,    10,   275,   275,
    2058,   405,  1746,   533,   453,   465,   499,  2693,   500,   501,
    2693,   554,  1746,  1746,   503,   592,   505,  1746,   137,  2128,
    -503,  -503,  -503,  -503,  -503,   -19,   507,  1746,   474,   225,
    -503,     7,   243,     7,   274,     7,   506,  -503,   297,  -503,
     630,   508,   331,   509,  -503,   -35,  -503,  3261,   515,   518,
     519,   275,  -503,  -503,  -503,  -503,  -503,  -503,  -503,  -503,
    4374,  -503,  -503,  -503,  -503,  2693,    28,  -503,  -503,   521,
     275,   178,  -503,   302,   640,    45,   641,   335,  5450,  2919,
    -503,  -503,  4699,  -503,  -503,  1352,  -503,  -503,   407,  5518,
     185,   185,   185,   452,   452,  -503,  2746,  2746,  2746,  5416,
    5484,  2746,  4522,   976,   976,   976,   452,   452,   202,   202,
     185,  -503,  -503,  -503,  1746,   522,   647,   524,  -503,   166,
    -503,  -503,  -503,   264,  -503,  5382,   255,    46,  -503,   869,
    -503,   529,  -503,  -503,  -503,   945,   339,   -42,  -503,   318,
    -503,  -503,  -503,  1746,  -503,  -503,  -503,  -503,  -503,  -503,
    -503,  -503,   528,    35,   537,   538,  -503,    35,  1746,   275,
    -503,  1428,  -503,   539,   542,   275,   543,   544,  -503,   659,
    -503,  2198,  1746,  3338,   546,  1746,  1746,  1746,  -503,    62,
    1746,  2268,   547,  3294,  3403,  1746,   548,  1746,  1859,  -503,
    -503,  -503,  1021,  -503,  -503,  1479,  1479,  1555,   342,  1746,
    -503,   355,   319,   355,  -503,   354,   355,  -503,   406,   355,
     336,  1988,   348,   671,   336,  1988,  1746,  -503,    58,   672,
    4470,  1746,  1746,    35,   551,  -503,  -503,  -503,   278,   275,
    -503,   -45,  1746,   552,  -503,   675,    69,   555,   178,   427,
      49,  -503,  -503,  1746,  1746,  1746,  1746,  -503,  -503,  -503,
    1746,  5450,  1746,   556,  1746,  -503,  -503,  -503,  -503,  -503,
    -503,  -503,  -503,  -503,  -503,  -503,   264,  -503,  -503,   678,
     557,    37,   351,  -503,   360,  1555,  -503,   681,   370,  -503,
     374,   560,    99,   563,  -503,  -503,   380,   512,   561,  1746,
    1746,  -503,  5450,  -503,   562,   384,  1746,  -503,   564,  -503,
    -503,  2693,  -503,  -503,  4764,  -503,  -503,  4802,  4867,  4905,
      35,   484,  4970,  -503,  -503,  1746,  -503,  5008,  -503,  5073,
    -503,  -503,  1746,  1746,   110,  -503,  5450,  1746,  3441,  1746,
    3506,   387,   403,   566,  5450,  -503,  -503,   486,  -503,   489,
    -503,   491,   413,    41,   683,    10,   275,   275,   275,  1988,
    -503,  2343,   336,  1988,   570,   421,  1988,   638,  5450,  -503,
    4662,  -503,  5111,  5176,   493,  -503,   275,   571,   569,  -503,
     576,  5450,  -503,   578,  -503,  1746,  -503,    18,  -503,   423,
     495,   700,  5450,  2963,  3028,  3072,  5450,  5450,  1746,  5450,
    -503,  -503,  -503,   -24,  -503,   581,   577,   583,   425,   434,
     586,  -503,   580,  -503,  -503,   587,   437,   577,  -503,   589,
    1746,  3544,  3609,  -503,   590,  3647,  -503,  2413,  2693,  1606,
    1746,  1746,   591,  1746,  2693,  3712,  2693,   -22,  5450,  5450,
    -503,  -503,  -503,  1021,  3750,  -503,  3815,  -503,   593,   594,
    -503,  -503,  -503,  -503,   595,   275,   120,   508,   508,   596,
      53,   124,   597,   598,  -503,  2483,  -503,   438,  1988,   655,
     340,   601,   656,  -503,  4566,  4662,  1691,  1746,   588,   275,
     724,  -503,  3853,  -503,   603,  -503,  -503,   447,   604,  -503,
    -503,  -503,  5450,  1742,   728,  -503,  -503,  -503,   607,   608,
    1746,  -503,  -503,   611,   449,  -503,  3918,  -503,  -503,  -503,
    -503,  -503,   699,   635,  1080,  -503,   688,   -52,  1165,  1216,
    1746,  3956,  -503,  -503,  -503,  2693,  -503,  -503,  -503,  -503,
    -503,  -503,  1988,   615,  -503,   616,   275,   508,   531,   240,
     617,   740,   535,   619,  -503,  -503,  -503,   620,   690,  -503,
      10,   275,  1988,  1988,  -503,  -503,   709,   645,  1301,  -503,
     698,   -33,  4021,   747,   624,   629,  -503,  -503,  -503,  -503,
    -503,  5214,   623,  -503,  -503,  5279,  -503,   634,  -503,  2693,
    2553,  -503,  -503,   710,  -503,  2623,  -503,   713,  -503,   715,
    4059,    35,  -503,  1988,   711,  -503,  -503,   643,   766,   648,
     536,   649,  -503,  1988,  -503,   651,    53,   176,   714,  1988,
     720,  4662,  2790,  -503,  -503,   729,  -503,  2886,    35,   654,
     781,  -503,  -503,   662,  -503,  -503,  -503,  -503,  -503,  -503,
    -503,  -503,  -503,  -503,    35,   472,   730,  -503,  -503,   663,
    -503,  -503,  1988,   731,  -503,   664,  -503,  -503,   732,  -503,
    -503,  -503,  -503,  -503,  -503,  -503,   478,  -503,   667,  1746,
     481,  2693,  -503,  -503,   737,  -503,  -503,  -503,  4662,  -503,
    5317,  2693,  -503,  -503,  -503,  -503,  -503
};

/* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
   Performed when YYTABLE does not specify something else to do.  Zero
   means the default is an error.  */
static const yytype_int16 yydefact[] =
{
       0,     0,    42,     0,     2,     4,     5,     6,     0,     0,
      44,    43,     1,     3,     0,     0,    12,     0,     0,     0,
     323,   322,   328,   329,   330,   331,   332,   333,   325,   326,
     324,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   366,    45,     0,    23,   282,   283,   284,     0,
       0,    16,     0,    27,     0,     9,     0,   295,   296,   294,
     305,   306,   297,     0,   298,   299,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   302,   303,   304,    41,
       0,     0,     0,     0,    27,    39,    36,    28,    29,    37,
      38,    33,    34,    35,    30,    31,    32,    40,     0,     0,
       0,     0,     0,   334,   337,     0,   371,   373,   372,   368,
     370,   369,   367,     0,     0,     0,   309,   311,   374,   375,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    11,
       0,   126,   286,   293,   289,   285,   287,   292,   290,   288,
      14,     0,     0,    17,     0,     0,     0,     0,     0,     0,
       0,     0,   270,     0,     0,     0,     0,     0,   252,     0,
     275,   300,   301,   277,     0,   270,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     166,   237,   234,   235,   236,     0,     0,     0,     0,     0,
     123,     0,     0,     0,     0,     0,     0,    47,     0,    84,
       0,    83,     0,     0,   245,     0,   243,     0,     0,     0,
       0,   302,   182,   174,   175,   176,   177,   178,   179,   181,
       0,   170,   180,   183,   165,     0,     0,     8,    26,     0,
       0,    48,    51,     0,     0,     0,     0,     0,   267,     0,
     335,   336,     0,   365,   312,     0,   307,   310,   350,   351,
     356,   355,   357,   359,   360,   349,   352,   353,   354,     0,
     345,   344,   346,   361,   362,   363,   347,   348,   339,   341,
     358,   340,   342,   343,     0,     0,     0,     0,    10,     0,
     291,    13,    15,     0,    19,     0,    18,     0,     7,     0,
     133,     0,   159,   161,   160,     0,     0,     0,   271,   274,
     151,   152,   153,     0,    75,    76,    77,    78,    79,    80,
      81,    82,     0,     0,     0,     0,    70,     0,     0,     0,
      55,     0,   233,     0,     0,     0,     0,     0,   202,     0,
     269,     0,     0,     0,     0,     0,     0,     0,   203,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   192,
     191,   190,     0,   219,   167,     0,     0,     0,     0,     0,
     121,     0,     0,     0,   113,     0,     0,   118,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   246,     0,     0,
       0,     0,     0,     0,     0,   168,   169,   164,     0,     0,
      52,     0,     0,     0,    56,     0,   277,     0,    48,     0,
       0,    46,   364,     0,     0,     0,     0,   281,   327,   308,
       0,   130,     0,     0,     0,   125,   313,   316,   317,   318,
     319,   320,   321,   315,   314,    24,     0,    20,    21,     0,
       0,     0,     0,   145,     0,     0,   163,     0,     0,   155,
       0,     0,     0,     0,   272,   273,     0,     0,     0,     0,
       0,   251,   253,   276,     0,     0,     0,   215,     0,   213,
     214,     0,   201,   268,     0,   212,   220,     0,     0,     0,
       0,     0,     0,   205,   221,     0,   217,     0,   239,     0,
     231,   232,     0,     0,     0,   197,   200,     0,     0,     0,
       0,     0,     0,     0,   124,   122,   114,     0,   115,     0,
     119,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      99,     0,     0,     0,     0,     0,     0,     0,   244,   242,
       0,   171,     0,     0,     0,   173,     0,     0,     0,    53,
       0,    49,    64,    48,    50,     0,    65,     0,    57,    48,
       0,     0,   266,     0,     0,     0,   338,   128,     0,   127,
      25,    22,   131,     0,   146,     0,     0,     0,     0,     0,
     157,   162,     0,   158,   139,     0,     0,     0,   150,     0,
       0,     0,     0,   222,     0,     0,   216,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   198,   199,
     194,   193,   195,     0,     0,   208,     0,   206,     0,     0,
     134,   117,   116,   120,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    98,     0,    86,     0,     0,     0,
       0,     0,     0,    95,     0,     0,     0,     0,     0,     0,
       0,    54,     0,    60,     0,    62,    58,     0,     0,   279,
     280,   278,   129,     0,     0,   136,   144,   138,     0,     0,
       0,   154,   132,     0,     0,    74,     0,    73,    71,   223,
     238,   204,   210,     0,     0,   255,     0,     0,     0,     0,
       0,     0,   250,   218,   249,     0,   240,   196,   209,   207,
     137,   135,     0,     0,   107,     0,     0,     0,   100,   277,
       0,     0,   111,     0,   101,   102,    85,     0,     0,    89,
       0,     0,     0,     0,    94,   172,   184,     0,     0,   257,
       0,     0,     0,     0,     0,     0,    66,    61,    63,    59,
     148,     0,     0,   142,   143,     0,   140,     0,    72,     0,
       0,   224,   254,     0,   226,     0,   227,     0,   229,     0,
       0,     0,   241,     0,     0,   110,   108,     0,     0,     0,
     103,     0,   112,     0,    88,     0,     0,     0,     0,     0,
       0,     0,     0,   186,   256,     0,   188,     0,     0,     0,
       0,    69,   147,     0,   156,   141,   211,   263,   262,   225,
     259,   258,   228,   230,     0,     0,     0,    90,   109,     0,
     104,   105,     0,     0,   100,     0,   111,    87,     0,    96,
     185,   265,   264,   187,   261,   260,     0,    68,     0,     0,
       0,     0,    91,   106,     0,    92,   103,    97,     0,    67,
       0,     0,   247,    93,   189,   149,   248
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -503,  -503,  -503,   793,  -503,  -503,   782,  -387,   636,    24,
    -503,   390,     3,  -419,  -260,   159,   189,  -503,   326,  -503,
    -503,  -503,  -396,  -502,   191,   192,   193,    16,   411,  -503,
     496,   195,  -373,   218,  -165,  -503,   214,   708,   208,  -503,
    -233,  -249,  -503,   174,  -503,  -503,   186,    -6,  -503,   400,
     -18,  -503,  -503,  -503,  -361,  -336,  -228,  -503,  -363,    72,
    -319,    73,    -1,  -197,   -13,   125,   229,   -14,    19,  -503,
      88,  -503,   540,   356,    -8
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
       0,     3,     4,     5,     6,    17,    18,    50,    51,    83,
      84,    85,   242,   262,   263,   243,   244,   175,   342,   230,
      89,    90,   539,   540,   245,   246,   247,   219,   220,   150,
     151,   248,   462,   463,   176,   468,   469,   171,   249,    96,
     250,   251,   252,   226,   623,   514,   515,   360,   235,   236,
     211,   212,   213,   214,   177,   178,   694,   738,   695,   739,
     696,   740,   697,   361,   215,   184,   328,   329,    98,    99,
      42,   115,   116,   455,   268
};

/* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule whose
   number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
      97,   416,    43,   371,   410,   429,   564,   104,   501,   546,
     343,   481,   218,   532,   521,   183,   385,   545,   705,     8,
     163,    86,   261,   106,   107,   108,   109,   110,   111,   112,
     113,   117,   118,   119,    52,    97,   164,   644,   218,   228,
     172,   418,   583,   179,   644,   407,   183,   305,   316,   221,
     428,   458,   554,   765,   569,   229,    86,   253,   719,   146,
     210,   101,   635,   233,   172,   227,    97,   172,   172,   102,
     216,    15,   797,    16,   254,    45,   433,   167,    46,    47,
      48,   168,   559,   472,   500,   222,   224,    86,   165,    12,
     271,   165,   588,   408,   269,   433,     1,   272,    44,   596,
     267,   673,   147,   148,   234,   706,   322,   323,   258,   674,
     386,    19,   278,   279,   280,   281,   282,   283,   284,   285,
     286,   287,   288,   289,   290,   291,   292,   293,   294,   295,
     296,   297,   298,   299,   300,   301,   302,   303,   330,   331,
     165,   169,   379,   165,   180,   663,   644,   648,   165,   100,
     165,   165,   668,   620,   180,   647,   584,   315,   419,   180,
       2,   416,   344,   345,   612,    39,   165,   165,   180,   326,
     570,   146,   105,   353,   165,   165,   165,    87,   165,   165,
     149,    52,   165,   173,   363,   324,   165,   173,   174,    39,
     217,   368,    39,    39,   373,   374,    49,   349,   565,   378,
     169,   170,   274,   384,   541,   277,   161,    88,   162,    91,
      92,    93,    87,    94,   147,   148,   388,   332,   159,   253,
     517,   519,   380,   259,   684,   595,    95,   325,     9,    10,
     644,   461,   253,   122,   123,   124,   621,   392,   622,   395,
     209,   398,    88,    87,    91,    92,    93,   714,    94,   417,
     103,   722,   181,   165,   732,   255,   381,   165,   319,   333,
     320,    95,   382,   180,   180,   160,   165,   117,   446,   127,
      11,   644,   182,    88,   180,    91,    92,    93,   180,    94,
     183,   166,   447,   448,   449,   180,   127,   644,   180,   450,
     451,   452,    95,   308,   607,   309,   441,   180,   223,   225,
     351,   231,   352,   826,   143,   144,   145,   422,   102,   165,
     453,   165,   354,   356,   357,   475,   773,   654,   464,   142,
     644,   143,   144,   145,   470,   152,   153,   260,   265,   154,
     478,   762,   476,   270,   179,   762,   762,   789,   346,   347,
     482,    45,   645,   180,    46,    47,    48,   454,   533,   534,
     485,   730,   390,   391,   494,   493,   179,   497,   498,   499,
     218,   731,   502,   537,   538,   493,   414,   507,   349,   509,
     394,   391,   511,   165,   516,   763,   306,   518,   520,   767,
     769,   524,   698,   699,   456,   421,   522,   822,   165,   427,
       7,   232,   253,   275,     7,   317,   276,   321,   548,   547,
     179,   397,   391,   552,   553,   416,   736,   208,   556,   527,
     815,   165,   529,   256,   561,   531,   355,    14,    15,    52,
      16,   257,   400,    52,   401,   572,   573,   574,   575,   424,
     425,   180,   576,   266,   577,   180,   579,   836,   122,   123,
     124,   125,   126,   155,   156,   157,   526,   391,   158,   180,
     393,   102,   396,   840,   399,    39,   404,   180,   405,   180,
     403,   432,   304,   433,   589,   471,   180,   433,   523,   307,
     433,   601,   602,   542,   483,   543,   310,   585,   605,   586,
     488,   528,   391,   122,   123,   124,   587,   179,   433,   180,
     423,   127,   311,   180,   430,   313,   591,   615,   592,   314,
     593,   180,   433,   318,   618,   619,   598,   327,   433,   624,
     604,   626,   433,   628,   348,   586,   135,   136,   350,   137,
     138,   139,   140,   141,   142,   349,   143,   144,   145,   629,
     362,   433,   253,   530,   391,   493,   127,   649,   364,   634,
     652,   162,   830,   832,   558,   457,   459,   651,   835,   162,
     665,   678,   422,   586,   568,   425,   473,   662,   474,   372,
     679,    52,   433,   683,   727,   586,   162,   140,   141,   142,
     672,   143,   144,   145,   748,   757,   422,   586,   365,   180,
     334,   335,   336,   337,   338,   339,   340,   341,   180,  -215,
     366,  -215,   686,  -213,  -216,  -213,  -216,   376,   841,   854,
     347,   493,   692,   389,   848,   701,   347,   851,   702,   347,
     704,   613,   347,   631,   391,   516,   632,   391,   633,   391,
     657,   347,   666,   425,   367,   369,   370,   180,   375,   180,
     377,   180,   387,   383,   180,   402,   253,   253,   406,   493,
     411,   165,   728,   412,   413,   426,   431,   557,   420,   742,
     560,   442,   443,   444,   465,   741,   477,   567,   636,   571,
     639,   641,   642,   643,   491,   751,   479,   480,   486,   487,
     489,   490,   755,   496,   504,   508,   544,   550,   555,   562,
     563,   658,   566,   581,   582,   578,   590,   594,   597,   603,
     600,   606,   770,   630,   638,   180,   180,   650,   653,   772,
     660,   659,   180,   661,   180,   667,   774,   422,   675,   461,
     677,   680,   467,   729,   682,   685,   734,   689,   700,   743,
     710,   711,   712,   718,   724,   725,   788,   790,   733,   745,
     747,   749,   752,   180,   753,   754,   180,   741,   756,   759,
     760,   764,   775,   776,   780,   781,   782,   783,   784,   791,
     792,   796,   799,   806,   808,   800,   801,   803,   179,   811,
     713,   805,   637,   809,   640,   720,   812,   816,   813,   817,
     818,   819,   827,   253,   253,   820,   821,   823,   824,   253,
     829,   837,   833,   828,   744,   179,   838,   839,   842,   845,
     843,   846,   847,   180,   849,   853,   664,    13,   312,    53,
     180,   179,   525,   599,   676,   445,   681,   264,   549,   707,
     794,   795,   580,     0,     0,   439,   844,     0,     0,     0,
     180,   180,     0,     0,     0,     0,     0,     0,     0,     0,
     253,   850,     0,     0,     0,   852,     0,     0,     0,     0,
       0,   777,     0,     0,     0,   856,     0,   180,   180,     0,
       0,     0,     0,   180,     0,   785,   787,     0,     0,   180,
       0,   180,     0,     0,     0,   715,   716,   717,     0,   721,
     723,   180,     0,    20,    21,     0,     0,   180,     0,     0,
       0,     0,     0,     0,     0,     0,   180,    22,    23,    24,
       0,     0,     0,     0,    25,    26,    27,     0,     0,     0,
       0,     0,   180,     0,     0,     0,     0,     0,     0,     0,
     180,   825,     0,     0,     0,    28,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   180,
       0,     0,     0,     0,     0,     0,    29,     0,     0,   180,
       0,     0,     0,     0,     0,     0,   778,     0,   779,    20,
      21,     0,    30,     0,     0,     0,     0,     0,     0,   786,
      31,    32,    33,    22,    23,    24,     0,     0,     0,     0,
      25,    26,    27,     0,     0,    34,    35,    36,     0,     0,
       0,     0,     0,     0,     0,    37,     0,     0,     0,     0,
       0,    28,     0,     0,    38,   460,     0,     0,     0,    39,
       0,   461,     0,     0,     0,    40,    41,   122,   123,   124,
     125,   126,    29,     0,     0,   721,   723,     0,     0,     0,
       0,     0,     0,     0,     0,    20,    21,     0,    30,     0,
       0,     0,     0,     0,     0,     0,    31,    32,    33,    22,
      23,    24,     0,     0,     0,     0,    25,    26,    27,     0,
       0,    34,    35,    36,     0,     0,     0,     0,     0,     0,
     127,    37,   512,   513,     0,     0,     0,    28,     0,     0,
      38,   466,     0,     0,     0,    39,     0,   467,     0,     0,
       0,    40,    41,     0,    20,    21,     0,     0,    29,   138,
     139,   140,   141,   142,     0,   143,   144,   145,    22,    23,
      24,     0,     0,     0,    30,    25,    26,    27,     0,     0,
       0,     0,    31,    32,    33,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    28,    34,    35,    36,
       0,     0,     0,   761,   693,     0,     0,    37,     0,     0,
       0,     0,     0,     0,     0,     0,    38,    29,     0,     0,
       0,    39,     0,     0,     0,     0,     0,    40,    41,     0,
       0,     0,     0,    30,     0,     0,     0,     0,     0,    20,
      21,    31,    32,    33,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    22,    23,    24,    34,    35,    36,     0,
      25,    26,    27,     0,     0,     0,    37,     0,     0,     0,
       0,     0,     0,     0,     0,    38,     0,     0,     0,     0,
      39,    28,     0,     0,     0,     0,    40,    41,   766,   693,
      20,    21,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    29,     0,    22,    23,    24,     0,     0,     0,
       0,    25,    26,    27,     0,     0,     0,     0,    30,     0,
       0,     0,     0,     0,     0,     0,    31,    32,    33,     0,
       0,     0,    28,     0,     0,     0,     0,     0,     0,   768,
     693,    34,    35,    36,     0,     0,     0,     0,     0,     0,
       0,    37,     0,    29,     0,     0,     0,     0,     0,     0,
      38,     0,     0,     0,     0,    39,     0,     0,     0,    30,
       0,    40,    41,     0,     0,    20,    21,    31,    32,    33,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    22,
      23,    24,    34,    35,    36,     0,    25,    26,    27,     0,
       0,     0,    37,     0,     0,     0,     0,     0,     0,     0,
       0,    38,     0,     0,     0,     0,    39,    28,     0,     0,
       0,     0,    40,    41,   793,   737,    20,    21,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    29,     0,
      22,    23,    24,     0,     0,     0,     0,    25,    26,    27,
       0,     0,     0,     0,    30,     0,     0,     0,     0,     0,
       0,     0,    31,    32,    33,     0,     0,     0,    28,     0,
       0,     0,     0,     0,     0,     0,     0,    34,    35,    36,
       0,     0,     0,     0,     0,     0,     0,    37,     0,    29,
       0,     0,     0,     0,     0,     0,    38,     0,     0,     0,
       0,    39,    20,    21,     0,    30,     0,    40,    41,     0,
       0,     0,     0,    31,    32,    33,    22,    23,    24,     0,
       0,     0,     0,    25,    26,    27,     0,     0,    34,    35,
      36,   114,     0,     0,     0,     0,     0,     0,    37,     0,
       0,     0,     0,     0,    28,     0,     0,    38,     0,     0,
       0,     0,    39,    20,    21,     0,     0,     0,    40,    41,
       0,     0,     0,     0,     0,    29,     0,    22,    23,    24,
       0,     0,     0,     0,    25,    26,    27,     0,     0,     0,
       0,    30,     0,     0,     0,     0,     0,     0,     0,    31,
      32,    33,     0,     0,     0,    28,     0,     0,     0,     0,
       0,     0,     0,     0,    34,    35,    36,     0,     0,     0,
       0,     0,     0,     0,    37,     0,    29,     0,     0,     0,
       0,     0,     0,    38,   484,     0,     0,     0,    39,    20,
      21,     0,    30,     0,    40,    41,     0,     0,     0,     0,
      31,    32,    33,    22,    23,    24,     0,     0,     0,     0,
      25,    26,    27,     0,     0,    34,    35,    36,     0,     0,
       0,     0,     0,     0,     0,    37,     0,     0,     0,     0,
       0,    28,     0,   173,    38,     0,     0,     0,     0,    39,
      20,    21,     0,     0,     0,    40,    41,     0,     0,     0,
       0,     0,    29,     0,    22,    23,    24,     0,     0,     0,
       0,    25,    26,    27,     0,     0,     0,     0,    30,     0,
       0,     0,     0,     0,     0,     0,    31,    32,    33,     0,
       0,     0,    28,     0,     0,     0,     0,     0,     0,     0,
     693,    34,    35,    36,     0,     0,     0,     0,     0,     0,
       0,    37,     0,    29,     0,     0,     0,     0,     0,     0,
      38,     0,     0,     0,     0,    39,     0,   461,     0,    30,
       0,    40,    41,     0,     0,    20,    21,    31,    32,    33,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    22,
      23,    24,    34,    35,    36,     0,    25,    26,    27,     0,
       0,     0,    37,     0,     0,     0,     0,     0,     0,     0,
       0,    38,     0,     0,     0,     0,    39,    28,     0,     0,
       0,     0,    40,    41,     0,   737,    20,    21,     0,     0,
      20,    21,     0,     0,     0,     0,     0,     0,    29,     0,
      22,    23,    24,     0,    22,    23,    24,    25,    26,    27,
       0,    25,    26,    27,    30,     0,     0,     0,     0,     0,
       0,     0,    31,    32,    33,     0,     0,     0,    28,     0,
       0,     0,    28,     0,     0,     0,     0,    34,    35,    36,
       0,     0,     0,     0,     0,     0,     0,    37,     0,    29,
       0,     0,     0,    29,     0,     0,    38,     0,     0,     0,
       0,    39,     0,     0,     0,    30,     0,    40,    41,    30,
       0,     0,     0,    31,    32,    33,     0,    31,    32,    33,
       0,     0,     0,     0,     0,     0,     0,     0,    34,    35,
      36,     0,    34,    35,    36,     0,     0,     0,    37,     0,
       0,     0,    37,     0,   185,     0,   186,    38,   750,     0,
     187,    38,    39,     0,     0,     0,    39,     0,    40,    41,
     188,   189,    40,    41,     0,     0,     0,     0,   120,   121,
     122,   123,   124,   125,   126,     0,   190,     0,   191,     0,
       0,     0,     0,   192,   193,     0,     0,     0,     0,   194,
     195,   196,     0,     0,     0,   197,     0,     0,     0,     0,
     198,   199,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   200,     0,   201,    74,     0,
       0,     0,     0,   127,     0,     0,     0,     0,   202,   203,
     128,   129,   130,   204,     0,     0,     0,   205,     0,     0,
       0,     0,   206,   131,     0,   132,   133,   134,   135,   136,
       0,   137,   138,   139,   140,   141,   142,     0,   143,   144,
     145,     0,     0,   207,     0,     0,   510,     0,     0,    39,
       0,     0,     0,   185,   208,   186,   533,   534,     0,   535,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   536,
     189,   537,   538,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   190,     0,   191,     0,     0,
       0,     0,   192,   193,     0,     0,     0,     0,   194,   195,
     196,     0,     0,     0,   197,     0,     0,     0,     0,   198,
     199,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   185,   200,   186,   201,    74,     0,   187,
       0,     0,     0,     0,     0,     0,     0,   202,   203,   188,
     189,     0,   204,     0,     0,     0,   205,     0,     0,     0,
       0,   206,     0,     0,     0,   190,   358,   191,     0,     0,
       0,     0,   192,   193,     0,     0,     0,     0,   194,   195,
     196,     0,   207,     0,   197,     0,     0,     0,    39,   198,
     199,     0,     0,   208,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   185,   200,   186,   201,    74,     0,   187,
       0,     0,     0,     0,     0,     0,     0,   202,   203,   188,
     189,     0,   204,     0,     0,     0,   205,     0,     0,     0,
       0,   206,     0,   359,     0,   190,     0,   191,     0,     0,
       0,     0,   192,   193,     0,     0,     0,     0,   194,   195,
     196,     0,   207,     0,   197,     0,     0,     0,    39,   198,
     199,     0,     0,   208,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   185,   200,   186,   201,    74,     0,   187,
       0,     0,     0,     0,     0,     0,     0,   202,   203,   188,
     189,     0,   204,     0,     0,     0,   205,     0,     0,     0,
       0,   206,     0,     0,     0,   190,   492,   191,     0,     0,
       0,     0,   192,   193,     0,     0,     0,     0,   194,   195,
     196,     0,   207,     0,   197,   383,     0,     0,    39,   198,
     199,     0,     0,   208,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   185,   200,   186,   201,    74,     0,   187,
       0,     0,     0,     0,     0,     0,     0,   202,   203,   188,
     189,     0,   204,     0,     0,     0,   205,     0,     0,     0,
       0,   206,     0,     0,     0,   190,     0,   191,     0,     0,
       0,     0,   192,   193,     0,     0,     0,     0,   194,   195,
     196,     0,   207,     0,   197,     0,     0,     0,    39,   198,
     199,     0,     0,   208,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   200,   503,   201,    74,   185,     0,
     186,     0,     0,     0,   187,     0,     0,   202,   203,     0,
       0,     0,   204,     0,   188,   189,   205,     0,     0,     0,
       0,   206,     0,     0,     0,     0,     0,     0,     0,     0,
     190,     0,   191,     0,     0,     0,     0,   192,   193,     0,
       0,     0,   207,   194,   195,   196,     0,     0,    39,   197,
       0,   646,     0,   208,   198,   199,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   185,   200,
     186,   201,    74,     0,   187,     0,     0,     0,     0,     0,
       0,     0,   202,   203,   188,   189,     0,   204,     0,     0,
       0,   205,     0,     0,     0,     0,   206,     0,     0,     0,
     190,   691,   191,     0,     0,     0,     0,   192,   193,     0,
       0,     0,     0,   194,   195,   196,     0,   207,     0,   197,
       0,     0,     0,    39,   198,   199,     0,     0,   208,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   185,   200,
     186,   201,    74,     0,   187,     0,     0,     0,     0,     0,
       0,     0,   202,   203,   188,   189,     0,   204,     0,     0,
       0,   205,     0,     0,     0,     0,   206,     0,     0,     0,
     190,     0,   191,     0,     0,     0,     0,   192,   193,     0,
       0,     0,     0,   194,   195,   196,     0,   207,     0,   197,
       0,   726,     0,    39,   198,   199,     0,     0,   208,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   185,   200,
     186,   201,    74,     0,   187,     0,     0,     0,     0,     0,
       0,     0,   202,   203,   188,   189,     0,   204,     0,     0,
       0,   205,     0,     0,     0,     0,   206,     0,     0,     0,
     190,     0,   191,     0,     0,     0,     0,   192,   193,     0,
       0,     0,     0,   194,   195,   196,     0,   207,     0,   197,
       0,     0,     0,    39,   198,   199,     0,     0,   208,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   185,   200,
     186,   201,    74,     0,   187,     0,     0,     0,     0,     0,
       0,     0,   202,   203,   188,   189,     0,   204,     0,     0,
       0,   205,     0,     0,     0,     0,   206,     0,     0,     0,
     190,     0,   191,     0,     0,     0,     0,   192,   193,     0,
       0,     0,     0,   194,   195,   196,     0,   207,     0,   197,
     807,     0,     0,    39,   198,   199,     0,     0,   208,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   185,   200,
     186,   201,    74,     0,   187,     0,     0,     0,     0,     0,
       0,     0,   202,   203,   188,   189,     0,   204,     0,     0,
       0,   205,     0,     0,     0,     0,   206,     0,     0,     0,
     190,     0,   191,     0,     0,     0,     0,   192,   193,     0,
       0,     0,     0,   194,   195,   196,     0,   207,     0,   197,
     810,     0,     0,    39,   198,   199,     0,     0,   208,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   200,
       0,   201,    74,     0,     0,   120,     0,   122,   123,   124,
     125,   126,   202,   203,     0,     0,     0,   204,     0,     0,
       0,   205,     0,     0,     0,    54,   206,    56,    46,    47,
      48,    57,    58,    59,    60,    61,    62,    63,     0,     0,
       0,    64,     0,    65,     0,     0,     0,   207,     0,     0,
       0,     0,     0,    39,     0,     0,    66,   237,   208,   238,
     127,     0,     0,    67,     0,     0,     0,    68,    69,    70,
     239,     0,     0,     0,     0,    71,     0,     0,     0,     0,
       0,   240,     0,     0,   134,   135,   136,     0,   137,   138,
     139,   140,   141,   142,     0,   143,   144,   145,     0,    74,
       0,     0,     0,     0,     0,     0,     0,     0,   241,     0,
       0,     0,     0,     0,     0,    77,    78,     0,     0,    80,
      81,    54,    82,    56,    46,    47,    48,    57,    58,    59,
      60,    61,    62,    63,     0,     0,     0,    64,     0,    65,
       0,     0,     0,     0,     0,     0,     0,   831,     0,     0,
       0,     0,    66,   237,     0,   238,     0,     0,     0,    67,
       0,     0,     0,    68,    69,    70,   239,     0,     0,     0,
       0,    71,     0,     0,     0,     0,     0,   240,   120,   121,
     122,   123,   124,   125,   126,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    74,     0,     0,     0,     0,
       0,     0,     0,     0,   241,     0,     0,     0,     0,     0,
       0,    77,    78,     0,     0,    80,    81,     0,    82,     0,
       0,     0,   120,   121,   122,   123,   124,   125,   126,     0,
     434,   435,     0,   127,     0,     0,     0,     0,     0,     0,
     128,   129,   130,   834,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   131,   436,   132,   133,   134,   135,   136,
       0,   137,   138,   139,   140,   141,   142,     0,   143,   144,
     145,     0,     0,     0,     0,     0,     0,   127,     0,     0,
       0,     0,     0,   437,   128,   129,   130,   120,   121,   122,
     123,   124,   125,   126,     0,     0,     0,   131,     0,   132,
     133,   134,   135,   136,     0,   137,   138,   139,   140,   141,
     142,     0,   143,   144,   145,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   669,     0,     0,
       0,   120,   121,   122,   123,   124,   125,   126,     0,     0,
       0,     0,   127,     0,     0,     0,     0,     0,     0,   128,
     129,   130,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   131,     0,   132,   133,   134,   135,   136,     0,
     137,   138,   139,   140,   141,   142,     0,   143,   144,   145,
       0,     0,     0,     0,     0,     0,   127,     0,     0,     0,
       0,     0,   670,   128,   129,   130,   120,   121,   122,   123,
     124,   125,   126,     0,     0,     0,   131,     0,   132,   133,
     134,   135,   136,     0,   137,   138,   139,   140,   141,   142,
       0,   143,   144,   145,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   671,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   127,     0,     0,     0,     0,     0,     0,   128,   129,
     130,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   131,     0,   132,   133,   134,   135,   136,     0,   137,
     138,   139,   140,   141,   142,     0,   143,   144,   145,     0,
       0,     0,     0,     0,     0,     0,    54,    39,    56,    46,
      47,    48,    57,    58,    59,    60,    61,    62,    63,     0,
       0,     0,    64,     0,    65,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    66,   237,     0,
     238,     0,     0,     0,    67,     0,     0,     0,    68,    69,
      70,   239,     0,     0,     0,     0,    71,     0,     0,     0,
       0,     0,   240,   120,   121,   122,   123,   124,   125,   126,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      74,     0,     0,     0,     0,     0,     0,     0,     0,   241,
       0,     0,     0,     0,     0,     0,    77,    78,     0,     0,
      80,    81,     0,    82,     0,     0,   409,   120,   121,   122,
     123,   124,   125,   126,     0,     0,     0,     0,   127,     0,
       0,     0,     0,     0,     0,   128,   129,   130,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   131,     0,
     132,   133,   134,   135,   136,     0,   137,   138,   139,   140,
     141,   142,     0,   143,   144,   145,     0,     0,     0,     0,
       0,     0,   127,   505,     0,     0,     0,     0,     0,   128,
     129,   130,   120,   121,   122,   123,   124,   125,   126,     0,
       0,     0,   131,     0,   132,   133,   134,   135,   136,     0,
     137,   138,   139,   140,   141,   142,     0,   143,   144,   145,
       0,     0,     0,     0,     0,   495,     0,     0,     0,     0,
     120,   121,   122,   123,   124,   125,   126,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   127,     0,     0,
       0,     0,     0,     0,   128,   129,   130,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   131,     0,   132,
     133,   134,   135,   136,     0,   137,   138,   139,   140,   141,
     142,     0,   143,   144,   145,   127,     0,     0,     0,     0,
     506,     0,   128,   129,   130,   120,   121,   122,   123,   124,
     125,   126,     0,     0,     0,   131,     0,   132,   133,   134,
     135,   136,     0,   137,   138,   139,   140,   141,   142,     0,
     143,   144,   145,     0,     0,     0,     0,     0,   625,     0,
       0,     0,     0,   120,   121,   122,   123,   124,   125,   126,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     127,     0,     0,     0,     0,     0,     0,   128,   129,   130,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     131,     0,   132,   133,   134,   135,   136,     0,   137,   138,
     139,   140,   141,   142,     0,   143,   144,   145,   127,     0,
       0,     0,     0,   627,     0,   128,   129,   130,   120,   121,
     122,   123,   124,   125,   126,     0,     0,     0,   131,     0,
     132,   133,   134,   135,   136,     0,   137,   138,   139,   140,
     141,   142,     0,   143,   144,   145,     0,     0,     0,     0,
       0,   687,     0,     0,     0,     0,   120,   121,   122,   123,
     124,   125,   126,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   127,     0,     0,     0,     0,     0,     0,
     128,   129,   130,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   131,     0,   132,   133,   134,   135,   136,
       0,   137,   138,   139,   140,   141,   142,     0,   143,   144,
     145,   127,     0,     0,     0,     0,   688,     0,   128,   129,
     130,   120,   121,   122,   123,   124,   125,   126,     0,     0,
       0,   131,     0,   132,   133,   134,   135,   136,     0,   137,
     138,   139,   140,   141,   142,     0,   143,   144,   145,     0,
       0,     0,     0,     0,   690,     0,     0,     0,     0,   120,
     121,   122,   123,   124,   125,   126,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   127,     0,     0,     0,
       0,     0,     0,   128,   129,   130,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   131,     0,   132,   133,
     134,   135,   136,     0,   137,   138,   139,   140,   141,   142,
       0,   143,   144,   145,   127,     0,     0,     0,     0,   703,
       0,   128,   129,   130,   120,   121,   122,   123,   124,   125,
     126,     0,     0,     0,   131,     0,   132,   133,   134,   135,
     136,     0,   137,   138,   139,   140,   141,   142,     0,   143,
     144,   145,     0,     0,     0,     0,     0,   708,     0,     0,
       0,     0,   120,   121,   122,   123,   124,   125,   126,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   127,
       0,     0,     0,     0,     0,     0,   128,   129,   130,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   131,
       0,   132,   133,   134,   135,   136,     0,   137,   138,   139,
     140,   141,   142,     0,   143,   144,   145,   127,     0,     0,
       0,     0,   709,     0,   128,   129,   130,   120,   121,   122,
     123,   124,   125,   126,     0,     0,     0,   131,     0,   132,
     133,   134,   135,   136,     0,   137,   138,   139,   140,   141,
     142,     0,   143,   144,   145,     0,     0,     0,     0,     0,
     746,     0,     0,     0,     0,   120,   121,   122,   123,   124,
     125,   126,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   127,     0,     0,     0,     0,     0,     0,   128,
     129,   130,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   131,     0,   132,   133,   134,   135,   136,     0,
     137,   138,   139,   140,   141,   142,     0,   143,   144,   145,
     127,     0,     0,     0,     0,   758,     0,   128,   129,   130,
     120,   121,   122,   123,   124,   125,   126,     0,     0,     0,
     131,     0,   132,   133,   134,   135,   136,     0,   137,   138,
     139,   140,   141,   142,     0,   143,   144,   145,     0,     0,
       0,     0,     0,   771,     0,     0,     0,     0,   120,   121,
     122,   123,   124,   125,   126,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   127,     0,     0,     0,     0,
       0,     0,   128,   129,   130,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   131,     0,   132,   133,   134,
     135,   136,     0,   137,   138,   139,   140,   141,   142,     0,
     143,   144,   145,   127,     0,     0,     0,     0,   798,     0,
     128,   129,   130,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   131,     0,   132,   133,   134,   135,   136,
       0,   137,   138,   139,   140,   141,   142,     0,   143,   144,
     145,     0,     0,     0,     0,     0,   814,    54,    55,    56,
      46,    47,    48,    57,    58,    59,    60,    61,    62,    63,
       0,     0,     0,    64,     0,    65,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    66,     0,
       0,     0,     0,     0,     0,    67,     0,     0,     0,    68,
      69,    70,     0,     0,     0,     0,     0,    71,     0,    72,
       0,    73,     0,     0,     0,     0,     0,     0,     0,     2,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    74,     0,     0,     0,     0,     0,     0,    75,     0,
      76,     0,     0,     0,     0,     0,     0,    77,    78,    79,
       0,    80,    81,    54,    82,    56,    46,    47,    48,    57,
      58,    59,    60,    61,    62,    63,     0,     0,     0,    64,
       0,    65,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    66,     0,     0,     0,     0,     0,
       0,    67,     0,     0,     0,    68,    69,    70,     0,     0,
       0,     0,     0,    71,     0,    72,     0,    73,     0,     0,
       0,     0,     0,     0,     0,     2,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    74,     0,     0,
       0,     0,     0,     0,    75,     0,    76,     0,     0,     0,
       0,     0,     0,    77,    78,    79,     0,    80,    81,    54,
      82,    56,    46,    47,    48,    57,    58,    59,    60,    61,
      62,    63,     0,     0,     0,    64,     0,    65,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      66,   237,     0,   238,     0,     0,     0,    67,     0,     0,
       0,    68,    69,    70,   239,     0,     0,     0,     0,    71,
       0,     0,     0,     0,     0,   240,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
       0,   415,   241,     0,     0,     0,     0,     0,     0,    77,
      78,     0,     0,    80,    81,    54,    82,    56,    46,    47,
      48,    57,    58,    59,    60,    61,    62,    63,     0,     0,
       0,    64,     0,    65,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    66,   237,   551,   238,
       0,     0,     0,    67,     0,     0,     0,    68,    69,    70,
     239,     0,     0,     0,     0,    71,     0,     0,     0,     0,
       0,   240,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    74,
       0,   120,     0,   122,   123,   124,   125,   126,   241,     0,
       0,     0,     0,     0,     0,    77,    78,     0,     0,    80,
      81,    54,    82,    56,    46,    47,    48,    57,    58,    59,
      60,    61,    62,    63,     0,     0,     0,    64,     0,    65,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    66,   237,   735,   238,   127,     0,     0,    67,
       0,     0,     0,    68,    69,    70,   239,     0,     0,     0,
       0,    71,     0,     0,     0,     0,     0,   240,     0,     0,
       0,   135,   136,     0,   137,   138,   139,   140,   141,   142,
       0,   143,   144,   145,     0,    74,     0,     0,     0,     0,
       0,     0,     0,     0,   241,     0,     0,     0,     0,     0,
       0,    77,    78,     0,     0,    80,    81,    54,    82,    56,
      46,    47,    48,    57,    58,    59,    60,    61,    62,    63,
       0,     0,     0,    64,     0,    65,     0,     0,     0,     0,
     120,   121,   122,   123,   124,   125,   126,     0,    66,   237,
       0,   238,     0,     0,     0,    67,     0,     0,     0,    68,
      69,    70,   239,     0,     0,     0,     0,    71,     0,     0,
       0,     0,     0,   240,     0,     0,     0,     0,   120,   121,
     122,   123,   124,   125,   126,     0,     0,     0,     0,     0,
       0,    74,     0,     0,     0,   127,     0,     0,     0,     0,
     241,     0,   128,   129,   130,     0,     0,    77,    78,     0,
       0,    80,    81,     0,    82,   131,     0,   132,   133,   134,
     135,   136,     0,   137,   138,   139,   140,   141,   142,     0,
     143,   144,   145,   127,     0,     0,     0,   273,     0,     0,
     128,   129,   130,   120,   121,   122,   123,   124,   125,   126,
       0,     0,     0,   131,     0,   132,   133,   134,   135,   136,
       0,   137,   138,   139,   140,   141,   142,     0,   143,   144,
     145,     0,     0,     0,     0,   438,     0,     0,     0,     0,
       0,   120,   121,   122,   123,   124,   125,   126,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   127,     0,
       0,     0,     0,     0,     0,   128,   129,   130,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   131,     0,
     132,   133,   134,   135,   136,     0,   137,   138,   139,   140,
     141,   142,     0,   143,   144,   145,   127,     0,     0,     0,
     608,     0,     0,   128,   129,   130,   120,   121,   122,   123,
     124,   125,   126,     0,     0,     0,   131,     0,   132,   133,
     134,   135,   136,     0,   137,   138,   139,   140,   141,   142,
       0,   143,   144,   145,     0,     0,     0,     0,   609,     0,
       0,     0,     0,     0,   120,   121,   122,   123,   124,   125,
     126,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   127,     0,     0,     0,     0,     0,     0,   128,   129,
     130,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   131,     0,   132,   133,   134,   135,   136,     0,   137,
     138,   139,   140,   141,   142,     0,   143,   144,   145,   127,
       0,     0,     0,   610,     0,     0,   128,   129,   130,   120,
     121,   122,   123,   124,   125,   126,     0,     0,     0,   131,
       0,   132,   133,   134,   135,   136,     0,   137,   138,   139,
     140,   141,   142,     0,   143,   144,   145,     0,     0,     0,
       0,   611,     0,     0,     0,     0,     0,   120,   121,   122,
     123,   124,   125,   126,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   127,     0,     0,     0,     0,     0,
       0,   128,   129,   130,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   131,     0,   132,   133,   134,   135,
     136,     0,   137,   138,   139,   140,   141,   142,     0,   143,
     144,   145,   127,     0,     0,     0,   614,     0,     0,   128,
     129,   130,   120,   121,   122,   123,   124,   125,   126,     0,
       0,     0,   131,     0,   132,   133,   134,   135,   136,     0,
     137,   138,   139,   140,   141,   142,     0,   143,   144,   145,
       0,     0,     0,     0,   616,     0,     0,     0,     0,     0,
     120,   121,   122,   123,   124,   125,   126,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   127,     0,     0,
       0,     0,     0,     0,   128,   129,   130,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   131,     0,   132,
     133,   134,   135,   136,     0,   137,   138,   139,   140,   141,
     142,     0,   143,   144,   145,   127,     0,     0,     0,   617,
       0,     0,   128,   129,   130,   120,   121,   122,   123,   124,
     125,   126,     0,     0,     0,   131,     0,   132,   133,   134,
     135,   136,     0,   137,   138,   139,   140,   141,   142,     0,
     143,   144,   145,     0,     0,     0,     0,   655,     0,     0,
       0,     0,     0,   120,   121,   122,   123,   124,   125,   126,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     127,     0,     0,     0,     0,     0,     0,   128,   129,   130,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     131,     0,   132,   133,   134,   135,   136,     0,   137,   138,
     139,   140,   141,   142,     0,   143,   144,   145,   127,     0,
       0,     0,   656,     0,     0,   128,   129,   130,   120,   121,
     122,   123,   124,   125,   126,     0,     0,     0,   131,     0,
     132,   133,   134,   135,   136,     0,   137,   138,   139,   140,
     141,   142,     0,   143,   144,   145,     0,     0,     0,     0,
     802,     0,     0,     0,     0,     0,   120,   121,   122,   123,
     124,   125,   126,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   127,     0,     0,     0,     0,     0,     0,
     128,   129,   130,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   131,     0,   132,   133,   134,   135,   136,
       0,   137,   138,   139,   140,   141,   142,     0,   143,   144,
     145,   127,     0,     0,     0,   804,     0,     0,   128,   129,
     130,   120,   121,   122,   123,   124,   125,   126,     0,     0,
       0,   131,     0,   132,   133,   134,   135,   136,     0,   137,
     138,   139,   140,   141,   142,     0,   143,   144,   145,     0,
       0,     0,     0,   855,     0,   120,   121,   122,   123,   124,
     125,   126,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   434,   435,     0,   127,     0,     0,     0,
       0,     0,     0,   128,   129,   130,     0,     0,     0,   120,
     121,   122,   123,   124,   125,   126,   131,   436,   132,   133,
     134,   135,   136,     0,   137,   138,   139,   140,   141,   142,
     127,   143,   144,   145,     0,     0,     0,   128,   129,   130,
       0,     0,     0,   120,   121,   122,   123,   124,   125,   126,
     131,   440,   132,   133,   134,   135,   136,     0,   137,   138,
     139,   140,   141,   142,   127,   143,   144,   145,     0,     0,
       0,   128,   129,   130,     0,     0,     0,   120,     0,   122,
     123,   124,   125,   126,   131,     0,   132,   133,   134,   135,
     136,     0,   137,   138,   139,   140,   141,   142,   127,   143,
     144,   145,     0,     0,     0,   128,   129,   130,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   133,   134,   135,   136,     0,   137,   138,   139,   140,
     141,   142,   127,   143,   144,   145,     0,     0,     0,   128,
     129,   130,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   133,   134,   135,   136,     0,
     137,   138,   139,   140,   141,   142,     0,   143,   144,   145
};

static const yytype_int16 yycheck[] =
{
      18,   250,    10,   200,   237,   265,   425,    21,   369,   405,
     175,   347,     5,   400,   387,     5,    35,   404,    40,     5,
       5,    18,     5,    31,    32,    33,    34,    35,    36,    37,
      38,    39,    40,    41,    15,    53,    21,   539,     5,     5,
       5,    13,     5,    56,   546,    80,     5,     5,     5,    16,
       5,     5,   413,   105,     5,    21,    53,    75,     5,     5,
      66,   125,    21,     5,     5,    71,    84,     5,     5,   133,
       5,   125,   105,   127,    80,     5,   128,    53,     8,     9,
      10,     5,   127,   125,    22,    69,    70,    84,   133,     0,
     104,   133,   465,   128,   102,   128,     3,   105,   125,   472,
     101,   125,    48,    49,    46,   127,     4,     5,    84,   133,
     129,     5,   120,   121,   122,   123,   124,   125,   126,   127,
     128,   129,   130,   131,   132,   133,   134,   135,   136,   137,
     138,   139,   140,   141,   142,   143,   144,   145,     4,     5,
     133,   124,     5,   133,    56,   127,   648,   543,   133,   120,
     133,   133,   571,    43,    66,   542,   119,   165,   130,    71,
      67,   410,   175,   176,   500,   130,   133,   133,    80,   170,
     430,     5,   125,   186,   133,   133,   133,    18,   133,   133,
     126,   162,   133,   124,   192,    83,   133,   124,   125,   130,
     125,   197,   130,   130,   202,   203,   126,   128,   129,   207,
     124,   125,   114,   209,   401,   117,   126,    18,   128,    18,
      18,    18,    53,    18,    48,    49,   217,    83,    12,   237,
     385,   386,    85,    98,   597,   126,    18,   125,     4,     5,
     732,   132,   250,    31,    32,    33,   126,   221,   128,   223,
      66,   225,    53,    84,    53,    53,    53,   127,    53,   255,
      21,   127,    16,   133,   650,    81,   119,   133,   125,   125,
     127,    53,   125,   175,   176,   127,   133,   275,     4,    84,
      46,   773,    16,    84,   186,    84,    84,    84,   190,    84,
       5,    52,    18,    19,    20,   197,    84,   789,   200,    25,
      26,    27,    84,   126,   491,   128,   304,   209,    69,    70,
     125,    72,   127,   127,   119,   120,   121,   129,   133,   133,
      46,   133,   187,   188,   189,   329,   712,   550,   319,   117,
     822,   119,   120,   121,   325,    12,    13,    98,    99,    16,
     343,   694,   333,   104,   347,   698,   699,   733,   127,   128,
     348,     5,   539,   255,     8,     9,    10,    83,     8,     9,
     351,    11,   127,   128,   362,   361,   369,   365,   366,   367,
       5,    21,   370,    23,    24,   371,   241,   375,   128,   377,
     127,   128,   378,   133,   382,   694,   147,   385,   386,   698,
     699,   389,   610,   611,   129,   260,   387,   783,   133,   264,
       0,     5,   410,   128,     4,   166,   131,   168,   406,   405,
     413,   127,   128,   411,   412,   654,   655,   135,   130,   393,
     771,   133,   396,   101,   422,   399,   187,   124,   125,   400,
     127,     6,   125,   404,   127,   433,   434,   435,   436,   127,
     128,   343,   440,     4,   442,   347,   444,   798,    31,    32,
      33,    34,    35,    11,    12,    13,   127,   128,    16,   361,
     221,   133,   223,   814,   225,   130,   125,   369,   127,   371,
     231,   126,   129,   128,   465,   126,   378,   128,   126,     5,
     128,   479,   480,   125,   349,   127,    16,   126,   486,   128,
     355,   127,   128,    31,    32,    33,   126,   500,   128,   401,
     261,    84,   127,   405,   265,   129,   126,   505,   128,     5,
     126,   413,   128,     6,   512,   513,   126,     5,   128,   517,
     126,   519,   128,   126,   129,   128,   109,   110,   127,   112,
     113,   114,   115,   116,   117,   128,   119,   120,   121,   126,
     125,   128,   550,   127,   128,   541,    84,   543,     5,   126,
     546,   128,   791,   792,   419,   316,   317,   126,   797,   128,
     127,   126,   129,   128,   127,   128,   327,   565,   329,     5,
     126,   542,   128,   126,   126,   128,   128,   115,   116,   117,
     578,   119,   120,   121,   127,   126,   129,   128,   125,   491,
      68,    69,    70,    71,    72,    73,    74,    75,   500,    58,
     125,    60,   600,    58,    58,    60,    60,     5,   126,   848,
     128,   607,   608,   129,   126,   613,   128,   126,   614,   128,
     616,   127,   128,   127,   128,   623,   127,   128,   127,   128,
     127,   128,   127,   128,   125,   125,   125,   539,   125,   541,
     125,   543,   125,   127,   546,     5,   654,   655,   129,   645,
     125,   133,   648,   125,   125,     5,     5,   418,   127,   657,
     421,   129,     5,   129,   125,   656,   128,   428,   533,   430,
     535,   536,   537,   538,     5,   673,   129,   129,   129,   127,
     127,   127,   680,   127,   127,   127,     5,     5,   127,   127,
       5,   556,   127,     5,   127,   129,     5,   127,   125,   127,
     129,   127,   700,   127,    11,   607,   608,   127,    60,   705,
     131,   130,   614,   127,   616,     5,   712,   129,   127,   132,
     127,   125,   132,    58,   127,   126,    60,   127,   127,   131,
     127,   127,   127,   127,   127,   127,   732,   733,   127,     5,
     127,   127,     4,   645,   127,   127,   648,   738,   127,    40,
     105,    53,   127,   127,   127,     5,   127,   127,    58,    40,
     105,    53,     5,   759,   760,   131,   127,   134,   771,   765,
     635,   127,   533,    53,   535,   640,    53,   773,    53,    58,
     127,     5,    58,   791,   792,   127,   127,   783,   127,   797,
      60,   127,    53,   789,   659,   798,     5,   125,    58,    58,
     127,   127,    60,   705,   127,    58,   567,     4,   162,    17,
     712,   814,   391,   477,   586,   309,   592,    99,   408,   623,
     738,   738,   456,    -1,    -1,   275,   822,    -1,    -1,    -1,
     732,   733,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     848,   839,    -1,    -1,    -1,   841,    -1,    -1,    -1,    -1,
      -1,   716,    -1,    -1,    -1,   851,    -1,   759,   760,    -1,
      -1,    -1,    -1,   765,    -1,   730,   731,    -1,    -1,   771,
      -1,   773,    -1,    -1,    -1,   636,   637,   638,    -1,   640,
     641,   783,    -1,     4,     5,    -1,    -1,   789,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   798,    18,    19,    20,
      -1,    -1,    -1,    -1,    25,    26,    27,    -1,    -1,    -1,
      -1,    -1,   814,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     822,   786,    -1,    -1,    -1,    46,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   841,
      -1,    -1,    -1,    -1,    -1,    -1,    67,    -1,    -1,   851,
      -1,    -1,    -1,    -1,    -1,    -1,   717,    -1,   719,     4,
       5,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,   730,
      91,    92,    93,    18,    19,    20,    -1,    -1,    -1,    -1,
      25,    26,    27,    -1,    -1,   106,   107,   108,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   116,    -1,    -1,    -1,    -1,
      -1,    46,    -1,    -1,   125,   126,    -1,    -1,    -1,   130,
      -1,   132,    -1,    -1,    -1,   136,   137,    31,    32,    33,
      34,    35,    67,    -1,    -1,   786,   787,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,     4,     5,    -1,    83,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    91,    92,    93,    18,
      19,    20,    -1,    -1,    -1,    -1,    25,    26,    27,    -1,
      -1,   106,   107,   108,    -1,    -1,    -1,    -1,    -1,    -1,
      84,   116,    41,    42,    -1,    -1,    -1,    46,    -1,    -1,
     125,   126,    -1,    -1,    -1,   130,    -1,   132,    -1,    -1,
      -1,   136,   137,    -1,     4,     5,    -1,    -1,    67,   113,
     114,   115,   116,   117,    -1,   119,   120,   121,    18,    19,
      20,    -1,    -1,    -1,    83,    25,    26,    27,    -1,    -1,
      -1,    -1,    91,    92,    93,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    46,   106,   107,   108,
      -1,    -1,    -1,    53,    54,    -1,    -1,   116,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   125,    67,    -1,    -1,
      -1,   130,    -1,    -1,    -1,    -1,    -1,   136,   137,    -1,
      -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,     4,
       5,    91,    92,    93,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    18,    19,    20,   106,   107,   108,    -1,
      25,    26,    27,    -1,    -1,    -1,   116,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   125,    -1,    -1,    -1,    -1,
     130,    46,    -1,    -1,    -1,    -1,   136,   137,    53,    54,
       4,     5,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    67,    -1,    18,    19,    20,    -1,    -1,    -1,
      -1,    25,    26,    27,    -1,    -1,    -1,    -1,    83,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    91,    92,    93,    -1,
      -1,    -1,    46,    -1,    -1,    -1,    -1,    -1,    -1,    53,
      54,   106,   107,   108,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   116,    -1,    67,    -1,    -1,    -1,    -1,    -1,    -1,
     125,    -1,    -1,    -1,    -1,   130,    -1,    -1,    -1,    83,
      -1,   136,   137,    -1,    -1,     4,     5,    91,    92,    93,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    18,
      19,    20,   106,   107,   108,    -1,    25,    26,    27,    -1,
      -1,    -1,   116,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   125,    -1,    -1,    -1,    -1,   130,    46,    -1,    -1,
      -1,    -1,   136,   137,    53,    54,     4,     5,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    67,    -1,
      18,    19,    20,    -1,    -1,    -1,    -1,    25,    26,    27,
      -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    91,    92,    93,    -1,    -1,    -1,    46,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   106,   107,   108,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   116,    -1,    67,
      -1,    -1,    -1,    -1,    -1,    -1,   125,    -1,    -1,    -1,
      -1,   130,     4,     5,    -1,    83,    -1,   136,   137,    -1,
      -1,    -1,    -1,    91,    92,    93,    18,    19,    20,    -1,
      -1,    -1,    -1,    25,    26,    27,    -1,    -1,   106,   107,
     108,   109,    -1,    -1,    -1,    -1,    -1,    -1,   116,    -1,
      -1,    -1,    -1,    -1,    46,    -1,    -1,   125,    -1,    -1,
      -1,    -1,   130,     4,     5,    -1,    -1,    -1,   136,   137,
      -1,    -1,    -1,    -1,    -1,    67,    -1,    18,    19,    20,
      -1,    -1,    -1,    -1,    25,    26,    27,    -1,    -1,    -1,
      -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    91,
      92,    93,    -1,    -1,    -1,    46,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   106,   107,   108,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   116,    -1,    67,    -1,    -1,    -1,
      -1,    -1,    -1,   125,   126,    -1,    -1,    -1,   130,     4,
       5,    -1,    83,    -1,   136,   137,    -1,    -1,    -1,    -1,
      91,    92,    93,    18,    19,    20,    -1,    -1,    -1,    -1,
      25,    26,    27,    -1,    -1,   106,   107,   108,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   116,    -1,    -1,    -1,    -1,
      -1,    46,    -1,   124,   125,    -1,    -1,    -1,    -1,   130,
       4,     5,    -1,    -1,    -1,   136,   137,    -1,    -1,    -1,
      -1,    -1,    67,    -1,    18,    19,    20,    -1,    -1,    -1,
      -1,    25,    26,    27,    -1,    -1,    -1,    -1,    83,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    91,    92,    93,    -1,
      -1,    -1,    46,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      54,   106,   107,   108,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   116,    -1,    67,    -1,    -1,    -1,    -1,    -1,    -1,
     125,    -1,    -1,    -1,    -1,   130,    -1,   132,    -1,    83,
      -1,   136,   137,    -1,    -1,     4,     5,    91,    92,    93,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    18,
      19,    20,   106,   107,   108,    -1,    25,    26,    27,    -1,
      -1,    -1,   116,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   125,    -1,    -1,    -1,    -1,   130,    46,    -1,    -1,
      -1,    -1,   136,   137,    -1,    54,     4,     5,    -1,    -1,
       4,     5,    -1,    -1,    -1,    -1,    -1,    -1,    67,    -1,
      18,    19,    20,    -1,    18,    19,    20,    25,    26,    27,
      -1,    25,    26,    27,    83,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    91,    92,    93,    -1,    -1,    -1,    46,    -1,
      -1,    -1,    46,    -1,    -1,    -1,    -1,   106,   107,   108,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   116,    -1,    67,
      -1,    -1,    -1,    67,    -1,    -1,   125,    -1,    -1,    -1,
      -1,   130,    -1,    -1,    -1,    83,    -1,   136,   137,    83,
      -1,    -1,    -1,    91,    92,    93,    -1,    91,    92,    93,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   106,   107,
     108,    -1,   106,   107,   108,    -1,    -1,    -1,   116,    -1,
      -1,    -1,   116,    -1,     5,    -1,     7,   125,   126,    -1,
      11,   125,   130,    -1,    -1,    -1,   130,    -1,   136,   137,
      21,    22,   136,   137,    -1,    -1,    -1,    -1,    29,    30,
      31,    32,    33,    34,    35,    -1,    37,    -1,    39,    -1,
      -1,    -1,    -1,    44,    45,    -1,    -1,    -1,    -1,    50,
      51,    52,    -1,    -1,    -1,    56,    -1,    -1,    -1,    -1,
      61,    62,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    76,    -1,    78,    79,    -1,
      -1,    -1,    -1,    84,    -1,    -1,    -1,    -1,    89,    90,
      91,    92,    93,    94,    -1,    -1,    -1,    98,    -1,    -1,
      -1,    -1,   103,   104,    -1,   106,   107,   108,   109,   110,
      -1,   112,   113,   114,   115,   116,   117,    -1,   119,   120,
     121,    -1,    -1,   124,    -1,    -1,   127,    -1,    -1,   130,
      -1,    -1,    -1,     5,   135,     7,     8,     9,    -1,    11,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    21,
      22,    23,    24,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    37,    -1,    39,    -1,    -1,
      -1,    -1,    44,    45,    -1,    -1,    -1,    -1,    50,    51,
      52,    -1,    -1,    -1,    56,    -1,    -1,    -1,    -1,    61,
      62,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,     5,    76,     7,    78,    79,    -1,    11,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    89,    90,    21,
      22,    -1,    94,    -1,    -1,    -1,    98,    -1,    -1,    -1,
      -1,   103,    -1,    -1,    -1,    37,    38,    39,    -1,    -1,
      -1,    -1,    44,    45,    -1,    -1,    -1,    -1,    50,    51,
      52,    -1,   124,    -1,    56,    -1,    -1,    -1,   130,    61,
      62,    -1,    -1,   135,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,     5,    76,     7,    78,    79,    -1,    11,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    89,    90,    21,
      22,    -1,    94,    -1,    -1,    -1,    98,    -1,    -1,    -1,
      -1,   103,    -1,   105,    -1,    37,    -1,    39,    -1,    -1,
      -1,    -1,    44,    45,    -1,    -1,    -1,    -1,    50,    51,
      52,    -1,   124,    -1,    56,    -1,    -1,    -1,   130,    61,
      62,    -1,    -1,   135,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,     5,    76,     7,    78,    79,    -1,    11,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    89,    90,    21,
      22,    -1,    94,    -1,    -1,    -1,    98,    -1,    -1,    -1,
      -1,   103,    -1,    -1,    -1,    37,    38,    39,    -1,    -1,
      -1,    -1,    44,    45,    -1,    -1,    -1,    -1,    50,    51,
      52,    -1,   124,    -1,    56,   127,    -1,    -1,   130,    61,
      62,    -1,    -1,   135,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,     5,    76,     7,    78,    79,    -1,    11,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    89,    90,    21,
      22,    -1,    94,    -1,    -1,    -1,    98,    -1,    -1,    -1,
      -1,   103,    -1,    -1,    -1,    37,    -1,    39,    -1,    -1,
      -1,    -1,    44,    45,    -1,    -1,    -1,    -1,    50,    51,
      52,    -1,   124,    -1,    56,    -1,    -1,    -1,   130,    61,
      62,    -1,    -1,   135,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    76,    77,    78,    79,     5,    -1,
       7,    -1,    -1,    -1,    11,    -1,    -1,    89,    90,    -1,
      -1,    -1,    94,    -1,    21,    22,    98,    -1,    -1,    -1,
      -1,   103,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      37,    -1,    39,    -1,    -1,    -1,    -1,    44,    45,    -1,
      -1,    -1,   124,    50,    51,    52,    -1,    -1,   130,    56,
      -1,    58,    -1,   135,    61,    62,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     5,    76,
       7,    78,    79,    -1,    11,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    89,    90,    21,    22,    -1,    94,    -1,    -1,
      -1,    98,    -1,    -1,    -1,    -1,   103,    -1,    -1,    -1,
      37,    38,    39,    -1,    -1,    -1,    -1,    44,    45,    -1,
      -1,    -1,    -1,    50,    51,    52,    -1,   124,    -1,    56,
      -1,    -1,    -1,   130,    61,    62,    -1,    -1,   135,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     5,    76,
       7,    78,    79,    -1,    11,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    89,    90,    21,    22,    -1,    94,    -1,    -1,
      -1,    98,    -1,    -1,    -1,    -1,   103,    -1,    -1,    -1,
      37,    -1,    39,    -1,    -1,    -1,    -1,    44,    45,    -1,
      -1,    -1,    -1,    50,    51,    52,    -1,   124,    -1,    56,
      -1,    58,    -1,   130,    61,    62,    -1,    -1,   135,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     5,    76,
       7,    78,    79,    -1,    11,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    89,    90,    21,    22,    -1,    94,    -1,    -1,
      -1,    98,    -1,    -1,    -1,    -1,   103,    -1,    -1,    -1,
      37,    -1,    39,    -1,    -1,    -1,    -1,    44,    45,    -1,
      -1,    -1,    -1,    50,    51,    52,    -1,   124,    -1,    56,
      -1,    -1,    -1,   130,    61,    62,    -1,    -1,   135,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     5,    76,
       7,    78,    79,    -1,    11,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    89,    90,    21,    22,    -1,    94,    -1,    -1,
      -1,    98,    -1,    -1,    -1,    -1,   103,    -1,    -1,    -1,
      37,    -1,    39,    -1,    -1,    -1,    -1,    44,    45,    -1,
      -1,    -1,    -1,    50,    51,    52,    -1,   124,    -1,    56,
     127,    -1,    -1,   130,    61,    62,    -1,    -1,   135,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     5,    76,
       7,    78,    79,    -1,    11,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    89,    90,    21,    22,    -1,    94,    -1,    -1,
      -1,    98,    -1,    -1,    -1,    -1,   103,    -1,    -1,    -1,
      37,    -1,    39,    -1,    -1,    -1,    -1,    44,    45,    -1,
      -1,    -1,    -1,    50,    51,    52,    -1,   124,    -1,    56,
     127,    -1,    -1,   130,    61,    62,    -1,    -1,   135,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    76,
      -1,    78,    79,    -1,    -1,    29,    -1,    31,    32,    33,
      34,    35,    89,    90,    -1,    -1,    -1,    94,    -1,    -1,
      -1,    98,    -1,    -1,    -1,     5,   103,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    16,    17,    -1,    -1,
      -1,    21,    -1,    23,    -1,    -1,    -1,   124,    -1,    -1,
      -1,    -1,    -1,   130,    -1,    -1,    36,    37,   135,    39,
      84,    -1,    -1,    43,    -1,    -1,    -1,    47,    48,    49,
      50,    -1,    -1,    -1,    -1,    55,    -1,    -1,    -1,    -1,
      -1,    61,    -1,    -1,   108,   109,   110,    -1,   112,   113,
     114,   115,   116,   117,    -1,   119,   120,   121,    -1,    79,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    88,    -1,
      -1,    -1,    -1,    -1,    -1,    95,    96,    -1,    -1,    99,
     100,     5,   102,     7,     8,     9,    10,    11,    12,    13,
      14,    15,    16,    17,    -1,    -1,    -1,    21,    -1,    23,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   127,    -1,    -1,
      -1,    -1,    36,    37,    -1,    39,    -1,    -1,    -1,    43,
      -1,    -1,    -1,    47,    48,    49,    50,    -1,    -1,    -1,
      -1,    55,    -1,    -1,    -1,    -1,    -1,    61,    29,    30,
      31,    32,    33,    34,    35,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    79,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    88,    -1,    -1,    -1,    -1,    -1,
      -1,    95,    96,    -1,    -1,    99,   100,    -1,   102,    -1,
      -1,    -1,    29,    30,    31,    32,    33,    34,    35,    -1,
      81,    82,    -1,    84,    -1,    -1,    -1,    -1,    -1,    -1,
      91,    92,    93,   127,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   104,   105,   106,   107,   108,   109,   110,
      -1,   112,   113,   114,   115,   116,   117,    -1,   119,   120,
     121,    -1,    -1,    -1,    -1,    -1,    -1,    84,    -1,    -1,
      -1,    -1,    -1,   134,    91,    92,    93,    29,    30,    31,
      32,    33,    34,    35,    -1,    -1,    -1,   104,    -1,   106,
     107,   108,   109,   110,    -1,   112,   113,   114,   115,   116,
     117,    -1,   119,   120,   121,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   134,    -1,    -1,
      -1,    29,    30,    31,    32,    33,    34,    35,    -1,    -1,
      -1,    -1,    84,    -1,    -1,    -1,    -1,    -1,    -1,    91,
      92,    93,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   104,    -1,   106,   107,   108,   109,   110,    -1,
     112,   113,   114,   115,   116,   117,    -1,   119,   120,   121,
      -1,    -1,    -1,    -1,    -1,    -1,    84,    -1,    -1,    -1,
      -1,    -1,   134,    91,    92,    93,    29,    30,    31,    32,
      33,    34,    35,    -1,    -1,    -1,   104,    -1,   106,   107,
     108,   109,   110,    -1,   112,   113,   114,   115,   116,   117,
      -1,   119,   120,   121,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   134,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    84,    -1,    -1,    -1,    -1,    -1,    -1,    91,    92,
      93,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   104,    -1,   106,   107,   108,   109,   110,    -1,   112,
     113,   114,   115,   116,   117,    -1,   119,   120,   121,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,     5,   130,     7,     8,
       9,    10,    11,    12,    13,    14,    15,    16,    17,    -1,
      -1,    -1,    21,    -1,    23,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    36,    37,    -1,
      39,    -1,    -1,    -1,    43,    -1,    -1,    -1,    47,    48,
      49,    50,    -1,    -1,    -1,    -1,    55,    -1,    -1,    -1,
      -1,    -1,    61,    29,    30,    31,    32,    33,    34,    35,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      79,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    88,
      -1,    -1,    -1,    -1,    -1,    -1,    95,    96,    -1,    -1,
      99,   100,    -1,   102,    -1,    -1,   105,    29,    30,    31,
      32,    33,    34,    35,    -1,    -1,    -1,    -1,    84,    -1,
      -1,    -1,    -1,    -1,    -1,    91,    92,    93,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   104,    -1,
     106,   107,   108,   109,   110,    -1,   112,   113,   114,   115,
     116,   117,    -1,   119,   120,   121,    -1,    -1,    -1,    -1,
      -1,    -1,    84,   129,    -1,    -1,    -1,    -1,    -1,    91,
      92,    93,    29,    30,    31,    32,    33,    34,    35,    -1,
      -1,    -1,   104,    -1,   106,   107,   108,   109,   110,    -1,
     112,   113,   114,   115,   116,   117,    -1,   119,   120,   121,
      -1,    -1,    -1,    -1,    -1,   127,    -1,    -1,    -1,    -1,
      29,    30,    31,    32,    33,    34,    35,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    84,    -1,    -1,
      -1,    -1,    -1,    -1,    91,    92,    93,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   104,    -1,   106,
     107,   108,   109,   110,    -1,   112,   113,   114,   115,   116,
     117,    -1,   119,   120,   121,    84,    -1,    -1,    -1,    -1,
     127,    -1,    91,    92,    93,    29,    30,    31,    32,    33,
      34,    35,    -1,    -1,    -1,   104,    -1,   106,   107,   108,
     109,   110,    -1,   112,   113,   114,   115,   116,   117,    -1,
     119,   120,   121,    -1,    -1,    -1,    -1,    -1,   127,    -1,
      -1,    -1,    -1,    29,    30,    31,    32,    33,    34,    35,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      84,    -1,    -1,    -1,    -1,    -1,    -1,    91,    92,    93,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     104,    -1,   106,   107,   108,   109,   110,    -1,   112,   113,
     114,   115,   116,   117,    -1,   119,   120,   121,    84,    -1,
      -1,    -1,    -1,   127,    -1,    91,    92,    93,    29,    30,
      31,    32,    33,    34,    35,    -1,    -1,    -1,   104,    -1,
     106,   107,   108,   109,   110,    -1,   112,   113,   114,   115,
     116,   117,    -1,   119,   120,   121,    -1,    -1,    -1,    -1,
      -1,   127,    -1,    -1,    -1,    -1,    29,    30,    31,    32,
      33,    34,    35,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    84,    -1,    -1,    -1,    -1,    -1,    -1,
      91,    92,    93,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   104,    -1,   106,   107,   108,   109,   110,
      -1,   112,   113,   114,   115,   116,   117,    -1,   119,   120,
     121,    84,    -1,    -1,    -1,    -1,   127,    -1,    91,    92,
      93,    29,    30,    31,    32,    33,    34,    35,    -1,    -1,
      -1,   104,    -1,   106,   107,   108,   109,   110,    -1,   112,
     113,   114,   115,   116,   117,    -1,   119,   120,   121,    -1,
      -1,    -1,    -1,    -1,   127,    -1,    -1,    -1,    -1,    29,
      30,    31,    32,    33,    34,    35,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    84,    -1,    -1,    -1,
      -1,    -1,    -1,    91,    92,    93,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   104,    -1,   106,   107,
     108,   109,   110,    -1,   112,   113,   114,   115,   116,   117,
      -1,   119,   120,   121,    84,    -1,    -1,    -1,    -1,   127,
      -1,    91,    92,    93,    29,    30,    31,    32,    33,    34,
      35,    -1,    -1,    -1,   104,    -1,   106,   107,   108,   109,
     110,    -1,   112,   113,   114,   115,   116,   117,    -1,   119,
     120,   121,    -1,    -1,    -1,    -1,    -1,   127,    -1,    -1,
      -1,    -1,    29,    30,    31,    32,    33,    34,    35,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    84,
      -1,    -1,    -1,    -1,    -1,    -1,    91,    92,    93,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   104,
      -1,   106,   107,   108,   109,   110,    -1,   112,   113,   114,
     115,   116,   117,    -1,   119,   120,   121,    84,    -1,    -1,
      -1,    -1,   127,    -1,    91,    92,    93,    29,    30,    31,
      32,    33,    34,    35,    -1,    -1,    -1,   104,    -1,   106,
     107,   108,   109,   110,    -1,   112,   113,   114,   115,   116,
     117,    -1,   119,   120,   121,    -1,    -1,    -1,    -1,    -1,
     127,    -1,    -1,    -1,    -1,    29,    30,    31,    32,    33,
      34,    35,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    84,    -1,    -1,    -1,    -1,    -1,    -1,    91,
      92,    93,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   104,    -1,   106,   107,   108,   109,   110,    -1,
     112,   113,   114,   115,   116,   117,    -1,   119,   120,   121,
      84,    -1,    -1,    -1,    -1,   127,    -1,    91,    92,    93,
      29,    30,    31,    32,    33,    34,    35,    -1,    -1,    -1,
     104,    -1,   106,   107,   108,   109,   110,    -1,   112,   113,
     114,   115,   116,   117,    -1,   119,   120,   121,    -1,    -1,
      -1,    -1,    -1,   127,    -1,    -1,    -1,    -1,    29,    30,
      31,    32,    33,    34,    35,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    84,    -1,    -1,    -1,    -1,
      -1,    -1,    91,    92,    93,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   104,    -1,   106,   107,   108,
     109,   110,    -1,   112,   113,   114,   115,   116,   117,    -1,
     119,   120,   121,    84,    -1,    -1,    -1,    -1,   127,    -1,
      91,    92,    93,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   104,    -1,   106,   107,   108,   109,   110,
      -1,   112,   113,   114,   115,   116,   117,    -1,   119,   120,
     121,    -1,    -1,    -1,    -1,    -1,   127,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    16,    17,
      -1,    -1,    -1,    21,    -1,    23,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    36,    -1,
      -1,    -1,    -1,    -1,    -1,    43,    -1,    -1,    -1,    47,
      48,    49,    -1,    -1,    -1,    -1,    -1,    55,    -1,    57,
      -1,    59,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    67,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    79,    -1,    -1,    -1,    -1,    -1,    -1,    86,    -1,
      88,    -1,    -1,    -1,    -1,    -1,    -1,    95,    96,    97,
      -1,    99,   100,     5,   102,     7,     8,     9,    10,    11,
      12,    13,    14,    15,    16,    17,    -1,    -1,    -1,    21,
      -1,    23,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    36,    -1,    -1,    -1,    -1,    -1,
      -1,    43,    -1,    -1,    -1,    47,    48,    49,    -1,    -1,
      -1,    -1,    -1,    55,    -1,    57,    -1,    59,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    67,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    79,    -1,    -1,
      -1,    -1,    -1,    -1,    86,    -1,    88,    -1,    -1,    -1,
      -1,    -1,    -1,    95,    96,    97,    -1,    99,   100,     5,
     102,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      16,    17,    -1,    -1,    -1,    21,    -1,    23,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      36,    37,    -1,    39,    -1,    -1,    -1,    43,    -1,    -1,
      -1,    47,    48,    49,    50,    -1,    -1,    -1,    -1,    55,
      -1,    -1,    -1,    -1,    -1,    61,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    79,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    87,    88,    -1,    -1,    -1,    -1,    -1,    -1,    95,
      96,    -1,    -1,    99,   100,     5,   102,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    16,    17,    -1,    -1,
      -1,    21,    -1,    23,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    36,    37,    38,    39,
      -1,    -1,    -1,    43,    -1,    -1,    -1,    47,    48,    49,
      50,    -1,    -1,    -1,    -1,    55,    -1,    -1,    -1,    -1,
      -1,    61,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    79,
      -1,    29,    -1,    31,    32,    33,    34,    35,    88,    -1,
      -1,    -1,    -1,    -1,    -1,    95,    96,    -1,    -1,    99,
     100,     5,   102,     7,     8,     9,    10,    11,    12,    13,
      14,    15,    16,    17,    -1,    -1,    -1,    21,    -1,    23,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    36,    37,    38,    39,    84,    -1,    -1,    43,
      -1,    -1,    -1,    47,    48,    49,    50,    -1,    -1,    -1,
      -1,    55,    -1,    -1,    -1,    -1,    -1,    61,    -1,    -1,
      -1,   109,   110,    -1,   112,   113,   114,   115,   116,   117,
      -1,   119,   120,   121,    -1,    79,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    88,    -1,    -1,    -1,    -1,    -1,
      -1,    95,    96,    -1,    -1,    99,   100,     5,   102,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    16,    17,
      -1,    -1,    -1,    21,    -1,    23,    -1,    -1,    -1,    -1,
      29,    30,    31,    32,    33,    34,    35,    -1,    36,    37,
      -1,    39,    -1,    -1,    -1,    43,    -1,    -1,    -1,    47,
      48,    49,    50,    -1,    -1,    -1,    -1,    55,    -1,    -1,
      -1,    -1,    -1,    61,    -1,    -1,    -1,    -1,    29,    30,
      31,    32,    33,    34,    35,    -1,    -1,    -1,    -1,    -1,
      -1,    79,    -1,    -1,    -1,    84,    -1,    -1,    -1,    -1,
      88,    -1,    91,    92,    93,    -1,    -1,    95,    96,    -1,
      -1,    99,   100,    -1,   102,   104,    -1,   106,   107,   108,
     109,   110,    -1,   112,   113,   114,   115,   116,   117,    -1,
     119,   120,   121,    84,    -1,    -1,    -1,   126,    -1,    -1,
      91,    92,    93,    29,    30,    31,    32,    33,    34,    35,
      -1,    -1,    -1,   104,    -1,   106,   107,   108,   109,   110,
      -1,   112,   113,   114,   115,   116,   117,    -1,   119,   120,
     121,    -1,    -1,    -1,    -1,   126,    -1,    -1,    -1,    -1,
      -1,    29,    30,    31,    32,    33,    34,    35,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    84,    -1,
      -1,    -1,    -1,    -1,    -1,    91,    92,    93,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   104,    -1,
     106,   107,   108,   109,   110,    -1,   112,   113,   114,   115,
     116,   117,    -1,   119,   120,   121,    84,    -1,    -1,    -1,
     126,    -1,    -1,    91,    92,    93,    29,    30,    31,    32,
      33,    34,    35,    -1,    -1,    -1,   104,    -1,   106,   107,
     108,   109,   110,    -1,   112,   113,   114,   115,   116,   117,
      -1,   119,   120,   121,    -1,    -1,    -1,    -1,   126,    -1,
      -1,    -1,    -1,    -1,    29,    30,    31,    32,    33,    34,
      35,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    84,    -1,    -1,    -1,    -1,    -1,    -1,    91,    92,
      93,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   104,    -1,   106,   107,   108,   109,   110,    -1,   112,
     113,   114,   115,   116,   117,    -1,   119,   120,   121,    84,
      -1,    -1,    -1,   126,    -1,    -1,    91,    92,    93,    29,
      30,    31,    32,    33,    34,    35,    -1,    -1,    -1,   104,
      -1,   106,   107,   108,   109,   110,    -1,   112,   113,   114,
     115,   116,   117,    -1,   119,   120,   121,    -1,    -1,    -1,
      -1,   126,    -1,    -1,    -1,    -1,    -1,    29,    30,    31,
      32,    33,    34,    35,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    84,    -1,    -1,    -1,    -1,    -1,
      -1,    91,    92,    93,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   104,    -1,   106,   107,   108,   109,
     110,    -1,   112,   113,   114,   115,   116,   117,    -1,   119,
     120,   121,    84,    -1,    -1,    -1,   126,    -1,    -1,    91,
      92,    93,    29,    30,    31,    32,    33,    34,    35,    -1,
      -1,    -1,   104,    -1,   106,   107,   108,   109,   110,    -1,
     112,   113,   114,   115,   116,   117,    -1,   119,   120,   121,
      -1,    -1,    -1,    -1,   126,    -1,    -1,    -1,    -1,    -1,
      29,    30,    31,    32,    33,    34,    35,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    84,    -1,    -1,
      -1,    -1,    -1,    -1,    91,    92,    93,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   104,    -1,   106,
     107,   108,   109,   110,    -1,   112,   113,   114,   115,   116,
     117,    -1,   119,   120,   121,    84,    -1,    -1,    -1,   126,
      -1,    -1,    91,    92,    93,    29,    30,    31,    32,    33,
      34,    35,    -1,    -1,    -1,   104,    -1,   106,   107,   108,
     109,   110,    -1,   112,   113,   114,   115,   116,   117,    -1,
     119,   120,   121,    -1,    -1,    -1,    -1,   126,    -1,    -1,
      -1,    -1,    -1,    29,    30,    31,    32,    33,    34,    35,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      84,    -1,    -1,    -1,    -1,    -1,    -1,    91,    92,    93,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     104,    -1,   106,   107,   108,   109,   110,    -1,   112,   113,
     114,   115,   116,   117,    -1,   119,   120,   121,    84,    -1,
      -1,    -1,   126,    -1,    -1,    91,    92,    93,    29,    30,
      31,    32,    33,    34,    35,    -1,    -1,    -1,   104,    -1,
     106,   107,   108,   109,   110,    -1,   112,   113,   114,   115,
     116,   117,    -1,   119,   120,   121,    -1,    -1,    -1,    -1,
     126,    -1,    -1,    -1,    -1,    -1,    29,    30,    31,    32,
      33,    34,    35,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    84,    -1,    -1,    -1,    -1,    -1,    -1,
      91,    92,    93,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   104,    -1,   106,   107,   108,   109,   110,
      -1,   112,   113,   114,   115,   116,   117,    -1,   119,   120,
     121,    84,    -1,    -1,    -1,   126,    -1,    -1,    91,    92,
      93,    29,    30,    31,    32,    33,    34,    35,    -1,    -1,
      -1,   104,    -1,   106,   107,   108,   109,   110,    -1,   112,
     113,   114,   115,   116,   117,    -1,   119,   120,   121,    -1,
      -1,    -1,    -1,   126,    -1,    29,    30,    31,    32,    33,
      34,    35,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    81,    82,    -1,    84,    -1,    -1,    -1,
      -1,    -1,    -1,    91,    92,    93,    -1,    -1,    -1,    29,
      30,    31,    32,    33,    34,    35,   104,   105,   106,   107,
     108,   109,   110,    -1,   112,   113,   114,   115,   116,   117,
      84,   119,   120,   121,    -1,    -1,    -1,    91,    92,    93,
      -1,    -1,    -1,    29,    30,    31,    32,    33,    34,    35,
     104,   105,   106,   107,   108,   109,   110,    -1,   112,   113,
     114,   115,   116,   117,    84,   119,   120,   121,    -1,    -1,
      -1,    91,    92,    93,    -1,    -1,    -1,    29,    -1,    31,
      32,    33,    34,    35,   104,    -1,   106,   107,   108,   109,
     110,    -1,   112,   113,   114,   115,   116,   117,    84,   119,
     120,   121,    -1,    -1,    -1,    91,    92,    93,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   107,   108,   109,   110,    -1,   112,   113,   114,   115,
     116,   117,    84,   119,   120,   121,    -1,    -1,    -1,    91,
      92,    93,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   107,   108,   109,   110,    -1,
     112,   113,   114,   115,   116,   117,    -1,   119,   120,   121
};

/* YYSTOS[STATE-NUM] -- The symbol kind of the accessing symbol of
   state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,     3,    67,   139,   140,   141,   142,   149,     5,     4,
       5,    46,     0,   141,   124,   125,   127,   143,   144,     5,
       4,     5,    18,    19,    20,    25,    26,    27,    46,    67,
      83,    91,    92,    93,   106,   107,   108,   116,   125,   130,
     136,   137,   208,   212,   125,     5,     8,     9,    10,   126,
     145,   146,   206,   144,     5,     6,     7,    11,    12,    13,
      14,    15,    16,    17,    21,    23,    36,    43,    47,    48,
      49,    55,    57,    59,    79,    86,    88,    95,    96,    97,
      99,   100,   102,   147,   148,   149,   150,   153,   154,   158,
     159,   162,   163,   164,   169,   176,   177,   188,   206,   207,
     120,   125,   133,   204,   205,   125,   212,   212,   212,   212,
     212,   212,   212,   212,   109,   209,   210,   212,   212,   212,
      29,    30,    31,    32,    33,    34,    35,    84,    91,    92,
      93,   104,   106,   107,   108,   109,   110,   112,   113,   114,
     115,   116,   117,   119,   120,   121,     5,    48,    49,   126,
     167,   168,    12,    13,    16,    11,    12,    13,    16,    12,
     127,   126,   128,     5,    21,   133,   204,   147,     5,   124,
     125,   175,     5,   124,   125,   155,   172,   192,   193,   202,
     208,    16,    16,     5,   203,     5,     7,    11,    21,    22,
      37,    39,    44,    45,    50,    51,    52,    56,    61,    62,
      76,    78,    89,    90,    94,    98,   103,   124,   135,   181,
     185,   188,   189,   190,   191,   202,     5,   125,     5,   165,
     166,    16,   165,   204,   165,   204,   181,   185,     5,    21,
     157,   204,     5,     5,    46,   186,   187,    37,    39,    50,
      61,    88,   150,   153,   154,   162,   163,   164,   169,   176,
     178,   179,   180,   188,   185,   181,   101,     6,   147,   203,
     204,     5,   151,   152,   175,   204,     4,   200,   212,   212,
     204,   205,   212,   126,   208,   128,   131,   208,   212,   212,
     212,   212,   212,   212,   212,   212,   212,   212,   212,   212,
     212,   212,   212,   212,   212,   212,   212,   212,   212,   212,
     212,   212,   212,   212,   129,     5,   204,     5,   126,   128,
      16,   127,   146,   129,     5,   212,     5,   204,     6,   125,
     127,   204,     4,     5,    83,   125,   200,     5,   204,   205,
       4,     5,    83,   125,    68,    69,    70,    71,    72,    73,
      74,    75,   156,   172,   202,   202,   127,   128,   129,   128,
     127,   125,   127,   202,   203,   204,   203,   203,    38,   105,
     185,   201,   125,   212,     5,   125,   125,   125,   185,   125,
     125,   201,     5,   212,   212,   125,     5,   125,   212,     5,
      85,   119,   125,   127,   185,    35,   129,   125,   200,   129,
     127,   128,   165,   204,   127,   165,   204,   127,   165,   204,
     125,   127,     5,   204,   125,   127,   129,    80,   128,   105,
     178,   125,   125,   125,   203,    87,   179,   185,    13,   130,
     127,   203,   129,   204,   127,   128,     5,   203,     5,   152,
     204,     5,   126,   128,    81,    82,   105,   134,   126,   210,
     105,   212,   129,     5,   129,   168,     4,    18,    19,    20,
      25,    26,    27,    46,    83,   211,   129,   204,     5,   204,
     126,   132,   170,   171,   200,   125,   126,   132,   173,   174,
     200,   126,   125,   204,   204,   205,   200,   128,   202,   129,
     129,   193,   212,   203,   126,   200,   129,   127,   203,   127,
     127,     5,    38,   185,   212,   127,   127,   212,   212,   212,
      22,   192,   212,    77,   127,   129,   127,   212,   127,   212,
     127,   185,    41,    42,   183,   184,   212,   172,   212,   172,
     212,   170,   200,   126,   212,   166,   127,   165,   127,   165,
     127,   165,   145,     8,     9,    11,    21,    23,    24,   160,
     161,   201,   125,   127,     5,   145,   160,   185,   212,   187,
       5,    38,   212,   212,   192,   127,   130,   204,   203,   127,
     204,   212,   127,     5,   151,   129,   127,   204,   127,     5,
     152,   204,   212,   212,   212,   212,   212,   212,   129,   212,
     211,     5,   127,     5,   119,   126,   128,   126,   170,   200,
       5,   126,   128,   126,   127,   126,   170,   125,   126,   156,
     129,   212,   212,   127,   126,   212,   127,   201,   126,   126,
     126,   126,   193,   127,   126,   212,   126,   126,   212,   212,
      43,   126,   128,   182,   212,   127,   212,   127,   126,   126,
     127,   127,   127,   127,   126,    21,   203,   204,    11,   203,
     204,   203,   203,   203,   161,   201,    58,   145,   160,   185,
     127,   126,   185,    60,   178,   126,   126,   127,   203,   130,
     131,   127,   212,   127,   204,   127,   127,     5,   151,   134,
     134,   134,   212,   125,   133,   127,   171,   127,   126,   126,
     125,   174,   127,   126,   170,   126,   212,   127,   127,   127,
     127,    38,   185,    54,   194,   196,   198,   200,   194,   194,
     127,   212,   185,   127,   185,    40,   127,   184,   127,   127,
     127,   127,   127,   203,   127,   204,   204,   204,   127,     5,
     203,   204,   127,   204,   127,   127,    58,   126,   185,    58,
      11,    21,   160,   127,    60,    38,   179,    54,   195,   197,
     199,   200,   212,   131,   203,     5,   127,   127,   127,   127,
     126,   212,     4,   127,   127,   212,   127,   126,   127,    40,
     105,    53,   196,   198,    53,   105,    53,   198,    53,   198,
     212,   127,   185,   160,   185,   127,   127,   203,   204,   204,
     127,     5,   127,   127,    58,   203,   204,   203,   185,   160,
     185,    40,   105,    53,   197,   199,    53,   105,   127,     5,
     131,   127,   126,   134,   126,   127,   185,   127,   185,    53,
     127,   185,    53,    53,   127,   192,   185,    58,   127,     5,
     127,   127,   160,   185,   127,   203,   127,    58,   185,    60,
     179,   127,   179,    53,   127,   179,   192,   127,     5,   125,
     192,   126,    58,   127,   185,    58,   127,    60,   126,   127,
     212,   126,   185,    58,   179,   126,   185
};

/* YYR1[RULE-NUM] -- Symbol kind of the left-hand side of rule RULE-NUM.  */
static const yytype_uint8 yyr1[] =
{
       0,   138,   139,   140,   140,   141,   141,   142,   142,   142,
     143,   143,   144,   144,   144,   145,   145,   146,   146,   146,
     146,   146,   146,   146,   146,   146,   147,   147,   148,   148,
     148,   148,   148,   148,   148,   148,   148,   148,   148,   148,
     148,   148,   149,   149,   149,   149,   149,   150,   151,   151,
     152,   152,   153,   153,   153,   153,   153,   153,   153,   153,
     153,   153,   153,   153,   153,   153,   153,   153,   153,   153,
     154,   154,   154,   154,   155,   156,   156,   156,   156,   156,
     156,   156,   156,   157,   157,   158,   158,   158,   158,   158,
     158,   158,   158,   158,   159,   159,   159,   159,   160,   160,
     161,   161,   161,   161,   161,   161,   161,   161,   161,   161,
     161,   161,   161,   162,   162,   162,   162,   162,   163,   163,
     163,   164,   165,   165,   166,   167,   167,   168,   168,   168,
     168,   169,   169,   169,   169,   169,   169,   169,   169,   169,
     169,   169,   169,   169,   170,   170,   171,   171,   171,   171,
     172,   172,   172,   172,   173,   173,   174,   174,   175,   175,
     175,   175,   175,   175,   176,   176,   176,   176,   177,   178,
     178,   179,   179,   179,   179,   179,   179,   179,   179,   179,
     179,   179,   179,   179,   179,   179,   179,   179,   179,   180,
     181,   181,   181,   181,   182,   182,   183,   183,   184,   184,
     184,   185,   185,   185,   185,   185,   185,   185,   185,   185,
     185,   185,   185,   185,   185,   185,   185,   185,   185,   185,
     185,   185,   185,   185,   185,   185,   185,   185,   185,   185,
     185,   185,   185,   185,   185,   185,   185,   185,   185,   185,
     185,   185,   186,   186,   187,   187,   188,   189,   189,   190,
     191,   192,   192,   193,   194,   194,   195,   195,   196,   196,
     197,   197,   198,   198,   199,   199,   200,   200,   201,   201,
     202,   202,   202,   202,   202,   202,   203,   203,   204,   204,
     204,   205,   206,   206,   206,   206,   206,   206,   206,   206,
     206,   206,   206,   206,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   208,   209,   209,
     210,   210,   210,   211,   211,   211,   211,   211,   211,   211,
     211,   211,   212,   212,   212,   212,   212,   212,   212,   212,
     212,   212,   212,   212,   212,   212,   212,   212,   212,   212,
     212,   212,   212,   212,   212,   212,   212,   212,   212,   212,
     212,   212,   212,   212,   212,   212,   212,   212,   212,   212,
     212,   212,   212,   212,   212,   212,   212,   212,   212,   212,
     212,   212,   212,   212,   212,   212
};

/* YYR2[RULE-NUM] -- Number of symbols on the right-hand side of rule RULE-NUM.  */
static const yytype_int8 yyr2[] =
{
       0,     2,     1,     2,     1,     1,     1,     6,     5,     4,
       4,     3,     1,     4,     3,     3,     1,     2,     3,     3,
       4,     4,     5,     1,     4,     5,     2,     0,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     2,     2,     3,     6,     2,     1,     3,
       3,     1,     3,     4,     5,     3,     3,     4,     5,     6,
       5,     6,     5,     6,     4,     4,     6,     9,     8,     7,
       3,     6,     7,     6,     5,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     6,     5,     8,     7,     6,
       8,     9,     9,    10,     6,     5,     8,     9,     2,     1,
       3,     3,     3,     4,     5,     5,     6,     3,     4,     5,
       4,     3,     4,     3,     4,     4,     5,     5,     3,     4,
       5,     3,     3,     1,     3,     3,     1,     4,     4,     5,
       3,     5,     6,     3,     5,     6,     6,     6,     6,     5,
       7,     8,     7,     7,     3,     1,     2,     5,     4,     8,
       4,     2,     2,     2,     3,     1,     5,     2,     4,     2,
       2,     2,     4,     3,     3,     2,     2,     3,     3,     2,
       1,     3,     5,     3,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     5,     7,     6,     7,     6,     9,
       2,     2,     2,     4,     1,     1,     3,     1,     2,     2,
       1,     3,     2,     2,     5,     3,     4,     5,     4,     5,
       5,     7,     3,     3,     3,     3,     4,     3,     5,     2,
       3,     3,     4,     5,     6,     7,     6,     6,     7,     6,
       7,     3,     3,     2,     1,     1,     1,     1,     5,     3,
       5,     6,     3,     1,     3,     1,     3,     9,    10,     5,
       5,     3,     1,     3,     2,     1,     2,     1,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     1,     2,     1,
       1,     2,     3,     3,     2,     1,     3,     1,     5,     5,
       5,     3,     1,     1,     1,     2,     2,     2,     2,     2,
       2,     3,     2,     2,     1,     1,     1,     1,     1,     1,
       2,     2,     1,     1,     1,     1,     1,     3,     3,     1,
       2,     1,     2,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     4,     1,     1,
       1,     1,     1,     1,     2,     3,     3,     2,     5,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     4,     3,     1,     2,     2,     2,
       2,     2,     2,     2,     2,     2
};


enum { YYENOMEM = -2 };

#define yyerrok         (yyerrstatus = 0)
#define yyclearin       (yychar = YYEMPTY)

#define YYACCEPT        goto yyacceptlab
#define YYABORT         goto yyabortlab
#define YYERROR         goto yyerrorlab
#define YYNOMEM         goto yyexhaustedlab


#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)                                    \
  do                                                              \
    if (yychar == YYEMPTY)                                        \
      {                                                           \
        yychar = (Token);                                         \
        yylval = (Value);                                         \
        YYPOPSTACK (yylen);                                       \
        yystate = *yyssp;                                         \
        goto yybackup;                                            \
      }                                                           \
    else                                                          \
      {                                                           \
        yyerror (YY_("syntax error: cannot back up")); \
        YYERROR;                                                  \
      }                                                           \
  while (0)

/* Backward compatibility with an undocumented macro.
   Use YYerror or YYUNDEF. */
#define YYERRCODE YYUNDEF


/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)                        \
do {                                            \
  if (yydebug)                                  \
    YYFPRINTF Args;                             \
} while (0)




# define YY_SYMBOL_PRINT(Title, Kind, Value, Location)                    \
do {                                                                      \
  if (yydebug)                                                            \
    {                                                                     \
      YYFPRINTF (stderr, "%s ", Title);                                   \
      yy_symbol_print (stderr,                                            \
                  Kind, Value); \
      YYFPRINTF (stderr, "\n");                                           \
    }                                                                     \
} while (0)


/*-----------------------------------.
| Print this symbol's value on YYO.  |
`-----------------------------------*/

static void
yy_symbol_value_print (FILE *yyo,
                       yysymbol_kind_t yykind, YYSTYPE const * const yyvaluep)
{
  FILE *yyoutput = yyo;
  YY_USE (yyoutput);
  if (!yyvaluep)
    return;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YY_USE (yykind);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}


/*---------------------------.
| Print this symbol on YYO.  |
`---------------------------*/

static void
yy_symbol_print (FILE *yyo,
                 yysymbol_kind_t yykind, YYSTYPE const * const yyvaluep)
{
  YYFPRINTF (yyo, "%s %s (",
             yykind < YYNTOKENS ? "token" : "nterm", yysymbol_name (yykind));

  yy_symbol_value_print (yyo, yykind, yyvaluep);
  YYFPRINTF (yyo, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

static void
yy_stack_print (yy_state_t *yybottom, yy_state_t *yytop)
{
  YYFPRINTF (stderr, "Stack now");
  for (; yybottom <= yytop; yybottom++)
    {
      int yybot = *yybottom;
      YYFPRINTF (stderr, " %d", yybot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)                            \
do {                                                            \
  if (yydebug)                                                  \
    yy_stack_print ((Bottom), (Top));                           \
} while (0)


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

static void
yy_reduce_print (yy_state_t *yyssp, YYSTYPE *yyvsp,
                 int yyrule)
{
  int yylno = yyrline[yyrule];
  int yynrhs = yyr2[yyrule];
  int yyi;
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %d):\n",
             yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      YYFPRINTF (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr,
                       YY_ACCESSING_SYMBOL (+yyssp[yyi + 1 - yynrhs]),
                       &yyvsp[(yyi + 1) - (yynrhs)]);
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)          \
do {                                    \
  if (yydebug)                          \
    yy_reduce_print (yyssp, yyvsp, Rule); \
} while (0)

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args) ((void) 0)
# define YY_SYMBOL_PRINT(Title, Kind, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif






/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

static void
yydestruct (const char *yymsg,
            yysymbol_kind_t yykind, YYSTYPE *yyvaluep)
{
  YY_USE (yyvaluep);
  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yykind, yyvaluep, yylocationp);

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YY_USE (yykind);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}


/* Lookahead token kind.  */
int yychar;

/* The semantic value of the lookahead symbol.  */
YYSTYPE yylval;
/* Number of syntax errors so far.  */
int yynerrs;




/*----------.
| yyparse.  |
`----------*/

int
yyparse (void)
{
    yy_state_fast_t yystate = 0;
    /* Number of tokens to shift before error messages enabled.  */
    int yyerrstatus = 0;

    /* Refer to the stacks through separate pointers, to allow yyoverflow
       to reallocate them elsewhere.  */

    /* Their size.  */
    YYPTRDIFF_T yystacksize = YYINITDEPTH;

    /* The state stack: array, bottom, top.  */
    yy_state_t yyssa[YYINITDEPTH];
    yy_state_t *yyss = yyssa;
    yy_state_t *yyssp = yyss;

    /* The semantic value stack: array, bottom, top.  */
    YYSTYPE yyvsa[YYINITDEPTH];
    YYSTYPE *yyvs = yyvsa;
    YYSTYPE *yyvsp = yyvs;

  int yyn;
  /* The return value of yyparse.  */
  int yyresult;
  /* Lookahead symbol kind.  */
  yysymbol_kind_t yytoken = YYSYMBOL_YYEMPTY;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;



#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yychar = YYEMPTY; /* Cause a token to be read.  */

  goto yysetstate;


/*------------------------------------------------------------.
| yynewstate -- push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;


/*--------------------------------------------------------------------.
| yysetstate -- set current state (the top of the stack) to yystate.  |
`--------------------------------------------------------------------*/
yysetstate:
  YYDPRINTF ((stderr, "Entering state %d\n", yystate));
  YY_ASSERT (0 <= yystate && yystate < YYNSTATES);
  YY_IGNORE_USELESS_CAST_BEGIN
  *yyssp = YY_CAST (yy_state_t, yystate);
  YY_IGNORE_USELESS_CAST_END
  YY_STACK_PRINT (yyss, yyssp);

  if (yyss + yystacksize - 1 <= yyssp)
#if !defined yyoverflow && !defined YYSTACK_RELOCATE
    YYNOMEM;
#else
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYPTRDIFF_T yysize = yyssp - yyss + 1;

# if defined yyoverflow
      {
        /* Give user a chance to reallocate the stack.  Use copies of
           these so that the &'s don't force the real ones into
           memory.  */
        yy_state_t *yyss1 = yyss;
        YYSTYPE *yyvs1 = yyvs;

        /* Each stack pointer address is followed by the size of the
           data in use in that stack, in bytes.  This used to be a
           conditional around just the two extra args, but that might
           be undefined if yyoverflow is a macro.  */
        yyoverflow (YY_("memory exhausted"),
                    &yyss1, yysize * YYSIZEOF (*yyssp),
                    &yyvs1, yysize * YYSIZEOF (*yyvsp),
                    &yystacksize);
        yyss = yyss1;
        yyvs = yyvs1;
      }
# else /* defined YYSTACK_RELOCATE */
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
        YYNOMEM;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
        yystacksize = YYMAXDEPTH;

      {
        yy_state_t *yyss1 = yyss;
        union yyalloc *yyptr =
          YY_CAST (union yyalloc *,
                   YYSTACK_ALLOC (YY_CAST (YYSIZE_T, YYSTACK_BYTES (yystacksize))));
        if (! yyptr)
          YYNOMEM;
        YYSTACK_RELOCATE (yyss_alloc, yyss);
        YYSTACK_RELOCATE (yyvs_alloc, yyvs);
#  undef YYSTACK_RELOCATE
        if (yyss1 != yyssa)
          YYSTACK_FREE (yyss1);
      }
# endif

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;

      YY_IGNORE_USELESS_CAST_BEGIN
      YYDPRINTF ((stderr, "Stack size increased to %ld\n",
                  YY_CAST (long, yystacksize)));
      YY_IGNORE_USELESS_CAST_END

      if (yyss + yystacksize - 1 <= yyssp)
        YYABORT;
    }
#endif /* !defined yyoverflow && !defined YYSTACK_RELOCATE */


  if (yystate == YYFINAL)
    YYACCEPT;

  goto yybackup;


/*-----------.
| yybackup.  |
`-----------*/
yybackup:
  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  yyn = yypact[yystate];
  if (yypact_value_is_default (yyn))
    goto yydefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either empty, or end-of-input, or a valid lookahead.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token\n"));
      yychar = yylex ();
    }

  if (yychar <= YYEOF)
    {
      yychar = YYEOF;
      yytoken = YYSYMBOL_YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else if (yychar == YYerror)
    {
      /* The scanner already issued an error message, process directly
         to error recovery.  But do not keep the error token as
         lookahead, it is too special and may lead us to an endless
         loop in error recovery. */
      yychar = YYUNDEF;
      yytoken = YYSYMBOL_YYerror;
      goto yyerrlab1;
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yytable_value_is_error (yyn))
        goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);
  yystate = yyn;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END

  /* Discard the shifted token.  */
  yychar = YYEMPTY;
  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     '$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {

#line 3062 "y.tab.c"

      default: break;
    }
  /* User semantic actions sometimes alter yychar, and that requires
     that yytoken be updated with the new translation.  We take the
     approach of translating immediately before every use of yytoken.
     One alternative is translating here after every semantic action,
     but that translation would be missed if the semantic action invokes
     YYABORT, YYACCEPT, or YYERROR immediately after altering yychar or
     if it invokes YYBACKUP.  In the case of YYABORT or YYACCEPT, an
     incorrect destructor might then be invoked immediately.  In the
     case of YYERROR or YYBACKUP, subsequent parser actions might lead
     to an incorrect destructor call or verbose syntax error message
     before the lookahead is translated.  */
  YY_SYMBOL_PRINT ("-> $$ =", YY_CAST (yysymbol_kind_t, yyr1[yyn]), &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;

  *++yyvsp = yyval;

  /* Now 'shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */
  {
    const int yylhs = yyr1[yyn] - YYNTOKENS;
    const int yyi = yypgoto[yylhs] + *yyssp;
    yystate = (0 <= yyi && yyi <= YYLAST && yycheck[yyi] == *yyssp
               ? yytable[yyi]
               : yydefgoto[yylhs]);
  }

  goto yynewstate;


/*--------------------------------------.
| yyerrlab -- here on detecting error.  |
`--------------------------------------*/
yyerrlab:
  /* Make sure we have latest lookahead translation.  See comments at
     user semantic actions for why this is necessary.  */
  yytoken = yychar == YYEMPTY ? YYSYMBOL_YYEMPTY : YYTRANSLATE (yychar);
  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
      yyerror (YY_("syntax error"));
    }

  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
         error, discard it.  */

      if (yychar <= YYEOF)
        {
          /* Return failure if at end of input.  */
          if (yychar == YYEOF)
            YYABORT;
        }
      else
        {
          yydestruct ("Error: discarding",
                      yytoken, &yylval);
          yychar = YYEMPTY;
        }
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:
  /* Pacify compilers when the user code never invokes YYERROR and the
     label yyerrorlab therefore never appears in user code.  */
  if (0)
    YYERROR;
  ++yynerrs;

  /* Do not reclaim the symbols of the rule whose action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;      /* Each real token shifted decrements this.  */

  /* Pop stack until we find a state that shifts the error token.  */
  for (;;)
    {
      yyn = yypact[yystate];
      if (!yypact_value_is_default (yyn))
        {
          yyn += YYSYMBOL_YYerror;
          if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYSYMBOL_YYerror)
            {
              yyn = yytable[yyn];
              if (0 < yyn)
                break;
            }
        }

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
        YYABORT;


      yydestruct ("Error: popping",
                  YY_ACCESSING_SYMBOL (yystate), yyvsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", YY_ACCESSING_SYMBOL (yyn), yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturnlab;


/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturnlab;


/*-----------------------------------------------------------.
| yyexhaustedlab -- YYNOMEM (memory exhaustion) comes here.  |
`-----------------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  goto yyreturnlab;


/*----------------------------------------------------------.
| yyreturnlab -- parsing is finished, clean up and return.  |
`----------------------------------------------------------*/
yyreturnlab:
  if (yychar != YYEMPTY)
    {
      /* Make sure we have latest lookahead translation.  See comments at
         user semantic actions for why this is necessary.  */
      yytoken = YYTRANSLATE (yychar);
      yydestruct ("Cleanup: discarding lookahead",
                  yytoken, &yylval);
    }
  /* Do not reclaim the symbols of the rule whose action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
                  YY_ACCESSING_SYMBOL (+*yyssp), yyvsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif

  return yyresult;
}

#line 398 "yaccs/verilog.yacc"

