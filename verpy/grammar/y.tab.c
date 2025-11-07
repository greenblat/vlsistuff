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
#define YYLAST   5615

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  138
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  75
/* YYNRULES -- Number of rules.  */
#define YYNRULES  376
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  858

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
      53,    55,    55,    56,    56,    56,    57,    57,    59,    59,
      59,    60,    61,    62,    63,    63,    63,    67,    67,    70,
      71,    72,    73,    74,    75,    76,    77,    78,    79,    80,
      81,    82,    83,    87,    87,    87,    87,    87,    88,    89,
      89,    90,    90,    92,    93,    94,    95,    96,    97,    98,
      99,   100,   101,   102,   103,   104,   105,   106,   107,   108,
     109,   113,   114,   115,   116,   119,   120,   120,   120,   120,
     120,   120,   120,   120,   121,   121,   123,   124,   125,   126,
     127,   128,   129,   130,   131,   134,   135,   136,   137,   140,
     140,   142,   143,   144,   145,   146,   147,   148,   149,   150,
     151,   152,   153,   154,   158,   159,   160,   161,   162,   164,
     164,   164,   165,   167,   167,   168,   170,   170,   172,   173,
     174,   175,   179,   180,   181,   182,   183,   184,   185,   186,
     187,   188,   189,   190,   191,   199,   199,   200,   200,   200,
     200,   202,   202,   202,   202,   203,   203,   204,   204,   205,
     205,   205,   205,   205,   205,   208,   208,   208,   208,   211,
     213,   213,   216,   217,   218,   219,   220,   221,   222,   223,
     224,   225,   226,   227,   228,   229,   230,   231,   232,   233,
     238,   243,   243,   243,   243,   244,   244,   245,   245,   246,
     246,   246,   251,   252,   253,   254,   255,   256,   257,   258,
     259,   260,   261,   262,   263,   264,   265,   266,   267,   268,
     269,   270,   271,   272,   273,   274,   275,   276,   277,   278,
     279,   280,   281,   282,   283,   284,   285,   286,   287,   288,
     289,   290,   291,   295,   295,   296,   296,   298,   301,   302,
     304,   305,   306,   306,   307,   308,   308,   309,   309,   310,
     310,   311,   311,   312,   312,   313,   313,   315,   315,   316,
     316,   319,   319,   319,   319,   319,   319,   321,   321,   323,
     323,   323,   324,   326,   326,   326,   326,   326,   326,   326,
     326,   326,   326,   326,   326,   328,   328,   328,   328,   328,
     328,   328,   328,   328,   328,   328,   328,   328,   330,   331,
     331,   333,   334,   335,   340,   341,   342,   343,   343,   343,
     343,   343,   343,   347,   348,   349,   350,   351,   352,   353,
     353,   353,   353,   353,   353,   354,   355,   356,   357,   358,
     359,   360,   361,   362,   363,   364,   365,   366,   367,   368,
     369,   370,   371,   372,   373,   374,   375,   376,   377,   378,
     379,   380,   381,   382,   383,   384,   385,   386,   387,   388,
     389,   390,   391,   392,   393,   394,   395
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

#define YYTABLE_NINF (-218)

#define yytable_value_is_error(Yyn) \
  0

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
static const yytype_int16 yypact[] =
{
     155,    80,   202,    95,   155,  -503,  -503,  -503,   185,   100,
    1624,  -503,  -503,  -503,   107,    71,  -503,   211,  4060,    18,
    -503,   -56,  -503,  -503,  -503,  -503,  -503,  -503,  -503,   119,
    -503,  1624,  1624,  1624,  1624,  1624,  1624,  1624,  1624,  1264,
    1624,  1624,  -503,  5426,   103,  -503,   349,   337,   254,   146,
     111,  -503,    13,  4158,    66,  -503,    63,   267,   306,  -503,
    -503,  -503,  -503,   341,  -503,  -503,  2571,    78,   359,    39,
      10,  2571,    37,   366,    38,  4638,  -503,  -503,  -503,  -503,
    2571,   165,   233,   351,  4254,  -503,  -503,  -503,  -503,  -503,
    -503,  -503,  -503,  -503,  -503,  -503,  -503,  -503,    17,    16,
     376,  1624,  1624,  -503,   261,  1624,  -503,  -503,  -503,  -503,
    -503,  -503,  -503,  4637,   259,   123,  -503,  3015,  -503,  -503,
    1624,  1624,  1624,  1624,  1624,  1624,  1624,  1624,  1624,  1624,
    1624,  1624,  1624,  1624,  1624,  1624,  1624,  1624,  1624,  1624,
    1624,  1624,  1624,  1624,  1624,  1624,   277,    43,   404,  -503,
     241,  -503,  -503,  -503,  -503,   418,  -503,  -503,  -503,  -503,
    -503,   293,   387,   319,   447,  1624,    44,  -503,   450,   101,
      83,  1624,   454,   261,    98,   491,    59,    12,   -55,  -503,
     333,  -503,  -503,  -503,   346,   354,   157,    12,    17,   341,
     341,  1936,   362,  1624,   499,   371,   383,   393,  2571,   397,
     414,  2571,   529,  1624,  1624,   492,   605,   493,  1624,   134,
    2006,  -503,  -503,  -503,  -503,  -503,    65,   494,  1624,   497,
     224,  -503,    10,   249,    10,   275,    10,   495,  -503,   247,
    -503,   615,   488,   256,   498,  -503,   -61,  -503,  3139,   506,
     508,   511,   341,  -503,  -503,  -503,  -503,  -503,  -503,  -503,
    -503,  4350,  -503,  -503,  -503,  -503,  2571,    26,  -503,  -503,
     507,   341,   141,  -503,   286,   634,    45,   636,   258,  5426,
    2797,  -503,  -503,  4675,  -503,  -503,  1264,  -503,  -503,  4119,
    5494,   137,   137,   137,   432,   432,  -503,   411,   411,   411,
    5392,  5460,   411,  2624,   541,   541,   541,   432,   432,   210,
     210,   137,  -503,  -503,  -503,  1624,   513,   639,   516,  -503,
      42,  -503,  -503,  -503,   457,  -503,  5358,   152,    47,  -503,
     784,  -503,   522,  -503,  -503,  -503,   944,   262,   -24,  -503,
     261,  -503,  -503,  -503,  1624,  -503,  -503,  -503,  -503,  -503,
    -503,  -503,  -503,   386,    12,   517,   520,  -503,    12,  1624,
     341,  -503,  1349,  -503,   523,   524,   341,   526,   532,  -503,
     658,  -503,  2076,  1624,  3216,   537,  1624,  1624,  1624,  -503,
      56,  1624,  2146,   538,  3172,  3281,  1624,   540,  1624,  1737,
    -503,  -503,  -503,   947,  -503,  -503,  1399,  1399,  1434,   284,
    1624,  -503,   359,   303,   359,  -503,   364,   359,  -503,   373,
     359,   387,  1866,   294,   663,   387,  1866,  1624,  -503,    38,
     664,  4446,  1624,  1624,    12,   543,  -503,  -503,  -503,   212,
     341,  -503,   -29,  1624,   544,  -503,   670,    70,   549,   141,
     415,    49,  -503,  -503,  1624,  1624,  1624,  1624,  -503,  -503,
    -503,  1624,  5426,  1624,   548,  1624,  -503,  -503,  -503,  -503,
    -503,  -503,  -503,  -503,  -503,  -503,  -503,   457,  -503,  -503,
     673,   552,    54,   296,  -503,   297,  1434,  -503,   675,   313,
    -503,   321,   554,   169,   557,  -503,  -503,   325,   491,   555,
    1624,  1624,  -503,  5426,  -503,   556,   329,  1624,  -503,   558,
    -503,  -503,  2571,  -503,  -503,  4740,  -503,  -503,  4778,  4843,
    4881,    12,   455,  4946,  -503,  -503,  1624,  -503,  4984,  -503,
    5049,  -503,  -503,  1624,  1624,   112,  -503,  5426,  1624,  3319,
    1624,  3384,   340,   343,   559,  5426,  -503,  -503,   463,  -503,
     472,  -503,   477,   352,    41,   676,    17,   341,   341,   341,
    1866,  -503,  2221,   387,  1866,   561,   360,  1866,   629,  5426,
    -503,  4638,  -503,  5087,  5152,   480,  -503,   341,   560,   564,
    -503,   565,  5426,  -503,   569,  -503,  1624,  -503,   175,  -503,
     370,   485,   694,  5426,  2841,  2906,  2950,  5426,  5426,  1624,
    5426,  -503,  -503,  -503,   138,  -503,   574,   570,   577,   381,
     385,   581,  -503,   576,  -503,  -503,   582,   389,   570,  -503,
     584,  1624,  3422,  3487,  -503,   585,  3525,  -503,  2291,  2571,
    1484,  1624,  1624,   587,  1624,  2571,  3590,  2571,   -20,  5426,
    5426,  -503,  -503,  -503,   947,  3628,  -503,  3693,  -503,   588,
     589,  -503,  -503,  -503,  -503,   590,   341,   178,   488,   488,
     591,    51,   180,   592,   593,  -503,  2361,  -503,   409,  1866,
     653,   295,   594,   662,  -503,  4542,  4638,  1569,  1624,   595,
     341,   718,  -503,  3731,  -503,   597,  -503,  -503,   427,   598,
    -503,  -503,  -503,  5426,  1620,   725,  -503,  -503,  -503,   603,
     604,  1624,  -503,  -503,   606,   429,  -503,  3796,  -503,  -503,
    -503,  -503,  -503,   692,   630,  1082,  -503,   683,   -42,  1085,
    1209,  1624,  3834,  -503,  -503,  -503,  2571,  -503,  -503,  -503,
    -503,  -503,  -503,  1866,   611,  -503,   612,   341,   488,   509,
     102,   613,   736,   510,   616,  -503,  -503,  -503,   617,   684,
    -503,    17,   341,  1866,  1866,  -503,  -503,   705,   641,  1212,
    -503,   695,   -35,  3899,   745,   621,   626,  -503,  -503,  -503,
    -503,  -503,  5190,   624,  -503,  -503,  5255,  -503,   632,  -503,
    2571,  2431,  -503,  -503,   708,  -503,  2501,  -503,   710,  -503,
     716,  3937,    12,  -503,  1866,   712,  -503,  -503,   644,   767,
     646,   521,   649,  -503,  1866,  -503,   650,    51,   206,   721,
    1866,   722,  4638,  2668,  -503,  -503,   728,  -503,  2764,    12,
     659,   785,  -503,  -503,   667,  -503,  -503,  -503,  -503,  -503,
    -503,  -503,  -503,  -503,  -503,    12,   459,   735,  -503,  -503,
     668,  -503,  -503,  1866,   738,  -503,   671,  -503,  -503,   737,
    -503,  -503,  -503,  -503,  -503,  -503,  -503,   460,  -503,   678,
    1624,   470,  2571,  -503,  -503,   742,  -503,  -503,  -503,  4638,
    -503,  5293,  2571,  -503,  -503,  -503,  -503,  -503
};

/* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
   Performed when YYTABLE does not specify something else to do.  Zero
   means the default is an error.  */
