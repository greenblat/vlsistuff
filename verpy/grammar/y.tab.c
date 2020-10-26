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
#define YYLAST   5507

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  131
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  70
/* YYNRULES -- Number of rules.  */
#define YYNRULES  352
/* YYNRULES -- Number of states.  */
#define YYNSTATES  783

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
     579,   586,   592,   600,   609,   617,   621,   623,   626,   632,
     637,   642,   645,   648,   651,   655,   657,   663,   666,   671,
     674,   677,   680,   685,   689,   692,   696,   700,   703,   705,
     709,   715,   719,   721,   723,   725,   727,   729,   731,   733,
     735,   737,   743,   751,   761,   764,   767,   770,   775,   777,
     779,   783,   785,   788,   791,   793,   797,   800,   803,   809,
     813,   818,   824,   829,   835,   841,   849,   853,   857,   861,
     866,   870,   876,   879,   883,   887,   892,   898,   905,   913,
     920,   927,   935,   942,   950,   954,   958,   961,   963,   965,
     967,   970,   972,   978,   982,   992,   998,  1004,  1008,  1010,
    1014,  1017,  1019,  1023,  1027,  1031,  1035,  1039,  1041,  1044,
    1046,  1048,  1051,  1055,  1059,  1062,  1064,  1066,  1070,  1072,
    1078,  1084,  1090,  1094,  1096,  1098,  1100,  1103,  1106,  1109,
    1112,  1115,  1118,  1122,  1125,  1128,  1130,  1132,  1134,  1136,
    1138,  1140,  1143,  1146,  1148,  1150,  1152,  1154,  1156,  1160,
    1164,  1166,  1169,  1171,  1174,  1178,  1182,  1187,  1192,  1199,
    1201,  1203,  1205,  1207,  1209,  1211,  1213,  1215,  1217,  1219,
    1221,  1223,  1225,  1227,  1229,  1234,  1236,  1238,  1240,  1242,
    1244,  1246,  1249,  1253,  1257,  1260,  1266,  1270,  1274,  1278,
    1282,  1286,  1290,  1294,  1298,  1302,  1306,  1310,  1314,  1318,
    1322,  1326,  1330,  1334,  1338,  1342,  1346,  1350,  1354,  1358,
    1362,  1366,  1371,  1375,  1377,  1380,  1383,  1386,  1389,  1392,
    1395,  1398,  1401
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
       5,   191,   118,   163,   119,   120,    -1,   163,   121,   164,
      -1,   164,    -1,   123,   112,    -1,   123,     5,   118,   200,
     119,    -1,   123,     5,   118,   119,    -1,   117,   118,   187,
     119,    -1,   117,     4,    -1,   117,     5,    -1,   117,    81,
      -1,   166,   121,   167,    -1,   167,    -1,   123,     5,   118,
     200,   119,    -1,   123,     5,    -1,   117,   118,   187,   119,
      -1,   117,     4,    -1,   117,    81,    -1,   117,     5,    -1,
     117,   118,   166,   119,    -1,   117,   118,   119,    -1,    35,
     178,    -1,    35,   174,   178,    -1,    84,   171,    85,    -1,
     171,   172,    -1,   172,    -1,    36,   171,    37,    -1,    36,
      98,     5,   171,    37,    -1,    86,     5,   120,    -1,   144,
      -1,   145,    -1,   153,    -1,   154,    -1,   155,    -1,   162,
      -1,   173,    -1,   169,    -1,   143,    -1,    38,   118,   200,
     119,   172,    -1,    38,   118,   200,   119,   172,    39,   172,
      -1,    60,   118,   182,   120,   200,   120,   182,   119,   172,
      -1,   124,   112,    -1,   124,    83,    -1,   124,     5,    -1,
     124,   118,   176,   119,    -1,    42,    -1,   121,    -1,   176,
     175,   177,    -1,   177,    -1,    40,   200,    -1,    41,   200,
      -1,   200,    -1,    36,   188,    37,    -1,    36,    37,    -1,
      55,   178,    -1,    36,    98,     5,   188,    37,    -1,    75,
     188,    76,    -1,   189,   122,   200,   120,    -1,   189,   122,
     165,   200,   120,    -1,   189,    34,   200,   120,    -1,   189,
      34,   165,   200,   120,    -1,    38,   118,   200,   119,   178,
      -1,    38,   118,   200,   119,   178,    39,   178,    -1,    43,
     200,   120,    -1,    21,   190,   120,    -1,    11,   190,   120,
      -1,    11,   191,   190,   120,    -1,    88,   200,   120,    -1,
      87,   200,   122,   200,   120,    -1,   174,   120,    -1,    44,
       5,   120,    -1,    77,     5,   120,    -1,     5,   118,   119,
     120,    -1,     5,   118,   187,   119,   120,    -1,    49,   118,
     200,   119,   184,    52,    -1,    49,   118,   200,   119,   184,
     186,    52,    -1,    49,   118,   200,   119,   186,    52,    -1,
      50,   118,   200,   119,   184,    52,    -1,    50,   118,   200,
     119,   184,   186,    52,    -1,    51,   118,   200,   119,   184,
      52,    -1,    51,   118,   200,   119,   184,   186,    52,    -1,
     117,   200,   120,    -1,   117,   200,   178,    -1,     5,   120,
      -1,   179,    -1,   180,    -1,   181,    -1,   198,   120,    -1,
      78,    -1,     7,   189,   122,   200,   120,    -1,    96,     5,
     120,    -1,    60,   118,   182,   120,   200,   120,   182,   119,
     178,    -1,    92,   118,   200,   119,   178,    -1,    61,   118,
     200,   119,   178,    -1,   182,   121,   183,    -1,   183,    -1,
     189,   122,   200,    -1,   184,   185,    -1,   185,    -1,   187,
      98,   178,    -1,   187,    98,   120,    -1,    53,    98,   178,
      -1,    53,    98,   120,    -1,   187,   121,   200,    -1,   200,
      -1,   188,   178,    -1,   178,    -1,     5,    -1,     5,   191,
      -1,     5,   192,   191,    -1,     5,   192,   192,    -1,     5,
     192,    -1,   198,    -1,   195,    -1,     5,   121,   190,    -1,
       5,    -1,   125,   200,    98,   200,   126,    -1,   125,   200,
      79,   200,   126,    -1,   125,   200,    80,   200,   126,    -1,
     125,   200,   126,    -1,     8,    -1,     9,    -1,    10,    -1,
       9,    11,    -1,     8,    12,    -1,     9,    12,    -1,    10,
      12,    -1,     8,    16,    -1,     9,    16,    -1,     9,    11,
      16,    -1,     9,    13,    -1,     8,    13,    -1,    13,    -1,
      11,    -1,    12,    -1,    16,    -1,    21,    -1,    22,    -1,
      11,    16,    -1,    12,    16,    -1,    86,    -1,    93,    -1,
      94,    -1,    14,    -1,    15,    -1,   127,   196,   128,    -1,
     196,   121,   197,    -1,   197,    -1,   200,   195,    -1,   200,
      -1,   105,   195,    -1,     5,   123,   198,    -1,     5,   123,
       5,    -1,     5,   123,     5,   191,    -1,     5,   123,     5,
     192,    -1,     5,   123,     5,   118,   200,   119,    -1,     4,
      -1,    81,    -1,    45,    -1,    18,    -1,    19,    -1,    20,
      -1,    24,    -1,    25,    -1,    26,    -1,     5,    -1,   198,
      -1,     4,    -1,    81,    -1,    45,    -1,    66,    -1,    66,
     118,   200,   119,    -1,    18,    -1,    19,    -1,    20,    -1,
      24,    -1,    25,    -1,    26,    -1,     5,   191,    -1,     5,
     192,   191,    -1,     5,   192,   192,    -1,     5,   192,    -1,
     200,    97,   200,    98,   200,    -1,   200,   108,   200,    -1,
     200,   112,   200,    -1,   200,   109,   200,    -1,   200,   113,
     200,    -1,   200,   114,   200,    -1,   200,   100,   200,    -1,
     200,    99,   200,    -1,   200,   101,   200,    -1,   200,   106,
     200,    -1,   200,   107,   200,    -1,   200,    82,   200,    -1,
     200,    28,   200,    -1,   200,    29,   200,    -1,   200,    89,
     200,    -1,   200,    90,   200,    -1,   200,    91,   200,    -1,
     200,    31,   200,    -1,   200,    30,   200,    -1,   200,    32,
     200,    -1,   200,   111,   200,    -1,   200,    33,   200,    -1,
     200,    34,   200,    -1,   200,   105,   200,    -1,   200,   104,
     200,    -1,   200,   102,   200,    -1,     5,   118,   187,   119,
      -1,   118,   200,   119,    -1,   195,    -1,   109,   200,    -1,
      99,   200,    -1,   101,   200,    -1,   100,   200,    -1,    89,
     200,    -1,    91,   200,    -1,    90,   200,    -1,   129,   200,
      -1,   130,   200,    -1
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
     172,   173,   174,   175,   176,   184,   184,   185,   185,   185,
     187,   187,   187,   187,   188,   188,   189,   189,   190,   190,
     190,   190,   190,   190,   193,   193,   196,   198,   198,   201,
     202,   203,   204,   205,   206,   207,   208,   209,   210,   211,
     212,   213,   214,   219,   224,   224,   224,   224,   225,   225,
     226,   226,   227,   227,   227,   232,   233,   234,   235,   236,
     237,   238,   239,   240,   241,   242,   243,   244,   245,   246,
     247,   248,   249,   250,   251,   252,   253,   254,   255,   256,
     257,   258,   259,   260,   261,   262,   263,   264,   265,   266,
     267,   268,   269,   270,   273,   274,   275,   276,   276,   277,
     278,   278,   279,   279,   280,   280,   282,   282,   283,   283,
     286,   286,   286,   286,   286,   286,   286,   288,   288,   290,
     290,   290,   291,   293,   293,   293,   293,   293,   293,   293,
     293,   293,   293,   293,   293,   295,   295,   295,   295,   295,
     295,   295,   295,   295,   295,   295,   295,   295,   297,   298,
     298,   300,   301,   302,   306,   307,   308,   309,   310,   314,
     315,   316,   317,   317,   317,   317,   317,   317,   321,   322,
     323,   324,   325,   326,   327,   328,   328,   328,   328,   328,
     328,   329,   330,   331,   332,   333,   334,   335,   336,   337,
     338,   339,   340,   341,   342,   343,   344,   345,   346,   347,
     348,   349,   350,   351,   352,   353,   354,   355,   356,   357,
     358,   359,   360,   361,   362,   363,   364,   365,   366,   367,
     368,   369,   370
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
     162,   162,   162,   162,   162,   163,   163,   164,   164,   164,
     165,   165,   165,   165,   166,   166,   167,   167,   168,   168,
     168,   168,   168,   168,   169,   169,   170,   171,   171,   172,
     172,   172,   172,   172,   172,   172,   172,   172,   172,   172,
     172,   172,   172,   173,   174,   174,   174,   174,   175,   175,
     176,   176,   177,   177,   177,   178,   178,   178,   178,   178,
     178,   178,   178,   178,   178,   178,   178,   178,   178,   178,
     178,   178,   178,   178,   178,   178,   178,   178,   178,   178,
     178,   178,   178,   178,   178,   178,   178,   178,   178,   178,
     178,   178,   178,   178,   179,   180,   181,   182,   182,   183,
     184,   184,   185,   185,   186,   186,   187,   187,   188,   188,
     189,   189,   189,   189,   189,   189,   189,   190,   190,   191,
     191,   191,   192,   193,   193,   193,   193,   193,   193,   193,
     193,   193,   193,   193,   193,   194,   194,   194,   194,   194,
     194,   194,   194,   194,   194,   194,   194,   194,   195,   196,
     196,   197,   197,   197,   198,   198,   198,   198,   198,   199,
     199,   199,   199,   199,   199,   199,   199,   199,   200,   200,
     200,   200,   200,   200,   200,   200,   200,   200,   200,   200,
     200,   200,   200,   200,   200,   200,   200,   200,   200,   200,
     200,   200,   200,   200,   200,   200,   200,   200,   200,   200,
     200,   200,   200,   200,   200,   200,   200,   200,   200,   200,
     200,   200,   200,   200,   200,   200,   200,   200,   200,   200,
     200,   200,   200
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
       6,     5,     7,     8,     7,     3,     1,     2,     5,     4,
       4,     2,     2,     2,     3,     1,     5,     2,     4,     2,
       2,     2,     4,     3,     2,     3,     3,     2,     1,     3,
       5,     3,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     5,     7,     9,     2,     2,     2,     4,     1,     1,
       3,     1,     2,     2,     1,     3,     2,     2,     5,     3,
       4,     5,     4,     5,     5,     7,     3,     3,     3,     4,
       3,     5,     2,     3,     3,     4,     5,     6,     7,     6,
       6,     7,     6,     7,     3,     3,     2,     1,     1,     1,
       2,     1,     5,     3,     9,     5,     5,     3,     1,     3,
       2,     1,     3,     3,     3,     3,     3,     1,     2,     1,
       1,     2,     3,     3,     2,     1,     1,     3,     1,     5,
       5,     5,     3,     1,     1,     1,     2,     2,     2,     2,
       2,     2,     3,     2,     2,     1,     1,     1,     1,     1,
       1,     2,     2,     1,     1,     1,     1,     1,     3,     3,
       1,     2,     1,     2,     3,     3,     4,     4,     6,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     4,     1,     1,     1,     1,     1,
       1,     2,     3,     3,     2,     5,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     4,     3,     1,     2,     2,     2,     2,     2,     2,
       2,     2,     2
};

