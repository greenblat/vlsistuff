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
     pragma1 = 333,
     pragma2 = 334,
     plus_range = 335,
     minus_range = 336,
     floating = 337,
     power = 338,
     star = 339,
     generate = 340,
     endgenerate = 341,
     genvar = 342,
     force = 343,
     release = 344,
     xnor = 345,
     nand = 346,
     nor = 347,
     repeat = 348,
     supply0 = 349,
     supply1 = 350,
     newver = 351,
     return = 352,
     always_comb = 353,
     arith_shift_right = 354,
     SignedLeft = 355,
     shift_right = 356,
     shift_left = 357,
     Veryequal = 358,
     noteqeq = 359,
     StarStar = 360,
     UNARY_PREC = 361
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
#define arith_shift_right 354
#define SignedLeft 355
#define shift_right 356
#define shift_left 357
#define Veryequal 358
#define noteqeq 359
#define StarStar 360
#define UNARY_PREC 361




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
#line 319 "y.tab.c"

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
#define YYLAST   5324

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  133
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  71
/* YYNRULES -- Number of rules.  */
#define YYNRULES  356
/* YYNRULES -- Number of states.  */
#define YYNSTATES  795

/* YYTRANSLATE(YYLEX) -- Bison symbol number corresponding to YYLEX.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   361

#define YYTRANSLATE(YYX)						\
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[YYLEX] -- Bison symbol number corresponding to YYLEX.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   131,     2,   119,     2,   116,   103,     2,
     120,   121,   114,   110,   123,   111,   125,   115,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,   100,   122,
     108,   124,   109,    99,   126,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,   127,     2,   128,   102,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   129,   101,   130,   132,     2,     2,     2,
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
      95,    96,    97,    98,   104,   105,   106,   107,   112,   113,
     117,   118
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
     520,   525,   530,   536,   540,   546,   553,   557,   563,   570,
     577,   584,   591,   597,   605,   614,   622,   630,   634,   636,
     639,   645,   650,   655,   658,   661,   664,   668,   670,   676,
     679,   684,   687,   690,   693,   698,   702,   705,   708,   712,
     716,   719,   721,   725,   731,   735,   737,   739,   741,   743,
     745,   747,   749,   751,   753,   759,   767,   777,   780,   783,
     786,   791,   793,   795,   799,   801,   804,   807,   809,   813,
     816,   819,   825,   829,   834,   840,   845,   851,   857,   865,
     869,   873,   877,   882,   886,   892,   895,   899,   903,   908,
     914,   921,   929,   936,   943,   951,   958,   966,   970,   974,
     977,   979,   981,   983,   986,   988,   994,   998,  1002,  1012,
    1018,  1024,  1028,  1030,  1034,  1037,  1039,  1043,  1047,  1051,
    1055,  1059,  1061,  1064,  1066,  1068,  1071,  1075,  1079,  1082,
    1084,  1086,  1090,  1092,  1098,  1104,  1110,  1114,  1116,  1118,
    1120,  1123,  1126,  1129,  1132,  1135,  1138,  1142,  1145,  1148,
    1150,  1152,  1154,  1156,  1158,  1160,  1163,  1166,  1168,  1170,
    1172,  1174,  1176,  1180,  1184,  1186,  1189,  1191,  1194,  1198,
    1202,  1207,  1212,  1219,  1221,  1223,  1225,  1227,  1229,  1231,
    1233,  1235,  1237,  1239,  1241,  1243,  1245,  1247,  1249,  1254,
    1256,  1258,  1260,  1262,  1264,  1266,  1269,  1273,  1277,  1280,
    1286,  1290,  1294,  1298,  1302,  1306,  1310,  1314,  1318,  1322,
    1326,  1330,  1334,  1338,  1342,  1346,  1350,  1354,  1358,  1362,
    1366,  1370,  1374,  1378,  1382,  1386,  1391,  1395,  1397,  1400,
    1403,  1406,  1409,  1412,  1415,  1418,  1421
};

/* YYRHS -- A `-1'-separated list of the rules' RHS.  */
static const yytype_int16 yyrhs[] =
{
     134,     0,    -1,   135,    -1,   135,   136,    -1,   136,    -1,
     137,    -1,   144,    -1,     3,     5,   138,   139,   142,     6,
      -1,   119,   120,   162,   121,    -1,   119,   120,   121,    -1,
      -1,   122,    -1,   120,   140,   121,   122,    -1,   120,   121,
     122,    -1,   140,   123,   141,    -1,   141,    -1,   196,     5,
      -1,   196,   194,     5,    -1,   196,    21,     5,    -1,   196,
     194,     5,   194,    -1,   196,   194,   194,     5,    -1,     5,
      -1,   196,     5,   124,   202,    -1,   196,   194,     5,   124,
     202,    -1,   143,   142,    -1,    -1,   146,    -1,   147,    -1,
     164,    -1,   171,    -1,   172,    -1,   155,    -1,   156,    -1,
     157,    -1,   145,    -1,   151,    -1,   152,    -1,   144,    -1,
     181,    -1,    96,    -1,    66,    45,    -1,    66,     5,    -1,
      66,     5,   203,    -1,    66,     4,     5,   115,     4,     5,
      -1,    54,   180,    -1,   196,   193,   122,    -1,    17,   193,
     122,    -1,   197,   193,   122,    -1,   197,   193,   124,   203,
     122,    -1,   196,   194,   193,   122,    -1,   196,   194,   193,
     194,   122,    -1,   197,   194,   193,   122,    -1,   197,   194,
       5,   124,   203,   122,    -1,   197,   194,     5,   194,   122,
      -1,   197,   194,   194,   193,   122,    -1,   197,   194,   194,
       5,   124,   203,   122,    -1,   197,     5,   194,   122,    -1,
     197,   170,   193,   122,    -1,   197,   170,     5,   124,   203,
     122,    -1,     5,    27,     5,     5,   122,    -1,     7,   185,
     122,    -1,     7,   167,   192,   124,   203,   122,    -1,     7,
     148,   167,   192,   124,   203,   122,    -1,     7,   148,   192,
     124,   203,   122,    -1,   120,   149,   123,   149,   121,    -1,
      67,    -1,    68,    -1,    69,    -1,    70,    -1,    71,    -1,
      72,    -1,    73,    -1,    74,    -1,   194,    -1,    21,    -1,
      56,     5,   122,   153,   191,    57,    -1,    56,     5,   122,
     191,    57,    -1,    56,   194,   194,     5,   122,   153,   180,
      57,    -1,    56,   150,     5,   122,   153,   180,    57,    -1,
      56,   150,     5,   122,   180,    57,    -1,    56,     5,   120,
     140,   121,   122,   180,    57,    -1,    56,     5,   120,   140,
     121,   122,   153,   180,    57,    -1,    56,   150,     5,   120,
     140,   121,   122,   180,    57,    -1,    56,   150,     5,   120,
     140,   121,   122,   153,   180,    57,    -1,    58,     5,   122,
     153,   180,    59,    -1,    58,     5,   122,   180,    59,    -1,
      58,     5,   120,   140,   121,   122,   180,    59,    -1,    58,
       5,   120,   140,   121,   122,   153,   180,    59,    -1,   153,
     154,    -1,   154,    -1,    11,   193,   122,    -1,    22,   193,
     122,    -1,    23,   193,   122,    -1,    11,   194,   193,   122,
      -1,    11,   194,     5,   194,   122,    -1,    11,   194,   194,
       5,   122,    -1,     9,    11,   194,   194,     5,   122,    -1,
       8,   193,   122,    -1,     8,   193,   194,   122,    -1,     8,
     194,   194,   193,   122,    -1,     8,    21,   193,   122,    -1,
      21,   193,   122,    -1,    21,   193,   194,   122,    -1,    47,
     160,   122,    -1,    47,    16,   160,   122,    -1,    47,   194,
     160,   122,    -1,    47,   194,   194,   160,   122,    -1,    47,
      16,   194,   160,   122,    -1,    48,   160,   122,    -1,    48,
     194,   160,   122,    -1,    48,   194,   194,   160,   122,    -1,
      46,   159,   122,    -1,   201,   124,   203,    -1,   159,   123,
     158,    -1,   158,    -1,   160,   123,   161,    -1,   161,    -1,
       5,   124,   203,    -1,   162,   123,   163,    -1,   163,    -1,
      48,     5,   124,   203,    -1,    47,     5,   124,   203,    -1,
      47,   194,     5,   124,   203,    -1,     5,   124,   203,    -1,
       5,     5,   120,   121,   122,    -1,     5,   170,     5,   120,
     121,   122,    -1,     5,     5,   122,    -1,    42,   120,   190,
     121,   122,    -1,    42,     5,   120,   190,   121,   122,    -1,
       5,     5,   120,   165,   121,   122,    -1,    42,     5,   120,
     165,   121,   122,    -1,     5,     5,   120,   190,   121,   122,
      -1,     5,   120,   190,   121,   122,    -1,     5,   170,     5,
     120,   165,   121,   122,    -1,     5,   170,     5,   194,   120,
     165,   121,   122,    -1,     5,     5,   194,   120,   165,   121,
     122,    -1,     5,     5,   194,   120,   190,   121,   122,    -1,
     165,   123,   166,    -1,   166,    -1,   125,   114,    -1,   125,
       5,   120,   203,   121,    -1,   125,     5,   120,   121,    -1,
     119,   120,   190,   121,    -1,   119,     4,    -1,   119,     5,
      -1,   119,    82,    -1,   168,   123,   169,    -1,   169,    -1,
     125,     5,   120,   203,   121,    -1,   125,     5,    -1,   119,
     120,   190,   121,    -1,   119,     4,    -1,   119,    82,    -1,
     119,     5,    -1,   119,   120,   168,   121,    -1,   119,   120,
     121,    -1,    98,   180,    -1,    35,   180,    -1,    35,   176,
     180,    -1,    85,   173,    86,    -1,   173,   174,    -1,   174,
      -1,    36,   173,    37,    -1,    36,   100,     5,   173,    37,
      -1,    87,     5,   122,    -1,   146,    -1,   147,    -1,   155,
      -1,   156,    -1,   157,    -1,   164,    -1,   175,    -1,   171,
      -1,   145,    -1,    38,   120,   203,   121,   174,    -1,    38,
     120,   203,   121,   174,    39,   174,    -1,    60,   120,   185,
     122,   203,   122,   185,   121,   174,    -1,   126,   114,    -1,
     126,    84,    -1,   126,     5,    -1,   126,   120,   178,   121,
      -1,    42,    -1,   123,    -1,   178,   177,   179,    -1,   179,
      -1,    40,   203,    -1,    41,   203,    -1,   203,    -1,    36,
     191,    37,    -1,    36,    37,    -1,    55,   180,    -1,    36,
     100,     5,   191,    37,    -1,    75,   191,    76,    -1,   192,
     124,   203,   122,    -1,   192,   124,   167,   203,   122,    -1,
     192,    34,   203,   122,    -1,   192,    34,   167,   203,   122,
      -1,    38,   120,   203,   121,   180,    -1,    38,   120,   203,
     121,   180,    39,   180,    -1,    43,   203,   122,    -1,    21,
     193,   122,    -1,    11,   193,   122,    -1,    11,   194,   193,
     122,    -1,    89,   203,   122,    -1,    88,   203,   124,   203,
     122,    -1,   176,   122,    -1,    44,     5,   122,    -1,    77,
       5,   122,    -1,     5,   120,   121,   122,    -1,     5,   120,
     190,   121,   122,    -1,    49,   120,   203,   121,   187,    52,
      -1,    49,   120,   203,   121,   187,   189,    52,    -1,    49,
     120,   203,   121,   189,    52,    -1,    50,   120,   203,   121,
     187,    52,    -1,    50,   120,   203,   121,   187,   189,    52,
      -1,    51,   120,   203,   121,   187,    52,    -1,    51,   120,
     203,   121,   187,   189,    52,    -1,   119,   203,   122,    -1,
     119,   203,   180,    -1,     5,   122,    -1,   182,    -1,   183,
      -1,   184,    -1,   201,   122,    -1,   181,    -1,     7,   192,
     124,   203,   122,    -1,    97,     5,   122,    -1,    78,    45,
      79,    -1,    60,   120,   185,   122,   203,   122,   185,   121,
     180,    -1,    93,   120,   203,   121,   180,    -1,    61,   120,
     203,   121,   180,    -1,   185,   123,   186,    -1,   186,    -1,
     192,   124,   203,    -1,   187,   188,    -1,   188,    -1,   190,
     100,   180,    -1,   190,   100,   122,    -1,    53,   100,   180,
      -1,    53,   100,   122,    -1,   190,   123,   203,    -1,   203,
      -1,   191,   180,    -1,   180,    -1,     5,    -1,     5,   194,
      -1,     5,   195,   194,    -1,     5,   195,   195,    -1,     5,
     195,    -1,   201,    -1,   198,    -1,     5,   123,   193,    -1,
       5,    -1,   127,   203,   100,   203,   128,    -1,   127,   203,
      80,   203,   128,    -1,   127,   203,    81,   203,   128,    -1,
     127,   203,   128,    -1,     8,    -1,     9,    -1,    10,    -1,
       9,    11,    -1,     8,    12,    -1,     9,    12,    -1,    10,
      12,    -1,     8,    16,    -1,     9,    16,    -1,     9,    11,
      16,    -1,     9,    13,    -1,     8,    13,    -1,    13,    -1,
      11,    -1,    12,    -1,    16,    -1,    21,    -1,    22,    -1,
      11,    16,    -1,    12,    16,    -1,    87,    -1,    94,    -1,
      95,    -1,    14,    -1,    15,    -1,   129,   199,   130,    -1,
     199,   123,   200,    -1,   200,    -1,   203,   198,    -1,   203,
      -1,   107,   198,    -1,     5,   125,   201,    -1,     5,   125,
       5,    -1,     5,   125,     5,   194,    -1,     5,   125,     5,
     195,    -1,     5,   125,     5,   120,   203,   121,    -1,     4,
      -1,    82,    -1,    45,    -1,    18,    -1,    19,    -1,    20,
      -1,    24,    -1,    25,    -1,    26,    -1,     5,    -1,   201,
      -1,     4,    -1,    82,    -1,    45,    -1,    66,    -1,    66,
     120,   203,   121,    -1,    18,    -1,    19,    -1,    20,    -1,
      24,    -1,    25,    -1,    26,    -1,     5,   194,    -1,     5,
     195,   194,    -1,     5,   195,   195,    -1,     5,   195,    -1,
     203,    99,   203,   100,   203,    -1,   203,   110,   203,    -1,
     203,   114,   203,    -1,   203,   111,   203,    -1,   203,   115,
     203,    -1,   203,   116,   203,    -1,   203,   102,   203,    -1,
     203,   101,   203,    -1,   203,   103,   203,    -1,   203,   108,
     203,    -1,   203,   109,   203,    -1,   203,    83,   203,    -1,
     203,    28,   203,    -1,   203,    29,   203,    -1,   203,    90,
     203,    -1,   203,    91,   203,    -1,   203,    92,   203,    -1,
     203,    31,   203,    -1,   203,    30,   203,    -1,   203,    32,
     203,    -1,   203,   113,   203,    -1,   203,    33,   203,    -1,
     203,    34,   203,    -1,   203,   107,   203,    -1,   203,   106,
     203,    -1,   203,   104,   203,    -1,     5,   120,   190,   121,
      -1,   120,   203,   121,    -1,   198,    -1,   111,   203,    -1,
     101,   203,    -1,   103,   203,    -1,   102,   203,    -1,    90,
     203,    -1,    92,   203,    -1,    91,   203,    -1,   131,   203,
      -1,   132,   203,    -1
};

