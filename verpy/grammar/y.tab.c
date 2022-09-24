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
     enum = 354,
     typedef = 355,
     arith_shift_right = 356,
     SignedLeft = 357,
     shift_right = 358,
     shift_left = 359,
     Veryequal = 360,
     noteqeq = 361,
     StarStar = 362,
     UNARY_PREC = 363
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
#define enum 354
#define typedef 355
#define arith_shift_right 356
#define SignedLeft 357
#define shift_right 358
#define shift_left 359
#define Veryequal 360
#define noteqeq 361
#define StarStar 362
#define UNARY_PREC 363




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
#line 323 "y.tab.c"

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
#define YYLAST   4880

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  135
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  73
/* YYNRULES -- Number of rules.  */
#define YYNRULES  360
/* YYNRULES -- Number of states.  */
#define YYNSTATES  803

/* YYTRANSLATE(YYLEX) -- Bison symbol number corresponding to YYLEX.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   363

#define YYTRANSLATE(YYX)						\
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[YYLEX] -- Bison symbol number corresponding to YYLEX.  */
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
/* YYPRHS[YYN] -- Index of the first RHS symbol of rule number YYN in
   YYRHS.  */
static const yytype_uint16 yyprhs[] =
{
       0,     0,     3,     5,     8,    10,    12,    14,    21,    26,
      30,    31,    33,    38,    42,    46,    48,    51,    55,    59,
      64,    69,    71,    76,    82,    85,    86,    88,    90,    92,
      94,    96,    98,   100,   102,   104,   106,   108,   110,   112,
     114,   117,   120,   124,   131,   134,   136,   140,   144,   146,
     150,   155,   161,   165,   169,   174,   180,   186,   191,   196,
     203,   213,   217,   224,   232,   239,   245,   247,   249,   251,
     253,   255,   257,   259,   261,   263,   265,   272,   278,   287,
     295,   302,   311,   321,   331,   342,   349,   355,   364,   374,
     377,   379,   383,   387,   391,   396,   402,   408,   415,   419,
     424,   430,   435,   439,   444,   448,   453,   458,   464,   470,
     474,   479,   485,   489,   493,   495,   499,   503,   505,   510,
     515,   521,   525,   531,   538,   542,   548,   555,   562,   569,
     576,   582,   590,   599,   607,   615,   619,   621,   624,   630,
     635,   644,   649,   652,   655,   658,   662,   664,   670,   673,
     678,   681,   684,   687,   692,   696,   699,   702,   706,   710,
     713,   715,   719,   725,   729,   731,   733,   735,   737,   739,
     741,   743,   745,   747,   749,   755,   763,   773,   776,   779,
     782,   787,   789,   791,   795,   797,   800,   803,   805,   809,
     812,   815,   821,   825,   830,   836,   841,   847,   853,   861,
     865,   869,   873,   878,   882,   888,   891,   895,   899,   904,
     910,   917,   925,   932,   939,   947,   954,   962,   966,   970,
     973,   975,   977,   979,   982,   984,   990,   994,   998,  1000,
    1004,  1006,  1010,  1020,  1026,  1032,  1036,  1038,  1042,  1045,
    1047,  1051,  1055,  1059,  1063,  1067,  1069,  1072,  1074,  1076,
    1079,  1083,  1087,  1090,  1092,  1094,  1098,  1100,  1106,  1112,
    1118,  1122,  1124,  1126,  1128,  1131,  1134,  1137,  1140,  1143,
    1146,  1150,  1153,  1156,  1158,  1160,  1162,  1164,  1166,  1168,
    1171,  1174,  1176,  1178,  1180,  1182,  1184,  1188,  1192,  1194,
    1197,  1199,  1202,  1206,  1210,  1215,  1220,  1227,  1229,  1231,
    1233,  1235,  1237,  1239,  1241,  1243,  1245,  1247,  1249,  1251,
    1253,  1255,  1257,  1262,  1264,  1266,  1268,  1270,  1272,  1274,
    1277,  1281,  1285,  1288,  1294,  1298,  1302,  1306,  1310,  1314,
    1318,  1322,  1326,  1330,  1334,  1338,  1342,  1346,  1350,  1354,
    1358,  1362,  1366,  1370,  1374,  1378,  1382,  1386,  1390,  1394,
    1399,  1403,  1405,  1408,  1411,  1414,  1417,  1420,  1423,  1426,
    1429
};

/* YYRHS -- A `-1'-separated list of the rules' RHS.  */
static const yytype_int16 yyrhs[] =
{
     136,     0,    -1,   137,    -1,   137,   138,    -1,   138,    -1,
     139,    -1,   146,    -1,     3,     5,   140,   141,   144,     6,
      -1,   121,   122,   164,   123,    -1,   121,   122,   123,    -1,
      -1,   124,    -1,   122,   142,   123,   124,    -1,   122,   123,
     124,    -1,   142,   125,   143,    -1,   143,    -1,   200,     5,
      -1,   200,   198,     5,    -1,   200,    21,     5,    -1,   200,
     198,     5,   198,    -1,   200,   198,   198,     5,    -1,     5,
      -1,   200,     5,   126,   206,    -1,   200,   198,     5,   126,
     206,    -1,   145,   144,    -1,    -1,   150,    -1,   151,    -1,
     166,    -1,   173,    -1,   174,    -1,   159,    -1,   160,    -1,
     161,    -1,   147,    -1,   155,    -1,   156,    -1,   146,    -1,
     185,    -1,    96,    -1,    66,    45,    -1,    66,     5,    -1,
      66,     5,   207,    -1,    66,     4,     5,   117,     4,     5,
      -1,    54,   182,    -1,     5,    -1,     5,   126,   207,    -1,
     149,   125,   148,    -1,   148,    -1,   200,   197,   124,    -1,
     200,   198,   197,   124,    -1,   200,   198,   197,   198,   124,
      -1,    17,   197,   124,    -1,   201,   149,   124,    -1,   201,
     198,   149,   124,    -1,   201,   198,   198,   149,   124,    -1,
     201,   198,     5,   198,   124,    -1,   201,     5,   198,   124,
      -1,   201,   172,   197,   124,    -1,   201,   172,     5,   126,
     207,   124,    -1,   100,    99,    13,   198,   127,   197,   128,
       5,   124,    -1,     7,   189,   124,    -1,     7,   169,   196,
     126,   207,   124,    -1,     7,   152,   169,   196,   126,   207,
     124,    -1,     7,   152,   196,   126,   207,   124,    -1,   122,
     153,   125,   153,   123,    -1,    67,    -1,    68,    -1,    69,
      -1,    70,    -1,    71,    -1,    72,    -1,    73,    -1,    74,
      -1,   198,    -1,    21,    -1,    56,     5,   124,   157,   195,
      57,    -1,    56,     5,   124,   195,    57,    -1,    56,   198,
     198,     5,   124,   157,   182,    57,    -1,    56,   154,     5,
     124,   157,   182,    57,    -1,    56,   154,     5,   124,   182,
      57,    -1,    56,     5,   122,   142,   123,   124,   182,    57,
      -1,    56,     5,   122,   142,   123,   124,   157,   182,    57,
      -1,    56,   154,     5,   122,   142,   123,   124,   182,    57,
      -1,    56,   154,     5,   122,   142,   123,   124,   157,   182,
      57,    -1,    58,     5,   124,   157,   182,    59,    -1,    58,
       5,   124,   182,    59,    -1,    58,     5,   122,   142,   123,
     124,   182,    59,    -1,    58,     5,   122,   142,   123,   124,
     157,   182,    59,    -1,   157,   158,    -1,   158,    -1,    11,
     197,   124,    -1,    22,   197,   124,    -1,    23,   197,   124,
      -1,    11,   198,   197,   124,    -1,    11,   198,     5,   198,
     124,    -1,    11,   198,   198,     5,   124,    -1,     9,    11,
     198,   198,     5,   124,    -1,     8,   197,   124,    -1,     8,
     197,   198,   124,    -1,     8,   198,   198,   197,   124,    -1,
       8,    21,   197,   124,    -1,    21,   197,   124,    -1,    21,
     197,   198,   124,    -1,    47,   162,   124,    -1,    47,    16,
     162,   124,    -1,    47,   198,   162,   124,    -1,    47,   198,
     198,   162,   124,    -1,    47,    16,   198,   162,   124,    -1,
      48,   162,   124,    -1,    48,   198,   162,   124,    -1,    48,
     198,   198,   162,   124,    -1,    46,   162,   124,    -1,   162,
     125,   163,    -1,   163,    -1,     5,   126,   207,    -1,   164,
     125,   165,    -1,   165,    -1,    48,     5,   126,   207,    -1,
      47,     5,   126,   207,    -1,    47,   198,     5,   126,   207,
      -1,     5,   126,   207,    -1,     5,     5,   122,   123,   124,
      -1,     5,   172,     5,   122,   123,   124,    -1,     5,     5,
     124,    -1,    42,   122,   194,   123,   124,    -1,    42,     5,
     122,   194,   123,   124,    -1,     5,     5,   122,   167,   123,
     124,    -1,    42,     5,   122,   167,   123,   124,    -1,     5,
       5,   122,   194,   123,   124,    -1,     5,   122,   194,   123,
     124,    -1,     5,   172,     5,   122,   167,   123,   124,    -1,
       5,   172,     5,   198,   122,   167,   123,   124,    -1,     5,
       5,   198,   122,   167,   123,   124,    -1,     5,     5,   198,
     122,   194,   123,   124,    -1,   167,   125,   168,    -1,   168,
      -1,   129,   116,    -1,   129,     5,   122,   207,   123,    -1,
     129,     5,   122,   123,    -1,   129,     5,   130,     4,   131,
     122,   207,   123,    -1,   121,   122,   194,   123,    -1,   121,
       4,    -1,   121,     5,    -1,   121,    82,    -1,   170,   125,
     171,    -1,   171,    -1,   129,     5,   122,   207,   123,    -1,
     129,     5,    -1,   121,   122,   194,   123,    -1,   121,     4,
      -1,   121,    82,    -1,   121,     5,    -1,   121,   122,   170,
     123,    -1,   121,   122,   123,    -1,    98,   182,    -1,    35,
     182,    -1,    35,   178,   182,    -1,    85,   175,    86,    -1,
     175,   176,    -1,   176,    -1,    36,   175,    37,    -1,    36,
     102,     5,   175,    37,    -1,    87,   197,   124,    -1,   150,
      -1,   151,    -1,   159,    -1,   160,    -1,   161,    -1,   166,
      -1,   177,    -1,   173,    -1,   147,    -1,   185,    -1,    38,
     122,   207,   123,   176,    -1,    38,   122,   207,   123,   176,
      39,   176,    -1,    60,   122,   189,   124,   207,   124,   189,
     123,   176,    -1,   132,   116,    -1,   132,    84,    -1,   132,
       5,    -1,   132,   122,   180,   123,    -1,    42,    -1,   125,
      -1,   180,   179,   181,    -1,   181,    -1,    40,   207,    -1,
      41,   207,    -1,   207,    -1,    36,   195,    37,    -1,    36,
      37,    -1,    55,   182,    -1,    36,   102,     5,   195,    37,
      -1,    75,   195,    76,    -1,   196,   126,   207,   124,    -1,
     196,   126,   169,   207,   124,    -1,   196,    34,   207,   124,
      -1,   196,    34,   169,   207,   124,    -1,    38,   122,   207,
     123,   182,    -1,    38,   122,   207,   123,   182,    39,   182,
      -1,    43,   207,   124,    -1,    21,   197,   124,    -1,    11,
     197,   124,    -1,    11,   198,   197,   124,    -1,    89,   207,
     124,    -1,    88,   207,   126,   207,   124,    -1,   178,   124,
      -1,    44,     5,   124,    -1,    77,     5,   124,    -1,     5,
     122,   123,   124,    -1,     5,   122,   194,   123,   124,    -1,
      49,   122,   207,   123,   191,    52,    -1,    49,   122,   207,
     123,   191,   193,    52,    -1,    49,   122,   207,   123,   193,
      52,    -1,    50,   122,   207,   123,   191,    52,    -1,    50,
     122,   207,   123,   191,   193,    52,    -1,    51,   122,   207,
     123,   191,    52,    -1,    51,   122,   207,   123,   191,   193,
      52,    -1,   121,   207,   124,    -1,   121,   207,   182,    -1,
       5,   124,    -1,   186,    -1,   187,    -1,   188,    -1,   205,
     124,    -1,   185,    -1,     7,   196,   126,   207,   124,    -1,
      97,     5,   124,    -1,   183,   125,   184,    -1,   184,    -1,
       5,   126,   207,    -1,    45,    -1,    78,   183,    79,    -1,
      60,   122,   189,   124,   207,   124,   189,   123,   182,    -1,
      93,   122,   207,   123,   182,    -1,    61,   122,   207,   123,
     182,    -1,   189,   125,   190,    -1,   190,    -1,   196,   126,
     207,    -1,   191,   192,    -1,   192,    -1,   194,   102,   182,
      -1,   194,   102,   124,    -1,    53,   102,   182,    -1,    53,
     102,   124,    -1,   194,   125,   207,    -1,   207,    -1,   195,
     182,    -1,   182,    -1,     5,    -1,     5,   198,    -1,     5,
     199,   198,    -1,     5,   199,   199,    -1,     5,   199,    -1,
     205,    -1,   202,    -1,     5,   125,   197,    -1,     5,    -1,
     130,   207,   102,   207,   131,    -1,   130,   207,    80,   207,
     131,    -1,   130,   207,    81,   207,   131,    -1,   130,   207,
     131,    -1,     8,    -1,     9,    -1,    10,    -1,     9,    11,
      -1,     8,    12,    -1,     9,    12,    -1,    10,    12,    -1,
       8,    16,    -1,     9,    16,    -1,     9,    11,    16,    -1,
       9,    13,    -1,     8,    13,    -1,    13,    -1,    11,    -1,
      12,    -1,    16,    -1,    21,    -1,    22,    -1,    11,    16,
      -1,    12,    16,    -1,    87,    -1,    94,    -1,    95,    -1,
      14,    -1,    15,    -1,   127,   203,   128,    -1,   203,   125,
     204,    -1,   204,    -1,   207,   202,    -1,   207,    -1,   109,
     202,    -1,     5,   129,   205,    -1,     5,   129,     5,    -1,
       5,   129,     5,   198,    -1,     5,   129,     5,   199,    -1,
       5,   129,     5,   122,   207,   123,    -1,     4,    -1,    82,
      -1,    45,    -1,    18,    -1,    19,    -1,    20,    -1,    24,
      -1,    25,    -1,    26,    -1,     5,    -1,   205,    -1,     4,
      -1,    82,    -1,    45,    -1,    66,    -1,    66,   122,   207,
     123,    -1,    18,    -1,    19,    -1,    20,    -1,    24,    -1,
      25,    -1,    26,    -1,     5,   198,    -1,     5,   199,   198,
      -1,     5,   199,   199,    -1,     5,   199,    -1,   207,   101,
     207,   102,   207,    -1,   207,   112,   207,    -1,   207,   116,
     207,    -1,   207,   113,   207,    -1,   207,   117,   207,    -1,
     207,   118,   207,    -1,   207,   104,   207,    -1,   207,   103,
     207,    -1,   207,   105,   207,    -1,   207,   110,   207,    -1,
     207,   111,   207,    -1,   207,    83,   207,    -1,   207,    28,
     207,    -1,   207,    29,   207,    -1,   207,    90,   207,    -1,
     207,    91,   207,    -1,   207,    92,   207,    -1,   207,    31,
     207,    -1,   207,    30,   207,    -1,   207,    32,   207,    -1,
     207,   115,   207,    -1,   207,    33,   207,    -1,   207,    34,
     207,    -1,   207,   109,   207,    -1,   207,   108,   207,    -1,
     207,   106,   207,    -1,     5,   122,   194,   123,    -1,   122,
     207,   123,    -1,   202,    -1,   113,   207,    -1,   103,   207,
      -1,   105,   207,    -1,   104,   207,    -1,    90,   207,    -1,
      92,   207,    -1,    91,   207,    -1,   133,   207,    -1,   134,
     207,    -1
};

