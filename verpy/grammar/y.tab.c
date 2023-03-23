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
  YYSYMBOL_real = 22,                      /* real  */
  YYSYMBOL_wreal = 23,                     /* wreal  */
  YYSYMBOL_ubin = 24,                      /* ubin  */
  YYSYMBOL_uhex = 25,                      /* uhex  */
  YYSYMBOL_udig = 26,                      /* udig  */
  YYSYMBOL_domino = 27,                    /* domino  */
  YYSYMBOL_and_and = 28,                   /* and_and  */
  YYSYMBOL_or_or = 29,                     /* or_or  */
  YYSYMBOL_eq3 = 30,                       /* eq3  */
  YYSYMBOL_eq_eq = 31,                     /* eq_eq  */
  YYSYMBOL_not_eq = 32,                    /* not_eq  */
  YYSYMBOL_gr_eq = 33,                     /* gr_eq  */
  YYSYMBOL_sm_eq = 34,                     /* sm_eq  */
  YYSYMBOL_always = 35,                    /* always  */
  YYSYMBOL_begin = 36,                     /* begin  */
  YYSYMBOL_end = 37,                       /* end  */
  YYSYMBOL_if = 38,                        /* if  */
  YYSYMBOL_else = 39,                      /* else  */
  YYSYMBOL_posedge = 40,                   /* posedge  */
  YYSYMBOL_negedge = 41,                   /* negedge  */
  YYSYMBOL_or = 42,                        /* or  */
  YYSYMBOL_wait = 43,                      /* wait  */
  YYSYMBOL_emit = 44,                      /* emit  */
  YYSYMBOL_string = 45,                    /* string  */
  YYSYMBOL_defparam = 46,                  /* defparam  */
  YYSYMBOL_parameter = 47,                 /* parameter  */
  YYSYMBOL_localparam = 48,                /* localparam  */
  YYSYMBOL_case = 49,                      /* case  */
  YYSYMBOL_casez = 50,                     /* casez  */
  YYSYMBOL_casex = 51,                     /* casex  */
  YYSYMBOL_endcase = 52,                   /* endcase  */
  YYSYMBOL_default = 53,                   /* default  */
  YYSYMBOL_initial = 54,                   /* initial  */
  YYSYMBOL_forever = 55,                   /* forever  */
  YYSYMBOL_function = 56,                  /* function  */
  YYSYMBOL_endfunction = 57,               /* endfunction  */
  YYSYMBOL_task = 58,                      /* task  */
  YYSYMBOL_endtask = 59,                   /* endtask  */
  YYSYMBOL_for = 60,                       /* for  */
  YYSYMBOL_while = 61,                     /* while  */
  YYSYMBOL_backtick_define = 62,           /* backtick_define  */
  YYSYMBOL_backtick_include = 63,          /* backtick_include  */
  YYSYMBOL_backtick_timescale = 64,        /* backtick_timescale  */
  YYSYMBOL_backtick_undef = 65,            /* backtick_undef  */
  YYSYMBOL_define = 66,                    /* define  */
  YYSYMBOL_strong1 = 67,                   /* strong1  */
  YYSYMBOL_strong0 = 68,                   /* strong0  */
  YYSYMBOL_pull1 = 69,                     /* pull1  */
  YYSYMBOL_pull0 = 70,                     /* pull0  */
  YYSYMBOL_weak1 = 71,                     /* weak1  */
  YYSYMBOL_weak0 = 72,                     /* weak0  */
  YYSYMBOL_highz1 = 73,                    /* highz1  */
  YYSYMBOL_highz0 = 74,                    /* highz0  */
  YYSYMBOL_fork = 75,                      /* fork  */
  YYSYMBOL_join = 76,                      /* join  */
  YYSYMBOL_disable = 77,                   /* disable  */
  YYSYMBOL_pragma1 = 78,                   /* pragma1  */
  YYSYMBOL_pragma2 = 79,                   /* pragma2  */
  YYSYMBOL_plus_range = 80,                /* plus_range  */
  YYSYMBOL_minus_range = 81,               /* minus_range  */
  YYSYMBOL_floating = 82,                  /* floating  */
  YYSYMBOL_power = 83,                     /* power  */
  YYSYMBOL_star = 84,                      /* star  */
  YYSYMBOL_generate = 85,                  /* generate  */
  YYSYMBOL_endgenerate = 86,               /* endgenerate  */
  YYSYMBOL_genvar = 87,                    /* genvar  */
  YYSYMBOL_force = 88,                     /* force  */
  YYSYMBOL_release = 89,                   /* release  */
  YYSYMBOL_xnor = 90,                      /* xnor  */
  YYSYMBOL_nand = 91,                      /* nand  */
  YYSYMBOL_nor = 92,                       /* nor  */
  YYSYMBOL_repeat = 93,                    /* repeat  */
  YYSYMBOL_supply0 = 94,                   /* supply0  */
  YYSYMBOL_supply1 = 95,                   /* supply1  */
  YYSYMBOL_newver = 96,                    /* newver  */
  YYSYMBOL_return = 97,                    /* return  */
  YYSYMBOL_always_comb = 98,               /* always_comb  */
  YYSYMBOL_enum = 99,                      /* enum  */
  YYSYMBOL_typedef = 100,                  /* typedef  */
  YYSYMBOL_101_ = 101,                     /* '?'  */
  YYSYMBOL_102_ = 102,                     /* ':'  */
  YYSYMBOL_103_ = 103,                     /* '|'  */
  YYSYMBOL_104_ = 104,                     /* '^'  */
  YYSYMBOL_105_ = 105,                     /* '&'  */
  YYSYMBOL_shift_left = 106,               /* shift_left  */
  YYSYMBOL_shift_right = 107,              /* shift_right  */
  YYSYMBOL_SignedLeft = 108,               /* SignedLeft  */
  YYSYMBOL_arith_shift_right = 109,        /* arith_shift_right  */
  YYSYMBOL_110_ = 110,                     /* '<'  */
  YYSYMBOL_111_ = 111,                     /* '>'  */
  YYSYMBOL_112_ = 112,                     /* '+'  */
  YYSYMBOL_113_ = 113,                     /* '-'  */
  YYSYMBOL_noteqeq = 114,                  /* noteqeq  */
  YYSYMBOL_Veryequal = 115,                /* Veryequal  */
  YYSYMBOL_116_ = 116,                     /* '*'  */
  YYSYMBOL_117_ = 117,                     /* '/'  */
  YYSYMBOL_118_ = 118,                     /* '%'  */
  YYSYMBOL_StarStar = 119,                 /* StarStar  */
  YYSYMBOL_UNARY_PREC = 120,               /* UNARY_PREC  */
  YYSYMBOL_121_ = 121,                     /* '#'  */
  YYSYMBOL_122_ = 122,                     /* '('  */
  YYSYMBOL_123_ = 123,                     /* ')'  */
  YYSYMBOL_124_ = 124,                     /* ';'  */
  YYSYMBOL_125_ = 125,                     /* ','  */
  YYSYMBOL_126_ = 126,                     /* '='  */
  YYSYMBOL_127_ = 127,                     /* '{'  */
  YYSYMBOL_128_ = 128,                     /* '}'  */
  YYSYMBOL_129_ = 129,                     /* '.'  */
  YYSYMBOL_130_ = 130,                     /* '['  */
  YYSYMBOL_131_ = 131,                     /* ']'  */
  YYSYMBOL_132_ = 132,                     /* '@'  */
  YYSYMBOL_133_ = 133,                     /* '!'  */
  YYSYMBOL_134_ = 134,                     /* '~'  */
  YYSYMBOL_YYACCEPT = 135,                 /* $accept  */
  YYSYMBOL_Main = 136,                     /* Main  */
  YYSYMBOL_Mains = 137,                    /* Mains  */
  YYSYMBOL_MainItem = 138,                 /* MainItem  */
  YYSYMBOL_Module = 139,                   /* Module  */
  YYSYMBOL_Hparams = 140,                  /* Hparams  */
  YYSYMBOL_Header = 141,                   /* Header  */
  YYSYMBOL_Header_list = 142,              /* Header_list  */
  YYSYMBOL_Header_item = 143,              /* Header_item  */
  YYSYMBOL_Module_stuffs = 144,            /* Module_stuffs  */
  YYSYMBOL_Mstuff = 145,                   /* Mstuff  */
  YYSYMBOL_Define = 146,                   /* Define  */
  YYSYMBOL_Initial = 147,                  /* Initial  */
  YYSYMBOL_OneDef = 148,                   /* OneDef  */
  YYSYMBOL_ManyDefs = 149,                 /* ManyDefs  */
  YYSYMBOL_Definition = 150,               /* Definition  */
  YYSYMBOL_Assign = 151,                   /* Assign  */
  YYSYMBOL_StrengthDef = 152,              /* StrengthDef  */
  YYSYMBOL_Strength = 153,                 /* Strength  */
  YYSYMBOL_WidthInt = 154,                 /* WidthInt  */
  YYSYMBOL_Function = 155,                 /* Function  */
  YYSYMBOL_Task = 156,                     /* Task  */
  YYSYMBOL_Mem_defs = 157,                 /* Mem_defs  */
  YYSYMBOL_Mem_def = 158,                  /* Mem_def  */
  YYSYMBOL_Parameter = 159,                /* Parameter  */
  YYSYMBOL_Localparam = 160,               /* Localparam  */
  YYSYMBOL_Defparam = 161,                 /* Defparam  */
  YYSYMBOL_Pairs = 162,                    /* Pairs  */
  YYSYMBOL_Pair = 163,                     /* Pair  */
  YYSYMBOL_head_params = 164,              /* head_params  */
  YYSYMBOL_head_param = 165,               /* head_param  */
  YYSYMBOL_Instance = 166,                 /* Instance  */
  YYSYMBOL_Conns_list = 167,               /* Conns_list  */
  YYSYMBOL_Connection = 168,               /* Connection  */
  YYSYMBOL_AssignParams = 169,             /* AssignParams  */
  YYSYMBOL_Prms_list = 170,                /* Prms_list  */
  YYSYMBOL_PrmAssign = 171,                /* PrmAssign  */
  YYSYMBOL_InstParams = 172,               /* InstParams  */
  YYSYMBOL_Always = 173,                   /* Always  */
  YYSYMBOL_Generate = 174,                 /* Generate  */
  YYSYMBOL_GenStatements = 175,            /* GenStatements  */
  YYSYMBOL_GenStatement = 176,             /* GenStatement  */
  YYSYMBOL_GenFor_statement = 177,         /* GenFor_statement  */
  YYSYMBOL_When = 178,                     /* When  */
  YYSYMBOL_Or_coma = 179,                  /* Or_coma  */
  YYSYMBOL_When_items = 180,               /* When_items  */
  YYSYMBOL_When_item = 181,                /* When_item  */
  YYSYMBOL_Statement = 182,                /* Statement  */
  YYSYMBOL_pragma_stuffs = 183,            /* pragma_stuffs  */
  YYSYMBOL_pragma_item = 184,              /* pragma_item  */
  YYSYMBOL_Pragma = 185,                   /* Pragma  */
  YYSYMBOL_For_statement = 186,            /* For_statement  */
  YYSYMBOL_Repeat_statement = 187,         /* Repeat_statement  */
  YYSYMBOL_While_statement = 188,          /* While_statement  */
  YYSYMBOL_Soft_assigns = 189,             /* Soft_assigns  */
  YYSYMBOL_Soft_assign = 190,              /* Soft_assign  */
  YYSYMBOL_Cases = 191,                    /* Cases  */
  YYSYMBOL_GenCases = 192,                 /* GenCases  */
  YYSYMBOL_Case = 193,                     /* Case  */
  YYSYMBOL_GenCase = 194,                  /* GenCase  */
  YYSYMBOL_Default = 195,                  /* Default  */
  YYSYMBOL_GenDefault = 196,               /* GenDefault  */
  YYSYMBOL_Exprs = 197,                    /* Exprs  */
  YYSYMBOL_Statements = 198,               /* Statements  */
  YYSYMBOL_LSH = 199,                      /* LSH  */
  YYSYMBOL_Tokens_list = 200,              /* Tokens_list  */
  YYSYMBOL_Width = 201,                    /* Width  */
  YYSYMBOL_BusBit = 202,                   /* BusBit  */
  YYSYMBOL_ExtDir = 203,                   /* ExtDir  */
  YYSYMBOL_IntDir = 204,                   /* IntDir  */
  YYSYMBOL_CurlyList = 205,                /* CurlyList  */
  YYSYMBOL_CurlyItems = 206,               /* CurlyItems  */
  YYSYMBOL_CurlyItem = 207,                /* CurlyItem  */
  YYSYMBOL_Literal = 208,                  /* Literal  */
  YYSYMBOL_Expr = 209                      /* Expr  */
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
#define YYLAST   5227

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  135
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  75
/* YYNRULES -- Number of rules.  */
#define YYNRULES  367
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  833

