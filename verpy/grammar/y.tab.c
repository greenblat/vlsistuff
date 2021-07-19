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
     arith_shift_right = 353,
     SignedLeft = 354,
     shift_right = 355,
     shift_left = 356,
     Veryequal = 357,
     noteqeq = 358,
     StarStar = 359,
     UNARY_PREC = 360
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
#define arith_shift_right 353
#define SignedLeft 354
#define shift_right 355
#define shift_left 356
#define Veryequal 357
#define noteqeq 358
#define StarStar 359
#define UNARY_PREC 360




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
#line 317 "y.tab.c"

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
#define YYLAST   5213

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  132
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  71
/* YYNRULES -- Number of rules.  */
#define YYNRULES  354
/* YYNRULES -- Number of states.  */
#define YYNSTATES  789

/* YYTRANSLATE(YYLEX) -- Bison symbol number corresponding to YYLEX.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   360

#define YYTRANSLATE(YYX)						\
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[YYLEX] -- Bison symbol number corresponding to YYLEX.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   130,     2,   118,     2,   115,   102,     2,
     119,   120,   113,   109,   122,   110,   124,   114,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,    99,   121,
     107,   123,   108,    98,   125,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,   126,     2,   127,   101,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   128,   100,   129,   131,     2,     2,     2,
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
      95,    96,    97,   103,   104,   105,   106,   111,   112,   116,
     117
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
     973,   975,   978,   980,   986,   990,   994,  1004,  1010,  1016,
    1020,  1022,  1026,  1029,  1031,  1035,  1039,  1043,  1047,  1051,
    1053,  1056,  1058,  1060,  1063,  1067,  1071,  1074,  1076,  1078,
    1082,  1084,  1090,  1096,  1102,  1106,  1108,  1110,  1112,  1115,
    1118,  1121,  1124,  1127,  1130,  1134,  1137,  1140,  1142,  1144,
    1146,  1148,  1150,  1152,  1155,  1158,  1160,  1162,  1164,  1166,
    1168,  1172,  1176,  1178,  1181,  1183,  1186,  1190,  1194,  1199,
    1204,  1211,  1213,  1215,  1217,  1219,  1221,  1223,  1225,  1227,
    1229,  1231,  1233,  1235,  1237,  1239,  1241,  1246,  1248,  1250,
    1252,  1254,  1256,  1258,  1261,  1265,  1269,  1272,  1278,  1282,
    1286,  1290,  1294,  1298,  1302,  1306,  1310,  1314,  1318,  1322,
    1326,  1330,  1334,  1338,  1342,  1346,  1350,  1354,  1358,  1362,
    1366,  1370,  1374,  1378,  1383,  1387,  1389,  1392,  1395,  1398,
    1401,  1404,  1407,  1410,  1413
};

/* YYRHS -- A `-1'-separated list of the rules' RHS.  */
static const yytype_int16 yyrhs[] =
{
     133,     0,    -1,   134,    -1,   134,   135,    -1,   135,    -1,
     136,    -1,   143,    -1,     3,     5,   137,   138,   141,     6,
      -1,   118,   119,   161,   120,    -1,   118,   119,   120,    -1,
      -1,   121,    -1,   119,   139,   120,   121,    -1,   119,   120,
     121,    -1,   139,   122,   140,    -1,   140,    -1,   195,     5,
      -1,   195,   193,     5,    -1,   195,    21,     5,    -1,   195,
     193,     5,   193,    -1,   195,   193,   193,     5,    -1,     5,
      -1,   195,     5,   123,   201,    -1,   195,   193,     5,   123,
     201,    -1,   142,   141,    -1,    -1,   145,    -1,   146,    -1,
     163,    -1,   170,    -1,   171,    -1,   154,    -1,   155,    -1,
     156,    -1,   144,    -1,   150,    -1,   151,    -1,   143,    -1,
     180,    -1,    96,    -1,    66,    45,    -1,    66,     5,    -1,
      66,     5,   202,    -1,    66,     4,     5,   114,     4,     5,
      -1,    54,   179,    -1,   195,   192,   121,    -1,    17,   192,
     121,    -1,   196,   192,   121,    -1,   196,   192,   123,   202,
     121,    -1,   195,   193,   192,   121,    -1,   195,   193,   192,
     193,   121,    -1,   196,   193,   192,   121,    -1,   196,   193,
       5,   123,   202,   121,    -1,   196,   193,     5,   193,   121,
      -1,   196,   193,   193,   192,   121,    -1,   196,   193,   193,
       5,   123,   202,   121,    -1,   196,     5,   193,   121,    -1,
     196,   169,   192,   121,    -1,   196,   169,     5,   123,   202,
     121,    -1,     5,    27,     5,     5,   121,    -1,     7,   184,
     121,    -1,     7,   166,   191,   123,   202,   121,    -1,     7,
     147,   166,   191,   123,   202,   121,    -1,     7,   147,   191,
     123,   202,   121,    -1,   119,   148,   122,   148,   120,    -1,
      67,    -1,    68,    -1,    69,    -1,    70,    -1,    71,    -1,
      72,    -1,    73,    -1,    74,    -1,   193,    -1,    21,    -1,
      56,     5,   121,   152,   190,    57,    -1,    56,     5,   121,
     190,    57,    -1,    56,   193,   193,     5,   121,   152,   179,
      57,    -1,    56,   149,     5,   121,   152,   179,    57,    -1,
      56,   149,     5,   121,   179,    57,    -1,    56,     5,   119,
     139,   120,   121,   179,    57,    -1,    56,     5,   119,   139,
     120,   121,   152,   179,    57,    -1,    56,   149,     5,   119,
     139,   120,   121,   179,    57,    -1,    56,   149,     5,   119,
     139,   120,   121,   152,   179,    57,    -1,    58,     5,   121,
     152,   179,    59,    -1,    58,     5,   121,   179,    59,    -1,
      58,     5,   119,   139,   120,   121,   179,    59,    -1,    58,
       5,   119,   139,   120,   121,   152,   179,    59,    -1,   152,
     153,    -1,   153,    -1,    11,   192,   121,    -1,    22,   192,
     121,    -1,    23,   192,   121,    -1,    11,   193,   192,   121,
      -1,    11,   193,     5,   193,   121,    -1,    11,   193,   193,
       5,   121,    -1,     9,    11,   193,   193,     5,   121,    -1,
       8,   192,   121,    -1,     8,   192,   193,   121,    -1,     8,
     193,   193,   192,   121,    -1,     8,    21,   192,   121,    -1,
      21,   192,   121,    -1,    21,   192,   193,   121,    -1,    47,
     159,   121,    -1,    47,    16,   159,   121,    -1,    47,   193,
     159,   121,    -1,    47,   193,   193,   159,   121,    -1,    47,
      16,   193,   159,   121,    -1,    48,   159,   121,    -1,    48,
     193,   159,   121,    -1,    48,   193,   193,   159,   121,    -1,
      46,   158,   121,    -1,   200,   123,   202,    -1,   158,   122,
     157,    -1,   157,    -1,   159,   122,   160,    -1,   160,    -1,
       5,   123,   202,    -1,   161,   122,   162,    -1,   162,    -1,
      47,     5,   123,   202,    -1,    47,   193,     5,   123,   202,
      -1,     5,   123,   202,    -1,     5,     5,   119,   120,   121,
      -1,     5,   169,     5,   119,   120,   121,    -1,     5,     5,
     121,    -1,    42,   119,   189,   120,   121,    -1,    42,     5,
     119,   189,   120,   121,    -1,     5,     5,   119,   164,   120,
     121,    -1,    42,     5,   119,   164,   120,   121,    -1,     5,
       5,   119,   189,   120,   121,    -1,     5,   119,   189,   120,
     121,    -1,     5,   169,     5,   119,   164,   120,   121,    -1,
       5,   169,     5,   193,   119,   164,   120,   121,    -1,     5,
       5,   193,   119,   164,   120,   121,    -1,     5,     5,   193,
     119,   189,   120,   121,    -1,   164,   122,   165,    -1,   165,
      -1,   124,   113,    -1,   124,     5,   119,   202,   120,    -1,
     124,     5,   119,   120,    -1,   118,   119,   189,   120,    -1,
     118,     4,    -1,   118,     5,    -1,   118,    82,    -1,   167,
     122,   168,    -1,   168,    -1,   124,     5,   119,   202,   120,
      -1,   124,     5,    -1,   118,   119,   189,   120,    -1,   118,
       4,    -1,   118,    82,    -1,   118,     5,    -1,   118,   119,
     167,   120,    -1,   118,   119,   120,    -1,    35,   179,    -1,
      35,   175,   179,    -1,    85,   172,    86,    -1,   172,   173,
      -1,   173,    -1,    36,   172,    37,    -1,    36,    99,     5,
     172,    37,    -1,    87,     5,   121,    -1,   145,    -1,   146,
      -1,   154,    -1,   155,    -1,   156,    -1,   163,    -1,   174,
      -1,   170,    -1,   144,    -1,    38,   119,   202,   120,   173,
      -1,    38,   119,   202,   120,   173,    39,   173,    -1,    60,
     119,   184,   121,   202,   121,   184,   120,   173,    -1,   125,
     113,    -1,   125,    84,    -1,   125,     5,    -1,   125,   119,
     177,   120,    -1,    42,    -1,   122,    -1,   177,   176,   178,
      -1,   178,    -1,    40,   202,    -1,    41,   202,    -1,   202,
      -1,    36,   190,    37,    -1,    36,    37,    -1,    55,   179,
      -1,    36,    99,     5,   190,    37,    -1,    75,   190,    76,
      -1,   191,   123,   202,   121,    -1,   191,   123,   166,   202,
     121,    -1,   191,    34,   202,   121,    -1,   191,    34,   166,
     202,   121,    -1,    38,   119,   202,   120,   179,    -1,    38,
     119,   202,   120,   179,    39,   179,    -1,    43,   202,   121,
      -1,    21,   192,   121,    -1,    11,   192,   121,    -1,    11,
     193,   192,   121,    -1,    89,   202,   121,    -1,    88,   202,
     123,   202,   121,    -1,   175,   121,    -1,    44,     5,   121,
      -1,    77,     5,   121,    -1,     5,   119,   120,   121,    -1,
       5,   119,   189,   120,   121,    -1,    49,   119,   202,   120,
     186,    52,    -1,    49,   119,   202,   120,   186,   188,    52,
      -1,    49,   119,   202,   120,   188,    52,    -1,    50,   119,
     202,   120,   186,    52,    -1,    50,   119,   202,   120,   186,
     188,    52,    -1,    51,   119,   202,   120,   186,    52,    -1,
      51,   119,   202,   120,   186,   188,    52,    -1,   118,   202,
     121,    -1,   118,   202,   179,    -1,     5,   121,    -1,   181,
      -1,   182,    -1,   183,    -1,   200,   121,    -1,   180,    -1,
       7,   191,   123,   202,   121,    -1,    97,     5,   121,    -1,
      78,    45,    79,    -1,    60,   119,   184,   121,   202,   121,
     184,   120,   179,    -1,    93,   119,   202,   120,   179,    -1,
      61,   119,   202,   120,   179,    -1,   184,   122,   185,    -1,
     185,    -1,   191,   123,   202,    -1,   186,   187,    -1,   187,
      -1,   189,    99,   179,    -1,   189,    99,   121,    -1,    53,
      99,   179,    -1,    53,    99,   121,    -1,   189,   122,   202,
      -1,   202,    -1,   190,   179,    -1,   179,    -1,     5,    -1,
       5,   193,    -1,     5,   194,   193,    -1,     5,   194,   194,
      -1,     5,   194,    -1,   200,    -1,   197,    -1,     5,   122,
     192,    -1,     5,    -1,   126,   202,    99,   202,   127,    -1,
     126,   202,    80,   202,   127,    -1,   126,   202,    81,   202,
     127,    -1,   126,   202,   127,    -1,     8,    -1,     9,    -1,
      10,    -1,     9,    11,    -1,     8,    12,    -1,     9,    12,
      -1,    10,    12,    -1,     8,    16,    -1,     9,    16,    -1,
       9,    11,    16,    -1,     9,    13,    -1,     8,    13,    -1,
      13,    -1,    11,    -1,    12,    -1,    16,    -1,    21,    -1,
      22,    -1,    11,    16,    -1,    12,    16,    -1,    87,    -1,
      94,    -1,    95,    -1,    14,    -1,    15,    -1,   128,   198,
     129,    -1,   198,   122,   199,    -1,   199,    -1,   202,   197,
      -1,   202,    -1,   106,   197,    -1,     5,   124,   200,    -1,
       5,   124,     5,    -1,     5,   124,     5,   193,    -1,     5,
     124,     5,   194,    -1,     5,   124,     5,   119,   202,   120,
      -1,     4,    -1,    82,    -1,    45,    -1,    18,    -1,    19,
      -1,    20,    -1,    24,    -1,    25,    -1,    26,    -1,     5,
      -1,   200,    -1,     4,    -1,    82,    -1,    45,    -1,    66,
      -1,    66,   119,   202,   120,    -1,    18,    -1,    19,    -1,
      20,    -1,    24,    -1,    25,    -1,    26,    -1,     5,   193,
      -1,     5,   194,   193,    -1,     5,   194,   194,    -1,     5,
     194,    -1,   202,    98,   202,    99,   202,    -1,   202,   109,
     202,    -1,   202,   113,   202,    -1,   202,   110,   202,    -1,
     202,   114,   202,    -1,   202,   115,   202,    -1,   202,   101,
     202,    -1,   202,   100,   202,    -1,   202,   102,   202,    -1,
     202,   107,   202,    -1,   202,   108,   202,    -1,   202,    83,
     202,    -1,   202,    28,   202,    -1,   202,    29,   202,    -1,
     202,    90,   202,    -1,   202,    91,   202,    -1,   202,    92,
     202,    -1,   202,    31,   202,    -1,   202,    30,   202,    -1,
     202,    32,   202,    -1,   202,   112,   202,    -1,   202,    33,
     202,    -1,   202,    34,   202,    -1,   202,   106,   202,    -1,
     202,   105,   202,    -1,   202,   103,   202,    -1,     5,   119,
     189,   120,    -1,   119,   202,   120,    -1,   197,    -1,   110,
     202,    -1,   100,   202,    -1,   102,   202,    -1,   101,   202,
      -1,    90,   202,    -1,    92,   202,    -1,    91,   202,    -1,
     130,   202,    -1,   131,   202,    -1
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
     267,   268,   269,   270,   271,   274,   275,   276,   277,   278,
     278,   279,   280,   280,   281,   281,   282,   282,   284,   284,
     285,   285,   288,   288,   288,   288,   288,   288,   288,   290,
     290,   292,   292,   292,   293,   295,   295,   295,   295,   295,
     295,   295,   295,   295,   295,   295,   295,   297,   297,   297,
     297,   297,   297,   297,   297,   297,   297,   297,   297,   297,
     299,   300,   300,   302,   303,   304,   308,   309,   310,   311,
     312,   316,   317,   318,   319,   319,   319,   319,   319,   319,
     323,   324,   325,   326,   327,   328,   329,   330,   330,   330,
     330,   330,   330,   331,   332,   333,   334,   335,   336,   337,
     338,   339,   340,   341,   342,   343,   344,   345,   346,   347,
     348,   349,   350,   351,   352,   353,   354,   355,   356,   357,
     358,   359,   360,   361,   362,   363,   364,   365,   366,   367,
     368,   369,   370,   371,   372
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
  "return", "'?'", "':'", "'|'", "'^'", "'&'", "arith_shift_right",
  "SignedLeft", "shift_right", "shift_left", "'<'", "'>'", "'+'", "'-'",
  "Veryequal", "noteqeq", "'*'", "'/'", "'%'", "StarStar", "UNARY_PREC",
  "'#'", "'('", "')'", "';'", "','", "'='", "'.'", "'@'", "'['", "']'",
  "'{'", "'}'", "'!'", "'~'", "$accept", "Main", "Mains", "MainItem",
  "Module", "Hparams", "Header", "Header_list", "Header_item",
  "Module_stuffs", "Mstuff", "Define", "Initial", "Definition", "Assign",
  "StrengthDef", "Strength", "WidthInt", "Function", "Task", "Mem_defs",
  "Mem_def", "Parameter", "Localparam", "Defparam", "DottedPair",
  "DottedPairs", "Pairs", "Pair", "head_params", "head_param", "Instance",
  "Conns_list", "Connection", "AssignParams", "Prms_list", "PrmAssign",
  "InstParams", "Always", "Generate", "GenStatements", "GenStatement",
  "GenFor_statement", "When", "Or_coma", "When_items", "When_item",
  "Statement", "Pragma", "For_statement", "Repeat_statement",
  "While_statement", "Soft_assigns", "Soft_assign", "Cases", "Case",
  "Default", "Exprs", "Statements", "LSH", "Tokens_list", "Width",
  "BusBit", "ExtDir", "IntDir", "CurlyList", "CurlyItems", "CurlyItem",
  "Dotted", "Literal", "Expr", 0
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
     345,   346,   347,   348,   349,   350,   351,   352,    63,    58,
     124,    94,    38,   353,   354,   355,   356,    60,    62,    43,
      45,   357,   358,    42,    47,    37,   359,   360,    35,    40,
      41,    59,    44,    61,    46,    64,    91,    93,   123,   125,
      33,   126
};
# endif

/* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint8 yyr1[] =
{
       0,   132,   133,   134,   134,   135,   135,   136,   137,   137,
     137,   138,   138,   138,   139,   139,   140,   140,   140,   140,
     140,   140,   140,   140,   141,   141,   142,   142,   142,   142,
     142,   142,   142,   142,   142,   142,   142,   142,   142,   142,
     143,   143,   143,   143,   144,   145,   145,   145,   145,   145,
     145,   145,   145,   145,   145,   145,   145,   145,   145,   145,
     146,   146,   146,   146,   147,   148,   148,   148,   148,   148,
     148,   148,   148,   149,   149,   150,   150,   150,   150,   150,
     150,   150,   150,   150,   151,   151,   151,   151,   152,   152,
     153,   153,   153,   153,   153,   153,   153,   153,   153,   153,
     153,   153,   153,   154,   154,   154,   154,   154,   155,   155,
     155,   156,   157,   158,   158,   159,   159,   160,   161,   161,
     162,   162,   162,   163,   163,   163,   163,   163,   163,   163,
     163,   163,   163,   163,   163,   163,   164,   164,   165,   165,
     165,   166,   166,   166,   166,   167,   167,   168,   168,   169,
     169,   169,   169,   169,   169,   170,   170,   171,   172,   172,
     173,   173,   173,   173,   173,   173,   173,   173,   173,   173,
     173,   173,   173,   173,   174,   175,   175,   175,   175,   176,
     176,   177,   177,   178,   178,   178,   179,   179,   179,   179,
     179,   179,   179,   179,   179,   179,   179,   179,   179,   179,
     179,   179,   179,   179,   179,   179,   179,   179,   179,   179,
     179,   179,   179,   179,   179,   179,   179,   179,   179,   179,
     179,   179,   179,   179,   179,   180,   181,   182,   183,   184,
     184,   185,   186,   186,   187,   187,   188,   188,   189,   189,
     190,   190,   191,   191,   191,   191,   191,   191,   191,   192,
     192,   193,   193,   193,   194,   195,   195,   195,   195,   195,
     195,   195,   195,   195,   195,   195,   195,   196,   196,   196,
     196,   196,   196,   196,   196,   196,   196,   196,   196,   196,
     197,   198,   198,   199,   199,   199,   200,   200,   200,   200,
     200,   201,   201,   201,   201,   201,   201,   201,   201,   201,
     202,   202,   202,   202,   202,   202,   202,   202,   202,   202,
     202,   202,   202,   202,   202,   202,   202,   202,   202,   202,
     202,   202,   202,   202,   202,   202,   202,   202,   202,   202,
     202,   202,   202,   202,   202,   202,   202,   202,   202,   202,
     202,   202,   202,   202,   202,   202,   202,   202,   202,   202,
     202,   202,   202,   202,   202
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
       1,     2,     1,     5,     3,     3,     9,     5,     5,     3,
       1,     3,     2,     1,     3,     3,     3,     3,     3,     1,
       2,     1,     1,     2,     3,     3,     2,     1,     1,     3,
       1,     5,     5,     5,     3,     1,     1,     1,     2,     2,
       2,     2,     2,     2,     3,     2,     2,     1,     1,     1,
       1,     1,     1,     2,     2,     1,     1,     1,     1,     1,
       3,     3,     1,     2,     1,     2,     3,     3,     4,     4,
       6,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     4,     1,     1,     1,
       1,     1,     1,     2,     3,     3,     2,     5,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     4,     3,     1,     2,     2,     2,     2,
       2,     2,     2,     2,     2
};

/* YYDEFACT[STATE-NAME] -- Default rule to reduce with in state
   STATE-NUM when YYTABLE doesn't specify something else to do.  Zero
   means the default is an error.  */