/* YYRLINE[YYN] -- source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,    45,    45,    46,    46,    47,    47,    48,    50,    50,
      50,    51,    51,    51,    52,    52,    54,    54,    54,    54,
      54,    54,    54,    54,    58,    58,    61,    62,    63,    64,
      65,    66,    67,    68,    69,    70,    71,    72,    73,    74,
      78,    78,    78,    78,    79,    80,    80,    81,    81,    83,
      84,    85,    86,    87,    88,    89,    92,    95,    96,    97,
      98,   103,   104,   105,   106,   109,   110,   110,   110,   110,
     110,   110,   110,   110,   111,   111,   113,   114,   115,   116,
     117,   118,   119,   120,   121,   124,   125,   126,   127,   130,
     130,   132,   133,   134,   135,   136,   137,   138,   139,   140,
     141,   142,   143,   144,   148,   149,   150,   151,   152,   154,
     154,   154,   155,   157,   157,   158,   160,   160,   162,   163,
     164,   165,   169,   170,   171,   172,   173,   174,   175,   176,
     177,   178,   179,   180,   181,   189,   189,   190,   190,   190,
     190,   192,   192,   192,   192,   193,   193,   194,   194,   195,
     195,   195,   195,   195,   195,   198,   198,   198,   201,   203,
     203,   206,   207,   208,   209,   210,   211,   212,   213,   214,
     215,   216,   217,   218,   219,   220,   225,   230,   230,   230,
     230,   231,   231,   232,   232,   233,   233,   233,   238,   239,
     240,   241,   242,   243,   244,   245,   246,   247,   248,   249,
     250,   251,   252,   253,   254,   255,   256,   257,   258,   259,
     260,   261,   262,   263,   264,   265,   266,   267,   268,   269,
     270,   271,   272,   273,   274,   275,   276,   280,   280,   281,
     281,   283,   285,   286,   287,   288,   288,   289,   290,   290,
     291,   291,   292,   292,   294,   294,   295,   295,   298,   298,
     298,   298,   298,   298,   298,   300,   300,   302,   302,   302,
     303,   305,   305,   305,   305,   305,   305,   305,   305,   305,
     305,   305,   305,   307,   307,   307,   307,   307,   307,   307,
     307,   307,   307,   307,   307,   307,   309,   310,   310,   312,
     313,   314,   318,   319,   320,   321,   322,   326,   327,   328,
     329,   329,   329,   329,   329,   329,   333,   334,   335,   336,
     337,   338,   339,   340,   340,   340,   340,   340,   340,   341,
     342,   343,   344,   345,   346,   347,   348,   349,   350,   351,
     352,   353,   354,   355,   356,   357,   358,   359,   360,   361,
     362,   363,   364,   365,   366,   367,   368,   369,   370,   371,
     372,   373,   374,   375,   376,   377,   378,   379,   380,   381,
     382
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
  "return", "always_comb", "enum", "typedef", "'?'", "':'", "'|'", "'^'",
  "'&'", "arith_shift_right", "SignedLeft", "shift_right", "shift_left",
  "'<'", "'>'", "'+'", "'-'", "Veryequal", "noteqeq", "'*'", "'/'", "'%'",
  "StarStar", "UNARY_PREC", "'#'", "'('", "')'", "';'", "','", "'='",
  "'{'", "'}'", "'.'", "'['", "']'", "'@'", "'!'", "'~'", "$accept",
  "Main", "Mains", "MainItem", "Module", "Hparams", "Header",
  "Header_list", "Header_item", "Module_stuffs", "Mstuff", "Define",
  "Initial", "OneDef", "ManyDefs", "Definition", "Assign", "StrengthDef",
  "Strength", "WidthInt", "Function", "Task", "Mem_defs", "Mem_def",
  "Parameter", "Localparam", "Defparam", "Pairs", "Pair", "head_params",
  "head_param", "Instance", "Conns_list", "Connection", "AssignParams",
  "Prms_list", "PrmAssign", "InstParams", "Always", "Generate",
  "GenStatements", "GenStatement", "GenFor_statement", "When", "Or_coma",
  "When_items", "When_item", "Statement", "pragma_stuffs", "pragma_item",
  "Pragma", "For_statement", "Repeat_statement", "While_statement",
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
     345,   346,   347,   348,   349,   350,   351,   352,   353,   354,
     355,    63,    58,   124,    94,    38,   356,   357,   358,   359,
      60,    62,    43,    45,   360,   361,    42,    47,    37,   362,
     363,    35,    40,    41,    59,    44,    61,   123,   125,    46,
      91,    93,    64,    33,   126
};
# endif

/* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint8 yyr1[] =
{
       0,   135,   136,   137,   137,   138,   138,   139,   140,   140,
     140,   141,   141,   141,   142,   142,   143,   143,   143,   143,
     143,   143,   143,   143,   144,   144,   145,   145,   145,   145,
     145,   145,   145,   145,   145,   145,   145,   145,   145,   145,
     146,   146,   146,   146,   147,   148,   148,   149,   149,   150,
     150,   150,   150,   150,   150,   150,   150,   150,   150,   150,
     150,   151,   151,   151,   151,   152,   153,   153,   153,   153,
     153,   153,   153,   153,   154,   154,   155,   155,   155,   155,
     155,   155,   155,   155,   155,   156,   156,   156,   156,   157,
     157,   158,   158,   158,   158,   158,   158,   158,   158,   158,
     158,   158,   158,   158,   159,   159,   159,   159,   159,   160,
     160,   160,   161,   162,   162,   163,   164,   164,   165,   165,
     165,   165,   166,   166,   166,   166,   166,   166,   166,   166,
     166,   166,   166,   166,   166,   167,   167,   168,   168,   168,
     168,   169,   169,   169,   169,   170,   170,   171,   171,   172,
     172,   172,   172,   172,   172,   173,   173,   173,   174,   175,
     175,   176,   176,   176,   176,   176,   176,   176,   176,   176,
     176,   176,   176,   176,   176,   176,   177,   178,   178,   178,
     178,   179,   179,   180,   180,   181,   181,   181,   182,   182,
     182,   182,   182,   182,   182,   182,   182,   182,   182,   182,
     182,   182,   182,   182,   182,   182,   182,   182,   182,   182,
     182,   182,   182,   182,   182,   182,   182,   182,   182,   182,
     182,   182,   182,   182,   182,   182,   182,   183,   183,   184,
     184,   185,   186,   187,   188,   189,   189,   190,   191,   191,
     192,   192,   193,   193,   194,   194,   195,   195,   196,   196,
     196,   196,   196,   196,   196,   197,   197,   198,   198,   198,
     199,   200,   200,   200,   200,   200,   200,   200,   200,   200,
     200,   200,   200,   201,   201,   201,   201,   201,   201,   201,
     201,   201,   201,   201,   201,   201,   202,   203,   203,   204,
     204,   204,   205,   205,   205,   205,   205,   206,   206,   206,
     206,   206,   206,   206,   206,   206,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207
};

/* YYR2[YYN] -- Number of symbols composing right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     1,     2,     1,     1,     1,     6,     4,     3,
       0,     1,     4,     3,     3,     1,     2,     3,     3,     4,
       4,     1,     4,     5,     2,     0,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       2,     2,     3,     6,     2,     1,     3,     3,     1,     3,
       4,     5,     3,     3,     4,     5,     5,     4,     4,     6,
       9,     3,     6,     7,     6,     5,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     6,     5,     8,     7,
       6,     8,     9,     9,    10,     6,     5,     8,     9,     2,
       1,     3,     3,     3,     4,     5,     5,     6,     3,     4,
       5,     4,     3,     4,     3,     4,     4,     5,     5,     3,
       4,     5,     3,     3,     1,     3,     3,     1,     4,     4,
       5,     3,     5,     6,     3,     5,     6,     6,     6,     6,
       5,     7,     8,     7,     7,     3,     1,     2,     5,     4,
       8,     4,     2,     2,     2,     3,     1,     5,     2,     4,
       2,     2,     2,     4,     3,     2,     2,     3,     3,     2,
       1,     3,     5,     3,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     5,     7,     9,     2,     2,     2,
       4,     1,     1,     3,     1,     2,     2,     1,     3,     2,
       2,     5,     3,     4,     5,     4,     5,     5,     7,     3,
       3,     3,     4,     3,     5,     2,     3,     3,     4,     5,
       6,     7,     6,     6,     7,     6,     7,     3,     3,     2,
       1,     1,     1,     2,     1,     5,     3,     3,     1,     3,
       1,     3,     9,     5,     5,     3,     1,     3,     2,     1,
       3,     3,     3,     3,     3,     1,     2,     1,     1,     2,
       3,     3,     2,     1,     1,     3,     1,     5,     5,     5,
       3,     1,     1,     1,     2,     2,     2,     2,     2,     2,
       3,     2,     2,     1,     1,     1,     1,     1,     1,     2,
       2,     1,     1,     1,     1,     1,     3,     3,     1,     2,
       1,     2,     3,     3,     4,     4,     6,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     4,     1,     1,     1,     1,     1,     1,     2,
       3,     3,     2,     5,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     4,
       3,     1,     2,     2,     2,     2,     2,     2,     2,     2,
       2
};

/* YYDEFACT[STATE-NAME] -- Default rule to reduce with in state
   STATE-NUM when YYTABLE doesn't specify something else to do.  Zero
   means the default is an error.  */
