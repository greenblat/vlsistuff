/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton implementation for Bison's Yacc-like parsers in C

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

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "2.3"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Using locations.  */
#define YYLSP_NEEDED 0



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
     logic = 268,
     tri0 = 269,
     tri1 = 270,
     signed = 271,
     event = 272,
     bin = 273,
     hex = 274,
     dig = 275,
     integer = 276,
     real = 277,
     wreal = 278,
     ubin = 279,
     uhex = 280,
     udig = 281,
     domino = 282,
     and_and = 283,
     or_or = 284,
     eq3 = 285,
     eq_eq = 286,
     not_eq = 287,
     gr_eq = 288,
     sm_eq = 289,
     always = 290,
     begin = 291,
     end = 292,
     if = 293,
     else = 294,
     posedge = 295,
     negedge = 296,
     or = 297,
     wait = 298,
     emit = 299,
     string = 300,
     defparam = 301,
     parameter = 302,
     localparam = 303,
     case = 304,
     casez = 305,
     casex = 306,
     endcase = 307,
     default = 308,
     initial = 309,
     forever = 310,
     function = 311,
     endfunction = 312,
     task = 313,
     endtask = 314,
     for = 315,
     while = 316,
     backtick_define = 317,
     backtick_include = 318,
     backtick_timescale = 319,
     backtick_undef = 320,
     define = 321,
     strong1 = 322,
     strong0 = 323,
     pull1 = 324,
     pull0 = 325,
     weak1 = 326,
     weak0 = 327,
     highz1 = 328,
     highz0 = 329,
     fork = 330,
     join = 331,
     disable = 332,
     pragma = 333,
     plus_range = 334,
     minus_range = 335,
     floating = 336,
     power = 337,
     star = 338,
     generate = 339,
     endgenerate = 340,
     genvar = 341,
     force = 342,
     release = 343,
     xnor = 344,
     nand = 345,
     nor = 346,
     repeat = 347,
     supply0 = 348,
     supply1 = 349,
     newver = 350,
     return = 351,
     arith_shift_right = 352,
     SignedLeft = 353,
     shift_right = 354,
     shift_left = 355,
     Veryequal = 356,
     noteqeq = 357,
     StarStar = 358,
     UNARY_PREC = 359
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
#define pragma 333
#define plus_range 334
#define minus_range 335
#define floating 336
#define power 337
#define star 338
#define generate 339
#define endgenerate 340
#define genvar 341
#define force 342
#define release 343
#define xnor 344
#define nand 345
#define nor 346
#define repeat 347
#define supply0 348
#define supply1 349
#define newver 350
#define return 351
#define arith_shift_right 352
#define SignedLeft 353
#define shift_right 354
#define shift_left 355
#define Veryequal 356
#define noteqeq 357
#define StarStar 358
#define UNARY_PREC 359




/* Copy the first part of user declarations.  */


/* Enabling traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 0
#endif

/* Enabling the token table.  */
#ifndef YYTOKEN_TABLE
# define YYTOKEN_TABLE 0
#endif

#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif



/* Copy the second part of user declarations.  */


/* Line 216 of yacc.c.  */
#line 315 "y.tab.c"

#ifdef short
# undef short
#endif

#ifdef YYTYPE_UINT8
typedef YYTYPE_UINT8 yytype_uint8;
#else
typedef unsigned char yytype_uint8;
#endif

#ifdef YYTYPE_INT8
typedef YYTYPE_INT8 yytype_int8;
#elif (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
typedef signed char yytype_int8;
#else
typedef short int yytype_int8;
#endif

#ifdef YYTYPE_UINT16
typedef YYTYPE_UINT16 yytype_uint16;
#else
typedef unsigned short int yytype_uint16;
#endif

#ifdef YYTYPE_INT16
typedef YYTYPE_INT16 yytype_int16;
#else
typedef short int yytype_int16;
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif ! defined YYSIZE_T && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned int
# endif
#endif

