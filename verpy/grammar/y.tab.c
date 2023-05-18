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
#define YYLAST   5427

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  137
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  75
/* YYNRULES -- Number of rules.  */
#define YYNRULES  370
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  847

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
       0,    45,    45,    46,    46,    47,    47,    48,    48,    50,
      50,    51,    51,    51,    52,    52,    54,    54,    54,    55,
      56,    57,    58,    58,    58,    62,    62,    65,    66,    67,
      68,    69,    70,    71,    72,    73,    74,    75,    76,    77,
      78,    82,    82,    82,    82,    83,    84,    84,    85,    85,
      87,    88,    89,    90,    91,    92,    93,    94,    95,    96,
      97,    98,    99,   100,   101,   102,   103,   107,   108,   109,
     110,   113,   114,   114,   114,   114,   114,   114,   114,   114,
     115,   115,   117,   118,   119,   120,   121,   122,   123,   124,
     125,   128,   129,   130,   131,   134,   134,   136,   137,   138,
     139,   140,   141,   142,   143,   144,   145,   146,   147,   148,
     152,   153,   154,   155,   156,   158,   158,   158,   159,   161,
     161,   162,   164,   164,   166,   167,   168,   169,   173,   174,
     175,   176,   177,   178,   179,   180,   181,   182,   183,   184,
     185,   193,   193,   194,   194,   194,   194,   196,   196,   196,
     196,   197,   197,   198,   198,   199,   199,   199,   199,   199,
     199,   202,   202,   202,   202,   205,   207,   207,   210,   211,
     212,   213,   214,   215,   216,   217,   218,   219,   220,   221,
     222,   223,   224,   225,   226,   227,   232,   237,   237,   237,
     237,   238,   238,   239,   239,   240,   240,   240,   245,   246,
     247,   248,   249,   250,   251,   252,   253,   254,   255,   256,
     257,   258,   259,   260,   261,   262,   263,   264,   265,   266,
     267,   268,   269,   270,   271,   272,   273,   274,   275,   276,
     277,   278,   279,   280,   281,   282,   283,   287,   287,   288,
     288,   290,   293,   294,   296,   297,   298,   298,   299,   300,
     300,   301,   301,   302,   302,   303,   303,   304,   304,   305,
     305,   307,   307,   308,   308,   311,   311,   311,   311,   311,
     311,   313,   313,   315,   315,   315,   316,   318,   318,   318,
     318,   318,   318,   318,   318,   318,   318,   318,   318,   320,
     320,   320,   320,   320,   320,   320,   320,   320,   320,   320,
     320,   320,   322,   323,   323,   325,   326,   327,   332,   333,
     334,   335,   335,   335,   335,   335,   335,   339,   340,   341,
     342,   343,   344,   345,   345,   345,   345,   345,   345,   346,
     347,   348,   349,   350,   351,   352,   353,   354,   355,   356,
     357,   358,   359,   360,   361,   362,   363,   364,   365,   366,
     367,   368,   369,   370,   371,   372,   373,   374,   375,   376,
     377,   378,   379,   380,   381,   382,   383,   384,   385,   386,
     387
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

#define YYPACT_NINF (-502)

#define yypact_value_is_default(Yyn) \
  ((Yyn) == YYPACT_NINF)

#define YYTABLE_NINF (-214)

#define yytable_value_is_error(Yyn) \
  0

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
static const yytype_int16 yypact[] =
{
      87,    62,    99,    77,    87,  -502,  -502,  -502,   199,    82,
    1847,  -502,  -502,  -502,   -17,    71,  -502,   -26,  3398,    28,
    -502,   -54,  -502,  -502,  -502,  -502,  -502,  -502,  -502,    74,
    -502,  1847,  1847,  1847,  1847,  1847,  1847,  1847,  1847,  1068,
    1847,  1847,  -502,  5274,    34,  -502,   375,   337,   201,   133,
     258,  -502,    16,  3398,    80,    63,   124,   221,  -502,  -502,
    -502,  -502,   261,  -502,  -502,  2684,    64,   270,    38,    12,
    2684,    39,   275,    56,  3782,  -502,  -502,  -502,  -502,  2684,
     181,   194,   306,  3398,  -502,  -502,  -502,  -502,  -502,  -502,
    -502,  -502,  -502,  -502,  -502,  -502,  -502,    14,    41,   320,
    1847,  1847,  -502,   204,  1847,  -502,  -502,  -502,  -502,  -502,
    -502,  -502,  4531,   229,   121,  -502,  3120,  -502,  -502,  1847,
    1847,  1847,  1847,  1847,  1847,  1847,  1847,  1847,  1847,  1847,
    1847,  1847,  1847,  1847,  1847,  1847,  1847,  1847,  1847,  1847,
    1847,  1847,  1847,  1847,  1847,   233,    45,   377,  -502,   267,
    -502,  -502,  -502,  -502,   383,  -502,  -502,  -502,  -502,  -502,
     283,   371,   265,   401,  1847,    46,   415,   128,   153,  1847,
     422,   204,   196,   368,    66,    10,    95,  -502,   329,  -502,
    -502,  -502,   340,   346,   195,    10,    14,   261,   261,  2105,
     357,  1847,   459,   386,   412,   418,  2684,   427,   439,  2684,
     471,  1847,  1847,   453,   487,  1847,    94,  2180,  -502,  -502,
    -502,  -502,  -502,    13,   474,  1847,   387,   162,  -502,    12,
     178,    12,   246,    12,   373,  -502,   209,  -502,   514,   436,
     272,   452,  -502,   -21,  -502,  3243,   481,   482,   483,   261,
    -502,  -502,  -502,  -502,  -502,  -502,  -502,  -502,  3494,  -502,
    -502,  -502,  -502,  2684,    23,  -502,  -502,   446,   261,    78,
    -502,   318,   604,    48,   606,   280,  5274,  2910,  -502,  -502,
    4596,  -502,  -502,  1068,  -502,  -502,  3079,  5307,   163,   163,
     163,   183,   183,  -502,  2735,  2735,  2735,  5241,   592,  2735,
    1189,   335,   335,   335,   183,   183,   225,   225,   163,  -502,
    -502,  -502,  1847,   484,   608,   486,  -502,    61,  -502,  -502,
    -502,   519,  -502,  5208,   136,    50,  -502,   883,  -502,   491,
    -502,  -502,  -502,   974,   285,   -40,  -502,   204,  -502,  -502,
    -502,  1847,  -502,  -502,  -502,  -502,  -502,  -502,  -502,  -502,
     489,    10,   490,   492,  -502,    10,  1847,   261,  -502,  1434,
    -502,   500,   493,   261,   503,   504,  -502,   612,  -502,  2243,
    1847,  3780,   508,  1847,  1847,  1847,  -502,    40,  1847,  2306,
     510,  3276,  3817,  1847,   512,  1956,  -502,  -502,  -502,  1102,
    -502,  -502,  1504,  1504,  1574,   289,  1847,  -502,   270,   399,
     270,  -502,   406,   270,  -502,   444,   270,   371,  2084,   291,
     634,   371,  2084,  1847,  -502,    56,   635,  3590,  1847,  1847,
      10,   515,  -502,  -502,  -502,   185,   261,  -502,   109,  1847,
     516,  -502,   640,   448,   521,    78,   456,    52,  -502,  -502,
    1847,  1847,  1847,  1847,  -502,  -502,  -502,  1847,  5274,  1847,
     523,  1847,  -502,  -502,  -502,  -502,  -502,  -502,  -502,  -502,
    -502,  -502,  -502,   519,  -502,  -502,   644,   528,    33,   293,
    -502,   301,  1574,  -502,   650,   307,  -502,   338,   530,   107,
     533,  -502,  -502,   352,   368,   532,  1847,  1847,  -502,  5274,
    -502,   535,   362,  1847,  -502,   536,  -502,  -502,  2684,  -502,
    -502,  4633,  -502,  -502,  4698,  4735,  4800,    10,   458,  4837,
    -502,  -502,  1847,  -502,  4902,  -502,  -502,  -502,  1847,  1847,
     106,  -502,  5274,  1847,  3882,  1847,  3919,   363,   366,   538,
    5274,  -502,  -502,   460,  -502,   463,  -502,   466,   370,    42,
     647,    14,   261,   261,   261,  2084,  -502,  2369,   371,  2084,
     539,   381,  2084,   607,  5274,  -502,  3782,  -502,  4939,  5004,
     468,  -502,   261,   541,   542,  -502,   545,  5274,  -502,   540,
    -502,  1847,  -502,   548,  -502,   334,   470,   670,  5274,  2948,
    3015,  3053,  5274,  5274,  1847,  5274,  -502,  -502,  -502,    67,
    -502,   552,   549,   553,   391,   395,   557,  -502,   551,  -502,
    -502,   561,   404,   549,  -502,   563,  1847,  3984,  4021,  -502,
     564,  4086,  -502,  2432,  2684,  1650,  1847,  1847,   565,  1847,
    2684,  4123,  2684,  5274,  5274,  -502,  -502,  -502,  1102,  4188,
    -502,  4225,  -502,   567,   569,  -502,  -502,  -502,  -502,   570,
     261,   137,   436,   436,   576,    53,   158,   583,   587,  -502,
    2495,  -502,   416,  2084,   631,   450,   590,   657,  -502,  3686,
    3782,  1726,  1847,   588,   261,   714,  -502,  4290,  -502,  -502,
    -502,   421,   594,  -502,  -502,  -502,  5274,  1777,   718,  -502,
    -502,  -502,   598,   599,  1847,  -502,  -502,   600,   423,  -502,
    4327,  -502,  -502,  -502,  -502,  -502,   687,   626,  1152,  -502,
     678,   -55,  1229,  1306,  1847,  4392,  -502,  -502,  -502,  -502,
    -502,  -502,  -502,  -502,  2084,   609,  -502,   610,   261,   436,
     438,   123,   611,   728,   494,   614,  -502,  -502,  -502,   616,
     676,  -502,    14,   261,  2084,  2084,  -502,  -502,   698,   639,
    1383,  -502,   691,   -30,  4429,   740,   617,   620,  -502,  -502,
    -502,  -502,  5041,   615,  -502,  -502,  5106,  -502,   624,  -502,
    2684,  2558,  -502,  -502,   699,  -502,  2621,  -502,   700,  -502,
     702,  4494,    10,  2084,   703,  -502,  -502,   630,   752,   636,
     498,   642,  -502,  2084,  -502,   645,    53,   161,   708,  2084,
     710,  3782,  2778,  -502,  -502,   707,  -502,  2874,    10,   646,
     768,  -502,  -502,   652,  -502,  -502,  -502,  -502,  -502,  -502,
    -502,  -502,  -502,  -502,    10,   434,   716,  -502,  -502,   651,
    -502,  -502,  2084,   720,  -502,   653,  -502,  -502,   721,  -502,
    -502,  -502,  -502,  -502,  -502,  -502,   437,  -502,   654,  1847,
     442,  2684,  -502,  -502,   724,  -502,  -502,  -502,  3782,  -502,
    5143,  2684,  -502,  -502,  -502,  -502,  -502
};

/* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
   Performed when YYTABLE does not specify something else to do.  Zero
   means the default is an error.  */