static const yytype_uint16 yydefact[] =
{
       0,     0,     0,     0,     2,     4,     5,     6,    10,     0,
      41,    40,     1,     3,     0,     0,     0,   308,   306,   313,
     314,   315,   316,   317,   318,   310,   311,   309,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   351,
     307,    42,     0,     0,    11,    25,     0,     0,     0,     0,
     319,   322,     0,   356,   358,   357,   353,   355,   354,   352,
       0,     0,     0,   288,   290,   359,   360,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     9,     0,   117,    21,
     261,   262,   263,     0,     0,    15,     0,     0,     0,   274,
     275,   273,   284,   285,   276,     0,   277,   278,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   281,   282,
     283,    39,     0,     0,     0,    25,    37,    34,    26,    27,
      35,    36,    31,    32,    33,    28,    29,    30,    38,     0,
       0,     0,     0,   245,   293,   292,     0,   320,   321,     0,
     350,   291,     0,   286,   289,   335,   336,   341,   340,   342,
     344,   345,   334,   337,   338,   339,     0,   330,   329,   331,
     348,   347,   346,   332,   333,   324,   326,   343,   325,   327,
     328,     0,     0,     0,     0,     0,     8,     0,   265,   272,
     268,   264,   266,   271,   269,   267,    13,     0,     0,    16,
       0,     0,     0,     0,     0,     0,   248,     0,     0,     0,
       0,     0,   236,     0,   254,   253,   279,   280,   256,     0,
     248,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   156,   224,   220,   221,   222,     0,   253,
       0,     0,     0,     0,   114,     0,     0,     0,     0,     0,
       0,    44,     0,    75,     0,    74,     0,     0,   230,     0,
     228,     0,     0,     0,   281,   172,   164,   165,   166,   167,
     168,   169,   171,     0,   160,   170,   173,   155,     0,     7,
      24,     0,     0,    45,    48,     0,     0,     0,    43,   349,
       0,     0,   294,   295,     0,     0,     0,   260,   312,   287,
       0,   121,     0,     0,     0,     0,   116,   270,    12,    14,
       0,    18,    17,     0,     0,   124,     0,   150,   152,   151,
       0,     0,     0,   249,   252,   142,   143,   144,     0,    66,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,    61,     0,     0,     0,    52,     0,   219,     0,     0,
       0,     0,   189,     0,   247,     0,     0,     0,     0,     0,
       0,     0,   190,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   179,   178,   177,     0,   205,   157,     0,     0,
     223,     0,     0,     0,   112,     0,     0,     0,   104,     0,
       0,   109,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   231,     0,     0,     0,     0,     0,     0,   158,   159,
       0,    49,     0,     0,     0,    53,     0,   256,     0,    45,
       0,     0,   244,     0,     0,     0,     0,   323,   119,     0,
     118,   297,   300,   301,   302,   303,   304,   305,   299,   298,
      22,     0,    19,    20,     0,     0,     0,   136,     0,     0,
     154,     0,     0,   146,     0,     0,     0,     0,   250,   251,
       0,     0,     0,     0,     0,   235,   237,   255,     0,     0,
       0,   201,     0,   200,     0,   188,   246,     0,   199,   206,
       0,     0,     0,     0,     0,   192,   207,     0,   203,     0,
     226,   217,   218,     0,     0,     0,   184,   187,     0,     0,
       0,     0,     0,     0,     0,   115,   113,   105,     0,   106,
       0,   110,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    90,     0,     0,     0,     0,     0,     0,     0,   229,
     227,     0,   161,     0,     0,   163,     0,    50,     0,    46,
      57,    45,    47,     0,    58,     0,    54,     0,   296,   258,
     259,   257,   120,    23,   122,     0,   137,     0,     0,     0,
       0,     0,   148,   153,     0,   149,   130,     0,     0,     0,
     141,     0,     0,     0,     0,   208,     0,     0,   202,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   185,   186,
     181,   180,   182,     0,     0,   195,     0,   193,     0,     0,
     125,   108,   107,   111,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    89,     0,    77,     0,     0,     0,
       0,     0,     0,    86,     0,     0,     0,     0,    51,     0,
      56,    55,     0,     0,   127,   135,   129,     0,     0,     0,
     145,   123,     0,     0,    65,     0,    64,    62,   209,   225,
     191,   197,     0,     0,   239,     0,     0,     0,     0,     0,
     234,   204,   233,   183,   196,   194,   128,   126,     0,     0,
      98,     0,     0,     0,    91,   256,     0,     0,   102,     0,
      92,    93,    76,     0,     0,    80,     0,     0,     0,     0,
      85,   162,   174,     0,     0,    59,   139,     0,     0,   133,
     134,     0,   131,     0,    63,     0,     0,   210,   238,     0,
     212,     0,   213,     0,   215,     0,     0,     0,     0,   101,
      99,     0,     0,     0,    94,     0,   103,     0,    79,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   138,     0,
     147,   132,   198,   243,   242,   211,   241,   240,   214,   216,
       0,     0,    81,   100,     0,    95,    96,     0,     0,    91,
       0,   102,    78,     0,    87,   175,     0,     0,     0,     0,
      82,    97,     0,    83,    94,    88,     0,    60,     0,   232,
      84,   176,   140
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,     3,     4,     5,     6,    15,    45,   104,   105,   134,
     135,     7,   285,   304,   305,   286,   287,   219,   357,   274,
     140,   141,   540,   541,   288,   289,   290,   263,   264,    97,
      98,   291,   466,   467,   220,   472,   473,   215,   292,   147,
     293,   294,   295,   270,   613,   515,   516,   374,   279,   280,
     254,   255,   256,   257,   221,   222,   673,   674,   675,   676,
     375,   258,   229,   343,   344,   149,   150,    39,    62,    63,
      40,   460,   153
};

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
#define YYPACT_NINF -533
static const yytype_int16 yypact[] =
{
      82,    97,   145,   127,    82,  -533,  -533,  -533,    43,   142,
    1613,  -533,  -533,  -533,    72,    60,    54,  -533,   121,  -533,
    -533,  -533,  -533,  -533,  -533,  -533,    96,  -533,  1613,  1613,
    1613,  1613,  1613,  1613,  1613,  1613,  1237,  1613,  1613,  -533,
    -533,  4666,    84,    91,  -533,  3551,   197,  1613,   208,  1613,
    -533,   100,  1613,  -533,  -533,  -533,  -533,  -533,  -533,  -533,
    3925,   128,   207,  -533,  2601,  -533,  -533,  1613,  1613,  1613,
    1613,  1613,  1613,  1613,  1613,  1613,  1613,  1613,  1613,  1613,
    1613,  1613,  1613,  1613,  1613,  1613,  1613,  1613,  1613,  1613,
    1613,  1613,  1613,   134,    32,   264,  -533,   236,  -533,  -533,
     413,   430,   282,   183,   271,  -533,    27,   106,    33,   304,
     339,  -533,  -533,  -533,  -533,   359,  -533,  -533,  2389,    98,
     368,    31,    36,  2389,    28,   381,   211,  3927,  -533,  -533,
    -533,  -533,  2389,   253,   421,  3551,  -533,  -533,  -533,  -533,
    -533,  -533,  -533,  -533,  -533,  -533,  -533,  -533,  -533,    40,
       9,   416,   279,  4666,   163,  -533,   881,  -533,  -533,  3961,
    -533,  -533,  1237,  -533,  -533,  3601,  4762,   155,   155,   155,
     201,   201,  -533,  3696,  3696,  3696,  4635,  4731,  3696,  3790,
     419,   419,   419,   201,   201,   317,   317,   155,  -533,  -533,
    -533,  1613,   311,  1613,   439,   329,  -533,   138,  -533,  -533,
    -533,   475,  -533,  -533,  -533,  -533,  -533,   338,   382,   369,
     464,    49,   166,    12,  1613,   500,   213,    87,   414,    46,
      79,   243,  -533,   386,  -533,  -533,  -533,  -533,   399,   409,
     153,    79,    40,   359,  1867,   426,  1613,   550,   438,   477,
     478,  2389,   479,   480,  2389,   557,  1613,  1613,   484,   576,
    1613,   103,  1941,  -533,  -533,  -533,  -533,  -533,   -21,   462,
     486,  1613,   467,   256,  -533,    36,   284,    36,   323,    36,
     483,  -533,   156,  -533,   583,   481,   292,   487,  -533,    11,
    -533,  2752,   488,   490,   359,  -533,  -533,  -533,  -533,  -533,
    -533,  -533,  -533,  3645,  -533,  -533,  -533,  -533,   596,  -533,
    -533,   491,   359,   -11,  -533,   440,   609,    50,  -533,  -533,
    1613,  1613,  -533,  -533,  1613,  1613,  1613,  -533,  -533,  -533,
    1613,  4666,  1613,  4570,   498,  1613,  -533,  -533,  -533,  -533,
     393,  -533,   118,   611,   769,  -533,   499,  -533,  -533,  -533,
     929,   333,   -13,  -533,   100,  -533,  -533,  -533,  1613,  -533,
    -533,  -533,  -533,  -533,  -533,  -533,  -533,   501,    79,   502,
     507,  -533,    79,  1613,   359,  -533,  1329,  -533,   508,   493,
     359,   511,  -533,   632,  -533,  1999,  1613,  2785,   514,  1613,
    1613,  1613,  -533,    79,  1613,  2064,   515,  2632,  2827,  1613,
     517,  1720,  -533,  -533,  -533,  1060,  -533,  -533,  1363,  1363,
    -533,  1453,   336,  1613,  -533,   368,   442,   368,  -533,   444,
     368,  -533,   446,   368,   382,  1846,   343,   638,   382,  1846,
    1613,  -533,   211,   641,  3739,  1613,    79,   523,  -533,  -533,
     481,  -533,   -12,  1613,   524,  -533,   646,   447,   529,   -11,
     451,   646,  4666,  4026,  2440,  2505,  2536,  4666,  4666,  1613,
    4666,  -533,  -533,  -533,  -533,  -533,  -533,  -533,  -533,  -533,
    -533,   393,  -533,  -533,   530,    83,   347,  -533,   353,  1453,
    -533,   650,   354,  -533,   367,   532,   210,   535,  -533,  -533,
     371,   414,   533,  1613,  1613,  -533,  4666,  -533,   534,   375,
    1613,  -533,   537,  -533,  2389,  -533,  -533,  4062,  -533,  -533,
    4127,  4163,  4228,   453,  4264,  -533,  -533,  1613,  -533,  4329,
    -533,  -533,  -533,  1613,  1613,    68,  -533,  4666,  1613,  2892,
    1613,  2928,   376,   390,   538,  4666,  -533,  -533,   455,  -533,
     459,  -533,   466,   394,    35,   652,    40,   359,   359,   359,
    1846,  -533,  2122,   382,  1846,   540,   395,  1846,   606,  4666,
    -533,  3927,  -533,  4365,   471,  -533,   539,  -533,   543,  4666,
    -533,   542,  -533,  1613,  -533,   545,  -533,   473,  -533,  -533,
    -533,  -533,  4666,  -533,  -533,    -1,  -533,   546,   547,   548,
     398,   402,   552,  -533,   553,  -533,  -533,   555,   415,   547,
    -533,   554,  1613,  2993,  3029,  -533,   560,  3094,  -533,  2187,
    2389,  1487,  1613,  1613,  1613,  2389,  3130,  2389,  4666,  4666,
    -533,  -533,  -533,  1060,  3195,  -533,  3231,  -533,   562,   564,
    -533,  -533,  -533,  -533,   565,   359,   105,   481,   481,   566,
      78,   216,   567,   568,  -533,  2245,  -533,   418,  1846,   624,
     300,   569,   635,  -533,  3833,  3927,  1613,   359,  -533,  3296,
    -533,  -533,  1579,   691,  -533,  -533,  -533,   572,   575,  1613,
    -533,  -533,   577,   422,  -533,  3332,  -533,  -533,  -533,  -533,
    -533,   661,   600,  1063,  -533,   651,    26,  1184,  1187,  3397,
    -533,  -533,  -533,  -533,  -533,  -533,  -533,  -533,  1846,   580,
    -533,   581,   359,   481,   485,   122,   582,   703,   492,   585,
    -533,  -533,  -533,   586,   654,  -533,    40,   359,  1846,  1846,
    -533,  -533,   673,  3433,   588,  -533,  -533,  4430,   589,  -533,
    -533,  4466,  -533,   590,  -533,  2389,  2310,  -533,  -533,   665,
    -533,  2368,  -533,   667,  -533,   669,    79,  1846,   668,  -533,
    -533,   598,   719,   602,   495,   603,  -533,  1846,  -533,   604,
      78,   230,   672,  1846,   675,  3927,    79,   727,  -533,   613,
    -533,  -533,  -533,  -533,  -533,  -533,  -533,  -533,  -533,  -533,
     433,   680,  -533,  -533,   615,  -533,  -533,  1846,   687,  -533,
     621,  -533,  -533,   688,  -533,  -533,   436,   622,  1613,  2389,
    -533,  -533,   692,  -533,  -533,  -533,  3927,  -533,  4531,  -533,
    -533,  -533,  -533
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -533,  -533,  -533,   744,  -533,  -533,  -533,  -384,   544,   616,
    -533,     5,    62,   314,  -296,    75,    77,  -533,   274,  -533,
    -533,  -533,  -418,  -532,    80,    88,    99,   -69,   352,  -533,
     561,   111,  -372,   181,  -210,  -533,   176,   612,   133,  -533,
    -277,  -287,  -533,   643,  -533,  -533,   150,   322,  -533,   342,
     -40,  -533,  -533,  -533,  -380,   403,  -428,  -375,  -272,    -3,
    -213,   -96,    93,    -8,   -16,   -36,  -533,   131,  -533,   605,
      45,   307,   -10
};

