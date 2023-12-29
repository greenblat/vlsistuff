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
    shift_left = 358,              /* shift_left  */
    shift_right = 359,             /* shift_right  */
    SignedLeft = 360,              /* SignedLeft  */
    arith_shift_right = 361,       /* arith_shift_right  */
    noteqeq = 362,                 /* noteqeq  */
    Veryequal = 363,               /* Veryequal  */
    StarStar = 364,                /* StarStar  */
    UNARY_PREC = 365               /* UNARY_PREC  */
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
#define shift_left 358
#define shift_right 359
#define SignedLeft 360
#define arith_shift_right 361
#define noteqeq 362
#define Veryequal 363
#define StarStar 364
#define UNARY_PREC 365

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
  YYSYMBOL_103_ = 103,                     /* '?'  */
  YYSYMBOL_104_ = 104,                     /* ':'  */
  YYSYMBOL_105_ = 105,                     /* '|'  */
  YYSYMBOL_106_ = 106,                     /* '^'  */
  YYSYMBOL_107_ = 107,                     /* '&'  */
  YYSYMBOL_shift_left = 108,               /* shift_left  */
  YYSYMBOL_shift_right = 109,              /* shift_right  */
  YYSYMBOL_SignedLeft = 110,               /* SignedLeft  */
  YYSYMBOL_arith_shift_right = 111,        /* arith_shift_right  */
  YYSYMBOL_112_ = 112,                     /* '<'  */
  YYSYMBOL_113_ = 113,                     /* '>'  */
  YYSYMBOL_114_ = 114,                     /* '+'  */
  YYSYMBOL_115_ = 115,                     /* '-'  */
  YYSYMBOL_noteqeq = 116,                  /* noteqeq  */
  YYSYMBOL_Veryequal = 117,                /* Veryequal  */
  YYSYMBOL_118_ = 118,                     /* '*'  */
  YYSYMBOL_119_ = 119,                     /* '/'  */
  YYSYMBOL_120_ = 120,                     /* '%'  */
  YYSYMBOL_StarStar = 121,                 /* StarStar  */
  YYSYMBOL_UNARY_PREC = 122,               /* UNARY_PREC  */
  YYSYMBOL_123_ = 123,                     /* '#'  */
  YYSYMBOL_124_ = 124,                     /* '('  */
  YYSYMBOL_125_ = 125,                     /* ')'  */
  YYSYMBOL_126_ = 126,                     /* ';'  */
  YYSYMBOL_127_ = 127,                     /* ','  */
  YYSYMBOL_128_ = 128,                     /* '='  */
  YYSYMBOL_129_ = 129,                     /* '{'  */
  YYSYMBOL_130_ = 130,                     /* '}'  */
  YYSYMBOL_131_ = 131,                     /* '.'  */
  YYSYMBOL_132_ = 132,                     /* '['  */
  YYSYMBOL_133_ = 133,                     /* ']'  */
  YYSYMBOL_134_ = 134,                     /* '@'  */
  YYSYMBOL_135_ = 135,                     /* '!'  */
  YYSYMBOL_136_ = 136,                     /* '~'  */
  YYSYMBOL_YYACCEPT = 137,                 /* $accept  */
  YYSYMBOL_Main = 138,                     /* Main  */
  YYSYMBOL_Mains = 139,                    /* Mains  */
  YYSYMBOL_MainItem = 140,                 /* MainItem  */
  YYSYMBOL_Module = 141,                   /* Module  */
  YYSYMBOL_Hparams = 142,                  /* Hparams  */
  YYSYMBOL_Header = 143,                   /* Header  */
  YYSYMBOL_Header_list = 144,              /* Header_list  */
  YYSYMBOL_Header_item = 145,              /* Header_item  */
  YYSYMBOL_Module_stuffs = 146,            /* Module_stuffs  */
  YYSYMBOL_Mstuff = 147,                   /* Mstuff  */
  YYSYMBOL_Define = 148,                   /* Define  */
  YYSYMBOL_Initial = 149,                  /* Initial  */
  YYSYMBOL_OneDef = 150,                   /* OneDef  */
  YYSYMBOL_ManyDefs = 151,                 /* ManyDefs  */
  YYSYMBOL_Definition = 152,               /* Definition  */
  YYSYMBOL_Assign = 153,                   /* Assign  */
  YYSYMBOL_StrengthDef = 154,              /* StrengthDef  */
  YYSYMBOL_Strength = 155,                 /* Strength  */
  YYSYMBOL_WidthInt = 156,                 /* WidthInt  */
  YYSYMBOL_Function = 157,                 /* Function  */
  YYSYMBOL_Task = 158,                     /* Task  */
  YYSYMBOL_Mem_defs = 159,                 /* Mem_defs  */
  YYSYMBOL_Mem_def = 160,                  /* Mem_def  */
  YYSYMBOL_Parameter = 161,                /* Parameter  */
  YYSYMBOL_Localparam = 162,               /* Localparam  */
  YYSYMBOL_Defparam = 163,                 /* Defparam  */
  YYSYMBOL_Pairs = 164,                    /* Pairs  */
  YYSYMBOL_Pair = 165,                     /* Pair  */
  YYSYMBOL_head_params = 166,              /* head_params  */
  YYSYMBOL_head_param = 167,               /* head_param  */
  YYSYMBOL_Instance = 168,                 /* Instance  */
  YYSYMBOL_Conns_list = 169,               /* Conns_list  */
  YYSYMBOL_Connection = 170,               /* Connection  */
  YYSYMBOL_AssignParams = 171,             /* AssignParams  */
  YYSYMBOL_Prms_list = 172,                /* Prms_list  */
  YYSYMBOL_PrmAssign = 173,                /* PrmAssign  */
  YYSYMBOL_InstParams = 174,               /* InstParams  */
  YYSYMBOL_Always = 175,                   /* Always  */
  YYSYMBOL_Generate = 176,                 /* Generate  */
  YYSYMBOL_GenStatements = 177,            /* GenStatements  */
  YYSYMBOL_GenStatement = 178,             /* GenStatement  */
  YYSYMBOL_GenFor_statement = 179,         /* GenFor_statement  */
  YYSYMBOL_When = 180,                     /* When  */
  YYSYMBOL_Or_coma = 181,                  /* Or_coma  */
  YYSYMBOL_When_items = 182,               /* When_items  */
  YYSYMBOL_When_item = 183,                /* When_item  */
  YYSYMBOL_Statement = 184,                /* Statement  */
  YYSYMBOL_pragma_stuffs = 185,            /* pragma_stuffs  */
  YYSYMBOL_pragma_item = 186,              /* pragma_item  */
  YYSYMBOL_Pragma = 187,                   /* Pragma  */
  YYSYMBOL_For_statement = 188,            /* For_statement  */
  YYSYMBOL_Repeat_statement = 189,         /* Repeat_statement  */
  YYSYMBOL_While_statement = 190,          /* While_statement  */
  YYSYMBOL_Soft_assigns = 191,             /* Soft_assigns  */
  YYSYMBOL_Soft_assign = 192,              /* Soft_assign  */
  YYSYMBOL_Cases = 193,                    /* Cases  */
  YYSYMBOL_GenCases = 194,                 /* GenCases  */
  YYSYMBOL_Case = 195,                     /* Case  */
  YYSYMBOL_GenCase = 196,                  /* GenCase  */
  YYSYMBOL_Default = 197,                  /* Default  */
  YYSYMBOL_GenDefault = 198,               /* GenDefault  */
  YYSYMBOL_Exprs = 199,                    /* Exprs  */
  YYSYMBOL_Statements = 200,               /* Statements  */
  YYSYMBOL_LSH = 201,                      /* LSH  */
  YYSYMBOL_Tokens_list = 202,              /* Tokens_list  */
  YYSYMBOL_Width = 203,                    /* Width  */
  YYSYMBOL_BusBit = 204,                   /* BusBit  */
  YYSYMBOL_ExtDir = 205,                   /* ExtDir  */
  YYSYMBOL_IntDir = 206,                   /* IntDir  */
  YYSYMBOL_CurlyList = 207,                /* CurlyList  */
  YYSYMBOL_CurlyItems = 208,               /* CurlyItems  */
  YYSYMBOL_CurlyItem = 209,                /* CurlyItem  */
  YYSYMBOL_Literal = 210,                  /* Literal  */
  YYSYMBOL_Expr = 211                      /* Expr  */
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
#define YYLAST   5414

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  137
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  75
/* YYNRULES -- Number of rules.  */
#define YYNRULES  373
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  850

/* YYMAXUTOK -- Last valid token kind.  */
#define YYMAXUTOK   365


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
       2,     2,     2,   135,     2,   123,     2,   120,   107,     2,
     124,   125,   118,   114,   127,   115,   131,   119,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,   104,   126,
     112,   128,   113,   103,   134,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,   132,     2,   133,   106,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   129,   105,   130,   136,     2,     2,     2,
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
      95,    96,    97,    98,    99,   100,   101,   102,   108,   109,
     110,   111,   116,   117,   121,   122
};