static const yytype_uint16 yydefact[] =
{
       0,     0,     0,     0,     2,     4,     5,     6,    10,     0,
      41,    40,     1,     3,     0,     0,     0,   302,   300,   307,
     308,   309,   310,   311,   312,   304,   305,   303,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   345,
     301,    42,     0,     0,    11,    25,     0,     0,     0,     0,
     313,   316,     0,   350,   352,   351,   347,   349,   348,   346,
       0,     0,     0,   282,   284,   353,   354,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     9,     0,   119,    21,   255,
     256,   257,     0,     0,    15,     0,     0,     0,   268,   269,
     267,   278,   279,   270,     0,   271,   272,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   275,   276,   277,
      39,     0,    25,    37,    34,    26,    27,    35,    36,    31,
      32,    33,    28,    29,    30,    38,     0,     0,     0,     0,
     239,   287,   286,     0,   314,   315,     0,   344,   285,     0,
     280,   283,   329,   330,   335,   334,   336,   338,   339,   328,
     331,   332,   333,     0,   324,   323,   325,   342,   341,   340,
     326,   327,   318,   320,   337,   319,   321,   322,     0,     0,
       0,     0,     8,     0,   259,   266,   262,   258,   260,   265,
     263,   261,    13,     0,     0,    16,     0,     0,     0,     0,
       0,     0,     0,   242,     0,     0,     0,     0,     0,   230,
       0,   248,   247,   273,   274,   250,     0,   242,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     155,   222,   218,   219,   220,     0,   247,     0,     0,     0,
     114,     0,     0,     0,     0,     0,   116,     0,     0,     0,
       0,    44,     0,    74,     0,    73,     0,     0,     0,     0,
       0,   275,   171,   163,   164,   165,   166,   167,   168,   170,
       0,   159,   169,     7,    24,     0,     0,   250,     0,     0,
       0,    43,   343,     0,     0,   288,   289,     0,     0,     0,
     254,   306,   281,     0,   122,     0,     0,     0,   118,   264,
      12,    14,     0,    18,    17,     0,     0,   125,     0,     0,
     150,   152,   151,     0,     0,     0,   243,   246,   142,   143,
     144,     0,    65,    66,    67,    68,    69,    70,    71,    72,
       0,     0,     0,     0,    60,     0,     0,     0,    46,     0,
     217,     0,     0,     0,     0,   187,     0,   241,     0,     0,
       0,     0,     0,     0,     0,   188,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   177,   176,   175,     0,   203,
     156,     0,     0,   221,     0,     0,   111,     0,     0,     0,
       0,     0,   103,     0,     0,     0,   108,     0,     0,     0,
       0,     0,     0,     0,     0,   225,     0,     0,     0,     0,
       0,   157,   158,    45,     0,     0,   250,     0,    47,     0,
     250,     0,     0,   238,     0,     0,     0,     0,   317,   120,
       0,   291,   294,   295,   296,   297,   298,   299,   293,   292,
      22,     0,    19,    20,     0,     0,     0,   137,     0,     0,
       0,   154,     0,     0,   146,     0,     0,     0,     0,   244,
     245,     0,     0,     0,     0,     0,   229,   231,   249,     0,
       0,     0,   199,     0,   198,     0,   186,   240,     0,   197,
     204,     0,     0,     0,     0,     0,   190,   205,     0,   201,
       0,   224,   215,   216,     0,     0,     0,   182,   185,     0,
       0,     0,     0,     0,     0,     0,   113,   112,   117,   104,
       0,   115,   105,     0,   109,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    89,     0,     0,     0,     0,     0,
       0,     0,     0,   160,     0,     0,   162,    49,     0,    56,
       0,    57,     0,     0,     0,    51,   250,     0,   290,   252,
     253,   251,   121,    23,   123,     0,   138,     0,     0,     0,
       0,     0,    59,   148,   153,     0,   149,   131,     0,     0,
       0,   141,     0,     0,     0,     0,   206,     0,     0,   200,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   183,
     184,   179,   178,   180,     0,     0,   193,     0,   191,     0,
       0,   126,   107,   106,   110,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    88,     0,    76,     0,     0,
       0,     0,     0,     0,    85,     0,     0,     0,    50,     0,
      48,     0,    53,     0,    54,     0,   128,   136,   130,     0,
       0,     0,   145,   124,     0,     0,    64,     0,    63,    61,
     207,   223,   189,   195,     0,     0,   233,     0,     0,     0,
       0,     0,   228,   202,   227,   181,   194,   192,   129,   127,
       0,     0,    97,     0,     0,     0,    90,   250,     0,     0,
     101,     0,    91,    92,    75,     0,     0,    79,     0,     0,
       0,     0,    84,   161,   172,     0,    58,    52,     0,   140,
       0,   134,   135,     0,   132,     0,    62,     0,     0,   208,
     232,     0,   210,     0,   211,     0,   213,     0,     0,     0,
       0,   100,    98,     0,     0,     0,    93,     0,   102,     0,
      78,     0,     0,     0,     0,     0,     0,     0,     0,    55,
     139,   147,   133,   196,   237,   236,   209,   235,   234,   212,
     214,     0,     0,    80,    99,     0,    94,    95,     0,     0,
      90,     0,   101,    77,     0,    86,   173,     0,     0,    81,
      96,     0,    82,    93,    87,     0,   226,    83,   174
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,     3,     4,     5,     6,    15,    45,   103,   104,   131,
     132,     7,   282,   283,   284,   216,   350,   274,   137,   138,
     533,   534,   285,   286,   287,   260,   261,   265,   266,    96,
      97,   288,   456,   457,   217,   463,   464,   212,   289,   144,
     290,   291,   292,   270,   604,   506,   507,   367,   251,   252,
     253,   254,   218,   219,   665,   666,   667,   668,   368,   255,
     226,   336,   337,   146,   147,    39,    62,    63,    40,   450,
     150
};

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
#define YYPACT_NINF -515
static const yytype_int16 yypact[] =
{
      61,    37,    71,    57,    61,  -515,  -515,  -515,   -67,    80,
    1840,  -515,  -515,  -515,   -53,   -28,   -12,  -515,   -56,  -515,
    -515,  -515,  -515,  -515,  -515,  -515,    14,  -515,  1840,  1840,
    1840,  1840,  1840,  1840,  1840,  1840,  1465,  1840,  1840,  -515,
    -515,  5010,    51,    45,  -515,  4923,   143,  1840,   182,  1840,
    -515,    95,  1840,  -515,  -515,  -515,  -515,  -515,  -515,  -515,
    4086,   121,   -26,  -515,  2650,  -515,  -515,  1840,  1840,  1840,
    1840,  1840,  1840,  1840,  1840,  1840,  1840,  1840,  1840,  1840,
    1840,  1840,  1840,  1840,  1840,  1840,  1840,  1840,  1840,  1840,
    1840,  1840,  1840,   111,    25,  -515,    39,  -515,  -515,   258,
     234,   245,   154,    88,  -515,    23,    12,     4,   286,   290,
    -515,  -515,  -515,  -515,   282,  -515,  -515,  2611,    53,   310,
      22,    28,  2611,    24,   317,   280,  4465,  -515,  -515,  -515,
    -515,   334,  4923,  -515,  -515,  -515,  -515,  -515,  -515,  -515,
    -515,  -515,  -515,  -515,  -515,  -515,    30,    27,   340,   192,
    5010,   -29,  -515,  2689,  -515,  -515,  4179,  -515,  -515,  1465,
    -515,  -515,  1903,  5098,   -35,   -35,   -35,   287,   287,  -515,
     399,   399,   399,  4962,  5050,   399,   417,   352,   352,   352,
     287,   287,   610,   610,   -35,  -515,  -515,  -515,  1840,   233,
    1840,   359,  -515,    15,  -515,  -515,  -515,   344,  -515,  -515,
    -515,  -515,  -515,   252,   228,   275,   390,    31,   -20,   398,
      18,  1840,   412,   213,    84,   211,    16,    10,    78,  -515,
     298,  -515,  -515,  -515,  -515,   259,   313,    90,    10,    30,
     282,   707,   306,  1840,   438,   327,   362,   365,  2611,   367,
     374,  2611,   458,  1840,  1840,   384,   463,  1840,   100,  2119,
    -515,  -515,  -515,  -515,  -515,     3,   351,   391,  1840,   364,
    -515,   106,   392,   394,    28,   118,  -515,    28,   173,    28,
     400,  -515,   222,  -515,   514,   402,   223,   461,  3038,   454,
     455,   539,  -515,  -515,  -515,  -515,  -515,  -515,  -515,  -515,
     544,  -515,  -515,  -515,  -515,   462,   282,   129,   570,   227,
      36,  -515,  -515,  1840,  1840,  -515,  -515,  1840,  1840,  1840,
    -515,  -515,  -515,  1840,  5010,  1840,  4922,   464,  -515,  -515,
    -515,  -515,   659,  -515,   136,   579,   872,  -515,   466,   583,
    -515,  -515,  -515,   931,   231,    76,  -515,    95,  -515,  -515,
    -515,  1840,  -515,  -515,  -515,  -515,  -515,  -515,  -515,  -515,
     467,    10,   471,   473,  -515,    10,  1840,   282,  -515,  1508,
    -515,   476,   480,   282,   481,  -515,   598,  -515,  2181,  1840,
    3071,   484,  1840,  1840,  1840,  -515,    10,  1840,  2241,   488,
    2921,  3110,  1840,   491,  1944,  -515,  -515,  -515,  1094,  -515,
    -515,  1587,  1587,  -515,  1630,   232,  -515,   310,  1840,  1840,
     335,   608,  -515,   608,   355,   608,  -515,   369,   608,   228,
    2059,   240,   609,   228,  2059,  -515,   611,  4213,  1840,    10,
     494,  -515,  -515,  -515,   -54,   496,   210,   497,  -515,  1840,
     212,   498,   616,  5010,  4212,  2777,  2805,  2893,  5010,  5010,
    1840,  -515,  -515,  -515,  -515,  -515,  -515,  -515,  -515,  -515,
    -515,   659,  -515,  -515,   501,    29,   243,  -515,   247,  1630,
     503,  -515,   621,   254,  -515,   257,   506,   180,   509,  -515,
    -515,   267,   211,   510,  1840,  1840,  -515,  5010,  -515,   508,
     268,  1840,  -515,   513,  -515,  2611,  -515,  -515,  4305,  -515,
    -515,  4338,  4431,  4464,   376,  4557,  -515,  -515,  1840,  -515,
    4590,  -515,  -515,  -515,  1840,  1840,   104,  -515,  5010,  1840,
    3204,  1840,  3232,   271,   272,   515,  -515,  5010,  5010,  -515,
     414,  -515,  -515,   416,  -515,   425,   284,    26,   624,    30,
     282,   282,   282,  2059,  -515,  2303,   228,  2059,   516,   292,
    2059,   587,  4465,  -515,  4683,   442,  -515,  -515,   526,  -515,
    1840,  -515,  3326,  1840,   527,  -515,   445,   528,  -515,  -515,
    -515,  -515,  5010,  -515,  -515,   535,  -515,   534,   533,   538,
     296,   300,  -515,   543,  -515,   540,  -515,  -515,   546,   304,
     533,  -515,   545,  1840,  3354,  3448,  -515,   547,  3476,  -515,
    2365,  2611,  1719,  1840,  1840,  1840,  2611,  3570,  2611,  5010,
    5010,  -515,  -515,  -515,  1094,  3598,  -515,  3692,  -515,   550,
     552,  -515,  -515,  -515,  -515,   569,   282,   -39,   402,   402,
     571,    44,    91,   573,   574,  -515,  2425,  -515,   319,  2059,
     639,   221,   577,   640,  -515,  4339,  4465,  1840,  -515,  3720,
    -515,  3814,  -515,  1840,  -515,  1751,  -515,  -515,  -515,   580,
     581,  1840,  -515,  -515,   582,   320,  -515,  3842,  -515,  -515,
    -515,  -515,  -515,   666,   607,  1214,  -515,   655,   -38,  1343,
    1386,  3936,  -515,  -515,  -515,  -515,  -515,  -515,  -515,  -515,
    2059,   588,  -515,   589,   282,   402,   321,   129,   592,   703,
     395,   594,  -515,  -515,  -515,   595,   660,  -515,    30,   282,
    2059,  2059,  -515,  -515,   680,  3964,  -515,  -515,  4058,  -515,
    4716,  -515,  -515,  4809,  -515,   605,  -515,  2611,  2487,  -515,
    -515,   675,  -515,  2549,  -515,   677,  -515,   681,    10,  2059,
     678,  -515,  -515,   613,   731,   617,   396,   618,  -515,  2059,
    -515,   625,    44,    99,   685,  2059,   688,  4465,    10,  -515,
    -515,  -515,  -515,  -515,  -515,  -515,  -515,  -515,  -515,  -515,
    -515,   349,   691,  -515,  -515,   628,  -515,  -515,  2059,   695,
    -515,   632,  -515,  -515,   696,  -515,  -515,   353,  2611,  -515,
    -515,   697,  -515,  -515,  -515,  4465,  -515,  -515,  -515
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -515,  -515,  -515,   733,  -515,  -515,  -515,  -395,   555,   631,
    -515,     7,    32,    41,    47,  -515,   293,  -515,  -515,  -515,
    -408,  -514,    59,    66,    72,   372,  -515,  -109,   361,  -515,
     578,    73,  -386,   198,  -203,  -515,   195,   626,    74,  -515,
    -273,  -289,  -515,   657,  -515,  -515,   168,   -57,    75,  -515,
    -515,  -515,  -373,   420,   -23,  -404,  -402,   -36,  -225,  -103,
    -122,   -11,    -8,   -41,  -515,    60,  -515,   620,   -48,   325,
     781
};

/* YYTABLE[YYPACT[STATE-NUM]].  What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule which
   number is the opposite.  If zero, do what YYDEFACT says.
   If YYTABLE_NINF, syntax error.  */