/* YYTABLE[YYPACT[STATE-NUM]].  What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule which
   number is the opposite.  If zero, do what YYDEFACT says.
   If YYTABLE_NINF, syntax error.  */
#define YYTABLE_NINF -203
static const yytype_int16 yytable[] =
{
      41,   547,    51,   503,   424,   148,   429,   106,   634,   358,
      50,   440,   223,   398,   303,   634,   337,   338,    53,    54,
      55,    56,    57,    58,    59,    60,    64,    65,    66,   522,
     533,   385,   209,   272,   546,   158,   262,   192,   216,   156,
     228,   262,   159,   157,   152,   228,   554,   265,   210,   273,
     136,   216,   266,   268,   332,   439,   625,   165,   166,   167,
     168,   169,   170,   171,   172,   173,   174,   175,   176,   177,
     178,   179,   180,   181,   182,   183,   184,   185,   186,   187,
     188,   189,   190,   695,   216,     1,   194,   296,   575,    93,
     421,   345,   346,   155,   339,   148,    99,   580,   211,   100,
     101,   102,     8,   260,   588,   399,   634,   137,   392,   476,
     610,   212,   557,   267,   269,   433,   275,   193,   193,   193,
     138,   652,   139,   359,   360,   142,   638,    12,   731,   653,
     213,    94,    95,   143,   340,   368,   422,   429,   313,   193,
     136,   302,   307,    93,   144,   567,   312,    16,     2,     9,
      10,   310,    64,   225,   217,   218,   145,   193,   193,   637,
      36,   193,   193,   259,    14,   193,   193,   217,   259,   347,
     193,    46,   106,    36,   677,   678,   634,   259,   146,   193,
     193,   321,    43,   323,    44,    94,    95,   393,   518,   520,
      11,   611,   161,   612,    42,   164,   406,   137,   409,   576,
     412,   151,   542,   333,   336,   634,    36,    96,   193,   348,
     138,   341,   139,   154,   103,   142,   277,   663,    52,   394,
     261,   634,   708,   143,   370,   395,   377,   213,   214,   690,
      49,    69,    70,    71,   144,   193,   387,   388,    74,   224,
     391,   296,   301,    47,   461,   634,   145,   364,   193,   224,
      48,    49,   193,   296,   224,    36,   278,   407,   402,   410,
     191,   413,   482,   224,   225,   225,   223,   417,   146,   195,
     737,    90,    91,    92,   644,   366,   225,   367,   414,   259,
     415,   599,    48,    49,    74,   311,   259,   223,   334,   259,
     335,   753,    48,    49,   205,   434,   193,   259,   728,   441,
     442,   443,   728,   728,   444,   445,   446,   206,   534,   535,
     447,   706,   448,    87,    88,   450,    89,    90,    91,    92,
     226,   707,   538,   539,   462,   369,   371,   635,   479,   777,
     223,   468,   162,   587,   477,   163,   478,   474,   528,   465,
     698,   530,    48,    49,   532,   480,   193,    69,    70,    71,
     224,   224,   298,   486,   781,   227,   770,   429,   712,   196,
     193,   197,   224,   489,   228,   224,   497,   361,   362,   500,
     501,   502,   224,   262,   504,   224,   786,   427,   106,   509,
     404,   405,   106,   224,   296,   517,   276,    99,   519,   521,
     100,   101,   102,   525,   207,   432,   208,   451,   523,   438,
      74,   729,   309,   225,   310,   733,   735,   225,   408,   405,
     549,   452,   453,   454,   418,   553,   419,   455,   456,   457,
     259,   308,   556,   559,   558,   198,   199,   299,   225,   200,
     259,   565,    89,    90,    91,    92,   259,   322,   458,   572,
     253,   201,   202,   203,   324,   271,   204,   411,   405,    69,
      70,    71,    72,    73,   297,   325,   475,   487,   310,   524,
     259,   310,   328,   492,   259,   543,   581,   544,   785,   331,
     577,   225,   578,   593,   594,   459,   579,   583,   310,   584,
     597,   349,   350,   351,   352,   353,   354,   355,   356,   224,
     585,   327,   310,   224,   590,   330,   310,   606,   596,   618,
     310,   578,    74,   608,   609,   342,   224,   106,   614,   801,
     616,   296,   363,   619,   224,   310,   224,   624,   641,   208,
     208,   657,   224,   578,   364,   658,   627,   310,   630,    85,
      86,    87,    88,   365,    89,    90,    91,    92,   662,   259,
     578,   703,  -201,   208,  -201,   723,   224,   578,   376,  -200,
     224,  -200,  -202,   649,  -202,   378,   789,   224,   362,   796,
     379,   362,   386,   382,   435,   436,   527,   405,   529,   405,
     531,   405,   364,   563,   397,   566,   436,   604,   362,   621,
     405,   390,   665,   622,   405,   259,   400,   259,   416,   259,
     623,   405,   259,   403,   679,   646,   362,   651,   436,   380,
     381,   383,   384,   517,   296,   296,   389,   396,   401,   430,
     425,   193,   426,   420,   437,   431,   463,   491,   691,   692,
     693,   469,   697,   699,   449,   224,   481,   626,   483,   629,
     631,   632,   633,   484,   490,   493,   713,   494,   499,   506,
     223,   510,   717,   545,   259,   259,   551,   555,   560,   721,
     259,   561,   259,   564,   574,   582,   586,   589,   595,   592,
     223,   598,   620,   628,   640,   643,   647,   648,   433,   650,
     654,   224,   656,   224,   659,   224,   465,   664,   224,   661,
     259,   705,   471,   259,   668,   742,   686,   743,   687,   688,
     694,   700,   701,   709,   710,   718,   719,   496,   750,   720,
     725,   722,   726,   730,   739,   740,   744,   496,   745,   746,
     747,   748,   755,   512,   761,   296,   757,   765,   689,   768,
     759,   769,   773,   696,   774,   772,   775,   776,   779,   782,
     224,   224,   787,   259,   784,   788,   224,   790,   224,   791,
     714,   548,   697,   699,   793,   794,   797,   795,    13,   800,
     562,   300,   329,   259,   259,   591,   296,   526,   326,   655,
     660,   252,   306,   683,   550,   485,   224,   319,   573,   224,
     259,   259,     0,    17,    18,     0,   259,     0,   798,     0,
       0,   225,   259,     0,     0,   741,     0,    19,    20,    21,
       0,     0,   259,    22,    23,    24,     0,     0,   259,   749,
     751,   225,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    25,     0,     0,     0,     0,   224,
       0,     0,   259,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   259,    26,     0,     0,     0,   224,
     224,     0,     0,   780,     0,     0,     0,     0,     0,     0,
       0,    27,     0,     0,     0,     0,   224,   224,     0,    28,
      29,    30,   224,     0,   496,     0,   639,   224,   224,   642,
       0,     0,    31,    32,    33,     0,     0,     0,   224,     0,
       0,     0,    34,     0,   224,     0,     0,   224,     0,     0,
       0,    35,   464,     0,     0,     0,    36,     0,   465,     0,
       0,     0,    37,    38,     0,     0,     0,     0,   224,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
     224,   496,   671,     0,     0,     0,     0,   680,     0,   682,
       0,     0,     0,    17,    18,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    19,    20,    21,
       0,     0,     0,    22,    23,    24,     0,   496,     0,     0,
     704,   314,   315,     0,    74,     0,     0,     0,     0,     0,
       0,    75,    76,    77,    25,     0,     0,     0,     0,     0,
       0,     0,    78,   316,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,    26,    89,    90,    91,    92,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     738,    27,   317,     0,     0,     0,     0,     0,     0,    28,
      29,    30,     0,     0,     0,     0,     0,     0,     0,     0,
     752,   754,    31,    32,    33,     0,     0,     0,     0,     0,
       0,     0,    34,     0,     0,     0,     0,   762,   764,     0,
       0,    35,   470,   767,     0,     0,    36,     0,   471,   771,
       0,     0,    37,    38,    17,    18,     0,    17,    18,   778,
       0,     0,     0,     0,     0,   783,     0,     0,    19,    20,
      21,    19,    20,    21,    22,    23,    24,    22,    23,    24,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   792,
     513,   514,     0,     0,     0,    25,     0,     0,    25,     0,
       0,   799,     0,     0,     0,   727,   672,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    26,     0,     0,    26,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    27,     0,     0,    27,     0,     0,     0,     0,
      28,    29,    30,    28,    29,    30,     0,     0,     0,     0,
       0,     0,     0,    31,    32,    33,    31,    32,    33,     0,
       0,     0,     0,    34,     0,     0,    34,     0,     0,     0,
       0,     0,    35,     0,     0,    35,     0,    36,    17,    18,
      36,    17,    18,    37,    38,     0,    37,    38,     0,     0,
       0,     0,    19,    20,    21,    19,    20,    21,    22,    23,
      24,    22,    23,    24,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    25,
       0,     0,    25,     0,     0,     0,   732,   672,     0,   734,
     672,    17,    18,     0,     0,     0,     0,     0,     0,     0,
      26,     0,     0,    26,     0,    19,    20,    21,     0,     0,
       0,    22,    23,    24,     0,     0,    27,     0,     0,    27,
       0,     0,     0,     0,    28,    29,    30,    28,    29,    30,
       0,     0,    25,     0,     0,     0,     0,    31,    32,    33,
      31,    32,    33,     0,     0,     0,     0,    34,     0,     0,
      34,     0,     0,    26,     0,     0,    35,     0,     0,    35,
       0,    36,     0,     0,    36,     0,     0,    37,    38,    27,
      37,    38,     0,     0,     0,     0,     0,    28,    29,    30,
       0,     0,     0,    17,    18,     0,     0,     0,     0,     0,
      31,    32,    33,     0,     0,     0,    61,    19,    20,    21,
      34,     0,     0,    22,    23,    24,     0,     0,     0,    35,
       0,     0,     0,     0,    36,     0,     0,    17,    18,     0,
      37,    38,     0,     0,    25,     0,     0,     0,     0,     0,
       0,    19,    20,    21,     0,     0,     0,    22,    23,    24,
       0,     0,     0,     0,     0,    26,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    25,     0,
       0,    27,     0,     0,     0,     0,     0,     0,     0,    28,
      29,    30,     0,     0,     0,     0,     0,     0,     0,    26,
       0,     0,    31,    32,    33,     0,     0,     0,     0,     0,
       0,     0,    34,     0,     0,    27,     0,     0,     0,     0,
       0,    35,   488,    28,    29,    30,    36,    17,    18,     0,
       0,     0,    37,    38,     0,     0,    31,    32,    33,     0,
       0,    19,    20,    21,     0,     0,    34,    22,    23,    24,
       0,     0,     0,     0,   217,    35,     0,     0,     0,     0,
      36,    17,    18,     0,     0,     0,    37,    38,    25,     0,
       0,     0,     0,     0,     0,    19,    20,    21,     0,     0,
       0,    22,    23,    24,     0,     0,     0,     0,     0,    26,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    25,     0,     0,    27,     0,     0,     0,     0,
     672,     0,     0,    28,    29,    30,     0,     0,     0,     0,
       0,     0,     0,    26,     0,     0,    31,    32,    33,     0,
       0,     0,     0,     0,     0,     0,    34,     0,     0,    27,
       0,     0,     0,     0,     0,    35,     0,    28,    29,    30,
      36,     0,   465,    17,    18,     0,    37,    38,     0,     0,
      31,    32,    33,     0,     0,     0,     0,    19,    20,    21,
      34,     0,     0,    22,    23,    24,     0,     0,     0,    35,
       0,     0,     0,     0,    36,     0,     0,    17,    18,     0,
      37,    38,     0,     0,    25,     0,     0,     0,     0,     0,
       0,    19,    20,    21,     0,     0,     0,    22,    23,    24,
       0,     0,     0,     0,     0,    26,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    25,     0,
       0,    27,     0,     0,     0,     0,     0,     0,     0,    28,
      29,    30,     0,     0,     0,     0,     0,     0,     0,    26,
       0,     0,    31,    32,    33,     0,     0,     0,     0,     0,
       0,     0,    34,     0,     0,    27,     0,     0,     0,     0,
       0,    35,   716,    28,    29,    30,    36,     0,     0,     0,
       0,     0,    37,    38,     0,     0,    31,    32,    33,     0,
       0,     0,     0,     0,     0,   230,    34,   231,     0,     0,
       0,   232,     0,     0,     0,    35,     0,     0,     0,     0,
      36,   233,     0,     0,     0,     0,    37,    38,    67,    68,
      69,    70,    71,    72,    73,     0,   234,     0,   235,     0,
       0,     0,     0,   236,   237,     0,     0,     0,     0,   238,
     239,   240,     0,     0,     0,   241,     0,     0,     0,     0,
     242,   243,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   244,     0,   245,   126,     0,
       0,     0,     0,    74,     0,     0,     0,     0,   246,   247,
      75,    76,    77,   248,     0,     0,     0,   249,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,   250,     0,     0,   511,     0,     0,    36,     0,     0,
       0,   230,   251,   231,   534,   535,     0,   536,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   537,   538,   539,
       0,     0,   230,     0,   231,     0,     0,     0,   232,     0,
       0,     0,   234,     0,   235,     0,     0,     0,   233,   236,
     237,     0,     0,     0,     0,   238,   239,   240,     0,     0,
       0,   241,     0,   234,   372,   235,   242,   243,     0,     0,
     236,   237,     0,     0,     0,     0,   238,   239,   240,     0,
       0,   244,   241,   245,   126,     0,     0,   242,   243,     0,
       0,     0,     0,     0,   246,   247,     0,     0,     0,   248,
       0,     0,   244,   249,   245,   126,   230,     0,   231,     0,
       0,     0,   232,     0,     0,   246,   247,     0,     0,     0,
     248,     0,   233,     0,   249,     0,     0,   250,     0,   373,
       0,     0,     0,    36,     0,     0,     0,   234,   251,   235,
       0,     0,     0,     0,   236,   237,     0,     0,   250,     0,
     238,   239,   240,     0,    36,     0,   241,     0,     0,   251,
       0,   242,   243,     0,   230,     0,   231,     0,     0,     0,
     232,     0,     0,     0,     0,     0,   244,     0,   245,   126,
     233,     0,     0,     0,     0,     0,     0,     0,     0,   246,
     247,     0,     0,     0,   248,   234,   495,   235,   249,     0,
       0,     0,   236,   237,     0,     0,     0,     0,   238,   239,
     240,     0,     0,     0,   241,     0,     0,     0,     0,   242,
     243,     0,   250,     0,     0,   396,     0,     0,    36,   230,
       0,   231,     0,   251,   244,   232,   245,   126,     0,     0,
       0,     0,     0,     0,     0,   233,     0,   246,   247,     0,
       0,     0,   248,     0,     0,     0,   249,     0,     0,     0,
     234,     0,   235,     0,     0,     0,     0,   236,   237,     0,
       0,     0,     0,   238,   239,   240,     0,     0,     0,   241,
     250,     0,     0,     0,   242,   243,    36,   230,     0,   231,
       0,   251,     0,   232,     0,     0,     0,     0,     0,   244,
     505,   245,   126,   233,     0,     0,     0,     0,     0,     0,
       0,     0,   246,   247,     0,     0,     0,   248,   234,     0,
     235,   249,     0,     0,     0,   236,   237,     0,     0,     0,
       0,   238,   239,   240,     0,     0,     0,   241,     0,   636,
       0,     0,   242,   243,     0,   250,     0,     0,     0,     0,
       0,    36,   230,     0,   231,     0,   251,   244,   232,   245,
     126,     0,     0,     0,     0,     0,     0,     0,   233,     0,
     246,   247,     0,     0,     0,   248,     0,     0,     0,   249,
       0,     0,     0,   234,   670,   235,     0,     0,     0,     0,
     236,   237,     0,     0,     0,     0,   238,   239,   240,     0,
       0,     0,   241,   250,     0,     0,     0,   242,   243,    36,
     230,     0,   231,     0,   251,     0,   232,     0,     0,     0,
       0,     0,   244,     0,   245,   126,   233,     0,     0,     0,
       0,     0,     0,     0,     0,   246,   247,     0,     0,     0,
     248,   234,     0,   235,   249,     0,     0,     0,   236,   237,
       0,     0,     0,     0,   238,   239,   240,     0,     0,     0,
     241,     0,   702,     0,     0,   242,   243,     0,   250,     0,
       0,     0,     0,     0,    36,   230,     0,   231,     0,   251,
     244,   232,   245,   126,     0,     0,     0,     0,     0,     0,
       0,   233,     0,   246,   247,     0,     0,     0,   248,     0,
       0,     0,   249,     0,     0,     0,   234,     0,   235,     0,
       0,     0,     0,   236,   237,     0,     0,     0,     0,   238,
     239,   240,     0,     0,     0,   241,   250,     0,     0,     0,
     242,   243,    36,   230,     0,   231,     0,   251,     0,   232,
       0,     0,     0,     0,     0,   244,     0,   245,   126,   233,
       0,     0,     0,     0,   230,     0,   231,     0,   246,   247,
     232,     0,     0,   248,   234,     0,   235,   249,     0,     0,
     233,   236,   237,     0,     0,     0,     0,   238,   239,   240,
       0,     0,     0,   241,     0,   234,     0,   235,   242,   243,
       0,   250,   236,   237,   763,     0,     0,    36,   238,   239,
     240,     0,   251,   244,   241,   245,   126,     0,     0,   242,
     243,     0,     0,     0,     0,     0,   246,   247,     0,     0,
       0,   248,     0,     0,   244,   249,   245,   126,    67,    68,
      69,    70,    71,    72,    73,     0,     0,   246,   247,     0,
       0,     0,   248,     0,     0,     0,   249,     0,     0,   250,
       0,     0,   766,     0,     0,    36,     0,     0,     0,     0,
     251,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     250,     0,     0,     0,     0,     0,    36,     0,     0,     0,
       0,   251,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,    67,    68,    69,    70,    71,    72,    73,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,     0,    67,    68,    69,    70,    71,    72,
      73,   569,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,    74,
      89,    90,    91,    92,     0,     0,    75,    76,    77,    67,
      68,    69,    70,    71,    72,    73,   570,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,     0,     0,     0,     0,     0,
      67,    68,    69,    70,    71,    72,    73,   571,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    74,     0,     0,     0,     0,     0,
       0,    75,    76,    77,     0,     0,     0,     0,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,    74,    89,    90,    91,    92,
       0,     0,    75,    76,    77,     0,     0,     0,    36,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,     0,     0,     0,     0,     0,     0,   107,   507,   108,
     100,   101,   102,   109,   110,   111,   112,   113,   114,   115,
       0,     0,     0,   116,   117,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   118,   281,     0,
     282,     0,     0,     0,   119,     0,     0,     0,   120,   121,
     122,     0,     0,     0,     0,     0,   123,     0,     0,     0,
       0,     0,   283,    67,    68,    69,    70,    71,    72,    73,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     126,     0,     0,     0,     0,     0,     0,     0,     0,   284,
       0,     0,     0,     0,     0,     0,   129,   130,     0,     0,
     132,     0,   133,     0,   423,    67,    68,    69,    70,    71,
      72,    73,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,     0,   498,
      74,     0,     0,     0,     0,     0,     0,    75,    76,    77,
      67,    68,    69,    70,    71,    72,    73,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,     0,     0,     0,     0,
       0,   508,     0,     0,     0,     0,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    74,     0,     0,     0,     0,
       0,     0,    75,    76,    77,     0,     0,     0,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,    74,     0,     0,     0,     0,   615,     0,    75,    76,
      77,    67,    68,    69,    70,    71,    72,    73,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,     0,
       0,     0,   617,     0,     0,     0,     0,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    74,     0,     0,     0,
       0,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,    74,     0,     0,     0,     0,   666,     0,    75,
      76,    77,    67,    68,    69,    70,    71,    72,    73,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,     0,     0,
       0,     0,     0,   667,     0,     0,     0,     0,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    74,     0,     0,
       0,     0,     0,     0,    75,    76,    77,     0,     0,     0,
       0,     0,     0,     0,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,    74,     0,     0,     0,     0,   669,     0,
      75,    76,    77,    67,    68,    69,    70,    71,    72,    73,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,     0,   681,     0,     0,     0,     0,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,    74,     0,     0,     0,     0,   684,
       0,    75,    76,    77,    67,    68,    69,    70,    71,    72,
      73,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
       0,     0,     0,     0,     0,   685,     0,     0,     0,     0,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    74,
       0,     0,     0,     0,     0,     0,    75,    76,    77,     0,
       0,     0,     0,     0,     0,     0,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,    74,     0,     0,     0,     0,
     715,     0,    75,    76,    77,    67,    68,    69,    70,    71,
      72,    73,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,     0,     0,     0,     0,     0,   724,     0,     0,     0,
       0,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      74,     0,     0,     0,     0,     0,     0,    75,    76,    77,
       0,     0,     0,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,    74,     0,     0,     0,
       0,   736,     0,    75,    76,    77,     0,     0,     0,     0,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,     0,     0,     0,     0,   107,   756,   108,   100,
     101,   102,   109,   110,   111,   112,   113,   114,   115,     0,
       0,     0,   116,   117,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   118,     0,     0,     0,
       0,     0,     0,   119,     0,     0,     0,   120,   121,   122,
       0,     0,     0,     0,     0,   123,     0,   124,     0,   125,
       0,     0,     0,     0,     0,     0,     0,     2,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   126,
       0,    69,    70,    71,    72,    73,   127,     0,   128,     0,
       0,     0,     0,     0,     0,   129,   130,   131,     0,   132,
     107,   133,   108,   100,   101,   102,   109,   110,   111,   112,
     113,   114,   115,     0,     0,     0,   116,   117,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     118,   281,     0,   282,    74,     0,     0,   119,     0,     0,
       0,   120,   121,   122,     0,     0,     0,     0,     0,   123,
       0,     0,     0,     0,     0,   283,     0,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
       0,     0,     0,   126,    67,     0,    69,    70,    71,    72,
      73,   428,   284,     0,     0,     0,     0,     0,     0,   129,
     130,     0,     0,   132,   107,   133,   108,   100,   101,   102,
     109,   110,   111,   112,   113,   114,   115,     0,     0,     0,
     116,   117,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   118,   281,   552,   282,     0,    74,
       0,   119,     0,     0,     0,   120,   121,   122,     0,     0,
       0,     0,     0,   123,     0,     0,     0,     0,     0,   283,
       0,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,     0,     0,   126,    67,     0,
      69,    70,    71,    72,    73,     0,   284,     0,     0,     0,
       0,     0,     0,   129,   130,     0,     0,   132,   107,   133,
     108,   100,   101,   102,   109,   110,   111,   112,   113,   114,
     115,     0,     0,     0,   116,   117,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   118,   281,
     711,   282,     0,    74,     0,   119,     0,     0,     0,   120,
     121,   122,     0,     0,     0,     0,     0,   123,     0,     0,
       0,     0,     0,   283,     0,     0,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,   126,     0,     0,     0,     0,     0,     0,     0,     0,
     284,     0,     0,     0,     0,     0,     0,   129,   130,     0,
       0,   132,   107,   133,   108,   100,   101,   102,   109,   110,
     111,   112,   113,   114,   115,     0,     0,     0,   116,   117,
       0,     0,     0,    67,    68,    69,    70,    71,    72,    73,
       0,     0,   118,   281,     0,   282,     0,     0,     0,   119,
       0,     0,     0,   120,   121,   122,     0,     0,     0,     0,
       0,   123,     0,     0,     0,     0,     0,   283,     0,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   126,     0,     0,    74,     0,
       0,     0,     0,     0,   284,    75,    76,    77,     0,     0,
       0,   129,   130,     0,     0,   132,    78,   133,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,    74,     0,     0,     0,   160,     0,
       0,    75,    76,    77,    67,    68,    69,    70,    71,    72,
      73,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
       0,     0,     0,     0,   318,     0,     0,     0,     0,     0,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    74,
       0,     0,     0,     0,     0,     0,    75,    76,    77,     0,
       0,     0,     0,     0,     0,     0,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,    74,     0,     0,     0,   568,
       0,     0,    75,    76,    77,    67,    68,    69,    70,    71,
      72,    73,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,     0,     0,     0,     0,   600,     0,     0,     0,     0,
       0,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      74,     0,     0,     0,     0,     0,     0,    75,    76,    77,
       0,     0,     0,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,    74,     0,     0,     0,
     601,     0,     0,    75,    76,    77,    67,    68,    69,    70,
      71,    72,    73,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,     0,     0,     0,     0,   602,     0,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    74,     0,     0,     0,     0,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,     0,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,    74,     0,     0,
       0,   603,     0,     0,    75,    76,    77,    67,    68,    69,
      70,    71,    72,    73,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,     0,     0,     0,     0,   605,     0,     0,
       0,     0,     0,    67,    68,    69,    70,    71,    72,    73,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    74,     0,     0,     0,     0,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,     0,     0,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,    74,     0,
       0,     0,   607,     0,     0,    75,    76,    77,    67,    68,
      69,    70,    71,    72,    73,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,   645,     0,
       0,     0,     0,     0,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,    74,
       0,     0,     0,   758,     0,     0,    75,    76,    77,    67,
      68,    69,    70,    71,    72,    73,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,     0,     0,     0,     0,   760,
       0,     0,     0,     0,     0,     0,     0,     0,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    74,     0,     0,     0,     0,     0,
       0,    75,    76,    77,     0,     0,     0,     0,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
     314,   315,     0,    74,   802,     0,     0,     0,     0,     0,
      75,    76,    77,    67,    68,    69,    70,    71,    72,    73,
       0,    78,   316,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,     0,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,     0,     0,     0,    78,   320,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,    74,
      89,    90,    91,    92,     0,     0,    75,    76,    77,    67,
      68,    69,    70,    71,    72,    73,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,     0,     0,     0,     0,     0,
      67,     0,    69,    70,    71,    72,    73,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    74,     0,     0,     0,     0,     0,
       0,    75,    76,    77,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,    74,    89,    90,    91,    92,
       0,     0,    75,    76,    77,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92
};