/* YYMAXUTOK -- Last valid token kind.  */
#define YYMAXUTOK   363


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
       2,     2,     2,   133,     2,   121,     2,   118,   105,     2,
     122,   123,   116,   112,   125,   113,   129,   117,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,   102,   124,
     110,   126,   111,   101,   132,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,   130,     2,   131,   104,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   127,   103,   128,   134,     2,     2,     2,
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
      95,    96,    97,    98,    99,   100,   106,   107,   108,   109,
     114,   115,   119,   120
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
     199,   202,   202,   202,   205,   207,   207,   210,   211,   212,
     213,   214,   215,   216,   217,   218,   219,   220,   221,   222,
     223,   224,   225,   226,   227,   232,   237,   237,   237,   237,
     238,   238,   239,   239,   240,   240,   240,   245,   246,   247,
     248,   249,   250,   251,   252,   253,   254,   255,   256,   257,
     258,   259,   260,   261,   262,   263,   264,   265,   266,   267,
     268,   269,   270,   271,   272,   273,   274,   275,   276,   277,
     278,   279,   280,   281,   282,   286,   286,   287,   287,   289,
     291,   292,   293,   294,   294,   295,   296,   296,   297,   297,
     298,   298,   299,   299,   300,   300,   301,   301,   303,   303,
     304,   304,   307,   307,   307,   307,   307,   307,   309,   309,
     311,   311,   311,   312,   314,   314,   314,   314,   314,   314,
     314,   314,   314,   314,   314,   314,   316,   316,   316,   316,
     316,   316,   316,   316,   316,   316,   316,   316,   316,   318,
     319,   319,   321,   322,   323,   328,   329,   330,   331,   331,
     331,   331,   331,   331,   335,   336,   337,   338,   339,   340,
     341,   341,   341,   341,   341,   341,   342,   343,   344,   345,
     346,   347,   348,   349,   350,   351,   352,   353,   354,   355,
     356,   357,   358,   359,   360,   361,   362,   363,   364,   365,
     366,   367,   368,   369,   370,   371,   372,   373,   374,   375,
     376,   377,   378,   379,   380,   381,   382,   383
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
  "integer", "real", "wreal", "ubin", "uhex", "udig", "domino", "and_and",
  "or_or", "eq3", "eq_eq", "not_eq", "gr_eq", "sm_eq", "always", "begin",
  "end", "if", "else", "posedge", "negedge", "or", "wait", "emit",
  "string", "defparam", "parameter", "localparam", "case", "casez",
  "casex", "endcase", "default", "initial", "forever", "function",
  "endfunction", "task", "endtask", "for", "while", "backtick_define",
  "backtick_include", "backtick_timescale", "backtick_undef", "define",
  "strong1", "strong0", "pull1", "pull0", "weak1", "weak0", "highz1",
  "highz0", "fork", "join", "disable", "pragma1", "pragma2", "plus_range",
  "minus_range", "floating", "power", "star", "generate", "endgenerate",
  "genvar", "force", "release", "xnor", "nand", "nor", "repeat", "supply0",
  "supply1", "newver", "return", "always_comb", "enum", "typedef", "'?'",
  "':'", "'|'", "'^'", "'&'", "shift_left", "shift_right", "SignedLeft",
  "arith_shift_right", "'<'", "'>'", "'+'", "'-'", "noteqeq", "Veryequal",
  "'*'", "'/'", "'%'", "StarStar", "UNARY_PREC", "'#'", "'('", "')'",
  "';'", "','", "'='", "'{'", "'}'", "'.'", "'['", "']'", "'@'", "'!'",
  "'~'", "$accept", "Main", "Mains", "MainItem", "Module", "Hparams",
  "Header", "Header_list", "Header_item", "Module_stuffs", "Mstuff",
  "Define", "Initial", "OneDef", "ManyDefs", "Definition", "Assign",
  "StrengthDef", "Strength", "WidthInt", "Function", "Task", "Mem_defs",
  "Mem_def", "Parameter", "Localparam", "Defparam", "Pairs", "Pair",
  "head_params", "head_param", "Instance", "Conns_list", "Connection",
  "AssignParams", "Prms_list", "PrmAssign", "InstParams", "Always",
  "Generate", "GenStatements", "GenStatement", "GenFor_statement", "When",
  "Or_coma", "When_items", "When_item", "Statement", "pragma_stuffs",
  "pragma_item", "Pragma", "For_statement", "Repeat_statement",
  "While_statement", "Soft_assigns", "Soft_assign", "Cases", "GenCases",
  "Case", "GenCase", "Default", "GenDefault", "Exprs", "Statements", "LSH",
  "Tokens_list", "Width", "BusBit", "ExtDir", "IntDir", "CurlyList",
  "CurlyItems", "CurlyItem", "Literal", "Expr", YY_NULLPTR
};

static const char *
yysymbol_name (yysymbol_kind_t yysymbol)
{
  return yytname[yysymbol];
}
#endif

#define YYPACT_NINF (-486)

#define yypact_value_is_default(Yyn) \
  ((Yyn) == YYPACT_NINF)

#define YYTABLE_NINF (-212)

#define yytable_value_is_error(Yyn) \
  0

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
static const yytype_int16 yypact[] =
{
      74,    64,    54,   101,    74,  -486,  -486,  -486,   131,   143,
    1700,  -486,  -486,  -486,   -28,    62,  -486,    89,  3896,   122,
    -486,   -46,  -486,  -486,  -486,  -486,  -486,  -486,  -486,    96,
    -486,  1700,  1700,  1700,  1700,  1700,  1700,  1700,  1700,  1328,
    1700,  1700,  -486,  5012,    15,  -486,   285,   329,   282,   180,
     141,  -486,    13,  3896,    73,    61,   296,   302,  -486,  -486,
    -486,  -486,   339,  -486,  -486,  2476,    70,   348,    30,    12,
    2476,    32,   371,    55,  4272,  -486,  -486,  -486,  -486,  2476,
     238,   357,  3896,  -486,  -486,  -486,  -486,  -486,  -486,  -486,
    -486,  -486,  -486,  -486,  -486,  -486,    36,    44,   389,  1700,
    1700,  -486,   272,  1700,  -486,  -486,  -486,  -486,  -486,  -486,
    -486,  4270,   278,   200,  -486,  2939,  -486,  -486,  1700,  1700,
    1700,  1700,  1700,  1700,  1700,  1700,  1700,  1700,  1700,  1700,
    1700,  1700,  1700,  1700,  1700,  1700,  1700,  1700,  1700,  1700,
    1700,  1700,  1700,  1700,   284,    37,   420,  -486,   241,  -486,
    -486,  -486,  -486,   424,  -486,  -486,  -486,  -486,  -486,   345,
     365,   322,   447,  1700,    39,   453,    77,    69,  1700,   489,
     272,   102,   360,    59,    49,   103,  -486,   374,  -486,  -486,
    -486,   379,   401,   135,    49,    36,   339,  1954,   421,  1700,
     540,   432,   433,   434,  2476,   436,   437,  2476,   542,  1700,
    1700,   438,   558,  1700,    87,  2028,  -486,  -486,  -486,  -486,
    -486,    71,   443,  1700,   440,   207,  -486,    12,   255,    12,
     260,    12,   444,  -486,   274,  -486,   564,   441,   279,   446,
    -486,    19,  -486,  3097,   451,   452,   454,   339,  -486,  -486,
    -486,  -486,  -486,  -486,  -486,  -486,  3990,  -486,  -486,  -486,
    -486,    25,  -486,  -486,   456,   339,    11,  -486,   388,   565,
      40,   570,   288,  5012,  2731,  -486,  -486,  4306,  -486,  -486,
    1328,  -486,  -486,  1763,  5109,   129,   129,   129,   244,   244,
    -486,   995,   995,   995,  4980,  5077,   995,   635,   800,   800,
     800,   244,   244,   203,   203,   129,  -486,  -486,  -486,  1700,
     455,   573,   457,  -486,    35,  -486,  -486,  -486,   218,  -486,
    4915,   157,    42,  -486,   802,  -486,   460,  -486,  -486,  -486,
     877,   312,   -43,  -486,   272,  -486,  -486,  -486,  1700,  -486,
    -486,  -486,  -486,  -486,  -486,  -486,  -486,   461,    49,   459,
     462,  -486,    49,  1700,   339,  -486,  1383,  -486,   463,   468,
     339,   469,  -486,   582,  -486,  2086,  1700,  3130,   470,  1700,
    1700,  1700,  -486,    49,  1700,  2151,   471,  2977,  3172,  1700,
     472,  1807,  -486,  -486,  -486,   952,  -486,  -486,  1433,  1433,
    1508,   313,  1700,  -486,   348,   391,   348,  -486,   394,   348,
    -486,   396,   348,   365,  1933,   317,   592,   365,  1933,  1700,
    -486,    55,   593,  4084,  1700,  1700,    49,   475,  -486,  -486,
     225,   339,  -486,    72,  1700,   477,  -486,   597,   152,   479,
      11,   399,    47,  -486,  -486,  1700,  1700,  1700,  1700,  -486,
    -486,  -486,  1700,  5012,  1700,   478,  1700,  -486,  -486,  -486,
    -486,  -486,  -486,  -486,  -486,  -486,  -486,  -486,   218,  -486,
    -486,   600,   482,    43,   319,  -486,   320,  1508,  -486,   602,
     324,  -486,   328,   484,    75,   487,  -486,  -486,   331,   360,
     485,  1700,  1700,  -486,  5012,  -486,   490,   332,  1700,  -486,
     491,  -486,  2476,  -486,  -486,  4371,  -486,  -486,  4407,  4472,
    4508,   403,  4573,  -486,  -486,  1700,  -486,  4609,  -486,  -486,
    -486,  1700,  1700,    94,  -486,  5012,  1700,  3237,  1700,  3273,
     335,   341,   492,  5012,  -486,  -486,   407,  -486,   413,  -486,
     415,   342,    34,   606,    36,   339,   339,   339,  1933,  -486,
    2209,   365,  1933,   495,   347,  1933,   562,  5012,  -486,  4272,
    -486,  4674,  4710,   417,  -486,   339,   496,   494,  -486,   502,
    5012,  -486,   501,  -486,  1700,  -486,   504,  -486,   350,   425,
     625,  5012,  2769,  2835,  2873,  5012,  5012,  1700,  5012,  -486,
    -486,  -486,   -33,  -486,   508,   506,   509,   352,   355,   515,
    -486,   510,  -486,  -486,   517,   358,   506,  -486,   519,  1700,
    3338,  3374,  -486,   520,  3439,  -486,  2274,  2476,  1557,  1700,
    1700,  1700,  2476,  3475,  2476,  5012,  5012,  -486,  -486,  -486,
     952,  3540,  -486,  3576,  -486,   521,   522,  -486,  -486,  -486,
    -486,   523,   339,   126,   441,   441,   528,    51,   149,   529,
     530,  -486,  2332,  -486,   359,  1933,   601,   398,   533,   603,
    -486,  4178,  4272,  1647,  1700,   531,   339,   655,  -486,  3641,
    -486,  -486,  -486,   363,   537,  -486,  -486,  -486,  5012,  1697,
     660,  -486,  -486,  -486,   546,   547,  1700,  -486,  -486,   548,
     370,  -486,  3677,  -486,  -486,  -486,  -486,  -486,   634,   572,
    1028,  -486,   624,   -34,  1134,  1188,  3742,  -486,  -486,  -486,
    -486,  -486,  -486,  -486,  -486,  1933,   557,  -486,   559,   339,
     441,   431,   -45,   561,   682,   442,   566,  -486,  -486,  -486,
     567,   631,  -486,    36,   339,  1933,  1933,  -486,  -486,   650,
     591,  1278,  -486,   642,   106,  3778,   690,   568,   575,  -486,
    -486,  -486,  -486,  4775,   569,  -486,  -486,  4811,  -486,   577,
    -486,  2476,  2397,  -486,  -486,   645,  -486,  2455,  -486,   651,
    -486,   654,    49,  1933,   652,  -486,  -486,   578,   702,   584,
     448,   590,  -486,  1933,  -486,   595,    51,   161,   658,  1933,
     657,  4272,  2602,  -486,  -486,   665,  -486,  2696,    49,   596,
     717,  -486,  -486,   604,  -486,  -486,  -486,  -486,  -486,  -486,
    -486,  -486,  -486,  -486,   385,   666,  -486,  -486,   605,  -486,
    -486,  1933,   667,  -486,   609,  -486,  -486,   668,  -486,  -486,
    -486,  -486,  -486,  -486,  -486,   386,  -486,   610,  1700,  2476,
    -486,  -486,   671,  -486,  -486,  -486,  4272,  -486,  4876,  -486,
    -486,  -486,  -486
};

/* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
   Performed when YYTABLE does not specify something else to do.  Zero
   means the default is an error.  */