#if YYDEBUG
/* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_int16 yyrline[] =
{
       0,    45,    45,    46,    46,    47,    47,    49,    50,    51,
      53,    53,    54,    54,    54,    55,    55,    57,    57,    57,
      58,    59,    60,    61,    61,    61,    65,    65,    68,    69,
      70,    71,    72,    73,    74,    75,    76,    77,    78,    79,
      80,    81,    85,    85,    85,    85,    85,    86,    87,    87,
      88,    88,    90,    91,    92,    93,    94,    95,    96,    97,
      98,    99,   100,   101,   102,   103,   104,   105,   106,   107,
     111,   112,   113,   114,   117,   118,   118,   118,   118,   118,
     118,   118,   118,   119,   119,   121,   122,   123,   124,   125,
     126,   127,   128,   129,   132,   133,   134,   135,   138,   138,
     140,   141,   142,   143,   144,   145,   146,   147,   148,   149,
     150,   151,   152,   156,   157,   158,   159,   160,   162,   162,
     162,   163,   165,   165,   166,   168,   168,   170,   171,   172,
     173,   177,   178,   179,   180,   181,   182,   183,   184,   185,
     186,   187,   188,   189,   197,   197,   198,   198,   198,   198,
     200,   200,   200,   200,   201,   201,   202,   202,   203,   203,
     203,   203,   203,   203,   206,   206,   206,   206,   209,   211,
     211,   214,   215,   216,   217,   218,   219,   220,   221,   222,
     223,   224,   225,   226,   227,   228,   229,   230,   231,   236,
     241,   241,   241,   241,   242,   242,   243,   243,   244,   244,
     244,   249,   250,   251,   252,   253,   254,   255,   256,   257,
     258,   259,   260,   261,   262,   263,   264,   265,   266,   267,
     268,   269,   270,   271,   272,   273,   274,   275,   276,   277,
     278,   279,   280,   281,   282,   283,   284,   285,   286,   287,
     291,   291,   292,   292,   294,   297,   298,   300,   301,   302,
     302,   303,   304,   304,   305,   305,   306,   306,   307,   307,
     308,   308,   309,   309,   311,   311,   312,   312,   315,   315,
     315,   315,   315,   315,   317,   317,   319,   319,   319,   320,
     322,   322,   322,   322,   322,   322,   322,   322,   322,   322,
     322,   322,   324,   324,   324,   324,   324,   324,   324,   324,
     324,   324,   324,   324,   324,   326,   327,   327,   329,   330,
     331,   336,   337,   338,   339,   339,   339,   339,   339,   339,
     343,   344,   345,   346,   347,   348,   349,   349,   349,   349,
     349,   349,   350,   351,   352,   353,   354,   355,   356,   357,
     358,   359,   360,   361,   362,   363,   364,   365,   366,   367,
     368,   369,   370,   371,   372,   373,   374,   375,   376,   377,
     378,   379,   380,   381,   382,   383,   384,   385,   386,   387,
     388,   389,   390,   391
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
  "typedef", "'?'", "':'", "'|'", "'^'", "'&'", "shift_left",
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

#define YYPACT_NINF (-495)

#define yypact_value_is_default(Yyn) \
  ((Yyn) == YYPACT_NINF)

#define YYTABLE_NINF (-217)

#define yytable_value_is_error(Yyn) \
  0

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
static const yytype_int16 yypact[] =
{
      36,    42,   229,    86,    36,  -495,  -495,  -495,   223,    71,
    1703,  -495,  -495,  -495,   100,    62,  -495,   -31,  3256,    67,
    -495,   -28,  -495,  -495,  -495,  -495,  -495,  -495,  -495,   120,
    -495,  1703,  1703,  1703,  1703,  1703,  1703,  1703,  1703,  1318,
    1703,  1703,  -495,  5228,   105,  -495,   358,   321,   287,   181,
     -16,  -495,    29,  3352,    76,  -495,    16,   328,   365,  -495,
    -495,  -495,  -495,   313,  -495,  -495,  2540,    73,   347,    32,
      10,  2540,    33,   387,    38,  3736,  -495,  -495,  -495,  -495,
    2540,   253,   309,   393,  3352,  -495,  -495,  -495,  -495,  -495,
    -495,  -495,  -495,  -495,  -495,  -495,  -495,  -495,    11,    15,
     418,  1703,  1703,  -495,   271,  1703,  -495,  -495,  -495,  -495,
    -495,  -495,  -495,  4485,   299,    75,  -495,  2976,  -495,  -495,
    1703,  1703,  1703,  1703,  1703,  1703,  1703,  1703,  1703,  1703,
    1703,  1703,  1703,  1703,  1703,  1703,  1703,  1703,  1703,  1703,
    1703,  1703,  1703,  1703,  1703,  1703,   303,    14,   430,  -495,
     110,  -495,  -495,  -495,  -495,   442,  -495,  -495,  -495,  -495,
    -495,   335,   333,   345,   434,  1703,    47,   471,   153,    69,
    1703,   488,   271,    97,   462,    40,    12,   236,  -495,   376,
    -495,  -495,  -495,   370,   394,   158,    12,    11,   313,   313,
    1961,   416,  1703,   538,   425,   428,   444,  2540,   450,   454,
    2540,   577,  1703,  1703,   463,   596,  1703,    83,  2036,  -495,
    -495,  -495,  -495,  -495,    45,   486,  1703,   484,   340,  -495,
      10,   385,    10,   401,    10,   494,  -495,   154,  -495,   609,
     497,   201,   500,  -495,   -40,  -495,  3099,   503,   506,   507,
     313,  -495,  -495,  -495,  -495,  -495,  -495,  -495,  -495,  3448,
    -495,  -495,  -495,  -495,  2540,    77,  -495,  -495,   511,   313,
     132,  -495,   438,   633,    56,   634,   185,  5228,  2766,  -495,
    -495,  4550,  -495,  -495,  1318,  -495,  -495,  1004,  5294,   143,
     143,   143,   336,   336,  -495,   624,   624,   624,  5195,  5261,
     624,   819,   457,   457,   457,   336,   336,   298,   298,   143,
    -495,  -495,  -495,  1703,   512,   636,   514,  -495,    59,  -495,
    -495,  -495,   222,  -495,  5162,   232,    57,  -495,   776,  -495,
     519,  -495,  -495,  -495,   890,   270,    90,  -495,   271,  -495,
    -495,  -495,  1703,  -495,  -495,  -495,  -495,  -495,  -495,  -495,
    -495,   517,    12,   518,   520,  -495,    12,  1703,   313,  -495,
    1388,  -495,   522,   526,   313,   534,   536,  -495,   658,  -495,
    2099,  1703,  3734,   539,  1703,  1703,  1703,  -495,    46,  1703,
    2162,   540,  3132,  3771,  1703,   544,  1812,  -495,  -495,  -495,
     967,  -495,  -495,  1439,  1439,  1515,   273,  1703,  -495,   347,
     458,   347,  -495,   464,   347,  -495,   466,   347,   333,  1940,
     282,   659,   333,  1940,  1703,  -495,    38,   667,  3544,  1703,
    1703,    12,   547,  -495,  -495,  -495,   124,   313,  -495,   -49,
    1703,   548,  -495,   670,   320,   550,   132,   470,    60,  -495,
    -495,  1703,  1703,  1703,  1703,  -495,  -495,  -495,  1703,  5228,
    1703,   551,  1703,  -495,  -495,  -495,  -495,  -495,  -495,  -495,
    -495,  -495,  -495,  -495,   222,  -495,  -495,   673,   554,    58,
     284,  -495,   288,  1515,  -495,   677,   294,  -495,   302,   557,
     126,   560,  -495,  -495,   311,   462,   558,  1703,  1703,  -495,
    5228,  -495,   559,   315,  1703,  -495,   561,  -495,  -495,  2540,
    -495,  -495,  4587,  -495,  -495,  4652,  4689,  4754,    12,   472,
    4791,  -495,  -495,  1703,  -495,  4856,  -495,  -495,  -495,  1703,
    1703,   142,  -495,  5228,  1703,  3836,  1703,  3873,   338,   355,
     563,  5228,  -495,  -495,   477,  -495,   479,  -495,   481,   359,
      39,   680,    11,   313,   313,   313,  1940,  -495,  2225,   333,
    1940,   566,   369,  1940,   635,  5228,  -495,  3736,  -495,  4893,
    4958,   491,  -495,   313,   564,   567,  -495,   568,  5228,  -495,
     570,  -495,  1703,  -495,   168,  -495,   357,   496,   691,  5228,
    2804,  2871,  2909,  5228,  5228,  1703,  5228,  -495,  -495,  -495,
     122,  -495,   573,   569,   578,   378,   382,   579,  -495,   574,
    -495,  -495,   583,   396,   569,  -495,   585,  1703,  3938,  3975,
    -495,   586,  4040,  -495,  2288,  2540,  1565,  1703,  1703,   587,
    1703,  2540,  4077,  2540,  5228,  5228,  -495,  -495,  -495,   967,
    4142,  -495,  4179,  -495,   588,   591,  -495,  -495,  -495,  -495,
     592,   313,   177,   497,   497,   593,    64,   188,   594,   595,
    -495,  2351,  -495,   399,  1940,   665,   451,   599,   666,  -495,
    3640,  3736,  1649,  1703,   597,   313,   725,  -495,  4244,  -495,
     620,  -495,  -495,   372,   621,  -495,  -495,  -495,  5228,  1700,
     744,  -495,  -495,  -495,   623,   627,  1703,  -495,  -495,   628,
     423,  -495,  4281,  -495,  -495,  -495,  -495,  -495,   710,   652,
    1044,  -495,   705,   -48,  1128,  1183,  1703,  4346,  -495,  -495,
    -495,  -495,  -495,  -495,  -495,  -495,  1940,   638,  -495,   639,
     313,   497,   495,   164,   642,   754,   498,   643,  -495,  -495,
    -495,   644,   702,  -495,    11,   313,  1940,  1940,  -495,  -495,
     721,   672,  1267,  -495,   724,   -22,  4383,   769,   648,   653,
    -495,  -495,  -495,  -495,  -495,  4995,   649,  -495,  -495,  5060,
    -495,   657,  -495,  2540,  2414,  -495,  -495,   731,  -495,  2477,
    -495,   732,  -495,   733,  4448,    12,  1940,   730,  -495,  -495,
     663,   786,   671,   499,   674,  -495,  1940,  -495,   678,    64,
     191,   734,  1940,   738,  3736,  2634,  -495,  -495,   740,  -495,
    2730,    12,   679,   794,  -495,  -495,   682,  -495,  -495,  -495,
    -495,  -495,  -495,  -495,  -495,  -495,  -495,    12,   435,   749,
    -495,  -495,   684,  -495,  -495,  1940,   750,  -495,   685,  -495,
    -495,   752,  -495,  -495,  -495,  -495,  -495,  -495,  -495,   436,
    -495,   687,  1703,   456,  2540,  -495,  -495,   756,  -495,  -495,
    -495,  3736,  -495,  5097,  2540,  -495,  -495,  -495,  -495,  -495
};

/* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
   Performed when YYTABLE does not specify something else to do.  Zero
   means the default is an error.  */
static const yytype_int16 yydefact[] =
{
       0,     0,    42,     0,     2,     4,     5,     6,     0,     0,
      44,    43,     1,     3,     0,     0,    12,     0,     0,     0,
     321,   320,   326,   327,   328,   329,   330,   331,   323,   324,
     322,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   364,    45,     0,    23,   280,   281,   282,     0,
       0,    16,     0,    27,     0,     9,     0,   293,   294,   292,
     303,   304,   295,     0,   296,   297,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   300,   301,   302,    41,
       0,     0,     0,     0,    27,    39,    36,    28,    29,    37,
      38,    33,    34,    35,    30,    31,    32,    40,     0,     0,
       0,     0,     0,   332,   335,     0,   369,   371,   370,   366,
     368,   367,   365,     0,     0,     0,   307,   309,   372,   373,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    11,
       0,   126,   284,   291,   287,   283,   285,   290,   288,   286,
      14,     0,     0,    17,     0,     0,     0,     0,     0,     0,
       0,     0,   268,     0,     0,     0,     0,     0,   250,     0,
     273,   298,   299,   275,     0,   268,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   166,
     237,   234,   235,   236,     0,     0,     0,     0,     0,   123,
       0,     0,     0,     0,     0,     0,    47,     0,    84,     0,
      83,     0,     0,   243,     0,   241,     0,     0,     0,     0,
     300,   182,   174,   175,   176,   177,   178,   179,   181,     0,
     170,   180,   183,   165,     0,     0,     8,    26,     0,     0,
      48,    51,     0,     0,     0,     0,     0,   265,     0,   333,
     334,     0,   363,   310,     0,   305,   308,   348,   349,   354,
     353,   355,   357,   358,   347,   350,   351,   352,     0,   343,
     342,   344,   359,   360,   361,   345,   346,   337,   339,   356,
     338,   340,   341,     0,     0,     0,     0,    10,     0,   289,
      13,    15,     0,    19,     0,    18,     0,     7,     0,   133,
       0,   159,   161,   160,     0,     0,     0,   269,   272,   151,
     152,   153,     0,    75,    76,    77,    78,    79,    80,    81,
      82,     0,     0,     0,     0,    70,     0,     0,     0,    55,
       0,   233,     0,     0,     0,     0,     0,   202,     0,   267,
       0,     0,     0,     0,     0,     0,     0,   203,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   192,   191,   190,
       0,   219,   167,     0,     0,     0,     0,     0,   121,     0,
       0,     0,   113,     0,     0,   118,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   244,     0,     0,     0,     0,
       0,     0,     0,   168,   169,   164,     0,     0,    52,     0,
       0,     0,    56,     0,   275,     0,    48,     0,     0,    46,
     362,     0,     0,     0,     0,   279,   325,   306,     0,   130,
       0,     0,     0,   125,   311,   314,   315,   316,   317,   318,
     319,   313,   312,    24,     0,    20,    21,     0,     0,     0,
       0,   145,     0,     0,   163,     0,     0,   155,     0,     0,
       0,     0,   270,   271,     0,     0,     0,     0,     0,   249,
     251,   274,     0,     0,     0,   215,     0,   213,   214,     0,
     201,   266,     0,   212,   220,     0,     0,     0,     0,     0,
       0,   205,   221,     0,   217,     0,   239,   231,   232,     0,
       0,     0,   197,   200,     0,     0,     0,     0,     0,     0,
       0,   124,   122,   114,     0,   115,     0,   119,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    99,     0,     0,
       0,     0,     0,     0,     0,   242,   240,     0,   171,     0,
       0,     0,   173,     0,     0,     0,    53,     0,    49,    64,
      48,    50,     0,    65,     0,    57,    48,     0,     0,   264,
       0,     0,     0,   336,   128,     0,   127,    25,    22,   131,
       0,   146,     0,     0,     0,     0,     0,   157,   162,     0,
     158,   139,     0,     0,     0,   150,     0,     0,     0,     0,
     222,     0,     0,   216,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   198,   199,   194,   193,   195,     0,
       0,   208,     0,   206,     0,     0,   134,   117,   116,   120,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      98,     0,    86,     0,     0,     0,     0,     0,     0,    95,
       0,     0,     0,     0,     0,     0,     0,    54,     0,    60,
       0,    62,    58,     0,     0,   277,   278,   276,   129,     0,
       0,   136,   144,   138,     0,     0,     0,   154,   132,     0,
       0,    74,     0,    73,    71,   223,   238,   204,   210,     0,
       0,   253,     0,     0,     0,     0,     0,     0,   248,   218,
     247,   196,   209,   207,   137,   135,     0,     0,   107,     0,
       0,     0,   100,   275,     0,     0,   111,     0,   101,   102,
      85,     0,     0,    89,     0,     0,     0,     0,    94,   172,
     184,     0,     0,   255,     0,     0,     0,     0,     0,     0,
      66,    61,    63,    59,   148,     0,     0,   142,   143,     0,
     140,     0,    72,     0,     0,   224,   252,     0,   226,     0,
     227,     0,   229,     0,     0,     0,     0,     0,   110,   108,
       0,     0,     0,   103,     0,   112,     0,    88,     0,     0,
       0,     0,     0,     0,     0,     0,   186,   254,     0,   188,
       0,     0,     0,     0,    69,   147,     0,   156,   141,   211,
     261,   260,   225,   257,   256,   228,   230,     0,     0,     0,
      90,   109,     0,   104,   105,     0,     0,   100,     0,   111,
      87,     0,    96,   185,   263,   262,   187,   259,   258,     0,
      68,     0,     0,     0,     0,    91,   106,     0,    92,   103,
      97,     0,    67,     0,     0,   245,    93,   189,   149,   246
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -495,  -495,  -495,   811,  -495,  -495,   799,  -380,   656,   128,
    -495,   373,   186,  -410,  -250,   190,   192,  -495,   346,  -495,
    -495,  -495,  -391,  -494,   197,   199,   205,   -11,   431,  -495,
     521,   218,  -378,   242,  -164,  -495,   237,   728,   220,  -495,
    -231,  -246,  -495,    25,  -495,  -495,   209,   -25,  -495,   424,
     -18,  -495,  -495,  -495,  -358,  -338,    17,  -495,  -340,    99,
    -301,   101,   -26,  -196,   -20,   -89,   447,   -15,   -14,  -495,
     111,  -495,   562,   380,    -8
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
       0,     3,     4,     5,     6,    17,    18,    50,    51,    83,
      84,    85,   241,   261,   262,   242,   243,   175,   341,   229,
      89,    90,   536,   537,   244,   245,   246,   218,   219,   150,
     151,   247,   460,   461,   176,   466,   467,   171,   248,    96,
     249,   250,   251,   225,   619,   511,   512,   359,   234,   235,
     210,   211,   212,   213,   177,   178,   690,   732,   691,   733,
     692,   734,   693,   360,   214,   184,   327,   328,    98,    99,
      42,   115,   116,   453,   267
};

/* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule whose
   number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
      97,    52,    43,   414,   370,   408,   104,   518,   479,   258,
     499,   342,   543,   561,   427,   217,   183,   172,   529,   304,
     260,   172,   542,   106,   107,   108,   109,   110,   111,   112,
     113,   117,   118,   119,   163,    97,   179,   217,   227,     1,
     405,   209,   640,   232,   183,   172,   226,     8,   220,   640,
     164,   172,   315,   551,   228,   253,   759,   252,   221,   223,
     631,   426,   456,   580,   146,   566,    97,    45,   498,   713,
      46,    47,    48,   321,   322,   266,    19,   556,   215,   431,
     383,   168,   790,   165,   233,   585,    12,   406,   377,   270,
     416,   208,   593,    15,   268,    16,   101,   271,   353,   355,
     356,   329,   330,     2,   102,   431,   254,   147,   148,   161,
     146,   162,   277,   278,   279,   280,   281,   282,   283,   284,
     285,   286,   287,   288,   289,   290,   291,   292,   293,   294,
     295,   296,   297,   298,   299,   300,   301,   302,   169,   173,
     174,    39,   165,   165,   325,    39,   165,   165,    52,   644,
     640,   412,   323,   147,   148,   343,   344,   314,   664,   643,
     609,   165,   414,   173,   165,   165,   352,   180,   378,    39,
     419,   165,   367,   384,   425,    39,   581,   180,   567,   165,
     331,   167,   180,   382,   362,   616,   100,    49,   165,   165,
     386,   180,   165,   324,   372,   373,   165,   216,   376,   169,
     170,   379,   274,   538,    86,   275,   417,   380,    87,   390,
      88,   393,   257,   396,   470,    91,   680,    92,   252,   514,
     516,   332,   165,    93,    44,   273,   444,   127,   276,   415,
     149,   252,   640,     9,    10,   307,    94,   308,    95,    86,
     445,   446,   447,    87,   105,    88,   669,   448,   449,   450,
      91,   592,    92,   553,   670,   726,   165,   459,    93,   481,
     420,   143,   144,   145,   165,   486,   117,   617,   451,   618,
      86,    94,   640,    95,    87,    11,    88,   318,   398,   319,
     399,    91,   350,    92,   351,   165,   180,   180,   640,    93,
     102,   348,   462,   604,   659,   439,   165,   180,   468,   159,
     165,   180,    94,   708,    95,   452,   474,   160,   180,   165,
     430,   180,   431,   473,   716,   766,   650,   819,   183,   180,
     165,   640,   476,   165,   483,   402,   179,   403,   555,   122,
     123,   124,   155,   156,   157,   491,   782,   158,    45,   480,
     641,    46,    47,    48,   181,   491,    14,    15,   179,    16,
     756,   508,   217,   492,   756,   756,   495,   496,   497,   519,
     454,   500,   345,   346,   165,   180,   505,   122,   123,   124,
     152,   153,   513,     7,   154,   515,   517,     7,   544,   521,
     524,   182,   127,   526,    52,   815,   528,   207,    52,   757,
     252,   179,   231,   761,   763,   469,   545,   431,   520,   256,
     431,   549,   550,   102,   414,   730,   539,   808,   540,   582,
     255,   583,   558,   584,   142,   431,   143,   144,   145,   588,
     127,   589,   265,   569,   570,   571,   572,   590,    39,   431,
     573,   303,   574,   829,   576,   306,   595,   586,   431,   313,
     601,   632,   431,   635,   637,   638,   639,   348,   562,   833,
     140,   141,   142,   180,   143,   144,   145,   180,   309,   530,
     531,   310,   724,   624,   654,   583,   388,   389,   103,   598,
     599,   180,   725,   312,   534,   535,   602,   317,   179,   180,
     625,   180,   431,   661,   630,   420,   162,   180,   122,   123,
     124,   125,   126,   326,   647,   612,   162,   348,   742,   166,
     420,   614,   615,   674,   347,   583,   620,   675,   622,   431,
     180,   392,   389,   491,   180,   645,   222,   224,   648,   230,
     349,   679,   180,   583,   721,    52,   162,   395,   389,   252,
     333,   334,   335,   336,   337,   338,   339,   340,   823,   825,
     361,   127,   707,   363,   828,   259,   264,   714,   751,   364,
     583,   269,   365,  -215,   658,  -215,  -213,  -216,  -213,  -216,
     834,   841,   346,   346,   422,   423,   738,   668,   366,   138,
     139,   140,   141,   142,   368,   143,   144,   145,   369,   491,
     688,   844,   371,   346,   523,   389,   698,   374,   700,   682,
     525,   389,   527,   389,   305,   847,   565,   423,   610,   346,
     180,   375,   697,   627,   389,   628,   389,   629,   389,   180,
     385,   513,   387,   316,   400,   320,   491,   653,   346,   722,
     381,   770,   662,   423,   694,   695,   735,   409,   404,   165,
     410,   411,   252,   252,   354,   778,   780,   418,   424,   429,
     440,   441,   442,   463,   475,   736,   477,   180,   478,   180,
     484,   180,   485,   120,   180,   122,   123,   124,   125,   126,
     487,   745,   488,   489,   541,   494,   502,   391,   749,   394,
     506,   397,   547,   552,   559,   560,   563,   401,   578,   575,
     579,   767,   587,   591,   594,   600,   597,   603,   764,   626,
     818,   634,   646,   655,   657,   649,   663,   656,   420,   671,
     459,   781,   783,   676,   673,   465,   735,   421,   127,   678,
     681,   428,   685,   696,   704,   180,   180,   705,   706,   712,
     718,   719,   180,   723,   180,   727,   728,   737,   799,   801,
     739,   134,   135,   136,   804,   137,   138,   139,   140,   141,
     142,   809,   143,   144,   145,   179,   741,   743,   746,   747,
     753,   816,   180,   748,   750,   180,   754,   821,   758,   774,
     777,   784,   455,   457,   768,   769,   252,   252,   773,   775,
     776,   179,   252,   471,   792,   472,   785,   789,   793,   794,
      20,    21,   796,   798,   802,   805,   806,   179,   810,   811,
     837,   812,   820,   826,    22,    23,    24,   813,   822,   831,
     814,    25,    26,    27,   817,   830,   832,   835,   838,   845,
     836,   839,   840,   842,   846,    13,    53,   180,   311,   849,
     522,   596,    28,   252,   843,   672,   677,   263,   701,   443,
     546,   787,     0,   788,   577,     0,   437,   180,   180,     0,
       0,     0,     0,    29,     0,     0,     0,     0,   120,     0,
     122,   123,   124,   125,   126,     0,     0,     0,     0,    30,
       0,     0,     0,   554,   180,   180,   557,    31,    32,    33,
     180,     0,     0,   564,     0,   568,   180,   180,     0,     0,
       0,    34,    35,    36,     0,     0,     0,   180,     0,     0,
       0,    37,     0,   180,    20,    21,     0,     0,     0,     0,
      38,   458,   180,   127,     0,    39,     0,   459,    22,    23,
      24,    40,    41,     0,     0,    25,    26,    27,   180,     0,
       0,     0,     0,     0,     0,     0,   180,   135,   136,     0,
     137,   138,   139,   140,   141,   142,    28,   143,   144,   145,
       0,     0,     0,     0,     0,   180,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   180,     0,    29,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    20,    21,    30,     0,     0,     0,   633,     0,   636,
       0,    31,    32,    33,     0,    22,    23,    24,     0,     0,
       0,     0,    25,    26,    27,    34,    35,    36,     0,     0,
       0,     0,     0,     0,     0,    37,     0,     0,   509,   510,
       0,   660,     0,    28,    38,   464,     0,     0,     0,    39,
       0,   465,     0,     0,     0,    40,    41,     0,     0,     0,
       0,     0,     0,     0,    29,   122,   123,   124,   125,   126,
       0,     0,     0,     0,     0,     0,     0,     0,    20,    21,
      30,     0,     0,     0,     0,     0,     0,     0,    31,    32,
      33,     0,    22,    23,    24,     0,     0,     0,     0,    25,
      26,    27,    34,    35,    36,     0,     0,     0,     0,   709,
     710,   711,    37,   715,   717,     0,     0,     0,   127,     0,
      28,    38,     0,     0,     0,     0,    39,   755,   689,     0,
       0,     0,    40,    41,     0,     0,     0,     0,     0,     0,
       0,    29,   135,   136,     0,   137,   138,   139,   140,   141,
     142,     0,   143,   144,   145,     0,     0,    30,     0,     0,
       0,     0,    20,    21,     0,    31,    32,    33,     0,     0,
       0,     0,     0,     0,     0,     0,    22,    23,    24,    34,
      35,    36,     0,    25,    26,    27,     0,     0,   771,    37,
     772,     0,     0,     0,     0,     0,     0,     0,    38,     0,
       0,   779,     0,    39,    28,     0,     0,     0,     0,    40,
      41,   760,   689,     0,     0,     0,     0,    20,    21,     0,
       0,     0,     0,     0,     0,    29,     0,     0,     0,     0,
       0,    22,    23,    24,     0,     0,     0,     0,    25,    26,
      27,    30,     0,     0,     0,     0,     0,     0,     0,    31,
      32,    33,     0,     0,     0,     0,   715,   717,     0,    28,
       0,     0,     0,    34,    35,    36,   762,   689,     0,     0,
       0,     0,     0,    37,     0,     0,     0,     0,     0,     0,
      29,     0,    38,     0,     0,     0,     0,    39,     0,     0,
       0,     0,     0,    40,    41,     0,    30,     0,     0,     0,
       0,    20,    21,     0,    31,    32,    33,     0,     0,     0,
       0,     0,     0,     0,     0,    22,    23,    24,    34,    35,
      36,     0,    25,    26,    27,     0,     0,     0,    37,     0,
       0,     0,     0,     0,     0,     0,     0,    38,     0,     0,
       0,     0,    39,    28,     0,     0,     0,     0,    40,    41,
     786,   731,    20,    21,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    29,     0,    22,    23,    24,     0,
       0,     0,     0,    25,    26,    27,     0,     0,     0,     0,
      30,     0,     0,     0,     0,     0,     0,     0,    31,    32,
      33,     0,     0,     0,    28,     0,     0,     0,     0,     0,
       0,     0,    34,    35,    36,     0,     0,     0,     0,     0,
       0,     0,    37,     0,     0,    29,     0,     0,     0,     0,
       0,    38,    20,    21,     0,     0,    39,     0,     0,     0,
       0,    30,    40,    41,     0,     0,    22,    23,    24,    31,
      32,    33,     0,    25,    26,    27,     0,     0,     0,     0,
       0,     0,     0,    34,    35,    36,   114,     0,     0,     0,
       0,     0,     0,    37,    28,     0,     0,     0,     0,     0,
       0,     0,    38,    20,    21,     0,     0,    39,     0,     0,
       0,     0,     0,    40,    41,    29,     0,    22,    23,    24,
       0,     0,     0,     0,    25,    26,    27,     0,     0,     0,
       0,    30,     0,     0,     0,     0,     0,     0,     0,    31,
      32,    33,     0,     0,     0,    28,     0,     0,     0,     0,
       0,     0,     0,    34,    35,    36,     0,     0,     0,     0,
       0,     0,     0,    37,     0,     0,    29,     0,     0,     0,
       0,     0,    38,   482,     0,     0,     0,    39,     0,    20,
      21,     0,    30,    40,    41,     0,     0,     0,     0,     0,
      31,    32,    33,    22,    23,    24,     0,     0,     0,     0,
      25,    26,    27,     0,    34,    35,    36,     0,     0,     0,
       0,     0,     0,     0,    37,     0,     0,     0,     0,     0,
       0,    28,   173,    38,     0,     0,     0,     0,    39,    20,
      21,     0,     0,     0,    40,    41,     0,     0,     0,     0,
       0,     0,    29,    22,    23,    24,     0,     0,     0,     0,
      25,    26,    27,     0,     0,     0,     0,     0,    30,     0,
       0,     0,     0,     0,     0,     0,    31,    32,    33,     0,
       0,    28,     0,     0,     0,     0,     0,     0,     0,   689,
      34,    35,    36,     0,     0,     0,     0,     0,     0,     0,
      37,     0,    29,     0,     0,     0,     0,     0,     0,    38,
       0,     0,     0,     0,    39,     0,   459,     0,    30,     0,
      40,    41,     0,    20,    21,     0,    31,    32,    33,     0,
       0,     0,     0,     0,     0,     0,     0,    22,    23,    24,
      34,    35,    36,     0,    25,    26,    27,     0,     0,     0,
      37,     0,     0,     0,     0,     0,     0,     0,     0,    38,
       0,     0,     0,     0,    39,    28,     0,     0,     0,     0,
      40,    41,     0,   731,    20,    21,     0,    20,    21,     0,
       0,     0,     0,     0,     0,     0,    29,     0,    22,    23,
      24,    22,    23,    24,     0,    25,    26,    27,    25,    26,
      27,     0,    30,     0,     0,     0,     0,     0,     0,     0,
      31,    32,    33,     0,     0,     0,    28,     0,     0,    28,
       0,     0,     0,     0,    34,    35,    36,     0,     0,     0,
       0,     0,     0,     0,    37,     0,     0,    29,     0,     0,
      29,     0,     0,    38,     0,     0,     0,     0,    39,     0,
       0,     0,     0,    30,    40,    41,    30,     0,     0,     0,
       0,    31,    32,    33,    31,    32,    33,     0,     0,     0,
       0,     0,     0,     0,     0,    34,    35,    36,    34,    35,
      36,     0,     0,     0,     0,    37,     0,   185,    37,   186,
       0,     0,     0,   187,    38,   744,     0,    38,     0,    39,
       0,     0,    39,   188,   189,    40,    41,     0,    40,    41,
       0,   120,   121,   122,   123,   124,   125,   126,     0,   190,
       0,   191,     0,     0,     0,     0,   192,   193,     0,     0,
       0,     0,   194,   195,   196,     0,     0,     0,   197,     0,
       0,     0,     0,   198,   199,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   200,     0,
     201,    74,     0,     0,     0,     0,   127,     0,     0,     0,
       0,   202,   203,   128,   129,   130,   204,     0,     0,     0,
     205,     0,     0,     0,     0,   131,     0,   132,   133,   134,
     135,   136,     0,   137,   138,   139,   140,   141,   142,     0,
     143,   144,   145,     0,     0,   206,     0,     0,   507,     0,
       0,    39,     0,     0,     0,   185,   207,   186,   530,   531,
       0,   532,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   533,   189,   534,   535,     0,   185,     0,   186,     0,
       0,     0,   187,     0,     0,     0,     0,   190,     0,   191,
       0,     0,   188,   189,   192,   193,     0,     0,     0,     0,
     194,   195,   196,     0,     0,     0,   197,     0,   190,   357,
     191,   198,   199,     0,     0,   192,   193,     0,     0,     0,
       0,   194,   195,   196,     0,     0,   200,   197,   201,    74,
       0,     0,   198,   199,     0,     0,     0,     0,     0,   202,
     203,     0,     0,     0,   204,     0,     0,   200,   205,   201,
      74,   185,     0,   186,     0,     0,     0,   187,     0,     0,
     202,   203,     0,     0,     0,   204,     0,   188,   189,   205,
       0,     0,     0,   206,     0,   358,     0,     0,     0,    39,
       0,     0,     0,   190,   207,   191,     0,     0,     0,     0,
     192,   193,     0,     0,   206,     0,   194,   195,   196,     0,
      39,     0,   197,     0,     0,   207,     0,   198,   199,     0,
       0,     0,     0,     0,   185,     0,   186,     0,     0,     0,
     187,     0,   200,     0,   201,    74,     0,     0,     0,     0,
     188,   189,     0,     0,     0,   202,   203,     0,     0,     0,
     204,     0,     0,     0,   205,     0,   190,   490,   191,     0,
       0,     0,     0,   192,   193,     0,     0,     0,     0,   194,
     195,   196,     0,     0,     0,   197,     0,     0,     0,   206,
     198,   199,   381,     0,     0,    39,     0,   185,     0,   186,
     207,     0,     0,   187,     0,   200,     0,   201,    74,     0,
       0,     0,     0,   188,   189,     0,     0,     0,   202,   203,
       0,     0,     0,   204,     0,     0,     0,   205,     0,   190,
       0,   191,     0,     0,     0,     0,   192,   193,     0,     0,
       0,     0,   194,   195,   196,     0,     0,     0,   197,     0,
       0,     0,   206,   198,   199,     0,     0,     0,    39,     0,
     185,     0,   186,   207,     0,     0,   187,     0,   200,   501,
     201,    74,     0,     0,     0,     0,   188,   189,     0,     0,
       0,   202,   203,     0,     0,     0,   204,     0,     0,     0,
     205,     0,   190,     0,   191,     0,     0,     0,     0,   192,
     193,     0,     0,     0,     0,   194,   195,   196,     0,     0,
       0,   197,     0,   642,     0,   206,   198,   199,     0,     0,
       0,    39,     0,   185,     0,   186,   207,     0,     0,   187,
       0,   200,     0,   201,    74,     0,     0,     0,     0,   188,
     189,     0,     0,     0,   202,   203,     0,     0,     0,   204,
       0,     0,     0,   205,     0,   190,   687,   191,     0,     0,
       0,     0,   192,   193,     0,     0,     0,     0,   194,   195,
     196,     0,     0,     0,   197,     0,     0,     0,   206,   198,
     199,     0,     0,     0,    39,     0,   185,     0,   186,   207,
       0,     0,   187,     0,   200,     0,   201,    74,     0,     0,
       0,     0,   188,   189,     0,     0,     0,   202,   203,     0,
       0,     0,   204,     0,     0,     0,   205,     0,   190,     0,
     191,     0,     0,     0,     0,   192,   193,     0,     0,     0,
       0,   194,   195,   196,     0,     0,     0,   197,     0,   720,
       0,   206,   198,   199,     0,     0,     0,    39,     0,   185,
       0,   186,   207,     0,     0,   187,     0,   200,     0,   201,
      74,     0,     0,     0,     0,   188,   189,     0,     0,     0,
     202,   203,     0,     0,     0,   204,     0,     0,     0,   205,
       0,   190,     0,   191,     0,     0,     0,     0,   192,   193,
       0,     0,     0,     0,   194,   195,   196,     0,     0,     0,
     197,     0,     0,     0,   206,   198,   199,     0,     0,     0,
      39,     0,   185,     0,   186,   207,     0,     0,   187,     0,
     200,     0,   201,    74,     0,     0,     0,     0,   188,   189,
       0,     0,     0,   202,   203,     0,     0,     0,   204,     0,
       0,     0,   205,     0,   190,     0,   191,     0,     0,     0,
       0,   192,   193,     0,     0,     0,     0,   194,   195,   196,
       0,     0,     0,   197,     0,     0,     0,   206,   198,   199,
     800,     0,     0,    39,     0,   185,     0,   186,   207,     0,
       0,   187,     0,   200,     0,   201,    74,     0,     0,     0,
       0,   188,   189,     0,     0,     0,   202,   203,     0,     0,
       0,   204,     0,     0,     0,   205,     0,   190,     0,   191,
       0,     0,     0,     0,   192,   193,     0,     0,     0,     0,
     194,   195,   196,     0,     0,     0,   197,     0,     0,     0,
     206,   198,   199,   803,     0,     0,    39,     0,     0,     0,
       0,   207,     0,     0,     0,     0,   200,     0,   201,    74,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   202,
     203,     0,     0,     0,   204,     0,     0,     0,   205,    54,
       0,    56,    46,    47,    48,    57,    58,    59,    60,    61,
      62,    63,     0,     0,     0,    64,     0,    65,     0,     0,
       0,     0,     0,   206,     0,     0,     0,     0,     0,    39,
      66,   236,     0,   237,   207,     0,     0,    67,     0,     0,
       0,    68,    69,    70,   238,     0,     0,     0,     0,    71,
       0,     0,     0,     0,     0,   239,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
       0,     0,   240,     0,     0,     0,     0,     0,     0,    77,
      78,     0,     0,    80,    81,    54,    82,    56,    46,    47,
      48,    57,    58,    59,    60,    61,    62,    63,     0,     0,
       0,    64,     0,    65,     0,     0,     0,     0,     0,     0,
     824,     0,     0,     0,     0,     0,    66,   236,     0,   237,
       0,     0,     0,    67,     0,     0,     0,    68,    69,    70,
     238,     0,     0,     0,     0,    71,     0,     0,     0,     0,
       0,   239,     0,     0,     0,   120,   121,   122,   123,   124,
     125,   126,     0,     0,     0,     0,     0,     0,     0,    74,
       0,     0,     0,     0,     0,     0,     0,     0,   240,     0,
       0,     0,     0,     0,     0,    77,    78,     0,     0,    80,
      81,     0,    82,   120,   121,   122,   123,   124,   125,   126,
       0,     0,     0,     0,     0,     0,     0,   432,   433,     0,
     127,     0,     0,     0,     0,     0,   827,   128,   129,   130,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   131,
     434,   132,   133,   134,   135,   136,     0,   137,   138,   139,
     140,   141,   142,     0,   143,   144,   145,     0,   127,     0,
       0,     0,     0,     0,     0,   128,   129,   130,     0,   435,
     120,   121,   122,   123,   124,   125,   126,   131,     0,   132,
     133,   134,   135,   136,     0,   137,   138,   139,   140,   141,
     142,     0,   143,   144,   145,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   665,   120,   121,
     122,   123,   124,   125,   126,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   127,     0,     0,     0,     0,
       0,     0,   128,   129,   130,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   131,     0,   132,   133,   134,   135,
     136,     0,   137,   138,   139,   140,   141,   142,     0,   143,
     144,   145,     0,   127,     0,     0,     0,     0,     0,     0,
     128,   129,   130,     0,   666,   120,   121,   122,   123,   124,
     125,   126,   131,     0,   132,   133,   134,   135,   136,     0,
     137,   138,   139,   140,   141,   142,     0,   143,   144,   145,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   667,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     127,     0,     0,     0,     0,     0,     0,   128,   129,   130,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   131,
       0,   132,   133,   134,   135,   136,     0,   137,   138,   139,
     140,   141,   142,     0,   143,   144,   145,     0,     0,     0,
       0,     0,     0,     0,    54,    39,    56,    46,    47,    48,
      57,    58,    59,    60,    61,    62,    63,     0,     0,     0,
      64,     0,    65,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    66,   236,     0,   237,     0,
       0,     0,    67,     0,     0,     0,    68,    69,    70,   238,
       0,     0,     0,     0,    71,     0,     0,     0,     0,     0,
     239,   120,   121,   122,   123,   124,   125,   126,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,     0,     0,   240,     0,     0,
       0,     0,     0,     0,    77,    78,     0,     0,    80,    81,
       0,    82,     0,   407,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   127,     0,     0,     0,
       0,     0,     0,   128,   129,   130,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   131,     0,   132,   133,   134,
     135,   136,     0,   137,   138,   139,   140,   141,   142,     0,
     143,   144,   145,     0,     0,     0,     0,     0,     0,     0,
     503,    54,    55,    56,    46,    47,    48,    57,    58,    59,
      60,    61,    62,    63,     0,     0,     0,    64,     0,    65,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    66,     0,     0,     0,     0,     0,     0,    67,
       0,     0,     0,    68,    69,    70,     0,     0,     0,     0,
       0,    71,     0,    72,     0,    73,     0,     0,     0,     0,
       0,     0,     0,     2,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    74,     0,     0,     0,     0,
       0,     0,    75,     0,    76,     0,     0,     0,     0,     0,
       0,    77,    78,    79,     0,    80,    81,    54,    82,    56,
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
       0,     0,     0,     0,    66,   236,     0,   237,     0,     0,
       0,    67,     0,     0,     0,    68,    69,    70,   238,     0,
       0,     0,     0,    71,     0,     0,     0,     0,     0,   239,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    74,     0,     0,
       0,     0,     0,     0,     0,   413,   240,     0,     0,     0,
       0,     0,     0,    77,    78,     0,     0,    80,    81,    54,
      82,    56,    46,    47,    48,    57,    58,    59,    60,    61,
      62,    63,     0,     0,     0,    64,     0,    65,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      66,   236,   548,   237,     0,     0,     0,    67,     0,     0,
       0,    68,    69,    70,   238,     0,     0,     0,     0,    71,
       0,     0,     0,     0,     0,   239,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
       0,     0,   240,     0,     0,     0,     0,     0,     0,    77,
      78,     0,     0,    80,    81,    54,    82,    56,    46,    47,
      48,    57,    58,    59,    60,    61,    62,    63,     0,     0,
       0,    64,     0,    65,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    66,   236,   729,   237,
       0,     0,     0,    67,     0,     0,     0,    68,    69,    70,
     238,     0,     0,     0,     0,    71,     0,     0,     0,     0,
       0,   239,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    74,
       0,     0,     0,     0,     0,     0,     0,     0,   240,     0,
       0,     0,     0,     0,     0,    77,    78,     0,     0,    80,
      81,    54,    82,    56,    46,    47,    48,    57,    58,    59,
      60,    61,    62,    63,     0,     0,     0,    64,     0,    65,
       0,     0,     0,   120,   121,   122,   123,   124,   125,   126,
       0,     0,    66,   236,     0,   237,     0,     0,     0,    67,
       0,     0,     0,    68,    69,    70,   238,     0,     0,     0,
       0,    71,     0,     0,     0,     0,     0,   239,     0,     0,
     120,   121,   122,   123,   124,   125,   126,     0,     0,     0,
       0,     0,     0,     0,     0,    74,     0,     0,   127,     0,
       0,     0,     0,     0,   240,   128,   129,   130,     0,     0,
       0,    77,    78,     0,     0,    80,    81,   131,    82,   132,
     133,   134,   135,   136,     0,   137,   138,   139,   140,   141,
     142,     0,   143,   144,   145,   127,     0,     0,     0,     0,
     493,     0,   128,   129,   130,   120,   121,   122,   123,   124,
     125,   126,     0,     0,   131,     0,   132,   133,   134,   135,
     136,     0,   137,   138,   139,   140,   141,   142,     0,   143,
     144,   145,     0,     0,     0,     0,     0,   504,     0,     0,
       0,     0,   120,   121,   122,   123,   124,   125,   126,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     127,     0,     0,     0,     0,     0,     0,   128,   129,   130,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   131,
       0,   132,   133,   134,   135,   136,     0,   137,   138,   139,
     140,   141,   142,     0,   143,   144,   145,   127,     0,     0,
       0,     0,   621,     0,   128,   129,   130,   120,   121,   122,
     123,   124,   125,   126,     0,     0,   131,     0,   132,   133,
     134,   135,   136,     0,   137,   138,   139,   140,   141,   142,
       0,   143,   144,   145,     0,     0,     0,     0,     0,   623,
       0,     0,     0,     0,   120,   121,   122,   123,   124,   125,
     126,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   127,     0,     0,     0,     0,     0,     0,   128,
     129,   130,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   131,     0,   132,   133,   134,   135,   136,     0,   137,
     138,   139,   140,   141,   142,     0,   143,   144,   145,   127,
       0,     0,     0,     0,   683,     0,   128,   129,   130,   120,
     121,   122,   123,   124,   125,   126,     0,     0,   131,     0,
     132,   133,   134,   135,   136,     0,   137,   138,   139,   140,
     141,   142,     0,   143,   144,   145,     0,     0,     0,     0,
       0,   684,     0,     0,     0,     0,   120,   121,   122,   123,
     124,   125,   126,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   127,     0,     0,     0,     0,     0,
       0,   128,   129,   130,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   131,     0,   132,   133,   134,   135,   136,
       0,   137,   138,   139,   140,   141,   142,     0,   143,   144,
     145,   127,     0,     0,     0,     0,   686,     0,   128,   129,
     130,   120,   121,   122,   123,   124,   125,   126,     0,     0,
     131,     0,   132,   133,   134,   135,   136,     0,   137,   138,
     139,   140,   141,   142,     0,   143,   144,   145,     0,     0,
       0,     0,     0,   699,     0,     0,     0,     0,   120,   121,
     122,   123,   124,   125,   126,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   127,     0,     0,     0,
       0,     0,     0,   128,   129,   130,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   131,     0,   132,   133,   134,
     135,   136,     0,   137,   138,   139,   140,   141,   142,     0,
     143,   144,   145,   127,     0,     0,     0,     0,   702,     0,
     128,   129,   130,   120,   121,   122,   123,   124,   125,   126,
       0,     0,   131,     0,   132,   133,   134,   135,   136,     0,
     137,   138,   139,   140,   141,   142,     0,   143,   144,   145,
       0,     0,     0,     0,     0,   703,     0,     0,     0,     0,
     120,   121,   122,   123,   124,   125,   126,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   127,     0,
       0,     0,     0,     0,     0,   128,   129,   130,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   131,     0,   132,
     133,   134,   135,   136,     0,   137,   138,   139,   140,   141,
     142,     0,   143,   144,   145,   127,     0,     0,     0,     0,
     740,     0,   128,   129,   130,   120,   121,   122,   123,   124,
     125,   126,     0,     0,   131,     0,   132,   133,   134,   135,
     136,     0,   137,   138,   139,   140,   141,   142,     0,   143,
     144,   145,     0,     0,     0,     0,     0,   752,     0,     0,
       0,     0,   120,   121,   122,   123,   124,   125,   126,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     127,     0,     0,     0,     0,     0,     0,   128,   129,   130,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   131,
       0,   132,   133,   134,   135,   136,     0,   137,   138,   139,
     140,   141,   142,     0,   143,   144,   145,   127,     0,     0,
       0,     0,   765,     0,   128,   129,   130,   120,   121,   122,
     123,   124,   125,   126,     0,     0,   131,     0,   132,   133,
     134,   135,   136,     0,   137,   138,   139,   140,   141,   142,
       0,   143,   144,   145,     0,     0,     0,     0,     0,   791,
       0,     0,     0,     0,   120,   121,   122,   123,   124,   125,
     126,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   127,     0,     0,     0,     0,     0,     0,   128,
     129,   130,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   131,     0,   132,   133,   134,   135,   136,     0,   137,
     138,   139,   140,   141,   142,     0,   143,   144,   145,   127,
       0,     0,     0,     0,   807,     0,   128,   129,   130,   120,
     121,   122,   123,   124,   125,   126,     0,     0,   131,     0,
     132,   133,   134,   135,   136,     0,   137,   138,   139,   140,
     141,   142,     0,   143,   144,   145,     0,     0,     0,     0,
     272,     0,     0,     0,     0,     0,   120,   121,   122,   123,
     124,   125,   126,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   127,     0,     0,     0,     0,     0,
       0,   128,   129,   130,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   131,     0,   132,   133,   134,   135,   136,
       0,   137,   138,   139,   140,   141,   142,     0,   143,   144,
     145,   127,     0,     0,     0,   436,     0,     0,   128,   129,
     130,   120,   121,   122,   123,   124,   125,   126,     0,     0,
     131,     0,   132,   133,   134,   135,   136,     0,   137,   138,
     139,   140,   141,   142,     0,   143,   144,   145,     0,     0,
       0,     0,   605,     0,     0,     0,     0,     0,   120,   121,
     122,   123,   124,   125,   126,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   127,     0,     0,     0,
       0,     0,     0,   128,   129,   130,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   131,     0,   132,   133,   134,
     135,   136,     0,   137,   138,   139,   140,   141,   142,     0,
     143,   144,   145,   127,     0,     0,     0,   606,     0,     0,
     128,   129,   130,   120,   121,   122,   123,   124,   125,   126,
       0,     0,   131,     0,   132,   133,   134,   135,   136,     0,
     137,   138,   139,   140,   141,   142,     0,   143,   144,   145,
       0,     0,     0,     0,   607,     0,     0,     0,     0,     0,
     120,   121,   122,   123,   124,   125,   126,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   127,     0,
       0,     0,     0,     0,     0,   128,   129,   130,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   131,     0,   132,
     133,   134,   135,   136,     0,   137,   138,   139,   140,   141,
     142,     0,   143,   144,   145,   127,     0,     0,     0,   608,
       0,     0,   128,   129,   130,   120,   121,   122,   123,   124,
     125,   126,     0,     0,   131,     0,   132,   133,   134,   135,
     136,     0,   137,   138,   139,   140,   141,   142,     0,   143,
     144,   145,     0,     0,     0,     0,   611,     0,     0,     0,
       0,     0,   120,   121,   122,   123,   124,   125,   126,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     127,     0,     0,     0,     0,     0,     0,   128,   129,   130,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   131,
       0,   132,   133,   134,   135,   136,     0,   137,   138,   139,
     140,   141,   142,     0,   143,   144,   145,   127,     0,     0,
       0,   613,     0,     0,   128,   129,   130,   120,   121,   122,
     123,   124,   125,   126,     0,     0,   131,     0,   132,   133,
     134,   135,   136,     0,   137,   138,   139,   140,   141,   142,
       0,   143,   144,   145,     0,     0,     0,     0,   651,     0,
       0,     0,     0,     0,   120,   121,   122,   123,   124,   125,
     126,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   127,     0,     0,     0,     0,     0,     0,   128,
     129,   130,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   131,     0,   132,   133,   134,   135,   136,     0,   137,
     138,   139,   140,   141,   142,     0,   143,   144,   145,   127,
       0,     0,     0,   652,     0,     0,   128,   129,   130,   120,
     121,   122,   123,   124,   125,   126,     0,     0,   131,     0,
     132,   133,   134,   135,   136,     0,   137,   138,   139,   140,
     141,   142,     0,   143,   144,   145,     0,     0,     0,     0,
     795,     0,     0,     0,     0,     0,   120,   121,   122,   123,
     124,   125,   126,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   127,     0,     0,     0,     0,     0,
       0,   128,   129,   130,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   131,     0,   132,   133,   134,   135,   136,
       0,   137,   138,   139,   140,   141,   142,     0,   143,   144,
     145,   127,     0,     0,     0,   797,     0,     0,   128,   129,
     130,   120,   121,   122,   123,   124,   125,   126,     0,     0,
     131,     0,   132,   133,   134,   135,   136,     0,   137,   138,
     139,   140,   141,   142,     0,   143,   144,   145,     0,     0,
       0,     0,   848,     0,   120,   121,   122,   123,   124,   125,
     126,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   432,   433,     0,   127,     0,     0,     0,
       0,     0,     0,   128,   129,   130,     0,   120,   121,   122,
     123,   124,   125,   126,     0,   131,   434,   132,   133,   134,
     135,   136,     0,   137,   138,   139,   140,   141,   142,   127,
     143,   144,   145,     0,     0,     0,   128,   129,   130,     0,
     120,   121,   122,   123,   124,   125,   126,     0,   131,   438,
     132,   133,   134,   135,   136,     0,   137,   138,   139,   140,
     141,   142,   127,   143,   144,   145,     0,     0,     0,   128,
     129,   130,     0,   120,     0,   122,   123,   124,   125,   126,
       0,   131,     0,   132,   133,   134,   135,   136,     0,   137,
     138,   139,   140,   141,   142,   127,   143,   144,   145,     0,
       0,     0,   128,   129,   130,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   133,   134,   135,
     136,     0,   137,   138,   139,   140,   141,   142,   127,   143,
     144,   145,     0,     0,     0,   128,   129,   130,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     133,   134,   135,   136,     0,   137,   138,   139,   140,   141,
     142,     0,   143,   144,   145
};

static const yytype_int16 yycheck[] =
{
      18,    15,    10,   249,   200,   236,    21,   385,   346,    98,
     368,   175,   403,   423,   264,     5,     5,     5,   398,     5,
       5,     5,   402,    31,    32,    33,    34,    35,    36,    37,
      38,    39,    40,    41,     5,    53,    56,     5,     5,     3,
      80,    66,   536,     5,     5,     5,    71,     5,    16,   543,
      21,     5,     5,   411,    21,    80,   104,    75,    69,    70,
      21,     5,     5,     5,     5,     5,    84,     5,    22,     5,
       8,     9,    10,     4,     5,   101,     5,   126,     5,   127,
      35,     5,   104,   132,    46,   463,     0,   127,     5,   104,
      13,    66,   470,   124,   102,   126,   124,   105,   187,   188,
     189,     4,     5,    67,   132,   127,    81,    48,    49,   125,
       5,   127,   120,   121,   122,   123,   124,   125,   126,   127,
     128,   129,   130,   131,   132,   133,   134,   135,   136,   137,
     138,   139,   140,   141,   142,   143,   144,   145,   123,   123,
     124,   129,   132,   132,   170,   129,   132,   132,   162,   540,
     644,   240,    83,    48,    49,   175,   176,   165,   568,   539,
     498,   132,   408,   123,   132,   132,   186,    56,    85,   129,
     259,   132,   197,   128,   263,   129,   118,    66,   428,   132,
      83,    53,    71,   208,   192,    43,   119,   125,   132,   132,
     216,    80,   132,   124,   202,   203,   132,   124,   206,   123,
     124,   118,   127,   399,    18,   130,   129,   124,    18,   220,
      18,   222,    84,   224,   124,    18,   594,    18,   236,   383,
     384,   124,   132,    18,   124,   114,     4,    84,   117,   254,
     125,   249,   726,     4,     5,   125,    18,   127,    18,    53,
      18,    19,    20,    53,   124,    53,   124,    25,    26,    27,
      53,   125,    53,   129,   132,   646,   132,   131,    53,   348,
     128,   118,   119,   120,   132,   354,   274,   125,    46,   127,
      84,    53,   766,    53,    84,    46,    84,   124,   124,   126,
     126,    84,   124,    84,   126,   132,   175,   176,   782,    84,
     132,   127,   318,   489,   126,   303,   132,   186,   324,    12,
     132,   190,    84,   126,    84,    83,   332,   126,   197,   132,
     125,   200,   127,   328,   126,   706,   547,   126,     5,   208,
     132,   815,   342,   132,   350,   124,   346,   126,   417,    31,
      32,    33,    11,    12,    13,   360,   727,    16,     5,   347,
     536,     8,     9,    10,    16,   370,   123,   124,   368,   126,
     690,   376,     5,   361,   694,   695,   364,   365,   366,   385,
     128,   369,   126,   127,   132,   254,   374,    31,    32,    33,
      12,    13,   380,     0,    16,   383,   384,     4,   403,   387,
     391,    16,    84,   394,   398,   776,   397,   134,   402,   690,
     408,   411,     5,   694,   695,   125,   404,   127,   125,     6,
     127,   409,   410,   132,   650,   651,   124,   765,   126,   125,
     101,   127,   420,   125,   116,   127,   118,   119,   120,   125,
      84,   127,     4,   431,   432,   433,   434,   125,   129,   127,
     438,   128,   440,   791,   442,     5,   125,   463,   127,     5,
     125,   530,   127,   532,   533,   534,   535,   127,   128,   807,
     114,   115,   116,   342,   118,   119,   120,   346,    16,     8,
       9,   126,    11,   125,   553,   127,   126,   127,    21,   477,
     478,   360,    21,   128,    23,    24,   484,     6,   498,   368,
     125,   370,   127,   126,   125,   128,   127,   376,    31,    32,
      33,    34,    35,     5,   125,   503,   127,   127,   126,    52,
     128,   509,   510,   125,   128,   127,   514,   125,   516,   127,
     399,   126,   127,   538,   403,   540,    69,    70,   543,    72,
     126,   125,   411,   127,   125,   539,   127,   126,   127,   547,
      68,    69,    70,    71,    72,    73,    74,    75,   784,   785,
     124,    84,   631,     5,   790,    98,    99,   636,   125,   124,
     127,   104,   124,    58,   562,    60,    58,    58,    60,    60,
     125,   125,   127,   127,   126,   127,   655,   575,   124,   112,
     113,   114,   115,   116,   124,   118,   119,   120,   124,   604,
     605,   125,     5,   127,   126,   127,   611,   124,   613,   597,
     126,   127,   126,   127,   147,   841,   126,   127,   126,   127,
     489,     5,   610,   126,   127,   126,   127,   126,   127,   498,
     124,   619,   128,   166,     5,   168,   641,   126,   127,   644,
     126,   710,   126,   127,   607,   608,   652,   124,   128,   132,
     124,   124,   650,   651,   187,   724,   725,   126,     5,     5,
     128,     5,   128,   124,   127,   653,   128,   536,   128,   538,
     128,   540,   126,    29,   543,    31,    32,    33,    34,    35,
     126,   669,   126,     5,     5,   126,   126,   220,   676,   222,
     126,   224,     5,   126,   126,     5,   126,   230,     5,   128,
     126,   706,     5,   126,   124,   126,   128,   126,   696,   126,
     779,    11,   126,   129,   126,    60,     5,   130,   128,   126,
     131,   726,   727,   124,   126,   131,   732,   260,    84,   126,
     125,   264,   126,   126,   126,   604,   605,   126,   126,   126,
     126,   126,   611,    58,   613,   126,    60,   130,   753,   754,
       5,   107,   108,   109,   759,   111,   112,   113,   114,   115,
     116,   766,   118,   119,   120,   765,   126,   126,     4,   126,
      40,   776,   641,   126,   126,   644,   104,   782,    53,     5,
      58,    40,   315,   316,   126,   126,   784,   785,   126,   126,
     126,   791,   790,   326,     5,   328,   104,    53,   130,   126,
       4,     5,   133,   126,    53,    53,    53,   807,    58,   126,
     815,     5,    58,    53,    18,    19,    20,   126,    60,     5,
     126,    25,    26,    27,   126,   126,   124,    58,    58,   834,
     126,   126,    60,   126,    58,     4,    17,   706,   162,   844,
     389,   475,    46,   841,   832,   583,   589,    99,   619,   308,
     406,   732,    -1,   732,   454,    -1,   274,   726,   727,    -1,
      -1,    -1,    -1,    67,    -1,    -1,    -1,    -1,    29,    -1,
      31,    32,    33,    34,    35,    -1,    -1,    -1,    -1,    83,
      -1,    -1,    -1,   416,   753,   754,   419,    91,    92,    93,
     759,    -1,    -1,   426,    -1,   428,   765,   766,    -1,    -1,
      -1,   105,   106,   107,    -1,    -1,    -1,   776,    -1,    -1,
      -1,   115,    -1,   782,     4,     5,    -1,    -1,    -1,    -1,
     124,   125,   791,    84,    -1,   129,    -1,   131,    18,    19,
      20,   135,   136,    -1,    -1,    25,    26,    27,   807,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   815,   108,   109,    -1,
     111,   112,   113,   114,   115,   116,    46,   118,   119,   120,
      -1,    -1,    -1,    -1,    -1,   834,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   844,    -1,    67,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,     4,     5,    83,    -1,    -1,    -1,   530,    -1,   532,
      -1,    91,    92,    93,    -1,    18,    19,    20,    -1,    -1,
      -1,    -1,    25,    26,    27,   105,   106,   107,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   115,    -1,    -1,    41,    42,
      -1,   564,    -1,    46,   124,   125,    -1,    -1,    -1,   129,
      -1,   131,    -1,    -1,    -1,   135,   136,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    67,    31,    32,    33,    34,    35,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     4,     5,
      83,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    91,    92,
      93,    -1,    18,    19,    20,    -1,    -1,    -1,    -1,    25,
      26,    27,   105,   106,   107,    -1,    -1,    -1,    -1,   632,
     633,   634,   115,   636,   637,    -1,    -1,    -1,    84,    -1,
      46,   124,    -1,    -1,    -1,    -1,   129,    53,    54,    -1,
      -1,    -1,   135,   136,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    67,   108,   109,    -1,   111,   112,   113,   114,   115,
     116,    -1,   118,   119,   120,    -1,    -1,    83,    -1,    -1,
      -1,    -1,     4,     5,    -1,    91,    92,    93,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    18,    19,    20,   105,
     106,   107,    -1,    25,    26,    27,    -1,    -1,   711,   115,
     713,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   124,    -1,
      -1,   724,    -1,   129,    46,    -1,    -1,    -1,    -1,   135,
     136,    53,    54,    -1,    -1,    -1,    -1,     4,     5,    -1,
      -1,    -1,    -1,    -1,    -1,    67,    -1,    -1,    -1,    -1,
      -1,    18,    19,    20,    -1,    -1,    -1,    -1,    25,    26,
      27,    83,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    91,
      92,    93,    -1,    -1,    -1,    -1,   779,   780,    -1,    46,
      -1,    -1,    -1,   105,   106,   107,    53,    54,    -1,    -1,
      -1,    -1,    -1,   115,    -1,    -1,    -1,    -1,    -1,    -1,
      67,    -1,   124,    -1,    -1,    -1,    -1,   129,    -1,    -1,
      -1,    -1,    -1,   135,   136,    -1,    83,    -1,    -1,    -1,
      -1,     4,     5,    -1,    91,    92,    93,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    18,    19,    20,   105,   106,
     107,    -1,    25,    26,    27,    -1,    -1,    -1,   115,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   124,    -1,    -1,
      -1,    -1,   129,    46,    -1,    -1,    -1,    -1,   135,   136,
      53,    54,     4,     5,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    67,    -1,    18,    19,    20,    -1,
      -1,    -1,    -1,    25,    26,    27,    -1,    -1,    -1,    -1,
      83,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    91,    92,
      93,    -1,    -1,    -1,    46,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   105,   106,   107,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   115,    -1,    -1,    67,    -1,    -1,    -1,    -1,
      -1,   124,     4,     5,    -1,    -1,   129,    -1,    -1,    -1,
      -1,    83,   135,   136,    -1,    -1,    18,    19,    20,    91,
      92,    93,    -1,    25,    26,    27,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   105,   106,   107,   108,    -1,    -1,    -1,
      -1,    -1,    -1,   115,    46,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   124,     4,     5,    -1,    -1,   129,    -1,    -1,
      -1,    -1,    -1,   135,   136,    67,    -1,    18,    19,    20,
      -1,    -1,    -1,    -1,    25,    26,    27,    -1,    -1,    -1,
      -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    91,
      92,    93,    -1,    -1,    -1,    46,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   105,   106,   107,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   115,    -1,    -1,    67,    -1,    -1,    -1,
      -1,    -1,   124,   125,    -1,    -1,    -1,   129,    -1,     4,
       5,    -1,    83,   135,   136,    -1,    -1,    -1,    -1,    -1,
      91,    92,    93,    18,    19,    20,    -1,    -1,    -1,    -1,
      25,    26,    27,    -1,   105,   106,   107,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   115,    -1,    -1,    -1,    -1,    -1,
      -1,    46,   123,   124,    -1,    -1,    -1,    -1,   129,     4,
       5,    -1,    -1,    -1,   135,   136,    -1,    -1,    -1,    -1,
      -1,    -1,    67,    18,    19,    20,    -1,    -1,    -1,    -1,
      25,    26,    27,    -1,    -1,    -1,    -1,    -1,    83,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    91,    92,    93,    -1,
      -1,    46,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    54,
     105,   106,   107,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     115,    -1,    67,    -1,    -1,    -1,    -1,    -1,    -1,   124,
      -1,    -1,    -1,    -1,   129,    -1,   131,    -1,    83,    -1,
     135,   136,    -1,     4,     5,    -1,    91,    92,    93,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    18,    19,    20,
     105,   106,   107,    -1,    25,    26,    27,    -1,    -1,    -1,
     115,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   124,
      -1,    -1,    -1,    -1,   129,    46,    -1,    -1,    -1,    -1,
     135,   136,    -1,    54,     4,     5,    -1,     4,     5,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    67,    -1,    18,    19,
      20,    18,    19,    20,    -1,    25,    26,    27,    25,    26,
      27,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      91,    92,    93,    -1,    -1,    -1,    46,    -1,    -1,    46,
      -1,    -1,    -1,    -1,   105,   106,   107,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   115,    -1,    -1,    67,    -1,    -1,
      67,    -1,    -1,   124,    -1,    -1,    -1,    -1,   129,    -1,
      -1,    -1,    -1,    83,   135,   136,    83,    -1,    -1,    -1,
      -1,    91,    92,    93,    91,    92,    93,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   105,   106,   107,   105,   106,
     107,    -1,    -1,    -1,    -1,   115,    -1,     5,   115,     7,
      -1,    -1,    -1,    11,   124,   125,    -1,   124,    -1,   129,
      -1,    -1,   129,    21,    22,   135,   136,    -1,   135,   136,
      -1,    29,    30,    31,    32,    33,    34,    35,    -1,    37,
      -1,    39,    -1,    -1,    -1,    -1,    44,    45,    -1,    -1,
      -1,    -1,    50,    51,    52,    -1,    -1,    -1,    56,    -1,
      -1,    -1,    -1,    61,    62,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    76,    -1,
      78,    79,    -1,    -1,    -1,    -1,    84,    -1,    -1,    -1,
      -1,    89,    90,    91,    92,    93,    94,    -1,    -1,    -1,
      98,    -1,    -1,    -1,    -1,   103,    -1,   105,   106,   107,
     108,   109,    -1,   111,   112,   113,   114,   115,   116,    -1,
     118,   119,   120,    -1,    -1,   123,    -1,    -1,   126,    -1,
      -1,   129,    -1,    -1,    -1,     5,   134,     7,     8,     9,
      -1,    11,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    21,    22,    23,    24,    -1,     5,    -1,     7,    -1,
      -1,    -1,    11,    -1,    -1,    -1,    -1,    37,    -1,    39,
      -1,    -1,    21,    22,    44,    45,    -1,    -1,    -1,    -1,
      50,    51,    52,    -1,    -1,    -1,    56,    -1,    37,    38,
      39,    61,    62,    -1,    -1,    44,    45,    -1,    -1,    -1,
      -1,    50,    51,    52,    -1,    -1,    76,    56,    78,    79,
      -1,    -1,    61,    62,    -1,    -1,    -1,    -1,    -1,    89,
      90,    -1,    -1,    -1,    94,    -1,    -1,    76,    98,    78,
      79,     5,    -1,     7,    -1,    -1,    -1,    11,    -1,    -1,
      89,    90,    -1,    -1,    -1,    94,    -1,    21,    22,    98,
      -1,    -1,    -1,   123,    -1,   104,    -1,    -1,    -1,   129,
      -1,    -1,    -1,    37,   134,    39,    -1,    -1,    -1,    -1,
      44,    45,    -1,    -1,   123,    -1,    50,    51,    52,    -1,
     129,    -1,    56,    -1,    -1,   134,    -1,    61,    62,    -1,
      -1,    -1,    -1,    -1,     5,    -1,     7,    -1,    -1,    -1,
      11,    -1,    76,    -1,    78,    79,    -1,    -1,    -1,    -1,
      21,    22,    -1,    -1,    -1,    89,    90,    -1,    -1,    -1,
      94,    -1,    -1,    -1,    98,    -1,    37,    38,    39,    -1,
      -1,    -1,    -1,    44,    45,    -1,    -1,    -1,    -1,    50,
      51,    52,    -1,    -1,    -1,    56,    -1,    -1,    -1,   123,
      61,    62,   126,    -1,    -1,   129,    -1,     5,    -1,     7,
     134,    -1,    -1,    11,    -1,    76,    -1,    78,    79,    -1,
      -1,    -1,    -1,    21,    22,    -1,    -1,    -1,    89,    90,
      -1,    -1,    -1,    94,    -1,    -1,    -1,    98,    -1,    37,
      -1,    39,    -1,    -1,    -1,    -1,    44,    45,    -1,    -1,
      -1,    -1,    50,    51,    52,    -1,    -1,    -1,    56,    -1,
      -1,    -1,   123,    61,    62,    -1,    -1,    -1,   129,    -1,
       5,    -1,     7,   134,    -1,    -1,    11,    -1,    76,    77,
      78,    79,    -1,    -1,    -1,    -1,    21,    22,    -1,    -1,
      -1,    89,    90,    -1,    -1,    -1,    94,    -1,    -1,    -1,
      98,    -1,    37,    -1,    39,    -1,    -1,    -1,    -1,    44,
      45,    -1,    -1,    -1,    -1,    50,    51,    52,    -1,    -1,
      -1,    56,    -1,    58,    -1,   123,    61,    62,    -1,    -1,
      -1,   129,    -1,     5,    -1,     7,   134,    -1,    -1,    11,
      -1,    76,    -1,    78,    79,    -1,    -1,    -1,    -1,    21,
      22,    -1,    -1,    -1,    89,    90,    -1,    -1,    -1,    94,
      -1,    -1,    -1,    98,    -1,    37,    38,    39,    -1,    -1,
      -1,    -1,    44,    45,    -1,    -1,    -1,    -1,    50,    51,
      52,    -1,    -1,    -1,    56,    -1,    -1,    -1,   123,    61,
      62,    -1,    -1,    -1,   129,    -1,     5,    -1,     7,   134,
      -1,    -1,    11,    -1,    76,    -1,    78,    79,    -1,    -1,
      -1,    -1,    21,    22,    -1,    -1,    -1,    89,    90,    -1,
      -1,    -1,    94,    -1,    -1,    -1,    98,    -1,    37,    -1,
      39,    -1,    -1,    -1,    -1,    44,    45,    -1,    -1,    -1,
      -1,    50,    51,    52,    -1,    -1,    -1,    56,    -1,    58,
      -1,   123,    61,    62,    -1,    -1,    -1,   129,    -1,     5,
      -1,     7,   134,    -1,    -1,    11,    -1,    76,    -1,    78,
      79,    -1,    -1,    -1,    -1,    21,    22,    -1,    -1,    -1,
      89,    90,    -1,    -1,    -1,    94,    -1,    -1,    -1,    98,
      -1,    37,    -1,    39,    -1,    -1,    -1,    -1,    44,    45,
      -1,    -1,    -1,    -1,    50,    51,    52,    -1,    -1,    -1,
      56,    -1,    -1,    -1,   123,    61,    62,    -1,    -1,    -1,
     129,    -1,     5,    -1,     7,   134,    -1,    -1,    11,    -1,
      76,    -1,    78,    79,    -1,    -1,    -1,    -1,    21,    22,
      -1,    -1,    -1,    89,    90,    -1,    -1,    -1,    94,    -1,
      -1,    -1,    98,    -1,    37,    -1,    39,    -1,    -1,    -1,
      -1,    44,    45,    -1,    -1,    -1,    -1,    50,    51,    52,
      -1,    -1,    -1,    56,    -1,    -1,    -1,   123,    61,    62,
     126,    -1,    -1,   129,    -1,     5,    -1,     7,   134,    -1,
      -1,    11,    -1,    76,    -1,    78,    79,    -1,    -1,    -1,
      -1,    21,    22,    -1,    -1,    -1,    89,    90,    -1,    -1,
      -1,    94,    -1,    -1,    -1,    98,    -1,    37,    -1,    39,
      -1,    -1,    -1,    -1,    44,    45,    -1,    -1,    -1,    -1,
      50,    51,    52,    -1,    -1,    -1,    56,    -1,    -1,    -1,
     123,    61,    62,   126,    -1,    -1,   129,    -1,    -1,    -1,
      -1,   134,    -1,    -1,    -1,    -1,    76,    -1,    78,    79,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    89,
      90,    -1,    -1,    -1,    94,    -1,    -1,    -1,    98,     5,
      -1,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      16,    17,    -1,    -1,    -1,    21,    -1,    23,    -1,    -1,
      -1,    -1,    -1,   123,    -1,    -1,    -1,    -1,    -1,   129,
      36,    37,    -1,    39,   134,    -1,    -1,    43,    -1,    -1,
      -1,    47,    48,    49,    50,    -1,    -1,    -1,    -1,    55,
      -1,    -1,    -1,    -1,    -1,    61,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    79,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    88,    -1,    -1,    -1,    -1,    -1,    -1,    95,
      96,    -1,    -1,    99,   100,     5,   102,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    16,    17,    -1,    -1,
      -1,    21,    -1,    23,    -1,    -1,    -1,    -1,    -1,    -1,
     126,    -1,    -1,    -1,    -1,    -1,    36,    37,    -1,    39,
      -1,    -1,    -1,    43,    -1,    -1,    -1,    47,    48,    49,
      50,    -1,    -1,    -1,    -1,    55,    -1,    -1,    -1,    -1,
      -1,    61,    -1,    -1,    -1,    29,    30,    31,    32,    33,
      34,    35,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    79,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    88,    -1,
      -1,    -1,    -1,    -1,    -1,    95,    96,    -1,    -1,    99,
     100,    -1,   102,    29,    30,    31,    32,    33,    34,    35,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    81,    82,    -1,
      84,    -1,    -1,    -1,    -1,    -1,   126,    91,    92,    93,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   103,
     104,   105,   106,   107,   108,   109,    -1,   111,   112,   113,
     114,   115,   116,    -1,   118,   119,   120,    -1,    84,    -1,
      -1,    -1,    -1,    -1,    -1,    91,    92,    93,    -1,   133,
      29,    30,    31,    32,    33,    34,    35,   103,    -1,   105,
     106,   107,   108,   109,    -1,   111,   112,   113,   114,   115,
     116,    -1,   118,   119,   120,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   133,    29,    30,
      31,    32,    33,    34,    35,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    84,    -1,    -1,    -1,    -1,
      -1,    -1,    91,    92,    93,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   103,    -1,   105,   106,   107,   108,
     109,    -1,   111,   112,   113,   114,   115,   116,    -1,   118,
     119,   120,    -1,    84,    -1,    -1,    -1,    -1,    -1,    -1,
      91,    92,    93,    -1,   133,    29,    30,    31,    32,    33,
      34,    35,   103,    -1,   105,   106,   107,   108,   109,    -1,
     111,   112,   113,   114,   115,   116,    -1,   118,   119,   120,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   133,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      84,    -1,    -1,    -1,    -1,    -1,    -1,    91,    92,    93,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   103,
      -1,   105,   106,   107,   108,   109,    -1,   111,   112,   113,
     114,   115,   116,    -1,   118,   119,   120,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,     5,   129,     7,     8,     9,    10,
      11,    12,    13,    14,    15,    16,    17,    -1,    -1,    -1,
      21,    -1,    23,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    36,    37,    -1,    39,    -1,
      -1,    -1,    43,    -1,    -1,    -1,    47,    48,    49,    50,
      -1,    -1,    -1,    -1,    55,    -1,    -1,    -1,    -1,    -1,
      61,    29,    30,    31,    32,    33,    34,    35,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    79,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    88,    -1,    -1,
      -1,    -1,    -1,    -1,    95,    96,    -1,    -1,    99,   100,
      -1,   102,    -1,   104,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    84,    -1,    -1,    -1,
      -1,    -1,    -1,    91,    92,    93,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   103,    -1,   105,   106,   107,
     108,   109,    -1,   111,   112,   113,   114,   115,   116,    -1,
     118,   119,   120,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     128,     5,     6,     7,     8,     9,    10,    11,    12,    13,
      14,    15,    16,    17,    -1,    -1,    -1,    21,    -1,    23,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    36,    -1,    -1,    -1,    -1,    -1,    -1,    43,
      -1,    -1,    -1,    47,    48,    49,    -1,    -1,    -1,    -1,
      -1,    55,    -1,    57,    -1,    59,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    67,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    79,    -1,    -1,    -1,    -1,
      -1,    -1,    86,    -1,    88,    -1,    -1,    -1,    -1,    -1,
      -1,    95,    96,    97,    -1,    99,   100,     5,   102,     7,
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
      -1,    -1,    -1,    -1,    36,    37,    -1,    39,    -1,    -1,
      -1,    43,    -1,    -1,    -1,    47,    48,    49,    50,    -1,
      -1,    -1,    -1,    55,    -1,    -1,    -1,    -1,    -1,    61,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    79,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    87,    88,    -1,    -1,    -1,
      -1,    -1,    -1,    95,    96,    -1,    -1,    99,   100,     5,
     102,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      16,    17,    -1,    -1,    -1,    21,    -1,    23,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      36,    37,    38,    39,    -1,    -1,    -1,    43,    -1,    -1,
      -1,    47,    48,    49,    50,    -1,    -1,    -1,    -1,    55,
      -1,    -1,    -1,    -1,    -1,    61,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    79,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    88,    -1,    -1,    -1,    -1,    -1,    -1,    95,
      96,    -1,    -1,    99,   100,     5,   102,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    16,    17,    -1,    -1,
      -1,    21,    -1,    23,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    36,    37,    38,    39,
      -1,    -1,    -1,    43,    -1,    -1,    -1,    47,    48,    49,
      50,    -1,    -1,    -1,    -1,    55,    -1,    -1,    -1,    -1,
      -1,    61,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    79,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    88,    -1,
      -1,    -1,    -1,    -1,    -1,    95,    96,    -1,    -1,    99,
     100,     5,   102,     7,     8,     9,    10,    11,    12,    13,
      14,    15,    16,    17,    -1,    -1,    -1,    21,    -1,    23,
      -1,    -1,    -1,    29,    30,    31,    32,    33,    34,    35,
      -1,    -1,    36,    37,    -1,    39,    -1,    -1,    -1,    43,
      -1,    -1,    -1,    47,    48,    49,    50,    -1,    -1,    -1,
      -1,    55,    -1,    -1,    -1,    -1,    -1,    61,    -1,    -1,
      29,    30,    31,    32,    33,    34,    35,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    79,    -1,    -1,    84,    -1,
      -1,    -1,    -1,    -1,    88,    91,    92,    93,    -1,    -1,
      -1,    95,    96,    -1,    -1,    99,   100,   103,   102,   105,
     106,   107,   108,   109,    -1,   111,   112,   113,   114,   115,
     116,    -1,   118,   119,   120,    84,    -1,    -1,    -1,    -1,
     126,    -1,    91,    92,    93,    29,    30,    31,    32,    33,
      34,    35,    -1,    -1,   103,    -1,   105,   106,   107,   108,
     109,    -1,   111,   112,   113,   114,   115,   116,    -1,   118,
     119,   120,    -1,    -1,    -1,    -1,    -1,   126,    -1,    -1,
      -1,    -1,    29,    30,    31,    32,    33,    34,    35,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      84,    -1,    -1,    -1,    -1,    -1,    -1,    91,    92,    93,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   103,
      -1,   105,   106,   107,   108,   109,    -1,   111,   112,   113,
     114,   115,   116,    -1,   118,   119,   120,    84,    -1,    -1,
      -1,    -1,   126,    -1,    91,    92,    93,    29,    30,    31,
      32,    33,    34,    35,    -1,    -1,   103,    -1,   105,   106,
     107,   108,   109,    -1,   111,   112,   113,   114,   115,   116,
      -1,   118,   119,   120,    -1,    -1,    -1,    -1,    -1,   126,
      -1,    -1,    -1,    -1,    29,    30,    31,    32,    33,    34,
      35,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    84,    -1,    -1,    -1,    -1,    -1,    -1,    91,
      92,    93,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   103,    -1,   105,   106,   107,   108,   109,    -1,   111,
     112,   113,   114,   115,   116,    -1,   118,   119,   120,    84,
      -1,    -1,    -1,    -1,   126,    -1,    91,    92,    93,    29,
      30,    31,    32,    33,    34,    35,    -1,    -1,   103,    -1,
     105,   106,   107,   108,   109,    -1,   111,   112,   113,   114,
     115,   116,    -1,   118,   119,   120,    -1,    -1,    -1,    -1,
      -1,   126,    -1,    -1,    -1,    -1,    29,    30,    31,    32,
      33,    34,    35,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    84,    -1,    -1,    -1,    -1,    -1,
      -1,    91,    92,    93,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   103,    -1,   105,   106,   107,   108,   109,
      -1,   111,   112,   113,   114,   115,   116,    -1,   118,   119,
     120,    84,    -1,    -1,    -1,    -1,   126,    -1,    91,    92,
      93,    29,    30,    31,    32,    33,    34,    35,    -1,    -1,
     103,    -1,   105,   106,   107,   108,   109,    -1,   111,   112,
     113,   114,   115,   116,    -1,   118,   119,   120,    -1,    -1,
      -1,    -1,    -1,   126,    -1,    -1,    -1,    -1,    29,    30,
      31,    32,    33,    34,    35,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    84,    -1,    -1,    -1,
      -1,    -1,    -1,    91,    92,    93,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   103,    -1,   105,   106,   107,
     108,   109,    -1,   111,   112,   113,   114,   115,   116,    -1,
     118,   119,   120,    84,    -1,    -1,    -1,    -1,   126,    -1,
      91,    92,    93,    29,    30,    31,    32,    33,    34,    35,
      -1,    -1,   103,    -1,   105,   106,   107,   108,   109,    -1,
     111,   112,   113,   114,   115,   116,    -1,   118,   119,   120,
      -1,    -1,    -1,    -1,    -1,   126,    -1,    -1,    -1,    -1,
      29,    30,    31,    32,    33,    34,    35,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    84,    -1,
      -1,    -1,    -1,    -1,    -1,    91,    92,    93,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   103,    -1,   105,
     106,   107,   108,   109,    -1,   111,   112,   113,   114,   115,
     116,    -1,   118,   119,   120,    84,    -1,    -1,    -1,    -1,
     126,    -1,    91,    92,    93,    29,    30,    31,    32,    33,
      34,    35,    -1,    -1,   103,    -1,   105,   106,   107,   108,
     109,    -1,   111,   112,   113,   114,   115,   116,    -1,   118,
     119,   120,    -1,    -1,    -1,    -1,    -1,   126,    -1,    -1,
      -1,    -1,    29,    30,    31,    32,    33,    34,    35,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      84,    -1,    -1,    -1,    -1,    -1,    -1,    91,    92,    93,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   103,
      -1,   105,   106,   107,   108,   109,    -1,   111,   112,   113,
     114,   115,   116,    -1,   118,   119,   120,    84,    -1,    -1,
      -1,    -1,   126,    -1,    91,    92,    93,    29,    30,    31,
      32,    33,    34,    35,    -1,    -1,   103,    -1,   105,   106,
     107,   108,   109,    -1,   111,   112,   113,   114,   115,   116,
      -1,   118,   119,   120,    -1,    -1,    -1,    -1,    -1,   126,
      -1,    -1,    -1,    -1,    29,    30,    31,    32,    33,    34,
      35,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    84,    -1,    -1,    -1,    -1,    -1,    -1,    91,
      92,    93,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   103,    -1,   105,   106,   107,   108,   109,    -1,   111,
     112,   113,   114,   115,   116,    -1,   118,   119,   120,    84,
      -1,    -1,    -1,    -1,   126,    -1,    91,    92,    93,    29,
      30,    31,    32,    33,    34,    35,    -1,    -1,   103,    -1,
     105,   106,   107,   108,   109,    -1,   111,   112,   113,   114,
     115,   116,    -1,   118,   119,   120,    -1,    -1,    -1,    -1,
     125,    -1,    -1,    -1,    -1,    -1,    29,    30,    31,    32,
      33,    34,    35,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    84,    -1,    -1,    -1,    -1,    -1,
      -1,    91,    92,    93,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   103,    -1,   105,   106,   107,   108,   109,
      -1,   111,   112,   113,   114,   115,   116,    -1,   118,   119,
     120,    84,    -1,    -1,    -1,   125,    -1,    -1,    91,    92,
      93,    29,    30,    31,    32,    33,    34,    35,    -1,    -1,
     103,    -1,   105,   106,   107,   108,   109,    -1,   111,   112,
     113,   114,   115,   116,    -1,   118,   119,   120,    -1,    -1,
      -1,    -1,   125,    -1,    -1,    -1,    -1,    -1,    29,    30,
      31,    32,    33,    34,    35,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    84,    -1,    -1,    -1,
      -1,    -1,    -1,    91,    92,    93,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   103,    -1,   105,   106,   107,
     108,   109,    -1,   111,   112,   113,   114,   115,   116,    -1,
     118,   119,   120,    84,    -1,    -1,    -1,   125,    -1,    -1,
      91,    92,    93,    29,    30,    31,    32,    33,    34,    35,
      -1,    -1,   103,    -1,   105,   106,   107,   108,   109,    -1,
     111,   112,   113,   114,   115,   116,    -1,   118,   119,   120,
      -1,    -1,    -1,    -1,   125,    -1,    -1,    -1,    -1,    -1,
      29,    30,    31,    32,    33,    34,    35,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    84,    -1,
      -1,    -1,    -1,    -1,    -1,    91,    92,    93,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   103,    -1,   105,
     106,   107,   108,   109,    -1,   111,   112,   113,   114,   115,
     116,    -1,   118,   119,   120,    84,    -1,    -1,    -1,   125,
      -1,    -1,    91,    92,    93,    29,    30,    31,    32,    33,
      34,    35,    -1,    -1,   103,    -1,   105,   106,   107,   108,
     109,    -1,   111,   112,   113,   114,   115,   116,    -1,   118,
     119,   120,    -1,    -1,    -1,    -1,   125,    -1,    -1,    -1,
      -1,    -1,    29,    30,    31,    32,    33,    34,    35,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      84,    -1,    -1,    -1,    -1,    -1,    -1,    91,    92,    93,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   103,
      -1,   105,   106,   107,   108,   109,    -1,   111,   112,   113,
     114,   115,   116,    -1,   118,   119,   120,    84,    -1,    -1,
      -1,   125,    -1,    -1,    91,    92,    93,    29,    30,    31,
      32,    33,    34,    35,    -1,    -1,   103,    -1,   105,   106,
     107,   108,   109,    -1,   111,   112,   113,   114,   115,   116,
      -1,   118,   119,   120,    -1,    -1,    -1,    -1,   125,    -1,
      -1,    -1,    -1,    -1,    29,    30,    31,    32,    33,    34,
      35,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    84,    -1,    -1,    -1,    -1,    -1,    -1,    91,
      92,    93,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   103,    -1,   105,   106,   107,   108,   109,    -1,   111,
     112,   113,   114,   115,   116,    -1,   118,   119,   120,    84,
      -1,    -1,    -1,   125,    -1,    -1,    91,    92,    93,    29,
      30,    31,    32,    33,    34,    35,    -1,    -1,   103,    -1,
     105,   106,   107,   108,   109,    -1,   111,   112,   113,   114,
     115,   116,    -1,   118,   119,   120,    -1,    -1,    -1,    -1,
     125,    -1,    -1,    -1,    -1,    -1,    29,    30,    31,    32,
      33,    34,    35,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    84,    -1,    -1,    -1,    -1,    -1,
      -1,    91,    92,    93,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   103,    -1,   105,   106,   107,   108,   109,
      -1,   111,   112,   113,   114,   115,   116,    -1,   118,   119,
     120,    84,    -1,    -1,    -1,   125,    -1,    -1,    91,    92,
      93,    29,    30,    31,    32,    33,    34,    35,    -1,    -1,
     103,    -1,   105,   106,   107,   108,   109,    -1,   111,   112,
     113,   114,   115,   116,    -1,   118,   119,   120,    -1,    -1,
      -1,    -1,   125,    -1,    29,    30,    31,    32,    33,    34,
      35,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    81,    82,    -1,    84,    -1,    -1,    -1,
      -1,    -1,    -1,    91,    92,    93,    -1,    29,    30,    31,
      32,    33,    34,    35,    -1,   103,   104,   105,   106,   107,
     108,   109,    -1,   111,   112,   113,   114,   115,   116,    84,
     118,   119,   120,    -1,    -1,    -1,    91,    92,    93,    -1,
      29,    30,    31,    32,    33,    34,    35,    -1,   103,   104,
     105,   106,   107,   108,   109,    -1,   111,   112,   113,   114,
     115,   116,    84,   118,   119,   120,    -1,    -1,    -1,    91,
      92,    93,    -1,    29,    -1,    31,    32,    33,    34,    35,
      -1,   103,    -1,   105,   106,   107,   108,   109,    -1,   111,
     112,   113,   114,   115,   116,    84,   118,   119,   120,    -1,
      -1,    -1,    91,    92,    93,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   106,   107,   108,
     109,    -1,   111,   112,   113,   114,   115,   116,    84,   118,
     119,   120,    -1,    -1,    -1,    91,    92,    93,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     106,   107,   108,   109,    -1,   111,   112,   113,   114,   115,
     116,    -1,   118,   119,   120
};

/* YYSTOS[STATE-NUM] -- The symbol kind of the accessing symbol of
   state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,     3,    67,   138,   139,   140,   141,   148,     5,     4,
       5,    46,     0,   140,   123,   124,   126,   142,   143,     5,
       4,     5,    18,    19,    20,    25,    26,    27,    46,    67,
      83,    91,    92,    93,   105,   106,   107,   115,   124,   129,
     135,   136,   207,   211,   124,     5,     8,     9,    10,   125,
     144,   145,   205,   143,     5,     6,     7,    11,    12,    13,
      14,    15,    16,    17,    21,    23,    36,    43,    47,    48,
      49,    55,    57,    59,    79,    86,    88,    95,    96,    97,
      99,   100,   102,   146,   147,   148,   149,   152,   153,   157,
     158,   161,   162,   163,   168,   175,   176,   187,   205,   206,
     119,   124,   132,   203,   204,   124,   211,   211,   211,   211,
     211,   211,   211,   211,   108,   208,   209,   211,   211,   211,
      29,    30,    31,    32,    33,    34,    35,    84,    91,    92,
      93,   103,   105,   106,   107,   108,   109,   111,   112,   113,
     114,   115,   116,   118,   119,   120,     5,    48,    49,   125,
     166,   167,    12,    13,    16,    11,    12,    13,    16,    12,
     126,   125,   127,     5,    21,   132,   203,   146,     5,   123,
     124,   174,     5,   123,   124,   154,   171,   191,   192,   201,
     207,    16,    16,     5,   202,     5,     7,    11,    21,    22,
      37,    39,    44,    45,    50,    51,    52,    56,    61,    62,
      76,    78,    89,    90,    94,    98,   123,   134,   180,   184,
     187,   188,   189,   190,   201,     5,   124,     5,   164,   165,
      16,   164,   203,   164,   203,   180,   184,     5,    21,   156,
     203,     5,     5,    46,   185,   186,    37,    39,    50,    61,
      88,   149,   152,   153,   161,   162,   163,   168,   175,   177,
     178,   179,   187,   184,   180,   101,     6,   146,   202,   203,
       5,   150,   151,   174,   203,     4,   199,   211,   211,   203,
     204,   211,   125,   207,   127,   130,   207,   211,   211,   211,
     211,   211,   211,   211,   211,   211,   211,   211,   211,   211,
     211,   211,   211,   211,   211,   211,   211,   211,   211,   211,
     211,   211,   211,   128,     5,   203,     5,   125,   127,    16,
     126,   145,   128,     5,   211,     5,   203,     6,   124,   126,
     203,     4,     5,    83,   124,   199,     5,   203,   204,     4,
       5,    83,   124,    68,    69,    70,    71,    72,    73,    74,
      75,   155,   171,   201,   201,   126,   127,   128,   127,   126,
     124,   126,   201,   202,   203,   202,   202,    38,   104,   184,
     200,   124,   211,     5,   124,   124,   124,   184,   124,   124,
     200,     5,   211,   211,   124,     5,   211,     5,    85,   118,
     124,   126,   184,    35,   128,   124,   199,   128,   126,   127,
     164,   203,   126,   164,   203,   126,   164,   203,   124,   126,
       5,   203,   124,   126,   128,    80,   127,   104,   177,   124,
     124,   124,   202,    87,   178,   184,    13,   129,   126,   202,
     128,   203,   126,   127,     5,   202,     5,   151,   203,     5,
     125,   127,    81,    82,   104,   133,   125,   209,   104,   211,
     128,     5,   128,   167,     4,    18,    19,    20,    25,    26,
      27,    46,    83,   210,   128,   203,     5,   203,   125,   131,
     169,   170,   199,   124,   125,   131,   172,   173,   199,   125,
     124,   203,   203,   204,   199,   127,   201,   128,   128,   192,
     211,   202,   125,   199,   128,   126,   202,   126,   126,     5,
      38,   184,   211,   126,   126,   211,   211,   211,    22,   191,
     211,    77,   126,   128,   126,   211,   126,   126,   184,    41,
      42,   182,   183,   211,   171,   211,   171,   211,   169,   199,
     125,   211,   165,   126,   164,   126,   164,   126,   164,   144,
       8,     9,    11,    21,    23,    24,   159,   160,   200,   124,
     126,     5,   144,   159,   184,   211,   186,     5,    38,   211,
     211,   191,   126,   129,   203,   202,   126,   203,   211,   126,
       5,   150,   128,   126,   203,   126,     5,   151,   203,   211,
     211,   211,   211,   211,   211,   128,   211,   210,     5,   126,
       5,   118,   125,   127,   125,   169,   199,     5,   125,   127,
     125,   126,   125,   169,   124,   125,   155,   128,   211,   211,
     126,   125,   211,   126,   200,   125,   125,   125,   125,   192,
     126,   125,   211,   125,   211,   211,    43,   125,   127,   181,
     211,   126,   211,   126,   125,   125,   126,   126,   126,   126,
     125,    21,   202,   203,    11,   202,   203,   202,   202,   202,
     160,   200,    58,   144,   159,   184,   126,   125,   184,    60,
     177,   125,   125,   126,   202,   129,   130,   126,   211,   126,
     203,   126,   126,     5,   150,   133,   133,   133,   211,   124,
     132,   126,   170,   126,   125,   125,   124,   173,   126,   125,
     169,   125,   211,   126,   126,   126,   126,    38,   184,    54,
     193,   195,   197,   199,   193,   193,   126,   211,   184,   126,
     184,   183,   126,   126,   126,   126,   126,   202,   126,   203,
     203,   203,   126,     5,   202,   203,   126,   203,   126,   126,
      58,   125,   184,    58,    11,    21,   159,   126,    60,    38,
     178,    54,   194,   196,   198,   199,   211,   130,   202,     5,
     126,   126,   126,   126,   125,   211,     4,   126,   126,   211,
     126,   125,   126,    40,   104,    53,   195,   197,    53,   104,
      53,   197,    53,   197,   211,   126,   159,   184,   126,   126,
     202,   203,   203,   126,     5,   126,   126,    58,   202,   203,
     202,   184,   159,   184,    40,   104,    53,   196,   198,    53,
     104,   126,     5,   130,   126,   125,   133,   125,   126,   184,
     126,   184,    53,   126,   184,    53,    53,   126,   191,   184,
      58,   126,     5,   126,   126,   159,   184,   126,   202,   126,
      58,   184,    60,   178,   126,   178,    53,   126,   178,   191,
     126,     5,   124,   191,   125,    58,   126,   184,    58,   126,
      60,   125,   126,   211,   125,   184,    58,   178,   125,   184
};

/* YYR1[RULE-NUM] -- Symbol kind of the left-hand side of rule RULE-NUM.  */
static const yytype_uint8 yyr1[] =
{
       0,   137,   138,   139,   139,   140,   140,   141,   141,   141,
     142,   142,   143,   143,   143,   144,   144,   145,   145,   145,
     145,   145,   145,   145,   145,   145,   146,   146,   147,   147,
     147,   147,   147,   147,   147,   147,   147,   147,   147,   147,
     147,   147,   148,   148,   148,   148,   148,   149,   150,   150,
     151,   151,   152,   152,   152,   152,   152,   152,   152,   152,
     152,   152,   152,   152,   152,   152,   152,   152,   152,   152,
     153,   153,   153,   153,   154,   155,   155,   155,   155,   155,
     155,   155,   155,   156,   156,   157,   157,   157,   157,   157,
     157,   157,   157,   157,   158,   158,   158,   158,   159,   159,
     160,   160,   160,   160,   160,   160,   160,   160,   160,   160,
     160,   160,   160,   161,   161,   161,   161,   161,   162,   162,
     162,   163,   164,   164,   165,   166,   166,   167,   167,   167,
     167,   168,   168,   168,   168,   168,   168,   168,   168,   168,
     168,   168,   168,   168,   169,   169,   170,   170,   170,   170,
     171,   171,   171,   171,   172,   172,   173,   173,   174,   174,
     174,   174,   174,   174,   175,   175,   175,   175,   176,   177,
     177,   178,   178,   178,   178,   178,   178,   178,   178,   178,
     178,   178,   178,   178,   178,   178,   178,   178,   178,   179,
     180,   180,   180,   180,   181,   181,   182,   182,   183,   183,
     183,   184,   184,   184,   184,   184,   184,   184,   184,   184,
     184,   184,   184,   184,   184,   184,   184,   184,   184,   184,
     184,   184,   184,   184,   184,   184,   184,   184,   184,   184,
     184,   184,   184,   184,   184,   184,   184,   184,   184,   184,
     185,   185,   186,   186,   187,   188,   188,   189,   190,   191,
     191,   192,   193,   193,   194,   194,   195,   195,   196,   196,
     197,   197,   198,   198,   199,   199,   200,   200,   201,   201,
     201,   201,   201,   201,   202,   202,   203,   203,   203,   204,
     205,   205,   205,   205,   205,   205,   205,   205,   205,   205,
     205,   205,   206,   206,   206,   206,   206,   206,   206,   206,
     206,   206,   206,   206,   206,   207,   208,   208,   209,   209,
     209,   210,   210,   210,   210,   210,   210,   210,   210,   210,
     211,   211,   211,   211,   211,   211,   211,   211,   211,   211,
     211,   211,   211,   211,   211,   211,   211,   211,   211,   211,
     211,   211,   211,   211,   211,   211,   211,   211,   211,   211,
     211,   211,   211,   211,   211,   211,   211,   211,   211,   211,
     211,   211,   211,   211,   211,   211,   211,   211,   211,   211,
     211,   211,   211,   211
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
       3,     1,     3,     1,     3,     9,    10,     5,     5,     3,
       1,     3,     2,     1,     2,     1,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     1,     2,     1,     1,     2,
       3,     3,     2,     1,     3,     1,     5,     5,     5,     3,
       1,     1,     1,     2,     2,     2,     2,     2,     2,     3,
       2,     2,     1,     1,     1,     1,     1,     1,     2,     2,
       1,     1,     1,     1,     1,     3,     3,     1,     2,     1,
       2,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     4,     1,     1,     1,     1,
       1,     1,     2,     3,     3,     2,     5,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     4,     3,     1,     2,     2,     2,     2,     2,
       2,     2,     2,     2
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

#line 3012 "y.tab.c"

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

#line 395 "yaccs/verilog.yacc"