static const yytype_int16 yycheck[] =
{
      10,   419,    18,   383,   281,    45,   293,    43,   540,   219,
      18,   307,   108,    34,     5,   547,     4,     5,    28,    29,
      30,    31,    32,    33,    34,    35,    36,    37,    38,   401,
     414,   244,     5,     5,   418,    51,     5,     5,     5,    49,
       5,     5,    52,    51,    47,     5,   426,    16,    21,    21,
      45,     5,   121,   122,     5,     5,    21,    67,    68,    69,
      70,    71,    72,    73,    74,    75,    76,    77,    78,    79,
      80,    81,    82,    83,    84,    85,    86,    87,    88,    89,
      90,    91,    92,     5,     5,     3,    94,   127,     5,     5,
      79,     4,     5,    48,    82,   135,     5,   469,   106,     8,
       9,    10,     5,     5,   476,   126,   638,    45,     5,   122,
      42,     5,   124,   121,   122,   126,   124,   130,   130,   130,
      45,   122,    45,   219,   220,    45,   544,     0,   102,   130,
     121,    47,    48,    45,   122,   231,   125,   424,   154,   130,
     135,   149,   150,     5,    45,   441,   154,     5,    66,     4,
       5,   125,   162,   108,   121,   122,    45,   130,   130,   543,
     127,   130,   130,   118,   121,   130,   130,   121,   123,    82,
     130,   117,   208,   127,   602,   603,   708,   132,    45,   130,
     130,   191,   122,   193,   124,    47,    48,    84,   398,   399,
      45,   123,    61,   125,   122,    64,   265,   135,   267,   116,
     269,     4,   415,   211,   212,   737,   127,   123,   130,   122,
     135,   214,   135,     5,   123,   135,     5,   589,   122,   116,
     122,   753,   640,   135,   232,   122,   236,   121,   122,   124,
     130,    30,    31,    32,   135,   130,   246,   247,    83,   108,
     250,   281,   149,   122,   126,   777,   135,   125,   130,   118,
     129,   130,   130,   293,   123,   127,    45,   265,   261,   267,
     126,   269,   358,   132,   219,   220,   362,   275,   135,     5,
     688,   116,   117,   118,   551,   122,   231,   124,   122,   234,
     124,   494,   129,   130,    83,   122,   241,   383,   122,   244,
     124,   709,   129,   130,    12,   303,   130,   252,   673,   307,
     310,   311,   677,   678,   314,   315,   316,   124,     8,     9,
     320,    11,   322,   112,   113,   325,   115,   116,   117,   118,
      16,    21,    22,    23,   332,   232,   233,   540,   344,   747,
     426,   334,   125,   123,   342,   128,   344,   340,   407,   129,
     124,   410,   129,   130,   413,   348,   130,    30,    31,    32,
     219,   220,    99,   363,   124,    16,   736,   644,   645,   123,
     130,   125,   231,   366,     5,   234,   376,   124,   125,   379,
     380,   381,   241,     5,   384,   244,   756,   284,   414,   389,
     124,   125,   418,   252,   424,   395,     5,     5,   398,   399,
       8,     9,    10,   403,   123,   302,   125,     4,   401,   306,
      83,   673,   123,   358,   125,   677,   678,   362,   124,   125,
     420,    18,    19,    20,   122,   425,   124,    24,    25,    26,
     375,     5,   430,   433,   432,    12,    13,     6,   383,    16,
     385,   439,   115,   116,   117,   118,   391,   126,    45,   449,
     118,    11,    12,    13,     5,   123,    16,   124,   125,    30,
      31,    32,    33,    34,   132,   126,   123,   364,   125,   123,
     415,   125,   124,   370,   419,   122,   469,   124,   755,     5,
     123,   426,   125,   483,   484,    82,   123,   123,   125,   125,
     490,    67,    68,    69,    70,    71,    72,    73,    74,   358,
     123,    16,   125,   362,   123,   126,   125,   507,   123,   123,
     125,   125,    83,   513,   514,     5,   375,   543,   518,   796,
     520,   551,   126,   123,   383,   125,   385,   123,   123,   125,
     125,   123,   391,   125,   125,   123,   534,   125,   536,   110,
     111,   112,   113,   124,   115,   116,   117,   118,   123,   494,
     125,   123,    57,   125,    59,   123,   415,   125,   122,    57,
     419,    59,    57,   563,    59,     5,   123,   426,   125,   123,
     122,   125,     5,   241,   124,   125,   124,   125,   124,   125,
     124,   125,   125,   126,   252,   124,   125,   124,   125,   124,
     125,     5,   592,   124,   125,   540,   124,   542,     5,   544,
     124,   125,   547,   126,   604,   124,   125,   124,   125,   122,
     122,   122,   122,   613,   644,   645,   122,   124,   122,    13,
     122,   130,   122,   126,     5,   124,     5,   124,   626,   627,
     628,   122,   630,   631,   126,   494,   125,   534,   126,   536,
     537,   538,   539,   126,   126,   124,   646,     5,   124,   124,
     736,   124,   652,     5,   599,   600,     5,   124,   124,   659,
     605,     5,   607,   124,   124,     5,   124,   122,   124,   126,
     756,   124,   124,    11,   124,    59,   127,   124,   126,   124,
     124,   540,   124,   542,   122,   544,   129,   123,   547,   124,
     635,    57,   129,   638,   124,   693,   124,   695,   124,   124,
     124,   124,   124,   124,    59,     4,   124,   375,   706,   124,
      39,   124,   102,    52,   124,   124,   124,   385,     5,   124,
     124,    57,    39,   391,   124,   755,   128,    52,   625,    52,
     131,    52,   124,   630,     5,    57,   124,   124,   124,    57,
     599,   600,     5,   688,    59,   122,   605,    57,   607,   124,
     647,   419,   750,   751,    57,   124,   124,    59,     4,    57,
     436,   135,   208,   708,   709,   481,   796,   405,   197,   578,
     584,   118,   150,   613,   422,   362,   635,   162,   461,   638,
     725,   726,    -1,     4,     5,    -1,   731,    -1,   788,    -1,
      -1,   736,   737,    -1,    -1,   692,    -1,    18,    19,    20,
      -1,    -1,   747,    24,    25,    26,    -1,    -1,   753,   706,
     707,   756,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    45,    -1,    -1,    -1,    -1,   688,
      -1,    -1,   777,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   789,    66,    -1,    -1,    -1,   708,
     709,    -1,    -1,   750,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    82,    -1,    -1,    -1,    -1,   725,   726,    -1,    90,
      91,    92,   731,    -1,   542,    -1,   544,   736,   737,   547,
      -1,    -1,   103,   104,   105,    -1,    -1,    -1,   747,    -1,
      -1,    -1,   113,    -1,   753,    -1,    -1,   756,    -1,    -1,
      -1,   122,   123,    -1,    -1,    -1,   127,    -1,   129,    -1,
      -1,    -1,   133,   134,    -1,    -1,    -1,    -1,   777,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
     789,   599,   600,    -1,    -1,    -1,    -1,   605,    -1,   607,
      -1,    -1,    -1,     4,     5,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    18,    19,    20,
      -1,    -1,    -1,    24,    25,    26,    -1,   635,    -1,    -1,
     638,    80,    81,    -1,    83,    -1,    -1,    -1,    -1,    -1,
      -1,    90,    91,    92,    45,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   101,   102,   103,   104,   105,   106,    -1,   108,
     109,   110,   111,   112,   113,    66,   115,   116,   117,   118,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     688,    82,   131,    -1,    -1,    -1,    -1,    -1,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     708,   709,   103,   104,   105,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   113,    -1,    -1,    -1,    -1,   725,   726,    -1,
      -1,   122,   123,   731,    -1,    -1,   127,    -1,   129,   737,
      -1,    -1,   133,   134,     4,     5,    -1,     4,     5,   747,
      -1,    -1,    -1,    -1,    -1,   753,    -1,    -1,    18,    19,
      20,    18,    19,    20,    24,    25,    26,    24,    25,    26,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   777,
      40,    41,    -1,    -1,    -1,    45,    -1,    -1,    45,    -1,
      -1,   789,    -1,    -1,    -1,    52,    53,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    66,    -1,    -1,    66,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    82,    -1,    -1,    82,    -1,    -1,    -1,    -1,
      90,    91,    92,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   103,   104,   105,   103,   104,   105,    -1,
      -1,    -1,    -1,   113,    -1,    -1,   113,    -1,    -1,    -1,
      -1,    -1,   122,    -1,    -1,   122,    -1,   127,     4,     5,
     127,     4,     5,   133,   134,    -1,   133,   134,    -1,    -1,
      -1,    -1,    18,    19,    20,    18,    19,    20,    24,    25,
      26,    24,    25,    26,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    45,
      -1,    -1,    45,    -1,    -1,    -1,    52,    53,    -1,    52,
      53,     4,     5,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      66,    -1,    -1,    66,    -1,    18,    19,    20,    -1,    -1,
      -1,    24,    25,    26,    -1,    -1,    82,    -1,    -1,    82,
      -1,    -1,    -1,    -1,    90,    91,    92,    90,    91,    92,
      -1,    -1,    45,    -1,    -1,    -1,    -1,   103,   104,   105,
     103,   104,   105,    -1,    -1,    -1,    -1,   113,    -1,    -1,
     113,    -1,    -1,    66,    -1,    -1,   122,    -1,    -1,   122,
      -1,   127,    -1,    -1,   127,    -1,    -1,   133,   134,    82,
     133,   134,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,
      -1,    -1,    -1,     4,     5,    -1,    -1,    -1,    -1,    -1,
     103,   104,   105,    -1,    -1,    -1,   109,    18,    19,    20,
     113,    -1,    -1,    24,    25,    26,    -1,    -1,    -1,   122,
      -1,    -1,    -1,    -1,   127,    -1,    -1,     4,     5,    -1,
     133,   134,    -1,    -1,    45,    -1,    -1,    -1,    -1,    -1,
      -1,    18,    19,    20,    -1,    -1,    -1,    24,    25,    26,
      -1,    -1,    -1,    -1,    -1,    66,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    45,    -1,
      -1,    82,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    66,
      -1,    -1,   103,   104,   105,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   113,    -1,    -1,    82,    -1,    -1,    -1,    -1,
      -1,   122,   123,    90,    91,    92,   127,     4,     5,    -1,
      -1,    -1,   133,   134,    -1,    -1,   103,   104,   105,    -1,
      -1,    18,    19,    20,    -1,    -1,   113,    24,    25,    26,
      -1,    -1,    -1,    -1,   121,   122,    -1,    -1,    -1,    -1,
     127,     4,     5,    -1,    -1,    -1,   133,   134,    45,    -1,
      -1,    -1,    -1,    -1,    -1,    18,    19,    20,    -1,    -1,
      -1,    24,    25,    26,    -1,    -1,    -1,    -1,    -1,    66,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    45,    -1,    -1,    82,    -1,    -1,    -1,    -1,
      53,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    66,    -1,    -1,   103,   104,   105,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   113,    -1,    -1,    82,
      -1,    -1,    -1,    -1,    -1,   122,    -1,    90,    91,    92,
     127,    -1,   129,     4,     5,    -1,   133,   134,    -1,    -1,
     103,   104,   105,    -1,    -1,    -1,    -1,    18,    19,    20,
     113,    -1,    -1,    24,    25,    26,    -1,    -1,    -1,   122,
      -1,    -1,    -1,    -1,   127,    -1,    -1,     4,     5,    -1,
     133,   134,    -1,    -1,    45,    -1,    -1,    -1,    -1,    -1,
      -1,    18,    19,    20,    -1,    -1,    -1,    24,    25,    26,
      -1,    -1,    -1,    -1,    -1,    66,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    45,    -1,
      -1,    82,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    66,
      -1,    -1,   103,   104,   105,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   113,    -1,    -1,    82,    -1,    -1,    -1,    -1,
      -1,   122,   123,    90,    91,    92,   127,    -1,    -1,    -1,
      -1,    -1,   133,   134,    -1,    -1,   103,   104,   105,    -1,
      -1,    -1,    -1,    -1,    -1,     5,   113,     7,    -1,    -1,
      -1,    11,    -1,    -1,    -1,   122,    -1,    -1,    -1,    -1,
     127,    21,    -1,    -1,    -1,    -1,   133,   134,    28,    29,
      30,    31,    32,    33,    34,    -1,    36,    -1,    38,    -1,
      -1,    -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,
      50,    51,    -1,    -1,    -1,    55,    -1,    -1,    -1,    -1,
      60,    61,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    75,    -1,    77,    78,    -1,
      -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    88,    89,
      90,    91,    92,    93,    -1,    -1,    -1,    97,    -1,    -1,
      -1,   101,    -1,   103,   104,   105,   106,    -1,   108,   109,
     110,   111,   112,   113,    -1,   115,   116,   117,   118,    -1,
      -1,   121,    -1,    -1,   124,    -1,    -1,   127,    -1,    -1,
      -1,     5,   132,     7,     8,     9,    -1,    11,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    21,    22,    23,
      -1,    -1,     5,    -1,     7,    -1,    -1,    -1,    11,    -1,
      -1,    -1,    36,    -1,    38,    -1,    -1,    -1,    21,    43,
      44,    -1,    -1,    -1,    -1,    49,    50,    51,    -1,    -1,
      -1,    55,    -1,    36,    37,    38,    60,    61,    -1,    -1,
      43,    44,    -1,    -1,    -1,    -1,    49,    50,    51,    -1,
      -1,    75,    55,    77,    78,    -1,    -1,    60,    61,    -1,
      -1,    -1,    -1,    -1,    88,    89,    -1,    -1,    -1,    93,
      -1,    -1,    75,    97,    77,    78,     5,    -1,     7,    -1,
      -1,    -1,    11,    -1,    -1,    88,    89,    -1,    -1,    -1,
      93,    -1,    21,    -1,    97,    -1,    -1,   121,    -1,   102,
      -1,    -1,    -1,   127,    -1,    -1,    -1,    36,   132,    38,
      -1,    -1,    -1,    -1,    43,    44,    -1,    -1,   121,    -1,
      49,    50,    51,    -1,   127,    -1,    55,    -1,    -1,   132,
      -1,    60,    61,    -1,     5,    -1,     7,    -1,    -1,    -1,
      11,    -1,    -1,    -1,    -1,    -1,    75,    -1,    77,    78,
      21,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    88,
      89,    -1,    -1,    -1,    93,    36,    37,    38,    97,    -1,
      -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,    50,
      51,    -1,    -1,    -1,    55,    -1,    -1,    -1,    -1,    60,
      61,    -1,   121,    -1,    -1,   124,    -1,    -1,   127,     5,
      -1,     7,    -1,   132,    75,    11,    77,    78,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    21,    -1,    88,    89,    -1,
      -1,    -1,    93,    -1,    -1,    -1,    97,    -1,    -1,    -1,
      36,    -1,    38,    -1,    -1,    -1,    -1,    43,    44,    -1,
      -1,    -1,    -1,    49,    50,    51,    -1,    -1,    -1,    55,
     121,    -1,    -1,    -1,    60,    61,   127,     5,    -1,     7,
      -1,   132,    -1,    11,    -1,    -1,    -1,    -1,    -1,    75,
      76,    77,    78,    21,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    88,    89,    -1,    -1,    -1,    93,    36,    -1,
      38,    97,    -1,    -1,    -1,    43,    44,    -1,    -1,    -1,
      -1,    49,    50,    51,    -1,    -1,    -1,    55,    -1,    57,
      -1,    -1,    60,    61,    -1,   121,    -1,    -1,    -1,    -1,
      -1,   127,     5,    -1,     7,    -1,   132,    75,    11,    77,
      78,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    21,    -1,
      88,    89,    -1,    -1,    -1,    93,    -1,    -1,    -1,    97,
      -1,    -1,    -1,    36,    37,    38,    -1,    -1,    -1,    -1,
      43,    44,    -1,    -1,    -1,    -1,    49,    50,    51,    -1,
      -1,    -1,    55,   121,    -1,    -1,    -1,    60,    61,   127,
       5,    -1,     7,    -1,   132,    -1,    11,    -1,    -1,    -1,
      -1,    -1,    75,    -1,    77,    78,    21,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    88,    89,    -1,    -1,    -1,
      93,    36,    -1,    38,    97,    -1,    -1,    -1,    43,    44,
      -1,    -1,    -1,    -1,    49,    50,    51,    -1,    -1,    -1,
      55,    -1,    57,    -1,    -1,    60,    61,    -1,   121,    -1,
      -1,    -1,    -1,    -1,   127,     5,    -1,     7,    -1,   132,
      75,    11,    77,    78,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    21,    -1,    88,    89,    -1,    -1,    -1,    93,    -1,
      -1,    -1,    97,    -1,    -1,    -1,    36,    -1,    38,    -1,
      -1,    -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,
      50,    51,    -1,    -1,    -1,    55,   121,    -1,    -1,    -1,
      60,    61,   127,     5,    -1,     7,    -1,   132,    -1,    11,
      -1,    -1,    -1,    -1,    -1,    75,    -1,    77,    78,    21,
      -1,    -1,    -1,    -1,     5,    -1,     7,    -1,    88,    89,
      11,    -1,    -1,    93,    36,    -1,    38,    97,    -1,    -1,
      21,    43,    44,    -1,    -1,    -1,    -1,    49,    50,    51,
      -1,    -1,    -1,    55,    -1,    36,    -1,    38,    60,    61,
      -1,   121,    43,    44,   124,    -1,    -1,   127,    49,    50,
      51,    -1,   132,    75,    55,    77,    78,    -1,    -1,    60,
      61,    -1,    -1,    -1,    -1,    -1,    88,    89,    -1,    -1,
      -1,    93,    -1,    -1,    75,    97,    77,    78,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    88,    89,    -1,
      -1,    -1,    93,    -1,    -1,    -1,    97,    -1,    -1,   121,
      -1,    -1,   124,    -1,    -1,   127,    -1,    -1,    -1,    -1,
     132,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     121,    -1,    -1,    -1,    -1,    -1,   127,    -1,    -1,    -1,
      -1,   132,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,
      90,    91,    92,    28,    29,    30,    31,    32,    33,    34,
      -1,   101,    -1,   103,   104,   105,   106,    -1,   108,   109,
     110,   111,   112,   113,    -1,   115,   116,   117,   118,    -1,
      -1,    -1,    -1,    -1,    28,    29,    30,    31,    32,    33,
      34,   131,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,
      -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   101,    -1,   103,   104,
     105,   106,    -1,   108,   109,   110,   111,   112,   113,    83,
     115,   116,   117,   118,    -1,    -1,    90,    91,    92,    28,
      29,    30,    31,    32,    33,    34,   131,   101,    -1,   103,
     104,   105,   106,    -1,   108,   109,   110,   111,   112,   113,
      -1,   115,   116,   117,   118,    -1,    -1,    -1,    -1,    -1,
      28,    29,    30,    31,    32,    33,    34,   131,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,
      -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   101,    -1,   103,   104,   105,   106,    -1,   108,
     109,   110,   111,   112,   113,    83,   115,   116,   117,   118,
      -1,    -1,    90,    91,    92,    -1,    -1,    -1,   127,    -1,
      -1,    -1,    -1,   101,    -1,   103,   104,   105,   106,    -1,
     108,   109,   110,   111,   112,   113,    -1,   115,   116,   117,
     118,    -1,    -1,    -1,    -1,    -1,    -1,     5,   126,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    16,    17,
      -1,    -1,    -1,    21,    22,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    35,    36,    -1,
      38,    -1,    -1,    -1,    42,    -1,    -1,    -1,    46,    47,
      48,    -1,    -1,    -1,    -1,    -1,    54,    -1,    -1,    -1,
      -1,    -1,    60,    28,    29,    30,    31,    32,    33,    34,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      78,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    87,
      -1,    -1,    -1,    -1,    -1,    -1,    94,    95,    -1,    -1,
      98,    -1,   100,    -1,   102,    28,    29,    30,    31,    32,
      33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,
      -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   101,    -1,   103,   104,
     105,   106,    -1,   108,   109,   110,   111,   112,   113,    -1,
     115,   116,   117,   118,    -1,    -1,    -1,    -1,    -1,   124,
      83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,
      28,    29,    30,    31,    32,    33,    34,    -1,   101,    -1,
     103,   104,   105,   106,    -1,   108,   109,   110,   111,   112,
     113,    -1,   115,   116,   117,   118,    -1,    -1,    -1,    -1,
      -1,   124,    -1,    -1,    -1,    -1,    28,    29,    30,    31,
      32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,
      -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   101,    -1,   103,   104,   105,   106,    -1,
     108,   109,   110,   111,   112,   113,    -1,   115,   116,   117,
     118,    83,    -1,    -1,    -1,    -1,   124,    -1,    90,    91,
      92,    28,    29,    30,    31,    32,    33,    34,    -1,   101,
      -1,   103,   104,   105,   106,    -1,   108,   109,   110,   111,
     112,   113,    -1,   115,   116,   117,   118,    -1,    -1,    -1,
      -1,    -1,   124,    -1,    -1,    -1,    -1,    28,    29,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   101,    -1,   103,   104,   105,   106,
      -1,   108,   109,   110,   111,   112,   113,    -1,   115,   116,
     117,   118,    83,    -1,    -1,    -1,    -1,   124,    -1,    90,
      91,    92,    28,    29,    30,    31,    32,    33,    34,    -1,
     101,    -1,   103,   104,   105,   106,    -1,   108,   109,   110,
     111,   112,   113,    -1,   115,   116,   117,   118,    -1,    -1,
      -1,    -1,    -1,   124,    -1,    -1,    -1,    -1,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,
      -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   101,    -1,   103,   104,   105,
     106,    -1,   108,   109,   110,   111,   112,   113,    -1,   115,
     116,   117,   118,    83,    -1,    -1,    -1,    -1,   124,    -1,
      90,    91,    92,    28,    29,    30,    31,    32,    33,    34,
      -1,   101,    -1,   103,   104,   105,   106,    -1,   108,   109,
     110,   111,   112,   113,    -1,   115,   116,   117,   118,    -1,
      -1,    -1,    -1,    -1,   124,    -1,    -1,    -1,    -1,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,
      -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   101,    -1,   103,   104,
     105,   106,    -1,   108,   109,   110,   111,   112,   113,    -1,
     115,   116,   117,   118,    83,    -1,    -1,    -1,    -1,   124,
      -1,    90,    91,    92,    28,    29,    30,    31,    32,    33,
      34,    -1,   101,    -1,   103,   104,   105,   106,    -1,   108,
     109,   110,   111,   112,   113,    -1,   115,   116,   117,   118,
      -1,    -1,    -1,    -1,    -1,   124,    -1,    -1,    -1,    -1,
      28,    29,    30,    31,    32,    33,    34,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,
      -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   101,    -1,   103,
     104,   105,   106,    -1,   108,   109,   110,   111,   112,   113,
      -1,   115,   116,   117,   118,    83,    -1,    -1,    -1,    -1,
     124,    -1,    90,    91,    92,    28,    29,    30,    31,    32,
      33,    34,    -1,   101,    -1,   103,   104,   105,   106,    -1,
     108,   109,   110,   111,   112,   113,    -1,   115,   116,   117,
     118,    -1,    -1,    -1,    -1,    -1,   124,    -1,    -1,    -1,
      -1,    28,    29,    30,    31,    32,    33,    34,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   101,    -1,
     103,   104,   105,   106,    -1,   108,   109,   110,   111,   112,
     113,    -1,   115,   116,   117,   118,    83,    -1,    -1,    -1,
      -1,   124,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   101,    -1,   103,   104,   105,   106,
      -1,   108,   109,   110,   111,   112,   113,    -1,   115,   116,
     117,   118,    -1,    -1,    -1,    -1,     5,   124,     7,     8,
       9,    10,    11,    12,    13,    14,    15,    16,    17,    -1,
      -1,    -1,    21,    22,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    35,    -1,    -1,    -1,
      -1,    -1,    -1,    42,    -1,    -1,    -1,    46,    47,    48,
      -1,    -1,    -1,    -1,    -1,    54,    -1,    56,    -1,    58,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    66,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    78,
      -1,    30,    31,    32,    33,    34,    85,    -1,    87,    -1,
      -1,    -1,    -1,    -1,    -1,    94,    95,    96,    -1,    98,
       5,   100,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    -1,    -1,    -1,    21,    22,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      35,    36,    -1,    38,    83,    -1,    -1,    42,    -1,    -1,
      -1,    46,    47,    48,    -1,    -1,    -1,    -1,    -1,    54,
      -1,    -1,    -1,    -1,    -1,    60,    -1,   106,    -1,   108,
     109,   110,   111,   112,   113,    -1,   115,   116,   117,   118,
      -1,    -1,    -1,    78,    28,    -1,    30,    31,    32,    33,
      34,    86,    87,    -1,    -1,    -1,    -1,    -1,    -1,    94,
      95,    -1,    -1,    98,     5,   100,     7,     8,     9,    10,
      11,    12,    13,    14,    15,    16,    17,    -1,    -1,    -1,
      21,    22,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    35,    36,    37,    38,    -1,    83,
      -1,    42,    -1,    -1,    -1,    46,    47,    48,    -1,    -1,
      -1,    -1,    -1,    54,    -1,    -1,    -1,    -1,    -1,    60,
      -1,   105,   106,    -1,   108,   109,   110,   111,   112,   113,
      -1,   115,   116,   117,   118,    -1,    -1,    78,    28,    -1,
      30,    31,    32,    33,    34,    -1,    87,    -1,    -1,    -1,
      -1,    -1,    -1,    94,    95,    -1,    -1,    98,     5,   100,
       7,     8,     9,    10,    11,    12,    13,    14,    15,    16,
      17,    -1,    -1,    -1,    21,    22,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    35,    36,
      37,    38,    -1,    83,    -1,    42,    -1,    -1,    -1,    46,
      47,    48,    -1,    -1,    -1,    -1,    -1,    54,    -1,    -1,
      -1,    -1,    -1,    60,    -1,    -1,   106,    -1,   108,   109,
     110,   111,   112,   113,    -1,   115,   116,   117,   118,    -1,
      -1,    78,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      87,    -1,    -1,    -1,    -1,    -1,    -1,    94,    95,    -1,
      -1,    98,     5,   100,     7,     8,     9,    10,    11,    12,
      13,    14,    15,    16,    17,    -1,    -1,    -1,    21,    22,
      -1,    -1,    -1,    28,    29,    30,    31,    32,    33,    34,
      -1,    -1,    35,    36,    -1,    38,    -1,    -1,    -1,    42,
      -1,    -1,    -1,    46,    47,    48,    -1,    -1,    -1,    -1,
      -1,    54,    -1,    -1,    -1,    -1,    -1,    60,    -1,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    78,    -1,    -1,    83,    -1,
      -1,    -1,    -1,    -1,    87,    90,    91,    92,    -1,    -1,
      -1,    94,    95,    -1,    -1,    98,   101,   100,   103,   104,
     105,   106,    -1,   108,   109,   110,   111,   112,   113,    -1,
     115,   116,   117,   118,    83,    -1,    -1,    -1,   123,    -1,
      -1,    90,    91,    92,    28,    29,    30,    31,    32,    33,
      34,    -1,   101,    -1,   103,   104,   105,   106,    -1,   108,
     109,   110,   111,   112,   113,    -1,   115,   116,   117,   118,
      -1,    -1,    -1,    -1,   123,    -1,    -1,    -1,    -1,    -1,
      28,    29,    30,    31,    32,    33,    34,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,
      -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   101,    -1,   103,
     104,   105,   106,    -1,   108,   109,   110,   111,   112,   113,
      -1,   115,   116,   117,   118,    83,    -1,    -1,    -1,   123,
      -1,    -1,    90,    91,    92,    28,    29,    30,    31,    32,
      33,    34,    -1,   101,    -1,   103,   104,   105,   106,    -1,
     108,   109,   110,   111,   112,   113,    -1,   115,   116,   117,
     118,    -1,    -1,    -1,    -1,   123,    -1,    -1,    -1,    -1,
      -1,    28,    29,    30,    31,    32,    33,    34,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   101,    -1,
     103,   104,   105,   106,    -1,   108,   109,   110,   111,   112,
     113,    -1,   115,   116,   117,   118,    83,    -1,    -1,    -1,
     123,    -1,    -1,    90,    91,    92,    28,    29,    30,    31,
      32,    33,    34,    -1,   101,    -1,   103,   104,   105,   106,
      -1,   108,   109,   110,   111,   112,   113,    -1,   115,   116,
     117,   118,    -1,    -1,    -1,    -1,   123,    -1,    -1,    -1,
      -1,    -1,    28,    29,    30,    31,    32,    33,    34,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,
      92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   101,
      -1,   103,   104,   105,   106,    -1,   108,   109,   110,   111,
     112,   113,    -1,   115,   116,   117,   118,    83,    -1,    -1,
      -1,   123,    -1,    -1,    90,    91,    92,    28,    29,    30,
      31,    32,    33,    34,    -1,   101,    -1,   103,   104,   105,
     106,    -1,   108,   109,   110,   111,   112,   113,    -1,   115,
     116,   117,   118,    -1,    -1,    -1,    -1,   123,    -1,    -1,
      -1,    -1,    -1,    28,    29,    30,    31,    32,    33,    34,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     101,    -1,   103,   104,   105,   106,    -1,   108,   109,   110,
     111,   112,   113,    -1,   115,   116,   117,   118,    83,    -1,
      -1,    -1,   123,    -1,    -1,    90,    91,    92,    28,    29,
      30,    31,    32,    33,    34,    -1,   101,    -1,   103,   104,
     105,   106,    -1,   108,   109,   110,   111,   112,   113,    -1,
     115,   116,   117,   118,    -1,    -1,    -1,    -1,   123,    -1,
      -1,    -1,    -1,    -1,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   101,    -1,   103,   104,   105,   106,    -1,   108,   109,
     110,   111,   112,   113,    -1,   115,   116,   117,   118,    83,
      -1,    -1,    -1,   123,    -1,    -1,    90,    91,    92,    28,
      29,    30,    31,    32,    33,    34,    -1,   101,    -1,   103,
     104,   105,   106,    -1,   108,   109,   110,   111,   112,   113,
      -1,   115,   116,   117,   118,    -1,    -1,    -1,    -1,   123,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,
      -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   101,    -1,   103,   104,   105,   106,    -1,   108,
     109,   110,   111,   112,   113,    -1,   115,   116,   117,   118,
      80,    81,    -1,    83,   123,    -1,    -1,    -1,    -1,    -1,
      90,    91,    92,    28,    29,    30,    31,    32,    33,    34,
      -1,   101,   102,   103,   104,   105,   106,    -1,   108,   109,
     110,   111,   112,   113,    -1,   115,   116,   117,   118,    -1,
      -1,    -1,    -1,    -1,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,
      -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   101,   102,   103,   104,
     105,   106,    -1,   108,   109,   110,   111,   112,   113,    83,
     115,   116,   117,   118,    -1,    -1,    90,    91,    92,    28,
      29,    30,    31,    32,    33,    34,    -1,   101,    -1,   103,
     104,   105,   106,    -1,   108,   109,   110,   111,   112,   113,
      -1,   115,   116,   117,   118,    -1,    -1,    -1,    -1,    -1,
      28,    -1,    30,    31,    32,    33,    34,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,
      -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   104,   105,   106,    -1,   108,
     109,   110,   111,   112,   113,    83,   115,   116,   117,   118,
      -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   104,   105,   106,    -1,
     108,   109,   110,   111,   112,   113,    -1,   115,   116,   117,
     118
};

/* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
   symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,     3,    66,   136,   137,   138,   139,   146,     5,     4,
       5,    45,     0,   138,   121,   140,     5,     4,     5,    18,
      19,    20,    24,    25,    26,    45,    66,    82,    90,    91,
      92,   103,   104,   105,   113,   122,   127,   133,   134,   202,
     205,   207,   122,   122,   124,   141,   117,   122,   129,   130,
     198,   199,   122,   207,   207,   207,   207,   207,   207,   207,
     207,   109,   203,   204,   207,   207,   207,    28,    29,    30,
      31,    32,    33,    34,    83,    90,    91,    92,   101,   103,
     104,   105,   106,   108,   109,   110,   111,   112,   113,   115,
     116,   117,   118,     5,    47,    48,   123,   164,   165,     5,
       8,     9,    10,   123,   142,   143,   200,     5,     7,    11,
      12,    13,    14,    15,    16,    17,    21,    22,    35,    42,
      46,    47,    48,    54,    56,    58,    78,    85,    87,    94,
      95,    96,    98,   100,   144,   145,   146,   147,   150,   151,
     155,   156,   159,   160,   161,   166,   173,   174,   185,   200,
     201,     4,   194,   207,     5,   205,   207,   198,   199,   207,
     123,   202,   125,   128,   202,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   126,     5,   130,   198,     5,   123,   125,    12,    13,
      16,    11,    12,    13,    16,    12,   124,   123,   125,     5,
      21,   198,     5,   121,   122,   172,     5,   121,   122,   152,
     169,   189,   190,   196,   202,   205,    16,    16,     5,   197,
       5,     7,    11,    21,    36,    38,    43,    44,    49,    50,
      51,    55,    60,    61,    75,    77,    88,    89,    93,    97,
     121,   132,   178,   182,   185,   186,   187,   188,   196,   205,
       5,   122,     5,   162,   163,    16,   162,   198,   162,   198,
     178,   182,     5,    21,   154,   198,     5,     5,    45,   183,
     184,    36,    38,    60,    87,   147,   150,   151,   159,   160,
     161,   166,   173,   175,   176,   177,   185,   182,    99,     6,
     144,   197,   198,     5,   148,   149,   172,   198,     5,   123,
     125,   122,   198,   199,    80,    81,   102,   131,   123,   204,
     102,   207,   126,   207,     5,   126,   165,    16,   124,   143,
     126,     5,     5,   198,   122,   124,   198,     4,     5,    82,
     122,   194,     5,   198,   199,     4,     5,    82,   122,    67,
      68,    69,    70,    71,    72,    73,    74,   153,   169,   196,
     196,   124,   125,   126,   125,   124,   122,   124,   196,   197,
     198,   197,    37,   102,   182,   195,   122,   207,     5,   122,
     122,   122,   182,   122,   122,   195,     5,   207,   207,   122,
       5,   207,     5,    84,   116,   122,   124,   182,    34,   126,
     124,   122,   194,   126,   124,   125,   162,   198,   124,   162,
     198,   124,   162,   198,   122,   124,     5,   198,   122,   124,
     126,    79,   125,   102,   175,   122,   122,   197,    86,   176,
      13,   124,   197,   126,   198,   124,   125,     5,   197,     5,
     149,   198,   207,   207,   207,   207,   207,   207,   207,   126,
     207,     4,    18,    19,    20,    24,    25,    26,    45,    82,
     206,   126,   198,     5,   123,   129,   167,   168,   194,   122,
     123,   129,   170,   171,   194,   123,   122,   198,   198,   199,
     194,   125,   196,   126,   126,   190,   207,   197,   123,   194,
     126,   124,   197,   124,     5,    37,   182,   207,   124,   124,
     207,   207,   207,   189,   207,    76,   124,   126,   124,   207,
     124,   124,   182,    40,    41,   180,   181,   207,   169,   207,
     169,   207,   167,   194,   123,   207,   163,   124,   162,   124,
     162,   124,   162,   142,     8,     9,    11,    21,    22,    23,
     157,   158,   195,   122,   124,     5,   142,   157,   182,   207,
     184,     5,    37,   207,   189,   124,   198,   124,   198,   207,
     124,     5,   148,   126,   124,   198,   124,   149,   123,   131,
     131,   131,   207,   206,   124,     5,   116,   123,   125,   123,
     167,   194,     5,   123,   125,   123,   124,   123,   167,   122,
     123,   153,   126,   207,   207,   124,   123,   207,   124,   195,
     123,   123,   123,   123,   124,   123,   207,   123,   207,   207,
      42,   123,   125,   179,   207,   124,   207,   124,   123,   123,
     124,   124,   124,   124,   123,    21,   197,   198,    11,   197,
     198,   197,   197,   197,   158,   195,    57,   142,   157,   182,
     124,   123,   182,    59,   175,   123,   124,   127,   124,   207,
     124,   124,   122,   130,   124,   168,   124,   123,   123,   122,
     171,   124,   123,   167,   123,   207,   124,   124,   124,   124,
      37,   182,    53,   191,   192,   193,   194,   191,   191,   207,
     182,   124,   182,   181,   124,   124,   124,   124,   124,   197,
     124,   198,   198,   198,   124,     5,   197,   198,   124,   198,
     124,   124,    57,   123,   182,    57,    11,    21,   157,   124,
      59,    37,   176,   207,   197,   124,   123,   207,     4,   124,
     124,   207,   124,   123,   124,    39,   102,    52,   192,   193,
      52,   102,    52,   193,    52,   193,   124,   157,   182,   124,
     124,   197,   198,   198,   124,     5,   124,   124,    57,   197,
     198,   197,   182,   157,   182,    39,   124,   128,   123,   131,
     123,   124,   182,   124,   182,    52,   124,   182,    52,    52,
     189,   182,    57,   124,     5,   124,   124,   157,   182,   124,
     197,   124,    57,   182,    59,   176,   189,     5,   122,   123,
      57,   124,   182,    57,   124,    59,   123,   124,   207,   182,
      57,   176,   123
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
#line 3074 "y.tab.c"
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


#line 386 "yaccs/verilog.yacc"