static const yytype_int16 yydefact[] =
{
       0,     0,    43,     0,     2,     4,     5,     6,     0,     0,
      45,    44,     1,     3,     0,     0,    13,     0,     0,     0,
     324,   323,   329,   330,   331,   332,   333,   334,   326,   327,
     325,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   367,    46,     0,    24,   283,   284,   285,     0,
       0,    17,     0,     0,     0,    10,     0,   296,   297,   295,
     306,   307,   298,     0,   299,   300,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   303,   304,   305,    42,
       0,     0,     0,     0,    28,    40,    37,    29,    30,    38,
      39,    34,    35,    36,    31,    32,    33,    41,     0,     0,
       0,     0,     0,   335,   338,     0,   372,   374,   373,   369,
     371,   370,   368,     0,     0,     0,   310,   312,   375,   376,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    12,
       0,   127,   287,   294,   290,   286,   288,   293,   291,   289,
      15,     0,     0,    18,     0,     0,     0,     8,     0,     0,
       0,     0,     0,   271,     0,     0,     0,     0,     0,   253,
       0,   276,   301,   302,   278,     0,   271,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   167,   238,   235,   236,   237,     0,     0,     0,     0,
       0,   124,     0,     0,     0,     0,     0,     0,    48,     0,
      85,     0,    84,     0,     0,   246,     0,   244,     0,     0,
       0,     0,   303,   183,   175,   176,   177,   178,   179,   180,
     182,     0,   171,   181,   184,   166,     0,     0,     9,    27,
       0,     0,    49,    52,     0,     0,     0,     0,     0,   268,
       0,   336,   337,     0,   366,   313,     0,   308,   311,   351,
     352,   357,   356,   358,   360,   361,   350,   353,   354,   355,
       0,   346,   345,   347,   362,   363,   364,   348,   349,   340,
     342,   359,   341,   343,   344,     0,     0,     0,     0,    11,
       0,   292,    14,    16,     0,    20,     0,    19,     0,     7,
       0,   134,     0,   160,   162,   161,     0,     0,     0,   272,
     275,   152,   153,   154,     0,    76,    77,    78,    79,    80,
      81,    82,    83,     0,     0,     0,     0,    71,     0,     0,
       0,    56,     0,   234,     0,     0,     0,     0,     0,   203,
       0,   270,     0,     0,     0,     0,     0,     0,     0,   204,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     193,   192,   191,     0,   220,   168,     0,     0,     0,     0,
       0,   122,     0,     0,     0,   114,     0,     0,   119,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   247,     0,
       0,     0,     0,     0,     0,     0,   169,   170,   165,     0,
       0,    53,     0,     0,     0,    57,     0,   278,     0,    49,
       0,     0,    47,   365,     0,     0,     0,     0,   282,   328,
     309,     0,   131,     0,     0,     0,   126,   314,   317,   318,
     319,   320,   321,   322,   316,   315,    25,     0,    21,    22,
       0,     0,     0,     0,   146,     0,     0,   164,     0,     0,
     156,     0,     0,     0,     0,   273,   274,     0,     0,     0,
       0,     0,   252,   254,   277,     0,     0,     0,   216,     0,
     214,   215,     0,   202,   269,     0,   213,   221,     0,     0,
       0,     0,     0,     0,   206,   222,     0,   218,     0,   240,
       0,   232,   233,     0,     0,     0,   198,   201,     0,     0,
       0,     0,     0,     0,     0,   125,   123,   115,     0,   116,
       0,   120,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   100,     0,     0,     0,     0,     0,     0,     0,   245,
     243,     0,   172,     0,     0,     0,   174,     0,     0,     0,
      54,     0,    50,    65,    49,    51,     0,    66,     0,    58,
      49,     0,     0,   267,     0,     0,     0,   339,   129,     0,
     128,    26,    23,   132,     0,   147,     0,     0,     0,     0,
       0,   158,   163,     0,   159,   140,     0,     0,     0,   151,
       0,     0,     0,     0,   223,     0,     0,   217,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   199,
     200,   195,   194,   196,     0,     0,   209,     0,   207,     0,
       0,   135,   118,   117,   121,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    99,     0,    87,     0,     0,
       0,     0,     0,     0,    96,     0,     0,     0,     0,     0,
       0,     0,    55,     0,    61,     0,    63,    59,     0,     0,
     280,   281,   279,   130,     0,     0,   137,   145,   139,     0,
       0,     0,   155,   133,     0,     0,    75,     0,    74,    72,
     224,   239,   205,   211,     0,     0,   256,     0,     0,     0,
       0,     0,     0,   251,   219,   250,     0,   241,   197,   210,
     208,   138,   136,     0,     0,   108,     0,     0,     0,   101,
     278,     0,     0,   112,     0,   102,   103,    86,     0,     0,
      90,     0,     0,     0,     0,    95,   173,   185,     0,     0,
     258,     0,     0,     0,     0,     0,     0,    67,    62,    64,
      60,   149,     0,     0,   143,   144,     0,   141,     0,    73,
       0,     0,   225,   255,     0,   227,     0,   228,     0,   230,
       0,     0,     0,   242,     0,     0,   111,   109,     0,     0,
       0,   104,     0,   113,     0,    89,     0,     0,     0,     0,
       0,     0,     0,     0,   187,   257,     0,   189,     0,     0,
       0,     0,    70,   148,     0,   157,   142,   212,   264,   263,
     226,   260,   259,   229,   231,     0,     0,     0,    91,   110,
       0,   105,   106,     0,     0,   101,     0,   112,    88,     0,
      97,   186,   266,   265,   188,   262,   261,     0,    69,     0,
       0,     0,     0,    92,   107,     0,    93,   104,    98,     0,
      68,     0,     0,   248,    94,   190,   150,   249
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -503,  -503,  -503,   802,  -503,  -503,   790,  -364,   651,    -2,
    -503,   292,    57,  -410,  -256,   183,   192,  -503,   330,  -503,
    -503,  -503,  -399,  -502,   193,   194,   196,   -57,   420,  -503,
     504,   207,  -374,   229,  -171,  -503,   222,   719,   209,  -503,
    -234,  -248,  -503,    30,  -503,  -503,   195,    -6,  -503,   416,
     -18,  -503,  -503,  -503,  -361,  -337,     3,  -503,  -482,    81,
    -375,    84,   -65,  -193,   -16,   228,   525,   -15,   -14,  -503,
      88,  -503,   550,   367,    -8
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
       0,     3,     4,     5,     6,    17,    18,    50,    51,    83,
      84,    85,   243,   263,   264,   244,   245,   176,   343,   231,
      89,    90,   540,   541,   246,   247,   248,   220,   221,   150,
     151,   249,   463,   464,   177,   469,   470,   172,   250,    96,
     251,   252,   253,   227,   624,   515,   516,   361,   236,   237,
     212,   213,   214,   215,   178,   179,   695,   739,   696,   740,
     697,   741,   698,   362,   216,   185,   329,   330,    98,    99,
      42,   115,   116,   456,   269
};

/* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule whose
   number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
      97,    52,    43,   417,   411,   344,   104,   547,   372,   502,
     430,   482,   223,   225,   522,   219,   565,   173,   163,   408,
     706,   262,   184,   106,   107,   108,   109,   110,   111,   112,
     113,   117,   118,   119,   164,    97,   268,   533,   645,   419,
     180,   546,   229,   234,   219,   645,   184,   146,   306,   317,
     429,   168,   459,   555,   570,   222,   720,   254,   230,   584,
     211,   173,   636,   766,   173,   228,    97,   409,   173,   101,
     798,   169,   347,   348,   255,    86,    45,   102,   501,    46,
      47,    48,   259,   217,   235,     8,   434,   323,   324,   272,
     147,   148,   589,   434,   270,    12,   210,   273,   560,   597,
     386,   473,   331,   332,   165,    19,   327,   707,   146,   165,
      86,   256,   279,   280,   281,   282,   283,   284,   285,   286,
     287,   288,   289,   290,   291,   292,   293,   294,   295,   296,
     297,   298,   299,   300,   301,   302,   303,   304,   100,   380,
     170,    86,    39,   165,   181,   649,   165,   645,    52,   165,
     165,   147,   148,   389,   181,   621,   420,   316,     1,   181,
     345,   346,   669,   417,   613,   393,   325,   396,   181,   399,
     165,   354,   165,   585,   165,   571,   165,   165,   165,   648,
     165,   333,   165,   174,   165,   364,    39,   174,   175,    39,
     170,   171,   369,    39,   387,   374,   375,    49,   350,   566,
     379,    87,   275,   218,   385,   278,     9,    10,   326,   542,
      88,    91,    92,   763,    93,   518,   520,   763,   763,   381,
     254,   127,     2,   334,   685,    94,   320,    95,   321,   149,
     350,   645,    44,   254,   165,   165,    87,   161,   622,   162,
     623,   122,   123,   124,   105,    88,    91,    92,    11,    93,
     418,   276,   733,   382,   277,   465,   143,   144,   145,   383,
      94,   471,    95,   674,   181,   181,   159,    87,   117,   477,
     423,   675,   645,   160,   165,   181,    88,    91,    92,   181,
      93,   457,   352,   182,   353,   165,   181,   486,   645,   181,
     102,    94,     7,    95,   127,   596,     7,   442,   181,   608,
     209,   462,   664,   534,   535,   715,   731,   723,   165,    14,
      15,   165,    16,   165,   774,   476,   732,   655,   538,   539,
     764,   645,   183,   523,   768,   770,   260,   142,   479,   143,
     144,   145,   180,   827,   257,   790,    15,   528,    16,   165,
     530,   483,   557,   532,   181,   165,   184,   646,   155,   156,
     157,   391,   392,   158,   180,   495,   494,   258,   498,   499,
     500,   152,   153,   503,   219,   154,   494,   309,   508,   310,
     510,   233,   401,   512,   402,   517,   395,   392,   519,   521,
     267,   405,   525,   406,   433,   823,   434,    52,   472,    39,
     434,    52,    45,   254,   102,    46,    47,    48,   180,   549,
     548,   590,   398,   392,   553,   554,   305,   417,   737,   308,
     524,   816,   434,   425,   426,   562,   355,   357,   358,   543,
     312,   544,   586,   588,   587,   434,   573,   574,   575,   576,
     527,   392,   181,   577,   311,   578,   181,   580,   837,   592,
     120,   593,   122,   123,   124,   125,   126,   594,   314,   434,
     181,   599,   315,   434,   841,   605,   319,   434,   181,   328,
     181,   447,   349,   122,   123,   124,   629,   181,   587,   630,
     415,   434,   602,   603,   350,   448,   449,   450,   635,   606,
     162,   351,   451,   452,   453,   180,   652,   363,   162,   422,
     181,   529,   392,   428,   181,   127,   366,   666,   616,   423,
     531,   392,   181,   454,   365,   619,   620,   679,   367,   587,
     625,   680,   627,   434,   478,   684,   127,   587,   368,   134,
     135,   136,   370,   137,   138,   139,   140,   141,   142,    52,
     143,   144,   145,   254,   373,   728,   494,   162,   650,   371,
     455,   653,   569,   426,   831,   833,   103,   140,   141,   142,
     836,   143,   144,   145,   749,   758,   423,   587,   663,   335,
     336,   337,   338,   339,   340,   341,   342,  -216,  -214,  -216,
    -214,   673,   122,   123,   124,   125,   126,   166,   484,  -217,
     181,  -217,   614,   348,   489,   842,   849,   348,   348,   181,
     632,   392,   742,   687,   224,   226,   852,   232,   348,   633,
     392,   855,   494,   693,   634,   392,   702,   658,   348,   703,
     377,   705,   667,   426,   699,   700,   517,   376,   378,   388,
     403,   165,   384,   261,   266,   127,   390,   407,   181,   271,
     181,   412,   181,   413,   421,   181,   414,   254,   254,   427,
     494,   432,   443,   729,   444,   445,   480,   466,   559,   481,
     743,   488,   487,   490,   138,   139,   140,   141,   142,   491,
     143,   144,   145,   492,   497,   505,   752,   509,   545,   551,
     556,   563,   307,   756,   742,   564,   567,   579,   582,   583,
     591,   595,   598,   604,   601,   607,   631,   639,   651,   654,
     660,   318,   662,   771,   322,   661,   181,   181,   423,   668,
     773,   676,   462,   181,   678,   181,   681,   775,   468,   683,
     686,   730,   690,   356,   701,   711,   712,   713,   719,   725,
     726,   734,   735,   746,   748,   750,   744,   789,   791,   753,
     754,   755,   760,   757,   181,   761,   765,   181,   776,   777,
     781,   782,   785,   783,   784,   792,   793,   394,   797,   397,
     800,   400,   801,   802,   807,   809,   180,   404,   804,   806,
     812,   810,   637,   813,   640,   642,   643,   644,   817,   814,
     818,   819,   820,   821,   254,   254,   822,   825,   824,   828,
     254,   834,   830,   180,   829,   659,   838,   424,    20,    21,
     839,   431,   840,   843,   181,   844,   846,   848,   847,   180,
     854,   181,    22,    23,    24,   850,    13,    53,   600,    25,
      26,    27,   526,   313,   446,   682,   677,   845,   265,   708,
     795,   181,   181,   796,   581,   550,   440,     0,     0,     0,
      28,   254,   851,     0,     0,     0,   853,     0,     0,     0,
       0,     0,   458,   460,     0,     0,   857,     0,   181,   181,
       0,    29,     0,   474,   181,   475,     0,     0,     0,     0,
     181,     0,   181,     0,   714,     0,     0,    30,     0,   721,
       0,     0,   181,     0,     0,    31,    32,    33,   181,     0,
       0,     0,     0,     0,     0,     0,     0,   181,   745,     0,
      34,    35,    36,     0,     0,     0,     0,     0,     0,     0,
      37,     0,     0,   181,     0,     0,     0,     0,     0,    38,
     461,   181,     0,     0,    39,     0,   462,     0,     0,     0,
      40,    41,     0,     0,     0,     0,     0,     0,     0,     0,
     181,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     181,     0,     0,     0,   558,   778,     0,   561,    20,    21,
       0,    20,    21,     0,   568,     0,   572,     0,     0,   786,
     788,     0,    22,    23,    24,    22,    23,    24,     0,    25,
      26,    27,    25,    26,    27,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   513,   514,
      28,     0,     0,    28,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    29,     0,     0,    29,   826,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    30,     0,     0,
      30,     0,     0,     0,     0,    31,    32,    33,    31,    32,
      33,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      34,    35,    36,    34,    35,    36,     0,     0,     0,   638,
      37,   641,     0,    37,     0,     0,     0,     0,     0,    38,
     467,     0,    38,     0,    39,     0,   468,    39,     0,     0,
      40,    41,     0,    40,    41,     0,    20,    21,     0,    20,
      21,     0,     0,   665,     0,     0,     0,     0,     0,     0,
      22,    23,    24,    22,    23,    24,     0,    25,    26,    27,
      25,    26,    27,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    28,     0,
       0,    28,     0,     0,     0,   762,   694,     0,   767,   694,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    29,
       0,     0,    29,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   716,   717,   718,    30,   722,   724,    30,     0,
       0,     0,     0,    31,    32,    33,    31,    32,    33,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    34,    35,
      36,    34,    35,    36,     0,     0,     0,     0,    37,     0,
       0,    37,     0,     0,     0,     0,     0,    38,     0,     0,
      38,     0,    39,    20,    21,    39,    20,    21,    40,    41,
       0,    40,    41,     0,     0,     0,     0,    22,    23,    24,
      22,    23,    24,     0,    25,    26,    27,    25,    26,    27,
       0,     0,     0,   779,     0,   780,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    28,   787,     0,    28,     0,
       0,     0,   769,   694,     0,   794,   738,     0,    20,    21,
       0,     0,     0,     0,     0,     0,    29,     0,     0,    29,
       0,     0,    22,    23,    24,     0,     0,     0,     0,    25,
      26,    27,    30,     0,     0,    30,     0,     0,     0,     0,
      31,    32,    33,    31,    32,    33,     0,     0,     0,     0,
      28,     0,   722,   724,     0,    34,    35,    36,    34,    35,
      36,     0,     0,     0,     0,    37,     0,     0,    37,     0,
       0,    29,     0,     0,    38,     0,     0,    38,     0,    39,
       0,     0,    39,     0,     0,    40,    41,    30,    40,    41,
       0,     0,     0,    20,    21,    31,    32,    33,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    22,    23,    24,
      34,    35,    36,   114,    25,    26,    27,     0,     0,     0,
      37,     0,     0,     0,     0,     0,     0,     0,     0,    38,
       0,     0,     0,     0,    39,    28,     0,     0,     0,     0,
      40,    41,     0,    20,    21,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    29,    22,    23,    24,
       0,     0,     0,     0,    25,    26,    27,     0,     0,     0,
       0,     0,    30,     0,     0,     0,     0,     0,    20,    21,
      31,    32,    33,     0,     0,    28,     0,     0,     0,     0,
       0,     0,    22,    23,    24,    34,    35,    36,     0,    25,
      26,    27,     0,     0,     0,    37,    29,     0,     0,     0,
       0,     0,     0,     0,    38,   485,     0,     0,     0,    39,
      28,     0,    30,     0,     0,    40,    41,     0,    20,    21,
      31,    32,    33,     0,     0,     0,     0,     0,     0,     0,
       0,    29,    22,    23,    24,    34,    35,    36,     0,    25,
      26,    27,     0,     0,     0,    37,     0,    30,     0,     0,
       0,     0,     0,   174,    38,    31,    32,    33,     0,    39,
      28,     0,     0,     0,     0,    40,    41,     0,   694,     0,
      34,    35,    36,     0,     0,     0,     0,     0,     0,     0,
      37,    29,     0,     0,     0,     0,     0,     0,     0,    38,
       0,     0,     0,     0,    39,     0,   462,    30,     0,     0,
      40,    41,     0,    20,    21,    31,    32,    33,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    22,    23,    24,
      34,    35,    36,     0,    25,    26,    27,     0,     0,     0,
      37,     0,     0,     0,     0,     0,     0,     0,     0,    38,
       0,     0,     0,     0,    39,    28,     0,     0,     0,     0,
      40,    41,     0,   738,    20,    21,     0,     0,    20,    21,
       0,     0,     0,     0,     0,     0,    29,     0,    22,    23,
      24,     0,    22,    23,    24,    25,    26,    27,     0,    25,
      26,    27,    30,     0,     0,     0,     0,     0,     0,     0,
      31,    32,    33,     0,     0,     0,    28,     0,     0,     0,
      28,     0,     0,     0,     0,    34,    35,    36,     0,     0,
       0,     0,     0,     0,     0,    37,     0,    29,     0,     0,
       0,    29,     0,     0,    38,     0,     0,     0,     0,    39,
       0,     0,     0,    30,     0,    40,    41,    30,     0,     0,
       0,    31,    32,    33,     0,    31,    32,    33,     0,     0,
       0,     0,     0,     0,     0,     0,    34,    35,    36,     0,
      34,    35,    36,     0,     0,     0,    37,     0,     0,     0,
      37,     0,   186,     0,   187,    38,   751,     0,   188,    38,
      39,     0,     0,     0,    39,     0,    40,    41,   189,   190,
      40,    41,     0,     0,     0,     0,   120,   121,   122,   123,
     124,   125,   126,     0,   191,     0,   192,     0,     0,     0,
       0,   193,   194,     0,     0,     0,     0,   195,   196,   197,
       0,     0,     0,   198,     0,     0,     0,     0,   199,   200,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   201,     0,   202,    74,     0,     0,     0,
       0,   127,     0,     0,     0,     0,   203,   204,   128,   129,
     130,   205,     0,     0,     0,   206,     0,     0,     0,     0,
     207,   131,     0,   132,   133,   134,   135,   136,     0,   137,
     138,   139,   140,   141,   142,     0,   143,   144,   145,     0,
       0,   208,     0,     0,   511,     0,     0,    39,     0,     0,
       0,   186,   209,   187,   534,   535,     0,   536,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   537,   190,   538,
     539,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   191,     0,   192,     0,     0,     0,     0,
     193,   194,     0,     0,     0,     0,   195,   196,   197,     0,
       0,     0,   198,     0,     0,     0,     0,   199,   200,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   186,   201,   187,   202,    74,     0,   188,     0,     0,
       0,     0,     0,     0,     0,   203,   204,   189,   190,     0,
     205,     0,     0,     0,   206,     0,     0,     0,     0,   207,
       0,     0,     0,   191,   359,   192,     0,     0,     0,     0,
     193,   194,     0,     0,     0,     0,   195,   196,   197,     0,
     208,     0,   198,     0,     0,     0,    39,   199,   200,     0,
       0,   209,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   186,   201,   187,   202,    74,     0,   188,     0,     0,
       0,     0,     0,     0,     0,   203,   204,   189,   190,     0,
     205,     0,     0,     0,   206,     0,     0,     0,     0,   207,
       0,   360,     0,   191,     0,   192,     0,     0,     0,     0,
     193,   194,     0,     0,     0,     0,   195,   196,   197,     0,
     208,     0,   198,     0,     0,     0,    39,   199,   200,     0,
       0,   209,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   186,   201,   187,   202,    74,     0,   188,     0,     0,
       0,     0,     0,     0,     0,   203,   204,   189,   190,     0,
     205,     0,     0,     0,   206,     0,     0,     0,     0,   207,
       0,     0,     0,   191,   493,   192,     0,     0,     0,     0,
     193,   194,     0,     0,     0,     0,   195,   196,   197,     0,
     208,     0,   198,   384,     0,     0,    39,   199,   200,     0,
       0,   209,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   186,   201,   187,   202,    74,     0,   188,     0,     0,
       0,     0,     0,     0,     0,   203,   204,   189,   190,     0,
     205,     0,     0,     0,   206,     0,     0,     0,     0,   207,
       0,     0,     0,   191,     0,   192,     0,     0,     0,     0,
     193,   194,     0,     0,     0,     0,   195,   196,   197,     0,
     208,     0,   198,     0,     0,     0,    39,   199,   200,     0,
       0,   209,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   201,   504,   202,    74,   186,     0,   187,     0,
       0,     0,   188,     0,     0,   203,   204,     0,     0,     0,
     205,     0,   189,   190,   206,     0,     0,     0,     0,   207,
       0,     0,     0,     0,     0,     0,     0,     0,   191,     0,
     192,     0,     0,     0,     0,   193,   194,     0,     0,     0,
     208,   195,   196,   197,     0,     0,    39,   198,     0,   647,
       0,   209,   199,   200,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   186,   201,   187,   202,
      74,     0,   188,     0,     0,     0,     0,     0,     0,     0,
     203,   204,   189,   190,     0,   205,     0,     0,     0,   206,
       0,     0,     0,     0,   207,     0,     0,     0,   191,   692,
     192,     0,     0,     0,     0,   193,   194,     0,     0,     0,
       0,   195,   196,   197,     0,   208,     0,   198,     0,     0,
       0,    39,   199,   200,     0,     0,   209,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   186,   201,   187,   202,
      74,     0,   188,     0,     0,     0,     0,     0,     0,     0,
     203,   204,   189,   190,     0,   205,     0,     0,     0,   206,
       0,     0,     0,     0,   207,     0,     0,     0,   191,     0,
     192,     0,     0,     0,     0,   193,   194,     0,     0,     0,
       0,   195,   196,   197,     0,   208,     0,   198,     0,   727,
       0,    39,   199,   200,     0,     0,   209,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   186,   201,   187,   202,
      74,     0,   188,     0,     0,     0,     0,     0,     0,     0,
     203,   204,   189,   190,     0,   205,     0,     0,     0,   206,
       0,     0,     0,     0,   207,     0,     0,     0,   191,     0,
     192,     0,     0,     0,     0,   193,   194,     0,     0,     0,
       0,   195,   196,   197,     0,   208,     0,   198,     0,     0,
       0,    39,   199,   200,     0,     0,   209,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   186,   201,   187,   202,
      74,     0,   188,     0,     0,     0,     0,     0,     0,     0,
     203,   204,   189,   190,     0,   205,     0,     0,     0,   206,
       0,     0,     0,     0,   207,     0,     0,     0,   191,     0,
     192,     0,     0,     0,     0,   193,   194,     0,     0,     0,
       0,   195,   196,   197,     0,   208,     0,   198,   808,     0,
       0,    39,   199,   200,     0,     0,   209,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   186,   201,   187,   202,
      74,     0,   188,     0,     0,     0,     0,     0,     0,     0,
     203,   204,   189,   190,     0,   205,     0,     0,     0,   206,
       0,     0,     0,     0,   207,     0,     0,     0,   191,     0,
     192,     0,     0,     0,     0,   193,   194,     0,     0,     0,
       0,   195,   196,   197,     0,   208,     0,   198,   811,     0,
       0,    39,   199,   200,     0,     0,   209,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   201,     0,   202,
      74,     0,     0,   120,     0,   122,   123,   124,   125,   126,
     203,   204,     0,     0,     0,   205,     0,     0,     0,   206,
       0,     0,     0,    54,   207,    56,    46,    47,    48,    57,
      58,    59,    60,    61,    62,    63,     0,     0,     0,    64,
       0,    65,     0,     0,     0,   208,     0,     0,     0,     0,
       0,    39,     0,     0,    66,   238,   209,   239,   127,     0,
       0,    67,     0,     0,     0,    68,    69,    70,   240,     0,
       0,     0,     0,    71,     0,     0,     0,     0,     0,   241,
       0,     0,     0,   135,   136,     0,   137,   138,   139,   140,
     141,   142,     0,   143,   144,   145,     0,    74,     0,     0,
       0,     0,     0,     0,     0,     0,   242,     0,     0,     0,
       0,     0,     0,    77,    78,     0,     0,    80,    81,    54,
      82,    56,    46,    47,    48,    57,    58,    59,    60,    61,
      62,    63,     0,     0,     0,    64,     0,    65,     0,     0,
       0,     0,     0,     0,     0,   832,     0,     0,     0,     0,
      66,   238,     0,   239,     0,     0,     0,    67,     0,     0,
       0,    68,    69,    70,   240,     0,     0,     0,     0,    71,
       0,     0,     0,     0,     0,   241,   120,   121,   122,   123,
     124,   125,   126,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
       0,     0,   242,     0,     0,     0,     0,     0,     0,    77,
      78,     0,     0,    80,    81,     0,    82,     0,     0,     0,
     120,   121,   122,   123,   124,   125,   126,     0,   435,   436,
       0,   127,     0,     0,     0,     0,     0,     0,   128,   129,
     130,   835,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   131,   437,   132,   133,   134,   135,   136,     0,   137,
     138,   139,   140,   141,   142,     0,   143,   144,   145,     0,
       0,     0,     0,     0,     0,   127,     0,     0,     0,     0,
       0,   438,   128,   129,   130,   120,   121,   122,   123,   124,
     125,   126,     0,     0,     0,   131,     0,   132,   133,   134,
     135,   136,     0,   137,   138,   139,   140,   141,   142,     0,
     143,   144,   145,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   670,     0,     0,     0,   120,
     121,   122,   123,   124,   125,   126,     0,     0,     0,     0,
     127,     0,     0,     0,     0,     0,     0,   128,   129,   130,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     131,     0,   132,   133,   134,   135,   136,     0,   137,   138,
     139,   140,   141,   142,     0,   143,   144,   145,     0,     0,
       0,     0,     0,     0,   127,     0,     0,     0,     0,     0,
     671,   128,   129,   130,   120,   121,   122,   123,   124,   125,
     126,     0,     0,     0,   131,     0,   132,   133,   134,   135,
     136,     0,   137,   138,   139,   140,   141,   142,     0,   143,
     144,   145,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   672,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   127,
       0,     0,     0,     0,     0,     0,   128,   129,   130,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   131,
       0,   132,   133,   134,   135,   136,     0,   137,   138,   139,
     140,   141,   142,     0,   143,   144,   145,     0,     0,     0,
       0,     0,     0,     0,    54,    39,    56,    46,    47,    48,
      57,    58,    59,    60,    61,    62,    63,     0,     0,     0,
      64,     0,    65,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    66,   238,     0,   239,     0,
       0,     0,    67,     0,     0,     0,    68,    69,    70,   240,
       0,     0,     0,     0,    71,     0,     0,     0,     0,     0,
     241,   120,   121,   122,   123,   124,   125,   126,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,     0,     0,   242,     0,     0,
       0,     0,     0,     0,    77,    78,     0,     0,    80,    81,
       0,    82,     0,     0,   410,   120,   121,   122,   123,   124,
     125,   126,     0,     0,     0,     0,   127,     0,     0,     0,
       0,     0,     0,   128,   129,   130,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   131,     0,   132,   133,
     134,   135,   136,     0,   137,   138,   139,   140,   141,   142,
       0,   143,   144,   145,     0,     0,     0,     0,     0,     0,
     127,   506,     0,     0,     0,     0,     0,   128,   129,   130,
     120,   121,   122,   123,   124,   125,   126,     0,     0,     0,
     131,     0,   132,   133,   134,   135,   136,     0,   137,   138,
     139,   140,   141,   142,     0,   143,   144,   145,     0,     0,
       0,     0,     0,   496,     0,     0,     0,     0,   120,   121,
     122,   123,   124,   125,   126,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   127,     0,     0,     0,     0,
       0,     0,   128,   129,   130,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   131,     0,   132,   133,   134,
     135,   136,     0,   137,   138,   139,   140,   141,   142,     0,
     143,   144,   145,   127,     0,     0,     0,     0,   507,     0,
     128,   129,   130,   120,   121,   122,   123,   124,   125,   126,
       0,     0,     0,   131,     0,   132,   133,   134,   135,   136,
       0,   137,   138,   139,   140,   141,   142,     0,   143,   144,
     145,     0,     0,     0,     0,     0,   626,     0,     0,     0,
       0,   120,   121,   122,   123,   124,   125,   126,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   127,     0,
       0,     0,     0,     0,     0,   128,   129,   130,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   131,     0,
     132,   133,   134,   135,   136,     0,   137,   138,   139,   140,
     141,   142,     0,   143,   144,   145,   127,     0,     0,     0,
       0,   628,     0,   128,   129,   130,   120,   121,   122,   123,
     124,   125,   126,     0,     0,     0,   131,     0,   132,   133,
     134,   135,   136,     0,   137,   138,   139,   140,   141,   142,
       0,   143,   144,   145,     0,     0,     0,     0,     0,   688,
       0,     0,     0,     0,   120,   121,   122,   123,   124,   125,
     126,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   127,     0,     0,     0,     0,     0,     0,   128,   129,
     130,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   131,     0,   132,   133,   134,   135,   136,     0,   137,
     138,   139,   140,   141,   142,     0,   143,   144,   145,   127,
       0,     0,     0,     0,   689,     0,   128,   129,   130,   120,
     121,   122,   123,   124,   125,   126,     0,     0,     0,   131,
       0,   132,   133,   134,   135,   136,     0,   137,   138,   139,
     140,   141,   142,     0,   143,   144,   145,     0,     0,     0,
       0,     0,   691,     0,     0,     0,     0,   120,   121,   122,
     123,   124,   125,   126,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   127,     0,     0,     0,     0,     0,
       0,   128,   129,   130,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   131,     0,   132,   133,   134,   135,
     136,     0,   137,   138,   139,   140,   141,   142,     0,   143,
     144,   145,   127,     0,     0,     0,     0,   704,     0,   128,
     129,   130,   120,   121,   122,   123,   124,   125,   126,     0,
       0,     0,   131,     0,   132,   133,   134,   135,   136,     0,
     137,   138,   139,   140,   141,   142,     0,   143,   144,   145,
       0,     0,     0,     0,     0,   709,     0,     0,     0,     0,
     120,   121,   122,   123,   124,   125,   126,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   127,     0,     0,
       0,     0,     0,     0,   128,   129,   130,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   131,     0,   132,
     133,   134,   135,   136,     0,   137,   138,   139,   140,   141,
     142,     0,   143,   144,   145,   127,     0,     0,     0,     0,
     710,     0,   128,   129,   130,   120,   121,   122,   123,   124,
     125,   126,     0,     0,     0,   131,     0,   132,   133,   134,
     135,   136,     0,   137,   138,   139,   140,   141,   142,     0,
     143,   144,   145,     0,     0,     0,     0,     0,   747,     0,
       0,     0,     0,   120,   121,   122,   123,   124,   125,   126,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     127,     0,     0,     0,     0,     0,     0,   128,   129,   130,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     131,     0,   132,   133,   134,   135,   136,     0,   137,   138,
     139,   140,   141,   142,     0,   143,   144,   145,   127,     0,
       0,     0,     0,   759,     0,   128,   129,   130,   120,   121,
     122,   123,   124,   125,   126,     0,     0,     0,   131,     0,
     132,   133,   134,   135,   136,     0,   137,   138,   139,   140,
     141,   142,     0,   143,   144,   145,     0,     0,     0,     0,
       0,   772,     0,     0,     0,     0,   120,   121,   122,   123,
     124,   125,   126,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   127,     0,     0,     0,     0,     0,     0,
     128,   129,   130,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   131,     0,   132,   133,   134,   135,   136,
       0,   137,   138,   139,   140,   141,   142,     0,   143,   144,
     145,   127,     0,     0,     0,     0,   799,     0,   128,   129,
     130,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   131,     0,   132,   133,   134,   135,   136,     0,   137,
     138,   139,   140,   141,   142,     0,   143,   144,   145,     0,
       0,     0,     0,     0,   815,    54,    55,    56,    46,    47,
      48,    57,    58,    59,    60,    61,    62,    63,     0,     0,
       0,    64,     0,    65,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    66,     0,     0,     0,
       0,     0,     0,    67,     0,     0,     0,    68,    69,    70,
       0,     0,     0,     0,     0,    71,     0,    72,     0,    73,
       0,     0,     0,     0,     0,     0,     0,     2,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    74,
       0,     0,     0,     0,     0,     0,    75,     0,    76,     0,
     122,   123,   124,   125,   126,    77,    78,    79,     0,    80,
      81,     0,    82,    54,   167,    56,    46,    47,    48,    57,
      58,    59,    60,    61,    62,    63,     0,     0,     0,    64,
       0,    65,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    66,     0,     0,     0,     0,     0,
       0,    67,     0,   127,     0,    68,    69,    70,     0,     0,
       0,     0,     0,    71,     0,    72,     0,    73,     0,     0,
       0,     0,     0,     0,     0,     2,     0,     0,   135,   136,
       0,   137,   138,   139,   140,   141,   142,    74,   143,   144,
     145,     0,     0,     0,    75,     0,    76,     0,     0,     0,
       0,     0,     0,    77,    78,    79,     0,    80,    81,    54,
      82,    56,    46,    47,    48,    57,    58,    59,    60,    61,
      62,    63,     0,     0,     0,    64,     0,    65,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      66,     0,     0,     0,     0,     0,     0,    67,     0,     0,
       0,    68,    69,    70,     0,     0,     0,     0,     0,    71,
       0,    72,     0,    73,     0,     0,     0,     0,     0,     0,
       0,     2,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,     0,    76,     0,     0,     0,     0,     0,     0,    77,
      78,    79,     0,    80,    81,    54,    82,    56,    46,    47,
      48,    57,    58,    59,    60,    61,    62,    63,     0,     0,
       0,    64,     0,    65,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    66,   238,     0,   239,
       0,     0,     0,    67,     0,     0,     0,    68,    69,    70,
     240,     0,     0,     0,     0,    71,     0,     0,     0,     0,
       0,   241,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    74,
       0,     0,     0,     0,     0,     0,     0,   416,   242,     0,
       0,     0,     0,     0,     0,    77,    78,     0,     0,    80,
      81,    54,    82,    56,    46,    47,    48,    57,    58,    59,
      60,    61,    62,    63,     0,     0,     0,    64,     0,    65,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    66,   238,   552,   239,     0,     0,     0,    67,
       0,     0,     0,    68,    69,    70,   240,     0,     0,     0,
       0,    71,     0,     0,     0,     0,     0,   241,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    74,     0,     0,     0,     0,
       0,     0,     0,     0,   242,     0,     0,     0,     0,     0,
       0,    77,    78,     0,     0,    80,    81,    54,    82,    56,
      46,    47,    48,    57,    58,    59,    60,    61,    62,    63,
       0,     0,     0,    64,     0,    65,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    66,   238,
     736,   239,     0,     0,     0,    67,     0,     0,     0,    68,
      69,    70,   240,     0,     0,     0,     0,    71,     0,     0,
       0,     0,     0,   241,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    74,     0,     0,     0,     0,     0,     0,     0,     0,
     242,     0,     0,     0,     0,     0,     0,    77,    78,     0,
       0,    80,    81,    54,    82,    56,    46,    47,    48,    57,
      58,    59,    60,    61,    62,    63,     0,     0,     0,    64,
       0,    65,     0,     0,     0,     0,   120,   121,   122,   123,
     124,   125,   126,     0,    66,   238,     0,   239,     0,     0,
       0,    67,     0,     0,     0,    68,    69,    70,   240,     0,
       0,     0,     0,    71,     0,     0,     0,     0,     0,   241,
       0,     0,     0,     0,   120,   121,   122,   123,   124,   125,
     126,     0,     0,     0,     0,     0,     0,    74,     0,     0,
       0,   127,     0,     0,     0,     0,   242,     0,   128,   129,
     130,     0,     0,    77,    78,     0,     0,    80,    81,     0,
      82,   131,     0,   132,   133,   134,   135,   136,     0,   137,
     138,   139,   140,   141,   142,     0,   143,   144,   145,   127,
       0,     0,     0,   274,     0,     0,   128,   129,   130,   120,
     121,   122,   123,   124,   125,   126,     0,     0,     0,   131,
       0,   132,   133,   134,   135,   136,     0,   137,   138,   139,
     140,   141,   142,     0,   143,   144,   145,     0,     0,     0,
       0,   439,     0,     0,     0,     0,     0,   120,   121,   122,
     123,   124,   125,   126,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   127,     0,     0,     0,     0,     0,
       0,   128,   129,   130,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   131,     0,   132,   133,   134,   135,
     136,     0,   137,   138,   139,   140,   141,   142,     0,   143,
     144,   145,   127,     0,     0,     0,   609,     0,     0,   128,
     129,   130,   120,   121,   122,   123,   124,   125,   126,     0,
       0,     0,   131,     0,   132,   133,   134,   135,   136,     0,
     137,   138,   139,   140,   141,   142,     0,   143,   144,   145,
       0,     0,     0,     0,   610,     0,     0,     0,     0,     0,
     120,   121,   122,   123,   124,   125,   126,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   127,     0,     0,
       0,     0,     0,     0,   128,   129,   130,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   131,     0,   132,
     133,   134,   135,   136,     0,   137,   138,   139,   140,   141,
     142,     0,   143,   144,   145,   127,     0,     0,     0,   611,
       0,     0,   128,   129,   130,   120,   121,   122,   123,   124,
     125,   126,     0,     0,     0,   131,     0,   132,   133,   134,
     135,   136,     0,   137,   138,   139,   140,   141,   142,     0,
     143,   144,   145,     0,     0,     0,     0,   612,     0,     0,
       0,     0,     0,   120,   121,   122,   123,   124,   125,   126,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     127,     0,     0,     0,     0,     0,     0,   128,   129,   130,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     131,     0,   132,   133,   134,   135,   136,     0,   137,   138,
     139,   140,   141,   142,     0,   143,   144,   145,   127,     0,
       0,     0,   615,     0,     0,   128,   129,   130,   120,   121,
     122,   123,   124,   125,   126,     0,     0,     0,   131,     0,
     132,   133,   134,   135,   136,     0,   137,   138,   139,   140,
     141,   142,     0,   143,   144,   145,     0,     0,     0,     0,
     617,     0,     0,     0,     0,     0,   120,   121,   122,   123,
     124,   125,   126,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   127,     0,     0,     0,     0,     0,     0,
     128,   129,   130,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   131,     0,   132,   133,   134,   135,   136,
       0,   137,   138,   139,   140,   141,   142,     0,   143,   144,
     145,   127,     0,     0,     0,   618,     0,     0,   128,   129,
     130,   120,   121,   122,   123,   124,   125,   126,     0,     0,
       0,   131,     0,   132,   133,   134,   135,   136,     0,   137,
     138,   139,   140,   141,   142,     0,   143,   144,   145,     0,
       0,     0,     0,   656,     0,     0,     0,     0,     0,   120,
     121,   122,   123,   124,   125,   126,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   127,     0,     0,     0,
       0,     0,     0,   128,   129,   130,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   131,     0,   132,   133,
     134,   135,   136,     0,   137,   138,   139,   140,   141,   142,
       0,   143,   144,   145,   127,     0,     0,     0,   657,     0,
       0,   128,   129,   130,   120,   121,   122,   123,   124,   125,
     126,     0,     0,     0,   131,     0,   132,   133,   134,   135,
     136,     0,   137,   138,   139,   140,   141,   142,     0,   143,
     144,   145,     0,     0,     0,     0,   803,     0,     0,     0,
       0,     0,   120,   121,   122,   123,   124,   125,   126,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   127,
       0,     0,     0,     0,     0,     0,   128,   129,   130,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   131,
       0,   132,   133,   134,   135,   136,     0,   137,   138,   139,
     140,   141,   142,     0,   143,   144,   145,   127,     0,     0,
       0,   805,     0,     0,   128,   129,   130,   120,   121,   122,
     123,   124,   125,   126,     0,     0,     0,   131,     0,   132,
     133,   134,   135,   136,     0,   137,   138,   139,   140,   141,
     142,     0,   143,   144,   145,     0,     0,     0,     0,   856,
       0,   120,   121,   122,   123,   124,   125,   126,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   435,
     436,     0,   127,     0,     0,     0,     0,     0,     0,   128,
     129,   130,     0,     0,     0,   120,   121,   122,   123,   124,
     125,   126,   131,   437,   132,   133,   134,   135,   136,     0,
     137,   138,   139,   140,   141,   142,   127,   143,   144,   145,
       0,     0,     0,   128,   129,   130,     0,     0,     0,   120,
     121,   122,   123,   124,   125,   126,   131,   441,   132,   133,
     134,   135,   136,     0,   137,   138,   139,   140,   141,   142,
     127,   143,   144,   145,     0,     0,     0,   128,   129,   130,
       0,     0,     0,   120,     0,   122,   123,   124,   125,   126,
     131,     0,   132,   133,   134,   135,   136,     0,   137,   138,
     139,   140,   141,   142,   127,   143,   144,   145,     0,     0,
       0,   128,   129,   130,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   133,   134,   135,
     136,     0,   137,   138,   139,   140,   141,   142,   127,   143,
     144,   145,     0,     0,     0,   128,   129,   130,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   133,   134,   135,   136,     0,   137,   138,   139,   140,
     141,   142,     0,   143,   144,   145
};

static const yytype_int16 yycheck[] =
{
      18,    15,    10,   251,   238,   176,    21,   406,   201,   370,
     266,   348,    69,    70,   388,     5,   426,     5,     5,    80,
      40,     5,     5,    31,    32,    33,    34,    35,    36,    37,
      38,    39,    40,    41,    21,    53,   101,   401,   540,    13,
      56,   405,     5,     5,     5,   547,     5,     5,     5,     5,
       5,    53,     5,   414,     5,    16,     5,    75,    21,     5,
      66,     5,    21,   105,     5,    71,    84,   128,     5,   125,
     105,     5,   127,   128,    80,    18,     5,   133,    22,     8,
       9,    10,    84,     5,    46,     5,   128,     4,     5,   104,
      48,    49,   466,   128,   102,     0,    66,   105,   127,   473,
      35,   125,     4,     5,   133,     5,   171,   127,     5,   133,
      53,    81,   120,   121,   122,   123,   124,   125,   126,   127,
     128,   129,   130,   131,   132,   133,   134,   135,   136,   137,
     138,   139,   140,   141,   142,   143,   144,   145,   120,     5,
     124,    84,   130,   133,    56,   544,   133,   649,   162,   133,
     133,    48,    49,   218,    66,    43,   130,   165,     3,    71,
     176,   177,   572,   411,   501,   222,    83,   224,    80,   226,
     133,   187,   133,   119,   133,   431,   133,   133,   133,   543,
     133,    83,   133,   124,   133,   193,   130,   124,   125,   130,
     124,   125,   198,   130,   129,   203,   204,   126,   128,   129,
     208,    18,   114,   125,   210,   117,     4,     5,   125,   402,
      18,    18,    18,   695,    18,   386,   387,   699,   700,    85,
     238,    84,    67,   125,   598,    18,   125,    18,   127,   126,
     128,   733,   125,   251,   133,   133,    53,   126,   126,   128,
     128,    31,    32,    33,   125,    53,    53,    53,    46,    53,
     256,   128,   651,   119,   131,   320,   119,   120,   121,   125,
      53,   326,    53,   125,   176,   177,    12,    84,   276,   334,
     129,   133,   774,   127,   133,   187,    84,    84,    84,   191,
      84,   129,   125,    16,   127,   133,   198,   352,   790,   201,
     133,    84,     0,    84,    84,   126,     4,   305,   210,   492,
     135,   132,   127,     8,     9,   127,    11,   127,   133,   124,
     125,   133,   127,   133,   713,   330,    21,   551,    23,    24,
     695,   823,    16,   388,   699,   700,    98,   117,   344,   119,
     120,   121,   348,   127,   101,   734,   125,   394,   127,   133,
     397,   349,   130,   400,   256,   133,     5,   540,    11,    12,
      13,   127,   128,    16,   370,   363,   362,     6,   366,   367,
     368,    12,    13,   371,     5,    16,   372,   126,   376,   128,
     378,     5,   125,   379,   127,   383,   127,   128,   386,   387,
       4,   125,   390,   127,   126,   784,   128,   401,   126,   130,
     128,   405,     5,   411,   133,     8,     9,    10,   414,   407,
     406,   466,   127,   128,   412,   413,   129,   655,   656,     5,
     126,   772,   128,   127,   128,   423,   188,   189,   190,   125,
     127,   127,   126,   126,   128,   128,   434,   435,   436,   437,
     127,   128,   344,   441,    16,   443,   348,   445,   799,   126,
      29,   128,    31,    32,    33,    34,    35,   126,   129,   128,
     362,   126,     5,   128,   815,   126,     6,   128,   370,     5,
     372,     4,   129,    31,    32,    33,   126,   379,   128,   126,
     242,   128,   480,   481,   128,    18,    19,    20,   126,   487,
     128,   127,    25,    26,    27,   501,   126,   125,   128,   261,
     402,   127,   128,   265,   406,    84,   125,   127,   506,   129,
     127,   128,   414,    46,     5,   513,   514,   126,   125,   128,
     518,   126,   520,   128,   128,   126,    84,   128,   125,   108,
     109,   110,   125,   112,   113,   114,   115,   116,   117,   543,
     119,   120,   121,   551,     5,   126,   542,   128,   544,   125,
      83,   547,   127,   128,   792,   793,    21,   115,   116,   117,
     798,   119,   120,   121,   127,   126,   129,   128,   566,    68,
      69,    70,    71,    72,    73,    74,    75,    58,    58,    60,
      60,   579,    31,    32,    33,    34,    35,    52,   350,    58,
     492,    60,   127,   128,   356,   126,   126,   128,   128,   501,
     127,   128,   657,   601,    69,    70,   126,    72,   128,   127,
     128,   849,   608,   609,   127,   128,   614,   127,   128,   615,
       5,   617,   127,   128,   611,   612,   624,   125,   125,   125,
       5,   133,   127,    98,    99,    84,   129,   129,   540,   104,
     542,   125,   544,   125,   127,   547,   125,   655,   656,     5,
     646,     5,   129,   649,     5,   129,   129,   125,   420,   129,
     658,   127,   129,   127,   113,   114,   115,   116,   117,   127,
     119,   120,   121,     5,   127,   127,   674,   127,     5,     5,
     127,   127,   147,   681,   739,     5,   127,   129,     5,   127,
       5,   127,   125,   127,   129,   127,   127,    11,   127,    60,
     130,   166,   127,   701,   169,   131,   608,   609,   129,     5,
     706,   127,   132,   615,   127,   617,   125,   713,   132,   127,
     126,    58,   127,   188,   127,   127,   127,   127,   127,   127,
     127,   127,    60,     5,   127,   127,   131,   733,   734,     4,
     127,   127,    40,   127,   646,   105,    53,   649,   127,   127,
     127,     5,    58,   127,   127,    40,   105,   222,    53,   224,
       5,   226,   131,   127,   760,   761,   772,   232,   134,   127,
     766,    53,   534,    53,   536,   537,   538,   539,   774,    53,
      58,   127,     5,   127,   792,   793,   127,   127,   784,    58,
     798,    53,    60,   799,   790,   557,   127,   262,     4,     5,
       5,   266,   125,    58,   706,   127,    58,    60,   127,   815,
      58,   713,    18,    19,    20,   127,     4,    17,   478,    25,
      26,    27,   392,   162,   310,   593,   587,   823,    99,   624,
     739,   733,   734,   739,   457,   409,   276,    -1,    -1,    -1,
      46,   849,   840,    -1,    -1,    -1,   842,    -1,    -1,    -1,
      -1,    -1,   317,   318,    -1,    -1,   852,    -1,   760,   761,
      -1,    67,    -1,   328,   766,   330,    -1,    -1,    -1,    -1,
     772,    -1,   774,    -1,   636,    -1,    -1,    83,    -1,   641,
      -1,    -1,   784,    -1,    -1,    91,    92,    93,   790,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   799,   660,    -1,
     106,   107,   108,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     116,    -1,    -1,   815,    -1,    -1,    -1,    -1,    -1,   125,
     126,   823,    -1,    -1,   130,    -1,   132,    -1,    -1,    -1,
     136,   137,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     842,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     852,    -1,    -1,    -1,   419,   717,    -1,   422,     4,     5,
      -1,     4,     5,    -1,   429,    -1,   431,    -1,    -1,   731,
     732,    -1,    18,    19,    20,    18,    19,    20,    -1,    25,
      26,    27,    25,    26,    27,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    41,    42,
      46,    -1,    -1,    46,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    67,    -1,    -1,    67,   787,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,
      83,    -1,    -1,    -1,    -1,    91,    92,    93,    91,    92,
      93,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     106,   107,   108,   106,   107,   108,    -1,    -1,    -1,   534,
     116,   536,    -1,   116,    -1,    -1,    -1,    -1,    -1,   125,
     126,    -1,   125,    -1,   130,    -1,   132,   130,    -1,    -1,
     136,   137,    -1,   136,   137,    -1,     4,     5,    -1,     4,
       5,    -1,    -1,   568,    -1,    -1,    -1,    -1,    -1,    -1,
      18,    19,    20,    18,    19,    20,    -1,    25,    26,    27,
      25,    26,    27,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    46,    -1,
      -1,    46,    -1,    -1,    -1,    53,    54,    -1,    53,    54,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    67,
      -1,    -1,    67,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   637,   638,   639,    83,   641,   642,    83,    -1,
      -1,    -1,    -1,    91,    92,    93,    91,    92,    93,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   106,   107,
     108,   106,   107,   108,    -1,    -1,    -1,    -1,   116,    -1,
      -1,   116,    -1,    -1,    -1,    -1,    -1,   125,    -1,    -1,
     125,    -1,   130,     4,     5,   130,     4,     5,   136,   137,
      -1,   136,   137,    -1,    -1,    -1,    -1,    18,    19,    20,
      18,    19,    20,    -1,    25,    26,    27,    25,    26,    27,
      -1,    -1,    -1,   718,    -1,   720,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    46,   731,    -1,    46,    -1,
      -1,    -1,    53,    54,    -1,    53,    54,    -1,     4,     5,
      -1,    -1,    -1,    -1,    -1,    -1,    67,    -1,    -1,    67,
      -1,    -1,    18,    19,    20,    -1,    -1,    -1,    -1,    25,
      26,    27,    83,    -1,    -1,    83,    -1,    -1,    -1,    -1,
      91,    92,    93,    91,    92,    93,    -1,    -1,    -1,    -1,
      46,    -1,   787,   788,    -1,   106,   107,   108,   106,   107,
     108,    -1,    -1,    -1,    -1,   116,    -1,    -1,   116,    -1,
      -1,    67,    -1,    -1,   125,    -1,    -1,   125,    -1,   130,
      -1,    -1,   130,    -1,    -1,   136,   137,    83,   136,   137,
      -1,    -1,    -1,     4,     5,    91,    92,    93,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    18,    19,    20,
     106,   107,   108,   109,    25,    26,    27,    -1,    -1,    -1,
     116,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   125,
      -1,    -1,    -1,    -1,   130,    46,    -1,    -1,    -1,    -1,
     136,   137,    -1,     4,     5,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    67,    18,    19,    20,
      -1,    -1,    -1,    -1,    25,    26,    27,    -1,    -1,    -1,
      -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,     4,     5,
      91,    92,    93,    -1,    -1,    46,    -1,    -1,    -1,    -1,
      -1,    -1,    18,    19,    20,   106,   107,   108,    -1,    25,
      26,    27,    -1,    -1,    -1,   116,    67,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   125,   126,    -1,    -1,    -1,   130,
      46,    -1,    83,    -1,    -1,   136,   137,    -1,     4,     5,
      91,    92,    93,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    67,    18,    19,    20,   106,   107,   108,    -1,    25,
      26,    27,    -1,    -1,    -1,   116,    -1,    83,    -1,    -1,
      -1,    -1,    -1,   124,   125,    91,    92,    93,    -1,   130,
      46,    -1,    -1,    -1,    -1,   136,   137,    -1,    54,    -1,
     106,   107,   108,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     116,    67,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   125,
      -1,    -1,    -1,    -1,   130,    -1,   132,    83,    -1,    -1,
     136,   137,    -1,     4,     5,    91,    92,    93,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    18,    19,    20,
     106,   107,   108,    -1,    25,    26,    27,    -1,    -1,    -1,
     116,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   125,
      -1,    -1,    -1,    -1,   130,    46,    -1,    -1,    -1,    -1,
     136,   137,    -1,    54,     4,     5,    -1,    -1,     4,     5,
      -1,    -1,    -1,    -1,    -1,    -1,    67,    -1,    18,    19,
      20,    -1,    18,    19,    20,    25,    26,    27,    -1,    25,
      26,    27,    83,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      91,    92,    93,    -1,    -1,    -1,    46,    -1,    -1,    -1,
      46,    -1,    -1,    -1,    -1,   106,   107,   108,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   116,    -1,    67,    -1,    -1,
      -1,    67,    -1,    -1,   125,    -1,    -1,    -1,    -1,   130,
      -1,    -1,    -1,    83,    -1,   136,   137,    83,    -1,    -1,
      -1,    91,    92,    93,    -1,    91,    92,    93,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   106,   107,   108,    -1,
     106,   107,   108,    -1,    -1,    -1,   116,    -1,    -1,    -1,
     116,    -1,     5,    -1,     7,   125,   126,    -1,    11,   125,
     130,    -1,    -1,    -1,   130,    -1,   136,   137,    21,    22,
     136,   137,    -1,    -1,    -1,    -1,    29,    30,    31,    32,
      33,    34,    35,    -1,    37,    -1,    39,    -1,    -1,    -1,
      -1,    44,    45,    -1,    -1,    -1,    -1,    50,    51,    52,
      -1,    -1,    -1,    56,    -1,    -1,    -1,    -1,    61,    62,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    76,    -1,    78,    79,    -1,    -1,    -1,
      -1,    84,    -1,    -1,    -1,    -1,    89,    90,    91,    92,
      93,    94,    -1,    -1,    -1,    98,    -1,    -1,    -1,    -1,
     103,   104,    -1,   106,   107,   108,   109,   110,    -1,   112,
     113,   114,   115,   116,   117,    -1,   119,   120,   121,    -1,
      -1,   124,    -1,    -1,   127,    -1,    -1,   130,    -1,    -1,
      -1,     5,   135,     7,     8,     9,    -1,    11,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    21,    22,    23,
      24,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    37,    -1,    39,    -1,    -1,    -1,    -1,
      44,    45,    -1,    -1,    -1,    -1,    50,    51,    52,    -1,
      -1,    -1,    56,    -1,    -1,    -1,    -1,    61,    62,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,     5,    76,     7,    78,    79,    -1,    11,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    89,    90,    21,    22,    -1,
      94,    -1,    -1,    -1,    98,    -1,    -1,    -1,    -1,   103,
      -1,    -1,    -1,    37,    38,    39,    -1,    -1,    -1,    -1,
      44,    45,    -1,    -1,    -1,    -1,    50,    51,    52,    -1,
     124,    -1,    56,    -1,    -1,    -1,   130,    61,    62,    -1,
      -1,   135,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,     5,    76,     7,    78,    79,    -1,    11,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    89,    90,    21,    22,    -1,
      94,    -1,    -1,    -1,    98,    -1,    -1,    -1,    -1,   103,
      -1,   105,    -1,    37,    -1,    39,    -1,    -1,    -1,    -1,
      44,    45,    -1,    -1,    -1,    -1,    50,    51,    52,    -1,
     124,    -1,    56,    -1,    -1,    -1,   130,    61,    62,    -1,
      -1,   135,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,     5,    76,     7,    78,    79,    -1,    11,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    89,    90,    21,    22,    -1,
      94,    -1,    -1,    -1,    98,    -1,    -1,    -1,    -1,   103,
      -1,    -1,    -1,    37,    38,    39,    -1,    -1,    -1,    -1,
      44,    45,    -1,    -1,    -1,    -1,    50,    51,    52,    -1,
     124,    -1,    56,   127,    -1,    -1,   130,    61,    62,    -1,
      -1,   135,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,     5,    76,     7,    78,    79,    -1,    11,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    89,    90,    21,    22,    -1,
      94,    -1,    -1,    -1,    98,    -1,    -1,    -1,    -1,   103,
      -1,    -1,    -1,    37,    -1,    39,    -1,    -1,    -1,    -1,
      44,    45,    -1,    -1,    -1,    -1,    50,    51,    52,    -1,
     124,    -1,    56,    -1,    -1,    -1,   130,    61,    62,    -1,
      -1,   135,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    76,    77,    78,    79,     5,    -1,     7,    -1,
      -1,    -1,    11,    -1,    -1,    89,    90,    -1,    -1,    -1,
      94,    -1,    21,    22,    98,    -1,    -1,    -1,    -1,   103,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    37,    -1,
      39,    -1,    -1,    -1,    -1,    44,    45,    -1,    -1,    -1,
     124,    50,    51,    52,    -1,    -1,   130,    56,    -1,    58,
      -1,   135,    61,    62,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,     5,    76,     7,    78,
      79,    -1,    11,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      89,    90,    21,    22,    -1,    94,    -1,    -1,    -1,    98,
      -1,    -1,    -1,    -1,   103,    -1,    -1,    -1,    37,    38,
      39,    -1,    -1,    -1,    -1,    44,    45,    -1,    -1,    -1,
      -1,    50,    51,    52,    -1,   124,    -1,    56,    -1,    -1,
      -1,   130,    61,    62,    -1,    -1,   135,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,     5,    76,     7,    78,
      79,    -1,    11,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      89,    90,    21,    22,    -1,    94,    -1,    -1,    -1,    98,
      -1,    -1,    -1,    -1,   103,    -1,    -1,    -1,    37,    -1,
      39,    -1,    -1,    -1,    -1,    44,    45,    -1,    -1,    -1,
      -1,    50,    51,    52,    -1,   124,    -1,    56,    -1,    58,
      -1,   130,    61,    62,    -1,    -1,   135,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,     5,    76,     7,    78,
      79,    -1,    11,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      89,    90,    21,    22,    -1,    94,    -1,    -1,    -1,    98,
      -1,    -1,    -1,    -1,   103,    -1,    -1,    -1,    37,    -1,
      39,    -1,    -1,    -1,    -1,    44,    45,    -1,    -1,    -1,
      -1,    50,    51,    52,    -1,   124,    -1,    56,    -1,    -1,
      -1,   130,    61,    62,    -1,    -1,   135,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,     5,    76,     7,    78,
      79,    -1,    11,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      89,    90,    21,    22,    -1,    94,    -1,    -1,    -1,    98,
      -1,    -1,    -1,    -1,   103,    -1,    -1,    -1,    37,    -1,
      39,    -1,    -1,    -1,    -1,    44,    45,    -1,    -1,    -1,
      -1,    50,    51,    52,    -1,   124,    -1,    56,   127,    -1,
      -1,   130,    61,    62,    -1,    -1,   135,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,     5,    76,     7,    78,
      79,    -1,    11,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      89,    90,    21,    22,    -1,    94,    -1,    -1,    -1,    98,
      -1,    -1,    -1,    -1,   103,    -1,    -1,    -1,    37,    -1,
      39,    -1,    -1,    -1,    -1,    44,    45,    -1,    -1,    -1,
      -1,    50,    51,    52,    -1,   124,    -1,    56,   127,    -1,
      -1,   130,    61,    62,    -1,    -1,   135,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    76,    -1,    78,
      79,    -1,    -1,    29,    -1,    31,    32,    33,    34,    35,
      89,    90,    -1,    -1,    -1,    94,    -1,    -1,    -1,    98,
      -1,    -1,    -1,     5,   103,     7,     8,     9,    10,    11,
      12,    13,    14,    15,    16,    17,    -1,    -1,    -1,    21,
      -1,    23,    -1,    -1,    -1,   124,    -1,    -1,    -1,    -1,
      -1,   130,    -1,    -1,    36,    37,   135,    39,    84,    -1,
      -1,    43,    -1,    -1,    -1,    47,    48,    49,    50,    -1,
      -1,    -1,    -1,    55,    -1,    -1,    -1,    -1,    -1,    61,
      -1,    -1,    -1,   109,   110,    -1,   112,   113,   114,   115,
     116,   117,    -1,   119,   120,   121,    -1,    79,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    88,    -1,    -1,    -1,
      -1,    -1,    -1,    95,    96,    -1,    -1,    99,   100,     5,
     102,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      16,    17,    -1,    -1,    -1,    21,    -1,    23,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   127,    -1,    -1,    -1,    -1,
      36,    37,    -1,    39,    -1,    -1,    -1,    43,    -1,    -1,
      -1,    47,    48,    49,    50,    -1,    -1,    -1,    -1,    55,
      -1,    -1,    -1,    -1,    -1,    61,    29,    30,    31,    32,
      33,    34,    35,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    79,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    88,    -1,    -1,    -1,    -1,    -1,    -1,    95,
      96,    -1,    -1,    99,   100,    -1,   102,    -1,    -1,    -1,
      29,    30,    31,    32,    33,    34,    35,    -1,    81,    82,
      -1,    84,    -1,    -1,    -1,    -1,    -1,    -1,    91,    92,
      93,   127,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   104,   105,   106,   107,   108,   109,   110,    -1,   112,
     113,   114,   115,   116,   117,    -1,   119,   120,   121,    -1,
      -1,    -1,    -1,    -1,    -1,    84,    -1,    -1,    -1,    -1,
      -1,   134,    91,    92,    93,    29,    30,    31,    32,    33,
      34,    35,    -1,    -1,    -1,   104,    -1,   106,   107,   108,
     109,   110,    -1,   112,   113,   114,   115,   116,   117,    -1,
     119,   120,   121,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   134,    -1,    -1,    -1,    29,
      30,    31,    32,    33,    34,    35,    -1,    -1,    -1,    -1,
      84,    -1,    -1,    -1,    -1,    -1,    -1,    91,    92,    93,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     104,    -1,   106,   107,   108,   109,   110,    -1,   112,   113,
     114,   115,   116,   117,    -1,   119,   120,   121,    -1,    -1,
      -1,    -1,    -1,    -1,    84,    -1,    -1,    -1,    -1,    -1,
     134,    91,    92,    93,    29,    30,    31,    32,    33,    34,
      35,    -1,    -1,    -1,   104,    -1,   106,   107,   108,   109,
     110,    -1,   112,   113,   114,   115,   116,   117,    -1,   119,
     120,   121,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   134,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    84,
      -1,    -1,    -1,    -1,    -1,    -1,    91,    92,    93,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   104,
      -1,   106,   107,   108,   109,   110,    -1,   112,   113,   114,
     115,   116,   117,    -1,   119,   120,   121,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,     5,   130,     7,     8,     9,    10,
      11,    12,    13,    14,    15,    16,    17,    -1,    -1,    -1,
      21,    -1,    23,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    36,    37,    -1,    39,    -1,
      -1,    -1,    43,    -1,    -1,    -1,    47,    48,    49,    50,
      -1,    -1,    -1,    -1,    55,    -1,    -1,    -1,    -1,    -1,
      61,    29,    30,    31,    32,    33,    34,    35,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    79,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    88,    -1,    -1,
      -1,    -1,    -1,    -1,    95,    96,    -1,    -1,    99,   100,
      -1,   102,    -1,    -1,   105,    29,    30,    31,    32,    33,
      34,    35,    -1,    -1,    -1,    -1,    84,    -1,    -1,    -1,
      -1,    -1,    -1,    91,    92,    93,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   104,    -1,   106,   107,
     108,   109,   110,    -1,   112,   113,   114,   115,   116,   117,
      -1,   119,   120,   121,    -1,    -1,    -1,    -1,    -1,    -1,
      84,   129,    -1,    -1,    -1,    -1,    -1,    91,    92,    93,
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
      91,    92,    93,    29,    30,    31,    32,    33,    34,    35,
      -1,    -1,    -1,   104,    -1,   106,   107,   108,   109,   110,
      -1,   112,   113,   114,   115,   116,   117,    -1,   119,   120,
     121,    -1,    -1,    -1,    -1,    -1,   127,    -1,    -1,    -1,
      -1,    29,    30,    31,    32,    33,    34,    35,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    84,    -1,
      -1,    -1,    -1,    -1,    -1,    91,    92,    93,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   104,    -1,
     106,   107,   108,   109,   110,    -1,   112,   113,   114,   115,
     116,   117,    -1,   119,   120,   121,    84,    -1,    -1,    -1,
      -1,   127,    -1,    91,    92,    93,    29,    30,    31,    32,
      33,    34,    35,    -1,    -1,    -1,   104,    -1,   106,   107,
     108,   109,   110,    -1,   112,   113,   114,   115,   116,   117,
      -1,   119,   120,   121,    -1,    -1,    -1,    -1,    -1,   127,
      -1,    -1,    -1,    -1,    29,    30,    31,    32,    33,    34,
      35,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    84,    -1,    -1,    -1,    -1,    -1,    -1,    91,    92,
      93,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   104,    -1,   106,   107,   108,   109,   110,    -1,   112,
     113,   114,   115,   116,   117,    -1,   119,   120,   121,    84,
      -1,    -1,    -1,    -1,   127,    -1,    91,    92,    93,    29,
      30,    31,    32,    33,    34,    35,    -1,    -1,    -1,   104,
      -1,   106,   107,   108,   109,   110,    -1,   112,   113,   114,
     115,   116,   117,    -1,   119,   120,   121,    -1,    -1,    -1,
      -1,    -1,   127,    -1,    -1,    -1,    -1,    29,    30,    31,
      32,    33,    34,    35,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    84,    -1,    -1,    -1,    -1,    -1,
      -1,    91,    92,    93,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   104,    -1,   106,   107,   108,   109,
     110,    -1,   112,   113,   114,   115,   116,   117,    -1,   119,
     120,   121,    84,    -1,    -1,    -1,    -1,   127,    -1,    91,
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
      93,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   104,    -1,   106,   107,   108,   109,   110,    -1,   112,
     113,   114,   115,   116,   117,    -1,   119,   120,   121,    -1,
      -1,    -1,    -1,    -1,   127,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    16,    17,    -1,    -1,
      -1,    21,    -1,    23,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    36,    -1,    -1,    -1,
      -1,    -1,    -1,    43,    -1,    -1,    -1,    47,    48,    49,
      -1,    -1,    -1,    -1,    -1,    55,    -1,    57,    -1,    59,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    67,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    79,
      -1,    -1,    -1,    -1,    -1,    -1,    86,    -1,    88,    -1,
      31,    32,    33,    34,    35,    95,    96,    97,    -1,    99,
     100,    -1,   102,     5,     6,     7,     8,     9,    10,    11,
      12,    13,    14,    15,    16,    17,    -1,    -1,    -1,    21,
      -1,    23,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    36,    -1,    -1,    -1,    -1,    -1,
      -1,    43,    -1,    84,    -1,    47,    48,    49,    -1,    -1,
      -1,    -1,    -1,    55,    -1,    57,    -1,    59,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    67,    -1,    -1,   109,   110,
      -1,   112,   113,   114,   115,   116,   117,    79,   119,   120,
     121,    -1,    -1,    -1,    86,    -1,    88,    -1,    -1,    -1,
      -1,    -1,    -1,    95,    96,    97,    -1,    99,   100,     5,
     102,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      16,    17,    -1,    -1,    -1,    21,    -1,    23,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      36,    -1,    -1,    -1,    -1,    -1,    -1,    43,    -1,    -1,
      -1,    47,    48,    49,    -1,    -1,    -1,    -1,    -1,    55,
      -1,    57,    -1,    59,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    67,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    79,    -1,    -1,    -1,    -1,    -1,    -1,
      86,    -1,    88,    -1,    -1,    -1,    -1,    -1,    -1,    95,
      96,    97,    -1,    99,   100,     5,   102,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    16,    17,    -1,    -1,
      -1,    21,    -1,    23,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    36,    37,    -1,    39,
      -1,    -1,    -1,    43,    -1,    -1,    -1,    47,    48,    49,
      50,    -1,    -1,    -1,    -1,    55,    -1,    -1,    -1,    -1,
      -1,    61,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    79,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    87,    88,    -1,
      -1,    -1,    -1,    -1,    -1,    95,    96,    -1,    -1,    99,
     100,     5,   102,     7,     8,     9,    10,    11,    12,    13,
      14,    15,    16,    17,    -1,    -1,    -1,    21,    -1,    23,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    36,    37,    38,    39,    -1,    -1,    -1,    43,
      -1,    -1,    -1,    47,    48,    49,    50,    -1,    -1,    -1,
      -1,    55,    -1,    -1,    -1,    -1,    -1,    61,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    79,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    88,    -1,    -1,    -1,    -1,    -1,
      -1,    95,    96,    -1,    -1,    99,   100,     5,   102,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    16,    17,
      -1,    -1,    -1,    21,    -1,    23,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    36,    37,
      38,    39,    -1,    -1,    -1,    43,    -1,    -1,    -1,    47,
      48,    49,    50,    -1,    -1,    -1,    -1,    55,    -1,    -1,
      -1,    -1,    -1,    61,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    79,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      88,    -1,    -1,    -1,    -1,    -1,    -1,    95,    96,    -1,
      -1,    99,   100,     5,   102,     7,     8,     9,    10,    11,
      12,    13,    14,    15,    16,    17,    -1,    -1,    -1,    21,
      -1,    23,    -1,    -1,    -1,    -1,    29,    30,    31,    32,
      33,    34,    35,    -1,    36,    37,    -1,    39,    -1,    -1,
      -1,    43,    -1,    -1,    -1,    47,    48,    49,    50,    -1,
      -1,    -1,    -1,    55,    -1,    -1,    -1,    -1,    -1,    61,
      -1,    -1,    -1,    -1,    29,    30,    31,    32,    33,    34,
      35,    -1,    -1,    -1,    -1,    -1,    -1,    79,    -1,    -1,
      -1,    84,    -1,    -1,    -1,    -1,    88,    -1,    91,    92,
      93,    -1,    -1,    95,    96,    -1,    -1,    99,   100,    -1,
     102,   104,    -1,   106,   107,   108,   109,   110,    -1,   112,
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
      -1,    -1,    -1,   126,    -1,    -1,    -1,    -1,    -1,    29,
      30,    31,    32,    33,    34,    35,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    84,    -1,    -1,    -1,
      -1,    -1,    -1,    91,    92,    93,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   104,    -1,   106,   107,
     108,   109,   110,    -1,   112,   113,   114,   115,   116,   117,
      -1,   119,   120,   121,    84,    -1,    -1,    -1,   126,    -1,
      -1,    91,    92,    93,    29,    30,    31,    32,    33,    34,
      35,    -1,    -1,    -1,   104,    -1,   106,   107,   108,   109,
     110,    -1,   112,   113,   114,   115,   116,   117,    -1,   119,
     120,   121,    -1,    -1,    -1,    -1,   126,    -1,    -1,    -1,
      -1,    -1,    29,    30,    31,    32,    33,    34,    35,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    84,
      -1,    -1,    -1,    -1,    -1,    -1,    91,    92,    93,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   104,
      -1,   106,   107,   108,   109,   110,    -1,   112,   113,   114,
     115,   116,   117,    -1,   119,   120,   121,    84,    -1,    -1,
      -1,   126,    -1,    -1,    91,    92,    93,    29,    30,    31,
      32,    33,    34,    35,    -1,    -1,    -1,   104,    -1,   106,
     107,   108,   109,   110,    -1,   112,   113,   114,   115,   116,
     117,    -1,   119,   120,   121,    -1,    -1,    -1,    -1,   126,
      -1,    29,    30,    31,    32,    33,    34,    35,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    81,
      82,    -1,    84,    -1,    -1,    -1,    -1,    -1,    -1,    91,
      92,    93,    -1,    -1,    -1,    29,    30,    31,    32,    33,
      34,    35,   104,   105,   106,   107,   108,   109,   110,    -1,
     112,   113,   114,   115,   116,   117,    84,   119,   120,   121,
      -1,    -1,    -1,    91,    92,    93,    -1,    -1,    -1,    29,
      30,    31,    32,    33,    34,    35,   104,   105,   106,   107,
     108,   109,   110,    -1,   112,   113,   114,   115,   116,   117,
      84,   119,   120,   121,    -1,    -1,    -1,    91,    92,    93,
      -1,    -1,    -1,    29,    -1,    31,    32,    33,    34,    35,
     104,    -1,   106,   107,   108,   109,   110,    -1,   112,   113,
     114,   115,   116,   117,    84,   119,   120,   121,    -1,    -1,
      -1,    91,    92,    93,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   107,   108,   109,
     110,    -1,   112,   113,   114,   115,   116,   117,    84,   119,
     120,   121,    -1,    -1,    -1,    91,    92,    93,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   107,   108,   109,   110,    -1,   112,   113,   114,   115,
     116,   117,    -1,   119,   120,   121
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
     127,   126,   128,     5,    21,   133,   204,     6,   147,     5,
     124,   125,   175,     5,   124,   125,   155,   172,   192,   193,
     202,   208,    16,    16,     5,   203,     5,     7,    11,    21,
      22,    37,    39,    44,    45,    50,    51,    52,    56,    61,
      62,    76,    78,    89,    90,    94,    98,   103,   124,   135,
     181,   185,   188,   189,   190,   191,   202,     5,   125,     5,
     165,   166,    16,   165,   204,   165,   204,   181,   185,     5,
      21,   157,   204,     5,     5,    46,   186,   187,    37,    39,
      50,    61,    88,   150,   153,   154,   162,   163,   164,   169,
     176,   178,   179,   180,   188,   185,   181,   101,     6,   147,
     203,   204,     5,   151,   152,   175,   204,     4,   200,   212,
     212,   204,   205,   212,   126,   208,   128,   131,   208,   212,
     212,   212,   212,   212,   212,   212,   212,   212,   212,   212,
     212,   212,   212,   212,   212,   212,   212,   212,   212,   212,
     212,   212,   212,   212,   212,   129,     5,   204,     5,   126,
     128,    16,   127,   146,   129,     5,   212,     5,   204,     6,
     125,   127,   204,     4,     5,    83,   125,   200,     5,   204,
     205,     4,     5,    83,   125,    68,    69,    70,    71,    72,
      73,    74,    75,   156,   172,   202,   202,   127,   128,   129,
     128,   127,   125,   127,   202,   203,   204,   203,   203,    38,
     105,   185,   201,   125,   212,     5,   125,   125,   125,   185,
     125,   125,   201,     5,   212,   212,   125,     5,   125,   212,
       5,    85,   119,   125,   127,   185,    35,   129,   125,   200,
     129,   127,   128,   165,   204,   127,   165,   204,   127,   165,
     204,   125,   127,     5,   204,   125,   127,   129,    80,   128,
     105,   178,   125,   125,   125,   203,    87,   179,   185,    13,
     130,   127,   203,   129,   204,   127,   128,     5,   203,     5,
     152,   204,     5,   126,   128,    81,    82,   105,   134,   126,
     210,   105,   212,   129,     5,   129,   168,     4,    18,    19,
      20,    25,    26,    27,    46,    83,   211,   129,   204,     5,
     204,   126,   132,   170,   171,   200,   125,   126,   132,   173,
     174,   200,   126,   125,   204,   204,   205,   200,   128,   202,
     129,   129,   193,   212,   203,   126,   200,   129,   127,   203,
     127,   127,     5,    38,   185,   212,   127,   127,   212,   212,
     212,    22,   192,   212,    77,   127,   129,   127,   212,   127,
     212,   127,   185,    41,    42,   183,   184,   212,   172,   212,
     172,   212,   170,   200,   126,   212,   166,   127,   165,   127,
     165,   127,   165,   145,     8,     9,    11,    21,    23,    24,
     160,   161,   201,   125,   127,     5,   145,   160,   185,   212,
     187,     5,    38,   212,   212,   192,   127,   130,   204,   203,
     127,   204,   212,   127,     5,   151,   129,   127,   204,   127,
       5,   152,   204,   212,   212,   212,   212,   212,   212,   129,
     212,   211,     5,   127,     5,   119,   126,   128,   126,   170,
     200,     5,   126,   128,   126,   127,   126,   170,   125,   126,
     156,   129,   212,   212,   127,   126,   212,   127,   201,   126,
     126,   126,   126,   193,   127,   126,   212,   126,   126,   212,
     212,    43,   126,   128,   182,   212,   127,   212,   127,   126,
     126,   127,   127,   127,   127,   126,    21,   203,   204,    11,
     203,   204,   203,   203,   203,   161,   201,    58,   145,   160,
     185,   127,   126,   185,    60,   178,   126,   126,   127,   203,
     130,   131,   127,   212,   127,   204,   127,   127,     5,   151,
     134,   134,   134,   212,   125,   133,   127,   171,   127,   126,
     126,   125,   174,   127,   126,   170,   126,   212,   127,   127,
     127,   127,    38,   185,    54,   194,   196,   198,   200,   194,
     194,   127,   212,   185,   127,   185,    40,   127,   184,   127,
     127,   127,   127,   127,   203,   127,   204,   204,   204,   127,
       5,   203,   204,   127,   204,   127,   127,    58,   126,   185,
      58,    11,    21,   160,   127,    60,    38,   179,    54,   195,
     197,   199,   200,   212,   131,   203,     5,   127,   127,   127,
     127,   126,   212,     4,   127,   127,   212,   127,   126,   127,
      40,   105,    53,   196,   198,    53,   105,    53,   198,    53,
     198,   212,   127,   185,   160,   185,   127,   127,   203,   204,
     204,   127,     5,   127,   127,    58,   203,   204,   203,   185,
     160,   185,    40,   105,    53,   197,   199,    53,   105,   127,
       5,   131,   127,   126,   134,   126,   127,   185,   127,   185,
      53,   127,   185,    53,    53,   127,   192,   185,    58,   127,
       5,   127,   127,   160,   185,   127,   203,   127,    58,   185,
      60,   179,   127,   179,    53,   127,   179,   192,   127,     5,
     125,   192,   126,    58,   127,   185,    58,   127,    60,   126,
     127,   212,   126,   185,    58,   179,   126,   185
};

/* YYR1[RULE-NUM] -- Symbol kind of the left-hand side of rule RULE-NUM.  */
static const yytype_uint8 yyr1[] =
{
       0,   138,   139,   140,   140,   141,   141,   142,   142,   142,
     142,   143,   143,   144,   144,   144,   145,   145,   146,   146,
     146,   146,   146,   146,   146,   146,   146,   147,   147,   148,
     148,   148,   148,   148,   148,   148,   148,   148,   148,   148,
     148,   148,   148,   149,   149,   149,   149,   149,   150,   151,
     151,   152,   152,   153,   153,   153,   153,   153,   153,   153,
     153,   153,   153,   153,   153,   153,   153,   153,   153,   153,
     153,   154,   154,   154,   154,   155,   156,   156,   156,   156,
     156,   156,   156,   156,   157,   157,   158,   158,   158,   158,
     158,   158,   158,   158,   158,   159,   159,   159,   159,   160,
     160,   161,   161,   161,   161,   161,   161,   161,   161,   161,
     161,   161,   161,   161,   162,   162,   162,   162,   162,   163,
     163,   163,   164,   165,   165,   166,   167,   167,   168,   168,
     168,   168,   169,   169,   169,   169,   169,   169,   169,   169,
     169,   169,   169,   169,   169,   170,   170,   171,   171,   171,
     171,   172,   172,   172,   172,   173,   173,   174,   174,   175,
     175,   175,   175,   175,   175,   176,   176,   176,   176,   177,
     178,   178,   179,   179,   179,   179,   179,   179,   179,   179,
     179,   179,   179,   179,   179,   179,   179,   179,   179,   179,
     180,   181,   181,   181,   181,   182,   182,   183,   183,   184,
     184,   184,   185,   185,   185,   185,   185,   185,   185,   185,
     185,   185,   185,   185,   185,   185,   185,   185,   185,   185,
     185,   185,   185,   185,   185,   185,   185,   185,   185,   185,
     185,   185,   185,   185,   185,   185,   185,   185,   185,   185,
     185,   185,   185,   186,   186,   187,   187,   188,   189,   189,
     190,   191,   192,   192,   193,   194,   194,   195,   195,   196,
     196,   197,   197,   198,   198,   199,   199,   200,   200,   201,
     201,   202,   202,   202,   202,   202,   202,   203,   203,   204,
     204,   204,   205,   206,   206,   206,   206,   206,   206,   206,
     206,   206,   206,   206,   206,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   208,   209,
     209,   210,   210,   210,   211,   211,   211,   211,   211,   211,
     211,   211,   211,   212,   212,   212,   212,   212,   212,   212,
     212,   212,   212,   212,   212,   212,   212,   212,   212,   212,
     212,   212,   212,   212,   212,   212,   212,   212,   212,   212,
     212,   212,   212,   212,   212,   212,   212,   212,   212,   212,
     212,   212,   212,   212,   212,   212,   212,   212,   212,   212,
     212,   212,   212,   212,   212,   212,   212
};