/* YYDEFACT[STATE-NAME] -- Default rule to reduce with in state
   STATE-NUM when YYTABLE doesn't specify something else to do.  Zero
   means the default is an error.  */
static const yytype_uint16 yydefact[] =
{
       0,     0,     0,     0,     2,     4,     5,     6,    10,     0,
      41,    40,     1,     3,     0,     0,     0,   300,   298,   305,
     306,   307,   308,   309,   310,   302,   303,   301,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   343,
     299,    42,     0,     0,    11,    25,     0,     0,     0,     0,
     311,   314,     0,   348,   350,   349,   345,   347,   346,   344,
       0,     0,     0,   280,   282,   351,   352,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     9,     0,   119,    21,   253,
     254,   255,     0,     0,    15,     0,     0,     0,   266,   267,
     265,   276,   277,   268,     0,   269,   270,     0,     0,     0,
       0,     0,     0,     0,     0,    38,     0,   273,   274,   275,
      39,     0,    25,    37,    34,    26,    27,    35,    36,    31,
      32,    33,    28,    29,    30,     0,     0,     0,     0,   237,
     285,   284,     0,   312,   313,     0,   342,   283,     0,   278,
     281,   327,   328,   333,   332,   334,   336,   337,   326,   329,
     330,   331,     0,   322,   321,   323,   340,   339,   338,   324,
     325,   316,   318,   335,   317,   319,   320,     0,     0,     0,
       0,     8,     0,   257,   264,   260,   256,   258,   263,   261,
     259,    13,     0,     0,    16,     0,     0,     0,     0,     0,
       0,     0,   240,     0,     0,     0,     0,     0,   228,     0,
     246,   245,   271,   272,   248,     0,   240,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   221,     0,     0,     0,     0,     0,     0,     0,
     154,   217,   218,   219,     0,   245,     0,     0,     0,   114,
       0,     0,     0,     0,     0,   116,     0,     0,     0,     0,
      44,     0,    74,     0,    73,     0,     0,     0,     0,   273,
     170,   162,   163,   164,   165,   166,   167,   169,     0,   158,
     168,     7,    24,     0,     0,   248,     0,     0,     0,    43,
     341,     0,     0,   286,   287,     0,     0,     0,   252,   304,
     279,     0,   122,     0,     0,     0,   118,   262,    12,    14,
       0,    18,    17,     0,     0,   125,     0,     0,   149,   151,
     150,     0,     0,     0,   241,   244,   141,   142,   143,     0,
      65,    66,    67,    68,    69,    70,    71,    72,     0,     0,
       0,     0,    60,     0,     0,     0,    46,     0,   216,     0,
       0,     0,     0,   186,     0,   239,     0,     0,     0,     0,
       0,     0,     0,   187,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   176,   175,   174,     0,   202,   155,     0,
       0,   220,     0,     0,   111,     0,     0,     0,     0,     0,
     103,     0,     0,     0,   108,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   156,   157,
      45,     0,     0,   248,     0,    47,     0,   248,     0,     0,
     236,     0,     0,     0,     0,   315,   120,     0,   289,   292,
     293,   294,   295,   296,   297,   291,   290,    22,     0,    19,
      20,     0,     0,     0,   136,     0,     0,     0,   153,     0,
       0,   145,     0,     0,     0,     0,   242,   243,     0,     0,
       0,     0,     0,   227,   229,   247,     0,     0,     0,   198,
       0,   197,     0,   185,   238,     0,   196,   203,     0,     0,
       0,     0,     0,   189,   204,     0,   200,     0,   223,   214,
     215,     0,     0,     0,   181,   184,     0,     0,     0,     0,
       0,     0,     0,   113,   112,   117,   104,     0,   115,   105,
       0,   109,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    89,     0,     0,     0,     0,     0,     0,     0,     0,
     159,     0,     0,   161,    49,     0,    56,     0,    57,     0,
       0,     0,    51,   248,     0,   288,   250,   251,   249,   121,
      23,   123,     0,   137,     0,     0,     0,     0,    59,   147,
     152,     0,   148,   131,     0,     0,     0,   140,     0,     0,
       0,     0,   205,     0,     0,   199,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   182,   183,   178,   177,   179,
       0,     0,   192,     0,   190,     0,     0,   126,   107,   106,
     110,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    88,     0,    76,     0,     0,     0,     0,     0,     0,
      85,     0,     0,     0,    50,     0,    48,     0,    53,     0,
      54,     0,   128,   135,   130,     0,     0,   144,   124,     0,
       0,    64,     0,    63,    61,   206,   222,   188,   194,     0,
       0,   231,     0,     0,     0,     0,     0,   226,   201,   225,
     180,   193,   191,   129,   127,     0,     0,    97,     0,     0,
       0,    90,   248,     0,     0,   101,     0,    91,    92,    75,
       0,     0,    79,     0,     0,     0,     0,    84,   160,   171,
       0,    58,    52,     0,   139,     0,   134,     0,   132,     0,
      62,     0,     0,   207,   230,     0,   209,     0,   210,     0,
     212,     0,     0,     0,     0,   100,    98,     0,     0,     0,
      93,     0,   102,     0,    78,     0,     0,     0,     0,     0,
       0,     0,     0,    55,   138,   146,   133,   195,   235,   234,
     208,   233,   232,   211,   213,     0,     0,    80,    99,     0,
      94,    95,     0,     0,    90,     0,   101,    77,     0,    86,
     172,     0,     0,    81,    96,     0,    82,    93,    87,     0,
     224,    83,   173
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,     3,     4,     5,     6,    15,    45,   103,   104,   131,
     132,     7,   280,   281,   282,   215,   348,   273,   137,   138,
     530,   531,   283,   284,   285,   259,   260,   264,   265,    96,
      97,   286,   453,   454,   216,   460,   461,   211,   287,   144,
     288,   289,   290,   269,   600,   503,   504,   365,   251,   252,
     253,   217,   218,   660,   661,   662,   663,   366,   254,   225,
     334,   335,   145,   146,    39,    62,    63,    40,   447,   149
};

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
#define YYPACT_NINF -521
static const yytype_int16 yypact[] =
{
      53,    47,    63,    64,    53,  -521,  -521,  -521,   -41,    83,
    1811,  -521,  -521,  -521,   -17,    73,    65,  -521,   -46,  -521,
    -521,  -521,  -521,  -521,  -521,  -521,    76,  -521,  1811,  1811,
    1811,  1811,  1811,  1811,  1811,  1811,  1454,  1811,  1811,  -521,
    -521,  5301,    43,    52,  -521,  4894,   133,  1811,   156,  1811,
    -521,    82,  1811,  -521,  -521,  -521,  -521,  -521,  -521,  -521,
    4064,    96,   -58,  -521,  2712,  -521,  -521,  1811,  1811,  1811,
    1811,  1811,  1811,  1811,  1811,  1811,  1811,  1811,  1811,  1811,
    1811,  1811,  1811,  1811,  1811,  1811,  1811,  1811,  1811,  1811,
    1811,  1811,  1811,    93,     6,  -521,    95,  -521,  -521,   147,
     249,   239,   139,   157,  -521,    23,    70,     7,   247,   250,
    -521,  -521,  -521,  -521,   287,  -521,  -521,  2673,    29,   292,
      24,    25,  2673,    26,   298,  -521,  5147,  -521,  -521,  -521,
    -521,   278,  4894,  -521,  -521,  -521,  -521,  -521,  -521,  -521,
    -521,  -521,  -521,  -521,  -521,    30,    27,   344,   161,  5301,
     -29,  -521,  2751,  -521,  -521,  4156,  -521,  -521,  1454,  -521,
    -521,  1264,  5393,   120,   120,   120,   399,   399,  -521,   446,
     446,   446,  5214,  5329,   446,  2804,   624,   624,   624,   399,
     399,   208,   208,   120,  -521,  -521,  -521,  1811,   188,  1811,
     357,  -521,    34,  -521,  -521,  -521,   341,  -521,  -521,  -521,
    -521,  -521,   245,   331,   248,   381,    31,    92,   405,    21,
    1811,   414,   112,    46,   323,    16,    19,   123,  -521,   306,
    -521,  -521,  -521,  -521,   222,   303,   -40,    19,    30,   287,
    2089,   289,  1811,   427,   322,   333,   346,  2673,   365,   372,
    2673,   461,  -521,  1811,  1811,   376,   465,  1811,    87,  2154,
    -521,  -521,  -521,  -521,   -16,   378,   388,  1811,   362,  -521,
     212,   374,   396,    25,   327,  -521,    25,   342,    25,   389,
    -521,   175,  -521,   521,   411,   184,   367,   417,   419,   524,
    -521,  -521,  -521,  -521,  -521,  -521,  -521,  -521,  4985,  -521,
    -521,  -521,  -521,   420,   287,   -21,   537,   187,    32,  -521,
    -521,  1811,  1811,  -521,  -521,  1811,  1811,  1811,  -521,  -521,
    -521,  1811,  5301,  1811,  5180,   421,  -521,  -521,  -521,  -521,
     202,  -521,   -13,   540,   865,  -521,   431,   551,  -521,  -521,
    -521,   923,   192,   -27,  -521,    82,  -521,  -521,  -521,  1811,
    -521,  -521,  -521,  -521,  -521,  -521,  -521,  -521,   440,    19,
     441,   442,  -521,    19,  1811,   287,  -521,  1504,  -521,   443,
     447,   287,   448,  -521,   557,  -521,  2215,  1811,  3068,   449,
    1811,  1811,  1811,  -521,    19,  1811,  2280,   450,  2981,  3096,
    1811,   451,  1914,  -521,  -521,  -521,  1085,  -521,  -521,  1572,
    1572,  -521,  1622,   195,  -521,   292,  1811,  1811,   348,   561,
    -521,   561,   352,   561,  -521,   380,   561,   331,  2028,   209,
     567,   331,  2028,   568,  5039,  1811,    19,   455,  -521,  -521,
    -521,    -4,   458,   366,   459,  -521,  1811,   -67,   463,   576,
    5301,  4189,  2838,  2866,  2953,  5301,  5301,  1811,  -521,  -521,
    -521,  -521,  -521,  -521,  -521,  -521,  -521,  -521,   202,  -521,
    -521,   464,    18,   223,  -521,   229,   462,   466,  -521,   582,
     233,  -521,   234,   468,    -1,   472,  -521,  -521,   237,   323,
     470,  1811,  1811,  -521,  5301,  -521,   474,   242,  1811,  -521,
     475,  -521,  2673,  -521,  -521,  4281,  -521,  -521,  4314,  4406,
    4439,   382,  4531,  -521,  -521,  1811,  -521,  4564,  -521,  -521,
    -521,  1811,  1811,    90,  -521,  5301,  1811,  3189,  1811,  3217,
     266,   279,   477,  -521,  5301,  5301,  -521,   384,  -521,  -521,
     400,  -521,   402,   280,    28,   587,    30,   287,   287,   287,
    2028,  -521,  2339,   331,  2028,   479,   285,  2028,   543,  5147,
    -521,  4656,   404,  -521,  -521,   486,  -521,  1811,  -521,  3310,
    1811,   489,  -521,   410,   490,  -521,  -521,  -521,  -521,  5301,
    -521,  -521,   493,  -521,   492,   462,   494,   297,  -521,   495,
    -521,   496,  -521,  -521,   498,   301,   462,  -521,   501,  1811,
    3338,  3431,  -521,   503,  3459,  -521,  2404,  2673,  1690,  1811,
    1811,  1811,  2673,  3552,  2673,  5301,  5301,  -521,  -521,  -521,
    1085,  3580,  -521,  3673,  -521,   504,   505,  -521,  -521,  -521,
    -521,   506,   287,    88,   411,   411,   509,    33,   116,   510,
     511,  -521,  2463,  -521,   305,  2028,   558,   246,   512,   574,
    -521,  5093,  5147,  1811,  -521,  3701,  -521,  3794,  -521,  1811,
    -521,  1743,  -521,  -521,  -521,   514,  1811,  -521,  -521,   515,
     317,  -521,  3822,  -521,  -521,  -521,  -521,  -521,   597,   539,
    1202,  -521,   588,   -55,  1336,  1386,  3915,  -521,  -521,  -521,
    -521,  -521,  -521,  -521,  -521,  2028,   519,  -521,   522,   287,
     411,   386,   -21,   523,   644,   387,   532,  -521,  -521,  -521,
     541,   602,  -521,    30,   287,  2028,  2028,  -521,  -521,   621,
    3943,  -521,  -521,  4036,  -521,  4689,  -521,  4781,  -521,   542,
    -521,  2673,  2522,  -521,  -521,   613,  -521,  2612,  -521,   614,
    -521,   616,    19,  2028,   619,  -521,  -521,   553,   666,   559,
     395,   560,  -521,  2028,  -521,   562,    33,   152,   629,  2028,
     628,  5147,    19,  -521,  -521,  -521,  -521,  -521,  -521,  -521,
    -521,  -521,  -521,  -521,  -521,   337,   631,  -521,  -521,   569,
    -521,  -521,  2028,   633,  -521,   572,  -521,  -521,   634,  -521,
    -521,   338,  2673,  -521,  -521,   638,  -521,  -521,  -521,  5147,
    -521,  -521,  -521
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -521,  -521,  -521,   674,  -521,  -521,  -521,  -392,   497,   564,
    -521,   -25,    -3,    37,    41,  -521,   228,  -521,  -521,  -521,
    -396,  -520,    42,    48,    54,   304,  -521,   -68,   300,  -521,
     513,    58,  -391,   137,  -206,  -521,   127,   563,    72,  -521,
    -269,  -286,  -521,   586,  -521,  -521,   104,   -95,  -521,  -521,
    -521,  -371,   354,   -56,  -435,  -415,   -33,  -236,  -101,   221,
     -10,    -5,   -38,  -521,    59,  -521,   550,   -48,   262,   774
};