#define YYTABLE_NINF -201
static const yytype_int16 yytable[] =
{
     152,   422,   105,   494,   220,   417,   540,    50,   513,   213,
      51,   149,   268,   351,   526,   213,   378,   208,   539,   625,
      93,   213,   330,   331,   295,   299,   625,   263,   205,   272,
     189,   225,   297,   263,   565,   225,   324,   391,   264,   209,
     154,   430,     8,   155,   206,   273,   545,   616,    74,   687,
      98,    14,   133,    99,   100,   101,    93,    12,   257,   222,
     250,   723,    94,    47,     1,   271,    42,   547,    48,   256,
      49,   262,   190,   570,   256,     9,    10,   134,    90,    91,
      92,   579,   682,   191,   303,    16,   135,   190,   338,   339,
     304,    43,   136,    44,   207,    48,   159,    49,    94,   326,
     332,   327,    46,   160,   139,   385,   190,   362,   364,   267,
     269,   140,   275,   352,   353,   625,    11,   141,   142,   143,
     145,   158,   214,   215,   161,   361,   392,     2,   422,   629,
     210,   211,    36,    52,   214,   296,   300,   333,    36,   133,
     305,   628,   566,   306,    36,   210,   601,   148,   190,   190,
     190,   190,   190,   190,   190,   400,   190,   190,   404,   192,
     407,   193,   190,   105,   134,   102,   340,   221,   222,   222,
     190,    95,   258,   135,   424,   334,   427,   221,   431,   136,
     222,   375,   221,   256,   386,   535,   625,   151,   509,   511,
     256,   139,   390,   256,   655,   467,   325,   328,   140,   354,
     355,   256,   190,   341,   141,   142,   143,   145,   203,   359,
     204,   360,   690,   387,    48,   625,    49,   190,   363,   388,
     772,    49,   395,   700,   602,   190,   603,   396,   397,   527,
     528,   625,   698,    98,   188,   478,    99,   100,   101,   402,
     403,   483,   699,   531,   532,   197,   198,   199,   473,    36,
     200,   357,   220,   401,   625,   190,   405,   201,   408,   451,
     590,   720,   190,   721,   412,   720,   720,   725,   727,   635,
     194,   195,   729,   220,   196,   202,   221,   221,   342,   343,
     344,   345,   346,   347,   348,   349,   425,   225,   221,   432,
     458,   221,   520,   745,   406,   403,   523,   465,   221,   525,
     578,   221,   223,   222,   455,   471,   224,   222,   626,   221,
     557,   487,   302,   452,   303,   259,   220,    69,    70,    71,
     256,   487,   276,   480,   468,   277,   469,   503,   222,   470,
     256,   768,   357,   550,   357,   553,   256,    48,   190,    49,
     293,   409,   413,   410,   414,   301,   422,   704,   428,   262,
     429,   466,   515,   303,   303,   761,   315,   541,   514,   536,
     319,   537,   256,   567,   317,   568,   256,   569,   105,   303,
      74,   222,   105,   320,   574,   777,   575,   576,  -199,   303,
    -199,   357,    69,    70,    71,    72,    73,   581,   587,   303,
     303,   609,   610,   568,   303,   323,    87,    88,   322,    89,
      90,    91,    92,   329,   615,   617,   204,   620,   622,   623,
     624,   221,   632,   548,   204,   221,   649,   335,   568,   554,
     650,   356,   303,   571,   654,   369,   568,    67,   221,    69,
      70,    71,    72,    73,   358,    74,   221,   256,   221,   695,
     715,   204,   568,   371,   221,    67,   372,    69,    70,    71,
      72,    73,  -198,  -200,  -198,  -200,   519,   403,   776,    85,
      86,    87,    88,   379,    89,    90,    91,    92,   383,   778,
     221,   355,   393,   785,   221,   355,   522,   403,   487,   221,
     630,   373,    74,   633,   374,   256,   376,   256,    48,   256,
     524,   403,   256,   377,   681,   105,   788,   595,   355,   688,
      74,    81,    82,   382,    83,    84,    85,    86,    87,    88,
     394,    89,    90,    91,    92,   398,   618,   399,   621,   411,
      82,   389,    83,    84,    85,    86,    87,    88,   190,    89,
      90,    91,    92,   487,   663,   612,   403,   613,   403,   672,
     415,   674,   256,   256,   420,   221,   614,   403,   256,   106,
     256,   107,    99,   100,   101,   108,   109,   110,   111,   112,
     113,   114,   733,   637,   355,   115,   116,   357,   643,   487,
     669,   670,   696,   418,   419,   426,   741,   743,   256,   117,
     278,   256,   279,   423,   453,   459,   118,   440,   460,   472,
     119,   120,   121,   221,   474,   221,   475,   221,   122,   481,
     221,   482,   484,   485,   280,   490,   683,   684,   685,   497,
     689,   691,   501,   263,   538,   546,   542,   549,   551,   555,
     771,   556,   564,   730,   572,   220,   573,   577,   580,   586,
     421,   281,   256,   583,   589,   619,   611,   631,   128,   129,
      69,    70,    71,   744,   746,   220,   634,   638,   642,   644,
     221,   221,   256,   256,   645,   646,   221,   455,   221,   648,
     753,   755,   651,   441,   462,   656,   758,   653,   660,   256,
     256,   678,   762,   679,   734,   256,   735,   442,   443,   444,
     222,   256,   769,   445,   446,   447,   221,   742,   774,   221,
     680,   256,   686,    74,   692,   693,   697,   256,   701,   702,
     222,   711,   712,   714,   448,   717,   718,   722,   737,   731,
     732,   781,   227,   736,   228,   738,   739,   740,   229,   747,
     256,   786,    89,    90,    91,    92,   752,   756,   230,   759,
     256,   689,   691,   760,   764,   763,   765,    13,   766,   767,
     221,   449,   773,   231,   365,   232,   770,   775,   779,   780,
     233,   234,   782,   783,   787,   784,   235,   236,   237,   321,
     221,   221,   238,   294,   521,   582,   647,   239,   240,   516,
     652,   318,   675,   298,   249,   476,   563,   221,   221,   312,
       0,     0,   241,   221,   242,   125,     0,     0,   221,   221,
       0,    41,     0,     0,     0,   243,   244,     0,     0,   221,
     245,     0,     0,     0,   246,   221,   366,     0,   221,    53,
      54,    55,    56,    57,    58,    59,    60,    64,    65,    66,
       0,     0,     0,     0,     0,   247,     0,     0,   221,     0,
     153,     0,   248,   156,     0,    36,     0,     0,   221,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   162,   163,
     164,   165,   166,   167,   168,   169,   170,   171,   172,   173,
     174,   175,   176,   177,   178,   179,   180,   181,   182,   183,
     184,   185,   186,   187,     0,     0,    17,    18,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      19,    20,    21,     0,     0,     0,    22,    23,    24,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    25,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    17,    18,     0,    26,     0,
      64,     0,     0,     0,     0,     0,     0,     0,     0,    19,
      20,    21,     0,     0,    27,    22,    23,    24,     0,     0,
       0,     0,    28,    29,    30,     0,     0,     0,     0,   314,
       0,   316,    31,    32,    33,     0,    25,     0,     0,     0,
       0,     0,    34,     0,     0,     0,     0,     0,     0,     0,
       0,    35,   454,     0,     0,     0,   455,    26,     0,     0,
      36,     0,    37,    38,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    27,   370,     0,     0,     0,     0,     0,
       0,    28,    29,    30,   380,   381,     0,     0,   384,     0,
       0,    31,    32,    33,     0,     0,     0,     0,     0,     0,
       0,    34,     0,     0,     0,     0,     0,     0,     0,     0,
      35,   461,     0,     0,     0,   462,     0,     0,     0,    36,
       0,    37,    38,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   433,   434,     0,     0,   435,   436,
     437,     0,     0,     0,   438,     0,   439,     0,    17,    18,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    19,    20,    21,     0,     0,     0,    22,    23,
      24,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   504,   505,     0,   477,     0,    25,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     488,     0,     0,   491,   492,   493,     0,     0,   495,     0,
      26,     0,     0,   500,     0,     0,     0,     0,     0,   508,
       0,     0,   510,   512,     0,     0,    27,     0,     0,   517,
     518,     0,     0,     0,    28,    29,    30,     0,     0,     0,
       0,     0,     0,     0,    31,    32,    33,     0,     0,   544,
       0,     0,     0,     0,    34,     0,     0,     0,     0,     0,
     552,     0,     0,    35,     0,     0,     0,     0,    17,    18,
       0,   562,    36,     0,    37,    38,     0,     0,     0,     0,
       0,     0,    19,    20,    21,     0,     0,     0,    22,    23,
      24,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   584,   585,     0,     0,    25,
       0,     0,   588,     0,     0,     0,   719,   664,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   597,
      26,     0,     0,     0,     0,   599,   600,     0,     0,     0,
     605,     0,   607,     0,     0,     0,    27,     0,     0,     0,
       0,     0,     0,     0,    28,    29,    30,     0,     0,     0,
       0,     0,     0,     0,    31,    32,    33,     0,     0,     0,
       0,     0,     0,     0,    34,     0,     0,     0,     0,     0,
       0,   639,     0,    35,   641,     0,     0,     0,     0,     0,
       0,     0,    36,     0,    37,    38,     0,    17,    18,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    19,    20,    21,   657,     0,     0,    22,    23,    24,
       0,     0,     0,     0,     0,     0,   671,     0,     0,     0,
       0,     0,     0,     0,     0,   508,     0,     0,    25,     0,
      17,    18,     0,     0,     0,   724,   664,     0,     0,     0,
       0,     0,     0,     0,    19,    20,    21,     0,     0,    26,
      22,    23,    24,     0,     0,     0,     0,     0,   705,     0,
       0,     0,     0,     0,   708,    27,   710,     0,     0,     0,
       0,    25,   713,    28,    29,    30,     0,     0,   726,   664,
       0,     0,     0,    31,    32,    33,     0,     0,     0,     0,
       0,     0,    26,    34,     0,     0,     0,     0,     0,     0,
       0,     0,    35,     0,     0,     0,     0,     0,    27,    17,
      18,    36,     0,    37,    38,     0,    28,    29,    30,     0,
       0,     0,     0,    19,    20,    21,    31,    32,    33,    22,
      23,    24,     0,     0,     0,     0,    34,     0,     0,     0,
       0,     0,     0,     0,     0,    35,     0,     0,     0,     0,
      25,     0,    17,    18,    36,     0,    37,    38,     0,     0,
       0,     0,     0,     0,     0,     0,    19,    20,    21,     0,
       0,    26,    22,    23,    24,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    27,     0,     0,
       0,     0,     0,    25,     0,    28,    29,    30,     0,     0,
       0,     0,     0,     0,     0,    31,    32,    33,     0,     0,
       0,    61,     0,     0,    26,    34,     0,     0,     0,     0,
       0,     0,     0,     0,    35,     0,     0,     0,     0,     0,
      27,    17,    18,    36,     0,    37,    38,     0,    28,    29,
      30,     0,     0,     0,     0,    19,    20,    21,    31,    32,
      33,    22,    23,    24,     0,     0,     0,     0,    34,     0,
       0,     0,     0,     0,     0,     0,     0,    35,   479,     0,
       0,     0,    25,     0,    17,    18,    36,     0,    37,    38,
       0,     0,     0,     0,     0,     0,     0,     0,    19,    20,
      21,     0,     0,    26,    22,    23,    24,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    27,
       0,     0,     0,     0,     0,    25,     0,    28,    29,    30,
       0,     0,     0,     0,     0,     0,     0,    31,    32,    33,
       0,     0,     0,     0,     0,     0,    26,    34,     0,     0,
       0,     0,     0,     0,     0,   214,    35,     0,     0,     0,
       0,     0,    27,     0,     0,    36,     0,    37,    38,     0,
      28,    29,    30,    17,    18,     0,     0,     0,     0,     0,
      31,    32,    33,     0,     0,     0,     0,    19,    20,    21,
      34,     0,     0,    22,    23,    24,     0,     0,     0,    35,
       0,     0,     0,     0,   455,    17,    18,     0,    36,     0,
      37,    38,     0,     0,    25,     0,     0,     0,     0,    19,
      20,    21,   664,     0,     0,    22,    23,    24,     0,     0,
       0,     0,     0,     0,     0,    26,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    25,     0,     0,     0,
       0,    27,     0,     0,     0,     0,     0,     0,     0,    28,
      29,    30,     0,     0,     0,     0,     0,    26,     0,    31,
      32,    33,     0,     0,     0,     0,     0,     0,     0,    34,
       0,     0,     0,    27,     0,     0,     0,     0,    35,     0,
       0,    28,    29,    30,    17,    18,     0,    36,     0,    37,
      38,    31,    32,    33,     0,     0,     0,     0,    19,    20,
      21,    34,     0,     0,    22,    23,    24,     0,     0,     0,
      35,   709,     0,     0,     0,     0,     0,     0,     0,    36,
       0,    37,    38,     0,     0,    25,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    26,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    27,     0,     0,     0,     0,     0,     0,     0,
      28,    29,    30,    69,    70,    71,    72,    73,     0,     0,
      31,    32,    33,     0,     0,     0,     0,     0,     0,   227,
      34,   228,     0,     0,     0,   229,     0,     0,     0,    35,
       0,     0,     0,     0,     0,   230,     0,     0,    36,     0,
      37,    38,    67,    68,    69,    70,    71,    72,    73,     0,
     231,     0,   232,     0,     0,     0,    74,   233,   234,     0,
       0,     0,     0,   235,   236,   237,     0,     0,     0,   238,
       0,     0,     0,     0,   239,   240,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,   241,
       0,   242,   125,     0,     0,     0,     0,    74,     0,     0,
       0,     0,   243,   244,    75,    76,    77,   245,     0,     0,
       0,   246,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
       0,     0,   247,     0,   227,   502,   228,   527,   528,   248,
     529,     0,    36,     0,     0,     0,     0,     0,     0,     0,
     530,   531,   532,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   231,     0,   232,     0,     0,
       0,     0,   233,   234,     0,     0,     0,     0,   235,   236,
     237,     0,     0,     0,   238,     0,     0,     0,     0,   239,
     240,     0,     0,     0,   227,     0,   228,     0,     0,     0,
     229,     0,     0,     0,   241,     0,   242,   125,     0,     0,
     230,     0,     0,     0,     0,     0,     0,   243,   244,     0,
       0,     0,   245,     0,     0,   231,   246,   232,     0,     0,
       0,     0,   233,   234,     0,     0,     0,     0,   235,   236,
     237,     0,     0,     0,   238,     0,     0,   247,     0,   239,
     240,     0,     0,     0,   248,     0,   227,    36,   228,     0,
       0,     0,   229,     0,   241,     0,   242,   125,     0,     0,
       0,     0,   230,     0,     0,     0,     0,   243,   244,     0,
       0,     0,   245,     0,     0,     0,   246,   231,   486,   232,
       0,     0,     0,     0,   233,   234,     0,     0,     0,     0,
     235,   236,   237,     0,     0,     0,   238,   247,     0,     0,
     389,   239,   240,     0,   248,     0,   227,    36,   228,     0,
       0,     0,   229,     0,     0,     0,   241,     0,   242,   125,
       0,     0,   230,     0,     0,     0,     0,     0,     0,   243,
     244,     0,     0,     0,   245,     0,     0,   231,   246,   232,
       0,     0,     0,     0,   233,   234,     0,     0,     0,     0,
     235,   236,   237,     0,     0,     0,   238,     0,     0,   247,
       0,   239,   240,     0,     0,     0,   248,     0,   227,    36,
     228,     0,     0,     0,   229,     0,   241,   496,   242,   125,
       0,     0,     0,     0,   230,     0,     0,     0,     0,   243,
     244,     0,     0,     0,   245,     0,     0,     0,   246,   231,
       0,   232,     0,     0,     0,     0,   233,   234,     0,     0,
       0,     0,   235,   236,   237,     0,     0,     0,   238,   247,
     627,     0,     0,   239,   240,     0,   248,     0,     0,    36,
     227,     0,   228,     0,     0,     0,   229,     0,   241,     0,
     242,   125,     0,     0,     0,     0,   230,     0,     0,     0,
       0,   243,   244,     0,     0,     0,   245,     0,     0,     0,
     246,   231,   662,   232,     0,     0,     0,     0,   233,   234,
       0,     0,     0,     0,   235,   236,   237,     0,     0,     0,
     238,   247,     0,     0,     0,   239,   240,     0,   248,     0,
     227,    36,   228,     0,     0,     0,   229,     0,     0,     0,
     241,     0,   242,   125,     0,     0,   230,     0,     0,     0,
       0,     0,     0,   243,   244,     0,     0,     0,   245,     0,
       0,   231,   246,   232,     0,     0,     0,     0,   233,   234,
       0,     0,     0,     0,   235,   236,   237,     0,     0,     0,
     238,     0,   694,   247,     0,   239,   240,     0,     0,     0,
     248,     0,   227,    36,   228,     0,     0,     0,   229,     0,
     241,     0,   242,   125,     0,     0,     0,     0,   230,     0,
       0,     0,     0,   243,   244,     0,     0,     0,   245,     0,
       0,     0,   246,   231,     0,   232,     0,     0,     0,     0,
     233,   234,     0,     0,     0,     0,   235,   236,   237,     0,
       0,     0,   238,   247,     0,     0,     0,   239,   240,     0,
     248,     0,     0,    36,   227,     0,   228,     0,     0,     0,
     229,     0,   241,     0,   242,   125,     0,     0,     0,     0,
     230,     0,     0,     0,     0,   243,   244,     0,     0,     0,
     245,     0,     0,     0,   246,   231,     0,   232,     0,     0,
       0,     0,   233,   234,     0,     0,     0,     0,   235,   236,
     237,     0,     0,     0,   238,   247,     0,     0,   754,   239,
     240,     0,   248,     0,     0,    36,   227,     0,   228,     0,
       0,     0,   229,     0,   241,     0,   242,   125,     0,     0,
       0,     0,   230,     0,     0,     0,     0,   243,   244,     0,
       0,     0,   245,     0,     0,     0,   246,   231,     0,   232,
       0,     0,     0,     0,   233,   234,     0,     0,     0,     0,
     235,   236,   237,     0,     0,     0,   238,   247,     0,     0,
     757,   239,   240,     0,   248,     0,     0,    36,    67,    68,
      69,    70,    71,    72,    73,     0,   241,     0,   242,   125,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   243,
     244,     0,     0,     0,   245,     0,     0,     0,   246,     0,
       0,     0,     0,     0,     0,     0,     0,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,   247,
       0,     0,     0,    74,     0,     0,   248,     0,     0,    36,
      75,    76,    77,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,     0,     0,     0,   307,
     308,     0,    74,     0,     0,     0,     0,     0,    36,    75,
      76,    77,     0,     0,     0,     0,     0,    78,   309,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,    67,    68,    69,    70,    71,
      72,    73,     0,     0,     0,     0,   310,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    67,    68,    69,    70,    71,    72,    73,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      74,     0,     0,     0,     0,     0,     0,    75,    76,    77,
       0,     0,     0,     0,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,    74,    89,
      90,    91,    92,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,    78,   559,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,   560,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    74,     0,     0,     0,
       0,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,    74,    89,    90,    91,    92,     0,
       0,    75,    76,    77,     0,     0,     0,     0,     0,    78,
     561,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,     0,
       0,     0,     0,   106,   498,   107,    99,   100,   101,   108,
     109,   110,   111,   112,   113,   114,     0,     0,     0,   115,
     116,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   117,   278,     0,   279,     0,     0,     0,
     118,     0,     0,     0,   119,   120,   121,     0,     0,     0,
       0,     0,   122,     0,     0,     0,     0,     0,   280,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   281,     0,     0,     0,     0,
       0,     0,   128,   129,     0,     0,     0,   416,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    74,     0,     0,     0,     0,     0,
       0,    75,    76,    77,     0,     0,     0,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,     0,
       0,     0,   489,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,     0,     0,     0,     0,
       0,   499,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    74,     0,     0,
       0,     0,     0,     0,    75,    76,    77,     0,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,    74,    89,    90,    91,    92,
       0,     0,    75,    76,    77,   606,     0,     0,     0,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,     0,     0,
       0,     0,     0,   608,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    74,
       0,     0,     0,     0,     0,     0,    75,    76,    77,     0,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,    74,    89,    90,
      91,    92,     0,     0,    75,    76,    77,   640,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
       0,     0,     0,     0,     0,   658,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    74,     0,     0,     0,     0,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,    74,
      89,    90,    91,    92,     0,     0,    75,    76,    77,   659,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,     0,     0,     0,     0,     0,   661,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,    74,    89,    90,    91,    92,     0,     0,    75,    76,
      77,   673,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,     0,   676,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    74,     0,     0,     0,     0,
       0,     0,    75,    76,    77,     0,     0,     0,     0,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,    74,    89,    90,    91,    92,     0,     0,
      75,    76,    77,   677,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,     0,     0,     0,     0,
       0,   706,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    74,     0,     0,
       0,     0,     0,     0,    75,    76,    77,     0,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,    74,    89,    90,    91,    92,
       0,     0,    75,    76,    77,   707,     0,     0,     0,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,     0,     0,
       0,     0,     0,   716,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    74,
       0,     0,     0,     0,     0,     0,    75,    76,    77,     0,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,    74,    89,    90,
      91,    92,     0,     0,    75,    76,    77,   728,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
       0,     0,     0,     0,     0,   748,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    74,     0,     0,     0,     0,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,    74,
      89,    90,    91,    92,     0,     0,    75,    76,    77,   749,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,     0,     0,     0,     0,   157,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,   106,     0,
     107,    99,   100,   101,   108,   109,   110,   111,   112,   113,
     114,     0,     0,     0,   115,   116,     0,     0,     0,     0,
      67,    68,    69,    70,    71,    72,    73,     0,   117,   278,
     543,   279,     0,     0,     0,   118,     0,     0,     0,   119,
     120,   121,    74,     0,     0,     0,     0,   122,     0,    75,
      76,    77,     0,   280,     0,     0,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,    74,     0,     0,     0,   311,
     281,     0,    75,    76,    77,     0,     0,   128,   129,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,     0,     0,
       0,     0,   558,    67,    68,    69,    70,    71,    72,    73,
       0,     0,     0,     0,   106,     0,   107,    99,   100,   101,
     108,   109,   110,   111,   112,   113,   114,     0,     0,     0,
     115,   116,     0,     0,     0,     0,    67,    68,    69,    70,
      71,    72,    73,     0,   117,   278,   703,   279,     0,     0,
       0,   118,     0,     0,     0,   119,   120,   121,    74,     0,
       0,     0,     0,   122,     0,    75,    76,    77,     0,   280,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,    74,     0,     0,     0,   591,   281,     0,    75,    76,
      77,     0,     0,   128,   129,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,   592,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
     106,     0,   107,    99,   100,   101,   108,   109,   110,   111,
     112,   113,   114,     0,     0,     0,   115,   116,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,     0,
     117,   278,     0,   279,     0,     0,     0,   118,     0,     0,
       0,   119,   120,   121,    74,     0,     0,     0,     0,   122,
       0,    75,    76,    77,     0,   280,     0,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,    74,     0,     0,
       0,   593,   281,     0,    75,    76,    77,     0,     0,   128,
     129,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
       0,     0,     0,     0,   594,    67,    68,    69,    70,    71,
      72,    73,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      74,     0,     0,     0,     0,     0,     0,    75,    76,    77,
       0,     0,     0,     0,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,    74,     0,     0,     0,   596,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,     0,     0,     0,     0,
     598,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    74,     0,     0,     0,
       0,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,    74,
       0,     0,     0,   636,     0,     0,    75,    76,    77,     0,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,     0,     0,     0,     0,   750,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    74,     0,     0,     0,     0,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,     0,     0,     0,   106,   751,
     107,    99,   100,   101,   108,   109,   110,   111,   112,   113,
     114,     0,     0,     0,   115,   116,     0,     0,     0,     0,
      67,    68,    69,    70,    71,    72,    73,     0,   117,     0,
       0,     0,     0,     0,     0,   118,     0,     0,     0,   119,
     120,   121,     0,     0,     0,     0,     0,   122,     0,   123,
       0,   124,     0,     0,     0,     0,     0,     0,     0,     2,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,   125,   307,   308,     0,    74,     0,     0,   126,     0,
     127,     0,    75,    76,    77,     0,     0,   128,   129,   130,
      78,   309,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,    67,    68,
      69,    70,    71,    72,    73,    74,     0,     0,     0,     0,
       0,     0,    75,    76,    77,     0,     0,     0,     0,     0,
      78,   313,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,    67,     0,    69,    70,
      71,    72,    73,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,     0,     0,
       0,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    74,     0,     0,     0,     0,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,     0,     0,     0,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92
};