/* YYRLINE[YYN] -- source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,    45,    45,    46,    46,    47,    47,    48,    50,    50,
      50,    51,    51,    51,    52,    52,    54,    54,    54,    54,
      54,    54,    54,    54,    58,    58,    61,    62,    63,    64,
      65,    66,    67,    68,    69,    70,    71,    72,    73,    74,
      78,    78,    78,    78,    79,    81,    82,    83,    84,    85,
      86,    87,    88,    89,    90,    91,    92,    93,    94,    95,
      99,   100,   101,   102,   105,   106,   106,   106,   106,   106,
     106,   106,   106,   107,   107,   109,   110,   111,   112,   113,
     114,   115,   116,   117,   120,   121,   122,   123,   126,   126,
     128,   129,   130,   131,   132,   133,   134,   135,   136,   137,
     138,   139,   140,   144,   145,   146,   147,   148,   150,   150,
     150,   151,   152,   153,   153,   155,   155,   156,   158,   158,
     160,   161,   162,   163,   167,   168,   169,   170,   171,   172,
     173,   174,   175,   176,   177,   178,   179,   187,   187,   188,
     188,   188,   190,   190,   190,   190,   191,   191,   192,   192,
     193,   193,   193,   193,   193,   193,   196,   196,   196,   199,
     201,   201,   204,   205,   206,   207,   208,   209,   210,   211,
     212,   213,   214,   215,   216,   217,   222,   227,   227,   227,
     227,   228,   228,   229,   229,   230,   230,   230,   235,   236,
     237,   238,   239,   240,   241,   242,   243,   244,   245,   246,
     247,   248,   249,   250,   251,   252,   253,   254,   255,   256,
     257,   258,   259,   260,   261,   262,   263,   264,   265,   266,
     267,   268,   269,   270,   271,   272,   273,   276,   277,   278,
     279,   280,   280,   281,   282,   282,   283,   283,   284,   284,
     286,   286,   287,   287,   290,   290,   290,   290,   290,   290,
     290,   292,   292,   294,   294,   294,   295,   297,   297,   297,
     297,   297,   297,   297,   297,   297,   297,   297,   297,   299,
     299,   299,   299,   299,   299,   299,   299,   299,   299,   299,
     299,   299,   301,   302,   302,   304,   305,   306,   310,   311,
     312,   313,   314,   318,   319,   320,   321,   321,   321,   321,
     321,   321,   325,   326,   327,   328,   329,   330,   331,   332,
     332,   332,   332,   332,   332,   333,   334,   335,   336,   337,
     338,   339,   340,   341,   342,   343,   344,   345,   346,   347,
     348,   349,   350,   351,   352,   353,   354,   355,   356,   357,
     358,   359,   360,   361,   362,   363,   364,   365,   366,   367,
     368,   369,   370,   371,   372,   373,   374
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
  "disable", "pragma1", "pragma2", "plus_range", "minus_range", "floating",
  "power", "star", "generate", "endgenerate", "genvar", "force", "release",
  "xnor", "nand", "nor", "repeat", "supply0", "supply1", "newver",
  "return", "always_comb", "'?'", "':'", "'|'", "'^'", "'&'",
  "arith_shift_right", "SignedLeft", "shift_right", "shift_left", "'<'",
  "'>'", "'+'", "'-'", "Veryequal", "noteqeq", "'*'", "'/'", "'%'",
  "StarStar", "UNARY_PREC", "'#'", "'('", "')'", "';'", "','", "'='",
  "'.'", "'@'", "'['", "']'", "'{'", "'}'", "'!'", "'~'", "$accept",
  "Main", "Mains", "MainItem", "Module", "Hparams", "Header",
  "Header_list", "Header_item", "Module_stuffs", "Mstuff", "Define",
  "Initial", "Definition", "Assign", "StrengthDef", "Strength", "WidthInt",
  "Function", "Task", "Mem_defs", "Mem_def", "Parameter", "Localparam",
  "Defparam", "DottedPair", "DottedPairs", "Pairs", "Pair", "head_params",
  "head_param", "Instance", "Conns_list", "Connection", "AssignParams",
  "Prms_list", "PrmAssign", "InstParams", "Always", "Generate",
  "GenStatements", "GenStatement", "GenFor_statement", "When", "Or_coma",
  "When_items", "When_item", "Statement", "Pragma", "For_statement",
  "Repeat_statement", "While_statement", "Soft_assigns", "Soft_assign",
  "Cases", "Case", "Default", "Exprs", "Statements", "LSH", "Tokens_list",
  "Width", "BusBit", "ExtDir", "IntDir", "CurlyList", "CurlyItems",
  "CurlyItem", "Dotted", "Literal", "Expr", 0
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
     345,   346,   347,   348,   349,   350,   351,   352,   353,    63,
      58,   124,    94,    38,   354,   355,   356,   357,    60,    62,
      43,    45,   358,   359,    42,    47,    37,   360,   361,    35,
      40,    41,    59,    44,    61,    46,    64,    91,    93,   123,
     125,    33,   126
};
# endif

/* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint8 yyr1[] =
{
       0,   133,   134,   135,   135,   136,   136,   137,   138,   138,
     138,   139,   139,   139,   140,   140,   141,   141,   141,   141,
     141,   141,   141,   141,   142,   142,   143,   143,   143,   143,
     143,   143,   143,   143,   143,   143,   143,   143,   143,   143,
     144,   144,   144,   144,   145,   146,   146,   146,   146,   146,
     146,   146,   146,   146,   146,   146,   146,   146,   146,   146,
     147,   147,   147,   147,   148,   149,   149,   149,   149,   149,
     149,   149,   149,   150,   150,   151,   151,   151,   151,   151,
     151,   151,   151,   151,   152,   152,   152,   152,   153,   153,
     154,   154,   154,   154,   154,   154,   154,   154,   154,   154,
     154,   154,   154,   155,   155,   155,   155,   155,   156,   156,
     156,   157,   158,   159,   159,   160,   160,   161,   162,   162,
     163,   163,   163,   163,   164,   164,   164,   164,   164,   164,
     164,   164,   164,   164,   164,   164,   164,   165,   165,   166,
     166,   166,   167,   167,   167,   167,   168,   168,   169,   169,
     170,   170,   170,   170,   170,   170,   171,   171,   171,   172,
     173,   173,   174,   174,   174,   174,   174,   174,   174,   174,
     174,   174,   174,   174,   174,   174,   175,   176,   176,   176,
     176,   177,   177,   178,   178,   179,   179,   179,   180,   180,
     180,   180,   180,   180,   180,   180,   180,   180,   180,   180,
     180,   180,   180,   180,   180,   180,   180,   180,   180,   180,
     180,   180,   180,   180,   180,   180,   180,   180,   180,   180,
     180,   180,   180,   180,   180,   180,   180,   181,   182,   183,
     184,   185,   185,   186,   187,   187,   188,   188,   189,   189,
     190,   190,   191,   191,   192,   192,   192,   192,   192,   192,
     192,   193,   193,   194,   194,   194,   195,   196,   196,   196,
     196,   196,   196,   196,   196,   196,   196,   196,   196,   197,
     197,   197,   197,   197,   197,   197,   197,   197,   197,   197,
     197,   197,   198,   199,   199,   200,   200,   200,   201,   201,
     201,   201,   201,   202,   202,   202,   202,   202,   202,   202,
     202,   202,   203,   203,   203,   203,   203,   203,   203,   203,
     203,   203,   203,   203,   203,   203,   203,   203,   203,   203,
     203,   203,   203,   203,   203,   203,   203,   203,   203,   203,
     203,   203,   203,   203,   203,   203,   203,   203,   203,   203,
     203,   203,   203,   203,   203,   203,   203,   203,   203,   203,
     203,   203,   203,   203,   203,   203,   203
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
       4,     4,     5,     3,     5,     6,     3,     5,     6,     6,
       6,     6,     5,     7,     8,     7,     7,     3,     1,     2,
       5,     4,     4,     2,     2,     2,     3,     1,     5,     2,
       4,     2,     2,     2,     4,     3,     2,     2,     3,     3,
       2,     1,     3,     5,     3,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     5,     7,     9,     2,     2,     2,
       4,     1,     1,     3,     1,     2,     2,     1,     3,     2,
       2,     5,     3,     4,     5,     4,     5,     5,     7,     3,
       3,     3,     4,     3,     5,     2,     3,     3,     4,     5,
       6,     7,     6,     6,     7,     6,     7,     3,     3,     2,
       1,     1,     1,     2,     1,     5,     3,     3,     9,     5,
       5,     3,     1,     3,     2,     1,     3,     3,     3,     3,
       3,     1,     2,     1,     1,     2,     3,     3,     2,     1,
       1,     3,     1,     5,     5,     5,     3,     1,     1,     1,
       2,     2,     2,     2,     2,     2,     3,     2,     2,     1,
       1,     1,     1,     1,     1,     2,     2,     1,     1,     1,
       1,     1,     3,     3,     1,     2,     1,     2,     3,     3,
       4,     4,     6,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     4,     1,
       1,     1,     1,     1,     1,     2,     3,     3,     2,     5,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     4,     3,     1,     2,     2,
       2,     2,     2,     2,     2,     2,     2
};

/* YYDEFACT[STATE-NAME] -- Default rule to reduce with in state
   STATE-NUM when YYTABLE doesn't specify something else to do.  Zero
   means the default is an error.  */