/* YYR2[RULE-NUM] -- Number of symbols on the right-hand side of rule RULE-NUM.  */
static const yytype_int8 yyr2[] =
{
       0,     2,     1,     2,     1,     1,     1,     6,     5,     5,
       4,     4,     3,     1,     4,     3,     3,     1,     2,     3,
       3,     4,     4,     5,     1,     4,     5,     2,     0,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     2,     2,     3,     6,     2,     1,
       3,     3,     1,     3,     4,     5,     3,     3,     4,     5,
       6,     5,     6,     5,     6,     4,     4,     6,     9,     8,
       7,     3,     6,     7,     6,     5,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     6,     5,     8,     7,
       6,     8,     9,     9,    10,     6,     5,     8,     9,     2,
       1,     3,     3,     3,     4,     5,     5,     6,     3,     4,
       5,     4,     3,     4,     3,     4,     4,     5,     5,     3,
       4,     5,     3,     3,     1,     3,     3,     1,     4,     4,
       5,     3,     5,     6,     3,     5,     6,     6,     6,     6,
       5,     7,     8,     7,     7,     3,     1,     2,     5,     4,
       8,     4,     2,     2,     2,     3,     1,     5,     2,     4,
       2,     2,     2,     4,     3,     3,     2,     2,     3,     3,
       2,     1,     3,     5,     3,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     5,     7,     6,     7,     6,
       9,     2,     2,     2,     4,     1,     1,     3,     1,     2,
       2,     1,     3,     2,     2,     5,     3,     4,     5,     4,
       5,     5,     7,     3,     3,     3,     3,     4,     3,     5,
       2,     3,     3,     4,     5,     6,     7,     6,     6,     7,
       6,     7,     3,     3,     2,     1,     1,     1,     1,     5,
       3,     5,     6,     3,     1,     3,     1,     3,     9,    10,
       5,     5,     3,     1,     3,     2,     1,     2,     1,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     1,     2,
       1,     1,     2,     3,     3,     2,     1,     3,     1,     5,
       5,     5,     3,     1,     1,     1,     2,     2,     2,     2,
       2,     2,     3,     2,     2,     1,     1,     1,     1,     1,
       1,     2,     2,     1,     1,     1,     1,     1,     3,     3,
       1,     2,     1,     2,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     4,     1,
       1,     1,     1,     1,     1,     2,     3,     3,     2,     5,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     4,     3,     1,     2,     2,
       2,     2,     2,     2,     2,     2,     2
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

#line 3058 "y.tab.c"

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

#line 399 "yaccs/verilog.yacc"