static const yytype_int16 yydefact[] =
{
       0,     0,     0,     0,     2,     4,     5,     6,     0,     0,
      42,    41,     1,     3,     0,     0,    11,     0,    26,     0,
     318,   317,   323,   324,   325,   326,   327,   328,   320,   321,
     319,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   361,    43,     0,    22,   277,   278,   279,     0,
       0,    15,     0,    26,     0,     0,   290,   291,   289,   300,
     301,   292,     0,   293,   294,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   297,   298,   299,    40,     0,
       0,     0,     0,    26,    38,    35,    27,    28,    36,    37,
      32,    33,    34,    29,    30,    31,    39,     0,     0,     0,
       0,     0,   329,   332,     0,   366,   368,   367,   363,   365,
     364,   362,     0,     0,     0,   304,   306,   369,   370,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    10,     0,
     123,   281,   288,   284,   280,   282,   287,   285,   283,    13,
       0,     0,    16,     0,     0,     0,     0,     0,     0,     0,
       0,   265,     0,     0,     0,     0,     0,   247,     0,   270,
     295,   296,   272,     0,   265,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   163,   234,
     231,   232,   233,     0,     0,     0,     0,     0,   120,     0,
       0,     0,     0,     0,     0,    45,     0,    81,     0,    80,
       0,     0,   240,     0,   238,     0,     0,     0,     0,   297,
     179,   171,   172,   173,   174,   175,   176,   178,     0,   167,
     177,   180,   162,     0,     0,     8,    25,     0,     0,    46,
      49,     0,     0,     0,     0,     0,   262,     0,   330,   331,
       0,   360,   307,     0,   302,   305,   345,   346,   351,   350,
     352,   354,   355,   344,   347,   348,   349,     0,   340,   339,
     341,   356,   357,   358,   342,   343,   334,   336,   353,   335,
     337,   338,     0,     0,     0,     0,     9,     0,   286,    12,
      14,     0,    18,     0,    17,     0,     7,     0,   130,     0,
     156,   158,   157,     0,     0,     0,   266,   269,   148,   149,
     150,     0,    72,    73,    74,    75,    76,    77,    78,    79,
       0,     0,     0,     0,    67,     0,     0,     0,    53,     0,
     230,     0,     0,     0,     0,     0,   199,     0,   264,     0,
       0,     0,     0,     0,     0,     0,   200,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   189,   188,   187,     0,
     216,   164,     0,     0,     0,     0,     0,   118,     0,     0,
       0,   110,     0,     0,   115,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   241,     0,     0,     0,     0,     0,
       0,     0,   165,   166,   161,     0,     0,    50,     0,     0,
       0,    54,     0,   272,     0,    46,     0,     0,    44,   359,
       0,     0,     0,     0,   276,   322,   303,     0,   127,     0,
       0,     0,   122,   308,   311,   312,   313,   314,   315,   316,
     310,   309,    23,     0,    19,    20,     0,     0,     0,     0,
     142,     0,     0,   160,     0,     0,   152,     0,     0,     0,
       0,   267,   268,     0,     0,     0,     0,     0,   246,   248,
     271,     0,     0,     0,   212,     0,   210,   211,     0,   198,
     263,     0,   209,   217,     0,     0,     0,     0,     0,     0,
     202,   218,     0,   214,     0,   236,   228,   229,     0,     0,
       0,   194,   197,     0,     0,     0,     0,     0,     0,     0,
     121,   119,   111,     0,   112,     0,   116,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    96,     0,     0,     0,
       0,     0,     0,     0,   239,   237,     0,   168,     0,     0,
       0,   170,     0,     0,     0,    51,     0,    47,    61,    46,
      48,     0,    62,     0,    55,    46,     0,     0,   261,     0,
       0,     0,   333,   125,     0,   124,    24,    21,   128,     0,
     143,     0,     0,     0,     0,     0,   154,   159,     0,   155,
     136,     0,     0,     0,   147,     0,     0,     0,     0,   219,
       0,     0,   213,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   195,   196,   191,   190,   192,     0,     0,
     205,     0,   203,     0,     0,   131,   114,   113,   117,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    95,
       0,    83,     0,     0,     0,     0,     0,     0,    92,     0,
       0,     0,     0,     0,     0,     0,    52,     0,    58,    59,
      56,     0,     0,   274,   275,   273,   126,     0,     0,   133,
     141,   135,     0,     0,     0,   151,   129,     0,     0,    71,
       0,    70,    68,   220,   235,   201,   207,     0,     0,   250,
       0,     0,     0,     0,     0,     0,   245,   215,   244,   193,
     206,   204,   134,   132,     0,     0,   104,     0,     0,     0,
      97,   272,     0,     0,   108,     0,    98,    99,    82,     0,
       0,    86,     0,     0,     0,     0,    91,   169,   181,     0,
       0,   252,     0,     0,     0,     0,     0,     0,    63,    60,
      57,   145,     0,     0,   139,   140,     0,   137,     0,    69,
       0,     0,   221,   249,     0,   223,     0,   224,     0,   226,
       0,     0,     0,     0,     0,   107,   105,     0,     0,     0,
     100,     0,   109,     0,    85,     0,     0,     0,     0,     0,
       0,     0,     0,   183,   251,     0,   185,     0,     0,     0,
       0,    66,   144,     0,   153,   138,   208,   258,   257,   222,
     254,   253,   225,   227,     0,     0,     0,    87,   106,     0,
     101,   102,     0,     0,    97,     0,   108,    84,     0,    93,
     182,   260,   259,   184,   256,   255,     0,    65,     0,     0,
       0,     0,    88,   103,     0,    89,   100,    94,     0,    64,
       0,     0,   242,    90,   186,   146,   243
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -502,  -502,  -502,   779,  -502,  -502,   767,  -383,   625,    11,
    -502,   359,    22,  -414,  -252,    55,   187,  -502,   311,  -502,
    -502,  -502,  -396,  -501,   189,   190,   191,   -56,   400,  -502,
     480,   193,  -374,   207,  -154,  -502,   202,   694,   208,  -502,
    -230,  -247,  -502,    21,  -502,  -502,   175,   155,  -502,   389,
     -18,  -502,  -502,  -502,  -358,  -329,    -3,  -502,  -362,    69,
    -346,    70,   -78,  -196,   -13,   316,   414,   -14,   -11,  -502,
     111,  -502,   524,   343,    -8
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
       0,     3,     4,     5,     6,    17,    18,    50,    51,    82,
      83,    84,   240,   260,   261,   241,   242,   174,   340,   228,
      88,    89,   535,   536,   243,   244,   245,   217,   218,   149,
     150,   246,   459,   460,   175,   465,   466,   170,   247,    95,
     248,   249,   250,   224,   618,   510,   511,   358,   233,   234,
     209,   210,   211,   212,   176,   177,   688,   730,   689,   731,
     690,   732,   691,   359,   213,   183,   326,   327,    97,    98,
      42,   114,   115,   452,   266
};

/* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule whose
   number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
      96,   413,    43,   369,    52,   407,   542,   103,   560,   498,
     517,   426,   220,   222,   528,   171,   478,   216,   541,   182,
     341,   162,   265,   105,   106,   107,   108,   109,   110,   111,
     112,   116,   117,   118,   639,    96,   415,   163,   579,   145,
      85,   639,   178,   216,   226,   171,   259,   182,   382,   756,
     303,   314,   550,   425,   219,   455,   251,   565,   711,   404,
     227,   231,   497,   630,   166,    96,   145,     8,   171,   214,
     100,   171,   430,    86,   787,    85,    45,    12,   101,    46,
      47,    48,   146,   147,   469,   167,   207,    19,   584,   269,
       1,   324,   164,   267,   256,   592,   270,   430,    15,   376,
      16,   253,   232,     9,    10,    85,   405,    44,    86,   146,
     147,   276,   277,   278,   279,   280,   281,   282,   283,   284,
     285,   286,   287,   288,   289,   290,   291,   292,   293,   294,
     295,   296,   297,   298,   299,   300,   301,   385,    86,    39,
     180,   383,   639,   643,   164,    11,   164,    99,   164,   615,
      52,   580,   416,   662,     2,   642,   313,   320,   321,   148,
     413,   342,   343,   389,   168,   392,   179,   395,   608,    39,
     164,   164,   351,   164,   164,   566,   179,   164,   164,   377,
     164,   179,   164,   361,   164,   164,   172,   173,   215,   172,
     179,   667,    39,   371,   372,    39,    49,   375,   104,   668,
     328,   329,   537,   168,   169,    87,   419,    90,    91,    92,
     164,    93,   378,   158,   121,   122,   123,   251,   379,   678,
     208,   344,   345,   639,   272,   225,    94,   275,   513,   515,
     251,   616,   591,   617,   252,   555,   322,   181,   458,   461,
      87,   164,    90,    91,    92,   467,    93,   126,   273,   724,
     347,   274,   317,   473,   318,   164,   121,   122,   123,   159,
     164,    94,   639,   706,   453,   116,   182,   126,   164,   164,
      87,   482,    90,    91,    92,   216,    93,   323,   639,   330,
     230,   142,   143,   144,   714,   179,   179,   816,   387,   388,
     164,    94,   603,   164,   438,   254,   179,   139,   140,   141,
     179,   142,   143,   144,   391,   388,   518,   179,   763,   126,
     179,   639,   255,   472,   552,   206,   649,   164,   179,   349,
     331,   350,    14,    15,   264,    16,   753,   101,   475,   779,
     753,   753,   178,   397,   523,   398,   101,   525,   479,   640,
     527,   141,   754,   142,   143,   144,   758,   760,   154,   155,
     156,   366,   491,   157,   178,   494,   495,   496,    39,     7,
     499,   302,   381,     7,   179,   504,   121,   122,   123,   124,
     125,   512,   394,   388,   514,   516,    45,   812,   520,    46,
      47,    48,   305,   160,   585,   161,    52,   151,   152,   251,
      52,   153,   306,   311,   307,   544,   401,   178,   402,   308,
     548,   549,   413,   728,   805,   429,   312,   430,   414,   309,
     468,   557,   430,   257,   519,   538,   430,   539,   581,   126,
     582,   316,   568,   569,   570,   571,   583,   325,   430,   572,
     826,   573,   587,   575,   588,   102,   332,   333,   334,   335,
     336,   337,   338,   339,   421,   422,   830,   137,   138,   139,
     140,   141,   179,   142,   143,   144,   179,   346,   529,   530,
     659,   722,   419,   589,   362,   430,   165,   347,   597,   598,
     179,   723,   348,   533,   534,   601,   370,   594,   179,   430,
     179,   360,   221,   223,   178,   229,   179,   600,   623,   430,
     582,   624,   374,   430,   611,   629,  -212,   161,  -212,   380,
     613,   614,   352,   354,   355,   619,   646,   621,   161,   179,
     363,   258,   263,   179,   490,   386,   672,   268,   582,   399,
     673,   179,   430,   443,   490,   522,   388,    52,   251,   677,
     507,   582,   524,   388,   820,   822,   364,   444,   445,   446,
     825,   719,   365,   161,   447,   448,   449,   739,   748,   419,
     582,   367,  -210,   657,  -210,   411,  -213,   543,  -213,   831,
     304,   345,   838,   368,   345,   450,   666,   841,   164,   345,
     526,   388,   417,   733,   418,   347,   561,   373,   424,   315,
     403,   319,   564,   422,   609,   345,   626,   388,   680,   627,
     388,   844,   628,   388,   652,   345,   660,   422,   384,   179,
     353,   695,   451,   692,   693,   408,   409,   410,   179,   423,
     512,   428,   439,   440,   441,   462,   474,   488,   476,   484,
     477,   119,   120,   121,   122,   123,   124,   125,   483,   486,
     487,   251,   251,   390,   493,   393,   501,   396,   505,   540,
     546,   551,   558,   400,   734,   559,   179,   562,   179,   577,
     179,   574,   733,   179,   578,   586,   590,   593,   633,   742,
     596,   599,   602,   480,   625,   645,   746,   648,   419,   485,
     654,   656,   655,   420,   658,   661,   126,   427,   669,   671,
     458,   674,   464,   127,   128,   129,   761,   676,   679,   721,
     683,   694,   490,   702,   644,   703,   704,   647,   132,   133,
     134,   135,   710,   136,   137,   138,   139,   140,   141,   716,
     142,   143,   144,   717,   179,   179,   725,   726,   735,   737,
     740,   179,   743,   179,   744,   745,   747,   750,   454,   456,
     751,   755,   554,   771,   774,   765,   766,   770,   781,   470,
     772,   471,   773,   782,   786,   789,   791,   790,   793,   178,
     795,   179,   799,   802,   179,   803,   808,   809,   490,   686,
     823,   807,   810,   251,   251,   696,   817,   698,   811,   251,
     819,   814,   827,   828,   832,   178,   829,   833,   835,   836,
     839,   837,   843,    13,    53,   595,   310,   442,   521,   670,
     675,   178,   262,   699,   545,   490,   576,   436,   720,   784,
     785,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   179,     0,     0,     0,     0,
     251,   840,     0,     0,     0,     0,     0,     0,     0,   553,
       0,     0,   556,     0,     0,   179,   179,     0,     0,   563,
       0,   567,     0,     0,     0,   631,     0,   634,   636,   637,
     638,     0,     0,     0,     0,     0,     0,     0,     0,   764,
       0,   179,   179,     0,     0,     0,     0,   179,   653,     0,
       0,     0,     0,   179,   179,     0,     0,     0,     0,   778,
     780,     0,     0,     0,   179,     0,     0,    20,    21,     0,
     179,     0,     0,     0,     0,     0,     0,     0,     0,   179,
       0,    22,    23,    24,     0,   796,   798,     0,    25,    26,
      27,   801,     0,     0,     0,   179,     0,     0,   806,     0,
       0,     0,     0,   179,     0,     0,     0,     0,   813,    28,
       0,     0,     0,     0,   818,     0,     0,     0,     0,     0,
       0,     0,   179,   632,     0,   635,   705,     0,     0,     0,
      29,   712,   179,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    30,   834,     0,     0,
     736,     0,     0,     0,    31,    32,    33,     0,    20,    21,
       0,     0,     0,     0,     0,     0,   842,     0,    34,    35,
      36,     0,    22,    23,    24,     0,   846,     0,    37,    25,
      26,    27,     0,     0,     0,     0,     0,    38,   457,     0,
       0,     0,    39,     0,   458,     0,     0,     0,    40,    41,
      28,     0,     0,     0,   767,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   775,   777,
       0,    29,     0,     0,     0,   707,   708,   709,     0,   713,
     715,     0,     0,     0,     0,     0,     0,    30,     0,     0,
       0,     0,     0,     0,     0,    31,    32,    33,     0,     0,
       0,     0,    20,    21,     0,     0,     0,     0,     0,    34,
      35,    36,     0,     0,     0,     0,    22,    23,    24,    37,
       0,     0,   815,    25,    26,    27,     0,     0,    38,   463,
       0,     0,     0,    39,     0,   464,    20,    21,     0,    40,
      41,     0,     0,     0,    28,     0,     0,     0,     0,     0,
      22,    23,    24,   768,     0,   769,     0,    25,    26,    27,
       0,     0,     0,     0,     0,    29,   776,     0,     0,     0,
       0,     0,     0,   508,   509,     0,     0,     0,    28,     0,
       0,    30,     0,     0,     0,     0,    20,    21,     0,    31,
      32,    33,     0,     0,     0,     0,     0,     0,     0,    29,
      22,    23,    24,    34,    35,    36,   113,    25,    26,    27,
       0,     0,     0,    37,     0,    30,     0,     0,     0,     0,
     713,   715,    38,    31,    32,    33,     0,    39,    28,     0,
       0,     0,     0,    40,    41,   752,   687,    34,    35,    36,
       0,     0,     0,     0,     0,     0,     0,    37,   119,    29,
     121,   122,   123,   124,   125,     0,    38,     0,     0,     0,
       0,    39,     0,    20,    21,    30,     0,    40,    41,     0,
       0,     0,     0,    31,    32,    33,     0,    22,    23,    24,
       0,     0,     0,     0,    25,    26,    27,    34,    35,    36,
       0,     0,     0,     0,     0,     0,     0,    37,     0,     0,
       0,     0,     0,   126,     0,    28,    38,     0,     0,     0,
       0,    39,   757,   687,     0,     0,     0,    40,    41,     0,
       0,     0,     0,     0,     0,     0,    29,   134,   135,     0,
     136,   137,   138,   139,   140,   141,     0,   142,   143,   144,
      20,    21,    30,     0,     0,     0,     0,     0,     0,     0,
      31,    32,    33,     0,    22,    23,    24,     0,     0,     0,
       0,    25,    26,    27,    34,    35,    36,     0,     0,     0,
       0,     0,     0,     0,    37,     0,     0,     0,     0,     0,
       0,     0,    28,    38,     0,     0,     0,     0,    39,   759,
     687,     0,     0,     0,    40,    41,     0,     0,     0,     0,
       0,     0,     0,    29,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    20,    21,    30,
       0,     0,     0,     0,     0,     0,     0,    31,    32,    33,
       0,    22,    23,    24,     0,     0,     0,     0,    25,    26,
      27,    34,    35,    36,     0,     0,     0,     0,     0,     0,
       0,    37,     0,     0,     0,     0,     0,     0,     0,    28,
      38,     0,     0,     0,     0,    39,   783,   729,    20,    21,
       0,    40,    41,     0,     0,     0,     0,     0,     0,     0,
      29,     0,    22,    23,    24,     0,     0,     0,     0,    25,
      26,    27,     0,     0,     0,     0,    30,     0,     0,     0,
       0,     0,     0,     0,    31,    32,    33,     0,     0,     0,
      28,     0,     0,     0,     0,     0,     0,     0,    34,    35,
      36,     0,     0,     0,     0,     0,     0,     0,    37,     0,
       0,    29,     0,     0,     0,     0,     0,    38,    20,    21,
       0,     0,    39,     0,     0,     0,     0,    30,    40,    41,
       0,     0,    22,    23,    24,    31,    32,    33,     0,    25,
      26,    27,     0,     0,     0,     0,     0,     0,     0,    34,
      35,    36,     0,     0,     0,     0,     0,     0,     0,    37,
      28,     0,     0,     0,     0,     0,     0,     0,    38,   481,
       0,     0,     0,    39,     0,     0,     0,     0,     0,    40,
      41,    29,     0,     0,     0,     0,     0,     0,    20,    21,
       0,     0,     0,     0,     0,     0,     0,    30,     0,     0,
       0,     0,    22,    23,    24,    31,    32,    33,     0,    25,
      26,    27,     0,     0,     0,     0,     0,     0,     0,    34,
      35,    36,     0,     0,     0,     0,     0,     0,     0,    37,
      28,     0,     0,     0,     0,     0,     0,   172,    38,     0,
       0,     0,     0,    39,     0,     0,     0,     0,     0,    40,
      41,    29,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    20,    21,     0,    30,     0,     0,
       0,     0,     0,     0,     0,    31,    32,    33,    22,    23,
      24,     0,     0,     0,     0,    25,    26,    27,     0,    34,
      35,    36,     0,     0,     0,     0,     0,     0,     0,    37,
       0,     0,     0,     0,     0,     0,    28,     0,    38,     0,
       0,     0,     0,    39,   687,   458,     0,     0,     0,    40,
      41,     0,     0,     0,     0,     0,     0,    29,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      20,    21,     0,    30,     0,     0,     0,     0,     0,     0,
       0,    31,    32,    33,    22,    23,    24,     0,     0,     0,
       0,    25,    26,    27,     0,    34,    35,    36,     0,     0,
       0,     0,     0,     0,     0,    37,     0,     0,     0,     0,
       0,     0,    28,     0,    38,     0,     0,     0,     0,    39,
     729,    20,    21,     0,     0,    40,    41,     0,     0,     0,
       0,     0,     0,    29,     0,    22,    23,    24,     0,     0,
       0,     0,    25,    26,    27,     0,     0,     0,     0,    30,
       0,     0,     0,     0,     0,     0,     0,    31,    32,    33,
       0,     0,     0,    28,     0,     0,     0,     0,     0,     0,
       0,    34,    35,    36,     0,     0,     0,     0,     0,     0,
       0,    37,     0,     0,    29,     0,     0,     0,     0,     0,
      38,    20,    21,     0,     0,    39,     0,     0,     0,     0,
      30,    40,    41,     0,     0,    22,    23,    24,    31,    32,
      33,     0,    25,    26,    27,     0,     0,     0,     0,     0,
       0,     0,    34,    35,    36,     0,     0,     0,     0,     0,
       0,     0,    37,    28,     0,     0,     0,     0,     0,     0,
       0,    38,   741,     0,     0,     0,    39,     0,     0,     0,
       0,     0,    40,    41,    29,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      30,     0,     0,     0,     0,     0,     0,     0,    31,    32,
      33,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    34,    35,    36,     0,     0,     0,     0,     0,
       0,   184,    37,   185,     0,     0,     0,   186,     0,     0,
       0,    38,     0,     0,     0,     0,    39,   187,   188,     0,
       0,     0,    40,    41,     0,   119,   120,   121,   122,   123,
     124,   125,     0,   189,     0,   190,     0,     0,     0,     0,
     191,   192,     0,     0,     0,     0,   193,   194,   195,     0,
       0,     0,   196,     0,     0,     0,     0,   197,   198,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   199,     0,   200,    73,     0,     0,     0,     0,
     126,     0,     0,     0,     0,   201,   202,   127,   128,   129,
     203,     0,     0,     0,   204,     0,     0,     0,     0,   130,
       0,   131,   132,   133,   134,   135,     0,   136,   137,   138,
     139,   140,   141,     0,   142,   143,   144,     0,     0,   205,
       0,     0,   506,     0,     0,    39,     0,     0,     0,   184,
     206,   185,   529,   530,     0,   531,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   532,   188,   533,   534,     0,
     184,     0,   185,     0,     0,     0,   186,     0,     0,     0,
       0,   189,     0,   190,     0,     0,   187,   188,   191,   192,
       0,     0,     0,     0,   193,   194,   195,     0,     0,     0,
     196,     0,   189,   356,   190,   197,   198,     0,     0,   191,
     192,     0,     0,     0,     0,   193,   194,   195,     0,     0,
     199,   196,   200,    73,     0,     0,   197,   198,     0,     0,
       0,     0,     0,   201,   202,     0,     0,     0,   203,     0,
       0,   199,   204,   200,    73,   184,     0,   185,     0,     0,
       0,   186,     0,     0,   201,   202,     0,     0,     0,   203,
       0,   187,   188,   204,     0,     0,     0,   205,     0,   357,
       0,     0,     0,    39,     0,     0,     0,   189,   206,   190,
       0,     0,     0,     0,   191,   192,     0,     0,   205,     0,
     193,   194,   195,     0,    39,     0,   196,     0,     0,   206,
       0,   197,   198,     0,     0,     0,     0,     0,   184,     0,
     185,     0,     0,     0,   186,     0,   199,     0,   200,    73,
       0,     0,     0,     0,   187,   188,     0,     0,     0,   201,
     202,     0,     0,     0,   203,     0,     0,     0,   204,     0,
     189,   489,   190,     0,     0,     0,     0,   191,   192,     0,
       0,     0,     0,   193,   194,   195,     0,     0,     0,   196,
       0,     0,     0,   205,   197,   198,   380,     0,     0,    39,
       0,   184,     0,   185,   206,     0,     0,   186,     0,   199,
       0,   200,    73,     0,     0,     0,     0,   187,   188,     0,
       0,     0,   201,   202,     0,     0,     0,   203,     0,     0,
       0,   204,     0,   189,     0,   190,     0,     0,     0,     0,
     191,   192,     0,     0,     0,     0,   193,   194,   195,     0,
       0,     0,   196,     0,     0,     0,   205,   197,   198,     0,
       0,     0,    39,     0,   184,     0,   185,   206,     0,     0,
     186,     0,   199,   500,   200,    73,     0,     0,     0,     0,
     187,   188,     0,     0,     0,   201,   202,     0,     0,     0,
     203,     0,     0,     0,   204,     0,   189,     0,   190,     0,
       0,     0,     0,   191,   192,     0,     0,     0,     0,   193,
     194,   195,     0,     0,     0,   196,     0,   641,     0,   205,
     197,   198,     0,     0,     0,    39,     0,   184,     0,   185,
     206,     0,     0,   186,     0,   199,     0,   200,    73,     0,
       0,     0,     0,   187,   188,     0,     0,     0,   201,   202,
       0,     0,     0,   203,     0,     0,     0,   204,     0,   189,
     685,   190,     0,     0,     0,     0,   191,   192,     0,     0,
       0,     0,   193,   194,   195,     0,     0,     0,   196,     0,
       0,     0,   205,   197,   198,     0,     0,     0,    39,     0,
     184,     0,   185,   206,     0,     0,   186,     0,   199,     0,
     200,    73,     0,     0,     0,     0,   187,   188,     0,     0,
       0,   201,   202,     0,     0,     0,   203,     0,     0,     0,
     204,     0,   189,     0,   190,     0,     0,     0,     0,   191,
     192,     0,     0,     0,     0,   193,   194,   195,     0,     0,
       0,   196,     0,   718,     0,   205,   197,   198,     0,     0,
       0,    39,     0,   184,     0,   185,   206,     0,     0,   186,
       0,   199,     0,   200,    73,     0,     0,     0,     0,   187,
     188,     0,     0,     0,   201,   202,     0,     0,     0,   203,
       0,     0,     0,   204,     0,   189,     0,   190,     0,     0,
       0,     0,   191,   192,     0,     0,     0,     0,   193,   194,
     195,     0,     0,     0,   196,     0,     0,     0,   205,   197,
     198,     0,     0,     0,    39,     0,   184,     0,   185,   206,
       0,     0,   186,     0,   199,     0,   200,    73,     0,     0,
       0,     0,   187,   188,     0,     0,     0,   201,   202,     0,
       0,     0,   203,     0,     0,     0,   204,     0,   189,     0,
     190,     0,     0,     0,     0,   191,   192,     0,     0,     0,
       0,   193,   194,   195,     0,     0,     0,   196,     0,     0,
       0,   205,   197,   198,   797,     0,     0,    39,     0,   184,
       0,   185,   206,     0,     0,   186,     0,   199,     0,   200,
      73,     0,     0,     0,     0,   187,   188,     0,     0,     0,
     201,   202,     0,     0,     0,   203,     0,     0,     0,   204,
       0,   189,     0,   190,     0,     0,     0,     0,   191,   192,
       0,     0,     0,     0,   193,   194,   195,     0,     0,     0,
     196,     0,     0,     0,   205,   197,   198,   800,     0,     0,
      39,     0,     0,     0,     0,   206,     0,     0,     0,     0,
     199,     0,   200,    73,   119,     0,   121,   122,   123,   124,
     125,     0,     0,   201,   202,     0,     0,     0,   203,     0,
       0,     0,   204,    54,     0,    55,    46,    47,    48,    56,
      57,    58,    59,    60,    61,    62,     0,     0,     0,    63,
       0,    64,     0,     0,     0,     0,     0,   205,     0,     0,
       0,     0,     0,    39,    65,   235,     0,   236,   206,   126,
       0,    66,     0,     0,     0,    67,    68,    69,   237,     0,
       0,     0,     0,    70,     0,     0,     0,     0,     0,   238,
       0,     0,   133,   134,   135,     0,   136,   137,   138,   139,
     140,   141,     0,   142,   143,   144,     0,    73,     0,     0,
       0,     0,     0,     0,     0,     0,   239,     0,     0,     0,
       0,     0,     0,    76,    77,     0,     0,    79,    80,    54,
      81,    55,    46,    47,    48,    56,    57,    58,    59,    60,
      61,    62,     0,     0,     0,    63,     0,    64,     0,     0,
       0,     0,     0,     0,   821,     0,     0,     0,     0,     0,
      65,   235,     0,   236,     0,     0,     0,    66,     0,     0,
       0,    67,    68,    69,   237,     0,     0,     0,     0,    70,
       0,     0,     0,     0,     0,   238,     0,     0,     0,   119,
     120,   121,   122,   123,   124,   125,     0,     0,     0,     0,
       0,     0,     0,    73,     0,     0,     0,     0,     0,     0,
       0,     0,   239,     0,     0,     0,     0,     0,     0,    76,
      77,     0,     0,    79,    80,     0,    81,   119,   120,   121,
     122,   123,   124,   125,     0,     0,     0,     0,     0,     0,
       0,   431,   432,     0,   126,     0,     0,     0,     0,     0,
     824,   127,   128,   129,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   130,   433,   131,   132,   133,   134,   135,
       0,   136,   137,   138,   139,   140,   141,     0,   142,   143,
     144,     0,   126,     0,     0,     0,     0,     0,     0,   127,
     128,   129,     0,   434,   119,   120,   121,   122,   123,   124,
     125,   130,     0,   131,   132,   133,   134,   135,     0,   136,
     137,   138,   139,   140,   141,     0,   142,   143,   144,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   663,   119,   120,   121,   122,   123,   124,   125,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   126,
       0,     0,     0,     0,     0,     0,   127,   128,   129,     0,
     121,   122,   123,   124,   125,     0,     0,     0,   130,     0,
     131,   132,   133,   134,   135,     0,   136,   137,   138,   139,
     140,   141,     0,   142,   143,   144,     0,   126,     0,     0,
       0,     0,     0,     0,   127,   128,   129,     0,   664,   119,
     120,   121,   122,   123,   124,   125,   130,     0,   131,   132,
     133,   134,   135,   126,   136,   137,   138,   139,   140,   141,
       0,   142,   143,   144,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   665,   134,   135,     0,
     136,   137,   138,   139,   140,   141,     0,   142,   143,   144,
       0,     0,     0,     0,   126,     0,     0,     0,     0,     0,
       0,   127,   128,   129,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   130,     0,   131,   132,   133,   134,   135,
       0,   136,   137,   138,   139,   140,   141,     0,   142,   143,
     144,     0,     0,     0,     0,     0,     0,     0,    54,    39,
      55,    46,    47,    48,    56,    57,    58,    59,    60,    61,
      62,     0,     0,     0,    63,     0,    64,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    65,
     235,     0,   236,     0,     0,     0,    66,     0,     0,     0,
      67,    68,    69,   237,     0,     0,     0,     0,    70,     0,
       0,     0,     0,     0,   238,   119,   120,   121,   122,   123,
     124,   125,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    73,     0,     0,     0,     0,     0,     0,     0,
       0,   239,     0,     0,     0,     0,     0,     0,    76,    77,
       0,     0,    79,    80,     0,    81,     0,   406,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     126,     0,     0,     0,     0,     0,     0,   127,   128,   129,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   130,
       0,   131,   132,   133,   134,   135,     0,   136,   137,   138,
     139,   140,   141,     0,   142,   143,   144,     0,     0,     0,
       0,     0,     0,    54,   502,    55,    46,    47,    48,    56,
      57,    58,    59,    60,    61,    62,     0,     0,     0,    63,
       0,    64,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    65,     0,     0,     0,     0,     0,
       0,    66,     0,     0,     0,    67,    68,    69,     0,     0,
       0,     0,     0,    70,     0,    71,     0,    72,     0,     0,
       0,     0,     0,     0,     0,     2,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    73,     0,     0,
       0,     0,     0,     0,    74,     0,    75,     0,     0,     0,
       0,     0,     0,    76,    77,    78,     0,    79,    80,    54,
      81,    55,    46,    47,    48,    56,    57,    58,    59,    60,
      61,    62,     0,     0,     0,    63,     0,    64,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      65,   235,     0,   236,     0,     0,     0,    66,     0,     0,
       0,    67,    68,    69,   237,     0,     0,     0,     0,    70,
       0,     0,     0,     0,     0,   238,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    73,     0,     0,     0,     0,     0,     0,
       0,   412,   239,     0,     0,     0,     0,     0,     0,    76,
      77,     0,     0,    79,    80,    54,    81,    55,    46,    47,
      48,    56,    57,    58,    59,    60,    61,    62,     0,     0,
       0,    63,     0,    64,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    65,   235,   547,   236,
       0,     0,     0,    66,     0,     0,     0,    67,    68,    69,
     237,     0,     0,     0,     0,    70,     0,     0,     0,     0,
       0,   238,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    73,
       0,     0,     0,     0,     0,     0,     0,     0,   239,     0,
       0,     0,     0,     0,     0,    76,    77,     0,     0,    79,
      80,    54,    81,    55,    46,    47,    48,    56,    57,    58,
      59,    60,    61,    62,     0,     0,     0,    63,     0,    64,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    65,   235,   727,   236,     0,     0,     0,    66,
       0,     0,     0,    67,    68,    69,   237,     0,     0,     0,
       0,    70,     0,     0,     0,     0,     0,   238,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    73,     0,     0,     0,     0,
       0,     0,     0,     0,   239,     0,     0,     0,     0,     0,
       0,    76,    77,     0,     0,    79,    80,    54,    81,    55,
      46,    47,    48,    56,    57,    58,    59,    60,    61,    62,
       0,     0,     0,    63,     0,    64,     0,     0,     0,   119,
     120,   121,   122,   123,   124,   125,     0,     0,    65,   235,
       0,   236,     0,     0,     0,    66,     0,     0,     0,    67,
      68,    69,   237,     0,     0,     0,     0,    70,     0,     0,
       0,     0,     0,   238,     0,     0,   119,   120,   121,   122,
     123,   124,   125,     0,     0,     0,     0,     0,     0,     0,
       0,    73,     0,     0,   126,     0,     0,     0,     0,     0,
     239,   127,   128,   129,     0,     0,     0,    76,    77,     0,
       0,    79,    80,   130,    81,   131,   132,   133,   134,   135,
       0,   136,   137,   138,   139,   140,   141,     0,   142,   143,
     144,   126,     0,     0,     0,     0,   492,     0,   127,   128,
     129,   119,   120,   121,   122,   123,   124,   125,     0,     0,
     130,     0,   131,   132,   133,   134,   135,     0,   136,   137,
     138,   139,   140,   141,     0,   142,   143,   144,     0,     0,
       0,     0,     0,   503,     0,     0,     0,     0,   119,   120,
     121,   122,   123,   124,   125,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   126,     0,     0,     0,
       0,     0,     0,   127,   128,   129,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   130,     0,   131,   132,   133,
     134,   135,     0,   136,   137,   138,   139,   140,   141,     0,
     142,   143,   144,   126,     0,     0,     0,     0,   620,     0,
     127,   128,   129,   119,   120,   121,   122,   123,   124,   125,
       0,     0,   130,     0,   131,   132,   133,   134,   135,     0,
     136,   137,   138,   139,   140,   141,     0,   142,   143,   144,
       0,     0,     0,     0,     0,   622,     0,     0,     0,     0,
     119,   120,   121,   122,   123,   124,   125,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   126,     0,
       0,     0,     0,     0,     0,   127,   128,   129,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   130,     0,   131,
     132,   133,   134,   135,     0,   136,   137,   138,   139,   140,
     141,     0,   142,   143,   144,   126,     0,     0,     0,     0,
     681,     0,   127,   128,   129,   119,   120,   121,   122,   123,
     124,   125,     0,     0,   130,     0,   131,   132,   133,   134,
     135,     0,   136,   137,   138,   139,   140,   141,     0,   142,
     143,   144,     0,     0,     0,     0,     0,   682,     0,     0,
       0,     0,   119,   120,   121,   122,   123,   124,   125,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     126,     0,     0,     0,     0,     0,     0,   127,   128,   129,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   130,
       0,   131,   132,   133,   134,   135,     0,   136,   137,   138,
     139,   140,   141,     0,   142,   143,   144,   126,     0,     0,
       0,     0,   684,     0,   127,   128,   129,   119,   120,   121,
     122,   123,   124,   125,     0,     0,   130,     0,   131,   132,
     133,   134,   135,     0,   136,   137,   138,   139,   140,   141,
       0,   142,   143,   144,     0,     0,     0,     0,     0,   697,
       0,     0,     0,     0,   119,   120,   121,   122,   123,   124,
     125,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   126,     0,     0,     0,     0,     0,     0,   127,
     128,   129,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   130,     0,   131,   132,   133,   134,   135,     0,   136,
     137,   138,   139,   140,   141,     0,   142,   143,   144,   126,
       0,     0,     0,     0,   700,     0,   127,   128,   129,   119,
     120,   121,   122,   123,   124,   125,     0,     0,   130,     0,
     131,   132,   133,   134,   135,     0,   136,   137,   138,   139,
     140,   141,     0,   142,   143,   144,     0,     0,     0,     0,
       0,   701,     0,     0,     0,     0,   119,   120,   121,   122,
     123,   124,   125,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   126,     0,     0,     0,     0,     0,
       0,   127,   128,   129,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   130,     0,   131,   132,   133,   134,   135,
       0,   136,   137,   138,   139,   140,   141,     0,   142,   143,
     144,   126,     0,     0,     0,     0,   738,     0,   127,   128,
     129,   119,   120,   121,   122,   123,   124,   125,     0,     0,
     130,     0,   131,   132,   133,   134,   135,     0,   136,   137,
     138,   139,   140,   141,     0,   142,   143,   144,     0,     0,
       0,     0,     0,   749,     0,     0,     0,     0,   119,   120,
     121,   122,   123,   124,   125,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   126,     0,     0,     0,
       0,     0,     0,   127,   128,   129,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   130,     0,   131,   132,   133,
     134,   135,     0,   136,   137,   138,   139,   140,   141,     0,
     142,   143,   144,   126,     0,     0,     0,     0,   762,     0,
     127,   128,   129,   119,   120,   121,   122,   123,   124,   125,
       0,     0,   130,     0,   131,   132,   133,   134,   135,     0,
     136,   137,   138,   139,   140,   141,     0,   142,   143,   144,
       0,     0,     0,     0,     0,   788,     0,     0,     0,     0,
     119,   120,   121,   122,   123,   124,   125,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   126,     0,
       0,     0,     0,     0,     0,   127,   128,   129,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   130,     0,   131,
     132,   133,   134,   135,     0,   136,   137,   138,   139,   140,
     141,     0,   142,   143,   144,   126,     0,     0,     0,     0,
     804,     0,   127,   128,   129,   119,   120,   121,   122,   123,
     124,   125,     0,     0,   130,     0,   131,   132,   133,   134,
     135,     0,   136,   137,   138,   139,   140,   141,     0,   142,
     143,   144,     0,     0,     0,     0,   271,     0,     0,     0,
       0,     0,   119,   120,   121,   122,   123,   124,   125,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     126,     0,     0,     0,     0,     0,     0,   127,   128,   129,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   130,
       0,   131,   132,   133,   134,   135,     0,   136,   137,   138,
     139,   140,   141,     0,   142,   143,   144,   126,     0,     0,
       0,   435,     0,     0,   127,   128,   129,   119,   120,   121,
     122,   123,   124,   125,     0,     0,   130,     0,   131,   132,
     133,   134,   135,     0,   136,   137,   138,   139,   140,   141,
       0,   142,   143,   144,     0,     0,     0,     0,   604,     0,
       0,     0,     0,     0,   119,   120,   121,   122,   123,   124,
     125,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   126,     0,     0,     0,     0,     0,     0,   127,
     128,   129,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   130,     0,   131,   132,   133,   134,   135,     0,   136,
     137,   138,   139,   140,   141,     0,   142,   143,   144,   126,
       0,     0,     0,   605,     0,     0,   127,   128,   129,   119,
     120,   121,   122,   123,   124,   125,     0,     0,   130,     0,
     131,   132,   133,   134,   135,     0,   136,   137,   138,   139,
     140,   141,     0,   142,   143,   144,     0,     0,     0,     0,
     606,     0,     0,     0,     0,     0,   119,   120,   121,   122,
     123,   124,   125,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   126,     0,     0,     0,     0,     0,
       0,   127,   128,   129,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   130,     0,   131,   132,   133,   134,   135,
       0,   136,   137,   138,   139,   140,   141,     0,   142,   143,
     144,   126,     0,     0,     0,   607,     0,     0,   127,   128,
     129,   119,   120,   121,   122,   123,   124,   125,     0,     0,
     130,     0,   131,   132,   133,   134,   135,     0,   136,   137,
     138,   139,   140,   141,     0,   142,   143,   144,     0,     0,
       0,     0,   610,     0,     0,     0,     0,     0,   119,   120,
     121,   122,   123,   124,   125,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   126,     0,     0,     0,
       0,     0,     0,   127,   128,   129,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   130,     0,   131,   132,   133,
     134,   135,     0,   136,   137,   138,   139,   140,   141,     0,
     142,   143,   144,   126,     0,     0,     0,   612,     0,     0,
     127,   128,   129,   119,   120,   121,   122,   123,   124,   125,
       0,     0,   130,     0,   131,   132,   133,   134,   135,     0,
     136,   137,   138,   139,   140,   141,     0,   142,   143,   144,
       0,     0,     0,     0,   650,     0,     0,     0,     0,     0,
     119,   120,   121,   122,   123,   124,   125,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   126,     0,
       0,     0,     0,     0,     0,   127,   128,   129,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   130,     0,   131,
     132,   133,   134,   135,     0,   136,   137,   138,   139,   140,
     141,     0,   142,   143,   144,   126,     0,     0,     0,   651,
       0,     0,   127,   128,   129,   119,   120,   121,   122,   123,
     124,   125,     0,     0,   130,     0,   131,   132,   133,   134,
     135,     0,   136,   137,   138,   139,   140,   141,     0,   142,
     143,   144,     0,     0,     0,     0,   792,     0,     0,     0,
       0,     0,   119,   120,   121,   122,   123,   124,   125,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     126,     0,     0,     0,     0,     0,     0,   127,   128,   129,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   130,
       0,   131,   132,   133,   134,   135,     0,   136,   137,   138,
     139,   140,   141,     0,   142,   143,   144,   126,     0,     0,
       0,   794,     0,     0,   127,   128,   129,   119,   120,   121,
     122,   123,   124,   125,     0,     0,   130,     0,   131,   132,
     133,   134,   135,     0,   136,   137,   138,   139,   140,   141,
       0,   142,   143,   144,     0,     0,     0,     0,   845,     0,
     119,   120,   121,   122,   123,   124,   125,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   431,
     432,     0,   126,     0,     0,     0,     0,     0,     0,   127,
     128,   129,     0,   119,   120,   121,   122,   123,   124,   125,
       0,   130,   433,   131,   132,   133,   134,   135,     0,   136,
     137,   138,   139,   140,   141,   126,   142,   143,   144,     0,
       0,     0,   127,   128,   129,     0,   119,     0,   121,   122,
     123,   124,   125,     0,   130,   437,   131,   132,   133,   134,
     135,     0,   136,   137,   138,   139,   140,   141,   126,   142,
     143,   144,     0,     0,     0,   127,   128,   129,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   130,     0,   131,
     132,   133,   134,   135,     0,   136,   137,   138,   139,   140,
     141,   126,   142,   143,   144,     0,     0,     0,   127,   128,
     129,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   132,   133,   134,   135,     0,   136,   137,
     138,   139,   140,   141,     0,   142,   143,   144
};

static const yytype_int16 yycheck[] =
{
      18,   248,    10,   199,    15,   235,   402,    21,   422,   367,
     384,   263,    68,    69,   397,     5,   345,     5,   401,     5,
     174,     5,   100,    31,    32,    33,    34,    35,    36,    37,
      38,    39,    40,    41,   535,    53,    13,    21,     5,     5,
      18,   542,    55,     5,     5,     5,     5,     5,    35,   104,
       5,     5,   410,     5,    16,     5,    74,     5,     5,    80,
      21,     5,    22,    21,    53,    83,     5,     5,     5,     5,
     124,     5,   127,    18,   104,    53,     5,     0,   132,     8,
       9,    10,    48,    49,   124,     5,    65,     5,   462,   103,
       3,   169,   132,   101,    83,   469,   104,   127,   124,     5,
     126,    80,    46,     4,     5,    83,   127,   124,    53,    48,
      49,   119,   120,   121,   122,   123,   124,   125,   126,   127,
     128,   129,   130,   131,   132,   133,   134,   135,   136,   137,
     138,   139,   140,   141,   142,   143,   144,   215,    83,   129,
      16,   128,   643,   539,   132,    46,   132,   119,   132,    43,
     161,   118,   129,   567,    67,   538,   164,     4,     5,   125,
     407,   174,   175,   219,   123,   221,    55,   223,   497,   129,
     132,   132,   185,   132,   132,   427,    65,   132,   132,    85,
     132,    70,   132,   191,   132,   132,   123,   124,   124,   123,
      79,   124,   129,   201,   202,   129,   125,   205,   124,   132,
       4,     5,   398,   123,   124,    18,   128,    18,    18,    18,
     132,    18,   118,    12,    31,    32,    33,   235,   124,   593,
      65,   126,   127,   724,   113,    70,    18,   116,   382,   383,
     248,   125,   125,   127,    79,   126,    83,    16,   131,   317,
      53,   132,    53,    53,    53,   323,    53,    84,   127,   645,
     127,   130,   124,   331,   126,   132,    31,    32,    33,   126,
     132,    53,   763,   126,   128,   273,     5,    84,   132,   132,
      83,   349,    83,    83,    83,     5,    83,   124,   779,    83,
       5,   118,   119,   120,   126,   174,   175,   126,   126,   127,
     132,    83,   488,   132,   302,   101,   185,   114,   115,   116,
     189,   118,   119,   120,   126,   127,   384,   196,   704,    84,
     199,   812,     6,   327,   129,   134,   546,   132,   207,   124,
     124,   126,   123,   124,     4,   126,   688,   132,   341,   725,
     692,   693,   345,   124,   390,   126,   132,   393,   346,   535,
     396,   116,   688,   118,   119,   120,   692,   693,    11,    12,
      13,   196,   360,    16,   367,   363,   364,   365,   129,     0,
     368,   128,   207,     4,   253,   373,    31,    32,    33,    34,
      35,   379,   126,   127,   382,   383,     5,   773,   386,     8,
       9,    10,     5,   125,   462,   127,   397,    12,    13,   407,
     401,    16,   125,   128,   127,   403,   124,   410,   126,    16,
     408,   409,   649,   650,   762,   125,     5,   127,   253,   126,
     125,   419,   127,    97,   125,   124,   127,   126,   125,    84,
     127,     6,   430,   431,   432,   433,   125,     5,   127,   437,
     788,   439,   125,   441,   127,    21,    68,    69,    70,    71,
      72,    73,    74,    75,   126,   127,   804,   112,   113,   114,
     115,   116,   341,   118,   119,   120,   345,   128,     8,     9,
     126,    11,   128,   125,     5,   127,    52,   127,   476,   477,
     359,    21,   126,    23,    24,   483,     5,   125,   367,   127,
     369,   124,    68,    69,   497,    71,   375,   125,   125,   127,
     127,   125,     5,   127,   502,   125,    58,   127,    60,   126,
     508,   509,   186,   187,   188,   513,   125,   515,   127,   398,
     124,    97,    98,   402,   359,   128,   125,   103,   127,     5,
     125,   410,   127,     4,   369,   126,   127,   538,   546,   125,
     375,   127,   126,   127,   781,   782,   124,    18,    19,    20,
     787,   125,   124,   127,    25,    26,    27,   126,   125,   128,
     127,   124,    58,   561,    60,   239,    58,   402,    60,   125,
     146,   127,   125,   124,   127,    46,   574,   125,   132,   127,
     126,   127,   126,   651,   258,   127,   128,   124,   262,   165,
     128,   167,   126,   127,   126,   127,   126,   127,   596,   126,
     127,   838,   126,   127,   126,   127,   126,   127,   124,   488,
     186,   609,    83,   606,   607,   124,   124,   124,   497,     5,
     618,     5,   128,     5,   128,   124,   127,     5,   128,   126,
     128,    29,    30,    31,    32,    33,    34,    35,   128,   126,
     126,   649,   650,   219,   126,   221,   126,   223,   126,     5,
       5,   126,   126,   229,   652,     5,   535,   126,   537,     5,
     539,   128,   730,   542,   126,     5,   126,   124,    11,   667,
     128,   126,   126,   347,   126,   126,   674,    60,   128,   353,
     129,   126,   130,   259,   126,     5,    84,   263,   126,   126,
     131,   124,   131,    91,    92,    93,   694,   126,   125,    58,
     126,   126,   537,   126,   539,   126,   126,   542,   106,   107,
     108,   109,   126,   111,   112,   113,   114,   115,   116,   126,
     118,   119,   120,   126,   603,   604,   126,    60,   130,     5,
     126,   610,     4,   612,   126,   126,   126,    40,   314,   315,
     104,    53,   416,     5,    58,   126,   126,   126,    40,   325,
     126,   327,   126,   104,    53,     5,   126,   130,   133,   762,
     126,   640,    53,    53,   643,    53,   126,     5,   603,   604,
      53,    58,   126,   781,   782,   610,    58,   612,   126,   787,
      60,   126,   126,     5,    58,   788,   124,   126,    58,   126,
     126,    60,    58,     4,    17,   474,   161,   307,   388,   582,
     588,   804,    98,   618,   405,   640,   453,   273,   643,   730,
     730,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   704,    -1,    -1,    -1,    -1,
     838,   829,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   415,
      -1,    -1,   418,    -1,    -1,   724,   725,    -1,    -1,   425,
      -1,   427,    -1,    -1,    -1,   529,    -1,   531,   532,   533,
     534,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   704,
      -1,   750,   751,    -1,    -1,    -1,    -1,   756,   552,    -1,
      -1,    -1,    -1,   762,   763,    -1,    -1,    -1,    -1,   724,
     725,    -1,    -1,    -1,   773,    -1,    -1,     4,     5,    -1,
     779,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   788,
      -1,    18,    19,    20,    -1,   750,   751,    -1,    25,    26,
      27,   756,    -1,    -1,    -1,   804,    -1,    -1,   763,    -1,
      -1,    -1,    -1,   812,    -1,    -1,    -1,    -1,   773,    46,
      -1,    -1,    -1,    -1,   779,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   831,   529,    -1,   531,   630,    -1,    -1,    -1,
      67,   635,   841,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    83,   812,    -1,    -1,
     654,    -1,    -1,    -1,    91,    92,    93,    -1,     4,     5,
      -1,    -1,    -1,    -1,    -1,    -1,   831,    -1,   105,   106,
     107,    -1,    18,    19,    20,    -1,   841,    -1,   115,    25,
      26,    27,    -1,    -1,    -1,    -1,    -1,   124,   125,    -1,
      -1,    -1,   129,    -1,   131,    -1,    -1,    -1,   135,   136,
      46,    -1,    -1,    -1,   708,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   722,   723,
      -1,    67,    -1,    -1,    -1,   631,   632,   633,    -1,   635,
     636,    -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    91,    92,    93,    -1,    -1,
      -1,    -1,     4,     5,    -1,    -1,    -1,    -1,    -1,   105,
     106,   107,    -1,    -1,    -1,    -1,    18,    19,    20,   115,
      -1,    -1,   776,    25,    26,    27,    -1,    -1,   124,   125,
      -1,    -1,    -1,   129,    -1,   131,     4,     5,    -1,   135,
     136,    -1,    -1,    -1,    46,    -1,    -1,    -1,    -1,    -1,
      18,    19,    20,   709,    -1,   711,    -1,    25,    26,    27,
      -1,    -1,    -1,    -1,    -1,    67,   722,    -1,    -1,    -1,
      -1,    -1,    -1,    41,    42,    -1,    -1,    -1,    46,    -1,
      -1,    83,    -1,    -1,    -1,    -1,     4,     5,    -1,    91,
      92,    93,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    67,
      18,    19,    20,   105,   106,   107,   108,    25,    26,    27,
      -1,    -1,    -1,   115,    -1,    83,    -1,    -1,    -1,    -1,
     776,   777,   124,    91,    92,    93,    -1,   129,    46,    -1,
      -1,    -1,    -1,   135,   136,    53,    54,   105,   106,   107,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   115,    29,    67,
      31,    32,    33,    34,    35,    -1,   124,    -1,    -1,    -1,
      -1,   129,    -1,     4,     5,    83,    -1,   135,   136,    -1,
      -1,    -1,    -1,    91,    92,    93,    -1,    18,    19,    20,
      -1,    -1,    -1,    -1,    25,    26,    27,   105,   106,   107,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   115,    -1,    -1,
      -1,    -1,    -1,    84,    -1,    46,   124,    -1,    -1,    -1,
      -1,   129,    53,    54,    -1,    -1,    -1,   135,   136,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    67,   108,   109,    -1,
     111,   112,   113,   114,   115,   116,    -1,   118,   119,   120,
       4,     5,    83,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      91,    92,    93,    -1,    18,    19,    20,    -1,    -1,    -1,
      -1,    25,    26,    27,   105,   106,   107,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   115,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    46,   124,    -1,    -1,    -1,    -1,   129,    53,
      54,    -1,    -1,    -1,   135,   136,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    67,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,     4,     5,    83,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    91,    92,    93,
      -1,    18,    19,    20,    -1,    -1,    -1,    -1,    25,    26,
      27,   105,   106,   107,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   115,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    46,
     124,    -1,    -1,    -1,    -1,   129,    53,    54,     4,     5,
      -1,   135,   136,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      67,    -1,    18,    19,    20,    -1,    -1,    -1,    -1,    25,
      26,    27,    -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    91,    92,    93,    -1,    -1,    -1,
      46,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   105,   106,
     107,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   115,    -1,
      -1,    67,    -1,    -1,    -1,    -1,    -1,   124,     4,     5,
      -1,    -1,   129,    -1,    -1,    -1,    -1,    83,   135,   136,
      -1,    -1,    18,    19,    20,    91,    92,    93,    -1,    25,
      26,    27,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   105,
     106,   107,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   115,
      46,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   124,   125,
      -1,    -1,    -1,   129,    -1,    -1,    -1,    -1,    -1,   135,
     136,    67,    -1,    -1,    -1,    -1,    -1,    -1,     4,     5,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,
      -1,    -1,    18,    19,    20,    91,    92,    93,    -1,    25,
      26,    27,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   105,
     106,   107,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   115,
      46,    -1,    -1,    -1,    -1,    -1,    -1,   123,   124,    -1,
      -1,    -1,    -1,   129,    -1,    -1,    -1,    -1,    -1,   135,
     136,    67,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,     4,     5,    -1,    83,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    91,    92,    93,    18,    19,
      20,    -1,    -1,    -1,    -1,    25,    26,    27,    -1,   105,
     106,   107,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   115,
      -1,    -1,    -1,    -1,    -1,    -1,    46,    -1,   124,    -1,
      -1,    -1,    -1,   129,    54,   131,    -1,    -1,    -1,   135,
     136,    -1,    -1,    -1,    -1,    -1,    -1,    67,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
       4,     5,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    91,    92,    93,    18,    19,    20,    -1,    -1,    -1,
      -1,    25,    26,    27,    -1,   105,   106,   107,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   115,    -1,    -1,    -1,    -1,
      -1,    -1,    46,    -1,   124,    -1,    -1,    -1,    -1,   129,
      54,     4,     5,    -1,    -1,   135,   136,    -1,    -1,    -1,
      -1,    -1,    -1,    67,    -1,    18,    19,    20,    -1,    -1,
      -1,    -1,    25,    26,    27,    -1,    -1,    -1,    -1,    83,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    91,    92,    93,
      -1,    -1,    -1,    46,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   105,   106,   107,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   115,    -1,    -1,    67,    -1,    -1,    -1,    -1,    -1,
     124,     4,     5,    -1,    -1,   129,    -1,    -1,    -1,    -1,
      83,   135,   136,    -1,    -1,    18,    19,    20,    91,    92,
      93,    -1,    25,    26,    27,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   105,   106,   107,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   115,    46,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   124,   125,    -1,    -1,    -1,   129,    -1,    -1,    -1,
      -1,    -1,   135,   136,    67,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      83,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    91,    92,
      93,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   105,   106,   107,    -1,    -1,    -1,    -1,    -1,
      -1,     5,   115,     7,    -1,    -1,    -1,    11,    -1,    -1,
      -1,   124,    -1,    -1,    -1,    -1,   129,    21,    22,    -1,
      -1,    -1,   135,   136,    -1,    29,    30,    31,    32,    33,
      34,    35,    -1,    37,    -1,    39,    -1,    -1,    -1,    -1,
      44,    45,    -1,    -1,    -1,    -1,    50,    51,    52,    -1,
      -1,    -1,    56,    -1,    -1,    -1,    -1,    61,    62,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    76,    -1,    78,    79,    -1,    -1,    -1,    -1,
      84,    -1,    -1,    -1,    -1,    89,    90,    91,    92,    93,
      94,    -1,    -1,    -1,    98,    -1,    -1,    -1,    -1,   103,
      -1,   105,   106,   107,   108,   109,    -1,   111,   112,   113,
     114,   115,   116,    -1,   118,   119,   120,    -1,    -1,   123,
      -1,    -1,   126,    -1,    -1,   129,    -1,    -1,    -1,     5,
     134,     7,     8,     9,    -1,    11,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    21,    22,    23,    24,    -1,
       5,    -1,     7,    -1,    -1,    -1,    11,    -1,    -1,    -1,
      -1,    37,    -1,    39,    -1,    -1,    21,    22,    44,    45,
      -1,    -1,    -1,    -1,    50,    51,    52,    -1,    -1,    -1,
      56,    -1,    37,    38,    39,    61,    62,    -1,    -1,    44,
      45,    -1,    -1,    -1,    -1,    50,    51,    52,    -1,    -1,
      76,    56,    78,    79,    -1,    -1,    61,    62,    -1,    -1,
      -1,    -1,    -1,    89,    90,    -1,    -1,    -1,    94,    -1,
      -1,    76,    98,    78,    79,     5,    -1,     7,    -1,    -1,
      -1,    11,    -1,    -1,    89,    90,    -1,    -1,    -1,    94,
      -1,    21,    22,    98,    -1,    -1,    -1,   123,    -1,   104,
      -1,    -1,    -1,   129,    -1,    -1,    -1,    37,   134,    39,
      -1,    -1,    -1,    -1,    44,    45,    -1,    -1,   123,    -1,
      50,    51,    52,    -1,   129,    -1,    56,    -1,    -1,   134,
      -1,    61,    62,    -1,    -1,    -1,    -1,    -1,     5,    -1,
       7,    -1,    -1,    -1,    11,    -1,    76,    -1,    78,    79,
      -1,    -1,    -1,    -1,    21,    22,    -1,    -1,    -1,    89,
      90,    -1,    -1,    -1,    94,    -1,    -1,    -1,    98,    -1,
      37,    38,    39,    -1,    -1,    -1,    -1,    44,    45,    -1,
      -1,    -1,    -1,    50,    51,    52,    -1,    -1,    -1,    56,
      -1,    -1,    -1,   123,    61,    62,   126,    -1,    -1,   129,
      -1,     5,    -1,     7,   134,    -1,    -1,    11,    -1,    76,
      -1,    78,    79,    -1,    -1,    -1,    -1,    21,    22,    -1,
      -1,    -1,    89,    90,    -1,    -1,    -1,    94,    -1,    -1,
      -1,    98,    -1,    37,    -1,    39,    -1,    -1,    -1,    -1,
      44,    45,    -1,    -1,    -1,    -1,    50,    51,    52,    -1,
      -1,    -1,    56,    -1,    -1,    -1,   123,    61,    62,    -1,
      -1,    -1,   129,    -1,     5,    -1,     7,   134,    -1,    -1,
      11,    -1,    76,    77,    78,    79,    -1,    -1,    -1,    -1,
      21,    22,    -1,    -1,    -1,    89,    90,    -1,    -1,    -1,
      94,    -1,    -1,    -1,    98,    -1,    37,    -1,    39,    -1,
      -1,    -1,    -1,    44,    45,    -1,    -1,    -1,    -1,    50,
      51,    52,    -1,    -1,    -1,    56,    -1,    58,    -1,   123,
      61,    62,    -1,    -1,    -1,   129,    -1,     5,    -1,     7,
     134,    -1,    -1,    11,    -1,    76,    -1,    78,    79,    -1,
      -1,    -1,    -1,    21,    22,    -1,    -1,    -1,    89,    90,
      -1,    -1,    -1,    94,    -1,    -1,    -1,    98,    -1,    37,
      38,    39,    -1,    -1,    -1,    -1,    44,    45,    -1,    -1,
      -1,    -1,    50,    51,    52,    -1,    -1,    -1,    56,    -1,
      -1,    -1,   123,    61,    62,    -1,    -1,    -1,   129,    -1,
       5,    -1,     7,   134,    -1,    -1,    11,    -1,    76,    -1,
      78,    79,    -1,    -1,    -1,    -1,    21,    22,    -1,    -1,
      -1,    89,    90,    -1,    -1,    -1,    94,    -1,    -1,    -1,
      98,    -1,    37,    -1,    39,    -1,    -1,    -1,    -1,    44,
      45,    -1,    -1,    -1,    -1,    50,    51,    52,    -1,    -1,
      -1,    56,    -1,    58,    -1,   123,    61,    62,    -1,    -1,
      -1,   129,    -1,     5,    -1,     7,   134,    -1,    -1,    11,
      -1,    76,    -1,    78,    79,    -1,    -1,    -1,    -1,    21,
      22,    -1,    -1,    -1,    89,    90,    -1,    -1,    -1,    94,
      -1,    -1,    -1,    98,    -1,    37,    -1,    39,    -1,    -1,
      -1,    -1,    44,    45,    -1,    -1,    -1,    -1,    50,    51,
      52,    -1,    -1,    -1,    56,    -1,    -1,    -1,   123,    61,
      62,    -1,    -1,    -1,   129,    -1,     5,    -1,     7,   134,
      -1,    -1,    11,    -1,    76,    -1,    78,    79,    -1,    -1,
      -1,    -1,    21,    22,    -1,    -1,    -1,    89,    90,    -1,
      -1,    -1,    94,    -1,    -1,    -1,    98,    -1,    37,    -1,
      39,    -1,    -1,    -1,    -1,    44,    45,    -1,    -1,    -1,
      -1,    50,    51,    52,    -1,    -1,    -1,    56,    -1,    -1,
      -1,   123,    61,    62,   126,    -1,    -1,   129,    -1,     5,
      -1,     7,   134,    -1,    -1,    11,    -1,    76,    -1,    78,
      79,    -1,    -1,    -1,    -1,    21,    22,    -1,    -1,    -1,
      89,    90,    -1,    -1,    -1,    94,    -1,    -1,    -1,    98,
      -1,    37,    -1,    39,    -1,    -1,    -1,    -1,    44,    45,
      -1,    -1,    -1,    -1,    50,    51,    52,    -1,    -1,    -1,
      56,    -1,    -1,    -1,   123,    61,    62,   126,    -1,    -1,
     129,    -1,    -1,    -1,    -1,   134,    -1,    -1,    -1,    -1,
      76,    -1,    78,    79,    29,    -1,    31,    32,    33,    34,
      35,    -1,    -1,    89,    90,    -1,    -1,    -1,    94,    -1,
      -1,    -1,    98,     5,    -1,     7,     8,     9,    10,    11,
      12,    13,    14,    15,    16,    17,    -1,    -1,    -1,    21,
      -1,    23,    -1,    -1,    -1,    -1,    -1,   123,    -1,    -1,
      -1,    -1,    -1,   129,    36,    37,    -1,    39,   134,    84,
      -1,    43,    -1,    -1,    -1,    47,    48,    49,    50,    -1,
      -1,    -1,    -1,    55,    -1,    -1,    -1,    -1,    -1,    61,
      -1,    -1,   107,   108,   109,    -1,   111,   112,   113,   114,
     115,   116,    -1,   118,   119,   120,    -1,    79,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    88,    -1,    -1,    -1,
      -1,    -1,    -1,    95,    96,    -1,    -1,    99,   100,     5,
     102,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      16,    17,    -1,    -1,    -1,    21,    -1,    23,    -1,    -1,
      -1,    -1,    -1,    -1,   126,    -1,    -1,    -1,    -1,    -1,
      36,    37,    -1,    39,    -1,    -1,    -1,    43,    -1,    -1,
      -1,    47,    48,    49,    50,    -1,    -1,    -1,    -1,    55,
      -1,    -1,    -1,    -1,    -1,    61,    -1,    -1,    -1,    29,
      30,    31,    32,    33,    34,    35,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    79,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    88,    -1,    -1,    -1,    -1,    -1,    -1,    95,
      96,    -1,    -1,    99,   100,    -1,   102,    29,    30,    31,
      32,    33,    34,    35,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    81,    82,    -1,    84,    -1,    -1,    -1,    -1,    -1,
     126,    91,    92,    93,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   103,   104,   105,   106,   107,   108,   109,
      -1,   111,   112,   113,   114,   115,   116,    -1,   118,   119,
     120,    -1,    84,    -1,    -1,    -1,    -1,    -1,    -1,    91,
      92,    93,    -1,   133,    29,    30,    31,    32,    33,    34,
      35,   103,    -1,   105,   106,   107,   108,   109,    -1,   111,
     112,   113,   114,   115,   116,    -1,   118,   119,   120,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   133,    29,    30,    31,    32,    33,    34,    35,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    84,
      -1,    -1,    -1,    -1,    -1,    -1,    91,    92,    93,    -1,
      31,    32,    33,    34,    35,    -1,    -1,    -1,   103,    -1,
     105,   106,   107,   108,   109,    -1,   111,   112,   113,   114,
     115,   116,    -1,   118,   119,   120,    -1,    84,    -1,    -1,
      -1,    -1,    -1,    -1,    91,    92,    93,    -1,   133,    29,
      30,    31,    32,    33,    34,    35,   103,    -1,   105,   106,
     107,   108,   109,    84,   111,   112,   113,   114,   115,   116,
      -1,   118,   119,   120,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   133,   108,   109,    -1,
     111,   112,   113,   114,   115,   116,    -1,   118,   119,   120,
      -1,    -1,    -1,    -1,    84,    -1,    -1,    -1,    -1,    -1,
      -1,    91,    92,    93,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   103,    -1,   105,   106,   107,   108,   109,
      -1,   111,   112,   113,   114,   115,   116,    -1,   118,   119,
     120,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     5,   129,
       7,     8,     9,    10,    11,    12,    13,    14,    15,    16,
      17,    -1,    -1,    -1,    21,    -1,    23,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    36,
      37,    -1,    39,    -1,    -1,    -1,    43,    -1,    -1,    -1,
      47,    48,    49,    50,    -1,    -1,    -1,    -1,    55,    -1,
      -1,    -1,    -1,    -1,    61,    29,    30,    31,    32,    33,
      34,    35,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    79,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    88,    -1,    -1,    -1,    -1,    -1,    -1,    95,    96,
      -1,    -1,    99,   100,    -1,   102,    -1,   104,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      84,    -1,    -1,    -1,    -1,    -1,    -1,    91,    92,    93,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   103,
      -1,   105,   106,   107,   108,   109,    -1,   111,   112,   113,
     114,   115,   116,    -1,   118,   119,   120,    -1,    -1,    -1,
      -1,    -1,    -1,     5,   128,     7,     8,     9,    10,    11,
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
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    88,    -1,
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
      -1,    -1,    -1,    21,    -1,    23,    -1,    -1,    -1,    29,
      30,    31,    32,    33,    34,    35,    -1,    -1,    36,    37,
      -1,    39,    -1,    -1,    -1,    43,    -1,    -1,    -1,    47,
      48,    49,    50,    -1,    -1,    -1,    -1,    55,    -1,    -1,
      -1,    -1,    -1,    61,    -1,    -1,    29,    30,    31,    32,
      33,    34,    35,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    79,    -1,    -1,    84,    -1,    -1,    -1,    -1,    -1,
      88,    91,    92,    93,    -1,    -1,    -1,    95,    96,    -1,
      -1,    99,   100,   103,   102,   105,   106,   107,   108,   109,
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
      29,    30,    31,    32,    33,    34,    35,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    81,
      82,    -1,    84,    -1,    -1,    -1,    -1,    -1,    -1,    91,
      92,    93,    -1,    29,    30,    31,    32,    33,    34,    35,
      -1,   103,   104,   105,   106,   107,   108,   109,    -1,   111,
     112,   113,   114,   115,   116,    84,   118,   119,   120,    -1,
      -1,    -1,    91,    92,    93,    -1,    29,    -1,    31,    32,
      33,    34,    35,    -1,   103,   104,   105,   106,   107,   108,
     109,    -1,   111,   112,   113,   114,   115,   116,    84,   118,
     119,   120,    -1,    -1,    -1,    91,    92,    93,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   103,    -1,   105,
     106,   107,   108,   109,    -1,   111,   112,   113,   114,   115,
     116,    84,   118,   119,   120,    -1,    -1,    -1,    91,    92,
      93,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   106,   107,   108,   109,    -1,   111,   112,
     113,   114,   115,   116,    -1,   118,   119,   120
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
     144,   145,   205,   143,     5,     7,    11,    12,    13,    14,
      15,    16,    17,    21,    23,    36,    43,    47,    48,    49,
      55,    57,    59,    79,    86,    88,    95,    96,    97,    99,
     100,   102,   146,   147,   148,   149,   152,   153,   157,   158,
     161,   162,   163,   168,   175,   176,   187,   205,   206,   119,
     124,   132,   203,   204,   124,   211,   211,   211,   211,   211,
     211,   211,   211,   108,   208,   209,   211,   211,   211,    29,
      30,    31,    32,    33,    34,    35,    84,    91,    92,    93,
     103,   105,   106,   107,   108,   109,   111,   112,   113,   114,
     115,   116,   118,   119,   120,     5,    48,    49,   125,   166,
     167,    12,    13,    16,    11,    12,    13,    16,    12,   126,
     125,   127,     5,    21,   132,   203,   146,     5,   123,   124,
     174,     5,   123,   124,   154,   171,   191,   192,   201,   207,
      16,    16,     5,   202,     5,     7,    11,    21,    22,    37,
      39,    44,    45,    50,    51,    52,    56,    61,    62,    76,
      78,    89,    90,    94,    98,   123,   134,   180,   184,   187,
     188,   189,   190,   201,     5,   124,     5,   164,   165,    16,
     164,   203,   164,   203,   180,   184,     5,    21,   156,   203,
       5,     5,    46,   185,   186,    37,    39,    50,    61,    88,
     149,   152,   153,   161,   162,   163,   168,   175,   177,   178,
     179,   187,   184,   180,   101,     6,   146,   202,   203,     5,
     150,   151,   174,   203,     4,   199,   211,   211,   203,   204,
     211,   125,   207,   127,   130,   207,   211,   211,   211,   211,
     211,   211,   211,   211,   211,   211,   211,   211,   211,   211,
     211,   211,   211,   211,   211,   211,   211,   211,   211,   211,
     211,   211,   128,     5,   203,     5,   125,   127,    16,   126,
     145,   128,     5,   211,     5,   203,     6,   124,   126,   203,
       4,     5,    83,   124,   199,     5,   203,   204,     4,     5,
      83,   124,    68,    69,    70,    71,    72,    73,    74,    75,
     155,   171,   201,   201,   126,   127,   128,   127,   126,   124,
     126,   201,   202,   203,   202,   202,    38,   104,   184,   200,
     124,   211,     5,   124,   124,   124,   184,   124,   124,   200,
       5,   211,   211,   124,     5,   211,     5,    85,   118,   124,
     126,   184,    35,   128,   124,   199,   128,   126,   127,   164,
     203,   126,   164,   203,   126,   164,   203,   124,   126,     5,
     203,   124,   126,   128,    80,   127,   104,   177,   124,   124,
     124,   202,    87,   178,   184,    13,   129,   126,   202,   128,
     203,   126,   127,     5,   202,     5,   151,   203,     5,   125,
     127,    81,    82,   104,   133,   125,   209,   104,   211,   128,
       5,   128,   167,     4,    18,    19,    20,    25,    26,    27,
      46,    83,   210,   128,   203,     5,   203,   125,   131,   169,
     170,   199,   124,   125,   131,   172,   173,   199,   125,   124,
     203,   203,   204,   199,   127,   201,   128,   128,   192,   211,
     202,   125,   199,   128,   126,   202,   126,   126,     5,    38,
     184,   211,   126,   126,   211,   211,   211,    22,   191,   211,
      77,   126,   128,   126,   211,   126,   126,   184,    41,    42,
     182,   183,   211,   171,   211,   171,   211,   169,   199,   125,
     211,   165,   126,   164,   126,   164,   126,   164,   144,     8,
       9,    11,    21,    23,    24,   159,   160,   200,   124,   126,
       5,   144,   159,   184,   211,   186,     5,    38,   211,   211,
     191,   126,   129,   203,   202,   126,   203,   211,   126,     5,
     150,   128,   126,   203,   126,     5,   151,   203,   211,   211,
     211,   211,   211,   211,   128,   211,   210,     5,   126,     5,
     118,   125,   127,   125,   169,   199,     5,   125,   127,   125,
     126,   125,   169,   124,   125,   155,   128,   211,   211,   126,
     125,   211,   126,   200,   125,   125,   125,   125,   192,   126,
     125,   211,   125,   211,   211,    43,   125,   127,   181,   211,
     126,   211,   126,   125,   125,   126,   126,   126,   126,   125,
      21,   202,   203,    11,   202,   203,   202,   202,   202,   160,
     200,    58,   144,   159,   184,   126,   125,   184,    60,   177,
     125,   125,   126,   202,   129,   130,   126,   211,   126,   126,
     126,     5,   150,   133,   133,   133,   211,   124,   132,   126,
     170,   126,   125,   125,   124,   173,   126,   125,   169,   125,
     211,   126,   126,   126,   126,    38,   184,    54,   193,   195,
     197,   199,   193,   193,   126,   211,   184,   126,   184,   183,
     126,   126,   126,   126,   126,   202,   126,   203,   203,   203,
     126,     5,   202,   203,   126,   203,   126,   126,    58,   125,
     184,    58,    11,    21,   159,   126,    60,    38,   178,    54,
     194,   196,   198,   199,   211,   130,   202,     5,   126,   126,
     126,   125,   211,     4,   126,   126,   211,   126,   125,   126,
      40,   104,    53,   195,   197,    53,   104,    53,   197,    53,
     197,   211,   126,   159,   184,   126,   126,   202,   203,   203,
     126,     5,   126,   126,    58,   202,   203,   202,   184,   159,
     184,    40,   104,    53,   196,   198,    53,   104,   126,     5,
     130,   126,   125,   133,   125,   126,   184,   126,   184,    53,
     126,   184,    53,    53,   126,   191,   184,    58,   126,     5,
     126,   126,   159,   184,   126,   202,   126,    58,   184,    60,
     178,   126,   178,    53,   126,   178,   191,   126,     5,   124,
     191,   125,    58,   126,   184,    58,   126,    60,   125,   126,
     211,   125,   184,    58,   178,   125,   184
};

/* YYR1[RULE-NUM] -- Symbol kind of the left-hand side of rule RULE-NUM.  */
static const yytype_uint8 yyr1[] =
{
       0,   137,   138,   139,   139,   140,   140,   141,   141,   142,
     142,   143,   143,   143,   144,   144,   145,   145,   145,   145,
     145,   145,   145,   145,   145,   146,   146,   147,   147,   147,
     147,   147,   147,   147,   147,   147,   147,   147,   147,   147,
     147,   148,   148,   148,   148,   149,   150,   150,   151,   151,
     152,   152,   152,   152,   152,   152,   152,   152,   152,   152,
     152,   152,   152,   152,   152,   152,   152,   153,   153,   153,
     153,   154,   155,   155,   155,   155,   155,   155,   155,   155,
     156,   156,   157,   157,   157,   157,   157,   157,   157,   157,
     157,   158,   158,   158,   158,   159,   159,   160,   160,   160,
     160,   160,   160,   160,   160,   160,   160,   160,   160,   160,
     161,   161,   161,   161,   161,   162,   162,   162,   163,   164,
     164,   165,   166,   166,   167,   167,   167,   167,   168,   168,
     168,   168,   168,   168,   168,   168,   168,   168,   168,   168,
     168,   169,   169,   170,   170,   170,   170,   171,   171,   171,
     171,   172,   172,   173,   173,   174,   174,   174,   174,   174,
     174,   175,   175,   175,   175,   176,   177,   177,   178,   178,
     178,   178,   178,   178,   178,   178,   178,   178,   178,   178,
     178,   178,   178,   178,   178,   178,   179,   180,   180,   180,
     180,   181,   181,   182,   182,   183,   183,   183,   184,   184,
     184,   184,   184,   184,   184,   184,   184,   184,   184,   184,
     184,   184,   184,   184,   184,   184,   184,   184,   184,   184,
     184,   184,   184,   184,   184,   184,   184,   184,   184,   184,
     184,   184,   184,   184,   184,   184,   184,   185,   185,   186,
     186,   187,   188,   188,   189,   190,   191,   191,   192,   193,
     193,   194,   194,   195,   195,   196,   196,   197,   197,   198,
     198,   199,   199,   200,   200,   201,   201,   201,   201,   201,
     201,   202,   202,   203,   203,   203,   204,   205,   205,   205,
     205,   205,   205,   205,   205,   205,   205,   205,   205,   206,
     206,   206,   206,   206,   206,   206,   206,   206,   206,   206,
     206,   206,   207,   208,   208,   209,   209,   209,   210,   210,
     210,   210,   210,   210,   210,   210,   210,   211,   211,   211,
     211,   211,   211,   211,   211,   211,   211,   211,   211,   211,
     211,   211,   211,   211,   211,   211,   211,   211,   211,   211,
     211,   211,   211,   211,   211,   211,   211,   211,   211,   211,
     211,   211,   211,   211,   211,   211,   211,   211,   211,   211,
     211,   211,   211,   211,   211,   211,   211,   211,   211,   211,
     211
};