static const yytype_uint16 yydefact[] =
{
       0,     0,     0,     0,     2,     4,     5,     6,    10,     0,
      41,    40,     1,     3,     0,     0,     0,   304,   302,   309,
     310,   311,   312,   313,   314,   306,   307,   305,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   347,
     303,    42,     0,     0,    11,    25,     0,     0,     0,     0,
     315,   318,     0,   352,   354,   353,   349,   351,   350,   348,
       0,     0,     0,   284,   286,   355,   356,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     9,     0,   119,    21,
     257,   258,   259,     0,     0,    15,     0,     0,     0,   270,
     271,   269,   280,   281,   272,     0,   273,   274,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   277,   278,
     279,    39,     0,     0,    25,    37,    34,    26,    27,    35,
      36,    31,    32,    33,    28,    29,    30,    38,     0,     0,
       0,     0,   241,   289,   288,     0,   316,   317,     0,   346,
     287,     0,   282,   285,   331,   332,   337,   336,   338,   340,
     341,   330,   333,   334,   335,     0,   326,   325,   327,   344,
     343,   342,   328,   329,   320,   322,   339,   321,   323,   324,
       0,     0,     0,     0,     0,     8,     0,   261,   268,   264,
     260,   262,   267,   265,   263,    13,     0,     0,    16,     0,
       0,     0,     0,     0,     0,     0,   244,     0,     0,     0,
       0,     0,   232,     0,   250,   249,   275,   276,   252,     0,
     244,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   157,   224,   220,   221,   222,     0,   249,
       0,     0,     0,   114,     0,     0,     0,     0,     0,   116,
       0,     0,     0,     0,    44,     0,    74,     0,    73,     0,
       0,     0,     0,     0,   277,   173,   165,   166,   167,   168,
     169,   170,   172,     0,   161,   171,   156,     7,    24,     0,
       0,   252,     0,     0,     0,    43,   345,     0,     0,   290,
     291,     0,     0,     0,   256,   308,   283,     0,   123,     0,
       0,     0,     0,   118,   266,    12,    14,     0,    18,    17,
       0,     0,   126,     0,     0,   151,   153,   152,     0,     0,
       0,   245,   248,   143,   144,   145,     0,    65,    66,    67,
      68,    69,    70,    71,    72,     0,     0,     0,     0,    60,
       0,     0,     0,    46,     0,   219,     0,     0,     0,     0,
     189,     0,   243,     0,     0,     0,     0,     0,     0,     0,
     190,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     179,   178,   177,     0,   205,   158,     0,     0,   223,     0,
       0,   111,     0,     0,     0,     0,     0,   103,     0,     0,
       0,   108,     0,     0,     0,     0,     0,     0,     0,     0,
     227,     0,     0,     0,     0,     0,   159,   160,    45,     0,
       0,   252,     0,    47,     0,   252,     0,     0,   240,     0,
       0,     0,     0,   319,   121,     0,   120,   293,   296,   297,
     298,   299,   300,   301,   295,   294,    22,     0,    19,    20,
       0,     0,     0,   138,     0,     0,     0,   155,     0,     0,
     147,     0,     0,     0,     0,   246,   247,     0,     0,     0,
       0,     0,   231,   233,   251,     0,     0,     0,   201,     0,
     200,     0,   188,   242,     0,   199,   206,     0,     0,     0,
       0,     0,   192,   207,     0,   203,     0,   226,   217,   218,
       0,     0,     0,   184,   187,     0,     0,     0,     0,     0,
       0,     0,   113,   112,   117,   104,     0,   115,   105,     0,
     109,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      89,     0,     0,     0,     0,     0,     0,     0,     0,   162,
       0,     0,   164,    49,     0,    56,     0,    57,     0,     0,
       0,    51,   252,     0,   292,   254,   255,   253,   122,    23,
     124,     0,   139,     0,     0,     0,     0,     0,    59,   149,
     154,     0,   150,   132,     0,     0,     0,   142,     0,     0,
       0,     0,   208,     0,     0,   202,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   185,   186,   181,   180,   182,
       0,     0,   195,     0,   193,     0,     0,   127,   107,   106,
     110,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    88,     0,    76,     0,     0,     0,     0,     0,     0,
      85,     0,     0,     0,    50,     0,    48,     0,    53,     0,
      54,     0,   129,   137,   131,     0,     0,     0,   146,   125,
       0,     0,    64,     0,    63,    61,   209,   225,   191,   197,
       0,     0,   235,     0,     0,     0,     0,     0,   230,   204,
     229,   183,   196,   194,   130,   128,     0,     0,    97,     0,
       0,     0,    90,   252,     0,     0,   101,     0,    91,    92,
      75,     0,     0,    79,     0,     0,     0,     0,    84,   163,
     174,     0,    58,    52,     0,   141,     0,   135,   136,     0,
     133,     0,    62,     0,     0,   210,   234,     0,   212,     0,
     213,     0,   215,     0,     0,     0,     0,   100,    98,     0,
       0,     0,    93,     0,   102,     0,    78,     0,     0,     0,
       0,     0,     0,     0,     0,    55,   140,   148,   134,   198,
     239,   238,   211,   237,   236,   214,   216,     0,     0,    80,
      99,     0,    94,    95,     0,     0,    90,     0,   101,    77,
       0,    86,   175,     0,     0,    81,    96,     0,    82,    93,
      87,     0,   228,    83,   176
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,     3,     4,     5,     6,    15,    45,   104,   105,   133,
     134,     7,   285,   286,   287,   219,   355,   277,   139,   140,
     539,   540,   288,   289,   290,   263,   264,   268,   269,    97,
      98,   291,   462,   463,   220,   469,   470,   215,   292,   146,
     293,   294,   295,   273,   610,   512,   513,   372,   254,   255,
     256,   257,   221,   222,   671,   672,   673,   674,   373,   258,
     229,   341,   342,   148,   149,    39,    62,    63,    40,   456,
     152
};

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
#define YYPACT_NINF -517
static const yytype_int16 yypact[] =
{
      30,    44,   207,    82,    30,  -517,  -517,  -517,   -12,   113,
    1711,  -517,  -517,  -517,    11,   -19,    52,  -517,   -28,  -517,
    -517,  -517,  -517,  -517,  -517,  -517,   109,  -517,  1711,  1711,
    1711,  1711,  1711,  1711,  1711,  1711,    32,  1711,  1711,  -517,
    -517,  5119,    61,    59,  -517,  4012,   234,  1711,   208,  1711,
    -517,   117,  1711,  -517,  -517,  -517,  -517,  -517,  -517,  -517,
    4210,   133,   -44,  -517,  2573,  -517,  -517,  1711,  1711,  1711,
    1711,  1711,  1711,  1711,  1711,  1711,  1711,  1711,  1711,  1711,
    1711,  1711,  1711,  1711,  1711,  1711,  1711,  1711,  1711,  1711,
    1711,  1711,  1711,   167,    39,   277,  -517,    93,  -517,  -517,
     303,   257,   295,   178,   158,  -517,    14,    88,     7,   307,
     344,  -517,  -517,  -517,  -517,   335,  -517,  -517,  2522,     5,
     361,    22,    42,  2522,    20,   381,   325,  4325,  -517,  -517,
    -517,  -517,  2522,   388,  4012,  -517,  -517,  -517,  -517,  -517,
    -517,  -517,  -517,  -517,  -517,  -517,  -517,  -517,    48,    26,
     415,   209,  5119,    95,  -517,  2662,  -517,  -517,  4323,  -517,
    -517,    32,  -517,  -517,   365,   423,   150,   150,   150,   321,
     321,  -517,   539,   539,   539,  5090,  5208,   539,   683,  1090,
    1090,  1090,   321,   321,   326,   326,   150,  -517,  -517,  -517,
    1711,   306,  1711,   422,   309,  -517,    58,  -517,  -517,  -517,
     451,  -517,  -517,  -517,  -517,  -517,   316,   334,   346,   454,
      49,   123,   481,    38,  1711,   492,   211,    86,   521,    21,
      15,   125,  -517,   383,  -517,  -517,  -517,  -517,   389,   399,
     112,    15,    48,   335,  1953,   403,  1711,   523,   424,   426,
     433,  2522,   448,   455,  2522,   530,  1711,  1711,   457,   537,
    1711,    89,  2049,  -517,  -517,  -517,  -517,  -517,   -20,   456,
     460,  1711,   430,  -517,   132,   458,   459,    42,   149,  -517,
      42,   223,    42,   463,  -517,   262,  -517,   576,   469,   263,
     507,  2937,   477,   478,   594,  -517,  -517,  -517,  -517,  -517,
    -517,  -517,  -517,  4104,  -517,  -517,  -517,  -517,  -517,   479,
     335,   -99,   595,   265,    54,  -517,  -517,  1711,  1711,  -517,
    -517,  1711,  1711,  1711,  -517,  -517,  -517,  1711,  5119,  1711,
    5001,   480,  1711,  -517,  -517,  -517,  -517,   279,  -517,   -53,
     597,   729,  -517,   485,   601,  -517,  -517,  -517,   947,   280,
     104,  -517,   117,  -517,  -517,  -517,  1711,  -517,  -517,  -517,
    -517,  -517,  -517,  -517,  -517,   484,    15,   486,   487,  -517,
      15,  1711,   335,  -517,  1400,  -517,   491,   496,   335,   498,
    -517,   603,  -517,  2070,  1711,  2970,   499,  1711,  1711,  1711,
    -517,    15,  1711,  2159,   501,  2819,  3010,  1711,   502,  1816,
    -517,  -517,  -517,  1016,  -517,  -517,  1469,  1469,  -517,  1520,
     284,  -517,   361,  1711,  1711,   251,   604,  -517,   604,   256,
     604,  -517,   327,   604,   334,  1932,   288,   620,   334,  1932,
    -517,   621,  4158,  1711,    15,   505,  -517,  -517,  -517,   -88,
     506,   380,   510,  -517,  1711,   241,   511,   629,  5119,  4358,
     887,  2696,  2785,  5119,  5119,  1711,  5119,  -517,  -517,  -517,
    -517,  -517,  -517,  -517,  -517,  -517,  -517,   279,  -517,  -517,
     514,    71,   290,  -517,   291,  1520,   517,  -517,   635,   294,
    -517,   298,   519,   -60,   524,  -517,  -517,   302,   521,   532,
    1711,  1711,  -517,  5119,  -517,   535,   305,  1711,  -517,   538,
    -517,  2522,  -517,  -517,  4452,  -517,  -517,  4486,  4580,  4614,
     397,  4708,  -517,  -517,  1711,  -517,  4742,  -517,  -517,  -517,
    1711,  1711,   -21,  -517,  5119,  1711,  3105,  1711,  3134,   323,
     324,   540,  -517,  5119,  5119,  -517,   418,  -517,  -517,   428,
    -517,   435,   337,    27,   650,    48,   335,   335,   335,  1932,
    -517,  2219,   334,  1932,   541,   341,  1932,   605,  4325,  -517,
    4836,   439,  -517,  -517,   544,  -517,  1711,  -517,  3229,  1711,
     548,  -517,   440,   550,  -517,  -517,  -517,  -517,  5119,  -517,
    -517,   553,  -517,   555,   554,   556,   342,   345,  -517,   563,
    -517,   559,  -517,  -517,   566,   362,   554,  -517,   564,  1711,
    3258,  3353,  -517,   567,  3382,  -517,  2282,  2522,  1589,  1711,
    1711,  1711,  2522,  3477,  2522,  5119,  5119,  -517,  -517,  -517,
    1016,  3506,  -517,  3601,  -517,   568,   569,  -517,  -517,  -517,
    -517,   570,   335,   -42,   469,   469,   572,    57,   179,   573,
     574,  -517,  2342,  -517,   366,  1932,   641,   219,   577,   642,
    -517,  4212,  4325,  1711,  -517,  3630,  -517,  3725,  -517,  1711,
    -517,  1642,  -517,  -517,  -517,   578,   580,  1711,  -517,  -517,
     582,   369,  -517,  3754,  -517,  -517,  -517,  -517,  -517,   666,
     607,  1165,  -517,   656,   -45,  1220,  1349,  3849,  -517,  -517,
    -517,  -517,  -517,  -517,  -517,  -517,  1932,   587,  -517,   588,
     335,   469,   343,   -99,   590,   713,   437,   598,  -517,  -517,
    -517,   599,   665,  -517,    48,   335,  1932,  1932,  -517,  -517,
     684,  3878,  -517,  -517,  3973,  -517,  4870,  -517,  -517,  4964,
    -517,   606,  -517,  2522,  2402,  -517,  -517,   675,  -517,  2462,
    -517,   677,  -517,   679,    15,  1932,   678,  -517,  -517,   619,
     737,   622,   443,   623,  -517,  1932,  -517,   624,    57,   187,
     686,  1932,   691,  4325,    15,  -517,  -517,  -517,  -517,  -517,
    -517,  -517,  -517,  -517,  -517,  -517,  -517,   387,   694,  -517,
    -517,   630,  -517,  -517,  1932,   701,  -517,   637,  -517,  -517,
     702,  -517,  -517,   395,  2522,  -517,  -517,   707,  -517,  -517,
    -517,  4325,  -517,  -517,  -517
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -517,  -517,  -517,   761,  -517,  -517,  -517,  -396,   560,   636,
    -517,    28,    67,    76,    84,  -517,   293,  -517,  -517,  -517,
    -411,  -516,   115,   143,   146,   367,  -517,   -93,   364,  -517,
     579,   152,  -384,   199,  -202,  -517,   195,   628,   153,  -517,
    -272,  -292,  -517,   661,  -517,  -517,   170,    33,   160,  -517,
    -517,  -517,  -379,   421,   -34,  -387,  -349,   -36,  -228,  -103,
    -145,   -11,    -5,   -37,  -517,   128,  -517,   625,   -48,   328,
     855
};