/* YYTABLE[YYPACT[STATE-NUM]].  What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule which
   number is the opposite.  If zero, do what YYDEFACT says.
   If YYTABLE_NINF, syntax error.  */
#define YYTABLE_NINF -200
static const yytype_int16 yytable[] =
{
     151,   510,   419,   491,   376,   105,   219,   414,    50,   349,
     621,   188,   212,    51,   148,   523,   537,   621,   389,   536,
     133,   212,   250,   562,   212,   328,   329,   270,   204,   262,
     262,   271,   295,   224,   256,   224,   322,   427,   682,    93,
     263,   153,   134,   717,   205,   542,   154,   272,    93,   612,
     336,   337,     8,   267,   355,   550,     1,    98,   189,   221,
      99,   100,   101,   158,    12,   567,   301,     9,    10,   255,
     159,   261,    47,   575,   255,   207,    14,    48,   357,    49,
     358,    94,   135,    48,   190,    49,   136,   139,    16,   302,
      94,   464,   383,   140,    48,   206,    49,   208,   189,   141,
     355,    42,   330,   142,   189,   621,   390,   133,    11,   448,
     266,   268,   189,   274,   350,   351,   544,   143,   574,     2,
     157,   189,   452,   160,   213,   214,   359,   338,   419,   134,
     563,   189,   597,   213,    36,   294,   298,   147,   625,   331,
     303,   624,   373,    36,   209,   304,    36,   257,   189,   189,
     189,   189,   189,   189,   388,   189,   189,   189,   189,   193,
     194,   150,    95,   195,   339,   105,   220,   221,   221,   135,
     384,   102,   532,   136,   139,   621,   220,   332,    46,   221,
     140,   220,   255,   506,   508,   650,   141,   209,   210,   255,
     142,    43,   255,    44,    52,   398,   323,   326,   402,   385,
     405,   255,    74,   621,   143,   386,   438,    49,   677,   598,
     324,   599,   325,   189,   191,   187,   192,   189,   361,   621,
     439,   440,   441,    36,   393,   714,   442,   443,   444,   714,
     714,   695,    90,    91,    92,    48,   685,    49,    69,    70,
      71,   189,   621,   352,   353,   715,   586,   445,   470,   719,
     721,   200,   219,   399,   524,   525,   403,   693,   406,   201,
     196,   197,   198,   222,   410,   199,   223,   694,   528,   529,
     631,   484,   766,   219,   220,   220,   202,   189,   203,   723,
     300,   484,   301,   446,   291,   422,   220,   500,   429,   220,
      74,   455,   224,   407,   622,   408,   220,   258,   462,   220,
     739,   221,   411,   275,   412,   221,   468,   425,   220,   426,
     313,   463,   449,   301,   512,   219,   301,   538,   255,    89,
      90,    91,    92,   465,   477,   466,   221,   533,   255,   534,
     467,   517,   394,   395,   255,   520,    98,   762,   522,    99,
     100,   101,   564,   355,   565,   419,   699,   261,   566,   299,
     301,   755,   570,   572,   571,   301,   577,   317,   301,   511,
     255,   583,   315,   301,   255,   318,   293,   297,   221,   105,
     320,   771,   106,   105,   107,    99,   100,   101,   108,   109,
     110,   111,   112,   113,   114,   605,   321,   565,   115,   116,
     340,   341,   342,   343,   344,   345,   346,   347,   606,   611,
     301,   203,   117,   276,   628,   277,   203,   367,   220,   118,
     327,   545,   220,   119,   120,   121,   645,   551,   565,   333,
     649,   122,   565,   356,   690,   220,   203,   278,   354,    69,
      70,    71,   369,   220,   255,   220,   709,   484,   565,   626,
     370,   220,   629,  -198,  -197,  -198,  -197,   400,   401,   360,
     362,   371,  -199,   279,  -199,   770,   772,   779,   353,   353,
     128,   129,   404,   401,   372,   413,   377,   220,   516,   401,
     381,   220,   519,   401,    67,   220,    69,    70,    71,    72,
      73,    74,   255,   374,   255,    48,   255,   355,   547,   255,
     375,   484,   658,   782,   380,   105,   396,   667,   391,   669,
     521,   401,   591,   353,   608,   401,   392,    87,    88,   387,
      89,    90,    91,    92,   614,   421,   617,   424,   397,   428,
     609,   401,   610,   401,   633,   353,   409,   484,    74,   417,
     691,   355,   639,   664,   665,   415,   189,   416,   255,   255,
     420,   220,   423,   437,   255,   450,   255,    81,    82,   456,
      83,    84,    85,    86,    87,    88,   457,    89,    90,    91,
      92,   469,   482,   471,   472,   478,   262,   479,   481,   487,
     494,   498,   535,   539,   255,   543,   475,   255,   546,   548,
     724,   553,   480,   552,   561,   452,   568,   569,   573,   220,
     576,   220,   579,   220,   582,   585,   220,   607,   615,   627,
     738,   740,   630,   678,   679,   680,   634,   684,   686,   638,
     640,   641,   642,   646,   644,   692,   747,   749,   648,   459,
     651,   219,   752,   655,   673,   674,   675,   255,   756,   681,
     687,   688,   696,   697,   706,   708,   711,   712,   763,   725,
     716,   219,   726,   730,   768,   220,   220,   255,   255,   731,
     554,   220,   732,   220,    69,    70,    71,    72,    73,   734,
     741,   733,   746,   255,   255,   750,   753,   775,   754,   255,
     728,   759,   729,   758,   221,   255,   757,   780,    13,   760,
     761,   220,   764,   736,   220,   255,   767,   769,   773,   774,
     776,   255,   777,   778,   221,   781,   292,   578,   647,   513,
     319,   518,   643,   249,   670,   316,    74,   473,   310,   296,
     560,     0,     0,     0,   255,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   255,     0,   684,   686,     0,     0,
      85,    86,    87,    88,   220,    89,    90,    91,    92,     0,
       0,     0,     0,     0,     0,   613,     0,   616,   618,   619,
     620,     0,     0,     0,   220,   220,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     220,   220,     0,     0,     0,     0,   220,     0,     0,     0,
       0,   220,   220,     0,    41,     0,     0,     0,     0,     0,
       0,     0,   220,     0,     0,     0,     0,     0,   220,     0,
       0,   220,    53,    54,    55,    56,    57,    58,    59,    60,
      64,    65,    66,     0,     0,     0,     0,     0,     0,     0,
       0,   220,     0,   152,     0,     0,   155,     0,     0,     0,
       0,   220,     0,   676,     0,     0,     0,     0,   683,     0,
       0,   161,   162,   163,   164,   165,   166,   167,   168,   169,
     170,   171,   172,   173,   174,   175,   176,   177,   178,   179,
     180,   181,   182,   183,   184,   185,   186,     0,     0,    17,
      18,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    19,    20,    21,     0,     0,     0,    22,
      23,    24,     0,     0,     0,     0,     0,     0,     0,     0,
     727,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      25,     0,     0,     0,   735,   737,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    17,    18,     0,
       0,    26,    64,     0,     0,     0,     0,     0,     0,     0,
       0,    19,    20,    21,     0,     0,    27,    22,    23,    24,
       0,     0,     0,     0,    28,    29,    30,   765,     0,     0,
       0,   312,     0,   314,    31,    32,    33,     0,    25,     0,
       0,     0,     0,     0,    34,     0,     0,     0,     0,     0,
       0,     0,     0,    35,   451,     0,     0,     0,   452,    26,
       0,     0,    36,     0,    37,    38,     0,     0,     0,     0,
       0,     0,     0,     0,    27,     0,   368,     0,     0,     0,
       0,     0,    28,    29,    30,     0,     0,   378,   379,     0,
       0,   382,    31,    32,    33,     0,     0,     0,     0,     0,
       0,     0,    34,     0,     0,     0,     0,     0,     0,     0,
       0,    35,   458,     0,     0,     0,   459,     0,     0,     0,
      36,     0,    37,    38,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   430,   431,     0,     0,   432,
     433,   434,     0,     0,     0,   435,     0,   436,     0,    17,
      18,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    19,    20,    21,     0,     0,     0,    22,
      23,    24,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   501,   502,     0,   474,     0,
      25,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   485,     0,     0,   488,   489,   490,     0,     0,   492,
       0,    26,     0,     0,   497,     0,     0,     0,     0,     0,
     505,     0,     0,   507,   509,     0,    27,     0,     0,     0,
     514,   515,     0,     0,    28,    29,    30,     0,     0,     0,
       0,     0,     0,     0,    31,    32,    33,     0,     0,   541,
       0,     0,     0,     0,    34,     0,     0,     0,     0,     0,
     549,     0,     0,    35,     0,     0,    17,    18,     0,     0,
       0,   559,    36,     0,    37,    38,     0,     0,     0,     0,
      19,    20,    21,     0,     0,     0,    22,    23,    24,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   580,   581,    25,     0,     0,
       0,     0,   584,     0,   713,   659,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    26,   593,
       0,     0,     0,     0,     0,   595,   596,     0,     0,     0,
     601,     0,   603,    27,     0,     0,     0,     0,     0,     0,
       0,    28,    29,    30,    69,    70,    71,    72,    73,     0,
       0,    31,    32,    33,     0,     0,     0,     0,     0,     0,
       0,    34,     0,     0,     0,     0,     0,     0,     0,     0,
      35,   635,     0,     0,   637,     0,     0,     0,     0,    36,
       0,    37,    38,     0,     0,     0,     0,     0,     0,     0,
      17,    18,     0,     0,     0,     0,    74,     0,     0,     0,
       0,     0,     0,   652,    19,    20,    21,     0,     0,     0,
      22,    23,    24,     0,     0,   666,    82,     0,    83,    84,
      85,    86,    87,    88,   505,    89,    90,    91,    92,     0,
       0,    25,     0,     0,     0,     0,     0,     0,   718,   659,
      17,    18,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    26,     0,    19,    20,    21,   700,     0,     0,
      22,    23,    24,   703,     0,   705,     0,    27,     0,     0,
     707,     0,     0,     0,     0,    28,    29,    30,     0,     0,
       0,    25,     0,     0,     0,    31,    32,    33,   720,   659,
       0,     0,     0,     0,     0,    34,     0,     0,     0,     0,
       0,     0,    26,     0,    35,     0,     0,     0,    17,    18,
       0,     0,     0,    36,     0,    37,    38,    27,     0,     0,
       0,     0,    19,    20,    21,    28,    29,    30,    22,    23,
      24,     0,     0,     0,     0,    31,    32,    33,     0,     0,
       0,     0,     0,     0,     0,    34,     0,     0,     0,    25,
       0,     0,     0,     0,    35,     0,     0,     0,    17,    18,
       0,     0,     0,    36,     0,    37,    38,     0,     0,     0,
      26,     0,    19,    20,    21,     0,     0,     0,    22,    23,
      24,     0,     0,     0,     0,    27,     0,     0,     0,     0,
       0,     0,     0,    28,    29,    30,     0,     0,     0,    25,
       0,     0,     0,    31,    32,    33,     0,     0,     0,    61,
       0,     0,     0,    34,     0,     0,     0,     0,     0,     0,
      26,     0,    35,     0,     0,     0,    17,    18,     0,     0,
       0,    36,     0,    37,    38,    27,     0,     0,     0,     0,
      19,    20,    21,    28,    29,    30,    22,    23,    24,     0,
       0,     0,     0,    31,    32,    33,     0,     0,     0,     0,
       0,     0,     0,    34,     0,     0,     0,    25,     0,     0,
       0,     0,    35,   476,     0,     0,    17,    18,     0,     0,
       0,    36,     0,    37,    38,     0,     0,     0,    26,     0,
      19,    20,    21,     0,     0,     0,    22,    23,    24,     0,
       0,     0,     0,    27,     0,     0,     0,     0,     0,     0,
       0,    28,    29,    30,     0,     0,     0,    25,     0,     0,
       0,    31,    32,    33,     0,     0,     0,     0,     0,     0,
       0,    34,     0,     0,     0,     0,     0,     0,    26,   213,
      35,     0,     0,     0,    17,    18,     0,     0,     0,    36,
       0,    37,    38,    27,     0,     0,     0,     0,    19,    20,
      21,    28,    29,    30,    22,    23,    24,     0,     0,     0,
       0,    31,    32,    33,     0,     0,     0,     0,     0,     0,
       0,    34,     0,     0,     0,    25,     0,     0,     0,     0,
      35,     0,     0,   659,     0,   452,     0,    17,    18,    36,
       0,    37,    38,     0,     0,     0,    26,     0,     0,     0,
       0,    19,    20,    21,     0,     0,     0,    22,    23,    24,
       0,    27,     0,     0,     0,     0,     0,     0,     0,    28,
      29,    30,     0,     0,     0,     0,     0,     0,    25,    31,
      32,    33,     0,     0,     0,     0,     0,     0,     0,    34,
       0,     0,     0,     0,     0,     0,     0,     0,    35,    26,
       0,     0,     0,     0,     0,    17,    18,    36,     0,    37,
      38,     0,     0,     0,    27,     0,     0,     0,     0,    19,
      20,    21,    28,    29,    30,    22,    23,    24,     0,     0,
       0,     0,    31,    32,    33,     0,     0,     0,     0,     0,
       0,     0,    34,     0,     0,     0,    25,     0,     0,     0,
       0,    35,   704,     0,     0,     0,     0,     0,     0,     0,
      36,     0,    37,    38,     0,     0,     0,    26,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    27,     0,     0,     0,     0,     0,     0,     0,
      28,    29,    30,     0,     0,     0,     0,     0,     0,     0,
      31,    32,    33,     0,     0,     0,     0,     0,     0,   226,
      34,   227,     0,     0,     0,   228,     0,     0,     0,    35,
       0,     0,     0,     0,     0,   229,     0,     0,    36,     0,
      37,    38,    67,    68,    69,    70,    71,    72,    73,     0,
     230,     0,   231,     0,     0,     0,     0,   232,   233,     0,
       0,     0,     0,   234,   235,   236,     0,     0,     0,   237,
       0,     0,     0,     0,   238,   239,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   240,
       0,   241,   242,     0,     0,     0,    74,     0,     0,     0,
       0,   243,   244,    75,    76,    77,   245,     0,     0,     0,
     246,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,   247,     0,   226,   499,   227,   524,   525,   248,   526,
       0,    36,     0,     0,     0,     0,     0,     0,     0,   527,
     528,   529,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   230,     0,   231,     0,     0,     0,
       0,   232,   233,     0,     0,     0,     0,   234,   235,   236,
       0,     0,     0,   237,     0,     0,     0,     0,   238,   239,
       0,     0,     0,     0,   226,     0,   227,     0,     0,     0,
     228,     0,     0,   240,     0,   241,   242,     0,     0,     0,
     229,     0,     0,     0,     0,   243,   244,     0,     0,     0,
     245,     0,     0,     0,   246,   230,   363,   231,     0,     0,
       0,     0,   232,   233,     0,     0,     0,     0,   234,   235,
     236,     0,     0,     0,   237,   247,     0,     0,     0,   238,
     239,     0,   248,     0,     0,    36,     0,     0,     0,   226,
       0,   227,     0,     0,   240,   228,   241,   242,     0,     0,
       0,     0,     0,     0,     0,   229,   243,   244,     0,     0,
       0,   245,     0,     0,     0,   246,     0,   364,     0,     0,
     230,     0,   231,     0,     0,     0,     0,   232,   233,     0,
       0,     0,     0,   234,   235,   236,   247,     0,     0,   237,
       0,     0,     0,   248,   238,   239,    36,     0,     0,     0,
     226,     0,   227,     0,     0,     0,   228,     0,     0,   240,
       0,   241,   242,     0,     0,     0,   229,     0,     0,     0,
       0,   243,   244,     0,     0,     0,   245,     0,     0,     0,
     246,   230,   483,   231,     0,     0,     0,     0,   232,   233,
       0,     0,     0,     0,   234,   235,   236,     0,     0,     0,
     237,   247,     0,     0,   387,   238,   239,     0,   248,     0,
       0,    36,     0,     0,     0,   226,     0,   227,     0,     0,
     240,   228,   241,   242,     0,     0,     0,     0,     0,     0,
       0,   229,   243,   244,     0,     0,     0,   245,     0,     0,
       0,   246,     0,     0,     0,     0,   230,     0,   231,     0,
       0,     0,     0,   232,   233,     0,     0,     0,     0,   234,
     235,   236,   247,     0,     0,   237,     0,     0,     0,   248,
     238,   239,    36,     0,   226,     0,   227,     0,     0,     0,
     228,     0,     0,     0,     0,   240,   493,   241,   242,     0,
     229,     0,     0,     0,     0,     0,     0,   243,   244,     0,
       0,     0,   245,     0,     0,   230,   246,   231,     0,     0,
       0,     0,   232,   233,     0,     0,     0,     0,   234,   235,
     236,     0,     0,     0,   237,     0,   623,   247,     0,   238,
     239,     0,     0,     0,   248,     0,     0,    36,     0,   226,
       0,   227,     0,     0,   240,   228,   241,   242,     0,     0,
       0,     0,     0,     0,     0,   229,   243,   244,     0,     0,
       0,   245,     0,     0,     0,   246,     0,     0,     0,     0,
     230,   657,   231,     0,     0,     0,     0,   232,   233,     0,
       0,     0,     0,   234,   235,   236,   247,     0,     0,   237,
       0,     0,     0,   248,   238,   239,    36,     0,   226,     0,
     227,     0,     0,     0,   228,     0,     0,     0,     0,   240,
       0,   241,   242,     0,   229,     0,     0,     0,     0,     0,
       0,   243,   244,     0,     0,     0,   245,     0,     0,   230,
     246,   231,     0,     0,     0,     0,   232,   233,     0,     0,
       0,     0,   234,   235,   236,     0,     0,     0,   237,     0,
     689,   247,     0,   238,   239,     0,     0,   226,   248,   227,
       0,    36,     0,   228,     0,     0,     0,     0,   240,     0,
     241,   242,     0,   229,     0,     0,     0,     0,     0,     0,
     243,   244,     0,     0,     0,   245,     0,     0,   230,   246,
     231,     0,     0,     0,     0,   232,   233,     0,     0,     0,
       0,   234,   235,   236,     0,     0,     0,   237,     0,     0,
     247,     0,   238,   239,     0,     0,     0,   248,     0,     0,
      36,     0,     0,     0,     0,     0,     0,   240,     0,   241,
     242,     0,     0,     0,     0,     0,     0,     0,     0,   243,
     244,     0,     0,     0,   245,     0,     0,   226,   246,   227,
       0,     0,     0,   228,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   229,     0,     0,     0,     0,     0,   247,
       0,     0,   748,     0,     0,     0,   248,     0,   230,    36,
     231,     0,     0,     0,     0,   232,   233,     0,     0,     0,
       0,   234,   235,   236,     0,     0,     0,   237,     0,     0,
       0,     0,   238,   239,     0,     0,     0,     0,   226,     0,
     227,     0,     0,     0,   228,     0,     0,   240,     0,   241,
     242,     0,     0,     0,   229,     0,     0,     0,     0,   243,
     244,     0,     0,     0,   245,     0,     0,     0,   246,   230,
       0,   231,     0,     0,     0,     0,   232,   233,     0,     0,
       0,     0,   234,   235,   236,     0,     0,     0,   237,   247,
       0,     0,   751,   238,   239,     0,   248,     0,     0,    36,
      67,    68,    69,    70,    71,    72,    73,     0,   240,     0,
     241,   242,     0,     0,     0,     0,     0,     0,     0,     0,
     243,   244,     0,     0,     0,   245,     0,     0,     0,   246,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
     247,     0,     0,     0,    74,     0,     0,   248,     0,     0,
      36,    75,    76,    77,     0,     0,     0,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,     0,
     305,   306,    67,    74,    69,    70,    71,    72,    73,    36,
      75,    76,    77,     0,     0,     0,     0,     0,    78,   307,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,   308,     0,     0,
       0,     0,     0,     0,     0,     0,    74,     0,     0,     0,
       0,     0,     0,     0,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
      74,     0,     0,     0,     0,     0,     0,    75,    76,    77,
       0,     0,     0,     0,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,    74,    89,
      90,    91,    92,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,    78,   556,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,   557,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    74,     0,     0,     0,     0,
       0,     0,    75,    76,    77,     0,     0,     0,     0,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,    74,    89,    90,    91,    92,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,    78,   558,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,    67,    68,    69,    70,
      71,    72,    73,   495,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      74,     0,     0,     0,     0,     0,     0,    75,    76,    77,
       0,     0,     0,     0,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,    74,    89,
      90,    91,    92,     0,     0,    75,    76,    77,   486,     0,
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
      89,    90,    91,    92,     0,     0,    75,    76,    77,   602,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,     0,     0,     0,     0,     0,   604,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    74,     0,     0,     0,     0,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
      74,    89,    90,    91,    92,     0,     0,    75,    76,    77,
     636,     0,     0,     0,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,     0,     0,     0,     0,     0,   653,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,    74,    89,    90,    91,    92,     0,     0,    75,    76,
      77,   654,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,     0,   656,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    74,     0,     0,     0,     0,     0,
       0,    75,    76,    77,     0,     0,     0,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,    74,    89,    90,    91,    92,     0,     0,    75,
      76,    77,   668,     0,     0,     0,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,     0,     0,     0,     0,     0,
     671,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    74,     0,     0,     0,     0,
       0,     0,    75,    76,    77,     0,     0,     0,     0,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,    74,    89,    90,    91,    92,     0,     0,
      75,    76,    77,   672,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,     0,     0,     0,     0,
       0,   701,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    74,     0,     0,     0,
       0,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,    74,    89,    90,    91,    92,     0,
       0,    75,    76,    77,   702,     0,     0,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,     0,
       0,     0,   710,    67,    68,    69,    70,    71,    72,    73,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    74,     0,     0,
       0,     0,     0,     0,    75,    76,    77,     0,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,    74,    89,    90,    91,    92,
       0,     0,    75,    76,    77,   722,     0,     0,     0,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,     0,     0,
       0,     0,     0,   742,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,    74,    89,    90,    91,
      92,     0,     0,    75,    76,    77,   743,     0,     0,     0,
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
     587,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,   588,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,    74,     0,     0,     0,   589,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,   590,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,    74,     0,     0,     0,
     592,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,   594,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,    74,     0,     0,     0,   632,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,   744,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,     0,     0,     0,   106,
     745,   107,    99,   100,   101,   108,   109,   110,   111,   112,
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
     698,   277,   128,   129,     0,   118,     0,     0,     0,   119,
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
      48,   392,   288,   374,   240,    43,   107,   276,    18,   215,
     530,     5,     5,    18,    47,   407,   412,   537,    34,   411,
      45,     5,   117,     5,     5,     4,     5,   122,     5,     5,
       5,     5,     5,     5,     5,     5,     5,     5,     5,     5,
      16,    51,    45,    98,    21,   416,    51,    21,     5,    21,
       4,     5,     5,   121,   121,   122,     3,     5,   125,   107,
       8,     9,    10,   121,     0,   456,   121,     4,     5,   117,
     128,   119,   118,   464,   122,     5,   117,   123,   118,   125,
     120,    47,    45,   123,    94,   125,    45,    45,     5,   118,
      47,   118,     5,    45,   123,   105,   125,    27,   125,    45,
     121,   118,    81,    45,   125,   625,   122,   132,    45,   122,
     120,   121,   125,   123,   215,   216,   120,    45,   119,    66,
      61,   125,   123,    64,   117,   118,   227,    81,   414,   132,
     112,   125,    42,   117,   127,   145,   146,     4,   534,   118,
     150,   533,   237,   127,   117,   150,   127,   118,   125,   125,
     125,   125,   125,   125,   249,   125,   125,   125,   125,    12,
      13,     5,   119,    16,   118,   203,   107,   215,   216,   132,
      83,   119,   408,   132,   132,   695,   117,   210,   113,   227,
     132,   122,   230,   389,   390,   576,   132,   117,   118,   237,
     132,   118,   240,   120,   118,   263,   206,   207,   266,   112,
     268,   249,    82,   723,   132,   118,     4,   125,   120,   119,
     118,   121,   120,   125,   119,   122,   121,   125,   228,   739,
      18,    19,    20,   127,   257,   660,    24,    25,    26,   664,
     665,   627,   112,   113,   114,   123,   120,   125,    30,    31,
      32,   125,   762,   120,   121,   660,   482,    45,   349,   664,
     665,    12,   353,   263,     8,     9,   266,    11,   268,   120,
      11,    12,    13,    16,   274,    16,    16,    21,    22,    23,
     539,   366,   120,   374,   215,   216,   119,   125,   121,   675,
     119,   376,   121,    81,     6,   295,   227,   382,   298,   230,
      82,   324,     5,   118,   530,   120,   237,     5,   331,   240,
     696,   349,   118,     5,   120,   353,   339,   120,   249,   122,
     122,   119,   322,   121,   119,   416,   121,   412,   366,   111,
     112,   113,   114,   333,   357,   335,   374,   118,   376,   120,
     335,   399,   120,   121,   382,   403,     5,   733,   406,     8,
       9,    10,   119,   121,   121,   631,   632,   395,   119,     5,
     121,   722,   119,   119,   121,   121,   119,    16,   121,   392,
     408,   119,     5,   121,   412,   120,   145,   146,   416,   407,
     122,   742,     5,   411,     7,     8,     9,    10,    11,    12,
      13,    14,    15,    16,    17,   119,     5,   121,    21,    22,
      67,    68,    69,    70,    71,    72,    73,    74,   119,   119,
     121,   121,    35,    36,   119,    38,   121,   118,   349,    42,
       5,   421,   353,    46,    47,    48,   119,   427,   121,     5,
     119,    54,   121,   120,   119,   366,   121,    60,   122,    30,
      31,    32,     5,   374,   482,   376,   119,   532,   121,   534,
     118,   382,   537,    57,    57,    59,    59,   120,   121,   228,
     229,   118,    57,    86,    59,   741,   119,   119,   121,   121,
      93,    94,   120,   121,   118,    98,     5,   408,   120,   121,
       5,   412,   120,   121,    28,   416,    30,    31,    32,    33,
      34,    82,   530,   118,   532,   123,   534,   121,   122,   537,
     118,   586,   587,   779,   118,   533,   122,   592,   120,   594,
     120,   121,   120,   121,   120,   121,   118,   108,   109,   120,
     111,   112,   113,   114,   524,   294,   526,   296,   122,   298,
     120,   121,   120,   121,   120,   121,     5,   622,    82,     5,
     625,   121,   122,   589,   590,   118,   125,   118,   586,   587,
     120,   482,     5,   122,   592,     5,   594,   101,   102,   118,
     104,   105,   106,   107,   108,   109,     5,   111,   112,   113,
     114,   121,     5,   122,   122,   122,     5,   120,   120,   120,
     120,   120,     5,     5,   622,   120,   355,   625,   120,   120,
     675,     5,   361,   120,   120,   123,   120,     5,   120,   530,
     118,   532,   122,   534,   120,   120,   537,   120,    11,   120,
     695,   696,    59,   613,   614,   615,   120,   617,   618,   120,
     120,   118,   120,   118,   120,    57,   711,   712,   120,   123,
     119,   722,   717,   120,   120,   120,   120,   675,   723,   120,
     120,   120,   120,    59,   120,   120,    39,    98,   733,   120,
      52,   742,   120,   120,   739,   586,   587,   695,   696,     5,
     429,   592,   120,   594,    30,    31,    32,    33,    34,    57,
      39,   120,   120,   711,   712,    52,    52,   762,    52,   717,
     680,     5,   682,   120,   722,   723,    57,   772,     4,   120,
     120,   622,   120,   693,   625,   733,    57,    59,    57,   120,
      57,   739,   120,    59,   742,    57,   132,   469,   571,   395,
     203,   401,   565,   117,   600,   192,    82,   353,   158,   146,
     448,    -1,    -1,    -1,   762,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   772,    -1,   736,   737,    -1,    -1,
     106,   107,   108,   109,   675,   111,   112,   113,   114,    -1,
      -1,    -1,    -1,    -1,    -1,   524,    -1,   526,   527,   528,
     529,    -1,    -1,    -1,   695,   696,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     711,   712,    -1,    -1,    -1,    -1,   717,    -1,    -1,    -1,
      -1,   722,   723,    -1,    10,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   733,    -1,    -1,    -1,    -1,    -1,   739,    -1,
      -1,   742,    28,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   762,    -1,    49,    -1,    -1,    52,    -1,    -1,    -1,
      -1,   772,    -1,   612,    -1,    -1,    -1,    -1,   617,    -1,
      -1,    67,    68,    69,    70,    71,    72,    73,    74,    75,
      76,    77,    78,    79,    80,    81,    82,    83,    84,    85,
      86,    87,    88,    89,    90,    91,    92,    -1,    -1,     4,
       5,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    18,    19,    20,    -1,    -1,    -1,    24,
      25,    26,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     679,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      45,    -1,    -1,    -1,   693,   694,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,     4,     5,    -1,
      -1,    66,   158,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    18,    19,    20,    -1,    -1,    81,    24,    25,    26,
      -1,    -1,    -1,    -1,    89,    90,    91,   736,    -1,    -1,
      -1,   187,    -1,   189,    99,   100,   101,    -1,    45,    -1,
      -1,    -1,    -1,    -1,   109,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   118,   119,    -1,    -1,    -1,   123,    66,
      -1,    -1,   127,    -1,   129,   130,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    81,    -1,   232,    -1,    -1,    -1,
      -1,    -1,    89,    90,    91,    -1,    -1,   243,   244,    -1,
      -1,   247,    99,   100,   101,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   109,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   118,   119,    -1,    -1,    -1,   123,    -1,    -1,    -1,
     127,    -1,   129,   130,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   301,   302,    -1,    -1,   305,
     306,   307,    -1,    -1,    -1,   311,    -1,   313,    -1,     4,
       5,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    18,    19,    20,    -1,    -1,    -1,    24,
      25,    26,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    40,    41,    -1,   354,    -1,
      45,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   367,    -1,    -1,   370,   371,   372,    -1,    -1,   375,
      -1,    66,    -1,    -1,   380,    -1,    -1,    -1,    -1,    -1,
     386,    -1,    -1,   389,   390,    -1,    81,    -1,    -1,    -1,
     396,   397,    -1,    -1,    89,    90,    91,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    99,   100,   101,    -1,    -1,   415,
      -1,    -1,    -1,    -1,   109,    -1,    -1,    -1,    -1,    -1,
     426,    -1,    -1,   118,    -1,    -1,     4,     5,    -1,    -1,
      -1,   437,   127,    -1,   129,   130,    -1,    -1,    -1,    -1,
      18,    19,    20,    -1,    -1,    -1,    24,    25,    26,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   471,   472,    45,    -1,    -1,
      -1,    -1,   478,    -1,    52,    53,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    66,   495,
      -1,    -1,    -1,    -1,    -1,   501,   502,    -1,    -1,    -1,
     506,    -1,   508,    81,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    89,    90,    91,    30,    31,    32,    33,    34,    -1,
      -1,    99,   100,   101,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   109,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     118,   547,    -1,    -1,   550,    -1,    -1,    -1,    -1,   127,
      -1,   129,   130,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
       4,     5,    -1,    -1,    -1,    -1,    82,    -1,    -1,    -1,
      -1,    -1,    -1,   579,    18,    19,    20,    -1,    -1,    -1,
      24,    25,    26,    -1,    -1,   591,   102,    -1,   104,   105,
     106,   107,   108,   109,   600,   111,   112,   113,   114,    -1,
      -1,    45,    -1,    -1,    -1,    -1,    -1,    -1,    52,    53,
       4,     5,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    66,    -1,    18,    19,    20,   633,    -1,    -1,
      24,    25,    26,   639,    -1,   641,    -1,    81,    -1,    -1,
     646,    -1,    -1,    -1,    -1,    89,    90,    91,    -1,    -1,
      -1,    45,    -1,    -1,    -1,    99,   100,   101,    52,    53,
      -1,    -1,    -1,    -1,    -1,   109,    -1,    -1,    -1,    -1,
      -1,    -1,    66,    -1,   118,    -1,    -1,    -1,     4,     5,
      -1,    -1,    -1,   127,    -1,   129,   130,    81,    -1,    -1,
      -1,    -1,    18,    19,    20,    89,    90,    91,    24,    25,
      26,    -1,    -1,    -1,    -1,    99,   100,   101,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   109,    -1,    -1,    -1,    45,
      -1,    -1,    -1,    -1,   118,    -1,    -1,    -1,     4,     5,
      -1,    -1,    -1,   127,    -1,   129,   130,    -1,    -1,    -1,
      66,    -1,    18,    19,    20,    -1,    -1,    -1,    24,    25,
      26,    -1,    -1,    -1,    -1,    81,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    89,    90,    91,    -1,    -1,    -1,    45,
      -1,    -1,    -1,    99,   100,   101,    -1,    -1,    -1,   105,
      -1,    -1,    -1,   109,    -1,    -1,    -1,    -1,    -1,    -1,
      66,    -1,   118,    -1,    -1,    -1,     4,     5,    -1,    -1,
      -1,   127,    -1,   129,   130,    81,    -1,    -1,    -1,    -1,
      18,    19,    20,    89,    90,    91,    24,    25,    26,    -1,
      -1,    -1,    -1,    99,   100,   101,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   109,    -1,    -1,    -1,    45,    -1,    -1,
      -1,    -1,   118,   119,    -1,    -1,     4,     5,    -1,    -1,
      -1,   127,    -1,   129,   130,    -1,    -1,    -1,    66,    -1,
      18,    19,    20,    -1,    -1,    -1,    24,    25,    26,    -1,
      -1,    -1,    -1,    81,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    89,    90,    91,    -1,    -1,    -1,    45,    -1,    -1,
      -1,    99,   100,   101,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   109,    -1,    -1,    -1,    -1,    -1,    -1,    66,   117,
     118,    -1,    -1,    -1,     4,     5,    -1,    -1,    -1,   127,
      -1,   129,   130,    81,    -1,    -1,    -1,    -1,    18,    19,
      20,    89,    90,    91,    24,    25,    26,    -1,    -1,    -1,
      -1,    99,   100,   101,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   109,    -1,    -1,    -1,    45,    -1,    -1,    -1,    -1,
     118,    -1,    -1,    53,    -1,   123,    -1,     4,     5,   127,
      -1,   129,   130,    -1,    -1,    -1,    66,    -1,    -1,    -1,
      -1,    18,    19,    20,    -1,    -1,    -1,    24,    25,    26,
      -1,    81,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    89,
      90,    91,    -1,    -1,    -1,    -1,    -1,    -1,    45,    99,
     100,   101,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   109,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   118,    66,
      -1,    -1,    -1,    -1,    -1,     4,     5,   127,    -1,   129,
     130,    -1,    -1,    -1,    81,    -1,    -1,    -1,    -1,    18,
      19,    20,    89,    90,    91,    24,    25,    26,    -1,    -1,
      -1,    -1,    99,   100,   101,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   109,    -1,    -1,    -1,    45,    -1,    -1,    -1,
      -1,   118,   119,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     127,    -1,   129,   130,    -1,    -1,    -1,    66,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    81,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      89,    90,    91,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      99,   100,   101,    -1,    -1,    -1,    -1,    -1,    -1,     5,
     109,     7,    -1,    -1,    -1,    11,    -1,    -1,    -1,   118,
      -1,    -1,    -1,    -1,    -1,    21,    -1,    -1,   127,    -1,
     129,   130,    28,    29,    30,    31,    32,    33,    34,    -1,
      36,    -1,    38,    -1,    -1,    -1,    -1,    43,    44,    -1,
      -1,    -1,    -1,    49,    50,    51,    -1,    -1,    -1,    55,
      -1,    -1,    -1,    -1,    60,    61,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    75,
      -1,    77,    78,    -1,    -1,    -1,    82,    -1,    -1,    -1,
      -1,    87,    88,    89,    90,    91,    92,    -1,    -1,    -1,
      96,    97,    -1,    99,   100,   101,   102,    -1,   104,   105,
     106,   107,   108,   109,    -1,   111,   112,   113,   114,    -1,
      -1,   117,    -1,     5,   120,     7,     8,     9,   124,    11,
      -1,   127,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    21,
      22,    23,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    36,    -1,    38,    -1,    -1,    -1,
      -1,    43,    44,    -1,    -1,    -1,    -1,    49,    50,    51,
      -1,    -1,    -1,    55,    -1,    -1,    -1,    -1,    60,    61,
      -1,    -1,    -1,    -1,     5,    -1,     7,    -1,    -1,    -1,
      11,    -1,    -1,    75,    -1,    77,    78,    -1,    -1,    -1,
      21,    -1,    -1,    -1,    -1,    87,    88,    -1,    -1,    -1,
      92,    -1,    -1,    -1,    96,    36,    37,    38,    -1,    -1,
      -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,    50,
      51,    -1,    -1,    -1,    55,   117,    -1,    -1,    -1,    60,
      61,    -1,   124,    -1,    -1,   127,    -1,    -1,    -1,     5,
      -1,     7,    -1,    -1,    75,    11,    77,    78,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    21,    87,    88,    -1,    -1,
      -1,    92,    -1,    -1,    -1,    96,    -1,    98,    -1,    -1,
      36,    -1,    38,    -1,    -1,    -1,    -1,    43,    44,    -1,
      -1,    -1,    -1,    49,    50,    51,   117,    -1,    -1,    55,
      -1,    -1,    -1,   124,    60,    61,   127,    -1,    -1,    -1,
       5,    -1,     7,    -1,    -1,    -1,    11,    -1,    -1,    75,
      -1,    77,    78,    -1,    -1,    -1,    21,    -1,    -1,    -1,
      -1,    87,    88,    -1,    -1,    -1,    92,    -1,    -1,    -1,
      96,    36,    37,    38,    -1,    -1,    -1,    -1,    43,    44,
      -1,    -1,    -1,    -1,    49,    50,    51,    -1,    -1,    -1,
      55,   117,    -1,    -1,   120,    60,    61,    -1,   124,    -1,
      -1,   127,    -1,    -1,    -1,     5,    -1,     7,    -1,    -1,
      75,    11,    77,    78,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    21,    87,    88,    -1,    -1,    -1,    92,    -1,    -1,
      -1,    96,    -1,    -1,    -1,    -1,    36,    -1,    38,    -1,
      -1,    -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,
      50,    51,   117,    -1,    -1,    55,    -1,    -1,    -1,   124,
      60,    61,   127,    -1,     5,    -1,     7,    -1,    -1,    -1,
      11,    -1,    -1,    -1,    -1,    75,    76,    77,    78,    -1,
      21,    -1,    -1,    -1,    -1,    -1,    -1,    87,    88,    -1,
      -1,    -1,    92,    -1,    -1,    36,    96,    38,    -1,    -1,
      -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,    50,
      51,    -1,    -1,    -1,    55,    -1,    57,   117,    -1,    60,
      61,    -1,    -1,    -1,   124,    -1,    -1,   127,    -1,     5,
      -1,     7,    -1,    -1,    75,    11,    77,    78,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    21,    87,    88,    -1,    -1,
      -1,    92,    -1,    -1,    -1,    96,    -1,    -1,    -1,    -1,
      36,    37,    38,    -1,    -1,    -1,    -1,    43,    44,    -1,
      -1,    -1,    -1,    49,    50,    51,   117,    -1,    -1,    55,
      -1,    -1,    -1,   124,    60,    61,   127,    -1,     5,    -1,
       7,    -1,    -1,    -1,    11,    -1,    -1,    -1,    -1,    75,
      -1,    77,    78,    -1,    21,    -1,    -1,    -1,    -1,    -1,
      -1,    87,    88,    -1,    -1,    -1,    92,    -1,    -1,    36,
      96,    38,    -1,    -1,    -1,    -1,    43,    44,    -1,    -1,
      -1,    -1,    49,    50,    51,    -1,    -1,    -1,    55,    -1,
      57,   117,    -1,    60,    61,    -1,    -1,     5,   124,     7,
      -1,   127,    -1,    11,    -1,    -1,    -1,    -1,    75,    -1,
      77,    78,    -1,    21,    -1,    -1,    -1,    -1,    -1,    -1,
      87,    88,    -1,    -1,    -1,    92,    -1,    -1,    36,    96,
      38,    -1,    -1,    -1,    -1,    43,    44,    -1,    -1,    -1,
      -1,    49,    50,    51,    -1,    -1,    -1,    55,    -1,    -1,
     117,    -1,    60,    61,    -1,    -1,    -1,   124,    -1,    -1,
     127,    -1,    -1,    -1,    -1,    -1,    -1,    75,    -1,    77,
      78,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    87,
      88,    -1,    -1,    -1,    92,    -1,    -1,     5,    96,     7,
      -1,    -1,    -1,    11,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    21,    -1,    -1,    -1,    -1,    -1,   117,
      -1,    -1,   120,    -1,    -1,    -1,   124,    -1,    36,   127,
      38,    -1,    -1,    -1,    -1,    43,    44,    -1,    -1,    -1,
      -1,    49,    50,    51,    -1,    -1,    -1,    55,    -1,    -1,
      -1,    -1,    60,    61,    -1,    -1,    -1,    -1,     5,    -1,
       7,    -1,    -1,    -1,    11,    -1,    -1,    75,    -1,    77,
      78,    -1,    -1,    -1,    21,    -1,    -1,    -1,    -1,    87,
      88,    -1,    -1,    -1,    92,    -1,    -1,    -1,    96,    36,
      -1,    38,    -1,    -1,    -1,    -1,    43,    44,    -1,    -1,
      -1,    -1,    49,    50,    51,    -1,    -1,    -1,    55,   117,
      -1,    -1,   120,    60,    61,    -1,   124,    -1,    -1,   127,
      28,    29,    30,    31,    32,    33,    34,    -1,    75,    -1,
      77,    78,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      87,    88,    -1,    -1,    -1,    92,    -1,    -1,    -1,    96,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
     117,    -1,    -1,    -1,    82,    -1,    -1,   124,    -1,    -1,
     127,    89,    90,    91,    -1,    -1,    -1,    -1,    -1,    97,
      -1,    99,   100,   101,   102,    -1,   104,   105,   106,   107,
     108,   109,    -1,   111,   112,   113,   114,    -1,    -1,    -1,
      79,    80,    28,    82,    30,    31,    32,    33,    34,   127,
      89,    90,    91,    -1,    -1,    -1,    -1,    -1,    97,    98,
      99,   100,   101,   102,    -1,   104,   105,   106,   107,   108,
     109,    -1,   111,   112,   113,   114,    28,    29,    30,    31,
      32,    33,    34,    -1,    -1,    -1,    -1,   126,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    82,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,   102,    -1,   104,   105,
     106,   107,   108,   109,    -1,   111,   112,   113,   114,    -1,
      82,    -1,    -1,    -1,    -1,    -1,    -1,    89,    90,    91,
      -1,    -1,    -1,    -1,    -1,    97,    -1,    99,   100,   101,
     102,    -1,   104,   105,   106,   107,   108,   109,    82,   111,
     112,   113,   114,    -1,    -1,    89,    90,    91,    -1,    -1,
      -1,    -1,    -1,    97,   126,    99,   100,   101,   102,    -1,
     104,   105,   106,   107,   108,   109,    -1,   111,   112,   113,
     114,    28,    29,    30,    31,    32,    33,    34,    -1,    -1,
      -1,    -1,   126,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    82,    -1,    -1,    -1,    -1,
      -1,    -1,    89,    90,    91,    -1,    -1,    -1,    -1,    -1,
      97,    -1,    99,   100,   101,   102,    -1,   104,   105,   106,
     107,   108,   109,    82,   111,   112,   113,   114,    -1,    -1,
      89,    90,    91,    -1,    -1,    -1,    -1,    -1,    97,   126,
      99,   100,   101,   102,    -1,   104,   105,   106,   107,   108,
     109,    -1,   111,   112,   113,   114,    28,    29,    30,    31,
      32,    33,    34,   122,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      82,    -1,    -1,    -1,    -1,    -1,    -1,    89,    90,    91,
      -1,    -1,    -1,    -1,    -1,    97,    -1,    99,   100,   101,
     102,    -1,   104,   105,   106,   107,   108,   109,    82,   111,
     112,   113,   114,    -1,    -1,    89,    90,    91,   120,    -1,
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
     199,   120,     5,   112,   119,   121,   119,   163,   120,     5,
     119,   121,   119,   120,   119,   163,   118,   119,   147,   122,
     200,   200,   120,   119,   200,   120,   188,   119,   119,   119,
     119,   120,   119,   200,   119,   200,   200,    42,   119,   121,
     175,   200,   120,   200,   120,   119,   119,   120,   120,   120,
     120,   119,    21,   190,   191,    11,   190,   191,   190,   190,
     190,   152,   188,    57,   138,   151,   178,   120,   119,   178,
      59,   171,   119,   120,   120,   200,   120,   200,   120,   122,
     120,   118,   120,   164,   120,   119,   118,   167,   120,   119,
     163,   119,   200,   120,   120,   120,   120,    37,   178,    53,
     184,   185,   186,   187,   184,   184,   200,   178,   120,   178,
     177,   120,   120,   120,   120,   120,   190,   120,   191,   191,
     191,   120,     5,   190,   191,   120,   191,   120,   120,    57,
     119,   178,    57,    11,    21,   151,   120,    59,    37,   172,
     200,   120,   120,   200,   119,   200,   120,   200,   120,   119,
     120,    39,    98,    52,   185,   186,    52,    98,    52,   186,
      52,   186,   120,   151,   178,   120,   120,   190,   191,   191,
     120,     5,   120,   120,    57,   190,   191,   190,   178,   151,
     178,    39,   120,   120,   119,   119,   120,   178,   120,   178,
      52,   120,   178,    52,    52,   182,   178,    57,   120,     5,
     120,   120,   151,   178,   120,   190,   120,    57,   178,    59,
     172,   182,   119,    57,   120,   178,    57,   120,    59,   119,
     178,    57,   172
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
#line 3173 "y.tab.c"
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


#line 374 "yaccs/verilog.yacc"