/* YYR2[RULE-NUM] -- Number of symbols on the right-hand side of rule RULE-NUM.  */
static const yytype_int8 yyr2[] =
{
       0,     2,     1,     2,     1,     1,     1,     6,     5,     4,
       3,     1,     4,     3,     3,     1,     2,     3,     3,     4,
       4,     5,     1,     4,     5,     2,     0,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     2,     2,     3,     6,     2,     1,     3,     3,     1,
       3,     4,     5,     3,     3,     4,     5,     6,     5,     5,
       6,     4,     4,     6,     9,     8,     7,     3,     6,     7,
       6,     5,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     6,     5,     8,     7,     6,     8,     9,     9,
      10,     6,     5,     8,     9,     2,     1,     3,     3,     3,
       4,     5,     5,     6,     3,     4,     5,     4,     3,     4,
       3,     4,     4,     5,     5,     3,     4,     5,     3,     3,
       1,     3,     3,     1,     4,     4,     5,     3,     5,     6,
       3,     5,     6,     6,     6,     6,     5,     7,     8,     7,
       7,     3,     1,     2,     5,     4,     8,     4,     2,     2,
       2,     3,     1,     5,     2,     4,     2,     2,     2,     4,
       3,     3,     2,     2,     3,     3,     2,     1,     3,     5,
       3,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     5,     7,     6,     7,     6,     9,     2,     2,     2,
       4,     1,     1,     3,     1,     2,     2,     1,     3,     2,
       2,     5,     3,     4,     5,     4,     5,     5,     7,     3,
       3,     3,     3,     4,     3,     5,     2,     3,     3,     4,
       5,     6,     7,     6,     6,     7,     6,     7,     3,     3,
       2,     1,     1,     1,     1,     5,     3,     3,     1,     3,
       1,     3,     9,    10,     5,     5,     3,     1,     3,     2,
       1,     2,     1,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     1,     2,     1,     1,     2,     3,     3,     2,
       1,     3,     1,     5,     5,     5,     3,     1,     1,     1,
       2,     2,     2,     2,     2,     2,     3,     2,     2,     1,
       1,     1,     1,     1,     1,     2,     2,     1,     1,     1,
       1,     1,     3,     3,     1,     2,     1,     2,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     4,     1,     1,     1,     1,     1,     1,     2,
       3,     3,     2,     5,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     4,
       3,     1,     2,     2,     2,     2,     2,     2,     2,     2,
       2
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

#line 3014 "y.tab.c"

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

#line 391 "yaccs/verilog.yacc"