/* YYTABLE[YYPACT[STATE-NUM]].  What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule which
   number is the opposite.  If zero, do what YYDEFACT says.
   If YYTABLE_NINF, syntax error.  */
#define YYTABLE_NINF -203
static const yytype_int16 yytable[] =
{
     154,   427,   500,   299,   303,   223,   106,    50,   546,   422,
     260,   151,   216,    51,   396,   519,   383,   356,   532,   208,
     216,   607,   545,   631,   362,   275,   216,   266,   192,   271,
     631,   301,   228,     1,   553,   209,    17,    18,   267,   192,
     156,   276,   335,   336,   191,   551,   157,   266,   622,     8,
      19,    20,    21,   228,   329,   729,    22,    23,    24,   435,
     225,   584,   693,    93,    99,   461,    93,   100,   101,   102,
     259,   457,   265,   135,   192,   259,   571,    25,   307,   161,
     688,   576,    12,   193,   259,   192,   162,   367,   369,   585,
     343,   344,    47,   211,   390,   210,     2,    48,    26,    49,
     608,    43,   609,    44,   397,    94,    95,    14,    94,    95,
     270,   272,   136,   278,    27,   212,   357,   358,    16,   631,
     337,   137,    28,    29,    30,   261,   217,   218,   366,   138,
     427,    42,   635,    31,    32,    33,    36,   300,   304,    61,
     217,   192,   309,    34,    36,   213,   634,   192,   310,   192,
      36,   253,    35,   192,   192,   429,   274,   432,   338,   436,
     141,    36,   135,    37,    38,   296,   192,    46,   345,   192,
     106,   225,   225,   391,   405,   192,   192,   409,   339,   412,
     103,   192,    96,   225,   192,   572,   259,   541,   142,   160,
     631,   143,   163,   259,   515,   517,   259,   144,   145,   330,
     333,   136,   661,   392,   259,   147,   346,   213,   214,   393,
     137,     9,    10,   153,   195,   308,   196,   484,   138,   631,
      48,   368,    49,   489,   473,   400,   706,   533,   534,    52,
     704,   192,   364,    74,   365,   631,   224,    48,   150,    49,
     705,   537,   538,   331,    49,   332,   224,   359,   360,   141,
     192,   224,    11,   479,   401,   402,   406,   223,   631,   410,
     224,   413,    36,   596,    90,    91,    92,   417,   200,   201,
     202,   407,   408,   203,   380,   735,   641,   142,   223,   206,
     143,   207,   194,   447,   726,   395,   144,   145,   726,   726,
     430,   190,   563,   437,   147,   464,   751,   448,   449,   450,
     205,   696,   471,   451,   452,   453,   192,   204,   225,   778,
     477,   632,   225,   526,   192,   197,   198,   529,   458,   199,
     531,   223,   727,   226,   454,   259,   731,   733,   486,   474,
     306,   475,   307,   225,   774,   259,    48,   476,    49,    99,
     228,   259,   100,   101,   102,   411,   408,   224,   224,   427,
     710,    69,    70,    71,   265,   767,    69,    70,    71,   224,
     227,   455,   224,   520,   362,   559,   262,   259,   192,   224,
     280,   259,   224,   525,   408,   783,   225,   106,   528,   408,
     224,   106,   414,   418,   415,   419,   279,   433,   623,   434,
     626,   628,   629,   630,   297,    69,    70,    71,    72,    73,
    -201,   472,  -201,   307,    74,   521,   493,   307,   542,    74,
     543,   573,   575,   574,   307,   580,   493,   581,   554,   582,
     305,   307,   509,   587,   560,   307,   593,   321,   307,   577,
     319,    87,    88,   322,    89,    90,    91,    92,   325,    89,
      90,    91,    92,   259,   615,   616,   574,   307,    74,   530,
     408,    67,   547,    69,    70,    71,    72,    73,   621,   328,
     207,   782,   638,   655,   207,   574,   656,   324,   307,    82,
     327,    83,    84,    85,    86,    87,    88,   687,    89,    90,
      91,    92,   694,   660,   224,   574,   334,   701,   224,   207,
     721,   259,   574,   259,  -200,   259,  -200,   340,   259,   794,
    -202,   224,  -202,   362,   556,   106,    74,   361,   784,   224,
     360,   224,   362,    75,    76,    77,   791,   224,   360,   601,
     360,   363,   624,   374,   627,    80,    81,    82,   376,    83,
      84,    85,    86,    87,    88,   384,    89,    90,    91,    92,
     618,   408,   388,   224,   377,   739,   378,   224,   259,   259,
     619,   408,   224,   379,   259,    48,   259,   620,   408,   747,
     749,   643,   360,   362,   649,   675,   676,    67,   381,    69,
      70,    71,    72,    73,   493,   382,   636,   387,   398,   639,
     399,   416,   403,   404,   259,   394,   420,   259,   347,   348,
     349,   350,   351,   352,   353,   354,   192,   423,   424,   425,
     431,   428,   459,   777,   445,   465,   466,   478,   491,   266,
     480,   481,   689,   690,   691,   487,   695,   697,   488,   224,
     490,   496,    74,   503,   507,   544,   548,   552,   555,   493,
     669,   223,   557,   561,   562,   678,   570,   680,   259,   578,
     579,   583,    81,    82,   586,    83,    84,    85,    86,    87,
      88,   223,    89,    90,    91,    92,   589,   592,   259,   259,
     595,   625,   617,   637,   640,   493,   644,   224,   702,   224,
     648,   224,   650,   651,   224,   259,   259,   652,   654,   461,
     740,   259,   741,   657,   468,   662,   225,   259,   659,   666,
     684,   685,   686,   748,   692,   698,   699,   259,   703,   707,
     717,   708,   718,   259,   720,   723,   225,   724,   728,   737,
     738,    67,   742,    69,    70,    71,    72,    73,   743,   736,
     744,   745,   746,   753,   224,   224,   259,   762,   758,   765,
     224,   766,   224,    17,    18,   769,   259,   695,   697,   750,
     752,   770,   771,   779,   772,   773,   776,    19,    20,    21,
     781,   785,   786,    22,    23,    24,   759,   761,   788,   789,
     224,   790,   764,   224,   793,    13,    74,   326,   768,   522,
     298,   588,   527,   653,    25,   323,   658,   302,   775,   252,
     681,   482,     0,     0,   780,   569,   316,    82,     0,    83,
      84,    85,    86,    87,    88,    26,    89,    90,    91,    92,
       0,     0,     0,     0,     0,     0,     0,   787,     0,     0,
       0,    27,     0,     0,   224,     0,     0,   792,     0,    28,
      29,    30,     0,     0,     0,     0,     0,     0,     0,     0,
      31,    32,    33,     0,   224,   224,     0,     0,     0,     0,
      34,     0,     0,     0,     0,     0,     0,     0,     0,    35,
     460,   224,   224,     0,   461,     0,     0,   224,    36,     0,
      37,    38,   224,   224,     0,    41,     0,     0,     0,     0,
       0,     0,     0,   224,     0,     0,     0,     0,     0,   224,
       0,     0,   224,    53,    54,    55,    56,    57,    58,    59,
      60,    64,    65,    66,     0,     0,     0,     0,     0,     0,
       0,     0,   224,     0,   155,     0,     0,   158,     0,     0,
       0,     0,   224,     0,     0,    67,    68,    69,    70,    71,
      72,    73,   164,   165,   166,   167,   168,   169,   170,   171,
     172,   173,   174,   175,   176,   177,   178,   179,   180,   181,
     182,   183,   184,   185,   186,   187,   188,   189,     0,     0,
       0,    17,    18,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    19,    20,    21,     0,     0,
      74,    22,    23,    24,     0,     0,     0,    75,    76,    77,
       0,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,    25,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    26,     0,   565,    64,     0,     0,     0,
      17,    18,     0,     0,     0,     0,     0,     0,     0,    27,
       0,     0,     0,     0,    19,    20,    21,    28,    29,    30,
      22,    23,    24,     0,     0,   318,     0,   320,    31,    32,
      33,     0,     0,     0,     0,     0,   510,   511,    34,     0,
       0,    25,     0,     0,     0,     0,     0,    35,   467,     0,
       0,     0,   468,     0,     0,     0,    36,     0,    37,    38,
       0,     0,    26,     0,     0,     0,     0,     0,     0,     0,
       0,   375,     0,     0,     0,     0,     0,     0,    27,     0,
       0,   385,   386,     0,     0,   389,    28,    29,    30,     0,
       0,     0,     0,     0,     0,     0,     0,    31,    32,    33,
      69,    70,    71,    72,    73,     0,     0,    34,     0,     0,
       0,     0,     0,     0,     0,     0,    35,     0,     0,     0,
       0,     0,     0,     0,     0,    36,     0,    37,    38,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   438,   439,     0,     0,   440,   441,   442,    17,
      18,     0,   443,    74,   444,     0,     0,   446,     0,     0,
       0,     0,     0,    19,    20,    21,     0,     0,     0,    22,
      23,    24,     0,     0,     0,     0,     0,     0,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,     0,
      25,     0,     0,     0,     0,     0,   483,   725,   670,     0,
       0,     0,     0,     0,    17,    18,     0,     0,     0,   494,
       0,    26,   497,   498,   499,     0,     0,   501,    19,    20,
      21,     0,   506,     0,    22,    23,    24,    27,   514,     0,
       0,   516,   518,     0,     0,    28,    29,    30,   523,   524,
       0,     0,     0,     0,     0,    25,    31,    32,    33,     0,
       0,     0,   730,   670,     0,     0,    34,     0,   550,     0,
       0,     0,     0,     0,     0,    35,    26,     0,     0,   558,
       0,     0,     0,     0,    36,     0,    37,    38,     0,     0,
     568,     0,    27,     0,     0,     0,     0,     0,     0,     0,
      28,    29,    30,     0,     0,     0,     0,     0,     0,     0,
       0,    31,    32,    33,     0,     0,     0,     0,     0,     0,
       0,    34,     0,     0,     0,   590,   591,     0,     0,     0,
      35,     0,   594,     0,     0,     0,     0,     0,     0,    36,
       0,    37,    38,    17,    18,     0,     0,     0,     0,   603,
       0,     0,     0,     0,     0,   605,   606,    19,    20,    21,
     611,     0,   613,    22,    23,    24,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    25,     0,     0,     0,     0,     0,
       0,   732,   670,     0,    17,    18,     0,     0,     0,     0,
       0,   645,     0,     0,   647,    26,     0,     0,    19,    20,
      21,     0,     0,     0,    22,    23,    24,     0,     0,     0,
       0,    27,     0,     0,     0,     0,     0,     0,     0,    28,
      29,    30,     0,     0,   663,    25,     0,     0,     0,     0,
      31,    32,    33,     0,     0,     0,   677,     0,     0,     0,
      34,     0,     0,     0,     0,   514,    26,     0,     0,    35,
       0,     0,     0,    17,    18,     0,     0,     0,    36,     0,
      37,    38,    27,     0,     0,     0,     0,    19,    20,    21,
      28,    29,    30,    22,    23,    24,     0,     0,   711,     0,
       0,    31,    32,    33,   714,     0,   716,     0,     0,     0,
       0,    34,   719,     0,    25,     0,     0,     0,     0,     0,
      35,   485,     0,     0,    17,    18,     0,     0,     0,    36,
       0,    37,    38,     0,     0,    26,     0,     0,    19,    20,
      21,     0,     0,     0,    22,    23,    24,     0,     0,     0,
       0,    27,     0,     0,     0,     0,     0,     0,     0,    28,
      29,    30,     0,     0,     0,    25,     0,     0,     0,     0,
      31,    32,    33,     0,     0,     0,     0,     0,     0,     0,
      34,     0,     0,     0,     0,     0,    26,     0,   217,    35,
       0,     0,     0,    17,    18,     0,     0,     0,    36,     0,
      37,    38,    27,     0,     0,     0,     0,    19,    20,    21,
      28,    29,    30,    22,    23,    24,     0,     0,     0,     0,
       0,    31,    32,    33,     0,     0,     0,     0,     0,     0,
       0,    34,     0,     0,    25,     0,     0,     0,     0,     0,
      35,     0,   670,     0,     0,   461,    17,    18,     0,    36,
       0,    37,    38,     0,     0,    26,     0,     0,     0,     0,
      19,    20,    21,     0,     0,     0,    22,    23,    24,     0,
       0,    27,     0,     0,     0,     0,     0,     0,     0,    28,
      29,    30,     0,     0,     0,     0,     0,    25,     0,     0,
      31,    32,    33,     0,     0,     0,     0,     0,     0,     0,
      34,     0,     0,     0,     0,     0,     0,     0,    26,    35,
       0,     0,     0,     0,     0,    17,    18,     0,    36,     0,
      37,    38,     0,     0,    27,     0,     0,     0,     0,    19,
      20,    21,    28,    29,    30,    22,    23,    24,     0,     0,
       0,     0,     0,    31,    32,    33,     0,     0,     0,     0,
       0,     0,     0,    34,     0,     0,    25,     0,     0,     0,
       0,     0,    35,   715,     0,     0,     0,     0,     0,     0,
       0,    36,     0,    37,    38,     0,     0,    26,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    27,     0,     0,     0,     0,     0,     0,
       0,    28,    29,    30,     0,     0,     0,     0,     0,     0,
       0,     0,    31,    32,    33,     0,     0,     0,     0,     0,
       0,   230,    34,   231,     0,     0,     0,   232,     0,     0,
       0,    35,     0,     0,     0,     0,     0,   233,     0,     0,
      36,     0,    37,    38,    67,    68,    69,    70,    71,    72,
      73,     0,   234,     0,   235,     0,     0,     0,     0,   236,
     237,     0,     0,     0,     0,   238,   239,   240,     0,     0,
       0,   241,     0,     0,     0,     0,   242,   243,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   244,     0,   245,   126,     0,     0,     0,     0,    74,
       0,     0,     0,     0,   246,   247,    75,    76,    77,   248,
       0,     0,     0,   249,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,     0,     0,   250,     0,   230,   508,   231,
     533,   534,   251,   535,     0,    36,     0,     0,     0,     0,
       0,     0,     0,   536,   537,   538,     0,     0,   230,     0,
     231,     0,     0,     0,   232,     0,     0,     0,   234,     0,
     235,     0,     0,     0,   233,   236,   237,     0,     0,     0,
       0,   238,   239,   240,     0,     0,     0,   241,     0,   234,
     370,   235,   242,   243,     0,     0,   236,   237,     0,     0,
       0,     0,   238,   239,   240,     0,     0,   244,   241,   245,
     126,     0,     0,   242,   243,     0,     0,     0,     0,     0,
     246,   247,     0,     0,     0,   248,     0,     0,   244,   249,
     245,   126,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   246,   247,     0,     0,     0,   248,     0,     0,     0,
     249,   250,     0,   371,   230,     0,   231,     0,   251,     0,
     232,    36,     0,     0,     0,     0,     0,     0,     0,     0,
     233,     0,   250,     0,     0,   230,     0,   231,     0,   251,
       0,   232,    36,     0,     0,   234,     0,   235,     0,     0,
       0,   233,   236,   237,     0,     0,     0,     0,   238,   239,
     240,     0,     0,     0,   241,     0,   234,   492,   235,   242,
     243,     0,     0,   236,   237,     0,     0,     0,     0,   238,
     239,   240,     0,     0,   244,   241,   245,   126,     0,     0,
     242,   243,     0,     0,     0,     0,     0,   246,   247,     0,
       0,     0,   248,     0,     0,   244,   249,   245,   126,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   246,   247,
       0,     0,     0,   248,   230,     0,   231,   249,   250,     0,
     232,   394,     0,     0,     0,   251,     0,     0,    36,     0,
     233,     0,     0,     0,     0,     0,     0,     0,     0,   250,
       0,     0,     0,     0,     0,   234,   251,   235,     0,    36,
       0,     0,   236,   237,     0,     0,     0,     0,   238,   239,
     240,     0,     0,     0,   241,     0,     0,     0,     0,   242,
     243,     0,     0,     0,   230,     0,   231,     0,     0,     0,
     232,     0,     0,     0,   244,   502,   245,   126,     0,     0,
     233,     0,     0,     0,     0,     0,     0,   246,   247,     0,
       0,     0,   248,     0,     0,   234,   249,   235,     0,     0,
       0,     0,   236,   237,     0,     0,     0,     0,   238,   239,
     240,     0,     0,     0,   241,     0,   633,     0,   250,   242,
     243,     0,     0,     0,     0,   251,     0,   230,    36,   231,
       0,     0,     0,   232,   244,     0,   245,   126,     0,     0,
       0,     0,     0,   233,     0,     0,     0,   246,   247,     0,
       0,     0,   248,     0,     0,     0,   249,     0,   234,   668,
     235,     0,     0,     0,     0,   236,   237,     0,     0,     0,
       0,   238,   239,   240,     0,     0,     0,   241,   250,     0,
       0,     0,   242,   243,     0,   251,     0,   230,    36,   231,
       0,     0,     0,   232,     0,     0,     0,   244,     0,   245,
     126,     0,     0,   233,     0,     0,     0,     0,     0,     0,
     246,   247,     0,     0,     0,   248,     0,     0,   234,   249,
     235,     0,     0,     0,     0,   236,   237,     0,     0,     0,
       0,   238,   239,   240,     0,     0,     0,   241,     0,   700,
       0,   250,   242,   243,     0,     0,     0,   230,   251,   231,
       0,    36,     0,   232,     0,     0,     0,   244,     0,   245,
     126,     0,     0,   233,     0,     0,     0,     0,     0,     0,
     246,   247,     0,     0,     0,   248,     0,     0,   234,   249,
     235,     0,     0,     0,     0,   236,   237,     0,     0,     0,
       0,   238,   239,   240,     0,     0,     0,   241,     0,     0,
       0,   250,   242,   243,     0,     0,     0,   230,   251,   231,
       0,    36,     0,   232,     0,     0,     0,   244,     0,   245,
     126,     0,     0,   233,     0,     0,     0,     0,     0,     0,
     246,   247,     0,     0,     0,   248,     0,     0,   234,   249,
     235,     0,     0,     0,     0,   236,   237,     0,     0,     0,
       0,   238,   239,   240,     0,     0,     0,   241,     0,     0,
       0,   250,   242,   243,   760,     0,     0,   230,   251,   231,
       0,    36,     0,   232,     0,     0,     0,   244,     0,   245,
     126,     0,     0,   233,     0,     0,     0,     0,     0,     0,
     246,   247,     0,     0,     0,   248,     0,     0,   234,   249,
     235,     0,     0,     0,     0,   236,   237,     0,     0,     0,
       0,   238,   239,   240,     0,     0,     0,   241,     0,     0,
       0,   250,   242,   243,   763,     0,     0,     0,   251,     0,
       0,    36,     0,     0,     0,     0,     0,   244,     0,   245,
     126,    67,    68,    69,    70,    71,    72,    73,     0,     0,
     246,   247,     0,     0,     0,   248,     0,     0,     0,   249,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   250,     0,     0,     0,     0,     0,     0,   251,     0,
       0,    36,     0,     0,     0,     0,    74,     0,     0,     0,
       0,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,     0,    36,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   311,   312,     0,    74,     0,     0,     0,     0,
       0,     0,    75,    76,    77,     0,     0,     0,     0,     0,
       0,    78,   313,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,    74,
       0,     0,     0,     0,     0,     0,    75,    76,    77,     0,
     314,     0,     0,     0,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,    67,    68,    69,    70,    71,    72,    73,
       0,     0,     0,     0,   566,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,    74,     0,     0,     0,     0,     0,     0,    75,
      76,    77,     0,   567,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,     0,     0,     0,     0,
       0,     0,   107,   504,   108,   100,   101,   102,   109,   110,
     111,   112,   113,   114,   115,     0,     0,     0,   116,   117,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   118,   281,     0,   282,     0,     0,     0,   119,
       0,     0,     0,   120,   121,   122,     0,     0,     0,     0,
       0,   123,     0,     0,     0,     0,     0,   283,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   284,     0,     0,     0,     0,     0,
       0,   129,   130,     0,     0,   132,     0,   421,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,     0,
       0,     0,   495,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,     0,
       0,     0,   505,    67,    68,    69,    70,    71,    72,    73,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,    74,    89,    90,
      91,    92,     0,     0,    75,    76,    77,   612,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,     0,     0,     0,     0,     0,   614,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    74,     0,     0,     0,     0,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,    74,    89,    90,    91,    92,     0,     0,    75,    76,
      77,   646,     0,     0,     0,     0,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,     0,     0,     0,     0,     0,
     664,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    74,     0,     0,     0,
       0,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,    74,    89,    90,    91,    92,
       0,     0,    75,    76,    77,   665,     0,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,     0,   667,    67,    68,    69,    70,    71,
      72,    73,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      74,     0,     0,     0,     0,     0,     0,    75,    76,    77,
       0,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,    74,
      89,    90,    91,    92,     0,     0,    75,    76,    77,   679,
       0,     0,     0,     0,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,     0,     0,     0,     0,     0,   682,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    74,     0,     0,     0,     0,     0,
       0,    75,    76,    77,     0,     0,     0,     0,     0,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,    74,    89,    90,    91,    92,     0,     0,
      75,    76,    77,   683,     0,     0,     0,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,     0,
       0,     0,   712,    67,    68,    69,    70,    71,    72,    73,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,    74,    89,    90,
      91,    92,     0,     0,    75,    76,    77,   713,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,     0,     0,     0,     0,     0,   722,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    74,     0,     0,     0,     0,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,    74,    89,    90,    91,    92,     0,     0,    75,    76,
      77,   734,     0,     0,     0,     0,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,     0,     0,     0,     0,     0,
     754,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   107,     0,   108,
     100,   101,   102,   109,   110,   111,   112,   113,   114,   115,
       0,     0,     0,   116,   117,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   118,     0,     0,
       0,     0,     0,     0,   119,     0,    74,     0,   120,   121,
     122,     0,     0,    75,    76,    77,   123,     0,   124,     0,
     125,     0,    78,     0,    79,    80,    81,    82,     2,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
     126,     0,     0,     0,     0,   755,     0,   127,     0,   128,
       0,     0,     0,     0,     0,     0,   129,   130,   131,   107,
     132,   108,   100,   101,   102,   109,   110,   111,   112,   113,
     114,   115,     0,     0,     0,   116,   117,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   118,
     281,     0,   282,     0,     0,     0,   119,     0,     0,     0,
     120,   121,   122,     0,     0,     0,     0,     0,   123,     0,
       0,     0,     0,   107,   283,   108,   100,   101,   102,   109,
     110,   111,   112,   113,   114,   115,     0,     0,     0,   116,
     117,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     426,   284,     0,   118,   281,   549,   282,     0,   129,   130,
     119,     0,   132,     0,   120,   121,   122,     0,     0,     0,
       0,     0,   123,     0,     0,     0,     0,   107,   283,   108,
     100,   101,   102,   109,   110,   111,   112,   113,   114,   115,
       0,     0,     0,   116,   117,     0,     0,     0,    67,    68,
      69,    70,    71,    72,    73,   284,     0,   118,   281,   709,
     282,     0,   129,   130,   119,     0,   132,     0,   120,   121,
     122,     0,     0,     0,     0,     0,   123,     0,     0,     0,
       0,     0,   283,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,   284,
      75,    76,    77,     0,     0,     0,   129,   130,     0,    78,
     132,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,     0,
     107,   159,   108,   100,   101,   102,   109,   110,   111,   112,
     113,   114,   115,     0,     0,     0,   116,   117,     0,     0,
       0,    67,    68,    69,    70,    71,    72,    73,     0,     0,
     118,   281,     0,   282,     0,     0,     0,   119,     0,     0,
       0,   120,   121,   122,     0,     0,     0,     0,     0,   123,
       0,     0,     0,     0,     0,   283,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    74,     0,     0,     0,
       0,     0,   284,    75,    76,    77,     0,     0,     0,   129,
     130,     0,    78,   132,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
       0,    74,     0,     0,   315,     0,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,     0,     0,     0,     0,   564,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    74,     0,     0,     0,     0,
       0,     0,    75,    76,    77,     0,     0,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,    74,
       0,     0,     0,   597,     0,     0,    75,    76,    77,     0,
       0,     0,     0,     0,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,     0,     0,     0,     0,   598,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,    74,     0,     0,
       0,   599,     0,     0,    75,    76,    77,     0,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,     0,     0,     0,     0,   600,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    74,     0,     0,     0,     0,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,    74,     0,     0,     0,   602,
       0,     0,    75,    76,    77,     0,     0,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,   604,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    74,
       0,     0,     0,     0,     0,     0,    75,    76,    77,     0,
       0,     0,     0,     0,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,    74,     0,     0,     0,   642,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,     0,
       0,   756,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    74,     0,     0,
       0,     0,     0,     0,    75,    76,    77,     0,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,   311,   312,     0,    74,   757,     0,     0,     0,     0,
       0,    75,    76,    77,     0,     0,     0,     0,     0,     0,
      78,   313,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,     0,    78,
     317,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,    74,    89,    90,    91,    92,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    74,     0,     0,     0,     0,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92
};