static const yytype_int16 yydefact[] =
{
       0,     0,     0,     0,     2,     4,     5,     6,     0,     0,
      42,    41,     1,     3,     0,     0,    11,     0,    26,     0,
     315,   314,   320,   321,   322,   323,   324,   325,   317,   318,
     316,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   358,    43,     0,    22,   274,   275,   276,     0,
       0,    15,     0,    26,     0,     0,   287,   288,   286,   297,
     298,   289,     0,   290,   291,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   294,   295,   296,    40,     0,
       0,     0,    26,    38,    35,    27,    28,    36,    37,    32,
      33,    34,    29,    30,    31,    39,     0,     0,     0,     0,
       0,   326,   329,     0,   363,   365,   364,   360,   362,   361,
     359,     0,     0,     0,   301,   303,   366,   367,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    10,     0,   123,
     278,   285,   281,   277,   279,   284,   282,   280,    13,     0,
       0,    16,     0,     0,     0,     0,     0,     0,     0,     0,
     262,     0,     0,     0,     0,     0,   244,     0,   267,   292,
     293,   269,     0,   262,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   162,   232,   229,   230,
     231,     0,     0,     0,     0,     0,   120,     0,     0,     0,
       0,     0,     0,    45,     0,    81,     0,    80,     0,     0,
     238,     0,   236,     0,     0,     0,     0,   294,   178,   170,
     171,   172,   173,   174,   175,   177,     0,   166,   176,   179,
     161,     0,     8,    25,     0,     0,    46,    49,     0,     0,
       0,     0,     0,   259,     0,   327,   328,     0,   357,   304,
       0,   299,   302,   342,   343,   348,   347,   349,   351,   352,
     341,   344,   345,   346,     0,   337,   336,   338,   353,   354,
     355,   339,   340,   331,   333,   350,   332,   334,   335,     0,
       0,     0,     0,     9,     0,   283,    12,    14,     0,    18,
       0,    17,     0,     7,     0,   130,     0,   156,   158,   157,
       0,     0,     0,   263,   266,   148,   149,   150,     0,    72,
      73,    74,    75,    76,    77,    78,    79,     0,     0,     0,
       0,    67,     0,     0,     0,    53,     0,   228,     0,     0,
       0,     0,   198,     0,   261,     0,     0,     0,     0,     0,
       0,     0,   199,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   188,   187,   186,     0,   214,   163,     0,     0,
       0,     0,     0,   118,     0,     0,     0,   110,     0,     0,
     115,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     239,     0,     0,     0,     0,     0,     0,     0,   164,   165,
       0,     0,    50,     0,     0,     0,    54,     0,   269,     0,
      46,     0,     0,    44,   356,     0,     0,     0,     0,   273,
     319,   300,     0,   127,     0,     0,     0,   122,   305,   308,
     309,   310,   311,   312,   313,   307,   306,    23,     0,    19,
      20,     0,     0,     0,     0,   142,     0,     0,   160,     0,
       0,   152,     0,     0,     0,     0,   264,   265,     0,     0,
       0,     0,     0,   243,   245,   268,     0,     0,     0,   210,
       0,   209,     0,   197,   260,     0,   208,   215,     0,     0,
       0,     0,     0,   201,   216,     0,   212,     0,   234,   226,
     227,     0,     0,     0,   193,   196,     0,     0,     0,     0,
       0,     0,     0,   121,   119,   111,     0,   112,     0,   116,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    96,
       0,     0,     0,     0,     0,     0,     0,   237,   235,     0,
     167,     0,     0,     0,   169,     0,     0,     0,    51,     0,
      47,    61,    46,    48,     0,    62,     0,    55,    46,     0,
       0,   258,     0,     0,     0,   330,   125,     0,   124,    24,
      21,   128,     0,   143,     0,     0,     0,     0,     0,   154,
     159,     0,   155,   136,     0,     0,     0,   147,     0,     0,
       0,     0,   217,     0,     0,   211,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   194,   195,   190,   189,   191,
       0,     0,   204,     0,   202,     0,     0,   131,   114,   113,
     117,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    95,     0,    83,     0,     0,     0,     0,     0,     0,
      92,     0,     0,     0,     0,     0,     0,     0,    52,     0,
      58,    59,    56,     0,     0,   271,   272,   270,   126,     0,
       0,   133,   141,   135,     0,     0,     0,   151,   129,     0,
       0,    71,     0,    70,    68,   218,   233,   200,   206,     0,
       0,   247,     0,     0,     0,     0,     0,   242,   213,   241,
     192,   205,   203,   134,   132,     0,     0,   104,     0,     0,
       0,    97,   269,     0,     0,   108,     0,    98,    99,    82,
       0,     0,    86,     0,     0,     0,     0,    91,   168,   180,
       0,     0,   249,     0,     0,     0,     0,     0,     0,    63,
      60,    57,   145,     0,     0,   139,   140,     0,   137,     0,
      69,     0,     0,   219,   246,     0,   221,     0,   222,     0,
     224,     0,     0,     0,     0,   107,   105,     0,     0,     0,
     100,     0,   109,     0,    85,     0,     0,     0,     0,     0,
       0,     0,     0,   182,   248,     0,   184,     0,     0,     0,
       0,    66,   144,     0,   153,   138,   207,   255,   254,   220,
     251,   250,   223,   225,     0,     0,    87,   106,     0,   101,
     102,     0,     0,    97,     0,   108,    84,     0,    93,   181,
     257,   256,   183,   253,   252,     0,    65,     0,     0,     0,
      88,   103,     0,    89,   100,    94,     0,    64,     0,   240,
      90,   185,   146
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -486,  -486,  -486,   726,  -486,  -486,   718,  -382,   576,   -21,
    -486,   311,    86,  -403,  -247,   187,   188,  -486,   268,  -486,
    -486,  -486,  -386,  -485,   208,   214,   240,   -63,   354,  -486,
     458,   253,  -361,   175,  -164,  -486,   178,   659,   254,  -486,
    -231,  -242,  -486,   696,  -486,  -486,   154,    16,  -486,   364,
     -17,  -486,  -486,  -486,  -355,   426,   -47,  -486,  -337,    45,
    -302,    46,   -66,  -194,   -39,   153,   465,   -14,    -5,  -486,
     108,  -486,   500,   323,   -10
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
       0,     3,     4,     5,     6,    17,    18,    50,    51,    81,
      82,    83,   238,   257,   258,   239,   240,   173,   337,   226,
      87,    88,   528,   529,   241,   242,   243,   215,   216,   148,
     149,   244,   454,   455,   174,   460,   461,   169,   245,    94,
     246,   247,   248,   222,   610,   503,   504,   354,   231,   232,
     207,   208,   209,   210,   175,   176,   680,   721,   681,   722,
     682,   723,   683,   355,   211,   182,   323,   324,    96,    97,
      42,   113,   114,   447,   263
};

/* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule whose
   number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
      43,    95,   403,   365,   409,   218,   220,   102,   491,   338,
      52,   521,   535,   421,   553,   534,   177,   214,   161,   510,
     144,   104,   105,   106,   107,   108,   109,   110,   111,   115,
     116,   117,   165,   262,   162,   214,    95,   224,   410,   181,
     144,   181,   300,   631,   311,   420,   217,   450,   572,   256,
     631,   543,   558,   225,   170,   622,   702,   249,     9,    10,
     229,   253,   145,   146,   170,    95,   170,    45,   747,     8,
      46,    47,    48,   317,   318,   212,    99,     1,   166,   464,
     344,   206,   145,   146,   100,   163,   223,   163,   266,   659,
     264,   425,   372,   267,    44,   250,   577,   660,   400,    11,
     230,    12,   321,   585,    84,   378,   325,   326,   273,   274,
     275,   276,   277,   278,   279,   280,   281,   282,   283,   284,
     285,   286,   287,   288,   289,   290,   291,   292,   293,   294,
     295,   296,   297,   298,   339,   340,   607,   414,   147,    84,
       2,   163,   163,   163,   401,   348,   635,   381,    19,   634,
     631,   319,   411,   310,   385,    52,   388,   654,   391,   573,
     163,   409,   163,   178,   163,   167,   163,   163,    84,   163,
     163,   373,   163,   178,   163,   559,    39,   163,   178,   357,
     171,   163,   171,   172,   327,    49,    39,   178,    39,   367,
     368,   320,   213,   371,   167,   168,   548,   379,   584,   314,
     530,   315,   163,   374,   453,    85,    86,   163,   777,   375,
     362,    15,   125,    16,   506,   508,   249,   608,   103,   609,
     269,   377,   438,   272,   328,   670,    89,   341,   342,   249,
     631,   425,    90,   120,   121,   122,   439,   440,   441,    98,
      85,    86,   442,   443,   444,   141,   142,   143,   456,   254,
     697,   715,    14,    15,   462,    16,   163,   346,    91,   347,
     115,    89,   468,   445,   159,   100,   160,    90,   631,    85,
      86,    92,    93,   705,   120,   121,   122,   344,   554,   163,
     477,   178,   178,   448,   631,   805,   125,   163,   596,   433,
      89,   163,   178,    91,   157,   178,    90,   150,   151,   470,
     446,   152,   178,   177,   158,   178,    92,    93,   641,   753,
     467,     7,   179,   178,   511,     7,   631,   140,   180,   141,
     142,   143,    91,   516,   177,   270,   518,   125,   271,   520,
     769,   383,   384,   474,   632,    92,    93,   251,   349,   351,
     153,   154,   155,   744,   181,   156,   485,   744,   744,   488,
     489,   490,   545,   214,   492,   163,   138,   139,   140,   497,
     141,   142,   143,   252,   303,   505,   304,   177,   507,   509,
      45,   484,   513,    46,    47,    48,   228,   801,   745,   387,
     384,   484,   749,   751,   390,   384,   249,   500,    52,   537,
     407,   578,    52,   261,   541,   542,   393,   794,   394,   409,
     719,   397,   100,   398,   550,    39,   522,   523,   413,   713,
     299,   424,   419,   425,   536,   561,   562,   563,   564,   714,
     526,   527,   565,   815,   566,   302,   568,   329,   330,   331,
     332,   333,   334,   335,   336,   463,   512,   425,   425,   531,
     305,   532,   574,   576,   575,   425,   178,   580,   308,   581,
     178,   582,   309,   425,   587,   593,   425,   425,   615,   313,
     575,   590,   591,   178,   616,   621,   425,   160,   594,   306,
     638,   178,   160,   178,   651,   664,   414,   575,   665,   178,
     425,   669,   710,   575,   160,   603,   101,   730,  -210,   414,
    -210,   605,   606,   739,   322,   575,   611,   475,   613,  -209,
     343,  -209,   178,   480,   344,  -211,   178,  -211,   819,   826,
     342,   342,   416,   417,   178,   515,   384,   164,   517,   384,
     519,   384,   249,   557,   417,   345,    52,   601,   342,   809,
     811,   618,   384,   219,   221,   814,   227,   619,   384,   620,
     384,   644,   342,   356,   649,   358,   484,   366,   636,   652,
     417,   639,   684,   685,   359,   360,   361,   658,   363,   364,
     369,   255,   260,   370,   547,   380,   382,   265,   376,   395,
     418,   163,   399,   404,   405,   423,   406,   724,   435,   672,
     412,   434,   457,   436,   831,   471,   469,   482,   472,   478,
     178,   686,   479,   481,   487,   494,   498,   533,   539,   544,
     505,   551,   552,   555,   567,   570,   571,   579,   583,   586,
     301,   589,   484,   678,   592,   595,   617,   625,   687,   637,
     689,   640,   647,   646,   249,   249,   648,   414,   650,   312,
     653,   316,   661,   663,   725,   453,   178,   666,   178,   459,
     178,   668,   671,   178,   675,   693,   694,   695,   484,   733,
     350,   711,   701,   707,   708,   724,   737,   716,   712,   726,
     728,   731,   717,   118,   734,   120,   121,   122,   123,   124,
     735,   736,   738,   741,   742,   623,   746,   626,   628,   629,
     630,   755,   386,   756,   389,   760,   392,   761,   764,   771,
     762,   763,   396,   772,   776,   779,   780,   789,   645,   781,
     783,   785,   797,   792,   178,   178,   793,   798,   799,   796,
     178,   754,   178,   177,   800,   806,   808,   812,   125,   803,
     816,   415,   817,   820,   823,   422,   818,   825,   830,   821,
      13,   768,   770,   824,   827,    53,   307,   588,   514,   177,
     178,   133,   134,   178,   135,   136,   137,   138,   139,   140,
     662,   141,   142,   143,   249,   249,   259,   786,   788,   667,
     249,   205,   437,   791,   690,   538,   774,   775,   473,   795,
     431,   569,     0,     0,     0,   696,   449,   451,     0,   802,
     703,     0,     0,     0,     0,   807,     0,   465,     0,   466,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   727,
       0,     0,     0,   178,     0,     0,    20,    21,   828,   249,
       0,     0,     0,     0,     0,     0,     0,   822,     0,     0,
      22,    23,    24,   178,   178,     0,    25,    26,    27,     0,
     120,   121,   122,   123,   124,   829,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    28,     0,   178,
     178,     0,   757,     0,     0,   178,     0,     0,     0,     0,
     178,   178,     0,     0,     0,     0,   765,   767,    29,     0,
       0,   178,     0,     0,     0,   546,     0,   178,   549,     0,
       0,    20,    21,   125,    30,   556,   178,   560,     0,     0,
       0,     0,    31,    32,    33,    22,    23,    24,     0,     0,
       0,    25,    26,    27,     0,    34,    35,    36,     0,   178,
     136,   137,   138,   139,   140,    37,   141,   142,   143,   804,
       0,     0,    28,     0,    38,   452,     0,   178,     0,    39,
       0,   453,     0,     0,     0,    40,    41,     0,     0,     0,
       0,     0,     0,    29,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    20,    21,     0,    30,
       0,     0,     0,     0,     0,     0,     0,    31,    32,    33,
      22,    23,    24,     0,     0,     0,    25,    26,    27,     0,
      34,    35,    36,     0,     0,     0,     0,   624,     0,   627,
      37,     0,   501,   502,     0,     0,     0,    28,     0,    38,
     458,     0,     0,     0,    39,     0,   459,     0,     0,     0,
      40,    41,     0,     0,     0,     0,     0,     0,    29,     0,
       0,     0,     0,   118,     0,   120,   121,   122,   123,   124,
       0,     0,    20,    21,    30,     0,     0,     0,     0,     0,
       0,     0,    31,    32,    33,     0,    22,    23,    24,     0,
       0,     0,    25,    26,    27,    34,    35,    36,     0,     0,
       0,     0,     0,     0,     0,    37,     0,     0,     0,     0,
       0,     0,     0,    28,    38,     0,     0,     0,   125,    39,
     743,   679,     0,     0,     0,    40,    41,     0,   698,   699,
     700,     0,   704,   706,    29,     0,     0,     0,     0,     0,
     132,   133,   134,     0,   135,   136,   137,   138,   139,   140,
      30,   141,   142,   143,     0,     0,     0,     0,    31,    32,
      33,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    34,    35,    36,     0,     0,     0,     0,    20,    21,
       0,    37,     0,     0,     0,     0,     0,     0,     0,     0,
      38,     0,    22,    23,    24,    39,     0,     0,    25,    26,
      27,    40,    41,     0,     0,   758,     0,   759,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   766,    28,
       0,     0,     0,     0,     0,     0,   748,   679,     0,     0,
       0,     0,    20,    21,     0,     0,     0,     0,     0,     0,
      29,     0,     0,     0,     0,     0,    22,    23,    24,     0,
       0,     0,    25,    26,    27,     0,    30,     0,     0,     0,
       0,     0,     0,     0,    31,    32,    33,     0,     0,     0,
       0,   704,   706,    28,     0,     0,     0,    34,    35,    36,
     750,   679,     0,     0,     0,     0,     0,    37,     0,     0,
       0,     0,     0,     0,    29,     0,    38,     0,     0,     0,
       0,    39,     0,     0,     0,     0,     0,    40,    41,     0,
      30,     0,     0,     0,     0,     0,     0,     0,    31,    32,
      33,     0,    20,    21,     0,     0,     0,     0,     0,     0,
       0,    34,    35,    36,     0,     0,    22,    23,    24,     0,
       0,    37,    25,    26,    27,     0,     0,     0,     0,     0,
      38,     0,     0,     0,     0,    39,     0,     0,     0,     0,
       0,    40,    41,    28,     0,     0,     0,     0,     0,     0,
     773,   720,    20,    21,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    29,     0,    22,    23,    24,     0,
       0,     0,    25,    26,    27,     0,     0,     0,     0,     0,
      30,     0,     0,     0,     0,     0,     0,     0,    31,    32,
      33,     0,     0,    28,     0,     0,     0,     0,     0,     0,
       0,    34,    35,    36,     0,     0,     0,    20,    21,     0,
       0,    37,     0,     0,    29,     0,     0,     0,     0,     0,
      38,    22,    23,    24,     0,    39,     0,    25,    26,    27,
      30,    40,    41,     0,     0,     0,     0,     0,    31,    32,
      33,     0,     0,     0,     0,     0,     0,     0,    28,     0,
       0,    34,    35,    36,   112,     0,     0,    20,    21,     0,
       0,    37,     0,     0,     0,     0,     0,     0,     0,    29,
      38,    22,    23,    24,     0,    39,     0,    25,    26,    27,
       0,    40,    41,     0,     0,    30,     0,     0,     0,     0,
       0,     0,     0,    31,    32,    33,     0,     0,    28,     0,
       0,     0,     0,     0,     0,     0,    34,    35,    36,     0,
       0,     0,     0,     0,     0,     0,    37,     0,     0,    29,
       0,     0,     0,     0,     0,    38,   476,     0,     0,     0,
      39,     0,    20,    21,     0,    30,    40,    41,     0,     0,
       0,     0,     0,    31,    32,    33,    22,    23,    24,     0,
       0,     0,    25,    26,    27,     0,    34,    35,    36,     0,
       0,     0,     0,     0,     0,     0,    37,     0,     0,     0,
       0,     0,     0,    28,   171,    38,     0,     0,     0,     0,
      39,    20,    21,     0,     0,     0,    40,    41,     0,     0,
       0,     0,     0,     0,    29,    22,    23,    24,     0,     0,
       0,    25,    26,    27,     0,     0,     0,     0,     0,     0,
      30,     0,     0,     0,     0,     0,     0,     0,    31,    32,
      33,     0,    28,     0,     0,     0,     0,     0,     0,     0,
     679,    34,    35,    36,     0,     0,     0,     0,     0,     0,
       0,    37,     0,    29,     0,     0,     0,     0,     0,     0,
      38,     0,     0,     0,     0,    39,     0,   453,     0,    30,
       0,    40,    41,     0,     0,     0,     0,    31,    32,    33,
       0,    20,    21,     0,     0,     0,     0,     0,     0,     0,
      34,    35,    36,     0,     0,    22,    23,    24,     0,     0,
      37,    25,    26,    27,     0,     0,     0,     0,     0,    38,
       0,     0,     0,     0,    39,     0,     0,     0,     0,     0,
      40,    41,    28,     0,     0,     0,     0,     0,     0,     0,
     720,    20,    21,     0,    20,    21,     0,     0,     0,     0,
       0,     0,     0,    29,     0,    22,    23,    24,    22,    23,
      24,    25,    26,    27,    25,    26,    27,     0,     0,    30,
       0,     0,     0,     0,     0,     0,     0,    31,    32,    33,
       0,     0,    28,     0,     0,    28,     0,     0,     0,     0,
      34,    35,    36,     0,     0,     0,     0,     0,     0,     0,
      37,     0,     0,    29,     0,     0,    29,     0,     0,    38,
       0,     0,     0,     0,    39,     0,     0,     0,     0,    30,
      40,    41,    30,     0,     0,     0,     0,    31,    32,    33,
      31,    32,    33,   120,   121,   122,   123,   124,     0,     0,
      34,    35,    36,    34,    35,    36,     0,     0,     0,     0,
      37,     0,   183,    37,   184,     0,     0,     0,   185,    38,
     732,     0,    38,     0,    39,     0,     0,    39,   186,     0,
      40,    41,     0,    40,    41,   118,   119,   120,   121,   122,
     123,   124,     0,   187,     0,   188,   125,     0,     0,     0,
     189,   190,     0,     0,     0,     0,   191,   192,   193,     0,
       0,     0,   194,     0,     0,     0,     0,   195,   196,   133,
     134,     0,   135,   136,   137,   138,   139,   140,     0,   141,
     142,   143,   197,     0,   198,    73,     0,     0,     0,     0,
     125,     0,     0,     0,     0,   199,   200,   126,   127,   128,
     201,     0,     0,     0,   202,     0,     0,     0,   129,     0,
     130,   131,   132,   133,   134,     0,   135,   136,   137,   138,
     139,   140,     0,   141,   142,   143,     0,     0,   203,     0,
       0,   499,     0,     0,    39,     0,     0,     0,   183,   204,
     184,   522,   523,     0,   524,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   525,   526,   527,     0,     0,   183,
       0,   184,     0,     0,     0,   185,     0,     0,     0,   187,
       0,   188,     0,     0,     0,   186,   189,   190,     0,     0,
       0,     0,   191,   192,   193,     0,     0,     0,   194,     0,
     187,   352,   188,   195,   196,     0,     0,   189,   190,     0,
       0,     0,     0,   191,   192,   193,     0,     0,   197,   194,
     198,    73,     0,     0,   195,   196,     0,     0,     0,     0,
       0,   199,   200,     0,     0,     0,   201,     0,     0,   197,
     202,   198,    73,   183,     0,   184,     0,     0,     0,   185,
       0,     0,   199,   200,     0,     0,     0,   201,     0,   186,
       0,   202,     0,     0,   203,     0,   353,     0,     0,     0,
      39,     0,     0,     0,   187,   204,   188,     0,     0,     0,
       0,   189,   190,     0,     0,   203,     0,   191,   192,   193,
       0,    39,     0,   194,     0,     0,   204,     0,   195,   196,
       0,   183,     0,   184,     0,     0,     0,   185,     0,     0,
       0,     0,     0,   197,     0,   198,    73,   186,     0,     0,
       0,     0,     0,     0,     0,     0,   199,   200,     0,     0,
       0,   201,   187,   483,   188,   202,     0,     0,     0,   189,
     190,     0,     0,     0,     0,   191,   192,   193,     0,     0,
       0,   194,     0,     0,     0,     0,   195,   196,     0,   203,
       0,     0,   376,     0,     0,    39,   183,     0,   184,     0,
     204,   197,   185,   198,    73,     0,     0,     0,     0,     0,
       0,     0,   186,     0,   199,   200,     0,     0,     0,   201,
       0,     0,     0,   202,     0,     0,     0,   187,     0,   188,
       0,     0,     0,     0,   189,   190,     0,     0,     0,     0,
     191,   192,   193,     0,     0,     0,   194,   203,     0,     0,
       0,   195,   196,    39,   183,     0,   184,     0,   204,     0,
     185,     0,     0,     0,     0,     0,   197,   493,   198,    73,
     186,     0,     0,     0,     0,     0,     0,     0,     0,   199,
     200,     0,     0,     0,   201,   187,     0,   188,   202,     0,
       0,     0,   189,   190,     0,     0,     0,     0,   191,   192,
     193,     0,     0,     0,   194,     0,   633,     0,     0,   195,
     196,     0,   203,     0,     0,     0,     0,     0,    39,   183,
       0,   184,     0,   204,   197,   185,   198,    73,     0,     0,
       0,     0,     0,     0,     0,   186,     0,   199,   200,     0,
       0,     0,   201,     0,     0,     0,   202,     0,     0,     0,
     187,   677,   188,     0,     0,     0,     0,   189,   190,     0,
       0,     0,     0,   191,   192,   193,     0,     0,     0,   194,
     203,     0,     0,     0,   195,   196,    39,   183,     0,   184,
       0,   204,     0,   185,     0,     0,     0,     0,     0,   197,
       0,   198,    73,   186,     0,     0,     0,     0,     0,     0,
       0,     0,   199,   200,     0,     0,     0,   201,   187,     0,
     188,   202,     0,     0,     0,   189,   190,     0,     0,     0,
       0,   191,   192,   193,     0,     0,     0,   194,     0,   709,
       0,     0,   195,   196,     0,   203,     0,     0,     0,     0,
       0,    39,   183,     0,   184,     0,   204,   197,   185,   198,
      73,     0,     0,     0,     0,     0,     0,     0,   186,     0,
     199,   200,     0,     0,     0,   201,     0,     0,     0,   202,
       0,     0,     0,   187,     0,   188,     0,     0,     0,     0,
     189,   190,     0,     0,     0,     0,   191,   192,   193,     0,
       0,     0,   194,   203,     0,     0,     0,   195,   196,    39,
     183,     0,   184,     0,   204,     0,   185,     0,     0,     0,
       0,     0,   197,     0,   198,    73,   186,     0,     0,     0,
       0,   183,     0,   184,     0,   199,   200,   185,     0,     0,
     201,   187,     0,   188,   202,     0,     0,   186,   189,   190,
       0,     0,     0,     0,   191,   192,   193,     0,     0,     0,
     194,     0,   187,     0,   188,   195,   196,     0,   203,   189,
     190,   787,     0,     0,    39,   191,   192,   193,     0,   204,
     197,   194,   198,    73,     0,     0,   195,   196,     0,     0,
       0,     0,     0,   199,   200,     0,     0,     0,   201,     0,
       0,   197,   202,   198,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   199,   200,     0,     0,     0,   201,
       0,     0,     0,   202,     0,     0,   203,     0,     0,   790,
       0,     0,    39,     0,     0,     0,     0,   204,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   203,     0,     0,
       0,     0,     0,    39,     0,     0,     0,    54,   204,    55,
      46,    47,    48,    56,    57,    58,    59,    60,    61,    62,
       0,     0,     0,    63,    64,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    65,   233,     0,
     234,     0,     0,     0,    66,     0,     0,     0,    67,    68,
      69,   235,     0,     0,     0,     0,    70,     0,     0,     0,
       0,     0,   236,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      73,     0,     0,     0,     0,     0,     0,     0,     0,   237,
       0,     0,     0,     0,     0,     0,    76,    77,     0,     0,
      79,    54,    80,    55,    46,    47,    48,    56,    57,    58,
      59,    60,    61,    62,     0,     0,     0,    63,    64,     0,
       0,     0,     0,     0,     0,     0,   810,     0,     0,     0,
       0,    65,   233,     0,   234,     0,     0,     0,    66,     0,
       0,     0,    67,    68,    69,   235,     0,     0,     0,     0,
      70,     0,     0,     0,     0,     0,   236,     0,     0,   118,
     119,   120,   121,   122,   123,   124,     0,     0,     0,     0,
       0,     0,     0,     0,    73,     0,     0,     0,     0,     0,
       0,     0,     0,   237,     0,     0,     0,     0,     0,     0,
      76,    77,     0,     0,    79,     0,    80,   118,   119,   120,
     121,   122,   123,   124,     0,     0,     0,     0,     0,     0,
       0,   426,   427,     0,   125,     0,     0,     0,     0,     0,
     813,   126,   127,   128,     0,     0,     0,     0,     0,     0,
       0,     0,   129,   428,   130,   131,   132,   133,   134,     0,
     135,   136,   137,   138,   139,   140,     0,   141,   142,   143,
       0,     0,   125,     0,     0,     0,     0,     0,     0,   126,
     127,   128,   429,   118,   119,   120,   121,   122,   123,   124,
     129,     0,   130,   131,   132,   133,   134,     0,   135,   136,
     137,   138,   139,   140,     0,   141,   142,   143,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     655,   118,   119,   120,   121,   122,   123,   124,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   125,     0,
       0,     0,     0,     0,     0,   126,   127,   128,     0,     0,
       0,     0,     0,     0,     0,     0,   129,     0,   130,   131,
     132,   133,   134,     0,   135,   136,   137,   138,   139,   140,
       0,   141,   142,   143,     0,     0,   125,     0,     0,     0,
       0,     0,     0,   126,   127,   128,   656,   118,   119,   120,
     121,   122,   123,   124,   129,     0,   130,   131,   132,   133,
     134,     0,   135,   136,   137,   138,   139,   140,     0,   141,
     142,   143,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   657,   118,   119,   120,   121,   122,
     123,   124,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   125,     0,     0,     0,     0,     0,     0,   126,
     127,   128,     0,     0,     0,     0,     0,     0,     0,     0,
     129,     0,   130,   131,   132,   133,   134,     0,   135,   136,
     137,   138,   139,   140,     0,   141,   142,   143,     0,     0,
     125,     0,     0,     0,     0,     0,    39,   126,   127,   128,
       0,     0,     0,     0,     0,     0,     0,     0,   129,     0,
     130,   131,   132,   133,   134,     0,   135,   136,   137,   138,
     139,   140,     0,   141,   142,   143,     0,     0,     0,     0,
       0,     0,    54,   495,    55,    46,    47,    48,    56,    57,
      58,    59,    60,    61,    62,     0,     0,     0,    63,    64,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    65,   233,     0,   234,     0,     0,     0,    66,
       0,     0,     0,    67,    68,    69,   235,     0,     0,     0,
       0,    70,     0,     0,     0,     0,     0,   236,   118,   119,
     120,   121,   122,   123,   124,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    73,     0,     0,     0,     0,
       0,     0,     0,     0,   237,     0,     0,     0,     0,     0,
       0,    76,    77,     0,     0,    79,     0,    80,     0,   402,
     118,   119,   120,   121,   122,   123,   124,     0,     0,     0,
       0,     0,     0,   125,     0,     0,     0,     0,     0,     0,
     126,   127,   128,     0,     0,     0,     0,     0,     0,     0,
       0,   129,     0,   130,   131,   132,   133,   134,     0,   135,
     136,   137,   138,   139,   140,     0,   141,   142,   143,     0,
       0,     0,     0,     0,   486,   125,     0,     0,     0,     0,
       0,     0,   126,   127,   128,   118,   119,   120,   121,   122,
     123,   124,     0,   129,     0,   130,   131,   132,   133,   134,
       0,   135,   136,   137,   138,   139,   140,     0,   141,   142,
     143,     0,     0,     0,     0,     0,   496,     0,     0,     0,
       0,   118,   119,   120,   121,   122,   123,   124,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     125,     0,     0,     0,     0,     0,     0,   126,   127,   128,
       0,     0,     0,     0,     0,     0,     0,     0,   129,     0,
     130,   131,   132,   133,   134,     0,   135,   136,   137,   138,
     139,   140,     0,   141,   142,   143,   125,     0,     0,     0,
       0,   612,     0,   126,   127,   128,   118,   119,   120,   121,
     122,   123,   124,     0,   129,     0,   130,   131,   132,   133,
     134,     0,   135,   136,   137,   138,   139,   140,     0,   141,
     142,   143,     0,     0,     0,     0,     0,   614,     0,     0,
       0,     0,   118,   119,   120,   121,   122,   123,   124,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   125,     0,     0,     0,     0,     0,     0,   126,   127,
     128,     0,     0,     0,     0,     0,     0,     0,     0,   129,
       0,   130,   131,   132,   133,   134,     0,   135,   136,   137,
     138,   139,   140,     0,   141,   142,   143,   125,     0,     0,
       0,     0,   673,     0,   126,   127,   128,   118,   119,   120,
     121,   122,   123,   124,     0,   129,     0,   130,   131,   132,
     133,   134,     0,   135,   136,   137,   138,   139,   140,     0,
     141,   142,   143,     0,     0,     0,     0,     0,   674,     0,
       0,     0,     0,   118,   119,   120,   121,   122,   123,   124,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   125,     0,     0,     0,     0,     0,     0,   126,
     127,   128,     0,     0,     0,     0,     0,     0,     0,     0,
     129,     0,   130,   131,   132,   133,   134,     0,   135,   136,
     137,   138,   139,   140,     0,   141,   142,   143,   125,     0,
       0,     0,     0,   676,     0,   126,   127,   128,   118,   119,
     120,   121,   122,   123,   124,     0,   129,     0,   130,   131,
     132,   133,   134,     0,   135,   136,   137,   138,   139,   140,
       0,   141,   142,   143,     0,     0,     0,     0,     0,   688,
       0,     0,     0,     0,   118,   119,   120,   121,   122,   123,
     124,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   125,     0,     0,     0,     0,     0,     0,
     126,   127,   128,     0,     0,     0,     0,     0,     0,     0,
       0,   129,     0,   130,   131,   132,   133,   134,     0,   135,
     136,   137,   138,   139,   140,     0,   141,   142,   143,   125,
       0,     0,     0,     0,   691,     0,   126,   127,   128,   118,
     119,   120,   121,   122,   123,   124,     0,   129,     0,   130,
     131,   132,   133,   134,     0,   135,   136,   137,   138,   139,
     140,     0,   141,   142,   143,     0,     0,     0,     0,     0,
     692,     0,     0,     0,     0,   118,   119,   120,   121,   122,
     123,   124,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   125,     0,     0,     0,     0,     0,
       0,   126,   127,   128,     0,     0,     0,     0,     0,     0,
       0,     0,   129,     0,   130,   131,   132,   133,   134,     0,
     135,   136,   137,   138,   139,   140,     0,   141,   142,   143,
     125,     0,     0,     0,     0,   729,     0,   126,   127,   128,
     118,   119,   120,   121,   122,   123,   124,     0,   129,     0,
     130,   131,   132,   133,   134,     0,   135,   136,   137,   138,
     139,   140,     0,   141,   142,   143,     0,     0,     0,     0,
       0,   740,     0,     0,     0,     0,   118,   119,   120,   121,
     122,   123,   124,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   125,     0,     0,     0,     0,
       0,     0,   126,   127,   128,     0,     0,     0,     0,     0,
       0,     0,     0,   129,     0,   130,   131,   132,   133,   134,
       0,   135,   136,   137,   138,   139,   140,     0,   141,   142,
     143,   125,     0,     0,     0,     0,   752,     0,   126,   127,
     128,     0,     0,     0,     0,     0,     0,     0,     0,   129,
       0,   130,   131,   132,   133,   134,     0,   135,   136,   137,
     138,   139,   140,     0,   141,   142,   143,     0,     0,     0,
       0,    54,   778,    55,    46,    47,    48,    56,    57,    58,
      59,    60,    61,    62,     0,     0,     0,    63,    64,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    65,     0,     0,     0,     0,     0,     0,    66,     0,
       0,     0,    67,    68,    69,     0,     0,     0,     0,     0,
      70,     0,    71,     0,    72,     0,     0,     0,     0,     0,
       0,     0,     2,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    73,     0,     0,     0,     0,     0,
       0,    74,     0,    75,     0,     0,     0,     0,     0,     0,
      76,    77,    78,     0,    79,    54,    80,    55,    46,    47,
      48,    56,    57,    58,    59,    60,    61,    62,     0,     0,
       0,    63,    64,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    65,   233,     0,   234,     0,
       0,     0,    66,     0,     0,     0,    67,    68,    69,   235,
       0,     0,     0,     0,    70,     0,     0,     0,     0,     0,
     236,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    73,     0,
       0,     0,     0,     0,     0,     0,   408,   237,     0,     0,
       0,     0,     0,     0,    76,    77,     0,     0,    79,    54,
      80,    55,    46,    47,    48,    56,    57,    58,    59,    60,
      61,    62,     0,     0,     0,    63,    64,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    65,
     233,   540,   234,     0,     0,     0,    66,     0,     0,     0,
      67,    68,    69,   235,     0,     0,     0,     0,    70,     0,
       0,     0,     0,     0,   236,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    73,     0,     0,     0,     0,     0,     0,     0,
       0,   237,     0,     0,     0,     0,     0,     0,    76,    77,
       0,     0,    79,    54,    80,    55,    46,    47,    48,    56,
      57,    58,    59,    60,    61,    62,     0,     0,     0,    63,
      64,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    65,   233,   718,   234,     0,     0,     0,
      66,     0,     0,     0,    67,    68,    69,   235,     0,     0,
       0,     0,    70,     0,     0,     0,     0,     0,   236,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    73,     0,     0,     0,
       0,     0,     0,     0,     0,   237,     0,     0,     0,     0,
       0,     0,    76,    77,     0,     0,    79,    54,    80,    55,
      46,    47,    48,    56,    57,    58,    59,    60,    61,    62,
       0,     0,     0,    63,    64,     0,     0,     0,   118,   119,
     120,   121,   122,   123,   124,     0,     0,    65,   233,     0,
     234,     0,     0,     0,    66,     0,     0,     0,    67,    68,
      69,   235,     0,     0,     0,     0,    70,     0,     0,     0,
       0,     0,   236,     0,   118,   119,   120,   121,   122,   123,
     124,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      73,     0,     0,   125,     0,     0,     0,     0,     0,   237,
     126,   127,   128,     0,     0,     0,    76,    77,     0,     0,
      79,   129,    80,   130,   131,   132,   133,   134,     0,   135,
     136,   137,   138,   139,   140,     0,   141,   142,   143,   125,
       0,     0,     0,   268,     0,     0,   126,   127,   128,   118,
     119,   120,   121,   122,   123,   124,     0,   129,     0,   130,
     131,   132,   133,   134,     0,   135,   136,   137,   138,   139,
     140,     0,   141,   142,   143,     0,     0,     0,     0,   430,
       0,     0,     0,     0,     0,   118,   119,   120,   121,   122,
     123,   124,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   125,     0,     0,     0,     0,     0,
       0,   126,   127,   128,     0,     0,     0,     0,     0,     0,
       0,     0,   129,     0,   130,   131,   132,   133,   134,     0,
     135,   136,   137,   138,   139,   140,     0,   141,   142,   143,
     125,     0,     0,     0,   597,     0,     0,   126,   127,   128,
     118,   119,   120,   121,   122,   123,   124,     0,   129,     0,
     130,   131,   132,   133,   134,     0,   135,   136,   137,   138,
     139,   140,     0,   141,   142,   143,     0,     0,     0,     0,
     598,     0,     0,     0,     0,     0,   118,   119,   120,   121,
     122,   123,   124,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   125,     0,     0,     0,     0,
       0,     0,   126,   127,   128,     0,     0,     0,     0,     0,
       0,     0,     0,   129,     0,   130,   131,   132,   133,   134,
       0,   135,   136,   137,   138,   139,   140,     0,   141,   142,
     143,   125,     0,     0,     0,   599,     0,     0,   126,   127,
     128,   118,   119,   120,   121,   122,   123,   124,     0,   129,
       0,   130,   131,   132,   133,   134,     0,   135,   136,   137,
     138,   139,   140,     0,   141,   142,   143,     0,     0,     0,
       0,   600,     0,     0,     0,     0,     0,   118,   119,   120,
     121,   122,   123,   124,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   125,     0,     0,     0,
       0,     0,     0,   126,   127,   128,     0,     0,     0,     0,
       0,     0,     0,     0,   129,     0,   130,   131,   132,   133,
     134,     0,   135,   136,   137,   138,   139,   140,     0,   141,
     142,   143,   125,     0,     0,     0,   602,     0,     0,   126,
     127,   128,   118,   119,   120,   121,   122,   123,   124,     0,
     129,     0,   130,   131,   132,   133,   134,     0,   135,   136,
     137,   138,   139,   140,     0,   141,   142,   143,     0,     0,
       0,     0,   604,     0,     0,     0,     0,     0,   118,   119,
     120,   121,   122,   123,   124,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   125,     0,     0,
       0,     0,     0,     0,   126,   127,   128,     0,     0,     0,
       0,     0,     0,     0,     0,   129,     0,   130,   131,   132,
     133,   134,     0,   135,   136,   137,   138,   139,   140,     0,
     141,   142,   143,   125,     0,     0,     0,   642,     0,     0,
     126,   127,   128,   118,   119,   120,   121,   122,   123,   124,
       0,   129,     0,   130,   131,   132,   133,   134,     0,   135,
     136,   137,   138,   139,   140,     0,   141,   142,   143,     0,
       0,     0,     0,   643,     0,     0,     0,     0,     0,   118,
     119,   120,   121,   122,   123,   124,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   125,     0,
       0,     0,     0,     0,     0,   126,   127,   128,     0,     0,
       0,     0,     0,     0,     0,     0,   129,     0,   130,   131,
     132,   133,   134,     0,   135,   136,   137,   138,   139,   140,
       0,   141,   142,   143,   125,     0,     0,     0,   782,     0,
       0,   126,   127,   128,   118,   119,   120,   121,   122,   123,
     124,     0,   129,     0,   130,   131,   132,   133,   134,     0,
     135,   136,   137,   138,   139,   140,     0,   141,   142,   143,
       0,     0,     0,     0,   784,     0,     0,     0,     0,     0,
       0,     0,     0,   118,   119,   120,   121,   122,   123,   124,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   125,
       0,     0,     0,     0,     0,     0,   126,   127,   128,     0,
       0,     0,     0,     0,     0,     0,     0,   129,     0,   130,
     131,   132,   133,   134,     0,   135,   136,   137,   138,   139,
     140,     0,   141,   142,   143,   426,   427,     0,   125,   832,
       0,     0,     0,     0,     0,   126,   127,   128,   118,   119,
     120,   121,   122,   123,   124,     0,   129,   428,   130,   131,
     132,   133,   134,     0,   135,   136,   137,   138,   139,   140,
       0,   141,   142,   143,     0,     0,     0,     0,     0,     0,
     118,   119,   120,   121,   122,   123,   124,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   125,     0,     0,     0,     0,     0,     0,
     126,   127,   128,     0,     0,     0,     0,     0,     0,     0,
       0,   129,   432,   130,   131,   132,   133,   134,     0,   135,
     136,   137,   138,   139,   140,   125,   141,   142,   143,     0,
       0,     0,   126,   127,   128,   118,   119,   120,   121,   122,
     123,   124,     0,   129,     0,   130,   131,   132,   133,   134,
       0,   135,   136,   137,   138,   139,   140,     0,   141,   142,
     143,     0,     0,     0,     0,     0,     0,   118,     0,   120,
     121,   122,   123,   124,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     125,     0,     0,     0,     0,     0,     0,   126,   127,   128,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   131,   132,   133,   134,     0,   135,   136,   137,   138,
     139,   140,   125,   141,   142,   143,     0,     0,     0,   126,
     127,   128,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   131,   132,   133,   134,     0,   135,   136,
     137,   138,   139,   140,     0,   141,   142,   143
};

static const yytype_int16 yycheck[] =
{
      10,    18,   233,   197,   246,    68,    69,    21,   363,   173,
      15,   393,   398,   260,   417,   397,    55,     5,     5,   380,
       5,    31,    32,    33,    34,    35,    36,    37,    38,    39,
      40,    41,    53,    99,    21,     5,    53,     5,    13,     5,
       5,     5,     5,   528,     5,     5,    16,     5,     5,     5,
     535,   406,     5,    21,     5,    21,     5,    74,     4,     5,
       5,    82,    47,    48,     5,    82,     5,     5,   102,     5,
       8,     9,    10,     4,     5,     5,   122,     3,     5,   122,
     125,    65,    47,    48,   130,   130,    70,   130,   102,   122,
     100,   125,     5,   103,   122,    79,   457,   130,    79,    45,
      45,     0,   168,   464,    18,    34,     4,     5,   118,   119,
     120,   121,   122,   123,   124,   125,   126,   127,   128,   129,
     130,   131,   132,   133,   134,   135,   136,   137,   138,   139,
     140,   141,   142,   143,   173,   174,    42,   126,   123,    53,
      66,   130,   130,   130,   125,   184,   532,   213,     5,   531,
     635,    82,   127,   163,   217,   160,   219,   560,   221,   116,
     130,   403,   130,    55,   130,   121,   130,   130,    82,   130,
     130,    84,   130,    65,   130,   422,   127,   130,    70,   189,
     121,   130,   121,   122,    82,   123,   127,    79,   127,   199,
     200,   122,   122,   203,   121,   122,   124,   126,   123,   122,
     394,   124,   130,   116,   129,    18,    18,   130,   102,   122,
     194,   122,    83,   124,   378,   379,   233,   123,   122,   125,
     112,   205,     4,   115,   122,   586,    18,   124,   125,   246,
     715,   125,    18,    30,    31,    32,    18,    19,    20,   117,
      53,    53,    24,    25,    26,   116,   117,   118,   314,    96,
     124,   637,   121,   122,   320,   124,   130,   122,    18,   124,
     270,    53,   328,    45,   123,   130,   125,    53,   753,    82,
      82,    18,    18,   124,    30,    31,    32,   125,   126,   130,
     346,   173,   174,   126,   769,   124,    83,   130,   482,   299,
      82,   130,   184,    53,    12,   187,    82,    12,    13,   338,
      82,    16,   194,   342,   124,   197,    53,    53,   539,   695,
     324,     0,    16,   205,   380,     4,   801,   114,    16,   116,
     117,   118,    82,   386,   363,   125,   389,    83,   128,   392,
     716,   124,   125,   343,   528,    82,    82,    99,   185,   186,
      11,    12,    13,   680,     5,    16,   356,   684,   685,   359,
     360,   361,   127,     5,   364,   130,   112,   113,   114,   369,
     116,   117,   118,     6,   123,   375,   125,   406,   378,   379,
       5,   355,   382,     8,     9,    10,     5,   763,   680,   124,
     125,   365,   684,   685,   124,   125,   403,   371,   393,   399,
     237,   457,   397,     4,   404,   405,   122,   752,   124,   641,
     642,   122,   130,   124,   414,   127,     8,     9,   255,    11,
     126,   123,   259,   125,   398,   425,   426,   427,   428,    21,
      22,    23,   432,   778,   434,     5,   436,    67,    68,    69,
      70,    71,    72,    73,    74,   123,   123,   125,   125,   122,
      16,   124,   123,   123,   125,   125,   338,   123,   126,   125,
     342,   123,     5,   125,   123,   123,   125,   125,   123,     6,
     125,   471,   472,   355,   123,   123,   125,   125,   478,   124,
     123,   363,   125,   365,   124,   123,   126,   125,   123,   371,
     125,   123,   123,   125,   125,   495,    21,   124,    57,   126,
      59,   501,   502,   123,     5,   125,   506,   344,   508,    57,
     126,    59,   394,   350,   125,    57,   398,    59,   123,   123,
     125,   125,   124,   125,   406,   124,   125,    52,   124,   125,
     124,   125,   539,   124,   125,   124,   531,   124,   125,   771,
     772,   124,   125,    68,    69,   777,    71,   124,   125,   124,
     125,   124,   125,   122,   554,     5,   530,     5,   532,   124,
     125,   535,   599,   600,   122,   122,   122,   567,   122,   122,
     122,    96,    97,     5,   411,   122,   126,   102,   124,     5,
       5,   130,   126,   122,   122,     5,   122,   643,     5,   589,
     124,   126,   122,   126,   826,   126,   125,     5,   126,   126,
     482,   601,   124,   124,   124,   124,   124,     5,     5,   124,
     610,   124,     5,   124,   126,     5,   124,     5,   124,   122,
     145,   126,   596,   597,   124,   124,   124,    11,   602,   124,
     604,    59,   128,   127,   641,   642,   124,   126,   124,   164,
       5,   166,   124,   124,   644,   129,   528,   122,   530,   129,
     532,   124,   123,   535,   124,   124,   124,   124,   632,   659,
     185,   635,   124,   124,   124,   721,   666,   124,    57,   128,
       5,   124,    59,    28,     4,    30,    31,    32,    33,    34,
     124,   124,   124,    39,   102,   522,    52,   524,   525,   526,
     527,   124,   217,   124,   219,   124,   221,     5,    57,    39,
     124,   124,   227,   102,    52,     5,   128,    52,   545,   124,
     131,   124,   124,    52,   596,   597,    52,     5,   124,    57,
     602,   695,   604,   752,   124,    57,    59,    52,    83,   124,
     124,   256,     5,    57,    57,   260,   122,    59,    57,   124,
       4,   715,   716,   124,   124,    17,   160,   469,   384,   778,
     632,   106,   107,   635,   109,   110,   111,   112,   113,   114,
     575,   116,   117,   118,   771,   772,    97,   741,   742,   581,
     777,    65,   304,   747,   610,   401,   721,   721,   342,   753,
     270,   448,    -1,    -1,    -1,   622,   311,   312,    -1,   763,
     627,    -1,    -1,    -1,    -1,   769,    -1,   322,    -1,   324,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   646,
      -1,    -1,    -1,   695,    -1,    -1,     4,     5,   818,   826,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   801,    -1,    -1,
      18,    19,    20,   715,   716,    -1,    24,    25,    26,    -1,
      30,    31,    32,    33,    34,   819,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    45,    -1,   741,
     742,    -1,   699,    -1,    -1,   747,    -1,    -1,    -1,    -1,
     752,   753,    -1,    -1,    -1,    -1,   713,   714,    66,    -1,
      -1,   763,    -1,    -1,    -1,   410,    -1,   769,   413,    -1,
      -1,     4,     5,    83,    82,   420,   778,   422,    -1,    -1,
      -1,    -1,    90,    91,    92,    18,    19,    20,    -1,    -1,
      -1,    24,    25,    26,    -1,   103,   104,   105,    -1,   801,
     110,   111,   112,   113,   114,   113,   116,   117,   118,   766,
      -1,    -1,    45,    -1,   122,   123,    -1,   819,    -1,   127,
      -1,   129,    -1,    -1,    -1,   133,   134,    -1,    -1,    -1,
      -1,    -1,    -1,    66,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,     4,     5,    -1,    82,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,
      18,    19,    20,    -1,    -1,    -1,    24,    25,    26,    -1,
     103,   104,   105,    -1,    -1,    -1,    -1,   522,    -1,   524,
     113,    -1,    40,    41,    -1,    -1,    -1,    45,    -1,   122,
     123,    -1,    -1,    -1,   127,    -1,   129,    -1,    -1,    -1,
     133,   134,    -1,    -1,    -1,    -1,    -1,    -1,    66,    -1,
      -1,    -1,    -1,    28,    -1,    30,    31,    32,    33,    34,
      -1,    -1,     4,     5,    82,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    90,    91,    92,    -1,    18,    19,    20,    -1,
      -1,    -1,    24,    25,    26,   103,   104,   105,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   113,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    45,   122,    -1,    -1,    -1,    83,   127,
      52,    53,    -1,    -1,    -1,   133,   134,    -1,   623,   624,
     625,    -1,   627,   628,    66,    -1,    -1,    -1,    -1,    -1,
     105,   106,   107,    -1,   109,   110,   111,   112,   113,   114,
      82,   116,   117,   118,    -1,    -1,    -1,    -1,    90,    91,
      92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   103,   104,   105,    -1,    -1,    -1,    -1,     4,     5,
      -1,   113,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     122,    -1,    18,    19,    20,   127,    -1,    -1,    24,    25,
      26,   133,   134,    -1,    -1,   700,    -1,   702,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   713,    45,
      -1,    -1,    -1,    -1,    -1,    -1,    52,    53,    -1,    -1,
      -1,    -1,     4,     5,    -1,    -1,    -1,    -1,    -1,    -1,
      66,    -1,    -1,    -1,    -1,    -1,    18,    19,    20,    -1,
      -1,    -1,    24,    25,    26,    -1,    82,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,
      -1,   766,   767,    45,    -1,    -1,    -1,   103,   104,   105,
      52,    53,    -1,    -1,    -1,    -1,    -1,   113,    -1,    -1,
      -1,    -1,    -1,    -1,    66,    -1,   122,    -1,    -1,    -1,
      -1,   127,    -1,    -1,    -1,    -1,    -1,   133,   134,    -1,
      82,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,
      92,    -1,     4,     5,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   103,   104,   105,    -1,    -1,    18,    19,    20,    -1,
      -1,   113,    24,    25,    26,    -1,    -1,    -1,    -1,    -1,
     122,    -1,    -1,    -1,    -1,   127,    -1,    -1,    -1,    -1,
      -1,   133,   134,    45,    -1,    -1,    -1,    -1,    -1,    -1,
      52,    53,     4,     5,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    66,    -1,    18,    19,    20,    -1,
      -1,    -1,    24,    25,    26,    -1,    -1,    -1,    -1,    -1,
      82,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,
      92,    -1,    -1,    45,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   103,   104,   105,    -1,    -1,    -1,     4,     5,    -1,
      -1,   113,    -1,    -1,    66,    -1,    -1,    -1,    -1,    -1,
     122,    18,    19,    20,    -1,   127,    -1,    24,    25,    26,
      82,   133,   134,    -1,    -1,    -1,    -1,    -1,    90,    91,
      92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    45,    -1,
      -1,   103,   104,   105,   106,    -1,    -1,     4,     5,    -1,
      -1,   113,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    66,
     122,    18,    19,    20,    -1,   127,    -1,    24,    25,    26,
      -1,   133,   134,    -1,    -1,    82,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    91,    92,    -1,    -1,    45,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   103,   104,   105,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   113,    -1,    -1,    66,
      -1,    -1,    -1,    -1,    -1,   122,   123,    -1,    -1,    -1,
     127,    -1,     4,     5,    -1,    82,   133,   134,    -1,    -1,
      -1,    -1,    -1,    90,    91,    92,    18,    19,    20,    -1,
      -1,    -1,    24,    25,    26,    -1,   103,   104,   105,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   113,    -1,    -1,    -1,
      -1,    -1,    -1,    45,   121,   122,    -1,    -1,    -1,    -1,
     127,     4,     5,    -1,    -1,    -1,   133,   134,    -1,    -1,
      -1,    -1,    -1,    -1,    66,    18,    19,    20,    -1,    -1,
      -1,    24,    25,    26,    -1,    -1,    -1,    -1,    -1,    -1,
      82,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,
      92,    -1,    45,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      53,   103,   104,   105,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   113,    -1,    66,    -1,    -1,    -1,    -1,    -1,    -1,
     122,    -1,    -1,    -1,    -1,   127,    -1,   129,    -1,    82,
      -1,   133,   134,    -1,    -1,    -1,    -1,    90,    91,    92,
      -1,     4,     5,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     103,   104,   105,    -1,    -1,    18,    19,    20,    -1,    -1,
     113,    24,    25,    26,    -1,    -1,    -1,    -1,    -1,   122,
      -1,    -1,    -1,    -1,   127,    -1,    -1,    -1,    -1,    -1,
     133,   134,    45,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      53,     4,     5,    -1,     4,     5,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    66,    -1,    18,    19,    20,    18,    19,
      20,    24,    25,    26,    24,    25,    26,    -1,    -1,    82,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,
      -1,    -1,    45,    -1,    -1,    45,    -1,    -1,    -1,    -1,
     103,   104,   105,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     113,    -1,    -1,    66,    -1,    -1,    66,    -1,    -1,   122,
      -1,    -1,    -1,    -1,   127,    -1,    -1,    -1,    -1,    82,
     133,   134,    82,    -1,    -1,    -1,    -1,    90,    91,    92,
      90,    91,    92,    30,    31,    32,    33,    34,    -1,    -1,
     103,   104,   105,   103,   104,   105,    -1,    -1,    -1,    -1,
     113,    -1,     5,   113,     7,    -1,    -1,    -1,    11,   122,
     123,    -1,   122,    -1,   127,    -1,    -1,   127,    21,    -1,
     133,   134,    -1,   133,   134,    28,    29,    30,    31,    32,
      33,    34,    -1,    36,    -1,    38,    83,    -1,    -1,    -1,
      43,    44,    -1,    -1,    -1,    -1,    49,    50,    51,    -1,
      -1,    -1,    55,    -1,    -1,    -1,    -1,    60,    61,   106,
     107,    -1,   109,   110,   111,   112,   113,   114,    -1,   116,
     117,   118,    75,    -1,    77,    78,    -1,    -1,    -1,    -1,
      83,    -1,    -1,    -1,    -1,    88,    89,    90,    91,    92,
      93,    -1,    -1,    -1,    97,    -1,    -1,    -1,   101,    -1,
     103,   104,   105,   106,   107,    -1,   109,   110,   111,   112,
     113,   114,    -1,   116,   117,   118,    -1,    -1,   121,    -1,
      -1,   124,    -1,    -1,   127,    -1,    -1,    -1,     5,   132,
       7,     8,     9,    -1,    11,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    21,    22,    23,    -1,    -1,     5,
      -1,     7,    -1,    -1,    -1,    11,    -1,    -1,    -1,    36,
      -1,    38,    -1,    -1,    -1,    21,    43,    44,    -1,    -1,
      -1,    -1,    49,    50,    51,    -1,    -1,    -1,    55,    -1,
      36,    37,    38,    60,    61,    -1,    -1,    43,    44,    -1,
      -1,    -1,    -1,    49,    50,    51,    -1,    -1,    75,    55,
      77,    78,    -1,    -1,    60,    61,    -1,    -1,    -1,    -1,
      -1,    88,    89,    -1,    -1,    -1,    93,    -1,    -1,    75,
      97,    77,    78,     5,    -1,     7,    -1,    -1,    -1,    11,
      -1,    -1,    88,    89,    -1,    -1,    -1,    93,    -1,    21,
      -1,    97,    -1,    -1,   121,    -1,   102,    -1,    -1,    -1,
     127,    -1,    -1,    -1,    36,   132,    38,    -1,    -1,    -1,
      -1,    43,    44,    -1,    -1,   121,    -1,    49,    50,    51,
      -1,   127,    -1,    55,    -1,    -1,   132,    -1,    60,    61,
      -1,     5,    -1,     7,    -1,    -1,    -1,    11,    -1,    -1,
      -1,    -1,    -1,    75,    -1,    77,    78,    21,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    88,    89,    -1,    -1,
      -1,    93,    36,    37,    38,    97,    -1,    -1,    -1,    43,
      44,    -1,    -1,    -1,    -1,    49,    50,    51,    -1,    -1,
      -1,    55,    -1,    -1,    -1,    -1,    60,    61,    -1,   121,
      -1,    -1,   124,    -1,    -1,   127,     5,    -1,     7,    -1,
     132,    75,    11,    77,    78,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    21,    -1,    88,    89,    -1,    -1,    -1,    93,
      -1,    -1,    -1,    97,    -1,    -1,    -1,    36,    -1,    38,
      -1,    -1,    -1,    -1,    43,    44,    -1,    -1,    -1,    -1,
      49,    50,    51,    -1,    -1,    -1,    55,   121,    -1,    -1,
      -1,    60,    61,   127,     5,    -1,     7,    -1,   132,    -1,
      11,    -1,    -1,    -1,    -1,    -1,    75,    76,    77,    78,
      21,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    88,
      89,    -1,    -1,    -1,    93,    36,    -1,    38,    97,    -1,
      -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,    50,
      51,    -1,    -1,    -1,    55,    -1,    57,    -1,    -1,    60,
      61,    -1,   121,    -1,    -1,    -1,    -1,    -1,   127,     5,
      -1,     7,    -1,   132,    75,    11,    77,    78,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    21,    -1,    88,    89,    -1,
      -1,    -1,    93,    -1,    -1,    -1,    97,    -1,    -1,    -1,
      36,    37,    38,    -1,    -1,    -1,    -1,    43,    44,    -1,
      -1,    -1,    -1,    49,    50,    51,    -1,    -1,    -1,    55,
     121,    -1,    -1,    -1,    60,    61,   127,     5,    -1,     7,
      -1,   132,    -1,    11,    -1,    -1,    -1,    -1,    -1,    75,
      -1,    77,    78,    21,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    88,    89,    -1,    -1,    -1,    93,    36,    -1,
      38,    97,    -1,    -1,    -1,    43,    44,    -1,    -1,    -1,
      -1,    49,    50,    51,    -1,    -1,    -1,    55,    -1,    57,
      -1,    -1,    60,    61,    -1,   121,    -1,    -1,    -1,    -1,
      -1,   127,     5,    -1,     7,    -1,   132,    75,    11,    77,
      78,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    21,    -1,
      88,    89,    -1,    -1,    -1,    93,    -1,    -1,    -1,    97,
      -1,    -1,    -1,    36,    -1,    38,    -1,    -1,    -1,    -1,
      43,    44,    -1,    -1,    -1,    -1,    49,    50,    51,    -1,
      -1,    -1,    55,   121,    -1,    -1,    -1,    60,    61,   127,
       5,    -1,     7,    -1,   132,    -1,    11,    -1,    -1,    -1,
      -1,    -1,    75,    -1,    77,    78,    21,    -1,    -1,    -1,
      -1,     5,    -1,     7,    -1,    88,    89,    11,    -1,    -1,
      93,    36,    -1,    38,    97,    -1,    -1,    21,    43,    44,
      -1,    -1,    -1,    -1,    49,    50,    51,    -1,    -1,    -1,
      55,    -1,    36,    -1,    38,    60,    61,    -1,   121,    43,
      44,   124,    -1,    -1,   127,    49,    50,    51,    -1,   132,
      75,    55,    77,    78,    -1,    -1,    60,    61,    -1,    -1,
      -1,    -1,    -1,    88,    89,    -1,    -1,    -1,    93,    -1,
      -1,    75,    97,    77,    78,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    88,    89,    -1,    -1,    -1,    93,
      -1,    -1,    -1,    97,    -1,    -1,   121,    -1,    -1,   124,
      -1,    -1,   127,    -1,    -1,    -1,    -1,   132,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   121,    -1,    -1,
      -1,    -1,    -1,   127,    -1,    -1,    -1,     5,   132,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    16,    17,
      -1,    -1,    -1,    21,    22,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    35,    36,    -1,
      38,    -1,    -1,    -1,    42,    -1,    -1,    -1,    46,    47,
      48,    49,    -1,    -1,    -1,    -1,    54,    -1,    -1,    -1,
      -1,    -1,    60,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      78,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    87,
      -1,    -1,    -1,    -1,    -1,    -1,    94,    95,    -1,    -1,
      98,     5,   100,     7,     8,     9,    10,    11,    12,    13,
      14,    15,    16,    17,    -1,    -1,    -1,    21,    22,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   124,    -1,    -1,    -1,
      -1,    35,    36,    -1,    38,    -1,    -1,    -1,    42,    -1,
      -1,    -1,    46,    47,    48,    49,    -1,    -1,    -1,    -1,
      54,    -1,    -1,    -1,    -1,    -1,    60,    -1,    -1,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    78,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    87,    -1,    -1,    -1,    -1,    -1,    -1,
      94,    95,    -1,    -1,    98,    -1,   100,    28,    29,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    80,    81,    -1,    83,    -1,    -1,    -1,    -1,    -1,
     124,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   101,   102,   103,   104,   105,   106,   107,    -1,
     109,   110,   111,   112,   113,   114,    -1,   116,   117,   118,
      -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,
      91,    92,   131,    28,    29,    30,    31,    32,    33,    34,
     101,    -1,   103,   104,   105,   106,   107,    -1,   109,   110,
     111,   112,   113,   114,    -1,   116,   117,   118,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     131,    28,    29,    30,    31,    32,    33,    34,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,
      -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   101,    -1,   103,   104,
     105,   106,   107,    -1,   109,   110,   111,   112,   113,   114,
      -1,   116,   117,   118,    -1,    -1,    83,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    91,    92,   131,    28,    29,    30,
      31,    32,    33,    34,   101,    -1,   103,   104,   105,   106,
     107,    -1,   109,   110,   111,   112,   113,   114,    -1,   116,
     117,   118,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   131,    28,    29,    30,    31,    32,
      33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     101,    -1,   103,   104,   105,   106,   107,    -1,   109,   110,
     111,   112,   113,   114,    -1,   116,   117,   118,    -1,    -1,
      83,    -1,    -1,    -1,    -1,    -1,   127,    90,    91,    92,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   101,    -1,
     103,   104,   105,   106,   107,    -1,   109,   110,   111,   112,
     113,   114,    -1,   116,   117,   118,    -1,    -1,    -1,    -1,
      -1,    -1,     5,   126,     7,     8,     9,    10,    11,    12,
      13,    14,    15,    16,    17,    -1,    -1,    -1,    21,    22,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    35,    36,    -1,    38,    -1,    -1,    -1,    42,
      -1,    -1,    -1,    46,    47,    48,    49,    -1,    -1,    -1,
      -1,    54,    -1,    -1,    -1,    -1,    -1,    60,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    78,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    87,    -1,    -1,    -1,    -1,    -1,
      -1,    94,    95,    -1,    -1,    98,    -1,   100,    -1,   102,
      28,    29,    30,    31,    32,    33,    34,    -1,    -1,    -1,
      -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   101,    -1,   103,   104,   105,   106,   107,    -1,   109,
     110,   111,   112,   113,   114,    -1,   116,   117,   118,    -1,
      -1,    -1,    -1,    -1,   124,    83,    -1,    -1,    -1,    -1,
      -1,    -1,    90,    91,    92,    28,    29,    30,    31,    32,
      33,    34,    -1,   101,    -1,   103,   104,   105,   106,   107,
      -1,   109,   110,   111,   112,   113,   114,    -1,   116,   117,
     118,    -1,    -1,    -1,    -1,    -1,   124,    -1,    -1,    -1,
      -1,    28,    29,    30,    31,    32,    33,    34,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   101,    -1,
     103,   104,   105,   106,   107,    -1,   109,   110,   111,   112,
     113,   114,    -1,   116,   117,   118,    83,    -1,    -1,    -1,
      -1,   124,    -1,    90,    91,    92,    28,    29,    30,    31,
      32,    33,    34,    -1,   101,    -1,   103,   104,   105,   106,
     107,    -1,   109,   110,   111,   112,   113,   114,    -1,   116,
     117,   118,    -1,    -1,    -1,    -1,    -1,   124,    -1,    -1,
      -1,    -1,    28,    29,    30,    31,    32,    33,    34,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,
      92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   101,
      -1,   103,   104,   105,   106,   107,    -1,   109,   110,   111,
     112,   113,   114,    -1,   116,   117,   118,    83,    -1,    -1,
      -1,    -1,   124,    -1,    90,    91,    92,    28,    29,    30,
      31,    32,    33,    34,    -1,   101,    -1,   103,   104,   105,
     106,   107,    -1,   109,   110,   111,   112,   113,   114,    -1,
     116,   117,   118,    -1,    -1,    -1,    -1,    -1,   124,    -1,
      -1,    -1,    -1,    28,    29,    30,    31,    32,    33,    34,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     101,    -1,   103,   104,   105,   106,   107,    -1,   109,   110,
     111,   112,   113,   114,    -1,   116,   117,   118,    83,    -1,
      -1,    -1,    -1,   124,    -1,    90,    91,    92,    28,    29,
      30,    31,    32,    33,    34,    -1,   101,    -1,   103,   104,
     105,   106,   107,    -1,   109,   110,   111,   112,   113,   114,
      -1,   116,   117,   118,    -1,    -1,    -1,    -1,    -1,   124,
      -1,    -1,    -1,    -1,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   101,    -1,   103,   104,   105,   106,   107,    -1,   109,
     110,   111,   112,   113,   114,    -1,   116,   117,   118,    83,
      -1,    -1,    -1,    -1,   124,    -1,    90,    91,    92,    28,
      29,    30,    31,    32,    33,    34,    -1,   101,    -1,   103,
     104,   105,   106,   107,    -1,   109,   110,   111,   112,   113,
     114,    -1,   116,   117,   118,    -1,    -1,    -1,    -1,    -1,
     124,    -1,    -1,    -1,    -1,    28,    29,    30,    31,    32,
      33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,
      -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   101,    -1,   103,   104,   105,   106,   107,    -1,
     109,   110,   111,   112,   113,   114,    -1,   116,   117,   118,
      83,    -1,    -1,    -1,    -1,   124,    -1,    90,    91,    92,
      28,    29,    30,    31,    32,    33,    34,    -1,   101,    -1,
     103,   104,   105,   106,   107,    -1,   109,   110,   111,   112,
     113,   114,    -1,   116,   117,   118,    -1,    -1,    -1,    -1,
      -1,   124,    -1,    -1,    -1,    -1,    28,    29,    30,    31,
      32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,
      -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   101,    -1,   103,   104,   105,   106,   107,
      -1,   109,   110,   111,   112,   113,   114,    -1,   116,   117,
     118,    83,    -1,    -1,    -1,    -1,   124,    -1,    90,    91,
      92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   101,
      -1,   103,   104,   105,   106,   107,    -1,   109,   110,   111,
     112,   113,   114,    -1,   116,   117,   118,    -1,    -1,    -1,
      -1,     5,   124,     7,     8,     9,    10,    11,    12,    13,
      14,    15,    16,    17,    -1,    -1,    -1,    21,    22,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    35,    -1,    -1,    -1,    -1,    -1,    -1,    42,    -1,
      -1,    -1,    46,    47,    48,    -1,    -1,    -1,    -1,    -1,
      54,    -1,    56,    -1,    58,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    66,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    78,    -1,    -1,    -1,    -1,    -1,
      -1,    85,    -1,    87,    -1,    -1,    -1,    -1,    -1,    -1,
      94,    95,    96,    -1,    98,     5,   100,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    16,    17,    -1,    -1,
      -1,    21,    22,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    35,    36,    -1,    38,    -1,
      -1,    -1,    42,    -1,    -1,    -1,    46,    47,    48,    49,
      -1,    -1,    -1,    -1,    54,    -1,    -1,    -1,    -1,    -1,
      60,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    78,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    86,    87,    -1,    -1,
      -1,    -1,    -1,    -1,    94,    95,    -1,    -1,    98,     5,
     100,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      16,    17,    -1,    -1,    -1,    21,    22,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    35,
      36,    37,    38,    -1,    -1,    -1,    42,    -1,    -1,    -1,
      46,    47,    48,    49,    -1,    -1,    -1,    -1,    54,    -1,
      -1,    -1,    -1,    -1,    60,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    78,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    87,    -1,    -1,    -1,    -1,    -1,    -1,    94,    95,
      -1,    -1,    98,     5,   100,     7,     8,     9,    10,    11,
      12,    13,    14,    15,    16,    17,    -1,    -1,    -1,    21,
      22,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    35,    36,    37,    38,    -1,    -1,    -1,
      42,    -1,    -1,    -1,    46,    47,    48,    49,    -1,    -1,
      -1,    -1,    54,    -1,    -1,    -1,    -1,    -1,    60,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    78,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    87,    -1,    -1,    -1,    -1,
      -1,    -1,    94,    95,    -1,    -1,    98,     5,   100,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    16,    17,
      -1,    -1,    -1,    21,    22,    -1,    -1,    -1,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    35,    36,    -1,
      38,    -1,    -1,    -1,    42,    -1,    -1,    -1,    46,    47,
      48,    49,    -1,    -1,    -1,    -1,    54,    -1,    -1,    -1,
      -1,    -1,    60,    -1,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      78,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    87,
      90,    91,    92,    -1,    -1,    -1,    94,    95,    -1,    -1,
      98,   101,   100,   103,   104,   105,   106,   107,    -1,   109,
     110,   111,   112,   113,   114,    -1,   116,   117,   118,    83,
      -1,    -1,    -1,   123,    -1,    -1,    90,    91,    92,    28,
      29,    30,    31,    32,    33,    34,    -1,   101,    -1,   103,
     104,   105,   106,   107,    -1,   109,   110,   111,   112,   113,
     114,    -1,   116,   117,   118,    -1,    -1,    -1,    -1,   123,
      -1,    -1,    -1,    -1,    -1,    28,    29,    30,    31,    32,
      33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,
      -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   101,    -1,   103,   104,   105,   106,   107,    -1,
     109,   110,   111,   112,   113,   114,    -1,   116,   117,   118,
      83,    -1,    -1,    -1,   123,    -1,    -1,    90,    91,    92,
      28,    29,    30,    31,    32,    33,    34,    -1,   101,    -1,
     103,   104,   105,   106,   107,    -1,   109,   110,   111,   112,
     113,   114,    -1,   116,   117,   118,    -1,    -1,    -1,    -1,
     123,    -1,    -1,    -1,    -1,    -1,    28,    29,    30,    31,
      32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,
      -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   101,    -1,   103,   104,   105,   106,   107,
      -1,   109,   110,   111,   112,   113,   114,    -1,   116,   117,
     118,    83,    -1,    -1,    -1,   123,    -1,    -1,    90,    91,
      92,    28,    29,    30,    31,    32,    33,    34,    -1,   101,
      -1,   103,   104,   105,   106,   107,    -1,   109,   110,   111,
     112,   113,   114,    -1,   116,   117,   118,    -1,    -1,    -1,
      -1,   123,    -1,    -1,    -1,    -1,    -1,    28,    29,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   101,    -1,   103,   104,   105,   106,
     107,    -1,   109,   110,   111,   112,   113,   114,    -1,   116,
     117,   118,    83,    -1,    -1,    -1,   123,    -1,    -1,    90,
      91,    92,    28,    29,    30,    31,    32,    33,    34,    -1,
     101,    -1,   103,   104,   105,   106,   107,    -1,   109,   110,
     111,   112,   113,   114,    -1,   116,   117,   118,    -1,    -1,
      -1,    -1,   123,    -1,    -1,    -1,    -1,    -1,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,
      -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   101,    -1,   103,   104,   105,
     106,   107,    -1,   109,   110,   111,   112,   113,   114,    -1,
     116,   117,   118,    83,    -1,    -1,    -1,   123,    -1,    -1,
      90,    91,    92,    28,    29,    30,    31,    32,    33,    34,
      -1,   101,    -1,   103,   104,   105,   106,   107,    -1,   109,
     110,   111,   112,   113,   114,    -1,   116,   117,   118,    -1,
      -1,    -1,    -1,   123,    -1,    -1,    -1,    -1,    -1,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,
      -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   101,    -1,   103,   104,
     105,   106,   107,    -1,   109,   110,   111,   112,   113,   114,
      -1,   116,   117,   118,    83,    -1,    -1,    -1,   123,    -1,
      -1,    90,    91,    92,    28,    29,    30,    31,    32,    33,
      34,    -1,   101,    -1,   103,   104,   105,   106,   107,    -1,
     109,   110,   111,   112,   113,   114,    -1,   116,   117,   118,
      -1,    -1,    -1,    -1,   123,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    28,    29,    30,    31,    32,    33,    34,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,
      -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   101,    -1,   103,
     104,   105,   106,   107,    -1,   109,   110,   111,   112,   113,
     114,    -1,   116,   117,   118,    80,    81,    -1,    83,   123,
      -1,    -1,    -1,    -1,    -1,    90,    91,    92,    28,    29,
      30,    31,    32,    33,    34,    -1,   101,   102,   103,   104,
     105,   106,   107,    -1,   109,   110,   111,   112,   113,   114,
      -1,   116,   117,   118,    -1,    -1,    -1,    -1,    -1,    -1,
      28,    29,    30,    31,    32,    33,    34,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   101,   102,   103,   104,   105,   106,   107,    -1,   109,
     110,   111,   112,   113,   114,    83,   116,   117,   118,    -1,
      -1,    -1,    90,    91,    92,    28,    29,    30,    31,    32,
      33,    34,    -1,   101,    -1,   103,   104,   105,   106,   107,
      -1,   109,   110,   111,   112,   113,   114,    -1,   116,   117,
     118,    -1,    -1,    -1,    -1,    -1,    -1,    28,    -1,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   104,   105,   106,   107,    -1,   109,   110,   111,   112,
     113,   114,    83,   116,   117,   118,    -1,    -1,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   104,   105,   106,   107,    -1,   109,   110,
     111,   112,   113,   114,    -1,   116,   117,   118
};

/* YYSTOS[STATE-NUM] -- The symbol kind of the accessing symbol of
   state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,     3,    66,   136,   137,   138,   139,   146,     5,     4,
       5,    45,     0,   138,   121,   122,   124,   140,   141,     5,
       4,     5,    18,    19,    20,    24,    25,    26,    45,    66,
      82,    90,    91,    92,   103,   104,   105,   113,   122,   127,
     133,   134,   205,   209,   122,     5,     8,     9,    10,   123,
     142,   143,   203,   141,     5,     7,    11,    12,    13,    14,
      15,    16,    17,    21,    22,    35,    42,    46,    47,    48,
      54,    56,    58,    78,    85,    87,    94,    95,    96,    98,
     100,   144,   145,   146,   147,   150,   151,   155,   156,   159,
     160,   161,   166,   173,   174,   185,   203,   204,   117,   122,
     130,   201,   202,   122,   209,   209,   209,   209,   209,   209,
     209,   209,   106,   206,   207,   209,   209,   209,    28,    29,
      30,    31,    32,    33,    34,    83,    90,    91,    92,   101,
     103,   104,   105,   106,   107,   109,   110,   111,   112,   113,
     114,   116,   117,   118,     5,    47,    48,   123,   164,   165,
      12,    13,    16,    11,    12,    13,    16,    12,   124,   123,
     125,     5,    21,   130,   201,   144,     5,   121,   122,   172,
       5,   121,   122,   152,   169,   189,   190,   199,   205,    16,
      16,     5,   200,     5,     7,    11,    21,    36,    38,    43,
      44,    49,    50,    51,    55,    60,    61,    75,    77,    88,
      89,    93,    97,   121,   132,   178,   182,   185,   186,   187,
     188,   199,     5,   122,     5,   162,   163,    16,   162,   201,
     162,   201,   178,   182,     5,    21,   154,   201,     5,     5,
      45,   183,   184,    36,    38,    49,    60,    87,   147,   150,
     151,   159,   160,   161,   166,   173,   175,   176,   177,   185,
     182,    99,     6,   144,   200,   201,     5,   148,   149,   172,
     201,     4,   197,   209,   209,   201,   202,   209,   123,   205,
     125,   128,   205,   209,   209,   209,   209,   209,   209,   209,
     209,   209,   209,   209,   209,   209,   209,   209,   209,   209,
     209,   209,   209,   209,   209,   209,   209,   209,   209,   126,
       5,   201,     5,   123,   125,    16,   124,   143,   126,     5,
     209,     5,   201,     6,   122,   124,   201,     4,     5,    82,
     122,   197,     5,   201,   202,     4,     5,    82,   122,    67,
      68,    69,    70,    71,    72,    73,    74,   153,   169,   199,
     199,   124,   125,   126,   125,   124,   122,   124,   199,   200,
     201,   200,    37,   102,   182,   198,   122,   209,     5,   122,
     122,   122,   182,   122,   122,   198,     5,   209,   209,   122,
       5,   209,     5,    84,   116,   122,   124,   182,    34,   126,
     122,   197,   126,   124,   125,   162,   201,   124,   162,   201,
     124,   162,   201,   122,   124,     5,   201,   122,   124,   126,
      79,   125,   102,   175,   122,   122,   122,   200,    86,   176,
      13,   127,   124,   200,   126,   201,   124,   125,     5,   200,
       5,   149,   201,     5,   123,   125,    80,    81,   102,   131,
     123,   207,   102,   209,   126,     5,   126,   165,     4,    18,
      19,    20,    24,    25,    26,    45,    82,   208,   126,   201,
       5,   201,   123,   129,   167,   168,   197,   122,   123,   129,
     170,   171,   197,   123,   122,   201,   201,   202,   197,   125,
     199,   126,   126,   190,   209,   200,   123,   197,   126,   124,
     200,   124,     5,    37,   182,   209,   124,   124,   209,   209,
     209,   189,   209,    76,   124,   126,   124,   209,   124,   124,
     182,    40,    41,   180,   181,   209,   169,   209,   169,   209,
     167,   197,   123,   209,   163,   124,   162,   124,   162,   124,
     162,   142,     8,     9,    11,    21,    22,    23,   157,   158,
     198,   122,   124,     5,   142,   157,   182,   209,   184,     5,
      37,   209,   209,   189,   124,   127,   201,   200,   124,   201,
     209,   124,     5,   148,   126,   124,   201,   124,     5,   149,
     201,   209,   209,   209,   209,   209,   209,   126,   209,   208,
       5,   124,     5,   116,   123,   125,   123,   167,   197,     5,
     123,   125,   123,   124,   123,   167,   122,   123,   153,   126,
     209,   209,   124,   123,   209,   124,   198,   123,   123,   123,
     123,   124,   123,   209,   123,   209,   209,    42,   123,   125,
     179,   209,   124,   209,   124,   123,   123,   124,   124,   124,
     124,   123,    21,   200,   201,    11,   200,   201,   200,   200,
     200,   158,   198,    57,   142,   157,   182,   124,   123,   182,
      59,   175,   123,   123,   124,   200,   127,   128,   124,   209,
     124,   124,   124,     5,   148,   131,   131,   131,   209,   122,
     130,   124,   168,   124,   123,   123,   122,   171,   124,   123,
     167,   123,   209,   124,   124,   124,   124,    37,   182,    53,
     191,   193,   195,   197,   191,   191,   209,   182,   124,   182,
     181,   124,   124,   124,   124,   124,   200,   124,   201,   201,
     201,   124,     5,   200,   201,   124,   201,   124,   124,    57,
     123,   182,    57,    11,    21,   157,   124,    59,    37,   176,
      53,   192,   194,   196,   197,   209,   128,   200,     5,   124,
     124,   124,   123,   209,     4,   124,   124,   209,   124,   123,
     124,    39,   102,    52,   193,   195,    52,   102,    52,   195,
      52,   195,   124,   157,   182,   124,   124,   200,   201,   201,
     124,     5,   124,   124,    57,   200,   201,   200,   182,   157,
     182,    39,   102,    52,   194,   196,    52,   102,   124,     5,
     128,   124,   123,   131,   123,   124,   182,   124,   182,    52,
     124,   182,    52,    52,   189,   182,    57,   124,     5,   124,
     124,   157,   182,   124,   200,   124,    57,   182,    59,   176,
     124,   176,    52,   124,   176,   189,   124,     5,   122,   123,
      57,   124,   182,    57,   124,    59,   123,   124,   209,   182,
      57,   176,   123
};

/* YYR1[RULE-NUM] -- Symbol kind of the left-hand side of rule RULE-NUM.  */
static const yytype_uint8 yyr1[] =
{
       0,   135,   136,   137,   137,   138,   138,   139,   139,   140,
     140,   141,   141,   141,   142,   142,   143,   143,   143,   143,
     143,   143,   143,   143,   143,   144,   144,   145,   145,   145,
     145,   145,   145,   145,   145,   145,   145,   145,   145,   145,
     145,   146,   146,   146,   146,   147,   148,   148,   149,   149,
     150,   150,   150,   150,   150,   150,   150,   150,   150,   150,
     150,   150,   150,   150,   150,   150,   150,   151,   151,   151,
     151,   152,   153,   153,   153,   153,   153,   153,   153,   153,
     154,   154,   155,   155,   155,   155,   155,   155,   155,   155,
     155,   156,   156,   156,   156,   157,   157,   158,   158,   158,
     158,   158,   158,   158,   158,   158,   158,   158,   158,   158,
     159,   159,   159,   159,   159,   160,   160,   160,   161,   162,
     162,   163,   164,   164,   165,   165,   165,   165,   166,   166,
     166,   166,   166,   166,   166,   166,   166,   166,   166,   166,
     166,   167,   167,   168,   168,   168,   168,   169,   169,   169,
     169,   170,   170,   171,   171,   172,   172,   172,   172,   172,
     172,   173,   173,   173,   174,   175,   175,   176,   176,   176,
     176,   176,   176,   176,   176,   176,   176,   176,   176,   176,
     176,   176,   176,   176,   176,   177,   178,   178,   178,   178,
     179,   179,   180,   180,   181,   181,   181,   182,   182,   182,
     182,   182,   182,   182,   182,   182,   182,   182,   182,   182,
     182,   182,   182,   182,   182,   182,   182,   182,   182,   182,
     182,   182,   182,   182,   182,   182,   182,   182,   182,   182,
     182,   182,   182,   182,   182,   183,   183,   184,   184,   185,
     186,   187,   188,   189,   189,   190,   191,   191,   192,   192,
     193,   193,   194,   194,   195,   195,   196,   196,   197,   197,
     198,   198,   199,   199,   199,   199,   199,   199,   200,   200,
     201,   201,   201,   202,   203,   203,   203,   203,   203,   203,
     203,   203,   203,   203,   203,   203,   204,   204,   204,   204,
     204,   204,   204,   204,   204,   204,   204,   204,   204,   205,
     206,   206,   207,   207,   207,   208,   208,   208,   208,   208,
     208,   208,   208,   208,   209,   209,   209,   209,   209,   209,
     209,   209,   209,   209,   209,   209,   209,   209,   209,   209,
     209,   209,   209,   209,   209,   209,   209,   209,   209,   209,
     209,   209,   209,   209,   209,   209,   209,   209,   209,   209,
     209,   209,   209,   209,   209,   209,   209,   209,   209,   209,
     209,   209,   209,   209,   209,   209,   209,   209
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
       3,     2,     2,     3,     3,     2,     1,     3,     5,     3,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       5,     7,     6,     7,     6,     9,     2,     2,     2,     4,
       1,     1,     3,     1,     2,     2,     1,     3,     2,     2,
       5,     3,     4,     5,     4,     5,     5,     7,     3,     3,
       3,     4,     3,     5,     2,     3,     3,     4,     5,     6,
       7,     6,     6,     7,     6,     7,     3,     3,     2,     1,
       1,     1,     1,     5,     3,     3,     1,     3,     1,     3,
       9,     5,     5,     3,     1,     3,     2,     1,     2,     1,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     1,
       2,     1,     1,     2,     3,     3,     2,     1,     3,     1,
       5,     5,     5,     3,     1,     1,     1,     2,     2,     2,
       2,     2,     2,     3,     2,     2,     1,     1,     1,     1,
       1,     1,     2,     2,     1,     1,     1,     1,     1,     3,
       3,     1,     2,     1,     2,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     4,
       1,     1,     1,     1,     1,     1,     2,     3,     3,     2,
       5,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     4,     3,     1,     2,
       2,     2,     2,     2,     2,     2,     2,     2
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

#line 2962 "y.tab.c"

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

#line 387 "yaccs/verilog.yacc"