static const yytype_int16 yycheck[] =
{
      48,   290,    43,   376,   107,   278,   414,    18,   394,     5,
      18,    47,   121,   216,   409,     5,   241,     5,   413,   533,
       5,     5,     4,     5,   146,   147,   540,     5,     5,     5,
       5,     5,     5,     5,     5,     5,     5,    34,    16,    27,
      51,     5,     5,    51,    21,    21,   419,    21,    83,     5,
       5,   118,    45,     8,     9,    10,     5,     0,     5,   107,
     117,    99,    47,   119,     3,   122,   119,   121,   124,   117,
     126,   119,   126,   459,   122,     4,     5,    45,   113,   114,
     115,   467,   121,    94,   122,     5,    45,   126,     4,     5,
     119,   119,    45,   121,   105,   124,   122,   126,    47,   119,
      82,   121,   114,   129,    45,     5,   126,   229,   230,   120,
     121,    45,   123,   216,   217,   629,    45,    45,    45,    45,
      45,    61,   118,   119,    64,   228,   123,    66,   417,   537,
     118,   119,   128,   119,   118,   146,   147,   119,   128,   132,
     151,   536,   113,   151,   128,   118,    42,     4,   126,   126,
     126,   126,   126,   126,   126,   264,   126,   126,   267,   120,
     269,   122,   126,   204,   132,   120,    82,   107,   216,   217,
     126,   120,   119,   132,   296,   211,   298,   117,   300,   132,
     228,   238,   122,   231,    84,   410,   700,     5,   391,   392,
     238,   132,   249,   241,   580,   119,   207,   208,   132,   121,
     122,   249,   126,   119,   132,   132,   132,   132,   120,   119,
     122,   121,   121,   113,   124,   729,   126,   126,   229,   119,
     121,   126,   258,   631,   120,   126,   122,   121,   122,     8,
       9,   745,    11,     5,   123,   357,     8,     9,    10,   121,
     122,   363,    21,    22,    23,    11,    12,    13,   351,   128,
      16,   122,   355,   264,   768,   126,   267,    12,   269,   123,
     485,   665,   126,   665,   275,   669,   670,   669,   670,   542,
      12,    13,   680,   376,    16,   121,   216,   217,    67,    68,
      69,    70,    71,    72,    73,    74,   297,     5,   228,   300,
     326,   231,   401,   701,   121,   122,   405,   333,   238,   408,
     120,   241,    16,   351,   124,   341,    16,   355,   533,   249,
     432,   368,   120,   324,   122,     5,   419,    30,    31,    32,
     368,   378,     5,   359,   335,    45,   337,   384,   376,   337,
     378,   739,   122,   123,   122,   123,   384,   124,   126,   126,
       6,   119,   119,   121,   121,     5,   635,   636,   121,   397,
     123,   120,   120,   122,   122,   728,   123,   414,   394,   119,
      16,   121,   410,   120,     5,   122,   414,   120,   409,   122,
      83,   419,   413,   121,   120,   748,   122,   120,    57,   122,
      59,   122,    30,    31,    32,    33,    34,   120,   120,   122,
     122,   120,   120,   122,   122,     5,   109,   110,   123,   112,
     113,   114,   115,     5,   120,   527,   122,   529,   530,   531,
     532,   351,   120,   424,   122,   355,   120,     5,   122,   430,
     120,   123,   122,   459,   120,   119,   122,    28,   368,    30,
      31,    32,    33,    34,   121,    83,   376,   485,   378,   120,
     120,   122,   122,     5,   384,    28,   119,    30,    31,    32,
      33,    34,    57,    57,    59,    59,   121,   122,   747,   107,
     108,   109,   110,     5,   112,   113,   114,   115,     5,   120,
     410,   122,   121,   120,   414,   122,   121,   122,   535,   419,
     537,   119,    83,   540,   119,   533,   119,   535,   124,   537,
     121,   122,   540,   119,   616,   536,   785,   121,   122,   621,
      83,   102,   103,   119,   105,   106,   107,   108,   109,   110,
     119,   112,   113,   114,   115,   123,   527,   123,   529,     5,
     103,   121,   105,   106,   107,   108,   109,   110,   126,   112,
     113,   114,   115,   590,   591,   121,   122,   121,   122,   596,
      79,   598,   590,   591,     5,   485,   121,   122,   596,     5,
     598,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      16,    17,   684,   121,   122,    21,    22,   122,   123,   626,
     593,   594,   629,   119,   119,     5,   698,   699,   626,    35,
      36,   629,    38,   121,     5,   119,    42,   123,     5,   122,
      46,    47,    48,   533,   123,   535,   123,   537,    54,   123,
     540,   121,   121,     5,    60,   121,   617,   618,   619,   121,
     621,   622,   121,     5,     5,   121,     5,   121,   121,   121,
     742,     5,   121,   680,   121,   728,     5,   121,   119,   121,
      86,    87,   680,   123,   121,    11,   121,   121,    94,    95,
      30,    31,    32,   700,   701,   748,    59,   121,   121,   121,
     590,   591,   700,   701,   119,   121,   596,   124,   598,   121,
     717,   718,   119,     4,   124,   120,   723,   121,   121,   717,
     718,   121,   729,   121,   685,   723,   687,    18,    19,    20,
     728,   729,   739,    24,    25,    26,   626,   698,   745,   629,
     121,   739,   121,    83,   121,   121,    57,   745,   121,    59,
     748,   121,   121,   121,    45,    39,    99,    52,     5,   121,
     121,   768,     5,   121,     7,   121,   121,    57,    11,    39,
     768,   778,   112,   113,   114,   115,   121,    52,    21,    52,
     778,   742,   743,    52,   121,    57,     5,     4,   121,   121,
     680,    82,    57,    36,    37,    38,   121,    59,    57,   121,
      43,    44,    57,   121,    57,    59,    49,    50,    51,   204,
     700,   701,    55,   132,   403,   472,   568,    60,    61,   397,
     575,   193,   604,   147,   117,   355,   451,   717,   718,   159,
      -1,    -1,    75,   723,    77,    78,    -1,    -1,   728,   729,
      -1,    10,    -1,    -1,    -1,    88,    89,    -1,    -1,   739,
      93,    -1,    -1,    -1,    97,   745,    99,    -1,   748,    28,
      29,    30,    31,    32,    33,    34,    35,    36,    37,    38,
      -1,    -1,    -1,    -1,    -1,   118,    -1,    -1,   768,    -1,
      49,    -1,   125,    52,    -1,   128,    -1,    -1,   778,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    67,    68,
      69,    70,    71,    72,    73,    74,    75,    76,    77,    78,
      79,    80,    81,    82,    83,    84,    85,    86,    87,    88,
      89,    90,    91,    92,    -1,    -1,     4,     5,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      18,    19,    20,    -1,    -1,    -1,    24,    25,    26,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    45,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,     4,     5,    -1,    66,    -1,
     159,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    18,
      19,    20,    -1,    -1,    82,    24,    25,    26,    -1,    -1,
      -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,   188,
      -1,   190,   100,   101,   102,    -1,    45,    -1,    -1,    -1,
      -1,    -1,   110,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   119,   120,    -1,    -1,    -1,   124,    66,    -1,    -1,
     128,    -1,   130,   131,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    82,   233,    -1,    -1,    -1,    -1,    -1,
      -1,    90,    91,    92,   243,   244,    -1,    -1,   247,    -1,
      -1,   100,   101,   102,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   110,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     119,   120,    -1,    -1,    -1,   124,    -1,    -1,    -1,   128,
      -1,   130,   131,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   303,   304,    -1,    -1,   307,   308,
     309,    -1,    -1,    -1,   313,    -1,   315,    -1,     4,     5,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    18,    19,    20,    -1,    -1,    -1,    24,    25,
      26,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    40,    41,    -1,   356,    -1,    45,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     369,    -1,    -1,   372,   373,   374,    -1,    -1,   377,    -1,
      66,    -1,    -1,   382,    -1,    -1,    -1,    -1,    -1,   388,
      -1,    -1,   391,   392,    -1,    -1,    82,    -1,    -1,   398,
     399,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   100,   101,   102,    -1,    -1,   418,
      -1,    -1,    -1,    -1,   110,    -1,    -1,    -1,    -1,    -1,
     429,    -1,    -1,   119,    -1,    -1,    -1,    -1,     4,     5,
      -1,   440,   128,    -1,   130,   131,    -1,    -1,    -1,    -1,
      -1,    -1,    18,    19,    20,    -1,    -1,    -1,    24,    25,
      26,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   474,   475,    -1,    -1,    45,
      -1,    -1,   481,    -1,    -1,    -1,    52,    53,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   498,
      66,    -1,    -1,    -1,    -1,   504,   505,    -1,    -1,    -1,
     509,    -1,   511,    -1,    -1,    -1,    82,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   100,   101,   102,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   110,    -1,    -1,    -1,    -1,    -1,
      -1,   550,    -1,   119,   553,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   128,    -1,   130,   131,    -1,     4,     5,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    18,    19,    20,   583,    -1,    -1,    24,    25,    26,
      -1,    -1,    -1,    -1,    -1,    -1,   595,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   604,    -1,    -1,    45,    -1,
       4,     5,    -1,    -1,    -1,    52,    53,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    18,    19,    20,    -1,    -1,    66,
      24,    25,    26,    -1,    -1,    -1,    -1,    -1,   637,    -1,
      -1,    -1,    -1,    -1,   643,    82,   645,    -1,    -1,    -1,
      -1,    45,   651,    90,    91,    92,    -1,    -1,    52,    53,
      -1,    -1,    -1,   100,   101,   102,    -1,    -1,    -1,    -1,
      -1,    -1,    66,   110,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   119,    -1,    -1,    -1,    -1,    -1,    82,     4,
       5,   128,    -1,   130,   131,    -1,    90,    91,    92,    -1,
      -1,    -1,    -1,    18,    19,    20,   100,   101,   102,    24,
      25,    26,    -1,    -1,    -1,    -1,   110,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   119,    -1,    -1,    -1,    -1,
      45,    -1,     4,     5,   128,    -1,   130,   131,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    18,    19,    20,    -1,
      -1,    66,    24,    25,    26,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    82,    -1,    -1,
      -1,    -1,    -1,    45,    -1,    90,    91,    92,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   100,   101,   102,    -1,    -1,
      -1,   106,    -1,    -1,    66,   110,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   119,    -1,    -1,    -1,    -1,    -1,
      82,     4,     5,   128,    -1,   130,   131,    -1,    90,    91,
      92,    -1,    -1,    -1,    -1,    18,    19,    20,   100,   101,
     102,    24,    25,    26,    -1,    -1,    -1,    -1,   110,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   119,   120,    -1,
      -1,    -1,    45,    -1,     4,     5,   128,    -1,   130,   131,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    18,    19,
      20,    -1,    -1,    66,    24,    25,    26,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    82,
      -1,    -1,    -1,    -1,    -1,    45,    -1,    90,    91,    92,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   100,   101,   102,
      -1,    -1,    -1,    -1,    -1,    -1,    66,   110,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   118,   119,    -1,    -1,    -1,
      -1,    -1,    82,    -1,    -1,   128,    -1,   130,   131,    -1,
      90,    91,    92,     4,     5,    -1,    -1,    -1,    -1,    -1,
     100,   101,   102,    -1,    -1,    -1,    -1,    18,    19,    20,
     110,    -1,    -1,    24,    25,    26,    -1,    -1,    -1,   119,
      -1,    -1,    -1,    -1,   124,     4,     5,    -1,   128,    -1,
     130,   131,    -1,    -1,    45,    -1,    -1,    -1,    -1,    18,
      19,    20,    53,    -1,    -1,    24,    25,    26,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    66,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    45,    -1,    -1,    -1,
      -1,    82,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    66,    -1,   100,
     101,   102,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   110,
      -1,    -1,    -1,    82,    -1,    -1,    -1,    -1,   119,    -1,
      -1,    90,    91,    92,     4,     5,    -1,   128,    -1,   130,
     131,   100,   101,   102,    -1,    -1,    -1,    -1,    18,    19,
      20,   110,    -1,    -1,    24,    25,    26,    -1,    -1,    -1,
     119,   120,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   128,
      -1,   130,   131,    -1,    -1,    45,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    66,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    82,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      90,    91,    92,    30,    31,    32,    33,    34,    -1,    -1,
     100,   101,   102,    -1,    -1,    -1,    -1,    -1,    -1,     5,
     110,     7,    -1,    -1,    -1,    11,    -1,    -1,    -1,   119,
      -1,    -1,    -1,    -1,    -1,    21,    -1,    -1,   128,    -1,
     130,   131,    28,    29,    30,    31,    32,    33,    34,    -1,
      36,    -1,    38,    -1,    -1,    -1,    83,    43,    44,    -1,
      -1,    -1,    -1,    49,    50,    51,    -1,    -1,    -1,    55,
      -1,    -1,    -1,    -1,    60,    61,   103,    -1,   105,   106,
     107,   108,   109,   110,    -1,   112,   113,   114,   115,    75,
      -1,    77,    78,    -1,    -1,    -1,    -1,    83,    -1,    -1,
      -1,    -1,    88,    89,    90,    91,    92,    93,    -1,    -1,
      -1,    97,    98,    -1,   100,   101,   102,   103,    -1,   105,
     106,   107,   108,   109,   110,    -1,   112,   113,   114,   115,
      -1,    -1,   118,    -1,     5,   121,     7,     8,     9,   125,
      11,    -1,   128,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      21,    22,    23,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    36,    -1,    38,    -1,    -1,
      -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,    50,
      51,    -1,    -1,    -1,    55,    -1,    -1,    -1,    -1,    60,
      61,    -1,    -1,    -1,     5,    -1,     7,    -1,    -1,    -1,
      11,    -1,    -1,    -1,    75,    -1,    77,    78,    -1,    -1,
      21,    -1,    -1,    -1,    -1,    -1,    -1,    88,    89,    -1,
      -1,    -1,    93,    -1,    -1,    36,    97,    38,    -1,    -1,
      -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,    50,
      51,    -1,    -1,    -1,    55,    -1,    -1,   118,    -1,    60,
      61,    -1,    -1,    -1,   125,    -1,     5,   128,     7,    -1,
      -1,    -1,    11,    -1,    75,    -1,    77,    78,    -1,    -1,
      -1,    -1,    21,    -1,    -1,    -1,    -1,    88,    89,    -1,
      -1,    -1,    93,    -1,    -1,    -1,    97,    36,    37,    38,
      -1,    -1,    -1,    -1,    43,    44,    -1,    -1,    -1,    -1,
      49,    50,    51,    -1,    -1,    -1,    55,   118,    -1,    -1,
     121,    60,    61,    -1,   125,    -1,     5,   128,     7,    -1,
      -1,    -1,    11,    -1,    -1,    -1,    75,    -1,    77,    78,
      -1,    -1,    21,    -1,    -1,    -1,    -1,    -1,    -1,    88,
      89,    -1,    -1,    -1,    93,    -1,    -1,    36,    97,    38,
      -1,    -1,    -1,    -1,    43,    44,    -1,    -1,    -1,    -1,
      49,    50,    51,    -1,    -1,    -1,    55,    -1,    -1,   118,
      -1,    60,    61,    -1,    -1,    -1,   125,    -1,     5,   128,
       7,    -1,    -1,    -1,    11,    -1,    75,    76,    77,    78,
      -1,    -1,    -1,    -1,    21,    -1,    -1,    -1,    -1,    88,
      89,    -1,    -1,    -1,    93,    -1,    -1,    -1,    97,    36,
      -1,    38,    -1,    -1,    -1,    -1,    43,    44,    -1,    -1,
      -1,    -1,    49,    50,    51,    -1,    -1,    -1,    55,   118,
      57,    -1,    -1,    60,    61,    -1,   125,    -1,    -1,   128,
       5,    -1,     7,    -1,    -1,    -1,    11,    -1,    75,    -1,
      77,    78,    -1,    -1,    -1,    -1,    21,    -1,    -1,    -1,
      -1,    88,    89,    -1,    -1,    -1,    93,    -1,    -1,    -1,
      97,    36,    37,    38,    -1,    -1,    -1,    -1,    43,    44,
      -1,    -1,    -1,    -1,    49,    50,    51,    -1,    -1,    -1,
      55,   118,    -1,    -1,    -1,    60,    61,    -1,   125,    -1,
       5,   128,     7,    -1,    -1,    -1,    11,    -1,    -1,    -1,
      75,    -1,    77,    78,    -1,    -1,    21,    -1,    -1,    -1,
      -1,    -1,    -1,    88,    89,    -1,    -1,    -1,    93,    -1,
      -1,    36,    97,    38,    -1,    -1,    -1,    -1,    43,    44,
      -1,    -1,    -1,    -1,    49,    50,    51,    -1,    -1,    -1,
      55,    -1,    57,   118,    -1,    60,    61,    -1,    -1,    -1,
     125,    -1,     5,   128,     7,    -1,    -1,    -1,    11,    -1,
      75,    -1,    77,    78,    -1,    -1,    -1,    -1,    21,    -1,
      -1,    -1,    -1,    88,    89,    -1,    -1,    -1,    93,    -1,
      -1,    -1,    97,    36,    -1,    38,    -1,    -1,    -1,    -1,
      43,    44,    -1,    -1,    -1,    -1,    49,    50,    51,    -1,
      -1,    -1,    55,   118,    -1,    -1,    -1,    60,    61,    -1,
     125,    -1,    -1,   128,     5,    -1,     7,    -1,    -1,    -1,
      11,    -1,    75,    -1,    77,    78,    -1,    -1,    -1,    -1,
      21,    -1,    -1,    -1,    -1,    88,    89,    -1,    -1,    -1,
      93,    -1,    -1,    -1,    97,    36,    -1,    38,    -1,    -1,
      -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,    50,
      51,    -1,    -1,    -1,    55,   118,    -1,    -1,   121,    60,
      61,    -1,   125,    -1,    -1,   128,     5,    -1,     7,    -1,
      -1,    -1,    11,    -1,    75,    -1,    77,    78,    -1,    -1,
      -1,    -1,    21,    -1,    -1,    -1,    -1,    88,    89,    -1,
      -1,    -1,    93,    -1,    -1,    -1,    97,    36,    -1,    38,
      -1,    -1,    -1,    -1,    43,    44,    -1,    -1,    -1,    -1,
      49,    50,    51,    -1,    -1,    -1,    55,   118,    -1,    -1,
     121,    60,    61,    -1,   125,    -1,    -1,   128,    28,    29,
      30,    31,    32,    33,    34,    -1,    75,    -1,    77,    78,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    88,
      89,    -1,    -1,    -1,    93,    -1,    -1,    -1,    97,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,    29,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,   118,
      -1,    -1,    -1,    83,    -1,    -1,   125,    -1,    -1,   128,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    98,    -1,
     100,   101,   102,   103,    -1,   105,   106,   107,   108,   109,
     110,    -1,   112,   113,   114,   115,    -1,    -1,    -1,    80,
      81,    -1,    83,    -1,    -1,    -1,    -1,    -1,   128,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    98,    99,   100,
     101,   102,   103,    -1,   105,   106,   107,   108,   109,   110,
      -1,   112,   113,   114,   115,    28,    29,    30,    31,    32,
      33,    34,    -1,    -1,    -1,    -1,   127,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    28,    29,    30,    31,    32,    33,    34,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,
      -1,    -1,    -1,    -1,    -1,    98,    -1,   100,   101,   102,
     103,    -1,   105,   106,   107,   108,   109,   110,    83,   112,
     113,   114,   115,    -1,    -1,    90,    91,    92,    -1,    -1,
      -1,    -1,    -1,    98,   127,   100,   101,   102,   103,    -1,
     105,   106,   107,   108,   109,   110,    -1,   112,   113,   114,
     115,    28,    29,    30,    31,    32,    33,    34,    -1,    -1,
      -1,    -1,   127,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    98,    -1,   100,   101,   102,   103,    -1,   105,   106,
     107,   108,   109,   110,    83,   112,   113,   114,   115,    -1,
      -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,    98,
     127,   100,   101,   102,   103,    -1,   105,   106,   107,   108,
     109,   110,    -1,   112,   113,   114,   115,    -1,    -1,    -1,
      -1,    -1,    -1,     5,   123,     7,     8,     9,    10,    11,
      12,    13,    14,    15,    16,    17,    -1,    -1,    -1,    21,
      22,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    35,    36,    -1,    38,    -1,    -1,    -1,
      42,    -1,    -1,    -1,    46,    47,    48,    -1,    -1,    -1,
      -1,    -1,    54,    -1,    -1,    -1,    -1,    -1,    60,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    87,    -1,    -1,    -1,    -1,
      -1,    -1,    94,    95,    -1,    -1,    -1,    99,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,
      -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,    98,
      -1,   100,   101,   102,   103,    -1,   105,   106,   107,   108,
     109,   110,    -1,   112,   113,   114,   115,    -1,    -1,    -1,
      -1,    -1,   121,    83,    -1,    -1,    -1,    -1,    -1,    -1,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    98,    -1,
     100,   101,   102,   103,    -1,   105,   106,   107,   108,   109,
     110,    -1,   112,   113,   114,   115,    -1,    -1,    -1,    -1,
      -1,   121,    28,    29,    30,    31,    32,    33,    34,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      28,    29,    30,    31,    32,    33,    34,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,
      -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,
      -1,    -1,    98,    -1,   100,   101,   102,   103,    -1,   105,
     106,   107,   108,   109,   110,    83,   112,   113,   114,   115,
      -1,    -1,    90,    91,    92,   121,    -1,    -1,    -1,    -1,
      98,    -1,   100,   101,   102,   103,    -1,   105,   106,   107,
     108,   109,   110,    -1,   112,   113,   114,   115,    -1,    -1,
      -1,    -1,    -1,   121,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    28,    29,    30,    31,    32,    33,    34,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,
      -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,
      -1,    -1,    -1,    -1,    98,    -1,   100,   101,   102,   103,
      -1,   105,   106,   107,   108,   109,   110,    83,   112,   113,
     114,   115,    -1,    -1,    90,    91,    92,   121,    -1,    -1,
      -1,    -1,    98,    -1,   100,   101,   102,   103,    -1,   105,
     106,   107,   108,   109,   110,    -1,   112,   113,   114,   115,
      -1,    -1,    -1,    -1,    -1,   121,    28,    29,    30,    31,
      32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,
      92,    -1,    -1,    -1,    -1,    -1,    98,    -1,   100,   101,
     102,   103,    -1,   105,   106,   107,   108,   109,   110,    83,
     112,   113,   114,   115,    -1,    -1,    90,    91,    92,   121,
      -1,    -1,    -1,    -1,    98,    -1,   100,   101,   102,   103,
      -1,   105,   106,   107,   108,   109,   110,    -1,   112,   113,
     114,   115,    -1,    -1,    -1,    -1,    -1,   121,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    28,    29,    30,    31,
      32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    98,    -1,
     100,   101,   102,   103,    -1,   105,   106,   107,   108,   109,
     110,    83,   112,   113,   114,   115,    -1,    -1,    90,    91,
      92,   121,    -1,    -1,    -1,    -1,    98,    -1,   100,   101,
     102,   103,    -1,   105,   106,   107,   108,   109,   110,    -1,
     112,   113,   114,   115,    -1,    -1,    -1,    -1,    -1,   121,
      28,    29,    30,    31,    32,    33,    34,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,
      -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,
      98,    -1,   100,   101,   102,   103,    -1,   105,   106,   107,
     108,   109,   110,    83,   112,   113,   114,   115,    -1,    -1,
      90,    91,    92,   121,    -1,    -1,    -1,    -1,    98,    -1,
     100,   101,   102,   103,    -1,   105,   106,   107,   108,   109,
     110,    -1,   112,   113,   114,   115,    -1,    -1,    -1,    -1,
      -1,   121,    28,    29,    30,    31,    32,    33,    34,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      28,    29,    30,    31,    32,    33,    34,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,
      -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,
      -1,    -1,    98,    -1,   100,   101,   102,   103,    -1,   105,
     106,   107,   108,   109,   110,    83,   112,   113,   114,   115,
      -1,    -1,    90,    91,    92,   121,    -1,    -1,    -1,    -1,
      98,    -1,   100,   101,   102,   103,    -1,   105,   106,   107,
     108,   109,   110,    -1,   112,   113,   114,   115,    -1,    -1,
      -1,    -1,    -1,   121,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    28,    29,    30,    31,    32,    33,    34,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,
      -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,
      -1,    -1,    -1,    -1,    98,    -1,   100,   101,   102,   103,
      -1,   105,   106,   107,   108,   109,   110,    83,   112,   113,
     114,   115,    -1,    -1,    90,    91,    92,   121,    -1,    -1,
      -1,    -1,    98,    -1,   100,   101,   102,   103,    -1,   105,
     106,   107,   108,   109,   110,    -1,   112,   113,   114,   115,
      -1,    -1,    -1,    -1,    -1,   121,    28,    29,    30,    31,
      32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,
      92,    -1,    -1,    -1,    -1,    -1,    98,    -1,   100,   101,
     102,   103,    -1,   105,   106,   107,   108,   109,   110,    83,
     112,   113,   114,   115,    -1,    -1,    90,    91,    92,   121,
      -1,    -1,    -1,    -1,    98,    -1,   100,   101,   102,   103,
      -1,   105,   106,   107,   108,   109,   110,    -1,   112,   113,
     114,   115,    -1,    -1,    -1,    -1,   120,    28,    29,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,     5,    -1,
       7,     8,     9,    10,    11,    12,    13,    14,    15,    16,
      17,    -1,    -1,    -1,    21,    22,    -1,    -1,    -1,    -1,
      28,    29,    30,    31,    32,    33,    34,    -1,    35,    36,
      37,    38,    -1,    -1,    -1,    42,    -1,    -1,    -1,    46,
      47,    48,    83,    -1,    -1,    -1,    -1,    54,    -1,    90,
      91,    92,    -1,    60,    -1,    -1,    -1,    98,    -1,   100,
     101,   102,   103,    -1,   105,   106,   107,   108,   109,   110,
      -1,   112,   113,   114,   115,    83,    -1,    -1,    -1,   120,
      87,    -1,    90,    91,    92,    -1,    -1,    94,    95,    -1,
      98,    -1,   100,   101,   102,   103,    -1,   105,   106,   107,
     108,   109,   110,    -1,   112,   113,   114,   115,    -1,    -1,
      -1,    -1,   120,    28,    29,    30,    31,    32,    33,    34,
      -1,    -1,    -1,    -1,     5,    -1,     7,     8,     9,    10,
      11,    12,    13,    14,    15,    16,    17,    -1,    -1,    -1,
      21,    22,    -1,    -1,    -1,    -1,    28,    29,    30,    31,
      32,    33,    34,    -1,    35,    36,    37,    38,    -1,    -1,
      -1,    42,    -1,    -1,    -1,    46,    47,    48,    83,    -1,
      -1,    -1,    -1,    54,    -1,    90,    91,    92,    -1,    60,
      -1,    -1,    -1,    98,    -1,   100,   101,   102,   103,    -1,
     105,   106,   107,   108,   109,   110,    -1,   112,   113,   114,
     115,    83,    -1,    -1,    -1,   120,    87,    -1,    90,    91,
      92,    -1,    -1,    94,    95,    -1,    98,    -1,   100,   101,
     102,   103,    -1,   105,   106,   107,   108,   109,   110,    -1,
     112,   113,   114,   115,    -1,    -1,    -1,    -1,   120,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
       5,    -1,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    -1,    -1,    -1,    21,    22,    -1,    -1,
      -1,    -1,    28,    29,    30,    31,    32,    33,    34,    -1,
      35,    36,    -1,    38,    -1,    -1,    -1,    42,    -1,    -1,
      -1,    46,    47,    48,    83,    -1,    -1,    -1,    -1,    54,
      -1,    90,    91,    92,    -1,    60,    -1,    -1,    -1,    98,
      -1,   100,   101,   102,   103,    -1,   105,   106,   107,   108,
     109,   110,    -1,   112,   113,   114,   115,    83,    -1,    -1,
      -1,   120,    87,    -1,    90,    91,    92,    -1,    -1,    94,
      95,    -1,    98,    -1,   100,   101,   102,   103,    -1,   105,
     106,   107,   108,   109,   110,    -1,   112,   113,   114,   115,
      -1,    -1,    -1,    -1,   120,    28,    29,    30,    31,    32,
      33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,
      -1,    -1,    -1,    -1,    -1,    98,    -1,   100,   101,   102,
     103,    -1,   105,   106,   107,   108,   109,   110,    -1,   112,
     113,   114,   115,    83,    -1,    -1,    -1,   120,    -1,    -1,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    98,    -1,
     100,   101,   102,   103,    -1,   105,   106,   107,   108,   109,
     110,    -1,   112,   113,   114,   115,    -1,    -1,    -1,    -1,
     120,    28,    29,    30,    31,    32,    33,    34,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    98,    -1,   100,   101,   102,   103,    -1,   105,   106,
     107,   108,   109,   110,    -1,   112,   113,   114,   115,    83,
      -1,    -1,    -1,   120,    -1,    -1,    90,    91,    92,    -1,
      -1,    -1,    -1,    -1,    98,    -1,   100,   101,   102,   103,
      -1,   105,   106,   107,   108,   109,   110,    -1,   112,   113,
     114,   115,    -1,    -1,    -1,    -1,   120,    28,    29,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    98,    -1,   100,
     101,   102,   103,    -1,   105,   106,   107,   108,   109,   110,
      -1,   112,   113,   114,   115,    -1,    -1,    -1,     5,   120,
       7,     8,     9,    10,    11,    12,    13,    14,    15,    16,
      17,    -1,    -1,    -1,    21,    22,    -1,    -1,    -1,    -1,
      28,    29,    30,    31,    32,    33,    34,    -1,    35,    -1,
      -1,    -1,    -1,    -1,    -1,    42,    -1,    -1,    -1,    46,
      47,    48,    -1,    -1,    -1,    -1,    -1,    54,    -1,    56,
      -1,    58,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    66,
      28,    29,    30,    31,    32,    33,    34,    -1,    -1,    -1,
      -1,    78,    80,    81,    -1,    83,    -1,    -1,    85,    -1,
      87,    -1,    90,    91,    92,    -1,    -1,    94,    95,    96,
      98,    99,   100,   101,   102,   103,    -1,   105,   106,   107,
     108,   109,   110,    -1,   112,   113,   114,   115,    28,    29,
      30,    31,    32,    33,    34,    83,    -1,    -1,    -1,    -1,
      -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,
      98,    99,   100,   101,   102,   103,    -1,   105,   106,   107,
     108,   109,   110,    -1,   112,   113,   114,   115,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    98,    -1,
     100,   101,   102,   103,    -1,   105,   106,   107,   108,   109,
     110,    -1,   112,   113,   114,   115,    28,    -1,    30,    31,
      32,    33,    34,    83,    -1,    -1,    -1,    -1,    -1,    -1,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   101,   102,   103,    -1,   105,   106,   107,   108,   109,
     110,    -1,   112,   113,   114,   115,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,
      92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   101,
     102,   103,    -1,   105,   106,   107,   108,   109,   110,    -1,
     112,   113,   114,   115
};

/* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
   symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,     3,    66,   133,   134,   135,   136,   143,     5,     4,
       5,    45,     0,   135,   118,   137,     5,     4,     5,    18,
      19,    20,    24,    25,    26,    45,    66,    82,    90,    91,
      92,   100,   101,   102,   110,   119,   128,   130,   131,   197,
     200,   202,   119,   119,   121,   138,   114,   119,   124,   126,
     193,   194,   119,   202,   202,   202,   202,   202,   202,   202,
     202,   106,   198,   199,   202,   202,   202,    28,    29,    30,
      31,    32,    33,    34,    83,    90,    91,    92,    98,   100,
     101,   102,   103,   105,   106,   107,   108,   109,   110,   112,
     113,   114,   115,     5,    47,   120,   161,   162,     5,     8,
       9,    10,   120,   139,   140,   195,     5,     7,    11,    12,
      13,    14,    15,    16,    17,    21,    22,    35,    42,    46,
      47,    48,    54,    56,    58,    78,    85,    87,    94,    95,
      96,   141,   142,   143,   144,   145,   146,   150,   151,   154,
     155,   156,   163,   170,   171,   180,   195,   196,     4,   189,
     202,     5,   200,   202,   193,   194,   202,   120,   197,   122,
     129,   197,   202,   202,   202,   202,   202,   202,   202,   202,
     202,   202,   202,   202,   202,   202,   202,   202,   202,   202,
     202,   202,   202,   202,   202,   202,   202,   202,   123,     5,
     126,   193,   120,   122,    12,    13,    16,    11,    12,    13,
      16,    12,   121,   120,   122,     5,    21,   193,     5,    27,
     118,   119,   169,     5,   118,   119,   147,   166,   184,   185,
     191,   197,   200,    16,    16,     5,   192,     5,     7,    11,
      21,    36,    38,    43,    44,    49,    50,    51,    55,    60,
      61,    75,    77,    88,    89,    93,    97,   118,   125,   175,
     179,   180,   181,   182,   183,   191,   200,     5,   119,     5,
     157,   158,   200,     5,    16,   159,   160,   193,   159,   193,
     175,   179,     5,    21,   149,   193,     5,    45,    36,    38,
      60,    87,   144,   145,   146,   154,   155,   156,   163,   170,
     172,   173,   174,     6,   141,   192,   193,     5,   169,   192,
     193,     5,   120,   122,   119,   193,   194,    80,    81,    99,
     127,   120,   199,    99,   202,   123,   202,     5,   162,    16,
     121,   140,   123,     5,     5,   193,   119,   121,   193,     5,
       4,     5,    82,   119,   189,     5,   193,   194,     4,     5,
      82,   119,    67,    68,    69,    70,    71,    72,    73,    74,
     148,   166,   191,   191,   121,   122,   123,   122,   121,   119,
     121,   191,   192,   193,   192,    37,    99,   179,   190,   119,
     202,     5,   119,   119,   119,   179,   119,   119,   190,     5,
     202,   202,   119,     5,   202,     5,    84,   113,   119,   121,
     179,    34,   123,   121,   119,   189,   121,   122,   123,   123,
     159,   193,   121,   122,   159,   193,   121,   159,   193,   119,
     121,     5,   193,   119,   121,    79,    99,   172,   119,   119,
       5,    86,   173,   121,   192,   193,     5,   192,   121,   123,
       5,   192,   193,   202,   202,   202,   202,   202,   202,   202,
     123,     4,    18,    19,    20,    24,    25,    26,    45,    82,
     201,   123,   193,     5,   120,   124,   164,   165,   189,   119,
       5,   120,   124,   167,   168,   189,   120,   119,   193,   193,
     194,   189,   122,   191,   123,   123,   185,   202,   192,   120,
     189,   123,   121,   192,   121,     5,    37,   179,   202,   121,
     121,   202,   202,   202,   184,   202,    76,   121,   123,   121,
     202,   121,   121,   179,    40,    41,   177,   178,   202,   166,
     202,   166,   202,   164,   189,   120,   157,   202,   202,   121,
     159,   160,   121,   159,   121,   159,   139,     8,     9,    11,
      21,    22,    23,   152,   153,   190,   119,   121,     5,   139,
     152,   179,     5,    37,   202,   184,   121,   121,   193,   121,
     123,   121,   202,   123,   193,   121,     5,   192,   120,   127,
     127,   127,   202,   201,   121,     5,   113,   120,   122,   120,
     164,   189,   121,     5,   120,   122,   120,   121,   120,   164,
     119,   120,   148,   123,   202,   202,   121,   120,   202,   121,
     190,   120,   120,   120,   120,   121,   120,   202,   120,   202,
     202,    42,   120,   122,   176,   202,   121,   202,   121,   120,
     120,   121,   121,   121,   121,   120,    21,   192,   193,    11,
     192,   193,   192,   192,   192,   153,   190,    57,   139,   152,
     179,   121,   120,   179,    59,   172,   120,   121,   121,   202,
     121,   202,   121,   123,   121,   119,   121,   165,   121,   120,
     120,   119,   168,   121,   120,   164,   120,   202,   121,   121,
     121,   121,    37,   179,    53,   186,   187,   188,   189,   186,
     186,   202,   179,   121,   179,   178,   121,   121,   121,   121,
     121,   192,   121,   193,   193,   193,   121,     5,   192,   193,
     121,   193,   121,   121,    57,   120,   179,    57,    11,    21,
     152,   121,    59,    37,   173,   202,   121,   121,   202,   120,
     202,   121,   121,   202,   121,   120,   121,    39,    99,    52,
     187,   188,    52,    99,    52,   188,    52,   188,   121,   152,
     179,   121,   121,   192,   193,   193,   121,     5,   121,   121,
      57,   192,   193,   192,   179,   152,   179,    39,   121,   121,
     120,   120,   121,   179,   121,   179,    52,   121,   179,    52,
      52,   184,   179,    57,   121,     5,   121,   121,   152,   179,
     121,   192,   121,    57,   179,    59,   173,   184,   120,    57,
     121,   179,    57,   121,    59,   120,   179,    57,   173
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
#line 3121 "y.tab.c"
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


#line 376 "yaccs/verilog.yacc"