static const yytype_int16 yycheck[] =
{
      48,   293,   381,   148,   149,   108,    43,    18,   419,   281,
       5,    47,     5,    18,    34,   399,   244,   219,   414,     5,
       5,    42,   418,   539,   123,     5,     5,     5,   127,   122,
     546,     5,     5,     3,   122,    21,     4,     5,    16,   127,
      51,    21,     4,     5,     5,   424,    51,     5,    21,     5,
      18,    19,    20,     5,     5,   100,    24,    25,    26,     5,
     108,   121,     5,     5,     5,   125,     5,     8,     9,    10,
     118,   124,   120,    45,   127,   123,     5,    45,   123,   123,
     122,   465,     0,    94,   132,   127,   130,   232,   233,   473,
       4,     5,   120,     5,     5,   106,    66,   125,    66,   127,
     121,   120,   123,   122,   124,    47,    48,   119,    47,    48,
     121,   122,    45,   124,    82,    27,   219,   220,     5,   635,
      82,    45,    90,    91,    92,   120,   119,   120,   231,    45,
     422,   120,   543,   101,   102,   103,   129,   148,   149,   107,
     119,   127,   153,   111,   129,   119,   542,   127,   153,   127,
     129,   118,   120,   127,   127,   300,   123,   302,   120,   304,
      45,   129,   134,   131,   132,   132,   127,   115,    82,   127,
     207,   219,   220,    84,   267,   127,   127,   270,   214,   272,
     121,   127,   121,   231,   127,   114,   234,   415,    45,    61,
     706,    45,    64,   241,   396,   397,   244,    45,    45,   210,
     211,   134,   586,   114,   252,    45,   120,   119,   120,   120,
     134,     4,     5,     5,   121,   120,   123,   362,   134,   735,
     125,   232,   127,   368,   120,   261,   637,     8,     9,   120,
      11,   127,   120,    83,   122,   751,   108,   125,     4,   127,
      21,    22,    23,   120,   127,   122,   118,   122,   123,   134,
     127,   123,    45,   356,   122,   123,   267,   360,   774,   270,
     132,   272,   129,   491,   114,   115,   116,   278,    11,    12,
      13,   122,   123,    16,   241,   686,   548,   134,   381,   121,
     134,   123,     5,     4,   671,   252,   134,   134,   675,   676,
     301,   124,   437,   304,   134,   331,   707,    18,    19,    20,
     122,   122,   338,    24,    25,    26,   127,    12,   356,   122,
     346,   539,   360,   406,   127,    12,    13,   410,   329,    16,
     413,   424,   671,    16,    45,   373,   675,   676,   364,   340,
     121,   342,   123,   381,   745,   383,   125,   342,   127,     5,
       5,   389,     8,     9,    10,   122,   123,   219,   220,   641,
     642,    30,    31,    32,   402,   734,    30,    31,    32,   231,
      16,    82,   234,   399,   123,   124,     5,   415,   127,   241,
      45,   419,   244,   122,   123,   754,   424,   414,   122,   123,
     252,   418,   120,   120,   122,   122,     5,   122,   533,   124,
     535,   536,   537,   538,     6,    30,    31,    32,    33,    34,
      57,   121,    59,   123,    83,   121,   373,   123,   120,    83,
     122,   121,   121,   123,   123,   121,   383,   123,   429,   121,
       5,   123,   389,   121,   435,   123,   121,     5,   123,   465,
     124,   110,   111,   124,   113,   114,   115,   116,   122,   113,
     114,   115,   116,   491,   121,   121,   123,   123,    83,   122,
     123,    28,   419,    30,    31,    32,    33,    34,   121,     5,
     123,   753,   121,   121,   123,   123,   121,    16,   123,   104,
     124,   106,   107,   108,   109,   110,   111,   622,   113,   114,
     115,   116,   627,   121,   356,   123,     5,   121,   360,   123,
     121,   539,   123,   541,    57,   543,    59,     5,   546,   791,
      57,   373,    59,   123,   124,   542,    83,   124,   121,   381,
     123,   383,   123,    90,    91,    92,   121,   389,   123,   122,
     123,   122,   533,   120,   535,   102,   103,   104,     5,   106,
     107,   108,   109,   110,   111,     5,   113,   114,   115,   116,
     122,   123,     5,   415,   120,   690,   120,   419,   596,   597,
     122,   123,   424,   120,   602,   125,   604,   122,   123,   704,
     705,   122,   123,   123,   124,   599,   600,    28,   120,    30,
      31,    32,    33,    34,   541,   120,   543,   120,   122,   546,
     120,     5,   124,   124,   632,   122,    79,   635,    67,    68,
      69,    70,    71,    72,    73,    74,   127,   120,   120,     5,
       5,   122,     5,   748,   124,   120,     5,   123,     5,     5,
     124,   124,   623,   624,   625,   124,   627,   628,   122,   491,
     122,   122,    83,   122,   122,     5,     5,   122,   122,   596,
     597,   734,   122,   122,     5,   602,   122,   604,   686,   122,
       5,   122,   103,   104,   120,   106,   107,   108,   109,   110,
     111,   754,   113,   114,   115,   116,   124,   122,   706,   707,
     122,    11,   122,   122,    59,   632,   122,   539,   635,   541,
     122,   543,   122,   120,   546,   723,   724,   122,   122,   125,
     691,   729,   693,   120,   125,   121,   734,   735,   122,   122,
     122,   122,   122,   704,   122,   122,   122,   745,    57,   122,
     122,    59,   122,   751,   122,    39,   754,   100,    52,   122,
     122,    28,   122,    30,    31,    32,    33,    34,     5,   686,
     122,   122,    57,    39,   596,   597,   774,    52,   122,    52,
     602,    52,   604,     4,     5,    57,   784,   748,   749,   706,
     707,   122,     5,    57,   122,   122,   122,    18,    19,    20,
      59,    57,   122,    24,    25,    26,   723,   724,    57,   122,
     632,    59,   729,   635,    57,     4,    83,   207,   735,   402,
     134,   478,   408,   574,    45,   196,   581,   149,   745,   118,
     610,   360,    -1,    -1,   751,   457,   161,   104,    -1,   106,
     107,   108,   109,   110,   111,    66,   113,   114,   115,   116,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   774,    -1,    -1,
      -1,    82,    -1,    -1,   686,    -1,    -1,   784,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     101,   102,   103,    -1,   706,   707,    -1,    -1,    -1,    -1,
     111,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   120,
     121,   723,   724,    -1,   125,    -1,    -1,   729,   129,    -1,
     131,   132,   734,   735,    -1,    10,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   745,    -1,    -1,    -1,    -1,    -1,   751,
      -1,    -1,   754,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   774,    -1,    49,    -1,    -1,    52,    -1,    -1,
      -1,    -1,   784,    -1,    -1,    28,    29,    30,    31,    32,
      33,    34,    67,    68,    69,    70,    71,    72,    73,    74,
      75,    76,    77,    78,    79,    80,    81,    82,    83,    84,
      85,    86,    87,    88,    89,    90,    91,    92,    -1,    -1,
      -1,     4,     5,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    18,    19,    20,    -1,    -1,
      83,    24,    25,    26,    -1,    -1,    -1,    90,    91,    92,
      -1,    -1,    -1,    -1,    -1,    -1,    99,    -1,   101,   102,
     103,   104,    45,   106,   107,   108,   109,   110,   111,    -1,
     113,   114,   115,   116,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    66,    -1,   128,   161,    -1,    -1,    -1,
       4,     5,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    82,
      -1,    -1,    -1,    -1,    18,    19,    20,    90,    91,    92,
      24,    25,    26,    -1,    -1,   190,    -1,   192,   101,   102,
     103,    -1,    -1,    -1,    -1,    -1,    40,    41,   111,    -1,
      -1,    45,    -1,    -1,    -1,    -1,    -1,   120,   121,    -1,
      -1,    -1,   125,    -1,    -1,    -1,   129,    -1,   131,   132,
      -1,    -1,    66,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   236,    -1,    -1,    -1,    -1,    -1,    -1,    82,    -1,
      -1,   246,   247,    -1,    -1,   250,    90,    91,    92,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   101,   102,   103,
      30,    31,    32,    33,    34,    -1,    -1,   111,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   120,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   129,    -1,   131,   132,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   307,   308,    -1,    -1,   311,   312,   313,     4,
       5,    -1,   317,    83,   319,    -1,    -1,   322,    -1,    -1,
      -1,    -1,    -1,    18,    19,    20,    -1,    -1,    -1,    24,
      25,    26,    -1,    -1,    -1,    -1,    -1,    -1,   108,   109,
     110,   111,    -1,   113,   114,   115,   116,    -1,    -1,    -1,
      45,    -1,    -1,    -1,    -1,    -1,   361,    52,    53,    -1,
      -1,    -1,    -1,    -1,     4,     5,    -1,    -1,    -1,   374,
      -1,    66,   377,   378,   379,    -1,    -1,   382,    18,    19,
      20,    -1,   387,    -1,    24,    25,    26,    82,   393,    -1,
      -1,   396,   397,    -1,    -1,    90,    91,    92,   403,   404,
      -1,    -1,    -1,    -1,    -1,    45,   101,   102,   103,    -1,
      -1,    -1,    52,    53,    -1,    -1,   111,    -1,   423,    -1,
      -1,    -1,    -1,    -1,    -1,   120,    66,    -1,    -1,   434,
      -1,    -1,    -1,    -1,   129,    -1,   131,   132,    -1,    -1,
     445,    -1,    82,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   101,   102,   103,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   111,    -1,    -1,    -1,   480,   481,    -1,    -1,    -1,
     120,    -1,   487,    -1,    -1,    -1,    -1,    -1,    -1,   129,
      -1,   131,   132,     4,     5,    -1,    -1,    -1,    -1,   504,
      -1,    -1,    -1,    -1,    -1,   510,   511,    18,    19,    20,
     515,    -1,   517,    24,    25,    26,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    45,    -1,    -1,    -1,    -1,    -1,
      -1,    52,    53,    -1,     4,     5,    -1,    -1,    -1,    -1,
      -1,   556,    -1,    -1,   559,    66,    -1,    -1,    18,    19,
      20,    -1,    -1,    -1,    24,    25,    26,    -1,    -1,    -1,
      -1,    82,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    90,
      91,    92,    -1,    -1,   589,    45,    -1,    -1,    -1,    -1,
     101,   102,   103,    -1,    -1,    -1,   601,    -1,    -1,    -1,
     111,    -1,    -1,    -1,    -1,   610,    66,    -1,    -1,   120,
      -1,    -1,    -1,     4,     5,    -1,    -1,    -1,   129,    -1,
     131,   132,    82,    -1,    -1,    -1,    -1,    18,    19,    20,
      90,    91,    92,    24,    25,    26,    -1,    -1,   643,    -1,
      -1,   101,   102,   103,   649,    -1,   651,    -1,    -1,    -1,
      -1,   111,   657,    -1,    45,    -1,    -1,    -1,    -1,    -1,
     120,   121,    -1,    -1,     4,     5,    -1,    -1,    -1,   129,
      -1,   131,   132,    -1,    -1,    66,    -1,    -1,    18,    19,
      20,    -1,    -1,    -1,    24,    25,    26,    -1,    -1,    -1,
      -1,    82,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    90,
      91,    92,    -1,    -1,    -1,    45,    -1,    -1,    -1,    -1,
     101,   102,   103,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     111,    -1,    -1,    -1,    -1,    -1,    66,    -1,   119,   120,
      -1,    -1,    -1,     4,     5,    -1,    -1,    -1,   129,    -1,
     131,   132,    82,    -1,    -1,    -1,    -1,    18,    19,    20,
      90,    91,    92,    24,    25,    26,    -1,    -1,    -1,    -1,
      -1,   101,   102,   103,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   111,    -1,    -1,    45,    -1,    -1,    -1,    -1,    -1,
     120,    -1,    53,    -1,    -1,   125,     4,     5,    -1,   129,
      -1,   131,   132,    -1,    -1,    66,    -1,    -1,    -1,    -1,
      18,    19,    20,    -1,    -1,    -1,    24,    25,    26,    -1,
      -1,    82,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    45,    -1,    -1,
     101,   102,   103,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     111,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    66,   120,
      -1,    -1,    -1,    -1,    -1,     4,     5,    -1,   129,    -1,
     131,   132,    -1,    -1,    82,    -1,    -1,    -1,    -1,    18,
      19,    20,    90,    91,    92,    24,    25,    26,    -1,    -1,
      -1,    -1,    -1,   101,   102,   103,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   111,    -1,    -1,    45,    -1,    -1,    -1,
      -1,    -1,   120,   121,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   129,    -1,   131,   132,    -1,    -1,    66,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    82,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   101,   102,   103,    -1,    -1,    -1,    -1,    -1,
      -1,     5,   111,     7,    -1,    -1,    -1,    11,    -1,    -1,
      -1,   120,    -1,    -1,    -1,    -1,    -1,    21,    -1,    -1,
     129,    -1,   131,   132,    28,    29,    30,    31,    32,    33,
      34,    -1,    36,    -1,    38,    -1,    -1,    -1,    -1,    43,
      44,    -1,    -1,    -1,    -1,    49,    50,    51,    -1,    -1,
      -1,    55,    -1,    -1,    -1,    -1,    60,    61,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    75,    -1,    77,    78,    -1,    -1,    -1,    -1,    83,
      -1,    -1,    -1,    -1,    88,    89,    90,    91,    92,    93,
      -1,    -1,    -1,    97,    -1,    99,    -1,   101,   102,   103,
     104,    -1,   106,   107,   108,   109,   110,   111,    -1,   113,
     114,   115,   116,    -1,    -1,   119,    -1,     5,   122,     7,
       8,     9,   126,    11,    -1,   129,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    21,    22,    23,    -1,    -1,     5,    -1,
       7,    -1,    -1,    -1,    11,    -1,    -1,    -1,    36,    -1,
      38,    -1,    -1,    -1,    21,    43,    44,    -1,    -1,    -1,
      -1,    49,    50,    51,    -1,    -1,    -1,    55,    -1,    36,
      37,    38,    60,    61,    -1,    -1,    43,    44,    -1,    -1,
      -1,    -1,    49,    50,    51,    -1,    -1,    75,    55,    77,
      78,    -1,    -1,    60,    61,    -1,    -1,    -1,    -1,    -1,
      88,    89,    -1,    -1,    -1,    93,    -1,    -1,    75,    97,
      77,    78,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    88,    89,    -1,    -1,    -1,    93,    -1,    -1,    -1,
      97,   119,    -1,   100,     5,    -1,     7,    -1,   126,    -1,
      11,   129,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      21,    -1,   119,    -1,    -1,     5,    -1,     7,    -1,   126,
      -1,    11,   129,    -1,    -1,    36,    -1,    38,    -1,    -1,
      -1,    21,    43,    44,    -1,    -1,    -1,    -1,    49,    50,
      51,    -1,    -1,    -1,    55,    -1,    36,    37,    38,    60,
      61,    -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,
      50,    51,    -1,    -1,    75,    55,    77,    78,    -1,    -1,
      60,    61,    -1,    -1,    -1,    -1,    -1,    88,    89,    -1,
      -1,    -1,    93,    -1,    -1,    75,    97,    77,    78,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    88,    89,
      -1,    -1,    -1,    93,     5,    -1,     7,    97,   119,    -1,
      11,   122,    -1,    -1,    -1,   126,    -1,    -1,   129,    -1,
      21,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   119,
      -1,    -1,    -1,    -1,    -1,    36,   126,    38,    -1,   129,
      -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,    50,
      51,    -1,    -1,    -1,    55,    -1,    -1,    -1,    -1,    60,
      61,    -1,    -1,    -1,     5,    -1,     7,    -1,    -1,    -1,
      11,    -1,    -1,    -1,    75,    76,    77,    78,    -1,    -1,
      21,    -1,    -1,    -1,    -1,    -1,    -1,    88,    89,    -1,
      -1,    -1,    93,    -1,    -1,    36,    97,    38,    -1,    -1,
      -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,    50,
      51,    -1,    -1,    -1,    55,    -1,    57,    -1,   119,    60,
      61,    -1,    -1,    -1,    -1,   126,    -1,     5,   129,     7,
      -1,    -1,    -1,    11,    75,    -1,    77,    78,    -1,    -1,
      -1,    -1,    -1,    21,    -1,    -1,    -1,    88,    89,    -1,
      -1,    -1,    93,    -1,    -1,    -1,    97,    -1,    36,    37,
      38,    -1,    -1,    -1,    -1,    43,    44,    -1,    -1,    -1,
      -1,    49,    50,    51,    -1,    -1,    -1,    55,   119,    -1,
      -1,    -1,    60,    61,    -1,   126,    -1,     5,   129,     7,
      -1,    -1,    -1,    11,    -1,    -1,    -1,    75,    -1,    77,
      78,    -1,    -1,    21,    -1,    -1,    -1,    -1,    -1,    -1,
      88,    89,    -1,    -1,    -1,    93,    -1,    -1,    36,    97,
      38,    -1,    -1,    -1,    -1,    43,    44,    -1,    -1,    -1,
      -1,    49,    50,    51,    -1,    -1,    -1,    55,    -1,    57,
      -1,   119,    60,    61,    -1,    -1,    -1,     5,   126,     7,
      -1,   129,    -1,    11,    -1,    -1,    -1,    75,    -1,    77,
      78,    -1,    -1,    21,    -1,    -1,    -1,    -1,    -1,    -1,
      88,    89,    -1,    -1,    -1,    93,    -1,    -1,    36,    97,
      38,    -1,    -1,    -1,    -1,    43,    44,    -1,    -1,    -1,
      -1,    49,    50,    51,    -1,    -1,    -1,    55,    -1,    -1,
      -1,   119,    60,    61,    -1,    -1,    -1,     5,   126,     7,
      -1,   129,    -1,    11,    -1,    -1,    -1,    75,    -1,    77,
      78,    -1,    -1,    21,    -1,    -1,    -1,    -1,    -1,    -1,
      88,    89,    -1,    -1,    -1,    93,    -1,    -1,    36,    97,
      38,    -1,    -1,    -1,    -1,    43,    44,    -1,    -1,    -1,
      -1,    49,    50,    51,    -1,    -1,    -1,    55,    -1,    -1,
      -1,   119,    60,    61,   122,    -1,    -1,     5,   126,     7,
      -1,   129,    -1,    11,    -1,    -1,    -1,    75,    -1,    77,
      78,    -1,    -1,    21,    -1,    -1,    -1,    -1,    -1,    -1,
      88,    89,    -1,    -1,    -1,    93,    -1,    -1,    36,    97,
      38,    -1,    -1,    -1,    -1,    43,    44,    -1,    -1,    -1,
      -1,    49,    50,    51,    -1,    -1,    -1,    55,    -1,    -1,
      -1,   119,    60,    61,   122,    -1,    -1,    -1,   126,    -1,
      -1,   129,    -1,    -1,    -1,    -1,    -1,    75,    -1,    77,
      78,    28,    29,    30,    31,    32,    33,    34,    -1,    -1,
      88,    89,    -1,    -1,    -1,    93,    -1,    -1,    -1,    97,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   119,    -1,    -1,    -1,    -1,    -1,    -1,   126,    -1,
      -1,   129,    -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    -1,    99,    -1,   101,   102,   103,   104,    -1,   106,
     107,   108,   109,   110,   111,    -1,   113,   114,   115,   116,
      28,    29,    30,    31,    32,    33,    34,    -1,    -1,    -1,
      -1,    -1,   129,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    80,    81,    -1,    83,    -1,    -1,    -1,    -1,
      -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,
      -1,    99,   100,   101,   102,   103,   104,    -1,   106,   107,
     108,   109,   110,   111,    -1,   113,   114,   115,   116,    83,
      -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,
     128,    -1,    -1,    -1,    -1,    99,    -1,   101,   102,   103,
     104,    -1,   106,   107,   108,   109,   110,   111,    -1,   113,
     114,   115,   116,    28,    29,    30,    31,    32,    33,    34,
      -1,    -1,    -1,    -1,   128,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,    29,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,
      -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,
      -1,    -1,    -1,    -1,    99,    -1,   101,   102,   103,   104,
      -1,   106,   107,   108,   109,   110,   111,    -1,   113,   114,
     115,   116,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,
      91,    92,    -1,   128,    -1,    -1,    -1,    -1,    99,    -1,
     101,   102,   103,   104,    -1,   106,   107,   108,   109,   110,
     111,    -1,   113,   114,   115,   116,    -1,    -1,    -1,    -1,
      -1,    -1,     5,   124,     7,     8,     9,    10,    11,    12,
      13,    14,    15,    16,    17,    -1,    -1,    -1,    21,    22,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    35,    36,    -1,    38,    -1,    -1,    -1,    42,
      -1,    -1,    -1,    46,    47,    48,    -1,    -1,    -1,    -1,
      -1,    54,    -1,    -1,    -1,    -1,    -1,    60,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    87,    -1,    -1,    -1,    -1,    -1,
      -1,    94,    95,    -1,    -1,    98,    -1,   100,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    99,
      -1,   101,   102,   103,   104,    -1,   106,   107,   108,   109,
     110,   111,    -1,   113,   114,   115,   116,    -1,    -1,    -1,
      -1,    -1,   122,    83,    -1,    -1,    -1,    -1,    -1,    -1,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    99,
      -1,   101,   102,   103,   104,    -1,   106,   107,   108,   109,
     110,   111,    -1,   113,   114,   115,   116,    -1,    -1,    -1,
      -1,    -1,   122,    28,    29,    30,    31,    32,    33,    34,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    28,    29,    30,    31,    32,    33,    34,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,
      -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,
      -1,    -1,    -1,    -1,    99,    -1,   101,   102,   103,   104,
      -1,   106,   107,   108,   109,   110,   111,    83,   113,   114,
     115,   116,    -1,    -1,    90,    91,    92,   122,    -1,    -1,
      -1,    -1,    -1,    99,    -1,   101,   102,   103,   104,    -1,
     106,   107,   108,   109,   110,   111,    -1,   113,   114,   115,
     116,    -1,    -1,    -1,    -1,    -1,   122,    28,    29,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    28,    29,    30,    31,
      32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    99,    -1,
     101,   102,   103,   104,    -1,   106,   107,   108,   109,   110,
     111,    83,   113,   114,   115,   116,    -1,    -1,    90,    91,
      92,   122,    -1,    -1,    -1,    -1,    -1,    99,    -1,   101,
     102,   103,   104,    -1,   106,   107,   108,   109,   110,   111,
      -1,   113,   114,   115,   116,    -1,    -1,    -1,    -1,    -1,
     122,    28,    29,    30,    31,    32,    33,    34,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      28,    29,    30,    31,    32,    33,    34,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    -1,    99,    -1,   101,   102,   103,   104,    -1,   106,
     107,   108,   109,   110,   111,    83,   113,   114,   115,   116,
      -1,    -1,    90,    91,    92,   122,    -1,    -1,    -1,    -1,
      -1,    99,    -1,   101,   102,   103,   104,    -1,   106,   107,
     108,   109,   110,   111,    -1,   113,   114,   115,   116,    -1,
      -1,    -1,    -1,    -1,   122,    28,    29,    30,    31,    32,
      33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,
      -1,    -1,    -1,    -1,    -1,    -1,    99,    -1,   101,   102,
     103,   104,    -1,   106,   107,   108,   109,   110,   111,    83,
     113,   114,   115,   116,    -1,    -1,    90,    91,    92,   122,
      -1,    -1,    -1,    -1,    -1,    99,    -1,   101,   102,   103,
     104,    -1,   106,   107,   108,   109,   110,   111,    -1,   113,
     114,   115,   116,    -1,    -1,    -1,    -1,    -1,   122,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,
      -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,
      99,    -1,   101,   102,   103,   104,    -1,   106,   107,   108,
     109,   110,   111,    83,   113,   114,   115,   116,    -1,    -1,
      90,    91,    92,   122,    -1,    -1,    -1,    -1,    -1,    99,
      -1,   101,   102,   103,   104,    -1,   106,   107,   108,   109,
     110,   111,    -1,   113,   114,   115,   116,    -1,    -1,    -1,
      -1,    -1,   122,    28,    29,    30,    31,    32,    33,    34,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    28,    29,    30,    31,    32,    33,    34,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,
      -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,
      -1,    -1,    -1,    -1,    99,    -1,   101,   102,   103,   104,
      -1,   106,   107,   108,   109,   110,   111,    83,   113,   114,
     115,   116,    -1,    -1,    90,    91,    92,   122,    -1,    -1,
      -1,    -1,    -1,    99,    -1,   101,   102,   103,   104,    -1,
     106,   107,   108,   109,   110,   111,    -1,   113,   114,   115,
     116,    -1,    -1,    -1,    -1,    -1,   122,    28,    29,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    28,    29,    30,    31,
      32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    99,    -1,
     101,   102,   103,   104,    -1,   106,   107,   108,   109,   110,
     111,    83,   113,   114,   115,   116,    -1,    -1,    90,    91,
      92,   122,    -1,    -1,    -1,    -1,    -1,    99,    -1,   101,
     102,   103,   104,    -1,   106,   107,   108,   109,   110,   111,
      -1,   113,   114,   115,   116,    -1,    -1,    -1,    -1,    -1,
     122,    28,    29,    30,    31,    32,    33,    34,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,     5,    -1,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    16,    17,
      -1,    -1,    -1,    21,    22,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    35,    -1,    -1,
      -1,    -1,    -1,    -1,    42,    -1,    83,    -1,    46,    47,
      48,    -1,    -1,    90,    91,    92,    54,    -1,    56,    -1,
      58,    -1,    99,    -1,   101,   102,   103,   104,    66,   106,
     107,   108,   109,   110,   111,    -1,   113,   114,   115,   116,
      78,    -1,    -1,    -1,    -1,   122,    -1,    85,    -1,    87,
      -1,    -1,    -1,    -1,    -1,    -1,    94,    95,    96,     5,
      98,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      16,    17,    -1,    -1,    -1,    21,    22,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    35,
      36,    -1,    38,    -1,    -1,    -1,    42,    -1,    -1,    -1,
      46,    47,    48,    -1,    -1,    -1,    -1,    -1,    54,    -1,
      -1,    -1,    -1,     5,    60,     7,     8,     9,    10,    11,
      12,    13,    14,    15,    16,    17,    -1,    -1,    -1,    21,
      22,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      86,    87,    -1,    35,    36,    37,    38,    -1,    94,    95,
      42,    -1,    98,    -1,    46,    47,    48,    -1,    -1,    -1,
      -1,    -1,    54,    -1,    -1,    -1,    -1,     5,    60,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    16,    17,
      -1,    -1,    -1,    21,    22,    -1,    -1,    -1,    28,    29,
      30,    31,    32,    33,    34,    87,    -1,    35,    36,    37,
      38,    -1,    94,    95,    42,    -1,    98,    -1,    46,    47,
      48,    -1,    -1,    -1,    -1,    -1,    54,    -1,    -1,    -1,
      -1,    -1,    60,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    87,
      90,    91,    92,    -1,    -1,    -1,    94,    95,    -1,    99,
      98,   101,   102,   103,   104,    -1,   106,   107,   108,   109,
     110,   111,    -1,   113,   114,   115,   116,    -1,    -1,    -1,
       5,   121,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    -1,    -1,    -1,    21,    22,    -1,    -1,
      -1,    28,    29,    30,    31,    32,    33,    34,    -1,    -1,
      35,    36,    -1,    38,    -1,    -1,    -1,    42,    -1,    -1,
      -1,    46,    47,    48,    -1,    -1,    -1,    -1,    -1,    54,
      -1,    -1,    -1,    -1,    -1,    60,    28,    29,    30,    31,
      32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,
      -1,    -1,    87,    90,    91,    92,    -1,    -1,    -1,    94,
      95,    -1,    99,    98,   101,   102,   103,   104,    -1,   106,
     107,   108,   109,   110,   111,    -1,   113,   114,   115,   116,
      -1,    83,    -1,    -1,   121,    -1,    -1,    -1,    90,    91,
      92,    -1,    -1,    -1,    -1,    -1,    -1,    99,    -1,   101,
     102,   103,   104,    -1,   106,   107,   108,   109,   110,   111,
      -1,   113,   114,   115,   116,    -1,    -1,    -1,    -1,   121,
      28,    29,    30,    31,    32,    33,    34,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,
      -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,
      -1,    99,    -1,   101,   102,   103,   104,    -1,   106,   107,
     108,   109,   110,   111,    -1,   113,   114,   115,   116,    83,
      -1,    -1,    -1,   121,    -1,    -1,    90,    91,    92,    -1,
      -1,    -1,    -1,    -1,    -1,    99,    -1,   101,   102,   103,
     104,    -1,   106,   107,   108,   109,   110,   111,    -1,   113,
     114,   115,   116,    -1,    -1,    -1,    -1,   121,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    28,    29,    30,    31,    32,    33,    34,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    99,
      -1,   101,   102,   103,   104,    -1,   106,   107,   108,   109,
     110,   111,    -1,   113,   114,   115,   116,    83,    -1,    -1,
      -1,   121,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,
      -1,    -1,    -1,    99,    -1,   101,   102,   103,   104,    -1,
     106,   107,   108,   109,   110,   111,    -1,   113,   114,   115,
     116,    -1,    -1,    -1,    -1,   121,    28,    29,    30,    31,
      32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      28,    29,    30,    31,    32,    33,    34,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,
      92,    -1,    -1,    -1,    -1,    -1,    -1,    99,    -1,   101,
     102,   103,   104,    -1,   106,   107,   108,   109,   110,   111,
      -1,   113,   114,   115,   116,    83,    -1,    -1,    -1,   121,
      -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,
      -1,    99,    -1,   101,   102,   103,   104,    -1,   106,   107,
     108,   109,   110,   111,    -1,   113,   114,   115,   116,    -1,
      -1,    -1,    -1,   121,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,
      -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,
      -1,    -1,    -1,    -1,    -1,    99,    -1,   101,   102,   103,
     104,    -1,   106,   107,   108,   109,   110,   111,    -1,   113,
     114,   115,   116,    83,    -1,    -1,    -1,   121,    -1,    -1,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    99,
      -1,   101,   102,   103,   104,    -1,   106,   107,   108,   109,
     110,   111,    -1,   113,   114,   115,   116,    -1,    -1,    -1,
      -1,   121,    28,    29,    30,    31,    32,    33,    34,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,
      -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,
      -1,    -1,    -1,    99,    -1,   101,   102,   103,   104,    -1,
     106,   107,   108,   109,   110,   111,    -1,   113,   114,   115,
     116,    80,    81,    -1,    83,   121,    -1,    -1,    -1,    -1,
      -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,
      99,   100,   101,   102,   103,   104,    -1,   106,   107,   108,
     109,   110,   111,    -1,   113,   114,   115,   116,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,    29,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    99,
     100,   101,   102,   103,   104,    -1,   106,   107,   108,   109,
     110,   111,    83,   113,   114,   115,   116,    -1,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    99,    -1,
     101,   102,   103,   104,    -1,   106,   107,   108,   109,   110,
     111,    -1,   113,   114,   115,   116,    28,    29,    30,    31,
      32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,
      92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     102,   103,   104,    -1,   106,   107,   108,   109,   110,   111,
      -1,   113,   114,   115,   116
};

/* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
   symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,     3,    66,   134,   135,   136,   137,   144,     5,     4,
       5,    45,     0,   136,   119,   138,     5,     4,     5,    18,
      19,    20,    24,    25,    26,    45,    66,    82,    90,    91,
      92,   101,   102,   103,   111,   120,   129,   131,   132,   198,
     201,   203,   120,   120,   122,   139,   115,   120,   125,   127,
     194,   195,   120,   203,   203,   203,   203,   203,   203,   203,
     203,   107,   199,   200,   203,   203,   203,    28,    29,    30,
      31,    32,    33,    34,    83,    90,    91,    92,    99,   101,
     102,   103,   104,   106,   107,   108,   109,   110,   111,   113,
     114,   115,   116,     5,    47,    48,   121,   162,   163,     5,
       8,     9,    10,   121,   140,   141,   196,     5,     7,    11,
      12,    13,    14,    15,    16,    17,    21,    22,    35,    42,
      46,    47,    48,    54,    56,    58,    78,    85,    87,    94,
      95,    96,    98,   142,   143,   144,   145,   146,   147,   151,
     152,   155,   156,   157,   164,   171,   172,   181,   196,   197,
       4,   190,   203,     5,   201,   203,   194,   195,   203,   121,
     198,   123,   130,   198,   203,   203,   203,   203,   203,   203,
     203,   203,   203,   203,   203,   203,   203,   203,   203,   203,
     203,   203,   203,   203,   203,   203,   203,   203,   203,   203,
     124,     5,   127,   194,     5,   121,   123,    12,    13,    16,
      11,    12,    13,    16,    12,   122,   121,   123,     5,    21,
     194,     5,    27,   119,   120,   170,     5,   119,   120,   148,
     167,   185,   186,   192,   198,   201,    16,    16,     5,   193,
       5,     7,    11,    21,    36,    38,    43,    44,    49,    50,
      51,    55,    60,    61,    75,    77,    88,    89,    93,    97,
     119,   126,   176,   180,   181,   182,   183,   184,   192,   201,
       5,   120,     5,   158,   159,   201,     5,    16,   160,   161,
     194,   160,   194,   176,   180,     5,    21,   150,   194,     5,
      45,    36,    38,    60,    87,   145,   146,   147,   155,   156,
     157,   164,   171,   173,   174,   175,   180,     6,   142,   193,
     194,     5,   170,   193,   194,     5,   121,   123,   120,   194,
     195,    80,    81,   100,   128,   121,   200,   100,   203,   124,
     203,     5,   124,   163,    16,   122,   141,   124,     5,     5,
     194,   120,   122,   194,     5,     4,     5,    82,   120,   190,
       5,   194,   195,     4,     5,    82,   120,    67,    68,    69,
      70,    71,    72,    73,    74,   149,   167,   192,   192,   122,
     123,   124,   123,   122,   120,   122,   192,   193,   194,   193,
      37,   100,   180,   191,   120,   203,     5,   120,   120,   120,
     180,   120,   120,   191,     5,   203,   203,   120,     5,   203,
       5,    84,   114,   120,   122,   180,    34,   124,   122,   120,
     190,   122,   123,   124,   124,   160,   194,   122,   123,   160,
     194,   122,   160,   194,   120,   122,     5,   194,   120,   122,
      79,   100,   173,   120,   120,     5,    86,   174,   122,   193,
     194,     5,   193,   122,   124,     5,   193,   194,   203,   203,
     203,   203,   203,   203,   203,   124,   203,     4,    18,    19,
      20,    24,    25,    26,    45,    82,   202,   124,   194,     5,
     121,   125,   165,   166,   190,   120,     5,   121,   125,   168,
     169,   190,   121,   120,   194,   194,   195,   190,   123,   192,
     124,   124,   186,   203,   193,   121,   190,   124,   122,   193,
     122,     5,    37,   180,   203,   122,   122,   203,   203,   203,
     185,   203,    76,   122,   124,   122,   203,   122,   122,   180,
      40,    41,   178,   179,   203,   167,   203,   167,   203,   165,
     190,   121,   158,   203,   203,   122,   160,   161,   122,   160,
     122,   160,   140,     8,     9,    11,    21,    22,    23,   153,
     154,   191,   120,   122,     5,   140,   153,   180,     5,    37,
     203,   185,   122,   122,   194,   122,   124,   122,   203,   124,
     194,   122,     5,   193,   121,   128,   128,   128,   203,   202,
     122,     5,   114,   121,   123,   121,   165,   190,   122,     5,
     121,   123,   121,   122,   121,   165,   120,   121,   149,   124,
     203,   203,   122,   121,   203,   122,   191,   121,   121,   121,
     121,   122,   121,   203,   121,   203,   203,    42,   121,   123,
     177,   203,   122,   203,   122,   121,   121,   122,   122,   122,
     122,   121,    21,   193,   194,    11,   193,   194,   193,   193,
     193,   154,   191,    57,   140,   153,   180,   122,   121,   180,
      59,   173,   121,   122,   122,   203,   122,   203,   122,   124,
     122,   120,   122,   166,   122,   121,   121,   120,   169,   122,
     121,   165,   121,   203,   122,   122,   122,   122,    37,   180,
      53,   187,   188,   189,   190,   187,   187,   203,   180,   122,
     180,   179,   122,   122,   122,   122,   122,   193,   122,   194,
     194,   194,   122,     5,   193,   194,   122,   194,   122,   122,
      57,   121,   180,    57,    11,    21,   153,   122,    59,    37,
     174,   203,   122,   122,   203,   121,   203,   122,   122,   203,
     122,   121,   122,    39,   100,    52,   188,   189,    52,   100,
      52,   189,    52,   189,   122,   153,   180,   122,   122,   193,
     194,   194,   122,     5,   122,   122,    57,   193,   194,   193,
     180,   153,   180,    39,   122,   122,   121,   121,   122,   180,
     122,   180,    52,   122,   180,    52,    52,   185,   180,    57,
     122,     5,   122,   122,   153,   180,   122,   193,   122,    57,
     180,    59,   174,   185,   121,    57,   122,   180,    57,   122,
      59,   121,   180,    57,   174
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
#line 3149 "y.tab.c"
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


#line 378 "yaccs/verilog.yacc"