#define YYSIZE_MAXIMUM ((YYSIZE_T) -1)

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(msgid) dgettext ("bison-runtime", msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(msgid) msgid
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(e) ((void) (e))
#else
# define YYUSE(e) /* empty */
#endif

/* Identity function, used to suppress warnings about constant conditions.  */
#ifndef lint
# define YYID(n) (n)
#else
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static int
YYID (int i)
#else
static int
YYID (i)
    int i;
#endif
{
  return i;
}
#endif

#if ! defined yyoverflow || YYERROR_VERBOSE

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
#    if ! defined _ALLOCA_H && ! defined _STDLIB_H && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#     ifndef _STDLIB_H
#      define _STDLIB_H 1
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's `empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (YYID (0))
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
#  if (defined __cplusplus && ! defined _STDLIB_H \
       && ! ((defined YYMALLOC || defined malloc) \
	     && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef _STDLIB_H
#    define _STDLIB_H 1
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined _STDLIB_H && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined _STDLIB_H && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined yyoverflow || YYERROR_VERBOSE */


#if (! defined yyoverflow \
     && (! defined __cplusplus \
	 || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yytype_int16 yyss;
  YYSTYPE yyvs;
  };

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (sizeof (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (sizeof (yytype_int16) + sizeof (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

/* Copy COUNT objects from FROM to TO.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(To, From, Count) \
      __builtin_memcpy (To, From, (Count) * sizeof (*(From)))
#  else
#   define YYCOPY(To, From, Count)		\
      do					\
	{					\
	  YYSIZE_T yyi;				\
	  for (yyi = 0; yyi < (Count); yyi++)	\
	    (To)[yyi] = (From)[yyi];		\
	}					\
      while (YYID (0))
#  endif
# endif

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack)					\
    do									\
      {									\
	YYSIZE_T yynewbytes;						\
	YYCOPY (&yyptr->Stack, Stack, yysize);				\
	Stack = &yyptr->Stack;						\
	yynewbytes = yystacksize * sizeof (*Stack) + YYSTACK_GAP_MAXIMUM; \
	yyptr += yynewbytes / sizeof (*yyptr);				\
      }									\
    while (YYID (0))

#endif

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  12
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   5547

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  131
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  70
/* YYNRULES -- Number of rules.  */
#define YYNRULES  353
/* YYNRULES -- Number of states.  */
#define YYNSTATES  786

/* YYTRANSLATE(YYLEX) -- Bison symbol number corresponding to YYLEX.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   359

#define YYTRANSLATE(YYX)						\
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[YYLEX] -- Bison symbol number corresponding to YYLEX.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   129,     2,   117,     2,   114,   101,     2,
     118,   119,   112,   108,   121,   109,   123,   113,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,    98,   120,
     106,   122,   107,    97,   124,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,   125,     2,   126,   100,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   127,    99,   128,   130,     2,     2,     2,
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
      95,    96,   102,   103,   104,   105,   110,   111,   115,   116
};

#if YYDEBUG
/* YYPRHS[YYN] -- Index of the first RHS symbol of rule number YYN in
   YYRHS.  */
static const yytype_uint16 yyprhs[] =
{
       0,     0,     3,     5,     8,    10,    12,    14,    21,    26,
      30,    31,    33,    38,    42,    46,    48,    51,    55,    59,
      64,    69,    71,    76,    82,    85,    86,    88,    90,    92,
      94,    96,    98,   100,   102,   104,   106,   108,   110,   112,
     114,   117,   120,   124,   131,   134,   138,   142,   146,   152,
     157,   163,   168,   175,   181,   187,   195,   200,   205,   212,
     218,   222,   229,   237,   244,   250,   252,   254,   256,   258,
     260,   262,   264,   266,   268,   270,   277,   283,   292,   300,
     307,   316,   326,   336,   347,   354,   360,   369,   379,   382,
     384,   388,   392,   396,   401,   407,   413,   420,   424,   429,
     435,   440,   444,   449,   453,   458,   463,   469,   475,   479,
     484,   490,   494,   498,   502,   504,   508,   510,   514,   518,
     520,   525,   531,   535,   541,   548,   552,   558,   565,   572,
     579,   586,   592,   600,   609,   617,   625,   629,   631,   634,
     640,   645,   650,   653,   656,   659,   663,   665,   671,   674,
     679,   682,   685,   688,   693,   697,   700,   704,   708,   711,
     713,   717,   723,   727,   729,   731,   733,   735,   737,   739,
     741,   743,   745,   751,   759,   769,   772,   775,   778,   783,
     785,   787,   791,   793,   796,   799,   801,   805,   808,   811,
     817,   821,   826,   832,   837,   843,   849,   857,   861,   865,
     869,   874,   878,   884,   887,   891,   895,   900,   906,   913,
     921,   928,   935,   943,   950,   958,   962,   966,   969,   971,
     973,   975,   978,   980,   986,   990,  1000,  1006,  1012,  1016,
    1018,  1022,  1025,  1027,  1031,  1035,  1039,  1043,  1047,  1049,
    1052,  1054,  1056,  1059,  1063,  1067,  1070,  1072,  1074,  1078,
    1080,  1086,  1092,  1098,  1102,  1104,  1106,  1108,  1111,  1114,
    1117,  1120,  1123,  1126,  1130,  1133,  1136,  1138,  1140,  1142,
    1144,  1146,  1148,  1151,  1154,  1156,  1158,  1160,  1162,  1164,
    1168,  1172,  1174,  1177,  1179,  1182,  1186,  1190,  1195,  1200,
    1207,  1209,  1211,  1213,  1215,  1217,  1219,  1221,  1223,  1225,
    1227,  1229,  1231,  1233,  1235,  1237,  1242,  1244,  1246,  1248,
    1250,  1252,  1254,  1257,  1261,  1265,  1268,  1274,  1278,  1282,
    1286,  1290,  1294,  1298,  1302,  1306,  1310,  1314,  1318,  1322,
    1326,  1330,  1334,  1338,  1342,  1346,  1350,  1354,  1358,  1362,
    1366,  1370,  1374,  1379,  1383,  1385,  1388,  1391,  1394,  1397,
    1400,  1403,  1406,  1409
};

/* YYRHS -- A `-1'-separated list of the rules' RHS.  */
static const yytype_int16 yyrhs[] =
{
     132,     0,    -1,   133,    -1,   133,   134,    -1,   134,    -1,
     135,    -1,   142,    -1,     3,     5,   136,   137,   140,     6,
      -1,   117,   118,   160,   119,    -1,   117,   118,   119,    -1,
      -1,   120,    -1,   118,   138,   119,   120,    -1,   118,   119,
     120,    -1,   138,   121,   139,    -1,   139,    -1,   193,     5,
      -1,   193,   191,     5,    -1,   193,    21,     5,    -1,   193,
     191,     5,   191,    -1,   193,   191,   191,     5,    -1,     5,
      -1,   193,     5,   122,   199,    -1,   193,   191,     5,   122,
     199,    -1,   141,   140,    -1,    -1,   144,    -1,   145,    -1,
     162,    -1,   169,    -1,   170,    -1,   153,    -1,   154,    -1,
     155,    -1,   143,    -1,   149,    -1,   150,    -1,   142,    -1,
      78,    -1,    95,    -1,    66,    45,    -1,    66,     5,    -1,
      66,     5,   200,    -1,    66,     4,     5,   113,     4,     5,
      -1,    54,   178,    -1,   193,   190,   120,    -1,    17,   190,
     120,    -1,   194,   190,   120,    -1,   194,   190,   122,   200,
     120,    -1,   193,   191,   190,   120,    -1,   193,   191,   190,
     191,   120,    -1,   194,   191,   190,   120,    -1,   194,   191,
       5,   122,   200,   120,    -1,   194,   191,     5,   191,   120,
      -1,   194,   191,   191,   190,   120,    -1,   194,   191,   191,
       5,   122,   200,   120,    -1,   194,     5,   191,   120,    -1,
     194,   168,   190,   120,    -1,   194,   168,     5,   122,   200,
     120,    -1,     5,    27,     5,     5,   120,    -1,     7,   182,
     120,    -1,     7,   165,   189,   122,   200,   120,    -1,     7,
     146,   165,   189,   122,   200,   120,    -1,     7,   146,   189,
     122,   200,   120,    -1,   118,   147,   121,   147,   119,    -1,
      67,    -1,    68,    -1,    69,    -1,    70,    -1,    71,    -1,
      72,    -1,    73,    -1,    74,    -1,   191,    -1,    21,    -1,
      56,     5,   120,   151,   188,    57,    -1,    56,     5,   120,
     188,    57,    -1,    56,   191,   191,     5,   120,   151,   178,
      57,    -1,    56,   148,     5,   120,   151,   178,    57,    -1,
      56,   148,     5,   120,   178,    57,    -1,    56,     5,   118,
     138,   119,   120,   178,    57,    -1,    56,     5,   118,   138,
     119,   120,   151,   178,    57,    -1,    56,   148,     5,   118,
     138,   119,   120,   178,    57,    -1,    56,   148,     5,   118,
     138,   119,   120,   151,   178,    57,    -1,    58,     5,   120,
     151,   178,    59,    -1,    58,     5,   120,   178,    59,    -1,
      58,     5,   118,   138,   119,   120,   178,    59,    -1,    58,
       5,   118,   138,   119,   120,   151,   178,    59,    -1,   151,
     152,    -1,   152,    -1,    11,   190,   120,    -1,    22,   190,
     120,    -1,    23,   190,   120,    -1,    11,   191,   190,   120,
      -1,    11,   191,     5,   191,   120,    -1,    11,   191,   191,
       5,   120,    -1,     9,    11,   191,   191,     5,   120,    -1,
       8,   190,   120,    -1,     8,   190,   191,   120,    -1,     8,
     191,   191,   190,   120,    -1,     8,    21,   190,   120,    -1,
      21,   190,   120,    -1,    21,   190,   191,   120,    -1,    47,
     158,   120,    -1,    47,    16,   158,   120,    -1,    47,   191,
     158,   120,    -1,    47,   191,   191,   158,   120,    -1,    47,
      16,   191,   158,   120,    -1,    48,   158,   120,    -1,    48,
     191,   158,   120,    -1,    48,   191,   191,   158,   120,    -1,
      46,   157,   120,    -1,   198,   122,   200,    -1,   157,   121,
     156,    -1,   156,    -1,   158,   121,   159,    -1,   159,    -1,
       5,   122,   200,    -1,   160,   121,   161,    -1,   161,    -1,
      47,     5,   122,   200,    -1,    47,   191,     5,   122,   200,
      -1,     5,   122,   200,    -1,     5,     5,   118,   119,   120,
      -1,     5,   168,     5,   118,   119,   120,    -1,     5,     5,
     120,    -1,    42,   118,   187,   119,   120,    -1,    42,     5,
     118,   187,   119,   120,    -1,     5,     5,   118,   163,   119,
     120,    -1,    42,     5,   118,   163,   119,   120,    -1,     5,
       5,   118,   187,   119,   120,    -1,     5,   118,   187,   119,
     120,    -1,     5,   168,     5,   118,   163,   119,   120,    -1,
       5,   168,     5,   191,   118,   163,   119,   120,    -1,     5,
       5,   191,   118,   163,   119,   120,    -1,     5,     5,   191,
     118,   187,   119,   120,    -1,   163,   121,   164,    -1,   164,
      -1,   123,   112,    -1,   123,     5,   118,   200,   119,    -1,
     123,     5,   118,   119,    -1,   117,   118,   187,   119,    -1,
     117,     4,    -1,   117,     5,    -1,   117,    81,    -1,   166,
     121,   167,    -1,   167,    -1,   123,     5,   118,   200,   119,
      -1,   123,     5,    -1,   117,   118,   187,   119,    -1,   117,
       4,    -1,   117,    81,    -1,   117,     5,    -1,   117,   118,
     166,   119,    -1,   117,   118,   119,    -1,    35,   178,    -1,
      35,   174,   178,    -1,    84,   171,    85,    -1,   171,   172,
      -1,   172,    -1,    36,   171,    37,    -1,    36,    98,     5,
     171,    37,    -1,    86,     5,   120,    -1,   144,    -1,   145,
      -1,   153,    -1,   154,    -1,   155,    -1,   162,    -1,   173,
      -1,   169,    -1,   143,    -1,    38,   118,   200,   119,   172,
      -1,    38,   118,   200,   119,   172,    39,   172,    -1,    60,
     118,   182,   120,   200,   120,   182,   119,   172,    -1,   124,
     112,    -1,   124,    83,    -1,   124,     5,    -1,   124,   118,
     176,   119,    -1,    42,    -1,   121,    -1,   176,   175,   177,
      -1,   177,    -1,    40,   200,    -1,    41,   200,    -1,   200,
      -1,    36,   188,    37,    -1,    36,    37,    -1,    55,   178,
      -1,    36,    98,     5,   188,    37,    -1,    75,   188,    76,
      -1,   189,   122,   200,   120,    -1,   189,   122,   165,   200,
     120,    -1,   189,    34,   200,   120,    -1,   189,    34,   165,
     200,   120,    -1,    38,   118,   200,   119,   178,    -1,    38,
     118,   200,   119,   178,    39,   178,    -1,    43,   200,   120,
      -1,    21,   190,   120,    -1,    11,   190,   120,    -1,    11,
     191,   190,   120,    -1,    88,   200,   120,    -1,    87,   200,
     122,   200,   120,    -1,   174,   120,    -1,    44,     5,   120,
      -1,    77,     5,   120,    -1,     5,   118,   119,   120,    -1,
       5,   118,   187,   119,   120,    -1,    49,   118,   200,   119,
     184,    52,    -1,    49,   118,   200,   119,   184,   186,    52,
      -1,    49,   118,   200,   119,   186,    52,    -1,    50,   118,
     200,   119,   184,    52,    -1,    50,   118,   200,   119,   184,
     186,    52,    -1,    51,   118,   200,   119,   184,    52,    -1,
      51,   118,   200,   119,   184,   186,    52,    -1,   117,   200,
     120,    -1,   117,   200,   178,    -1,     5,   120,    -1,   179,
      -1,   180,    -1,   181,    -1,   198,   120,    -1,    78,    -1,
       7,   189,   122,   200,   120,    -1,    96,     5,   120,    -1,
      60,   118,   182,   120,   200,   120,   182,   119,   178,    -1,
      92,   118,   200,   119,   178,    -1,    61,   118,   200,   119,
     178,    -1,   182,   121,   183,    -1,   183,    -1,   189,   122,
     200,    -1,   184,   185,    -1,   185,    -1,   187,    98,   178,
      -1,   187,    98,   120,    -1,    53,    98,   178,    -1,    53,
      98,   120,    -1,   187,   121,   200,    -1,   200,    -1,   188,
     178,    -1,   178,    -1,     5,    -1,     5,   191,    -1,     5,
     192,   191,    -1,     5,   192,   192,    -1,     5,   192,    -1,
     198,    -1,   195,    -1,     5,   121,   190,    -1,     5,    -1,
     125,   200,    98,   200,   126,    -1,   125,   200,    79,   200,
     126,    -1,   125,   200,    80,   200,   126,    -1,   125,   200,
     126,    -1,     8,    -1,     9,    -1,    10,    -1,     9,    11,
      -1,     8,    12,    -1,     9,    12,    -1,    10,    12,    -1,
       8,    16,    -1,     9,    16,    -1,     9,    11,    16,    -1,
       9,    13,    -1,     8,    13,    -1,    13,    -1,    11,    -1,
      12,    -1,    16,    -1,    21,    -1,    22,    -1,    11,    16,
      -1,    12,    16,    -1,    86,    -1,    93,    -1,    94,    -1,
      14,    -1,    15,    -1,   127,   196,   128,    -1,   196,   121,
     197,    -1,   197,    -1,   200,   195,    -1,   200,    -1,   105,
     195,    -1,     5,   123,   198,    -1,     5,   123,     5,    -1,
       5,   123,     5,   191,    -1,     5,   123,     5,   192,    -1,
       5,   123,     5,   118,   200,   119,    -1,     4,    -1,    81,
      -1,    45,    -1,    18,    -1,    19,    -1,    20,    -1,    24,
      -1,    25,    -1,    26,    -1,     5,    -1,   198,    -1,     4,
      -1,    81,    -1,    45,    -1,    66,    -1,    66,   118,   200,
     119,    -1,    18,    -1,    19,    -1,    20,    -1,    24,    -1,
      25,    -1,    26,    -1,     5,   191,    -1,     5,   192,   191,
      -1,     5,   192,   192,    -1,     5,   192,    -1,   200,    97,
     200,    98,   200,    -1,   200,   108,   200,    -1,   200,   112,
     200,    -1,   200,   109,   200,    -1,   200,   113,   200,    -1,
     200,   114,   200,    -1,   200,   100,   200,    -1,   200,    99,
     200,    -1,   200,   101,   200,    -1,   200,   106,   200,    -1,
     200,   107,   200,    -1,   200,    82,   200,    -1,   200,    28,
     200,    -1,   200,    29,   200,    -1,   200,    89,   200,    -1,
     200,    90,   200,    -1,   200,    91,   200,    -1,   200,    31,
     200,    -1,   200,    30,   200,    -1,   200,    32,   200,    -1,
     200,   111,   200,    -1,   200,    33,   200,    -1,   200,    34,
     200,    -1,   200,   105,   200,    -1,   200,   104,   200,    -1,
     200,   102,   200,    -1,     5,   118,   187,   119,    -1,   118,
     200,   119,    -1,   195,    -1,   109,   200,    -1,    99,   200,
      -1,   101,   200,    -1,   100,   200,    -1,    89,   200,    -1,
      91,   200,    -1,    90,   200,    -1,   129,   200,    -1,   130,
     200,    -1
};

/* YYRLINE[YYN] -- source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,    44,    44,    45,    45,    46,    46,    47,    49,    49,
      49,    50,    50,    50,    51,    51,    53,    53,    53,    53,
      53,    53,    53,    53,    57,    57,    60,    61,    62,    63,
      64,    65,    66,    67,    68,    69,    70,    71,    72,    73,
      77,    77,    77,    77,    78,    80,    81,    82,    83,    84,
      85,    86,    87,    88,    89,    90,    91,    92,    93,    94,
      98,    99,   100,   101,   104,   105,   105,   105,   105,   105,
     105,   105,   105,   106,   106,   108,   109,   110,   111,   112,
     113,   114,   115,   116,   119,   120,   121,   122,   125,   125,
     127,   128,   129,   130,   131,   132,   133,   134,   135,   136,
     137,   138,   139,   143,   144,   145,   146,   147,   149,   149,
     149,   150,   151,   152,   152,   154,   154,   155,   157,   157,
     159,   160,   161,   165,   166,   167,   168,   169,   170,   171,
     172,   173,   174,   175,   176,   177,   185,   185,   186,   186,
     186,   188,   188,   188,   188,   189,   189,   190,   190,   191,
     191,   191,   191,   191,   191,   194,   194,   197,   199,   199,
     202,   203,   204,   205,   206,   207,   208,   209,   210,   211,
     212,   213,   214,   215,   220,   225,   225,   225,   225,   226,
     226,   227,   227,   228,   228,   228,   233,   234,   235,   236,
     237,   238,   239,   240,   241,   242,   243,   244,   245,   246,
     247,   248,   249,   250,   251,   252,   253,   254,   255,   256,
     257,   258,   259,   260,   261,   262,   263,   264,   265,   266,
     267,   268,   269,   270,   271,   274,   275,   276,   277,   277,
     278,   279,   279,   280,   280,   281,   281,   283,   283,   284,
     284,   287,   287,   287,   287,   287,   287,   287,   289,   289,
     291,   291,   291,   292,   294,   294,   294,   294,   294,   294,
     294,   294,   294,   294,   294,   294,   296,   296,   296,   296,
     296,   296,   296,   296,   296,   296,   296,   296,   296,   298,
     299,   299,   301,   302,   303,   307,   308,   309,   310,   311,
     315,   316,   317,   318,   318,   318,   318,   318,   318,   322,
     323,   324,   325,   326,   327,   328,   329,   329,   329,   329,
     329,   329,   330,   331,   332,   333,   334,   335,   336,   337,
     338,   339,   340,   341,   342,   343,   344,   345,   346,   347,
     348,   349,   350,   351,   352,   353,   354,   355,   356,   357,
     358,   359,   360,   361,   362,   363,   364,   365,   366,   367,
     368,   369,   370,   371
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || YYTOKEN_TABLE
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "module", "number", "token", "endmodule",
  "assign", "input", "output", "inout", "reg", "wire", "logic", "tri0",
  "tri1", "signed", "event", "bin", "hex", "dig", "integer", "real",
  "wreal", "ubin", "uhex", "udig", "domino", "and_and", "or_or", "eq3",
  "eq_eq", "not_eq", "gr_eq", "sm_eq", "always", "begin", "end", "if",
  "else", "posedge", "negedge", "or", "wait", "emit", "string", "defparam",
  "parameter", "localparam", "case", "casez", "casex", "endcase",
  "default", "initial", "forever", "function", "endfunction", "task",
  "endtask", "for", "while", "backtick_define", "backtick_include",
  "backtick_timescale", "backtick_undef", "define", "strong1", "strong0",
  "pull1", "pull0", "weak1", "weak0", "highz1", "highz0", "fork", "join",
  "disable", "pragma", "plus_range", "minus_range", "floating", "power",
  "star", "generate", "endgenerate", "genvar", "force", "release", "xnor",
  "nand", "nor", "repeat", "supply0", "supply1", "newver", "return", "'?'",
  "':'", "'|'", "'^'", "'&'", "arith_shift_right", "SignedLeft",
  "shift_right", "shift_left", "'<'", "'>'", "'+'", "'-'", "Veryequal",
  "noteqeq", "'*'", "'/'", "'%'", "StarStar", "UNARY_PREC", "'#'", "'('",
  "')'", "';'", "','", "'='", "'.'", "'@'", "'['", "']'", "'{'", "'}'",
  "'!'", "'~'", "$accept", "Main", "Mains", "MainItem", "Module",
  "Hparams", "Header", "Header_list", "Header_item", "Module_stuffs",
  "Mstuff", "Define", "Initial", "Definition", "Assign", "StrengthDef",
  "Strength", "WidthInt", "Function", "Task", "Mem_defs", "Mem_def",
  "Parameter", "Localparam", "Defparam", "DottedPair", "DottedPairs",
  "Pairs", "Pair", "head_params", "head_param", "Instance", "Conns_list",
  "Connection", "AssignParams", "Prms_list", "PrmAssign", "InstParams",
  "Always", "Generate", "GenStatements", "GenStatement",
  "GenFor_statement", "When", "Or_coma", "When_items", "When_item",
  "Statement", "For_statement", "Repeat_statement", "While_statement",
  "Soft_assigns", "Soft_assign", "Cases", "Case", "Default", "Exprs",
  "Statements", "LSH", "Tokens_list", "Width", "BusBit", "ExtDir",
  "IntDir", "CurlyList", "CurlyItems", "CurlyItem", "Dotted", "Literal",
  "Expr", 0
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[YYLEX-NUM] -- Internal token number corresponding to
   token YYLEX-NUM.  */
static const yytype_uint16 yytoknum[] =
{
       0,   256,   257,   258,   259,   260,   261,   262,   263,   264,
     265,   266,   267,   268,   269,   270,   271,   272,   273,   274,
     275,   276,   277,   278,   279,   280,   281,   282,   283,   284,
     285,   286,   287,   288,   289,   290,   291,   292,   293,   294,
     295,   296,   297,   298,   299,   300,   301,   302,   303,   304,
     305,   306,   307,   308,   309,   310,   311,   312,   313,   314,
     315,   316,   317,   318,   319,   320,   321,   322,   323,   324,
     325,   326,   327,   328,   329,   330,   331,   332,   333,   334,
     335,   336,   337,   338,   339,   340,   341,   342,   343,   344,
     345,   346,   347,   348,   349,   350,   351,    63,    58,   124,
      94,    38,   352,   353,   354,   355,    60,    62,    43,    45,
     356,   357,    42,    47,    37,   358,   359,    35,    40,    41,
      59,    44,    61,    46,    64,    91,    93,   123,   125,    33,
     126
};
# endif

/* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint8 yyr1[] =
{
       0,   131,   132,   133,   133,   134,   134,   135,   136,   136,
     136,   137,   137,   137,   138,   138,   139,   139,   139,   139,
     139,   139,   139,   139,   140,   140,   141,   141,   141,   141,
     141,   141,   141,   141,   141,   141,   141,   141,   141,   141,
     142,   142,   142,   142,   143,   144,   144,   144,   144,   144,
     144,   144,   144,   144,   144,   144,   144,   144,   144,   144,
     145,   145,   145,   145,   146,   147,   147,   147,   147,   147,
     147,   147,   147,   148,   148,   149,   149,   149,   149,   149,
     149,   149,   149,   149,   150,   150,   150,   150,   151,   151,
     152,   152,   152,   152,   152,   152,   152,   152,   152,   152,
     152,   152,   152,   153,   153,   153,   153,   153,   154,   154,
     154,   155,   156,   157,   157,   158,   158,   159,   160,   160,
     161,   161,   161,   162,   162,   162,   162,   162,   162,   162,
     162,   162,   162,   162,   162,   162,   163,   163,   164,   164,
     164,   165,   165,   165,   165,   166,   166,   167,   167,   168,
     168,   168,   168,   168,   168,   169,   169,   170,   171,   171,
     172,   172,   172,   172,   172,   172,   172,   172,   172,   172,
     172,   172,   172,   172,   173,   174,   174,   174,   174,   175,
     175,   176,   176,   177,   177,   177,   178,   178,   178,   178,
     178,   178,   178,   178,   178,   178,   178,   178,   178,   178,
     178,   178,   178,   178,   178,   178,   178,   178,   178,   178,
     178,   178,   178,   178,   178,   178,   178,   178,   178,   178,
     178,   178,   178,   178,   178,   179,   180,   181,   182,   182,
     183,   184,   184,   185,   185,   186,   186,   187,   187,   188,
     188,   189,   189,   189,   189,   189,   189,   189,   190,   190,
     191,   191,   191,   192,   193,   193,   193,   193,   193,   193,
     193,   193,   193,   193,   193,   193,   194,   194,   194,   194,
     194,   194,   194,   194,   194,   194,   194,   194,   194,   195,
     196,   196,   197,   197,   197,   198,   198,   198,   198,   198,
     199,   199,   199,   199,   199,   199,   199,   199,   199,   200,
     200,   200,   200,   200,   200,   200,   200,   200,   200,   200,
     200,   200,   200,   200,   200,   200,   200,   200,   200,   200,
     200,   200,   200,   200,   200,   200,   200,   200,   200,   200,
     200,   200,   200,   200,   200,   200,   200,   200,   200,   200,
     200,   200,   200,   200,   200,   200,   200,   200,   200,   200,
     200,   200,   200,   200
};

/* YYR2[YYN] -- Number of symbols composing right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     1,     2,     1,     1,     1,     6,     4,     3,
       0,     1,     4,     3,     3,     1,     2,     3,     3,     4,
       4,     1,     4,     5,     2,     0,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       2,     2,     3,     6,     2,     3,     3,     3,     5,     4,
       5,     4,     6,     5,     5,     7,     4,     4,     6,     5,
       3,     6,     7,     6,     5,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     6,     5,     8,     7,     6,
       8,     9,     9,    10,     6,     5,     8,     9,     2,     1,
       3,     3,     3,     4,     5,     5,     6,     3,     4,     5,
       4,     3,     4,     3,     4,     4,     5,     5,     3,     4,
       5,     3,     3,     3,     1,     3,     1,     3,     3,     1,
       4,     5,     3,     5,     6,     3,     5,     6,     6,     6,
       6,     5,     7,     8,     7,     7,     3,     1,     2,     5,
       4,     4,     2,     2,     2,     3,     1,     5,     2,     4,
       2,     2,     2,     4,     3,     2,     3,     3,     2,     1,
       3,     5,     3,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     5,     7,     9,     2,     2,     2,     4,     1,
       1,     3,     1,     2,     2,     1,     3,     2,     2,     5,
       3,     4,     5,     4,     5,     5,     7,     3,     3,     3,
       4,     3,     5,     2,     3,     3,     4,     5,     6,     7,
       6,     6,     7,     6,     7,     3,     3,     2,     1,     1,
       1,     2,     1,     5,     3,     9,     5,     5,     3,     1,
       3,     2,     1,     3,     3,     3,     3,     3,     1,     2,
       1,     1,     2,     3,     3,     2,     1,     1,     3,     1,
       5,     5,     5,     3,     1,     1,     1,     2,     2,     2,
       2,     2,     2,     3,     2,     2,     1,     1,     1,     1,
       1,     1,     2,     2,     1,     1,     1,     1,     1,     3,
       3,     1,     2,     1,     2,     3,     3,     4,     4,     6,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     4,     1,     1,     1,     1,
       1,     1,     2,     3,     3,     2,     5,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     4,     3,     1,     2,     2,     2,     2,     2,
       2,     2,     2,     2
};

/* YYDEFACT[STATE-NAME] -- Default rule to reduce with in state
   STATE-NUM when YYTABLE doesn't specify something else to do.  Zero
   means the default is an error.  */
static const yytype_uint16 yydefact[] =
{
       0,     0,     0,     0,     2,     4,     5,     6,    10,     0,
      41,    40,     1,     3,     0,     0,     0,   301,   299,   306,
     307,   308,   309,   310,   311,   303,   304,   302,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   344,
     300,    42,     0,     0,    11,    25,     0,     0,     0,     0,
     312,   315,     0,   349,   351,   350,   346,   348,   347,   345,
       0,     0,     0,   281,   283,   352,   353,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     9,     0,   119,    21,   254,
     255,   256,     0,     0,    15,     0,     0,     0,   267,   268,
     266,   277,   278,   269,     0,   270,   271,     0,     0,     0,
       0,     0,     0,     0,     0,    38,     0,   274,   275,   276,
      39,     0,    25,    37,    34,    26,    27,    35,    36,    31,
      32,    33,    28,    29,    30,     0,     0,     0,     0,   238,
     286,   285,     0,   313,   314,     0,   343,   284,     0,   279,
     282,   328,   329,   334,   333,   335,   337,   338,   327,   330,
     331,   332,     0,   323,   322,   324,   341,   340,   339,   325,
     326,   317,   319,   336,   318,   320,   321,     0,     0,     0,
       0,     8,     0,   258,   265,   261,   257,   259,   264,   262,
     260,    13,     0,     0,    16,     0,     0,     0,     0,     0,
       0,     0,   241,     0,     0,     0,     0,     0,   229,     0,
     247,   246,   272,   273,   249,     0,   241,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   222,     0,     0,     0,     0,     0,     0,     0,
     155,   218,   219,   220,     0,   246,     0,     0,     0,   114,
       0,     0,     0,     0,     0,   116,     0,     0,     0,     0,
      44,     0,    74,     0,    73,     0,     0,     0,     0,   274,
     171,   163,   164,   165,   166,   167,   168,   170,     0,   159,
     169,     7,    24,     0,     0,   249,     0,     0,     0,    43,
     342,     0,     0,   287,   288,     0,     0,     0,   253,   305,
     280,     0,   122,     0,     0,     0,   118,   263,    12,    14,
       0,    18,    17,     0,     0,   125,     0,     0,   150,   152,
     151,     0,     0,     0,   242,   245,   142,   143,   144,     0,
      65,    66,    67,    68,    69,    70,    71,    72,     0,     0,
       0,     0,    60,     0,     0,     0,    46,     0,   217,     0,
       0,     0,     0,   187,     0,   240,     0,     0,     0,     0,
       0,     0,     0,   188,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   177,   176,   175,     0,   203,   156,     0,
       0,   221,     0,     0,   111,     0,     0,     0,     0,     0,
     103,     0,     0,     0,   108,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   157,   158,
      45,     0,     0,   249,     0,    47,     0,   249,     0,     0,
     237,     0,     0,     0,     0,   316,   120,     0,   290,   293,
     294,   295,   296,   297,   298,   292,   291,    22,     0,    19,
      20,     0,     0,     0,   137,     0,     0,     0,   154,     0,
       0,   146,     0,     0,     0,     0,   243,   244,     0,     0,
       0,     0,     0,   228,   230,   248,     0,     0,     0,   199,
       0,   198,     0,   186,   239,     0,   197,   204,     0,     0,
       0,     0,     0,   190,   205,     0,   201,     0,   224,   215,
     216,     0,     0,     0,   182,   185,     0,     0,     0,     0,
       0,     0,     0,   113,   112,   117,   104,     0,   115,   105,
       0,   109,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    89,     0,     0,     0,     0,     0,     0,     0,     0,
     160,     0,     0,   162,    49,     0,    56,     0,    57,     0,
       0,     0,    51,   249,     0,   289,   251,   252,   250,   121,
      23,   123,     0,   138,     0,     0,     0,     0,     0,    59,
     148,   153,     0,   149,   131,     0,     0,     0,   141,     0,
       0,     0,     0,   206,     0,     0,   200,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   183,   184,   179,   178,
     180,     0,     0,   193,     0,   191,     0,     0,   126,   107,
     106,   110,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    88,     0,    76,     0,     0,     0,     0,     0,
       0,    85,     0,     0,     0,    50,     0,    48,     0,    53,
       0,    54,     0,   128,   136,   130,     0,     0,     0,   145,
     124,     0,     0,    64,     0,    63,    61,   207,   223,   189,
     195,     0,     0,   232,     0,     0,     0,     0,     0,   227,
     202,   226,   181,   194,   192,   129,   127,     0,     0,    97,
       0,     0,     0,    90,   249,     0,     0,   101,     0,    91,
      92,    75,     0,     0,    79,     0,     0,     0,     0,    84,
     161,   172,     0,    58,    52,     0,   140,     0,   134,   135,
       0,   132,     0,    62,     0,     0,   208,   231,     0,   210,
       0,   211,     0,   213,     0,     0,     0,     0,   100,    98,
       0,     0,     0,    93,     0,   102,     0,    78,     0,     0,
       0,     0,     0,     0,     0,     0,    55,   139,   147,   133,
     196,   236,   235,   209,   234,   233,   212,   214,     0,     0,
      80,    99,     0,    94,    95,     0,     0,    90,     0,   101,
      77,     0,    86,   173,     0,     0,    81,    96,     0,    82,
      93,    87,     0,   225,    83,   174
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,     3,     4,     5,     6,    15,    45,   103,   104,   131,
     132,     7,   280,   281,   282,   215,   348,   273,   137,   138,
     530,   531,   283,   284,   285,   259,   260,   264,   265,    96,
      97,   286,   453,   454,   216,   460,   461,   211,   287,   144,
     288,   289,   290,   269,   601,   503,   504,   365,   251,   252,
     253,   217,   218,   662,   663,   664,   665,   366,   254,   225,
     334,   335,   145,   146,    39,    62,    63,    40,   447,   149
};

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
#define YYPACT_NINF -561
static const yytype_int16 yypact[] =
{
      45,    12,    48,    36,    45,  -561,  -561,  -561,   -90,    42,
    1778,  -561,  -561,  -561,   -57,    73,   -41,  -561,   -36,  -561,
    -561,  -561,  -561,  -561,  -561,  -561,   -40,  -561,  1778,  1778,
    1778,  1778,  1778,  1778,  1778,  1778,  1414,  1778,  1778,  -561,
    -561,  5341,    10,    55,  -561,  4934,   104,  1778,   120,  1778,
    -561,   119,  1778,  -561,  -561,  -561,  -561,  -561,  -561,  -561,
    4104,   126,   -55,  -561,  2679,  -561,  -561,  1778,  1778,  1778,
    1778,  1778,  1778,  1778,  1778,  1778,  1778,  1778,  1778,  1778,
    1778,  1778,  1778,  1778,  1778,  1778,  1778,  1778,  1778,  1778,
    1778,  1778,  1778,   140,    33,  -561,   124,  -561,  -561,   323,
     262,   244,   146,   158,  -561,     7,    63,     6,   254,   291,
    -561,  -561,  -561,  -561,   308,  -561,  -561,  2640,    65,   316,
      21,    34,  2640,    24,   333,  -561,  5187,  -561,  -561,  -561,
    -561,   298,  4934,  -561,  -561,  -561,  -561,  -561,  -561,  -561,
    -561,  -561,  -561,  -561,  -561,    37,    27,   345,   170,  5341,
      98,  -561,  2718,  -561,  -561,  4196,  -561,  -561,  1414,  -561,
    -561,  1292,  5433,    94,    94,    94,   344,   344,  -561,   827,
     827,   827,  5254,  5369,   827,  2771,   679,   679,   679,   344,
     344,   183,   183,    94,  -561,  -561,  -561,  1778,   233,  1778,
     353,  -561,    28,  -561,  -561,  -561,   346,  -561,  -561,  -561,
    -561,  -561,   297,   307,   260,   395,    41,   113,   403,    76,
    1778,   431,   175,    91,   320,    20,    16,    83,  -561,   300,
    -561,  -561,  -561,  -561,   304,   330,   -20,    16,    37,   308,
    2056,   336,  1778,   436,   341,   349,   355,  2640,   381,   387,
    2640,   489,  -561,  1778,  1778,   388,   502,  1778,    30,  2121,
    -561,  -561,  -561,  -561,   -18,   391,   394,  1778,   393,  -561,
      90,   392,   399,    34,   161,  -561,    34,   225,    34,   397,
    -561,   190,  -561,   517,   398,   211,  3064,   406,   407,   521,
    -561,  -561,  -561,  -561,  -561,  -561,  -561,  -561,  5025,  -561,
    -561,  -561,  -561,   410,   308,   103,   522,   221,    44,  -561,
    -561,  1778,  1778,  -561,  -561,  1778,  1778,  1778,  -561,  -561,
    -561,  1778,  5341,  1778,  5220,   411,  -561,  -561,  -561,  -561,
     222,  -561,   -34,   524,   892,  -561,   413,   527,  -561,  -561,
    -561,   950,   223,    -3,  -561,   119,  -561,  -561,  -561,  1778,
    -561,  -561,  -561,  -561,  -561,  -561,  -561,  -561,   415,    16,
     412,   421,  -561,    16,  1778,   308,  -561,  1482,  -561,   422,
     430,   308,   434,  -561,   536,  -561,  2182,  1778,  3097,   435,
    1778,  1778,  1778,  -561,    16,  1778,  2247,   437,  2948,  3136,
    1778,   438,  1881,  -561,  -561,  -561,  1112,  -561,  -561,  1532,
    1532,  -561,  1600,   232,  -561,   316,  1778,  1778,   245,   537,
    -561,   537,   250,   537,  -561,   283,   537,   307,  1995,   236,
     546,   307,  1995,   551,  5079,  1778,    16,   439,  -561,  -561,
    -561,   -58,   440,   311,   441,  -561,  1778,   198,   442,   558,
    5341,  4229,  2805,  2833,  2920,  5341,  5341,  1778,  -561,  -561,
    -561,  -561,  -561,  -561,  -561,  -561,  -561,  -561,   222,  -561,
    -561,   444,     8,   238,  -561,   242,  1600,   445,  -561,   561,
     258,  -561,   259,   447,   111,   450,  -561,  -561,   276,   320,
     448,  1778,  1778,  -561,  5341,  -561,   449,   277,  1778,  -561,
     452,  -561,  2640,  -561,  -561,  4321,  -561,  -561,  4354,  4446,
    4479,   342,  4571,  -561,  -561,  1778,  -561,  4604,  -561,  -561,
    -561,  1778,  1778,   108,  -561,  5341,  1778,  3229,  1778,  3257,
     280,   288,   454,  -561,  5341,  5341,  -561,   367,  -561,  -561,
     370,  -561,   372,   292,    29,   566,    37,   308,   308,   308,
    1995,  -561,  2306,   307,  1995,   459,   293,  1995,   523,  5187,
    -561,  4696,   376,  -561,  -561,   460,  -561,  1778,  -561,  3350,
    1778,   461,  -561,   380,   464,  -561,  -561,  -561,  -561,  5341,
    -561,  -561,   468,  -561,   469,   465,   471,   299,   309,  -561,
     474,  -561,   470,  -561,  -561,   475,   321,   465,  -561,   478,
    1778,  3378,  3471,  -561,   479,  3499,  -561,  2371,  2640,  1650,
    1778,  1778,  1778,  2640,  3592,  2640,  5341,  5341,  -561,  -561,
    -561,  1112,  3620,  -561,  3713,  -561,   480,   481,  -561,  -561,
    -561,  -561,   482,   308,    -4,   398,   398,   486,    46,   100,
     490,   491,  -561,  2430,  -561,   327,  1995,   541,   228,   492,
     535,  -561,  5133,  5187,  1778,  -561,  3741,  -561,  3834,  -561,
    1778,  -561,  1728,  -561,  -561,  -561,   493,   494,  1778,  -561,
    -561,   495,   328,  -561,  3862,  -561,  -561,  -561,  -561,  -561,
     570,   518,   419,  -561,   565,   -42,  1229,  1364,  3955,  -561,
    -561,  -561,  -561,  -561,  -561,  -561,  -561,  1995,   498,  -561,
     499,   308,   398,   409,   103,   500,   616,   417,   503,  -561,
    -561,  -561,   504,   568,  -561,    37,   308,  1995,  1995,  -561,
    -561,   583,  3983,  -561,  -561,  4076,  -561,  4729,  -561,  -561,
    4821,  -561,   508,  -561,  2640,  2489,  -561,  -561,   578,  -561,
    2579,  -561,   579,  -561,   581,    16,  1995,   580,  -561,  -561,
     515,   633,   519,   420,   525,  -561,  1995,  -561,   531,    46,
     134,   585,  1995,   584,  5187,    16,  -561,  -561,  -561,  -561,
    -561,  -561,  -561,  -561,  -561,  -561,  -561,  -561,   359,   587,
    -561,  -561,   532,  -561,  -561,  1995,   590,  -561,   533,  -561,
    -561,   595,  -561,  -561,   362,  2640,  -561,  -561,   598,  -561,
    -561,  -561,  5187,  -561,  -561,  -561
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -561,  -561,  -561,   653,  -561,  -561,  -561,  -397,   455,   528,
    -561,   -14,    -1,     9,    13,  -561,   192,  -561,  -561,  -561,
    -406,  -507,    31,    32,    52,   264,  -561,   -66,   263,  -561,
     476,    54,  -372,   105,  -191,  -561,    97,   529,    56,  -561,
    -267,  -284,  -561,   557,  -561,  -561,    62,    39,  -561,  -561,
    -561,  -373,   329,   -87,  -560,  -489,   -25,  -221,   -89,  -143,
     -11,   -10,   -38,  -561,    53,  -561,   534,   -48,   235,   801
};

/* YYTABLE[YYPACT[STATE-NUM]].  What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule which
   number is the opposite.  If zero, do what YYDEFACT says.
   If YYTABLE_NINF, syntax error.  */
#define YYTABLE_NINF -201
static const yytype_int16 yytable[] =
{
     151,   491,   293,   297,   419,   105,   537,    50,    51,   414,
     523,   212,   204,   562,   536,    93,   389,     8,   219,   376,
     510,   212,   148,   622,   349,   212,   262,    14,   205,   271,
     622,   133,   295,    93,   224,   383,    12,   263,   188,   262,
     153,   154,   224,   542,   134,   272,   322,    16,     1,   427,
     613,   684,     9,    10,   135,   267,   720,    94,   136,   221,
      98,    42,   544,    99,   100,   101,   158,   189,   207,   255,
     256,   261,    46,   159,   255,    94,   139,   140,    52,   301,
     328,   329,    47,   190,   567,   360,   362,    48,   448,    49,
     208,   189,   576,    11,   206,   336,   337,   141,   357,   142,
     358,   143,   717,    48,   390,    49,   717,   717,   147,   266,
     268,     2,   274,   384,   157,   464,   679,   160,   133,   622,
     563,   189,   189,   213,   214,   150,   350,   351,   626,    95,
     419,   134,   189,    36,   294,   298,   625,   213,   359,   303,
     304,   135,   385,    36,   209,   136,   189,    36,   386,   189,
     598,   421,   189,   424,   189,   428,   250,   330,   189,   189,
     220,   270,   189,   139,   140,   105,   189,   221,   221,   189,
     220,   189,   338,   718,   102,   220,    74,   722,   724,   221,
     209,   210,   255,   257,   141,   332,   142,   532,   143,   255,
     622,    43,   255,    44,   331,   323,   326,   398,   506,   508,
     402,   255,   405,   352,   353,   652,    90,    91,    92,   339,
     394,   395,   475,    69,    70,    71,   302,   361,   480,   622,
     687,    48,   697,    49,   355,   189,   438,   599,   189,   600,
     575,   324,   393,   325,   452,   622,   524,   525,   189,   695,
     439,   440,   441,   191,    49,   192,   442,   443,   444,   696,
     528,   529,   399,    36,   769,   403,   200,   406,   622,   189,
     470,   587,   187,   410,   219,    74,   201,   445,   220,   220,
     222,   726,   632,   196,   197,   198,   373,   202,   199,   203,
     220,   400,   401,   220,   422,   219,   554,   429,   388,   300,
     220,   301,   742,   220,    89,    90,    91,    92,    48,   455,
      49,   221,   220,   446,   291,   221,   462,   223,   407,   623,
     408,   449,    98,   224,   468,    99,   100,   101,   255,   355,
     550,   258,   465,   189,   466,   467,   221,   219,   255,   411,
     765,   412,   477,   517,   255,   193,   194,   520,   275,   195,
     522,   425,   463,   426,   301,   404,   401,   261,   419,   701,
     299,   512,   758,   301,   533,   313,   534,   564,   315,   565,
     255,   566,   317,   301,   255,   516,   401,   511,   221,   105,
     519,   401,   774,   105,    69,    70,    71,   571,   573,   572,
     301,   614,   320,   617,   619,   620,   621,   340,   341,   342,
     343,   344,   345,   346,   347,   578,   584,   301,   301,   606,
     321,   565,   220,   521,   401,   484,   220,   607,   327,   301,
     545,   612,   629,   203,   203,   484,   551,   318,   646,   220,
     565,   500,   354,    17,    18,   355,    74,   220,   647,   220,
     301,   568,   355,   547,   255,   220,   333,    19,    20,    21,
     651,   369,   565,    22,    23,    24,   692,   712,   203,   565,
     356,   538,    87,    88,   367,    89,    90,    91,    92,   370,
     773,   220,   592,   353,    25,   220,  -199,   371,  -199,   220,
     678,   716,   661,   372,  -198,   685,  -198,  -200,   775,  -200,
     353,   782,   255,   353,   255,    26,   255,   609,   401,   255,
     610,   401,   611,   401,   377,   105,   634,   353,   785,   374,
      27,   355,   640,   666,   667,   375,   380,   381,    28,    29,
      30,   391,   392,   615,   396,   618,    48,   387,    31,    32,
      33,   397,   409,   189,   415,   416,   417,   423,    34,   450,
     420,   456,   457,   437,   471,   220,   469,    35,   730,   255,
     255,   482,   262,   472,   478,   255,    36,   255,    37,    38,
     479,   535,   738,   740,   481,   487,   539,   494,   498,   543,
     546,   548,   552,   553,   561,   569,   570,   574,   577,   583,
     580,   484,   586,   627,   608,   255,   630,   616,   255,   628,
     635,   639,   631,   220,   641,   220,   642,   220,   452,   643,
     220,   645,   648,   459,   699,   650,   768,   653,   694,   657,
     675,   676,   677,   680,   681,   682,   683,   686,   688,   714,
     689,   690,   698,   708,   709,   711,   715,   719,   728,   729,
     733,   734,   744,   735,   736,   737,   484,   660,   749,   255,
     753,   756,   669,   757,   671,   761,   219,   760,   762,   763,
     220,   220,   770,   772,   776,   764,   220,   779,   220,   255,
     255,   767,   777,   780,   781,   784,   219,    13,   319,   513,
     292,   579,   484,   672,   518,   693,   255,   255,   316,   649,
     644,   731,   255,   732,   249,   296,   220,   221,   255,   220,
       0,     0,   473,   560,   739,     0,     0,     0,   255,     0,
       0,     0,   310,     0,   255,     0,     0,   221,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    69,
      70,    71,    72,    73,     0,     0,   727,   255,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   255,   686,   688,
     220,     0,     0,     0,     0,     0,   741,   743,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     220,   220,     0,   750,   752,     0,     0,     0,     0,   755,
       0,    74,     0,     0,     0,   759,     0,   220,   220,     0,
       0,     0,     0,   220,     0,   766,     0,     0,   220,   220,
       0,   771,     0,     0,     0,    85,    86,    87,    88,   220,
      89,    90,    91,    92,     0,   220,     0,     0,   220,     0,
       0,     0,     0,     0,   778,     0,     0,     0,     0,     0,
       0,    41,     0,     0,   783,     0,     0,     0,   220,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   220,    53,
      54,    55,    56,    57,    58,    59,    60,    64,    65,    66,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     152,     0,     0,   155,     0,    67,     0,    69,    70,    71,
      72,    73,     0,     0,     0,     0,     0,     0,   161,   162,
     163,   164,   165,   166,   167,   168,   169,   170,   171,   172,
     173,   174,   175,   176,   177,   178,   179,   180,   181,   182,
     183,   184,   185,   186,     0,     0,    17,    18,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    74,
      19,    20,    21,     0,     0,     0,    22,    23,    24,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    81,    82,
       0,    83,    84,    85,    86,    87,    88,    25,    89,    90,
      91,    92,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    17,    18,     0,     0,    26,    64,
       0,     0,     0,     0,     0,     0,     0,     0,    19,    20,
      21,     0,     0,    27,    22,    23,    24,     0,     0,     0,
       0,    28,    29,    30,     0,     0,     0,     0,   312,     0,
     314,    31,    32,    33,     0,    25,     0,     0,     0,     0,
       0,    34,     0,     0,     0,     0,     0,     0,     0,     0,
      35,   451,     0,     0,     0,   452,    26,     0,     0,    36,
       0,    37,    38,     0,     0,     0,     0,     0,     0,     0,
       0,    27,     0,   368,     0,     0,     0,     0,     0,    28,
      29,    30,     0,     0,   378,   379,     0,     0,   382,    31,
      32,    33,     0,     0,     0,     0,     0,     0,     0,    34,
       0,     0,     0,     0,     0,     0,     0,     0,    35,   458,
       0,     0,     0,   459,     0,     0,     0,    36,     0,    37,
      38,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   430,   431,     0,     0,   432,   433,   434,     0,
       0,     0,   435,     0,   436,     0,    17,    18,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      19,    20,    21,     0,     0,     0,    22,    23,    24,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   501,   502,     0,   474,     0,    25,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   485,     0,
       0,   488,   489,   490,     0,     0,   492,     0,    26,     0,
       0,   497,     0,     0,     0,     0,     0,   505,     0,     0,
     507,   509,     0,    27,     0,     0,     0,   514,   515,     0,
       0,    28,    29,    30,     0,     0,     0,     0,     0,     0,
       0,    31,    32,    33,     0,     0,   541,     0,     0,     0,
       0,    34,     0,     0,     0,     0,     0,   549,     0,     0,
      35,     0,     0,    17,    18,     0,     0,     0,   559,    36,
       0,    37,    38,     0,     0,     0,     0,    19,    20,    21,
       0,     0,     0,    22,    23,    24,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   581,   582,    25,     0,     0,     0,     0,   585,
       0,   721,   661,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    26,   594,     0,     0,     0,
       0,     0,   596,   597,     0,     0,     0,   602,     0,   604,
      27,     0,     0,     0,     0,     0,     0,     0,    28,    29,
      30,     0,    69,    70,    71,    72,    73,     0,    31,    32,
      33,     0,     0,     0,     0,     0,     0,     0,    34,     0,
       0,     0,     0,     0,     0,     0,     0,    35,   636,     0,
       0,   638,     0,     0,     0,     0,    36,     0,    37,    38,
       0,     0,     0,     0,     0,     0,     0,     0,    17,    18,
       0,     0,     0,     0,    74,     0,     0,     0,     0,     0,
       0,   654,    19,    20,    21,     0,     0,     0,    22,    23,
      24,     0,     0,   668,    82,     0,    83,    84,    85,    86,
      87,    88,   505,    89,    90,    91,    92,     0,     0,    25,
       0,     0,     0,     0,     0,     0,   723,   661,    17,    18,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      26,     0,    19,    20,    21,   702,     0,     0,    22,    23,
      24,   705,     0,   707,     0,    27,     0,     0,     0,   710,
       0,     0,     0,    28,    29,    30,     0,     0,     0,    25,
       0,     0,     0,    31,    32,    33,     0,     0,     0,     0,
       0,     0,     0,    34,     0,     0,     0,     0,     0,     0,
      26,     0,    35,     0,     0,     0,    17,    18,     0,     0,
       0,    36,     0,    37,    38,    27,     0,     0,     0,     0,
      19,    20,    21,    28,    29,    30,    22,    23,    24,     0,
       0,     0,     0,    31,    32,    33,     0,     0,     0,    61,
       0,     0,     0,    34,     0,     0,     0,    25,     0,     0,
       0,     0,    35,     0,     0,     0,    17,    18,     0,     0,
       0,    36,     0,    37,    38,     0,     0,     0,    26,     0,
      19,    20,    21,     0,     0,     0,    22,    23,    24,     0,
       0,     0,     0,    27,     0,     0,     0,     0,     0,     0,
       0,    28,    29,    30,     0,     0,     0,    25,     0,     0,
       0,    31,    32,    33,     0,     0,     0,     0,     0,     0,
       0,    34,     0,     0,     0,     0,     0,     0,    26,     0,
      35,   476,     0,     0,    17,    18,     0,     0,     0,    36,
       0,    37,    38,    27,     0,     0,     0,     0,    19,    20,
      21,    28,    29,    30,    22,    23,    24,     0,     0,     0,
       0,    31,    32,    33,     0,     0,     0,     0,     0,     0,
       0,    34,     0,     0,     0,    25,     0,     0,     0,   213,
      35,     0,     0,     0,    17,    18,     0,     0,     0,    36,
       0,    37,    38,     0,     0,     0,    26,     0,    19,    20,
      21,     0,     0,     0,    22,    23,    24,     0,     0,     0,
       0,    27,     0,     0,     0,     0,     0,     0,     0,    28,
      29,    30,     0,     0,     0,    25,     0,     0,     0,    31,
      32,    33,     0,   661,     0,     0,     0,     0,     0,    34,
       0,     0,     0,     0,     0,     0,    26,     0,    35,     0,
       0,     0,     0,   452,     0,     0,     0,    36,     0,    37,
      38,    27,    17,    18,     0,     0,     0,     0,     0,    28,
      29,    30,     0,     0,     0,     0,    19,    20,    21,    31,
      32,    33,    22,    23,    24,     0,     0,     0,     0,    34,
       0,     0,     0,     0,     0,     0,     0,     0,    35,     0,
       0,     0,     0,    25,     0,     0,     0,    36,     0,    37,
      38,     0,    17,    18,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    26,     0,    19,    20,    21,     0,
       0,     0,    22,    23,    24,     0,     0,     0,     0,    27,
       0,     0,     0,     0,     0,     0,     0,    28,    29,    30,
       0,     0,     0,    25,     0,     0,     0,    31,    32,    33,
       0,     0,     0,     0,     0,     0,     0,    34,     0,     0,
       0,     0,     0,     0,    26,     0,    35,   706,     0,     0,
       0,     0,     0,     0,     0,    36,     0,    37,    38,    27,
       0,     0,     0,     0,     0,     0,     0,    28,    29,    30,
       0,     0,     0,     0,     0,     0,     0,    31,    32,    33,
       0,     0,     0,     0,     0,     0,   226,    34,   227,     0,
       0,     0,   228,     0,     0,     0,    35,     0,     0,     0,
       0,     0,   229,     0,     0,    36,     0,    37,    38,    67,
      68,    69,    70,    71,    72,    73,     0,   230,     0,   231,
       0,     0,     0,     0,   232,   233,     0,     0,     0,     0,
     234,   235,   236,     0,     0,     0,   237,     0,     0,     0,
       0,   238,   239,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   240,     0,   241,   242,
       0,     0,     0,    74,     0,     0,     0,     0,   243,   244,
      75,    76,    77,   245,     0,     0,     0,   246,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,     0,     0,   247,     0,
     226,   499,   227,   524,   525,   248,   526,     0,    36,     0,
       0,     0,     0,     0,     0,     0,   527,   528,   529,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   230,     0,   231,     0,     0,     0,     0,   232,   233,
       0,     0,     0,     0,   234,   235,   236,     0,     0,     0,
     237,     0,     0,     0,     0,   238,   239,     0,     0,     0,
       0,   226,     0,   227,     0,     0,     0,   228,     0,     0,
     240,     0,   241,   242,     0,     0,     0,   229,     0,     0,
       0,     0,   243,   244,     0,     0,     0,   245,     0,     0,
       0,   246,   230,   363,   231,     0,     0,     0,     0,   232,
     233,     0,     0,     0,     0,   234,   235,   236,     0,     0,
       0,   237,   247,     0,     0,     0,   238,   239,     0,   248,
       0,     0,    36,     0,     0,     0,   226,     0,   227,     0,
       0,   240,   228,   241,   242,     0,     0,     0,     0,     0,
       0,     0,   229,   243,   244,     0,     0,     0,   245,     0,
       0,     0,   246,     0,   364,     0,     0,   230,     0,   231,
       0,     0,     0,     0,   232,   233,     0,     0,     0,     0,
     234,   235,   236,   247,     0,     0,   237,     0,     0,     0,
     248,   238,   239,    36,     0,     0,     0,   226,     0,   227,
       0,     0,     0,   228,     0,     0,   240,     0,   241,   242,
       0,     0,     0,   229,     0,     0,     0,     0,   243,   244,
       0,     0,     0,   245,     0,     0,     0,   246,   230,   483,
     231,     0,     0,     0,     0,   232,   233,     0,     0,     0,
       0,   234,   235,   236,     0,     0,     0,   237,   247,     0,
       0,   387,   238,   239,     0,   248,     0,     0,    36,     0,
       0,     0,   226,     0,   227,     0,     0,   240,   228,   241,
     242,     0,     0,     0,     0,     0,     0,     0,   229,   243,
     244,     0,     0,     0,   245,     0,     0,     0,   246,     0,
       0,     0,     0,   230,     0,   231,     0,     0,     0,     0,
     232,   233,     0,     0,     0,     0,   234,   235,   236,   247,
       0,     0,   237,     0,     0,     0,   248,   238,   239,    36,
       0,   226,     0,   227,     0,     0,     0,   228,     0,     0,
       0,     0,   240,   493,   241,   242,     0,   229,     0,     0,
       0,     0,     0,     0,   243,   244,     0,     0,     0,   245,
       0,     0,   230,   246,   231,     0,     0,     0,     0,   232,
     233,     0,     0,     0,     0,   234,   235,   236,     0,     0,
       0,   237,     0,   624,   247,     0,   238,   239,     0,     0,
       0,   248,     0,     0,    36,     0,   226,     0,   227,     0,
       0,   240,   228,   241,   242,     0,     0,     0,     0,     0,
       0,     0,   229,   243,   244,     0,     0,     0,   245,     0,
       0,     0,   246,     0,     0,     0,     0,   230,   659,   231,
       0,     0,     0,     0,   232,   233,     0,     0,     0,     0,
     234,   235,   236,   247,     0,     0,   237,     0,     0,     0,
     248,   238,   239,    36,     0,   226,     0,   227,     0,     0,
       0,   228,     0,     0,     0,     0,   240,     0,   241,   242,
       0,   229,     0,     0,     0,     0,     0,     0,   243,   244,
       0,     0,     0,   245,     0,     0,   230,   246,   231,     0,
       0,     0,     0,   232,   233,     0,     0,     0,     0,   234,
     235,   236,     0,     0,     0,   237,     0,   691,   247,     0,
     238,   239,     0,     0,   226,   248,   227,     0,    36,     0,
     228,     0,     0,     0,     0,   240,     0,   241,   242,     0,
     229,     0,     0,     0,     0,     0,     0,   243,   244,     0,
       0,     0,   245,     0,     0,   230,   246,   231,     0,     0,
       0,     0,   232,   233,     0,     0,     0,     0,   234,   235,
     236,     0,     0,     0,   237,     0,     0,   247,     0,   238,
     239,     0,     0,     0,   248,     0,     0,    36,     0,     0,
       0,     0,     0,     0,   240,     0,   241,   242,     0,     0,
       0,     0,     0,     0,     0,     0,   243,   244,     0,     0,
       0,   245,     0,     0,   226,   246,   227,     0,     0,     0,
     228,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     229,     0,     0,     0,     0,     0,   247,     0,     0,   751,
       0,     0,     0,   248,     0,   230,    36,   231,     0,     0,
       0,     0,   232,   233,     0,     0,     0,     0,   234,   235,
     236,     0,     0,     0,   237,     0,     0,     0,     0,   238,
     239,     0,     0,     0,     0,   226,     0,   227,     0,     0,
       0,   228,     0,     0,   240,     0,   241,   242,     0,     0,
       0,   229,     0,     0,     0,     0,   243,   244,     0,     0,
       0,   245,     0,     0,     0,   246,   230,     0,   231,     0,
       0,     0,     0,   232,   233,     0,     0,     0,     0,   234,
     235,   236,     0,     0,     0,   237,   247,     0,     0,   754,
     238,   239,     0,   248,     0,     0,    36,    67,    68,    69,
      70,    71,    72,    73,     0,   240,     0,   241,   242,     0,
       0,     0,     0,     0,     0,     0,     0,   243,   244,     0,
       0,     0,   245,     0,     0,     0,   246,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,   247,     0,     0,
       0,    74,     0,     0,   248,     0,     0,    36,    75,    76,
      77,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,   305,   306,    67,
      74,    69,    70,    71,    72,    73,    36,    75,    76,    77,
       0,     0,     0,     0,     0,    78,   307,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,    67,    68,    69,    70,    71,    72,    73,
       0,     0,     0,     0,   308,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
       0,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,     0,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,     0,    74,     0,     0,
       0,     0,     0,     0,    75,    76,    77,     0,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,    74,    89,    90,    91,    92,
       0,     0,    75,    76,    77,     0,     0,     0,     0,     0,
      78,   556,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,   557,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    74,     0,     0,     0,     0,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
      74,    89,    90,    91,    92,     0,     0,    75,    76,    77,
       0,     0,     0,     0,     0,    78,   558,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,     0,     0,     0,     0,     0,     0,   106,
     495,   107,    99,   100,   101,   108,   109,   110,   111,   112,
     113,   114,     0,     0,     0,   115,   116,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   117,
     276,     0,   277,     0,     0,     0,   118,     0,     0,     0,
     119,   120,   121,     0,     0,     0,     0,     0,   122,     0,
       0,     0,     0,     0,   278,    67,    68,    69,    70,    71,
      72,    73,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     279,     0,     0,     0,     0,     0,     0,   128,   129,     0,
       0,     0,   413,     0,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,    74,
       0,     0,     0,     0,     0,     0,    75,    76,    77,     0,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,     0,     0,     0,     0,     0,   486,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,     0,     0,     0,     0,     0,   496,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    67,    68,    69,    70,    71,
      72,    73,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    74,     0,     0,     0,     0,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,    74,
      89,    90,    91,    92,     0,     0,    75,    76,    77,   603,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,     0,     0,     0,     0,     0,   605,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    74,     0,     0,     0,     0,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
      74,    89,    90,    91,    92,     0,     0,    75,    76,    77,
     637,     0,     0,     0,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,     0,     0,     0,     0,     0,   655,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,    74,    89,    90,    91,    92,     0,     0,    75,    76,
      77,   656,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,     0,   658,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    74,     0,     0,     0,     0,     0,
       0,    75,    76,    77,     0,     0,     0,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,    74,    89,    90,    91,    92,     0,     0,    75,
      76,    77,   670,     0,     0,     0,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,     0,     0,     0,     0,     0,
     673,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    74,     0,     0,     0,     0,
       0,     0,    75,    76,    77,     0,     0,     0,     0,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,    74,    89,    90,    91,    92,     0,     0,
      75,    76,    77,   674,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,     0,     0,     0,     0,
       0,   703,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    74,     0,     0,     0,
       0,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,    74,    89,    90,    91,    92,     0,
       0,    75,    76,    77,   704,     0,     0,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,     0,
       0,     0,   713,    67,    68,    69,    70,    71,    72,    73,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    74,     0,     0,
       0,     0,     0,     0,    75,    76,    77,     0,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,    74,    89,    90,    91,    92,
       0,     0,    75,    76,    77,   725,     0,     0,     0,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,     0,     0,
       0,     0,     0,   745,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,    74,    89,    90,    91,
      92,     0,     0,    75,    76,    77,   746,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,   156,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,    74,     0,     0,     0,   309,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,   555,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,    74,     0,     0,     0,
     588,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,   589,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,    74,     0,     0,     0,   590,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,   591,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,    74,     0,     0,     0,
     593,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,   595,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,    74,     0,     0,     0,   633,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,   747,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,     0,     0,     0,   106,
     748,   107,    99,   100,   101,   108,   109,   110,   111,   112,
     113,   114,     0,     0,     0,   115,   116,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   117,
       0,     0,     0,     0,     0,     0,   118,     0,     0,     0,
     119,   120,   121,     0,     0,     0,     0,     0,   122,     0,
     123,     0,   124,     0,     0,     0,     0,     0,     0,     0,
       2,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   125,     0,     0,     0,     0,     0,   126,     0,
     127,     0,     0,     0,     0,     0,     0,   128,   129,   130,
     106,     0,   107,    99,   100,   101,   108,   109,   110,   111,
     112,   113,   114,     0,     0,     0,   115,   116,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     117,   276,     0,   277,     0,     0,     0,   118,     0,     0,
       0,   119,   120,   121,     0,     0,     0,     0,     0,   122,
       0,     0,     0,     0,   106,   278,   107,    99,   100,   101,
     108,   109,   110,   111,   112,   113,   114,     0,     0,     0,
     115,   116,     0,     0,     0,     0,     0,     0,     0,     0,
     418,   279,     0,     0,   117,   276,   540,   277,   128,   129,
       0,   118,     0,     0,     0,   119,   120,   121,     0,     0,
       0,     0,     0,   122,     0,     0,     0,     0,   106,   278,
     107,    99,   100,   101,   108,   109,   110,   111,   112,   113,
     114,     0,     0,     0,   115,   116,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   279,     0,     0,   117,   276,
     700,   277,   128,   129,     0,   118,     0,     0,     0,   119,
     120,   121,     0,     0,     0,     0,     0,   122,     0,     0,
       0,     0,   106,   278,   107,    99,   100,   101,   108,   109,
     110,   111,   112,   113,   114,     0,     0,     0,   115,   116,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   279,
       0,     0,   117,   276,     0,   277,   128,   129,     0,   118,
       0,     0,     0,   119,   120,   121,     0,     0,     0,     0,
       0,   122,     0,     0,     0,     0,     0,   278,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   279,     0,     0,     0,     0,     0,     0,
     128,   129,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   305,
     306,     0,    74,     0,     0,     0,     0,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,    78,   307,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,     0,    74,     0,     0,     0,
       0,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,    78,   311,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,    74,    89,    90,    91,    92,     0,     0,    75,    76,
      77,    67,     0,    69,    70,    71,    72,    73,     0,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    74,     0,     0,     0,     0,
       0,     0,    75,    76,    77,     0,     0,     0,     0,     0,
       0,     0,     0,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92
};

static const yytype_int16 yycheck[] =
{
      48,   374,   145,   146,   288,    43,   412,    18,    18,   276,
     407,     5,     5,     5,   411,     5,    34,     5,   107,   240,
     392,     5,    47,   530,   215,     5,     5,   117,    21,     5,
     537,    45,     5,     5,     5,     5,     0,    16,     5,     5,
      51,    51,     5,   416,    45,    21,     5,     5,     3,     5,
      21,     5,     4,     5,    45,   121,    98,    47,    45,   107,
       5,   118,   120,     8,     9,    10,   121,   125,     5,   117,
       5,   119,   113,   128,   122,    47,    45,    45,   118,   121,
       4,     5,   118,    94,   456,   228,   229,   123,   122,   125,
      27,   125,   464,    45,   105,     4,     5,    45,   118,    45,
     120,    45,   662,   123,   122,   125,   666,   667,     4,   120,
     121,    66,   123,    83,    61,   118,   120,    64,   132,   626,
     112,   125,   125,   117,   118,     5,   215,   216,   534,   119,
     414,   132,   125,   127,   145,   146,   533,   117,   227,   150,
     150,   132,   112,   127,   117,   132,   125,   127,   118,   125,
      42,   294,   125,   296,   125,   298,   117,    81,   125,   125,
     107,   122,   125,   132,   132,   203,   125,   215,   216,   125,
     117,   125,    81,   662,   119,   122,    82,   666,   667,   227,
     117,   118,   230,   118,   132,   210,   132,   408,   132,   237,
     697,   118,   240,   120,   118,   206,   207,   263,   389,   390,
     266,   249,   268,   120,   121,   577,   112,   113,   114,   118,
     120,   121,   355,    30,    31,    32,   118,   228,   361,   726,
     120,   123,   628,   125,   121,   125,     4,   119,   125,   121,
     119,   118,   257,   120,   123,   742,     8,     9,   125,    11,
      18,    19,    20,   119,   125,   121,    24,    25,    26,    21,
      22,    23,   263,   127,   120,   266,    12,   268,   765,   125,
     349,   482,   122,   274,   353,    82,   120,    45,   215,   216,
      16,   677,   539,    11,    12,    13,   237,   119,    16,   121,
     227,   120,   121,   230,   295,   374,   429,   298,   249,   119,
     237,   121,   698,   240,   111,   112,   113,   114,   123,   324,
     125,   349,   249,    81,     6,   353,   331,    16,   118,   530,
     120,   322,     5,     5,   339,     8,     9,    10,   366,   121,
     122,     5,   333,   125,   335,   335,   374,   416,   376,   118,
     736,   120,   357,   399,   382,    12,    13,   403,     5,    16,
     406,   120,   119,   122,   121,   120,   121,   395,   632,   633,
       5,   119,   725,   121,   118,   122,   120,   119,     5,   121,
     408,   119,    16,   121,   412,   120,   121,   392,   416,   407,
     120,   121,   745,   411,    30,    31,    32,   119,   119,   121,
     121,   524,   122,   526,   527,   528,   529,    67,    68,    69,
      70,    71,    72,    73,    74,   119,   119,   121,   121,   119,
       5,   121,   349,   120,   121,   366,   353,   119,     5,   121,
     421,   119,   119,   121,   121,   376,   427,   120,   119,   366,
     121,   382,   122,     4,     5,   121,    82,   374,   119,   376,
     121,   456,   121,   122,   482,   382,     5,    18,    19,    20,
     119,     5,   121,    24,    25,    26,   119,   119,   121,   121,
     120,   412,   108,   109,   118,   111,   112,   113,   114,   118,
     744,   408,   120,   121,    45,   412,    57,   118,    59,   416,
     613,    52,    53,   118,    57,   618,    59,    57,   119,    59,
     121,   119,   530,   121,   532,    66,   534,   120,   121,   537,
     120,   121,   120,   121,     5,   533,   120,   121,   782,   118,
      81,   121,   122,   590,   591,   118,   118,     5,    89,    90,
      91,   120,   118,   524,   122,   526,   123,   120,    99,   100,
     101,   122,     5,   125,   118,   118,     5,     5,   109,     5,
     120,   118,     5,   122,   122,   482,   121,   118,   681,   587,
     588,     5,     5,   122,   122,   593,   127,   595,   129,   130,
     120,     5,   695,   696,   120,   120,     5,   120,   120,   120,
     120,   120,   120,     5,   120,   120,     5,   120,   118,   120,
     122,   532,   120,   534,   120,   623,   537,    11,   626,   120,
     120,   120,    59,   530,   120,   532,   118,   534,   123,   120,
     537,   120,   118,   123,    59,   120,   739,   119,    57,   120,
     120,   120,   120,   614,   615,   616,   120,   618,   619,    39,
     120,   120,   120,   120,   120,   120,    98,    52,   120,   120,
     120,     5,    39,   120,   120,    57,   587,   588,   120,   677,
      52,    52,   593,    52,   595,   120,   725,    57,     5,   120,
     587,   588,    57,    59,    57,   120,   593,    57,   595,   697,
     698,   120,   120,   120,    59,    57,   745,     4,   203,   395,
     132,   469,   623,   601,   401,   626,   714,   715,   192,   572,
     565,   682,   720,   684,   117,   146,   623,   725,   726,   626,
      -1,    -1,   353,   448,   695,    -1,    -1,    -1,   736,    -1,
      -1,    -1,   158,    -1,   742,    -1,    -1,   745,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    30,
      31,    32,    33,    34,    -1,    -1,   677,   765,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   775,   739,   740,
     677,    -1,    -1,    -1,    -1,    -1,   697,   698,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     697,   698,    -1,   714,   715,    -1,    -1,    -1,    -1,   720,
      -1,    82,    -1,    -1,    -1,   726,    -1,   714,   715,    -1,
      -1,    -1,    -1,   720,    -1,   736,    -1,    -1,   725,   726,
      -1,   742,    -1,    -1,    -1,   106,   107,   108,   109,   736,
     111,   112,   113,   114,    -1,   742,    -1,    -1,   745,    -1,
      -1,    -1,    -1,    -1,   765,    -1,    -1,    -1,    -1,    -1,
      -1,    10,    -1,    -1,   775,    -1,    -1,    -1,   765,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   775,    28,
      29,    30,    31,    32,    33,    34,    35,    36,    37,    38,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      49,    -1,    -1,    52,    -1,    28,    -1,    30,    31,    32,
      33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    67,    68,
      69,    70,    71,    72,    73,    74,    75,    76,    77,    78,
      79,    80,    81,    82,    83,    84,    85,    86,    87,    88,
      89,    90,    91,    92,    -1,    -1,     4,     5,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    82,
      18,    19,    20,    -1,    -1,    -1,    24,    25,    26,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   101,   102,
      -1,   104,   105,   106,   107,   108,   109,    45,   111,   112,
     113,   114,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,     4,     5,    -1,    -1,    66,   158,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    18,    19,
      20,    -1,    -1,    81,    24,    25,    26,    -1,    -1,    -1,
      -1,    89,    90,    91,    -1,    -1,    -1,    -1,   187,    -1,
     189,    99,   100,   101,    -1,    45,    -1,    -1,    -1,    -1,
      -1,   109,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     118,   119,    -1,    -1,    -1,   123,    66,    -1,    -1,   127,
      -1,   129,   130,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    81,    -1,   232,    -1,    -1,    -1,    -1,    -1,    89,
      90,    91,    -1,    -1,   243,   244,    -1,    -1,   247,    99,
     100,   101,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   109,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   118,   119,
      -1,    -1,    -1,   123,    -1,    -1,    -1,   127,    -1,   129,
     130,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   301,   302,    -1,    -1,   305,   306,   307,    -1,
      -1,    -1,   311,    -1,   313,    -1,     4,     5,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      18,    19,    20,    -1,    -1,    -1,    24,    25,    26,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    40,    41,    -1,   354,    -1,    45,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   367,    -1,
      -1,   370,   371,   372,    -1,    -1,   375,    -1,    66,    -1,
      -1,   380,    -1,    -1,    -1,    -1,    -1,   386,    -1,    -1,
     389,   390,    -1,    81,    -1,    -1,    -1,   396,   397,    -1,
      -1,    89,    90,    91,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    99,   100,   101,    -1,    -1,   415,    -1,    -1,    -1,
      -1,   109,    -1,    -1,    -1,    -1,    -1,   426,    -1,    -1,
     118,    -1,    -1,     4,     5,    -1,    -1,    -1,   437,   127,
      -1,   129,   130,    -1,    -1,    -1,    -1,    18,    19,    20,
      -1,    -1,    -1,    24,    25,    26,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   471,   472,    45,    -1,    -1,    -1,    -1,   478,
      -1,    52,    53,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    66,   495,    -1,    -1,    -1,
      -1,    -1,   501,   502,    -1,    -1,    -1,   506,    -1,   508,
      81,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    89,    90,
      91,    -1,    30,    31,    32,    33,    34,    -1,    99,   100,
     101,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   109,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   118,   547,    -1,
      -1,   550,    -1,    -1,    -1,    -1,   127,    -1,   129,   130,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     4,     5,
      -1,    -1,    -1,    -1,    82,    -1,    -1,    -1,    -1,    -1,
      -1,   580,    18,    19,    20,    -1,    -1,    -1,    24,    25,
      26,    -1,    -1,   592,   102,    -1,   104,   105,   106,   107,
     108,   109,   601,   111,   112,   113,   114,    -1,    -1,    45,
      -1,    -1,    -1,    -1,    -1,    -1,    52,    53,     4,     5,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      66,    -1,    18,    19,    20,   634,    -1,    -1,    24,    25,
      26,   640,    -1,   642,    -1,    81,    -1,    -1,    -1,   648,
      -1,    -1,    -1,    89,    90,    91,    -1,    -1,    -1,    45,
      -1,    -1,    -1,    99,   100,   101,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   109,    -1,    -1,    -1,    -1,    -1,    -1,
      66,    -1,   118,    -1,    -1,    -1,     4,     5,    -1,    -1,
      -1,   127,    -1,   129,   130,    81,    -1,    -1,    -1,    -1,
      18,    19,    20,    89,    90,    91,    24,    25,    26,    -1,
      -1,    -1,    -1,    99,   100,   101,    -1,    -1,    -1,   105,
      -1,    -1,    -1,   109,    -1,    -1,    -1,    45,    -1,    -1,
      -1,    -1,   118,    -1,    -1,    -1,     4,     5,    -1,    -1,
      -1,   127,    -1,   129,   130,    -1,    -1,    -1,    66,    -1,
      18,    19,    20,    -1,    -1,    -1,    24,    25,    26,    -1,
      -1,    -1,    -1,    81,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    89,    90,    91,    -1,    -1,    -1,    45,    -1,    -1,
      -1,    99,   100,   101,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   109,    -1,    -1,    -1,    -1,    -1,    -1,    66,    -1,
     118,   119,    -1,    -1,     4,     5,    -1,    -1,    -1,   127,
      -1,   129,   130,    81,    -1,    -1,    -1,    -1,    18,    19,
      20,    89,    90,    91,    24,    25,    26,    -1,    -1,    -1,
      -1,    99,   100,   101,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   109,    -1,    -1,    -1,    45,    -1,    -1,    -1,   117,
     118,    -1,    -1,    -1,     4,     5,    -1,    -1,    -1,   127,
      -1,   129,   130,    -1,    -1,    -1,    66,    -1,    18,    19,
      20,    -1,    -1,    -1,    24,    25,    26,    -1,    -1,    -1,
      -1,    81,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    89,
      90,    91,    -1,    -1,    -1,    45,    -1,    -1,    -1,    99,
     100,   101,    -1,    53,    -1,    -1,    -1,    -1,    -1,   109,
      -1,    -1,    -1,    -1,    -1,    -1,    66,    -1,   118,    -1,
      -1,    -1,    -1,   123,    -1,    -1,    -1,   127,    -1,   129,
     130,    81,     4,     5,    -1,    -1,    -1,    -1,    -1,    89,
      90,    91,    -1,    -1,    -1,    -1,    18,    19,    20,    99,
     100,   101,    24,    25,    26,    -1,    -1,    -1,    -1,   109,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   118,    -1,
      -1,    -1,    -1,    45,    -1,    -1,    -1,   127,    -1,   129,
     130,    -1,     4,     5,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    66,    -1,    18,    19,    20,    -1,
      -1,    -1,    24,    25,    26,    -1,    -1,    -1,    -1,    81,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    89,    90,    91,
      -1,    -1,    -1,    45,    -1,    -1,    -1,    99,   100,   101,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   109,    -1,    -1,
      -1,    -1,    -1,    -1,    66,    -1,   118,   119,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   127,    -1,   129,   130,    81,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    89,    90,    91,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    99,   100,   101,
      -1,    -1,    -1,    -1,    -1,    -1,     5,   109,     7,    -1,
      -1,    -1,    11,    -1,    -1,    -1,   118,    -1,    -1,    -1,
      -1,    -1,    21,    -1,    -1,   127,    -1,   129,   130,    28,
      29,    30,    31,    32,    33,    34,    -1,    36,    -1,    38,
      -1,    -1,    -1,    -1,    43,    44,    -1,    -1,    -1,    -1,
      49,    50,    51,    -1,    -1,    -1,    55,    -1,    -1,    -1,
      -1,    60,    61,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    75,    -1,    77,    78,
      -1,    -1,    -1,    82,    -1,    -1,    -1,    -1,    87,    88,
      89,    90,    91,    92,    -1,    -1,    -1,    96,    97,    -1,
      99,   100,   101,   102,    -1,   104,   105,   106,   107,   108,
     109,    -1,   111,   112,   113,   114,    -1,    -1,   117,    -1,
       5,   120,     7,     8,     9,   124,    11,    -1,   127,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    21,    22,    23,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    36,    -1,    38,    -1,    -1,    -1,    -1,    43,    44,
      -1,    -1,    -1,    -1,    49,    50,    51,    -1,    -1,    -1,
      55,    -1,    -1,    -1,    -1,    60,    61,    -1,    -1,    -1,
      -1,     5,    -1,     7,    -1,    -1,    -1,    11,    -1,    -1,
      75,    -1,    77,    78,    -1,    -1,    -1,    21,    -1,    -1,
      -1,    -1,    87,    88,    -1,    -1,    -1,    92,    -1,    -1,
      -1,    96,    36,    37,    38,    -1,    -1,    -1,    -1,    43,
      44,    -1,    -1,    -1,    -1,    49,    50,    51,    -1,    -1,
      -1,    55,   117,    -1,    -1,    -1,    60,    61,    -1,   124,
      -1,    -1,   127,    -1,    -1,    -1,     5,    -1,     7,    -1,
      -1,    75,    11,    77,    78,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    21,    87,    88,    -1,    -1,    -1,    92,    -1,
      -1,    -1,    96,    -1,    98,    -1,    -1,    36,    -1,    38,
      -1,    -1,    -1,    -1,    43,    44,    -1,    -1,    -1,    -1,
      49,    50,    51,   117,    -1,    -1,    55,    -1,    -1,    -1,
     124,    60,    61,   127,    -1,    -1,    -1,     5,    -1,     7,
      -1,    -1,    -1,    11,    -1,    -1,    75,    -1,    77,    78,
      -1,    -1,    -1,    21,    -1,    -1,    -1,    -1,    87,    88,
      -1,    -1,    -1,    92,    -1,    -1,    -1,    96,    36,    37,
      38,    -1,    -1,    -1,    -1,    43,    44,    -1,    -1,    -1,
      -1,    49,    50,    51,    -1,    -1,    -1,    55,   117,    -1,
      -1,   120,    60,    61,    -1,   124,    -1,    -1,   127,    -1,
      -1,    -1,     5,    -1,     7,    -1,    -1,    75,    11,    77,
      78,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    21,    87,
      88,    -1,    -1,    -1,    92,    -1,    -1,    -1,    96,    -1,
      -1,    -1,    -1,    36,    -1,    38,    -1,    -1,    -1,    -1,
      43,    44,    -1,    -1,    -1,    -1,    49,    50,    51,   117,
      -1,    -1,    55,    -1,    -1,    -1,   124,    60,    61,   127,
      -1,     5,    -1,     7,    -1,    -1,    -1,    11,    -1,    -1,
      -1,    -1,    75,    76,    77,    78,    -1,    21,    -1,    -1,
      -1,    -1,    -1,    -1,    87,    88,    -1,    -1,    -1,    92,
      -1,    -1,    36,    96,    38,    -1,    -1,    -1,    -1,    43,
      44,    -1,    -1,    -1,    -1,    49,    50,    51,    -1,    -1,
      -1,    55,    -1,    57,   117,    -1,    60,    61,    -1,    -1,
      -1,   124,    -1,    -1,   127,    -1,     5,    -1,     7,    -1,
      -1,    75,    11,    77,    78,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    21,    87,    88,    -1,    -1,    -1,    92,    -1,
      -1,    -1,    96,    -1,    -1,    -1,    -1,    36,    37,    38,
      -1,    -1,    -1,    -1,    43,    44,    -1,    -1,    -1,    -1,
      49,    50,    51,   117,    -1,    -1,    55,    -1,    -1,    -1,
     124,    60,    61,   127,    -1,     5,    -1,     7,    -1,    -1,
      -1,    11,    -1,    -1,    -1,    -1,    75,    -1,    77,    78,
      -1,    21,    -1,    -1,    -1,    -1,    -1,    -1,    87,    88,
      -1,    -1,    -1,    92,    -1,    -1,    36,    96,    38,    -1,
      -1,    -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,
      50,    51,    -1,    -1,    -1,    55,    -1,    57,   117,    -1,
      60,    61,    -1,    -1,     5,   124,     7,    -1,   127,    -1,
      11,    -1,    -1,    -1,    -1,    75,    -1,    77,    78,    -1,
      21,    -1,    -1,    -1,    -1,    -1,    -1,    87,    88,    -1,
      -1,    -1,    92,    -1,    -1,    36,    96,    38,    -1,    -1,
      -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,    50,
      51,    -1,    -1,    -1,    55,    -1,    -1,   117,    -1,    60,
      61,    -1,    -1,    -1,   124,    -1,    -1,   127,    -1,    -1,
      -1,    -1,    -1,    -1,    75,    -1,    77,    78,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    87,    88,    -1,    -1,
      -1,    92,    -1,    -1,     5,    96,     7,    -1,    -1,    -1,
      11,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      21,    -1,    -1,    -1,    -1,    -1,   117,    -1,    -1,   120,
      -1,    -1,    -1,   124,    -1,    36,   127,    38,    -1,    -1,
      -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,    50,
      51,    -1,    -1,    -1,    55,    -1,    -1,    -1,    -1,    60,
      61,    -1,    -1,    -1,    -1,     5,    -1,     7,    -1,    -1,
      -1,    11,    -1,    -1,    75,    -1,    77,    78,    -1,    -1,
      -1,    21,    -1,    -1,    -1,    -1,    87,    88,    -1,    -1,
      -1,    92,    -1,    -1,    -1,    96,    36,    -1,    38,    -1,
      -1,    -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,
      50,    51,    -1,    -1,    -1,    55,   117,    -1,    -1,   120,
      60,    61,    -1,   124,    -1,    -1,   127,    28,    29,    30,
      31,    32,    33,    34,    -1,    75,    -1,    77,    78,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    87,    88,    -1,
      -1,    -1,    92,    -1,    -1,    -1,    96,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    28,    29,    30,    31,
      32,    33,    34,    -1,    -1,    -1,    -1,   117,    -1,    -1,
      -1,    82,    -1,    -1,   124,    -1,    -1,   127,    89,    90,
      91,    -1,    -1,    -1,    -1,    -1,    97,    -1,    99,   100,
     101,   102,    -1,   104,   105,   106,   107,   108,   109,    -1,
     111,   112,   113,   114,    -1,    -1,    -1,    79,    80,    28,
      82,    30,    31,    32,    33,    34,   127,    89,    90,    91,
      -1,    -1,    -1,    -1,    -1,    97,    98,    99,   100,   101,
     102,    -1,   104,   105,   106,   107,   108,   109,    -1,   111,
     112,   113,   114,    28,    29,    30,    31,    32,    33,    34,
      -1,    -1,    -1,    -1,   126,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    82,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    28,    29,    30,    31,    32,    33,    34,    -1,    -1,
      -1,    -1,    -1,   102,    -1,   104,   105,   106,   107,   108,
     109,    -1,   111,   112,   113,   114,    -1,    82,    -1,    -1,
      -1,    -1,    -1,    -1,    89,    90,    91,    -1,    -1,    -1,
      -1,    -1,    97,    -1,    99,   100,   101,   102,    -1,   104,
     105,   106,   107,   108,   109,    82,   111,   112,   113,   114,
      -1,    -1,    89,    90,    91,    -1,    -1,    -1,    -1,    -1,
      97,   126,    99,   100,   101,   102,    -1,   104,   105,   106,
     107,   108,   109,    -1,   111,   112,   113,   114,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,   126,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    28,    29,    30,    31,
      32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    82,    -1,    -1,    -1,    -1,    -1,    -1,    89,
      90,    91,    -1,    -1,    -1,    -1,    -1,    97,    -1,    99,
     100,   101,   102,    -1,   104,   105,   106,   107,   108,   109,
      82,   111,   112,   113,   114,    -1,    -1,    89,    90,    91,
      -1,    -1,    -1,    -1,    -1,    97,   126,    99,   100,   101,
     102,    -1,   104,   105,   106,   107,   108,   109,    -1,   111,
     112,   113,   114,    -1,    -1,    -1,    -1,    -1,    -1,     5,
     122,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      16,    17,    -1,    -1,    -1,    21,    22,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    35,
      36,    -1,    38,    -1,    -1,    -1,    42,    -1,    -1,    -1,
      46,    47,    48,    -1,    -1,    -1,    -1,    -1,    54,    -1,
      -1,    -1,    -1,    -1,    60,    28,    29,    30,    31,    32,
      33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      86,    -1,    -1,    -1,    -1,    -1,    -1,    93,    94,    -1,
      -1,    -1,    98,    -1,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    82,
      -1,    -1,    -1,    -1,    -1,    -1,    89,    90,    91,    -1,
      -1,    -1,    -1,    -1,    97,    -1,    99,   100,   101,   102,
      -1,   104,   105,   106,   107,   108,   109,    -1,   111,   112,
     113,   114,    -1,    -1,    -1,    -1,    -1,   120,    82,    -1,
      -1,    -1,    -1,    -1,    -1,    89,    90,    91,    -1,    -1,
      -1,    -1,    -1,    97,    -1,    99,   100,   101,   102,    -1,
     104,   105,   106,   107,   108,   109,    -1,   111,   112,   113,
     114,    -1,    -1,    -1,    -1,    -1,   120,    28,    29,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    28,    29,    30,    31,    32,
      33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    82,    -1,    -1,    -1,    -1,    -1,    -1,    89,    90,
      91,    -1,    -1,    -1,    -1,    -1,    97,    -1,    99,   100,
     101,   102,    -1,   104,   105,   106,   107,   108,   109,    82,
     111,   112,   113,   114,    -1,    -1,    89,    90,    91,   120,
      -1,    -1,    -1,    -1,    97,    -1,    99,   100,   101,   102,
      -1,   104,   105,   106,   107,   108,   109,    -1,   111,   112,
     113,   114,    -1,    -1,    -1,    -1,    -1,   120,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    28,    29,    30,    31,
      32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    82,    -1,    -1,    -1,    -1,    -1,    -1,    89,
      90,    91,    -1,    -1,    -1,    -1,    -1,    97,    -1,    99,
     100,   101,   102,    -1,   104,   105,   106,   107,   108,   109,
      82,   111,   112,   113,   114,    -1,    -1,    89,    90,    91,
     120,    -1,    -1,    -1,    -1,    97,    -1,    99,   100,   101,
     102,    -1,   104,   105,   106,   107,   108,   109,    -1,   111,
     112,   113,   114,    -1,    -1,    -1,    -1,    -1,   120,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,    29,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    82,    -1,    -1,    -1,    -1,    -1,    -1,
      89,    90,    91,    -1,    -1,    -1,    -1,    -1,    97,    -1,
      99,   100,   101,   102,    -1,   104,   105,   106,   107,   108,
     109,    82,   111,   112,   113,   114,    -1,    -1,    89,    90,
      91,   120,    -1,    -1,    -1,    -1,    97,    -1,    99,   100,
     101,   102,    -1,   104,   105,   106,   107,   108,   109,    -1,
     111,   112,   113,   114,    -1,    -1,    -1,    -1,    -1,   120,
      28,    29,    30,    31,    32,    33,    34,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    82,    -1,    -1,    -1,    -1,    -1,
      -1,    89,    90,    91,    -1,    -1,    -1,    -1,    -1,    97,
      -1,    99,   100,   101,   102,    -1,   104,   105,   106,   107,
     108,   109,    82,   111,   112,   113,   114,    -1,    -1,    89,
      90,    91,   120,    -1,    -1,    -1,    -1,    97,    -1,    99,
     100,   101,   102,    -1,   104,   105,   106,   107,   108,   109,
      -1,   111,   112,   113,   114,    -1,    -1,    -1,    -1,    -1,
     120,    28,    29,    30,    31,    32,    33,    34,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    82,    -1,    -1,    -1,    -1,
      -1,    -1,    89,    90,    91,    -1,    -1,    -1,    -1,    -1,
      97,    -1,    99,   100,   101,   102,    -1,   104,   105,   106,
     107,   108,   109,    82,   111,   112,   113,   114,    -1,    -1,
      89,    90,    91,   120,    -1,    -1,    -1,    -1,    97,    -1,
      99,   100,   101,   102,    -1,   104,   105,   106,   107,   108,
     109,    -1,   111,   112,   113,   114,    -1,    -1,    -1,    -1,
      -1,   120,    28,    29,    30,    31,    32,    33,    34,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      28,    29,    30,    31,    32,    33,    34,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    82,    -1,    -1,    -1,
      -1,    -1,    -1,    89,    90,    91,    -1,    -1,    -1,    -1,
      -1,    97,    -1,    99,   100,   101,   102,    -1,   104,   105,
     106,   107,   108,   109,    82,   111,   112,   113,   114,    -1,
      -1,    89,    90,    91,   120,    -1,    -1,    -1,    -1,    97,
      -1,    99,   100,   101,   102,    -1,   104,   105,   106,   107,
     108,   109,    -1,   111,   112,   113,   114,    -1,    -1,    -1,
      -1,    -1,   120,    28,    29,    30,    31,    32,    33,    34,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    28,    29,    30,    31,    32,    33,    34,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    82,    -1,    -1,
      -1,    -1,    -1,    -1,    89,    90,    91,    -1,    -1,    -1,
      -1,    -1,    97,    -1,    99,   100,   101,   102,    -1,   104,
     105,   106,   107,   108,   109,    82,   111,   112,   113,   114,
      -1,    -1,    89,    90,    91,   120,    -1,    -1,    -1,    -1,
      97,    -1,    99,   100,   101,   102,    -1,   104,   105,   106,
     107,   108,   109,    -1,   111,   112,   113,   114,    -1,    -1,
      -1,    -1,    -1,   120,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    28,    29,    30,    31,    32,    33,    34,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    82,    -1,
      -1,    -1,    -1,    -1,    -1,    89,    90,    91,    -1,    -1,
      -1,    -1,    -1,    97,    -1,    99,   100,   101,   102,    -1,
     104,   105,   106,   107,   108,   109,    82,   111,   112,   113,
     114,    -1,    -1,    89,    90,    91,   120,    -1,    -1,    -1,
      -1,    97,    -1,    99,   100,   101,   102,    -1,   104,   105,
     106,   107,   108,   109,    -1,   111,   112,   113,   114,    -1,
      -1,    -1,    -1,   119,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,    29,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    82,    -1,
      -1,    -1,    -1,    -1,    -1,    89,    90,    91,    -1,    -1,
      -1,    -1,    -1,    97,    -1,    99,   100,   101,   102,    -1,
     104,   105,   106,   107,   108,   109,    -1,   111,   112,   113,
     114,    82,    -1,    -1,    -1,   119,    -1,    -1,    89,    90,
      91,    -1,    -1,    -1,    -1,    -1,    97,    -1,    99,   100,
     101,   102,    -1,   104,   105,   106,   107,   108,   109,    -1,
     111,   112,   113,   114,    -1,    -1,    -1,    -1,   119,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    28,    29,    30,    31,    32,    33,    34,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    82,    -1,    -1,    -1,    -1,    -1,    -1,
      89,    90,    91,    -1,    -1,    -1,    -1,    -1,    97,    -1,
      99,   100,   101,   102,    -1,   104,   105,   106,   107,   108,
     109,    -1,   111,   112,   113,   114,    82,    -1,    -1,    -1,
     119,    -1,    -1,    89,    90,    91,    -1,    -1,    -1,    -1,
      -1,    97,    -1,    99,   100,   101,   102,    -1,   104,   105,
     106,   107,   108,   109,    -1,   111,   112,   113,   114,    -1,
      -1,    -1,    -1,   119,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,    29,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    82,    -1,
      -1,    -1,    -1,    -1,    -1,    89,    90,    91,    -1,    -1,
      -1,    -1,    -1,    97,    -1,    99,   100,   101,   102,    -1,
     104,   105,   106,   107,   108,   109,    -1,   111,   112,   113,
     114,    82,    -1,    -1,    -1,   119,    -1,    -1,    89,    90,
      91,    -1,    -1,    -1,    -1,    -1,    97,    -1,    99,   100,
     101,   102,    -1,   104,   105,   106,   107,   108,   109,    -1,
     111,   112,   113,   114,    -1,    -1,    -1,    -1,   119,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    28,    29,    30,    31,    32,    33,    34,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    82,    -1,    -1,    -1,    -1,    -1,    -1,
      89,    90,    91,    -1,    -1,    -1,    -1,    -1,    97,    -1,
      99,   100,   101,   102,    -1,   104,   105,   106,   107,   108,
     109,    -1,   111,   112,   113,   114,    82,    -1,    -1,    -1,
     119,    -1,    -1,    89,    90,    91,    -1,    -1,    -1,    -1,
      -1,    97,    -1,    99,   100,   101,   102,    -1,   104,   105,
     106,   107,   108,   109,    -1,   111,   112,   113,   114,    -1,
      -1,    -1,    -1,   119,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,    29,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    82,    -1,
      -1,    -1,    -1,    -1,    -1,    89,    90,    91,    -1,    -1,
      -1,    -1,    -1,    97,    -1,    99,   100,   101,   102,    -1,
     104,   105,   106,   107,   108,   109,    -1,   111,   112,   113,
     114,    82,    -1,    -1,    -1,   119,    -1,    -1,    89,    90,
      91,    -1,    -1,    -1,    -1,    -1,    97,    -1,    99,   100,
     101,   102,    -1,   104,   105,   106,   107,   108,   109,    -1,
     111,   112,   113,   114,    -1,    -1,    -1,    -1,   119,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    82,    -1,    -1,    -1,    -1,    -1,    -1,
      89,    90,    91,    -1,    -1,    -1,    -1,    -1,    97,    -1,
      99,   100,   101,   102,    -1,   104,   105,   106,   107,   108,
     109,    -1,   111,   112,   113,   114,    -1,    -1,    -1,     5,
     119,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      16,    17,    -1,    -1,    -1,    21,    22,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    35,
      -1,    -1,    -1,    -1,    -1,    -1,    42,    -1,    -1,    -1,
      46,    47,    48,    -1,    -1,    -1,    -1,    -1,    54,    -1,
      56,    -1,    58,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      66,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    78,    -1,    -1,    -1,    -1,    -1,    84,    -1,
      86,    -1,    -1,    -1,    -1,    -1,    -1,    93,    94,    95,
       5,    -1,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    -1,    -1,    -1,    21,    22,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      35,    36,    -1,    38,    -1,    -1,    -1,    42,    -1,    -1,
      -1,    46,    47,    48,    -1,    -1,    -1,    -1,    -1,    54,
      -1,    -1,    -1,    -1,     5,    60,     7,     8,     9,    10,
      11,    12,    13,    14,    15,    16,    17,    -1,    -1,    -1,
      21,    22,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      85,    86,    -1,    -1,    35,    36,    37,    38,    93,    94,
      -1,    42,    -1,    -1,    -1,    46,    47,    48,    -1,    -1,
      -1,    -1,    -1,    54,    -1,    -1,    -1,    -1,     5,    60,
       7,     8,     9,    10,    11,    12,    13,    14,    15,    16,
      17,    -1,    -1,    -1,    21,    22,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    86,    -1,    -1,    35,    36,
      37,    38,    93,    94,    -1,    42,    -1,    -1,    -1,    46,
      47,    48,    -1,    -1,    -1,    -1,    -1,    54,    -1,    -1,
      -1,    -1,     5,    60,     7,     8,     9,    10,    11,    12,
      13,    14,    15,    16,    17,    -1,    -1,    -1,    21,    22,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    86,
      -1,    -1,    35,    36,    -1,    38,    93,    94,    -1,    42,
      -1,    -1,    -1,    46,    47,    48,    -1,    -1,    -1,    -1,
      -1,    54,    -1,    -1,    -1,    -1,    -1,    60,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    86,    -1,    -1,    -1,    -1,    -1,    -1,
      93,    94,    28,    29,    30,    31,    32,    33,    34,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    79,
      80,    -1,    82,    -1,    -1,    -1,    -1,    -1,    -1,    89,
      90,    91,    -1,    -1,    -1,    -1,    -1,    97,    98,    99,
     100,   101,   102,    -1,   104,   105,   106,   107,   108,   109,
      -1,   111,   112,   113,   114,    -1,    82,    -1,    -1,    -1,
      -1,    -1,    -1,    89,    90,    91,    -1,    -1,    -1,    -1,
      -1,    97,    98,    99,   100,   101,   102,    -1,   104,   105,
     106,   107,   108,   109,    -1,   111,   112,   113,   114,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,    29,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    82,    -1,    -1,    -1,    -1,    -1,    -1,
      89,    90,    91,    -1,    -1,    -1,    -1,    -1,    97,    -1,
      99,   100,   101,   102,    -1,   104,   105,   106,   107,   108,
     109,    82,   111,   112,   113,   114,    -1,    -1,    89,    90,
      91,    28,    -1,    30,    31,    32,    33,    34,    -1,   100,
     101,   102,    -1,   104,   105,   106,   107,   108,   109,    -1,
     111,   112,   113,   114,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    82,    -1,    -1,    -1,    -1,
      -1,    -1,    89,    90,    91,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   100,   101,   102,    -1,   104,   105,   106,
     107,   108,   109,    -1,   111,   112,   113,   114
};

/* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
   symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,     3,    66,   132,   133,   134,   135,   142,     5,     4,
       5,    45,     0,   134,   117,   136,     5,     4,     5,    18,
      19,    20,    24,    25,    26,    45,    66,    81,    89,    90,
      91,    99,   100,   101,   109,   118,   127,   129,   130,   195,
     198,   200,   118,   118,   120,   137,   113,   118,   123,   125,
     191,   192,   118,   200,   200,   200,   200,   200,   200,   200,
     200,   105,   196,   197,   200,   200,   200,    28,    29,    30,
      31,    32,    33,    34,    82,    89,    90,    91,    97,    99,
     100,   101,   102,   104,   105,   106,   107,   108,   109,   111,
     112,   113,   114,     5,    47,   119,   160,   161,     5,     8,
       9,    10,   119,   138,   139,   193,     5,     7,    11,    12,
      13,    14,    15,    16,    17,    21,    22,    35,    42,    46,
      47,    48,    54,    56,    58,    78,    84,    86,    93,    94,
      95,   140,   141,   142,   143,   144,   145,   149,   150,   153,
     154,   155,   162,   169,   170,   193,   194,     4,   187,   200,
       5,   198,   200,   191,   192,   200,   119,   195,   121,   128,
     195,   200,   200,   200,   200,   200,   200,   200,   200,   200,
     200,   200,   200,   200,   200,   200,   200,   200,   200,   200,
     200,   200,   200,   200,   200,   200,   200,   122,     5,   125,
     191,   119,   121,    12,    13,    16,    11,    12,    13,    16,
      12,   120,   119,   121,     5,    21,   191,     5,    27,   117,
     118,   168,     5,   117,   118,   146,   165,   182,   183,   189,
     195,   198,    16,    16,     5,   190,     5,     7,    11,    21,
      36,    38,    43,    44,    49,    50,    51,    55,    60,    61,
      75,    77,    78,    87,    88,    92,    96,   117,   124,   174,
     178,   179,   180,   181,   189,   198,     5,   118,     5,   156,
     157,   198,     5,    16,   158,   159,   191,   158,   191,   174,
     178,     5,    21,   148,   191,     5,    36,    38,    60,    86,
     143,   144,   145,   153,   154,   155,   162,   169,   171,   172,
     173,     6,   140,   190,   191,     5,   168,   190,   191,     5,
     119,   121,   118,   191,   192,    79,    80,    98,   126,   119,
     197,    98,   200,   122,   200,     5,   161,    16,   120,   139,
     122,     5,     5,   191,   118,   120,   191,     5,     4,     5,
      81,   118,   187,     5,   191,   192,     4,     5,    81,   118,
      67,    68,    69,    70,    71,    72,    73,    74,   147,   165,
     189,   189,   120,   121,   122,   121,   120,   118,   120,   189,
     190,   191,   190,    37,    98,   178,   188,   118,   200,     5,
     118,   118,   118,   178,   118,   118,   188,     5,   200,   200,
     118,     5,   200,     5,    83,   112,   118,   120,   178,    34,
     122,   120,   118,   187,   120,   121,   122,   122,   158,   191,
     120,   121,   158,   191,   120,   158,   191,   118,   120,     5,
     191,   118,   120,    98,   171,   118,   118,     5,    85,   172,
     120,   190,   191,     5,   190,   120,   122,     5,   190,   191,
     200,   200,   200,   200,   200,   200,   200,   122,     4,    18,
      19,    20,    24,    25,    26,    45,    81,   199,   122,   191,
       5,   119,   123,   163,   164,   187,   118,     5,   119,   123,
     166,   167,   187,   119,   118,   191,   191,   192,   187,   121,
     189,   122,   122,   183,   200,   190,   119,   187,   122,   120,
     190,   120,     5,    37,   178,   200,   120,   120,   200,   200,
     200,   182,   200,    76,   120,   122,   120,   200,   120,   120,
     178,    40,    41,   176,   177,   200,   165,   200,   165,   200,
     163,   187,   119,   156,   200,   200,   120,   158,   159,   120,
     158,   120,   158,   138,     8,     9,    11,    21,    22,    23,
     151,   152,   188,   118,   120,     5,   138,   151,   178,     5,
      37,   200,   182,   120,   120,   191,   120,   122,   120,   200,
     122,   191,   120,     5,   190,   119,   126,   126,   126,   200,
     199,   120,     5,   112,   119,   121,   119,   163,   187,   120,
       5,   119,   121,   119,   120,   119,   163,   118,   119,   147,
     122,   200,   200,   120,   119,   200,   120,   188,   119,   119,
     119,   119,   120,   119,   200,   119,   200,   200,    42,   119,
     121,   175,   200,   120,   200,   120,   119,   119,   120,   120,
     120,   120,   119,    21,   190,   191,    11,   190,   191,   190,
     190,   190,   152,   188,    57,   138,   151,   178,   120,   119,
     178,    59,   171,   119,   120,   120,   200,   120,   200,   120,
     122,   120,   118,   120,   164,   120,   119,   119,   118,   167,
     120,   119,   163,   119,   200,   120,   120,   120,   120,    37,
     178,    53,   184,   185,   186,   187,   184,   184,   200,   178,
     120,   178,   177,   120,   120,   120,   120,   120,   190,   120,
     191,   191,   191,   120,     5,   190,   191,   120,   191,   120,
     120,    57,   119,   178,    57,    11,    21,   151,   120,    59,
      37,   172,   200,   120,   120,   200,   119,   200,   120,   120,
     200,   120,   119,   120,    39,    98,    52,   185,   186,    52,
      98,    52,   186,    52,   186,   120,   151,   178,   120,   120,
     190,   191,   191,   120,     5,   120,   120,    57,   190,   191,
     190,   178,   151,   178,    39,   120,   120,   119,   119,   120,
     178,   120,   178,    52,   120,   178,    52,    52,   182,   178,
      57,   120,     5,   120,   120,   151,   178,   120,   190,   120,
      57,   178,    59,   172,   182,   119,    57,   120,   178,    57,
     120,    59,   119,   178,    57,   172
};

#define yyerrok		(yyerrstatus = 0)
#define yyclearin	(yychar = YYEMPTY)
#define YYEMPTY		(-2)
#define YYEOF		0

#define YYACCEPT	goto yyacceptlab
#define YYABORT		goto yyabortlab
#define YYERROR		goto yyerrorlab


/* Like YYERROR except do call yyerror.  This remains here temporarily
   to ease the transition to the new meaning of YYERROR, for GCC.
   Once GCC version 2 has supplanted version 1, this can go.  */

#define YYFAIL		goto yyerrlab

#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)					\
do								\
  if (yychar == YYEMPTY && yylen == 1)				\
    {								\
      yychar = (Token);						\
      yylval = (Value);						\
      yytoken = YYTRANSLATE (yychar);				\
      YYPOPSTACK (1);						\
      goto yybackup;						\
    }								\
  else								\
    {								\
      yyerror (YY_("syntax error: cannot back up")); \
      YYERROR;							\
    }								\
while (YYID (0))


#define YYTERROR	1
#define YYERRCODE	256


/* YYLLOC_DEFAULT -- Set CURRENT to span from RHS[1] to RHS[N].
   If N is 0, then set CURRENT to the empty location which ends
   the previous symbol: RHS[0] (always defined).  */

#define YYRHSLOC(Rhs, K) ((Rhs)[K])
#ifndef YYLLOC_DEFAULT
# define YYLLOC_DEFAULT(Current, Rhs, N)				\
    do									\
      if (YYID (N))                                                    \
	{								\
	  (Current).first_line   = YYRHSLOC (Rhs, 1).first_line;	\
	  (Current).first_column = YYRHSLOC (Rhs, 1).first_column;	\
	  (Current).last_line    = YYRHSLOC (Rhs, N).last_line;		\
	  (Current).last_column  = YYRHSLOC (Rhs, N).last_column;	\
	}								\
      else								\
	{								\
	  (Current).first_line   = (Current).last_line   =		\
	    YYRHSLOC (Rhs, 0).last_line;				\
	  (Current).first_column = (Current).last_column =		\
	    YYRHSLOC (Rhs, 0).last_column;				\
	}								\
    while (YYID (0))
#endif


/* YY_LOCATION_PRINT -- Print the location on the stream.
   This macro was not mandated originally: define only if we know
   we won't break user code: when these are the locations we know.  */

#ifndef YY_LOCATION_PRINT
# if defined YYLTYPE_IS_TRIVIAL && YYLTYPE_IS_TRIVIAL
#  define YY_LOCATION_PRINT(File, Loc)			\
     fprintf (File, "%d.%d-%d.%d",			\
	      (Loc).first_line, (Loc).first_column,	\
	      (Loc).last_line,  (Loc).last_column)
# else
#  define YY_LOCATION_PRINT(File, Loc) ((void) 0)
# endif
#endif


/* YYLEX -- calling `yylex' with the right arguments.  */

#ifdef YYLEX_PARAM
# define YYLEX yylex (YYLEX_PARAM)
#else
# define YYLEX yylex ()
#endif

/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)			\
do {						\
  if (yydebug)					\
    YYFPRINTF Args;				\
} while (YYID (0))

# define YY_SYMBOL_PRINT(Title, Type, Value, Location)			  \
do {									  \
  if (yydebug)								  \
    {									  \
      YYFPRINTF (stderr, "%s ", Title);					  \
      yy_symbol_print (stderr,						  \
		  Type, Value); \
      YYFPRINTF (stderr, "\n");						  \
    }									  \
} while (YYID (0))


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

/*ARGSUSED*/
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_symbol_value_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
#else
static void
yy_symbol_value_print (yyoutput, yytype, yyvaluep)
    FILE *yyoutput;
    int yytype;
    YYSTYPE const * const yyvaluep;
#endif
{
  if (!yyvaluep)
    return;
# ifdef YYPRINT
  if (yytype < YYNTOKENS)
    YYPRINT (yyoutput, yytoknum[yytype], *yyvaluep);
# else
  YYUSE (yyoutput);
# endif
  switch (yytype)
    {
      default:
	break;
    }
}


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_symbol_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
#else
static void
yy_symbol_print (yyoutput, yytype, yyvaluep)
    FILE *yyoutput;
    int yytype;
    YYSTYPE const * const yyvaluep;
#endif
{
  if (yytype < YYNTOKENS)
    YYFPRINTF (yyoutput, "token %s (", yytname[yytype]);
  else
    YYFPRINTF (yyoutput, "nterm %s (", yytname[yytype]);

  yy_symbol_value_print (yyoutput, yytype, yyvaluep);
  YYFPRINTF (yyoutput, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_stack_print (yytype_int16 *bottom, yytype_int16 *top)
#else
static void
yy_stack_print (bottom, top)
    yytype_int16 *bottom;
    yytype_int16 *top;
#endif
{
  YYFPRINTF (stderr, "Stack now");
  for (; bottom <= top; ++bottom)
    YYFPRINTF (stderr, " %d", *bottom);
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)				\
do {								\
  if (yydebug)							\
    yy_stack_print ((Bottom), (Top));				\
} while (YYID (0))


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_reduce_print (YYSTYPE *yyvsp, int yyrule)
#else
static void
yy_reduce_print (yyvsp, yyrule)
    YYSTYPE *yyvsp;
    int yyrule;
#endif
{
  int yynrhs = yyr2[yyrule];
  int yyi;
  unsigned long int yylno = yyrline[yyrule];
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %lu):\n",
	     yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      fprintf (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr, yyrhs[yyprhs[yyrule] + yyi],
		       &(yyvsp[(yyi + 1) - (yynrhs)])
		       		       );
      fprintf (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)		\
do {					\
  if (yydebug)				\
    yy_reduce_print (yyvsp, Rule); \
} while (YYID (0))

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef	YYINITDEPTH
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



#if YYERROR_VERBOSE

# ifndef yystrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define yystrlen strlen
#  else
/* Return the length of YYSTR.  */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static YYSIZE_T
yystrlen (const char *yystr)
#else
static YYSIZE_T
yystrlen (yystr)
    const char *yystr;
#endif
{
  YYSIZE_T yylen;
  for (yylen = 0; yystr[yylen]; yylen++)
    continue;
  return yylen;
}
#  endif
# endif

# ifndef yystpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define yystpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static char *
yystpcpy (char *yydest, const char *yysrc)
#else
static char *
yystpcpy (yydest, yysrc)
    char *yydest;
    const char *yysrc;
#endif
{
  char *yyd = yydest;
  const char *yys = yysrc;

  while ((*yyd++ = *yys++) != '\0')
    continue;

  return yyd - 1;
}
#  endif
# endif

# ifndef yytnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yyerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yytname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYSIZE_T
yytnamerr (char *yyres, const char *yystr)
{
  if (*yystr == '"')
    {
      YYSIZE_T yyn = 0;
      char const *yyp = yystr;

      for (;;)
	switch (*++yyp)
	  {
	  case '\'':
	  case ',':
	    goto do_not_strip_quotes;

	  case '\\':
	    if (*++yyp != '\\')
	      goto do_not_strip_quotes;
	    /* Fall through.  */
	  default:
	    if (yyres)
	      yyres[yyn] = *yyp;
	    yyn++;
	    break;

	  case '"':
	    if (yyres)
	      yyres[yyn] = '\0';
	    return yyn;
	  }
    do_not_strip_quotes: ;
    }

  if (! yyres)
    return yystrlen (yystr);

  return yystpcpy (yyres, yystr) - yyres;
}
# endif

/* Copy into YYRESULT an error message about the unexpected token
   YYCHAR while in state YYSTATE.  Return the number of bytes copied,
   including the terminating null byte.  If YYRESULT is null, do not
   copy anything; just return the number of bytes that would be
   copied.  As a special case, return 0 if an ordinary "syntax error"
   message will do.  Return YYSIZE_MAXIMUM if overflow occurs during
   size calculation.  */
static YYSIZE_T
yysyntax_error (char *yyresult, int yystate, int yychar)
{
  int yyn = yypact[yystate];

  if (! (YYPACT_NINF < yyn && yyn <= YYLAST))
    return 0;
  else
    {
      int yytype = YYTRANSLATE (yychar);
      YYSIZE_T yysize0 = yytnamerr (0, yytname[yytype]);
      YYSIZE_T yysize = yysize0;
      YYSIZE_T yysize1;
      int yysize_overflow = 0;
      enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
      char const *yyarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
      int yyx;

# if 0
      /* This is so xgettext sees the translatable formats that are
	 constructed on the fly.  */
      YY_("syntax error, unexpected %s");
      YY_("syntax error, unexpected %s, expecting %s");
      YY_("syntax error, unexpected %s, expecting %s or %s");
      YY_("syntax error, unexpected %s, expecting %s or %s or %s");
      YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s");
# endif
      char *yyfmt;
      char const *yyf;
      static char const yyunexpected[] = "syntax error, unexpected %s";
      static char const yyexpecting[] = ", expecting %s";
      static char const yyor[] = " or %s";
      char yyformat[sizeof yyunexpected
		    + sizeof yyexpecting - 1
		    + ((YYERROR_VERBOSE_ARGS_MAXIMUM - 2)
		       * (sizeof yyor - 1))];
      char const *yyprefix = yyexpecting;

      /* Start YYX at -YYN if negative to avoid negative indexes in
	 YYCHECK.  */
      int yyxbegin = yyn < 0 ? -yyn : 0;

      /* Stay within bounds of both yycheck and yytname.  */
      int yychecklim = YYLAST - yyn + 1;
      int yyxend = yychecklim < YYNTOKENS ? yychecklim : YYNTOKENS;
      int yycount = 1;

      yyarg[0] = yytname[yytype];
      yyfmt = yystpcpy (yyformat, yyunexpected);

      for (yyx = yyxbegin; yyx < yyxend; ++yyx)
	if (yycheck[yyx + yyn] == yyx && yyx != YYTERROR)
	  {
	    if (yycount == YYERROR_VERBOSE_ARGS_MAXIMUM)
	      {
		yycount = 1;
		yysize = yysize0;
		yyformat[sizeof yyunexpected - 1] = '\0';
		break;
	      }
	    yyarg[yycount++] = yytname[yyx];
	    yysize1 = yysize + yytnamerr (0, yytname[yyx]);
	    yysize_overflow |= (yysize1 < yysize);
	    yysize = yysize1;
	    yyfmt = yystpcpy (yyfmt, yyprefix);
	    yyprefix = yyor;
	  }

      yyf = YY_(yyformat);
      yysize1 = yysize + yystrlen (yyf);
      yysize_overflow |= (yysize1 < yysize);
      yysize = yysize1;

      if (yysize_overflow)
	return YYSIZE_MAXIMUM;

      if (yyresult)
	{
	  /* Avoid sprintf, as that infringes on the user's name space.
	     Don't have undefined behavior even if the translation
	     produced a string with the wrong number of "%s"s.  */
	  char *yyp = yyresult;
	  int yyi = 0;
	  while ((*yyp = *yyf) != '\0')
	    {
	      if (*yyp == '%' && yyf[1] == 's' && yyi < yycount)
		{
		  yyp += yytnamerr (yyp, yyarg[yyi++]);
		  yyf += 2;
		}
	      else
		{
		  yyp++;
		  yyf++;
		}
	    }
	}
      return yysize;
    }
}
#endif /* YYERROR_VERBOSE */


/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

/*ARGSUSED*/
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yydestruct (const char *yymsg, int yytype, YYSTYPE *yyvaluep)
#else
static void
yydestruct (yymsg, yytype, yyvaluep)
    const char *yymsg;
    int yytype;
    YYSTYPE *yyvaluep;
#endif
{
  YYUSE (yyvaluep);

  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yytype, yyvaluep, yylocationp);

  switch (yytype)
    {

      default:
	break;
    }
}


/* Prevent warnings from -Wmissing-prototypes.  */

#ifdef YYPARSE_PARAM
#if defined __STDC__ || defined __cplusplus
int yyparse (void *YYPARSE_PARAM);
#else
int yyparse ();
#endif
#else /* ! YYPARSE_PARAM */
#if defined __STDC__ || defined __cplusplus
int yyparse (void);
#else
int yyparse ();
#endif
#endif /* ! YYPARSE_PARAM */



/* The look-ahead symbol.  */
int yychar;

/* The semantic value of the look-ahead symbol.  */
YYSTYPE yylval;

/* Number of syntax errors so far.  */
int yynerrs;



/*----------.
| yyparse.  |
`----------*/

#ifdef YYPARSE_PARAM
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
int
yyparse (void *YYPARSE_PARAM)
#else
int
yyparse (YYPARSE_PARAM)
    void *YYPARSE_PARAM;
#endif
#else /* ! YYPARSE_PARAM */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
int
yyparse (void)
#else
int
yyparse ()

#endif
#endif
{
  
  int yystate;
  int yyn;
  int yyresult;
  /* Number of tokens to shift before error messages enabled.  */
  int yyerrstatus;
  /* Look-ahead token as an internal (translated) token number.  */
  int yytoken = 0;
#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char yymsgbuf[128];
  char *yymsg = yymsgbuf;
  YYSIZE_T yymsg_alloc = sizeof yymsgbuf;
#endif

  /* Three stacks and their tools:
     `yyss': related to states,
     `yyvs': related to semantic values,
     `yyls': related to locations.

     Refer to the stacks thru separate pointers, to allow yyoverflow
     to reallocate them elsewhere.  */

  /* The state stack.  */
  yytype_int16 yyssa[YYINITDEPTH];
  yytype_int16 *yyss = yyssa;
  yytype_int16 *yyssp;

  /* The semantic value stack.  */
  YYSTYPE yyvsa[YYINITDEPTH];
  YYSTYPE *yyvs = yyvsa;
  YYSTYPE *yyvsp;



#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  YYSIZE_T yystacksize = YYINITDEPTH;

  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;


  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yystate = 0;
  yyerrstatus = 0;
  yynerrs = 0;
  yychar = YYEMPTY;		/* Cause a token to be read.  */

  /* Initialize stack pointers.
     Waste one element of value and location stack
     so that they stay on the same level as the state stack.
     The wasted elements are never initialized.  */

  yyssp = yyss;
  yyvsp = yyvs;

  goto yysetstate;

/*------------------------------------------------------------.
| yynewstate -- Push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
 yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;

 yysetstate:
  *yyssp = yystate;

  if (yyss + yystacksize - 1 <= yyssp)
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYSIZE_T yysize = yyssp - yyss + 1;

#ifdef yyoverflow
      {
	/* Give user a chance to reallocate the stack.  Use copies of
	   these so that the &'s don't force the real ones into
	   memory.  */
	YYSTYPE *yyvs1 = yyvs;
	yytype_int16 *yyss1 = yyss;


	/* Each stack pointer address is followed by the size of the
	   data in use in that stack, in bytes.  This used to be a
	   conditional around just the two extra args, but that might
	   be undefined if yyoverflow is a macro.  */
	yyoverflow (YY_("memory exhausted"),
		    &yyss1, yysize * sizeof (*yyssp),
		    &yyvs1, yysize * sizeof (*yyvsp),

		    &yystacksize);

	yyss = yyss1;
	yyvs = yyvs1;
      }
#else /* no yyoverflow */
# ifndef YYSTACK_RELOCATE
      goto yyexhaustedlab;
# else
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
	goto yyexhaustedlab;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
	yystacksize = YYMAXDEPTH;

      {
	yytype_int16 *yyss1 = yyss;
	union yyalloc *yyptr =
	  (union yyalloc *) YYSTACK_ALLOC (YYSTACK_BYTES (yystacksize));
	if (! yyptr)
	  goto yyexhaustedlab;
	YYSTACK_RELOCATE (yyss);
	YYSTACK_RELOCATE (yyvs);

#  undef YYSTACK_RELOCATE
	if (yyss1 != yyssa)
	  YYSTACK_FREE (yyss1);
      }
# endif
#endif /* no yyoverflow */

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;


      YYDPRINTF ((stderr, "Stack size increased to %lu\n",
		  (unsigned long int) yystacksize));

      if (yyss + yystacksize - 1 <= yyssp)
	YYABORT;
    }

  YYDPRINTF ((stderr, "Entering state %d\n", yystate));

  goto yybackup;

/*-----------.
| yybackup.  |
`-----------*/
yybackup:

  /* Do appropriate processing given the current state.  Read a
     look-ahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to look-ahead token.  */
  yyn = yypact[yystate];
  if (yyn == YYPACT_NINF)
    goto yydefault;

  /* Not known => get a look-ahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid look-ahead symbol.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      yychar = YYLEX;
    }

  if (yychar <= YYEOF)
    {
      yychar = yytoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
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
      if (yyn == 0 || yyn == YYTABLE_NINF)
	goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  if (yyn == YYFINAL)
    YYACCEPT;

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the look-ahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);

  /* Discard the shifted token unless it is eof.  */
  if (yychar != YYEOF)
    yychar = YYEMPTY;

  yystate = yyn;
  *++yyvsp = yylval;

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
| yyreduce -- Do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     `$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
      
/* Line 1267 of yacc.c.  */
#line 3182 "y.tab.c"
      default: break;
    }
  YY_SYMBOL_PRINT ("-> $$ =", yyr1[yyn], &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);

  *++yyvsp = yyval;


  /* Now `shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */

  yyn = yyr1[yyn];

  yystate = yypgoto[yyn - YYNTOKENS] + *yyssp;
  if (0 <= yystate && yystate <= YYLAST && yycheck[yystate] == *yyssp)
    yystate = yytable[yystate];
  else
    yystate = yydefgoto[yyn - YYNTOKENS];

  goto yynewstate;


/*------------------------------------.
| yyerrlab -- here on detecting error |
`------------------------------------*/
yyerrlab:
  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
#if ! YYERROR_VERBOSE
      yyerror (YY_("syntax error"));
#else
      {
	YYSIZE_T yysize = yysyntax_error (0, yystate, yychar);
	if (yymsg_alloc < yysize && yymsg_alloc < YYSTACK_ALLOC_MAXIMUM)
	  {
	    YYSIZE_T yyalloc = 2 * yysize;
	    if (! (yysize <= yyalloc && yyalloc <= YYSTACK_ALLOC_MAXIMUM))
	      yyalloc = YYSTACK_ALLOC_MAXIMUM;
	    if (yymsg != yymsgbuf)
	      YYSTACK_FREE (yymsg);
	    yymsg = (char *) YYSTACK_ALLOC (yyalloc);
	    if (yymsg)
	      yymsg_alloc = yyalloc;
	    else
	      {
		yymsg = yymsgbuf;
		yymsg_alloc = sizeof yymsgbuf;
	      }
	  }

	if (0 < yysize && yysize <= yymsg_alloc)
	  {
	    (void) yysyntax_error (yymsg, yystate, yychar);
	    yyerror (yymsg);
	  }
	else
	  {
	    yyerror (YY_("syntax error"));
	    if (yysize != 0)
	      goto yyexhaustedlab;
	  }
      }
#endif
    }



  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse look-ahead token after an
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

  /* Else will try to reuse look-ahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:

  /* Pacify compilers like GCC when the user code never invokes
     YYERROR and the label yyerrorlab therefore never appears in user
     code.  */
  if (/*CONSTCOND*/ 0)
     goto yyerrorlab;

  /* Do not reclaim the symbols of the rule which action triggered
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
  yyerrstatus = 3;	/* Each real token shifted decrements this.  */

  for (;;)
    {
      yyn = yypact[yystate];
      if (yyn != YYPACT_NINF)
	{
	  yyn += YYTERROR;
	  if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYTERROR)
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
		  yystos[yystate], yyvsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  if (yyn == YYFINAL)
    YYACCEPT;

  *++yyvsp = yylval;


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", yystos[yyn], yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturn;

/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturn;

#ifndef yyoverflow
/*-------------------------------------------------.
| yyexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  /* Fall through.  */
#endif

yyreturn:
  if (yychar != YYEOF && yychar != YYEMPTY)
     yydestruct ("Cleanup: discarding lookahead",
		 yytoken, &yylval);
  /* Do not reclaim the symbols of the rule which action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
		  yystos[*yyssp], yyvsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif
#if YYERROR_VERBOSE
  if (yymsg != yymsgbuf)
    YYSTACK_FREE (yymsg);
#endif
  /* Make sure YYID is used.  */
  return YYID (yyresult);
}


#line 375 "yaccs/verilog.yacc"


