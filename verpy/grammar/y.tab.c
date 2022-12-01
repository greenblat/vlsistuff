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
#define YYLAST   4938

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  135
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  73
/* YYNRULES -- Number of rules.  */
#define YYNRULES  365
/* YYNRULES -- Number of states.  */
#define YYNSTATES  820

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
      64,    69,    75,    77,    82,    88,    91,    92,    94,    96,
      98,   100,   102,   104,   106,   108,   110,   112,   114,   116,
     118,   120,   123,   126,   130,   137,   140,   142,   146,   150,
     152,   156,   161,   167,   171,   175,   180,   186,   192,   198,
     205,   210,   215,   222,   232,   241,   249,   253,   260,   268,
     275,   281,   283,   285,   287,   289,   291,   293,   295,   297,
     299,   301,   308,   314,   323,   331,   338,   347,   357,   367,
     378,   385,   391,   400,   410,   413,   415,   419,   423,   427,
     432,   438,   444,   451,   455,   460,   466,   471,   475,   480,
     484,   489,   494,   500,   506,   510,   515,   521,   525,   529,
     531,   535,   539,   541,   546,   551,   557,   561,   567,   574,
     578,   584,   591,   598,   605,   612,   618,   626,   635,   643,
     651,   655,   657,   660,   666,   671,   680,   685,   688,   691,
     694,   698,   700,   706,   709,   714,   717,   720,   723,   728,
     732,   735,   738,   742,   746,   749,   751,   755,   761,   765,
     767,   769,   771,   773,   775,   777,   779,   781,   783,   785,
     791,   799,   809,   812,   815,   818,   823,   825,   827,   831,
     833,   836,   839,   841,   845,   848,   851,   857,   861,   866,
     872,   877,   883,   889,   897,   901,   905,   909,   914,   918,
     924,   927,   931,   935,   940,   946,   953,   961,   968,   975,
     983,   990,   998,  1002,  1006,  1009,  1011,  1013,  1015,  1018,
    1020,  1026,  1030,  1034,  1036,  1040,  1042,  1046,  1056,  1062,
    1068,  1072,  1074,  1078,  1081,  1083,  1087,  1091,  1095,  1099,
    1103,  1105,  1108,  1110,  1112,  1115,  1119,  1123,  1126,  1128,
    1130,  1134,  1136,  1142,  1148,  1154,  1158,  1160,  1162,  1164,
    1167,  1170,  1173,  1176,  1179,  1182,  1186,  1189,  1192,  1194,
    1196,  1198,  1200,  1202,  1204,  1207,  1210,  1212,  1214,  1216,
    1218,  1220,  1224,  1228,  1230,  1233,  1235,  1238,  1242,  1246,
    1251,  1256,  1263,  1265,  1267,  1269,  1271,  1273,  1275,  1277,
    1279,  1281,  1283,  1285,  1287,  1289,  1291,  1293,  1298,  1300,
    1302,  1304,  1306,  1308,  1310,  1313,  1317,  1321,  1324,  1330,
    1334,  1338,  1342,  1346,  1350,  1354,  1358,  1362,  1366,  1370,
    1374,  1378,  1382,  1386,  1390,  1394,  1398,  1402,  1406,  1410,
    1414,  1418,  1422,  1426,  1430,  1435,  1439,  1441,  1444,  1447,
    1450,  1453,  1456,  1459,  1462,  1465
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
     198,     5,   198,    -1,   200,   198,   198,     5,    -1,   200,
     198,   198,   198,     5,    -1,     5,    -1,   200,     5,   126,
     206,    -1,   200,   198,     5,   126,   206,    -1,   145,   144,
      -1,    -1,   150,    -1,   151,    -1,   166,    -1,   173,    -1,
     174,    -1,   159,    -1,   160,    -1,   161,    -1,   147,    -1,
     155,    -1,   156,    -1,   146,    -1,   185,    -1,    96,    -1,
      66,    45,    -1,    66,     5,    -1,    66,     5,   207,    -1,
      66,     4,     5,   117,     4,     5,    -1,    54,   182,    -1,
       5,    -1,     5,   126,   207,    -1,   149,   125,   148,    -1,
     148,    -1,   200,   197,   124,    -1,   200,   198,   197,   124,
      -1,   200,   198,   197,   198,   124,    -1,    17,   197,   124,
      -1,   201,   149,   124,    -1,   201,   198,   149,   124,    -1,
     201,   198,   198,   149,   124,    -1,   201,   198,     5,   198,
     124,    -1,   201,   198,   198,     5,   124,    -1,   201,   198,
     198,   198,     5,   124,    -1,   201,     5,   198,   124,    -1,
     201,   172,   197,   124,    -1,   201,   172,     5,   126,   207,
     124,    -1,   100,    99,    13,   198,   127,   197,   128,     5,
     124,    -1,   100,    99,    13,   127,   197,   128,     5,   124,
      -1,   100,    99,   127,   197,   128,     5,   124,    -1,     7,
     189,   124,    -1,     7,   169,   196,   126,   207,   124,    -1,
       7,   152,   169,   196,   126,   207,   124,    -1,     7,   152,
     196,   126,   207,   124,    -1,   122,   153,   125,   153,   123,
      -1,    67,    -1,    68,    -1,    69,    -1,    70,    -1,    71,
      -1,    72,    -1,    73,    -1,    74,    -1,   198,    -1,    21,
      -1,    56,     5,   124,   157,   195,    57,    -1,    56,     5,
     124,   195,    57,    -1,    56,   198,   198,     5,   124,   157,
     182,    57,    -1,    56,   154,     5,   124,   157,   182,    57,
      -1,    56,   154,     5,   124,   182,    57,    -1,    56,     5,
     122,   142,   123,   124,   182,    57,    -1,    56,     5,   122,
     142,   123,   124,   157,   182,    57,    -1,    56,   154,     5,
     122,   142,   123,   124,   182,    57,    -1,    56,   154,     5,
     122,   142,   123,   124,   157,   182,    57,    -1,    58,     5,
     124,   157,   182,    59,    -1,    58,     5,   124,   182,    59,
      -1,    58,     5,   122,   142,   123,   124,   182,    59,    -1,
      58,     5,   122,   142,   123,   124,   157,   182,    59,    -1,
     157,   158,    -1,   158,    -1,    11,   197,   124,    -1,    22,
     197,   124,    -1,    23,   197,   124,    -1,    11,   198,   197,
     124,    -1,    11,   198,     5,   198,   124,    -1,    11,   198,
     198,     5,   124,    -1,     9,    11,   198,   198,     5,   124,
      -1,     8,   197,   124,    -1,     8,   197,   198,   124,    -1,
       8,   198,   198,   197,   124,    -1,     8,    21,   197,   124,
      -1,    21,   197,   124,    -1,    21,   197,   198,   124,    -1,
      47,   162,   124,    -1,    47,    16,   162,   124,    -1,    47,
     198,   162,   124,    -1,    47,   198,   198,   162,   124,    -1,
      47,    16,   198,   162,   124,    -1,    48,   162,   124,    -1,
      48,   198,   162,   124,    -1,    48,   198,   198,   162,   124,
      -1,    46,   162,   124,    -1,   162,   125,   163,    -1,   163,
      -1,     5,   126,   207,    -1,   164,   125,   165,    -1,   165,
      -1,    48,     5,   126,   207,    -1,    47,     5,   126,   207,
      -1,    47,   198,     5,   126,   207,    -1,     5,   126,   207,
      -1,     5,     5,   122,   123,   124,    -1,     5,   172,     5,
     122,   123,   124,    -1,     5,     5,   124,    -1,    42,   122,
     194,   123,   124,    -1,    42,     5,   122,   194,   123,   124,
      -1,     5,     5,   122,   167,   123,   124,    -1,    42,     5,
     122,   167,   123,   124,    -1,     5,     5,   122,   194,   123,
     124,    -1,     5,   122,   194,   123,   124,    -1,     5,   172,
       5,   122,   167,   123,   124,    -1,     5,   172,     5,   198,
     122,   167,   123,   124,    -1,     5,     5,   198,   122,   167,
     123,   124,    -1,     5,     5,   198,   122,   194,   123,   124,
      -1,   167,   125,   168,    -1,   168,    -1,   129,   116,    -1,
     129,     5,   122,   207,   123,    -1,   129,     5,   122,   123,
      -1,   129,     5,   130,     4,   131,   122,   207,   123,    -1,
     121,   122,   194,   123,    -1,   121,     4,    -1,   121,     5,
      -1,   121,    82,    -1,   170,   125,   171,    -1,   171,    -1,
     129,     5,   122,   207,   123,    -1,   129,     5,    -1,   121,
     122,   194,   123,    -1,   121,     4,    -1,   121,    82,    -1,
     121,     5,    -1,   121,   122,   170,   123,    -1,   121,   122,
     123,    -1,    98,   182,    -1,    35,   182,    -1,    35,   178,
     182,    -1,    85,   175,    86,    -1,   175,   176,    -1,   176,
      -1,    36,   175,    37,    -1,    36,   102,     5,   175,    37,
      -1,    87,   197,   124,    -1,   150,    -1,   151,    -1,   159,
      -1,   160,    -1,   161,    -1,   166,    -1,   177,    -1,   173,
      -1,   147,    -1,   185,    -1,    38,   122,   207,   123,   176,
      -1,    38,   122,   207,   123,   176,    39,   176,    -1,    60,
     122,   189,   124,   207,   124,   189,   123,   176,    -1,   132,
     116,    -1,   132,    84,    -1,   132,     5,    -1,   132,   122,
     180,   123,    -1,    42,    -1,   125,    -1,   180,   179,   181,
      -1,   181,    -1,    40,   207,    -1,    41,   207,    -1,   207,
      -1,    36,   195,    37,    -1,    36,    37,    -1,    55,   182,
      -1,    36,   102,     5,   195,    37,    -1,    75,   195,    76,
      -1,   196,   126,   207,   124,    -1,   196,   126,   169,   207,
     124,    -1,   196,    34,   207,   124,    -1,   196,    34,   169,
     207,   124,    -1,    38,   122,   207,   123,   182,    -1,    38,
     122,   207,   123,   182,    39,   182,    -1,    43,   207,   124,
      -1,    21,   197,   124,    -1,    11,   197,   124,    -1,    11,
     198,   197,   124,    -1,    89,   207,   124,    -1,    88,   207,
     126,   207,   124,    -1,   178,   124,    -1,    44,     5,   124,
      -1,    77,     5,   124,    -1,     5,   122,   123,   124,    -1,
       5,   122,   194,   123,   124,    -1,    49,   122,   207,   123,
     191,    52,    -1,    49,   122,   207,   123,   191,   193,    52,
      -1,    49,   122,   207,   123,   193,    52,    -1,    50,   122,
     207,   123,   191,    52,    -1,    50,   122,   207,   123,   191,
     193,    52,    -1,    51,   122,   207,   123,   191,    52,    -1,
      51,   122,   207,   123,   191,   193,    52,    -1,   121,   207,
     124,    -1,   121,   207,   182,    -1,     5,   124,    -1,   186,
      -1,   187,    -1,   188,    -1,   205,   124,    -1,   185,    -1,
       7,   196,   126,   207,   124,    -1,    97,     5,   124,    -1,
     183,   125,   184,    -1,   184,    -1,     5,   126,   207,    -1,
      45,    -1,    78,   183,    79,    -1,    60,   122,   189,   124,
     207,   124,   189,   123,   182,    -1,    93,   122,   207,   123,
     182,    -1,    61,   122,   207,   123,   182,    -1,   189,   125,
     190,    -1,   190,    -1,   196,   126,   207,    -1,   191,   192,
      -1,   192,    -1,   194,   102,   182,    -1,   194,   102,   124,
      -1,    53,   102,   182,    -1,    53,   102,   124,    -1,   194,
     125,   207,    -1,   207,    -1,   195,   182,    -1,   182,    -1,
       5,    -1,     5,   198,    -1,     5,   199,   198,    -1,     5,
     199,   199,    -1,     5,   199,    -1,   205,    -1,   202,    -1,
       5,   125,   197,    -1,     5,    -1,   130,   207,   102,   207,
     131,    -1,   130,   207,    80,   207,   131,    -1,   130,   207,
      81,   207,   131,    -1,   130,   207,   131,    -1,     8,    -1,
       9,    -1,    10,    -1,     9,    11,    -1,     8,    12,    -1,
       9,    12,    -1,    10,    12,    -1,     8,    16,    -1,     9,
      16,    -1,     9,    11,    16,    -1,     9,    13,    -1,     8,
      13,    -1,    13,    -1,    11,    -1,    12,    -1,    16,    -1,
      21,    -1,    22,    -1,    11,    16,    -1,    12,    16,    -1,
      87,    -1,    94,    -1,    95,    -1,    14,    -1,    15,    -1,
     127,   203,   128,    -1,   203,   125,   204,    -1,   204,    -1,
     207,   202,    -1,   207,    -1,   109,   202,    -1,     5,   129,
     205,    -1,     5,   129,     5,    -1,     5,   129,     5,   198,
      -1,     5,   129,     5,   199,    -1,     5,   129,     5,   122,
     207,   123,    -1,     4,    -1,    82,    -1,    45,    -1,    18,
      -1,    19,    -1,    20,    -1,    24,    -1,    25,    -1,    26,
      -1,     5,    -1,   205,    -1,     4,    -1,    82,    -1,    45,
      -1,    66,    -1,    66,   122,   207,   123,    -1,    18,    -1,
      19,    -1,    20,    -1,    24,    -1,    25,    -1,    26,    -1,
       5,   198,    -1,     5,   199,   198,    -1,     5,   199,   199,
      -1,     5,   199,    -1,   207,   101,   207,   102,   207,    -1,
     207,   112,   207,    -1,   207,   116,   207,    -1,   207,   113,
     207,    -1,   207,   117,   207,    -1,   207,   118,   207,    -1,
     207,   104,   207,    -1,   207,   103,   207,    -1,   207,   105,
     207,    -1,   207,   110,   207,    -1,   207,   111,   207,    -1,
     207,    83,   207,    -1,   207,    28,   207,    -1,   207,    29,
     207,    -1,   207,    90,   207,    -1,   207,    91,   207,    -1,
     207,    92,   207,    -1,   207,    31,   207,    -1,   207,    30,
     207,    -1,   207,    32,   207,    -1,   207,   115,   207,    -1,
     207,    33,   207,    -1,   207,    34,   207,    -1,   207,   109,
     207,    -1,   207,   108,   207,    -1,   207,   106,   207,    -1,
       5,   122,   194,   123,    -1,   122,   207,   123,    -1,   202,
      -1,   113,   207,    -1,   103,   207,    -1,   105,   207,    -1,
     104,   207,    -1,    90,   207,    -1,    92,   207,    -1,    91,
     207,    -1,   133,   207,    -1,   134,   207,    -1
};

/* YYRLINE[YYN] -- source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,    45,    45,    46,    46,    47,    47,    48,    50,    50,
      50,    51,    51,    51,    52,    52,    54,    54,    54,    55,
      56,    57,    58,    58,    58,    62,    62,    65,    66,    67,
      68,    69,    70,    71,    72,    73,    74,    75,    76,    77,
      78,    82,    82,    82,    82,    83,    84,    84,    85,    85,
      87,    88,    89,    90,    91,    92,    93,    96,    97,    98,
     100,   101,   102,   103,   104,   105,   110,   111,   112,   113,
     116,   117,   117,   117,   117,   117,   117,   117,   117,   118,
     118,   120,   121,   122,   123,   124,   125,   126,   127,   128,
     131,   132,   133,   134,   137,   137,   139,   140,   141,   142,
     143,   144,   145,   146,   147,   148,   149,   150,   151,   155,
     156,   157,   158,   159,   161,   161,   161,   162,   164,   164,
     165,   167,   167,   169,   170,   171,   172,   176,   177,   178,
     179,   180,   181,   182,   183,   184,   185,   186,   187,   188,
     196,   196,   197,   197,   197,   197,   199,   199,   199,   199,
     200,   200,   201,   201,   202,   202,   202,   202,   202,   202,
     205,   205,   205,   208,   210,   210,   213,   214,   215,   216,
     217,   218,   219,   220,   221,   222,   223,   224,   225,   226,
     227,   232,   237,   237,   237,   237,   238,   238,   239,   239,
     240,   240,   240,   245,   246,   247,   248,   249,   250,   251,
     252,   253,   254,   255,   256,   257,   258,   259,   260,   261,
     262,   263,   264,   265,   266,   267,   268,   269,   270,   271,
     272,   273,   274,   275,   276,   277,   278,   279,   280,   281,
     282,   283,   287,   287,   288,   288,   290,   292,   293,   294,
     295,   295,   296,   297,   297,   298,   298,   299,   299,   301,
     301,   302,   302,   305,   305,   305,   305,   305,   305,   305,
     307,   307,   309,   309,   309,   310,   312,   312,   312,   312,
     312,   312,   312,   312,   312,   312,   312,   312,   314,   314,
     314,   314,   314,   314,   314,   314,   314,   314,   314,   314,
     314,   316,   317,   317,   319,   320,   321,   325,   326,   327,
     328,   329,   333,   334,   335,   336,   336,   336,   336,   336,
     336,   340,   341,   342,   343,   344,   345,   346,   347,   347,
     347,   347,   347,   347,   348,   349,   350,   351,   352,   353,
     354,   355,   356,   357,   358,   359,   360,   361,   362,   363,
     364,   365,   366,   367,   368,   369,   370,   371,   372,   373,
     374,   375,   376,   377,   378,   379,   380,   381,   382,   383,
     384,   385,   386,   387,   388,   389
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
     143,   143,   143,   143,   143,   144,   144,   145,   145,   145,
     145,   145,   145,   145,   145,   145,   145,   145,   145,   145,
     145,   146,   146,   146,   146,   147,   148,   148,   149,   149,
     150,   150,   150,   150,   150,   150,   150,   150,   150,   150,
     150,   150,   150,   150,   150,   150,   151,   151,   151,   151,
     152,   153,   153,   153,   153,   153,   153,   153,   153,   154,
     154,   155,   155,   155,   155,   155,   155,   155,   155,   155,
     156,   156,   156,   156,   157,   157,   158,   158,   158,   158,
     158,   158,   158,   158,   158,   158,   158,   158,   158,   159,
     159,   159,   159,   159,   160,   160,   160,   161,   162,   162,
     163,   164,   164,   165,   165,   165,   165,   166,   166,   166,
     166,   166,   166,   166,   166,   166,   166,   166,   166,   166,
     167,   167,   168,   168,   168,   168,   169,   169,   169,   169,
     170,   170,   171,   171,   172,   172,   172,   172,   172,   172,
     173,   173,   173,   174,   175,   175,   176,   176,   176,   176,
     176,   176,   176,   176,   176,   176,   176,   176,   176,   176,
     176,   177,   178,   178,   178,   178,   179,   179,   180,   180,
     181,   181,   181,   182,   182,   182,   182,   182,   182,   182,
     182,   182,   182,   182,   182,   182,   182,   182,   182,   182,
     182,   182,   182,   182,   182,   182,   182,   182,   182,   182,
     182,   182,   182,   182,   182,   182,   182,   182,   182,   182,
     182,   182,   183,   183,   184,   184,   185,   186,   187,   188,
     189,   189,   190,   191,   191,   192,   192,   193,   193,   194,
     194,   195,   195,   196,   196,   196,   196,   196,   196,   196,
     197,   197,   198,   198,   198,   199,   200,   200,   200,   200,
     200,   200,   200,   200,   200,   200,   200,   200,   201,   201,
     201,   201,   201,   201,   201,   201,   201,   201,   201,   201,
     201,   202,   203,   203,   204,   204,   204,   205,   205,   205,
     205,   205,   206,   206,   206,   206,   206,   206,   206,   206,
     206,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207
};

/* YYR2[YYN] -- Number of symbols composing right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     1,     2,     1,     1,     1,     6,     4,     3,
       0,     1,     4,     3,     3,     1,     2,     3,     3,     4,
       4,     5,     1,     4,     5,     2,     0,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     2,     2,     3,     6,     2,     1,     3,     3,     1,
       3,     4,     5,     3,     3,     4,     5,     5,     5,     6,
       4,     4,     6,     9,     8,     7,     3,     6,     7,     6,
       5,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     6,     5,     8,     7,     6,     8,     9,     9,    10,
       6,     5,     8,     9,     2,     1,     3,     3,     3,     4,
       5,     5,     6,     3,     4,     5,     4,     3,     4,     3,
       4,     4,     5,     5,     3,     4,     5,     3,     3,     1,
       3,     3,     1,     4,     4,     5,     3,     5,     6,     3,
       5,     6,     6,     6,     6,     5,     7,     8,     7,     7,
       3,     1,     2,     5,     4,     8,     4,     2,     2,     2,
       3,     1,     5,     2,     4,     2,     2,     2,     4,     3,
       2,     2,     3,     3,     2,     1,     3,     5,     3,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     5,
       7,     9,     2,     2,     2,     4,     1,     1,     3,     1,
       2,     2,     1,     3,     2,     2,     5,     3,     4,     5,
       4,     5,     5,     7,     3,     3,     3,     4,     3,     5,
       2,     3,     3,     4,     5,     6,     7,     6,     6,     7,
       6,     7,     3,     3,     2,     1,     1,     1,     2,     1,
       5,     3,     3,     1,     3,     1,     3,     9,     5,     5,
       3,     1,     3,     2,     1,     3,     3,     3,     3,     3,
       1,     2,     1,     1,     2,     3,     3,     2,     1,     1,
       3,     1,     5,     5,     5,     3,     1,     1,     1,     2,
       2,     2,     2,     2,     2,     3,     2,     2,     1,     1,
       1,     1,     1,     1,     2,     2,     1,     1,     1,     1,
       1,     3,     3,     1,     2,     1,     2,     3,     3,     4,
       4,     6,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     4,     1,     1,
       1,     1,     1,     1,     2,     3,     3,     2,     5,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     4,     3,     1,     2,     2,     2,
       2,     2,     2,     2,     2,     2
};

/* YYDEFACT[STATE-NAME] -- Default rule to reduce with in state
   STATE-NUM when YYTABLE doesn't specify something else to do.  Zero
   means the default is an error.  */
static const yytype_uint16 yydefact[] =
{
       0,     0,     0,     0,     2,     4,     5,     6,    10,     0,
      42,    41,     1,     3,     0,     0,     0,   313,   311,   318,
     319,   320,   321,   322,   323,   315,   316,   314,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   356,
     312,    43,     0,     0,    11,    26,     0,     0,     0,     0,
     324,   327,     0,   361,   363,   362,   358,   360,   359,   357,
       0,     0,     0,   293,   295,   364,   365,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     9,     0,   122,    22,
     266,   267,   268,     0,     0,    15,     0,     0,     0,   279,
     280,   278,   289,   290,   281,     0,   282,   283,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   286,   287,
     288,    40,     0,     0,     0,    26,    38,    35,    27,    28,
      36,    37,    32,    33,    34,    29,    30,    31,    39,     0,
       0,     0,     0,   250,   298,   297,     0,   325,   326,     0,
     355,   296,     0,   291,   294,   340,   341,   346,   345,   347,
     349,   350,   339,   342,   343,   344,     0,   335,   334,   336,
     353,   352,   351,   337,   338,   329,   331,   348,   330,   332,
     333,     0,     0,     0,     0,     0,     8,     0,   270,   277,
     273,   269,   271,   276,   274,   272,    13,     0,     0,    16,
       0,     0,     0,     0,     0,     0,   253,     0,     0,     0,
       0,     0,   241,     0,   259,   258,   284,   285,   261,     0,
     253,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   161,   229,   225,   226,   227,     0,   258,
       0,     0,     0,     0,   119,     0,     0,     0,     0,     0,
       0,    45,     0,    80,     0,    79,     0,     0,   235,     0,
     233,     0,     0,     0,   286,   177,   169,   170,   171,   172,
     173,   174,   176,     0,   165,   175,   178,   160,     0,     7,
      25,     0,     0,    46,    49,     0,     0,     0,    44,   354,
       0,     0,   299,   300,     0,     0,     0,   265,   317,   292,
       0,   126,     0,     0,     0,     0,   121,   275,    12,    14,
       0,    18,    17,     0,     0,   129,     0,   155,   157,   156,
       0,     0,     0,   254,   257,   147,   148,   149,     0,    71,
      72,    73,    74,    75,    76,    77,    78,     0,     0,     0,
       0,    66,     0,     0,     0,    53,     0,   224,     0,     0,
       0,     0,   194,     0,   252,     0,     0,     0,     0,     0,
       0,     0,   195,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   184,   183,   182,     0,   210,   162,     0,     0,
     228,     0,     0,     0,   117,     0,     0,     0,   109,     0,
       0,   114,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   236,     0,     0,     0,     0,     0,     0,   163,   164,
       0,     0,    50,     0,     0,     0,    54,     0,   261,     0,
      46,     0,     0,   249,     0,     0,     0,     0,   328,   124,
       0,   123,   302,   305,   306,   307,   308,   309,   310,   304,
     303,    23,     0,    19,    20,     0,     0,     0,     0,   141,
       0,     0,   159,     0,     0,   151,     0,     0,     0,     0,
     255,   256,     0,     0,     0,     0,     0,   240,   242,   260,
       0,     0,     0,   206,     0,   205,     0,   193,   251,     0,
     204,   211,     0,     0,     0,     0,     0,   197,   212,     0,
     208,     0,   231,   222,   223,     0,     0,     0,   189,   192,
       0,     0,     0,     0,     0,     0,     0,   120,   118,   110,
       0,   111,     0,   115,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    95,     0,     0,     0,     0,     0,     0,
       0,   234,   232,     0,   166,     0,     0,   168,     0,     0,
       0,    51,     0,    47,    60,    46,    48,     0,    61,     0,
      55,    46,     0,     0,   301,   263,   264,   262,   125,    24,
      21,   127,     0,   142,     0,     0,     0,     0,     0,   153,
     158,     0,   154,   135,     0,     0,     0,   146,     0,     0,
       0,     0,   213,     0,     0,   207,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   190,   191,   186,   185,   187,
       0,     0,   200,     0,   198,     0,     0,   130,   113,   112,
     116,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    94,     0,    82,     0,     0,     0,     0,     0,     0,
      91,     0,     0,     0,     0,     0,     0,    52,     0,    57,
      58,    56,     0,     0,     0,   132,   140,   134,     0,     0,
       0,   150,   128,     0,     0,    70,     0,    69,    67,   214,
     230,   196,   202,     0,     0,   244,     0,     0,     0,     0,
       0,   239,   209,   238,   188,   201,   199,   133,   131,     0,
       0,   103,     0,     0,     0,    96,   261,     0,     0,   107,
       0,    97,    98,    81,     0,     0,    85,     0,     0,     0,
       0,    90,   167,   179,     0,     0,     0,     0,    62,    59,
     144,     0,     0,   138,   139,     0,   136,     0,    68,     0,
       0,   215,   243,     0,   217,     0,   218,     0,   220,     0,
       0,     0,     0,   106,   104,     0,     0,     0,    99,     0,
     108,     0,    84,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    65,   143,     0,   152,   137,   203,   248,
     247,   216,   246,   245,   219,   221,     0,     0,    86,   105,
       0,   100,   101,     0,     0,    96,     0,   107,    83,     0,
      92,   180,     0,    64,     0,     0,     0,    87,   102,     0,
      88,    99,    93,     0,    63,     0,   237,    89,   181,   145
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,     3,     4,     5,     6,    15,    45,   104,   105,   134,
     135,     7,   285,   304,   305,   286,   287,   219,   357,   274,
     140,   141,   542,   543,   288,   289,   290,   263,   264,    97,
      98,   291,   468,   469,   220,   474,   475,   215,   292,   147,
     293,   294,   295,   270,   620,   517,   518,   374,   279,   280,
     254,   255,   256,   257,   221,   222,   684,   685,   686,   687,
     375,   258,   229,   343,   344,   149,   150,    39,    62,    63,
      40,   461,   153
};

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
#define YYPACT_NINF -533
static const yytype_int16 yypact[] =
{
     119,    36,   170,   105,   119,  -533,  -533,  -533,     6,   131,
    1671,  -533,  -533,  -533,    81,    -4,   126,  -533,   101,  -533,
    -533,  -533,  -533,  -533,  -533,  -533,   152,  -533,  1671,  1671,
    1671,  1671,  1671,  1671,  1671,  1671,  1298,  1671,  1671,  -533,
    -533,  4724,   121,    88,  -533,  3609,   160,  1671,   207,  1671,
    -533,   158,  1671,  -533,  -533,  -533,  -533,  -533,  -533,  -533,
    3983,   176,    51,  -533,  2659,  -533,  -533,  1671,  1671,  1671,
    1671,  1671,  1671,  1671,  1671,  1671,  1671,  1671,  1671,  1671,
    1671,  1671,  1671,  1671,  1671,  1671,  1671,  1671,  1671,  1671,
    1671,  1671,  1671,   190,    30,   291,  -533,   211,  -533,  -533,
     243,   310,   301,   196,   217,  -533,    33,    95,    26,   308,
     313,  -533,  -533,  -533,  -533,   362,  -533,  -533,  2447,    40,
     367,    28,    42,  2447,    35,   373,    89,  3985,  -533,  -533,
    -533,  -533,  2447,   283,   388,  3609,  -533,  -533,  -533,  -533,
    -533,  -533,  -533,  -533,  -533,  -533,  -533,  -533,  -533,    43,
      29,   406,   274,  4724,   120,  -533,   459,  -533,  -533,  4019,
    -533,  -533,  1298,  -533,  -533,   779,  4820,   150,   150,   150,
     326,   326,  -533,  3754,  3754,  3754,  4693,  4789,  3754,  3848,
     708,   708,   708,   326,   326,   315,   315,   150,  -533,  -533,
    -533,  1671,   281,  1671,   415,   300,  -533,   191,  -533,  -533,
    -533,   446,  -533,  -533,  -533,  -533,  -533,   350,   382,   353,
     429,    47,    -1,   102,  1671,   503,   214,   110,   378,    10,
      24,   230,  -533,   368,  -533,  -533,  -533,  -533,   386,   405,
     154,    24,    43,   362,  1925,   397,  1671,   527,   414,   433,
     436,  2447,   444,   451,  2447,   587,  1671,  1671,   497,   595,
    1671,   106,  1999,  -533,  -533,  -533,  -533,  -533,     2,   507,
     512,  1671,   510,   330,  -533,    42,   454,    42,   470,    42,
     517,  -533,   280,  -533,   637,   516,   284,   521,  -533,    13,
    -533,  2810,   529,   532,   362,  -533,  -533,  -533,  -533,  -533,
    -533,  -533,  -533,  3703,  -533,  -533,  -533,  -533,    77,  -533,
    -533,   524,   362,    75,  -533,   472,   644,    48,  -533,  -533,
    1671,  1671,  -533,  -533,  1671,  1671,  1671,  -533,  -533,  -533,
    1671,  4724,  1671,  4628,   530,  1671,  -533,  -533,  -533,  -533,
     477,  -533,   169,    50,   853,  -533,   533,  -533,  -533,  -533,
     986,   293,   143,  -533,   158,  -533,  -533,  -533,  1671,  -533,
    -533,  -533,  -533,  -533,  -533,  -533,  -533,   534,    24,   535,
     537,  -533,    24,  1671,   362,  -533,  1353,  -533,   538,   541,
     362,   543,  -533,   653,  -533,  2057,  1671,  2843,   544,  1671,
    1671,  1671,  -533,    24,  1671,  2122,   545,  2690,  2885,  1671,
     546,  1778,  -533,  -533,  -533,  1062,  -533,  -533,  1422,  1422,
    -533,  1491,   294,  1671,  -533,   367,   474,   367,  -533,   478,
     367,  -533,   480,   367,   382,  1904,   336,   666,   382,  1904,
    1671,  -533,    89,   667,  3797,  1671,    24,   549,  -533,  -533,
      91,   362,  -533,   -21,  1671,   550,  -533,   670,   481,   552,
      75,   484,    80,  4724,  4084,  2498,  2563,  2594,  4724,  4724,
    1671,  4724,  -533,  -533,  -533,  -533,  -533,  -533,  -533,  -533,
    -533,  -533,   477,  -533,  -533,   672,   554,    25,   342,  -533,
     343,  1491,  -533,   676,   347,  -533,   348,   558,   122,   562,
    -533,  -533,   355,   378,   560,  1671,  1671,  -533,  4724,  -533,
     564,   360,  1671,  -533,   566,  -533,  2447,  -533,  -533,  4120,
    -533,  -533,  4185,  4221,  4286,   489,  4322,  -533,  -533,  1671,
    -533,  4387,  -533,  -533,  -533,  1671,  1671,   129,  -533,  4724,
    1671,  2950,  1671,  2986,   361,   375,   567,  4724,  -533,  -533,
     491,  -533,   493,  -533,   496,   384,    78,   681,    43,   362,
     362,   362,  1904,  -533,  2180,   382,  1904,   569,   391,  1904,
     635,  4724,  -533,  3985,  -533,  4423,   498,  -533,   362,   570,
     568,  -533,   574,  4724,  -533,   576,  -533,  1671,  -533,   579,
    -533,   335,   500,   695,  -533,  -533,  -533,  -533,  4724,  -533,
    -533,  -533,   159,  -533,   580,   578,   585,   392,   395,   588,
    -533,   584,  -533,  -533,   590,   402,   578,  -533,   592,  1671,
    3051,  3087,  -533,   593,  3152,  -533,  2245,  2447,  1546,  1671,
    1671,  1671,  2447,  3188,  2447,  4724,  4724,  -533,  -533,  -533,
    1062,  3253,  -533,  3289,  -533,   594,   596,  -533,  -533,  -533,
    -533,   597,   362,   147,   516,   516,   598,    83,   184,   600,
     601,  -533,  2303,  -533,   403,  1904,   659,   341,   602,   668,
    -533,  3891,  3985,  1671,   604,   362,   723,  -533,  3354,  -533,
    -533,  -533,   609,  1622,   730,  -533,  -533,  -533,   611,   619,
    1671,  -533,  -533,   620,   418,  -533,  3390,  -533,  -533,  -533,
    -533,  -533,   706,   645,  1117,  -533,   694,     0,  1193,  1248,
    3455,  -533,  -533,  -533,  -533,  -533,  -533,  -533,  -533,  1904,
     624,  -533,   625,   362,   516,   487,    61,   626,   746,   495,
     628,  -533,  -533,  -533,   629,   698,  -533,    43,   362,  1904,
    1904,  -533,  -533,   717,  3491,   756,   634,   639,  -533,  -533,
    -533,  4488,   633,  -533,  -533,  4524,  -533,   641,  -533,  2447,
    2368,  -533,  -533,   714,  -533,  2426,  -533,   715,  -533,   718,
      24,  1904,   722,  -533,  -533,   647,   767,   651,   526,   656,
    -533,  1904,  -533,   657,    83,   187,   725,  1904,   726,  3985,
      24,   660,   781,  -533,  -533,   665,  -533,  -533,  -533,  -533,
    -533,  -533,  -533,  -533,  -533,  -533,   463,   733,  -533,  -533,
     669,  -533,  -533,  1904,   735,  -533,   673,  -533,  -533,   737,
    -533,  -533,   468,  -533,   674,  1671,  2447,  -533,  -533,   744,
    -533,  -533,  -533,  3985,  -533,  4589,  -533,  -533,  -533,  -533
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -533,  -533,  -533,   790,  -533,  -533,  -533,  -402,   606,   671,
    -533,    59,    63,   366,  -300,    65,    67,  -533,   332,  -533,
    -533,  -533,  -413,  -532,    79,    85,    90,   -72,   417,  -533,
     630,    94,  -387,   244,  -210,  -533,   237,   680,   112,  -533,
    -278,  -292,  -533,   716,  -533,  -533,   212,   162,  -533,   411,
     -40,  -533,  -533,  -533,  -375,   473,    17,  -397,  -308,   -15,
    -233,   -65,    99,    -5,   -14,   -41,  -533,   304,  -533,   675,
      38,   374,   -10
};

/* YYTABLE[YYPACT[STATE-NUM]].  What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule which
   number is the opposite.  If zero, do what YYDEFACT says.
   If YYTABLE_NINF, syntax error.  */
#define YYTABLE_NINF -208
static const yytype_int16 yytable[] =
{
      41,   429,   106,   424,    51,   148,   549,   441,   505,   358,
     641,   385,   535,    50,   524,   216,   548,   641,    53,    54,
      55,    56,    57,    58,    59,    60,    64,    65,    66,   216,
     582,   216,   152,   262,   303,   192,   398,   158,   209,   156,
     272,     8,   159,   223,   265,   260,   157,   262,   228,   266,
     268,   556,   332,   440,   210,   464,   273,   165,   166,   167,
     168,   169,   170,   171,   172,   173,   174,   175,   176,   177,
     178,   179,   180,   181,   182,   183,   184,   185,   186,   187,
     188,   189,   190,   228,   587,   571,   155,   296,   706,   194,
     430,   595,   421,    99,   277,   148,   100,   101,   102,   632,
     212,   211,   745,   561,   136,    12,   337,   338,   137,   193,
     138,   392,   139,   641,   345,   346,   267,   269,    43,   275,
      44,   334,     1,   335,   142,   310,    93,    14,   399,   193,
     143,   217,   429,   645,   278,   144,    16,    36,   422,   145,
     313,   583,   572,   644,   302,   307,   225,   217,   218,   312,
     213,    36,    64,    36,   359,   360,   259,   146,   193,   193,
     193,   259,   261,   193,   151,   193,   368,   106,    94,    95,
     259,   617,   193,   193,     9,    10,   162,   193,   193,   163,
     193,   321,   544,   323,   339,     2,   364,   641,   520,   522,
     393,   193,   347,   406,   136,   409,    93,   412,   137,   341,
     138,   434,   139,    42,   431,   193,   333,   336,   193,   674,
     193,   103,   154,   193,   142,    11,   213,   214,   558,   641,
     143,   193,   394,    47,   340,   144,   377,   370,   395,   145,
      48,    49,   348,    74,   719,   641,   387,   388,    94,    95,
     391,   296,   311,    46,    96,   594,   402,   146,   301,    48,
      49,   467,   618,   296,   619,   198,   199,   225,   225,   200,
     407,   641,   410,   606,   413,   478,    90,    91,    92,   225,
     417,   701,   259,   193,    52,   651,   366,   193,   367,   259,
     253,   663,   259,    48,    49,   271,   751,   742,    49,   664,
     259,   742,   742,   484,   297,   462,   195,   223,   435,   193,
     443,   444,   442,    36,   445,   446,   447,   767,   709,   642,
     448,   797,   449,   205,   193,   451,   191,   193,   223,   470,
     206,   201,   202,   203,   226,   476,   204,   463,   465,   227,
     481,   369,   371,   482,   196,   530,   197,   479,   532,   480,
     207,   534,   208,    48,    49,    69,    70,    71,   793,   536,
     537,   491,   717,   488,   361,   362,    69,    70,    71,   429,
     723,   223,   718,   540,   541,   161,   499,   228,   164,   502,
     503,   504,   262,   106,   506,   786,   743,   106,   276,   511,
     747,   749,   298,   427,   296,   519,   525,    99,   521,   523,
     100,   101,   102,   527,   299,   802,   225,   309,    74,   310,
     225,   433,   414,   382,   415,   439,   418,   322,   419,    74,
     551,   308,   224,   259,   397,   555,   477,   526,   310,   310,
     324,   225,   224,   259,   563,   559,   325,   224,   562,   259,
      89,    90,    91,    92,   331,   569,   224,   573,    87,    88,
     578,    89,    90,    91,    92,   349,   350,   351,   352,   353,
     354,   355,   356,   259,   404,   405,   588,   259,   545,   660,
     546,   434,   327,   489,   225,   584,   586,   585,   310,   494,
     590,   592,   591,   310,   328,   600,   601,   801,   597,   330,
     310,   452,   604,   603,   625,   310,   585,    67,    68,    69,
      70,    71,    72,    73,   363,   453,   454,   455,   626,   613,
     310,   456,   457,   458,   106,   615,   616,   631,   342,   208,
     621,   364,   623,   296,   648,   668,   208,   585,   669,   376,
     310,   818,   459,   224,   224,   673,   714,   585,   208,   365,
     560,   634,   378,   637,   259,   224,   379,   498,   224,   314,
     315,   737,    74,   585,  -206,   224,  -206,   498,   224,    75,
      76,    77,  -205,   514,  -205,   380,   224,   658,   381,   460,
      78,   316,    79,    80,    81,    82,   383,    83,    84,    85,
      86,    87,    88,   384,    89,    90,    91,    92,   408,   405,
     259,   550,   259,  -207,   259,  -207,   806,   259,   362,   676,
     317,   813,   386,   362,   411,   405,   436,   437,   529,   405,
     390,   690,   531,   405,   533,   405,   364,   567,   570,   437,
     519,   296,   296,   611,   362,   628,   405,   629,   405,   389,
     630,   405,   653,   362,   661,   437,   688,   689,   702,   703,
     704,   400,   708,   710,   401,   633,   403,   636,   638,   639,
     640,   396,   416,   724,   259,   259,   193,   420,   432,   438,
     259,   425,   259,   731,   426,   471,   450,   654,   496,   483,
     735,   485,   224,   486,   492,   493,   224,   495,   501,   508,
     512,   547,   553,   557,   564,   565,   568,   580,   581,   224,
     259,   589,   593,   259,   596,   223,   599,   224,   602,   224,
     605,   627,   635,   647,   650,   224,   656,   655,   657,   756,
     662,   757,   434,   659,   665,   223,   498,   467,   646,   667,
     670,   649,   764,   473,   672,   675,   716,   679,   697,   224,
     698,   699,   705,   224,   711,   712,   720,   721,   727,   296,
     224,   700,   725,   729,   732,   733,   707,   259,    69,    70,
      71,    72,    73,   734,   736,   739,   744,   740,   753,   754,
     758,   759,   760,   761,   726,   762,   769,   259,   259,   708,
     710,   771,   772,   773,   775,   777,   781,   784,   498,   682,
     785,   789,   790,   296,   691,   791,   693,   259,   259,   788,
     792,   795,   798,   259,   803,   800,   804,   805,   225,   259,
     807,    74,   810,   808,    13,   815,   812,   811,   814,   259,
     224,   817,   755,   566,   498,   259,   300,   715,   225,    69,
      70,    71,    72,    73,   329,   598,   763,   765,    85,    86,
      87,    88,   528,    89,    90,    91,    92,   326,   671,   666,
     306,   259,   694,   552,   252,   487,   579,   319,     0,     0,
       0,     0,     0,     0,   259,     0,   224,     0,   224,     0,
     224,     0,     0,   224,     0,     0,     0,    17,    18,     0,
       0,   752,    74,   796,     0,     0,     0,     0,     0,     0,
       0,    19,    20,    21,     0,     0,     0,    22,    23,    24,
       0,   766,   768,     0,     0,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,    25,     0,
       0,   778,   780,     0,     0,     0,     0,   783,     0,     0,
     224,   224,     0,   787,     0,     0,   224,     0,   224,    26,
       0,     0,     0,   794,     0,     0,     0,     0,     0,   799,
       0,     0,     0,     0,     0,    27,     0,     0,     0,     0,
       0,     0,     0,    28,    29,    30,   224,     0,     0,   224,
       0,     0,     0,     0,     0,   809,    31,    32,    33,     0,
       0,     0,     0,     0,     0,     0,    34,     0,   816,     0,
       0,     0,     0,     0,     0,    35,   466,     0,     0,     0,
      36,     0,   467,     0,     0,     0,    37,    38,     0,     0,
      17,    18,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   224,    19,    20,    21,     0,     0,     0,
      22,    23,    24,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   224,   224,     0,     0,     0,     0,     0,
       0,    25,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   224,   224,     0,     0,     0,     0,   224,
       0,     0,    26,     0,   224,   224,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   224,    17,    18,    27,     0,
       0,   224,     0,     0,   224,     0,    28,    29,    30,     0,
      19,    20,    21,     0,     0,     0,    22,    23,    24,    31,
      32,    33,     0,     0,     0,     0,     0,   224,     0,    34,
       0,     0,   515,   516,     0,     0,     0,    25,    35,   472,
     224,     0,     0,    36,     0,   473,     0,     0,     0,    37,
      38,    17,    18,     0,     0,     0,     0,     0,    26,     0,
       0,     0,     0,     0,     0,    19,    20,    21,     0,     0,
       0,    22,    23,    24,    27,     0,     0,     0,     0,     0,
       0,     0,    28,    29,    30,     0,     0,     0,     0,     0,
       0,     0,    25,     0,     0,    31,    32,    33,     0,   741,
     683,     0,     0,     0,     0,    34,     0,     0,     0,     0,
       0,     0,     0,    26,    35,     0,     0,     0,     0,    36,
       0,     0,     0,     0,     0,    37,    38,    17,    18,    27,
       0,     0,     0,     0,     0,     0,     0,    28,    29,    30,
       0,    19,    20,    21,     0,     0,     0,    22,    23,    24,
      31,    32,    33,     0,     0,     0,     0,     0,     0,     0,
      34,     0,     0,     0,     0,     0,     0,     0,    25,    35,
       0,     0,     0,     0,    36,   746,   683,     0,     0,     0,
      37,    38,    17,    18,     0,     0,     0,     0,     0,    26,
       0,     0,     0,     0,     0,     0,    19,    20,    21,     0,
       0,     0,    22,    23,    24,    27,     0,     0,     0,     0,
       0,     0,     0,    28,    29,    30,     0,     0,     0,     0,
       0,     0,     0,    25,     0,     0,    31,    32,    33,     0,
     748,   683,    17,    18,     0,     0,    34,     0,     0,     0,
       0,     0,     0,     0,    26,    35,    19,    20,    21,     0,
      36,     0,    22,    23,    24,     0,    37,    38,     0,     0,
      27,     0,     0,     0,     0,     0,     0,     0,    28,    29,
      30,     0,     0,    25,     0,     0,     0,     0,     0,     0,
       0,    31,    32,    33,     0,     0,     0,    17,    18,     0,
       0,    34,     0,     0,    26,     0,     0,     0,     0,     0,
      35,    19,    20,    21,     0,    36,     0,    22,    23,    24,
      27,    37,    38,     0,     0,     0,     0,     0,    28,    29,
      30,     0,     0,     0,     0,     0,     0,     0,    25,     0,
       0,    31,    32,    33,     0,     0,     0,    61,     0,     0,
       0,    34,     0,     0,     0,     0,     0,     0,     0,    26,
      35,     0,     0,     0,     0,    36,    17,    18,     0,     0,
       0,    37,    38,     0,     0,    27,     0,     0,     0,     0,
      19,    20,    21,    28,    29,    30,    22,    23,    24,     0,
       0,     0,     0,     0,     0,     0,    31,    32,    33,     0,
       0,     0,     0,     0,     0,     0,    34,    25,     0,     0,
       0,     0,     0,     0,     0,    35,   490,     0,     0,     0,
      36,     0,     0,     0,     0,     0,    37,    38,    26,     0,
       0,     0,     0,     0,     0,    17,    18,     0,     0,     0,
       0,     0,     0,     0,    27,     0,     0,     0,     0,    19,
      20,    21,    28,    29,    30,    22,    23,    24,     0,     0,
       0,     0,     0,     0,     0,    31,    32,    33,     0,     0,
       0,     0,     0,     0,     0,    34,    25,     0,     0,     0,
       0,     0,     0,   217,    35,     0,     0,     0,     0,    36,
      17,    18,     0,     0,     0,    37,    38,    26,     0,     0,
       0,     0,     0,     0,    19,    20,    21,     0,     0,     0,
      22,    23,    24,    27,     0,     0,     0,     0,     0,     0,
       0,    28,    29,    30,     0,     0,     0,     0,     0,     0,
       0,    25,     0,     0,    31,    32,    33,     0,     0,   683,
       0,     0,     0,     0,    34,     0,     0,     0,     0,     0,
       0,     0,    26,    35,     0,     0,     0,     0,    36,     0,
     467,     0,     0,     0,    37,    38,    17,    18,    27,     0,
       0,     0,     0,     0,     0,     0,    28,    29,    30,     0,
      19,    20,    21,     0,     0,     0,    22,    23,    24,    31,
      32,    33,     0,     0,     0,     0,     0,     0,     0,    34,
       0,     0,     0,     0,     0,     0,     0,    25,    35,     0,
       0,     0,     0,    36,     0,    17,    18,     0,     0,    37,
      38,     0,     0,     0,     0,     0,     0,     0,    26,    19,
      20,    21,     0,     0,     0,    22,    23,    24,     0,     0,
       0,     0,     0,     0,    27,     0,     0,     0,     0,     0,
       0,     0,    28,    29,    30,     0,    25,     0,     0,     0,
       0,     0,     0,     0,     0,    31,    32,    33,     0,     0,
       0,     0,     0,     0,     0,    34,     0,    26,     0,     0,
       0,     0,     0,     0,    35,   730,     0,     0,     0,    36,
       0,     0,     0,    27,     0,    37,    38,     0,     0,     0,
       0,    28,    29,    30,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    31,    32,    33,     0,     0,     0,
       0,     0,     0,   230,    34,   231,     0,     0,     0,   232,
       0,     0,     0,    35,     0,     0,     0,     0,    36,   233,
       0,     0,     0,     0,    37,    38,    67,    68,    69,    70,
      71,    72,    73,     0,   234,     0,   235,     0,     0,     0,
       0,   236,   237,     0,     0,     0,     0,   238,   239,   240,
       0,     0,     0,   241,     0,     0,     0,     0,   242,   243,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   244,     0,   245,   126,     0,     0,     0,
       0,    74,     0,     0,     0,     0,   246,   247,    75,    76,
      77,   248,     0,     0,     0,   249,     0,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,   250,
       0,     0,   513,     0,     0,    36,     0,     0,     0,   230,
     251,   231,   536,   537,     0,   538,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   539,   540,   541,     0,     0,
     230,     0,   231,     0,     0,     0,   232,     0,     0,     0,
     234,     0,   235,     0,     0,     0,   233,   236,   237,     0,
       0,     0,     0,   238,   239,   240,     0,     0,     0,   241,
       0,   234,   372,   235,   242,   243,     0,     0,   236,   237,
       0,     0,     0,     0,   238,   239,   240,     0,     0,   244,
     241,   245,   126,     0,     0,   242,   243,     0,     0,     0,
       0,     0,   246,   247,     0,     0,     0,   248,     0,     0,
     244,   249,   245,   126,   230,     0,   231,     0,     0,     0,
     232,     0,     0,   246,   247,     0,     0,     0,   248,     0,
     233,     0,   249,     0,     0,   250,     0,   373,     0,     0,
       0,    36,     0,     0,     0,   234,   251,   235,     0,     0,
       0,     0,   236,   237,     0,     0,   250,     0,   238,   239,
     240,     0,    36,     0,   241,     0,     0,   251,     0,   242,
     243,     0,   230,     0,   231,     0,     0,     0,   232,     0,
       0,     0,     0,     0,   244,     0,   245,   126,   233,     0,
       0,     0,     0,     0,     0,     0,     0,   246,   247,     0,
       0,     0,   248,   234,   497,   235,   249,     0,     0,     0,
     236,   237,     0,     0,     0,     0,   238,   239,   240,     0,
       0,     0,   241,     0,     0,     0,     0,   242,   243,     0,
     250,     0,     0,   396,     0,     0,    36,   230,     0,   231,
       0,   251,   244,   232,   245,   126,     0,     0,     0,     0,
       0,     0,     0,   233,     0,   246,   247,     0,     0,     0,
     248,     0,     0,     0,   249,     0,     0,     0,   234,     0,
     235,     0,     0,     0,     0,   236,   237,     0,     0,     0,
       0,   238,   239,   240,     0,     0,     0,   241,   250,     0,
       0,     0,   242,   243,    36,   230,     0,   231,     0,   251,
       0,   232,     0,     0,     0,     0,     0,   244,   507,   245,
     126,   233,     0,     0,     0,     0,     0,     0,     0,     0,
     246,   247,     0,     0,     0,   248,   234,     0,   235,   249,
       0,     0,     0,   236,   237,     0,     0,     0,     0,   238,
     239,   240,     0,     0,     0,   241,     0,   643,     0,     0,
     242,   243,     0,   250,     0,     0,     0,     0,     0,    36,
     230,     0,   231,     0,   251,   244,   232,   245,   126,     0,
       0,     0,     0,     0,     0,     0,   233,     0,   246,   247,
       0,     0,     0,   248,     0,     0,     0,   249,     0,     0,
       0,   234,   681,   235,     0,     0,     0,     0,   236,   237,
       0,     0,     0,     0,   238,   239,   240,     0,     0,     0,
     241,   250,     0,     0,     0,   242,   243,    36,   230,     0,
     231,     0,   251,     0,   232,     0,     0,     0,     0,     0,
     244,     0,   245,   126,   233,     0,     0,     0,     0,     0,
       0,     0,     0,   246,   247,     0,     0,     0,   248,   234,
       0,   235,   249,     0,     0,     0,   236,   237,     0,     0,
       0,     0,   238,   239,   240,     0,     0,     0,   241,     0,
     713,     0,     0,   242,   243,     0,   250,     0,     0,     0,
       0,     0,    36,   230,     0,   231,     0,   251,   244,   232,
     245,   126,     0,     0,     0,     0,     0,     0,     0,   233,
       0,   246,   247,     0,     0,     0,   248,     0,     0,     0,
     249,     0,     0,     0,   234,     0,   235,     0,     0,     0,
       0,   236,   237,     0,     0,     0,     0,   238,   239,   240,
       0,     0,     0,   241,   250,     0,     0,     0,   242,   243,
      36,   230,     0,   231,     0,   251,     0,   232,     0,     0,
       0,     0,     0,   244,     0,   245,   126,   233,     0,     0,
       0,     0,   230,     0,   231,     0,   246,   247,   232,     0,
       0,   248,   234,     0,   235,   249,     0,     0,   233,   236,
     237,     0,     0,     0,     0,   238,   239,   240,     0,     0,
       0,   241,     0,   234,     0,   235,   242,   243,     0,   250,
     236,   237,   779,     0,     0,    36,   238,   239,   240,     0,
     251,   244,   241,   245,   126,     0,     0,   242,   243,     0,
       0,     0,     0,     0,   246,   247,     0,     0,     0,   248,
       0,     0,   244,   249,   245,   126,    67,    68,    69,    70,
      71,    72,    73,     0,     0,   246,   247,     0,     0,     0,
     248,     0,     0,     0,   249,     0,     0,   250,     0,     0,
     782,     0,     0,    36,     0,     0,     0,     0,   251,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   250,     0,
       0,     0,     0,     0,    36,     0,     0,     0,     0,   251,
       0,    74,     0,     0,     0,     0,     0,     0,    75,    76,
      77,    67,    68,    69,    70,    71,    72,    73,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,   575,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    74,     0,     0,     0,
       0,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,    74,    89,    90,
      91,    92,     0,     0,    75,    76,    77,    67,    68,    69,
      70,    71,    72,    73,   576,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,     0,     0,     0,     0,     0,    67,    68,
      69,    70,    71,    72,    73,   577,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    74,     0,     0,     0,     0,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,     0,     0,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,    74,    89,    90,    91,    92,     0,     0,
      75,    76,    77,     0,     0,     0,    36,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,     0,     0,   107,   509,   108,   100,   101,
     102,   109,   110,   111,   112,   113,   114,   115,     0,     0,
       0,   116,   117,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   118,   281,     0,   282,     0,
       0,     0,   119,     0,     0,     0,   120,   121,   122,     0,
       0,     0,     0,     0,   123,     0,     0,     0,     0,     0,
     283,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   126,     0,
       0,     0,     0,     0,     0,     0,     0,   284,     0,     0,
       0,     0,     0,     0,   129,   130,     0,     0,   132,     0,
     133,     0,   423,    67,    68,    69,    70,    71,    72,    73,
       0,     0,     0,     0,     0,     0,    74,     0,     0,     0,
       0,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,     0,     0,     0,     0,     0,   500,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,    67,    68,
      69,    70,    71,    72,    73,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,     0,   510,
       0,     0,     0,     0,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,    74,
       0,     0,     0,     0,   622,     0,    75,    76,    77,    67,
      68,    69,    70,    71,    72,    73,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,     0,     0,     0,     0,     0,
     624,     0,     0,     0,     0,    67,    68,    69,    70,    71,
      72,    73,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    74,     0,     0,     0,     0,     0,
       0,    75,    76,    77,     0,     0,     0,     0,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
      74,     0,     0,     0,     0,   677,     0,    75,    76,    77,
      67,    68,    69,    70,    71,    72,    73,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,     0,     0,     0,     0,
       0,   678,     0,     0,     0,     0,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    74,     0,     0,     0,     0,
       0,     0,    75,    76,    77,     0,     0,     0,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,    74,     0,     0,     0,     0,   680,     0,    75,    76,
      77,    67,    68,    69,    70,    71,    72,    73,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,     0,
       0,     0,   692,     0,     0,     0,     0,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    74,     0,     0,     0,
       0,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,    74,     0,     0,     0,     0,   695,     0,    75,
      76,    77,    67,    68,    69,    70,    71,    72,    73,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,     0,     0,
       0,     0,     0,   696,     0,     0,     0,     0,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    74,     0,     0,
       0,     0,     0,     0,    75,    76,    77,     0,     0,     0,
       0,     0,     0,     0,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,    74,     0,     0,     0,     0,   728,     0,
      75,    76,    77,    67,    68,    69,    70,    71,    72,    73,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,     0,   738,     0,     0,     0,     0,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,    74,     0,     0,     0,     0,   750,
       0,    75,    76,    77,     0,     0,     0,     0,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
       0,     0,     0,     0,   107,   770,   108,   100,   101,   102,
     109,   110,   111,   112,   113,   114,   115,     0,     0,     0,
     116,   117,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   118,     0,     0,     0,     0,     0,
       0,   119,     0,     0,     0,   120,   121,   122,     0,     0,
       0,     0,     0,   123,     0,   124,     0,   125,     0,     0,
       0,     0,     0,     0,     0,     2,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   126,     0,     0,
       0,     0,     0,     0,   127,     0,   128,     0,     0,     0,
       0,     0,     0,   129,   130,   131,     0,   132,   107,   133,
     108,   100,   101,   102,   109,   110,   111,   112,   113,   114,
     115,     0,     0,     0,   116,   117,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   118,   281,
       0,   282,     0,     0,     0,   119,     0,     0,     0,   120,
     121,   122,     0,     0,     0,     0,     0,   123,     0,     0,
       0,     0,     0,   283,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   126,    67,     0,    69,    70,    71,    72,    73,   428,
     284,     0,     0,     0,     0,     0,     0,   129,   130,     0,
       0,   132,   107,   133,   108,   100,   101,   102,   109,   110,
     111,   112,   113,   114,   115,     0,     0,     0,   116,   117,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   118,   281,   554,   282,     0,    74,     0,   119,
       0,     0,     0,   120,   121,   122,     0,     0,     0,     0,
       0,   123,     0,     0,     0,     0,     0,   283,     0,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,     0,     0,   126,    67,     0,    69,    70,
      71,    72,    73,     0,   284,     0,     0,     0,     0,     0,
       0,   129,   130,     0,     0,   132,   107,   133,   108,   100,
     101,   102,   109,   110,   111,   112,   113,   114,   115,     0,
       0,     0,   116,   117,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   118,   281,   722,   282,
       0,    74,     0,   119,     0,     0,     0,   120,   121,   122,
       0,     0,     0,     0,     0,   123,     0,     0,     0,     0,
       0,   283,     0,     0,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,   126,
       0,     0,     0,     0,     0,     0,     0,     0,   284,     0,
       0,     0,     0,     0,     0,   129,   130,     0,     0,   132,
     107,   133,   108,   100,   101,   102,   109,   110,   111,   112,
     113,   114,   115,     0,     0,     0,   116,   117,     0,     0,
       0,    67,    68,    69,    70,    71,    72,    73,     0,     0,
     118,   281,     0,   282,     0,     0,     0,   119,     0,     0,
       0,   120,   121,   122,     0,     0,     0,     0,     0,   123,
       0,     0,     0,     0,     0,   283,     0,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   126,     0,     0,    74,     0,     0,     0,
       0,     0,   284,    75,    76,    77,     0,     0,     0,   129,
     130,     0,     0,   132,    78,   133,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,    74,     0,     0,     0,   160,     0,     0,    75,
      76,    77,    67,    68,    69,    70,    71,    72,    73,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,     0,     0,
       0,     0,   318,     0,     0,     0,     0,     0,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    74,     0,     0,
       0,     0,     0,     0,    75,    76,    77,     0,     0,     0,
       0,     0,     0,     0,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,    74,     0,     0,     0,   574,     0,     0,
      75,    76,    77,    67,    68,    69,    70,    71,    72,    73,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,   607,     0,     0,     0,     0,     0,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,    74,     0,     0,     0,   608,     0,
       0,    75,    76,    77,    67,    68,    69,    70,    71,    72,
      73,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
       0,     0,     0,     0,   609,     0,     0,     0,     0,     0,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    74,
       0,     0,     0,     0,     0,     0,    75,    76,    77,     0,
       0,     0,     0,     0,     0,     0,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,    74,     0,     0,     0,   610,
       0,     0,    75,    76,    77,    67,    68,    69,    70,    71,
      72,    73,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,     0,     0,     0,     0,   612,     0,     0,     0,     0,
       0,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      74,     0,     0,     0,     0,     0,     0,    75,    76,    77,
       0,     0,     0,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,    74,     0,     0,     0,
     614,     0,     0,    75,    76,    77,    67,    68,    69,    70,
      71,    72,    73,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,     0,     0,     0,     0,   652,     0,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    74,     0,     0,     0,     0,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,     0,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,    74,     0,     0,
       0,   774,     0,     0,    75,    76,    77,    67,    68,    69,
      70,    71,    72,    73,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,     0,     0,     0,     0,   776,     0,     0,
       0,     0,     0,     0,     0,     0,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    74,     0,     0,     0,     0,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,     0,     0,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,   314,   315,
       0,    74,   819,     0,     0,     0,     0,     0,    75,    76,
      77,    67,    68,    69,    70,    71,    72,    73,     0,    78,
     316,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    74,     0,     0,     0,
       0,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,     0,     0,     0,    78,   320,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,    74,    89,    90,
      91,    92,     0,     0,    75,    76,    77,    67,    68,    69,
      70,    71,    72,    73,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,     0,     0,     0,     0,     0,    67,     0,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    74,     0,     0,     0,     0,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,    74,    89,    90,    91,    92,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92
};

static const yytype_int16 yycheck[] =
{
      10,   293,    43,   281,    18,    45,   419,   307,   383,   219,
     542,   244,   414,    18,   401,     5,   418,   549,    28,    29,
      30,    31,    32,    33,    34,    35,    36,    37,    38,     5,
       5,     5,    47,     5,     5,     5,    34,    51,     5,    49,
       5,     5,    52,   108,    16,     5,    51,     5,     5,   121,
     122,   426,     5,     5,    21,     5,    21,    67,    68,    69,
      70,    71,    72,    73,    74,    75,    76,    77,    78,    79,
      80,    81,    82,    83,    84,    85,    86,    87,    88,    89,
      90,    91,    92,     5,   471,     5,    48,   127,     5,    94,
      13,   478,    79,     5,     5,   135,     8,     9,    10,    21,
       5,   106,   102,   124,    45,     0,     4,     5,    45,   130,
      45,     5,    45,   645,     4,     5,   121,   122,   122,   124,
     124,   122,     3,   124,    45,   125,     5,   121,   126,   130,
      45,   121,   424,   546,    45,    45,     5,   127,   125,    45,
     154,   116,   442,   545,   149,   150,   108,   121,   122,   154,
     121,   127,   162,   127,   219,   220,   118,    45,   130,   130,
     130,   123,   122,   130,     4,   130,   231,   208,    47,    48,
     132,    42,   130,   130,     4,     5,   125,   130,   130,   128,
     130,   191,   415,   193,    82,    66,   125,   719,   398,   399,
      84,   130,    82,   265,   135,   267,     5,   269,   135,   214,
     135,   126,   135,   122,   127,   130,   211,   212,   130,   596,
     130,   123,     5,   130,   135,    45,   121,   122,   127,   751,
     135,   130,   116,   122,   122,   135,   236,   232,   122,   135,
     129,   130,   122,    83,   647,   767,   246,   247,    47,    48,
     250,   281,   122,   117,   123,   123,   261,   135,   149,   129,
     130,   129,   123,   293,   125,    12,    13,   219,   220,    16,
     265,   793,   267,   496,   269,   122,   116,   117,   118,   231,
     275,   124,   234,   130,   122,   553,   122,   130,   124,   241,
     118,   122,   244,   129,   130,   123,   699,   684,   130,   130,
     252,   688,   689,   358,   132,   126,     5,   362,   303,   130,
     310,   311,   307,   127,   314,   315,   316,   720,   124,   542,
     320,   124,   322,    12,   130,   325,   126,   130,   383,   334,
     124,    11,    12,    13,    16,   340,    16,   332,   333,    16,
     344,   232,   233,   348,   123,   407,   125,   342,   410,   344,
     123,   413,   125,   129,   130,    30,    31,    32,   761,     8,
       9,   366,    11,   363,   124,   125,    30,    31,    32,   651,
     652,   426,    21,    22,    23,    61,   376,     5,    64,   379,
     380,   381,     5,   414,   384,   750,   684,   418,     5,   389,
     688,   689,    99,   284,   424,   395,   401,     5,   398,   399,
       8,     9,    10,   403,     6,   770,   358,   123,    83,   125,
     362,   302,   122,   241,   124,   306,   122,   126,   124,    83,
     420,     5,   108,   375,   252,   425,   123,   123,   125,   125,
       5,   383,   118,   385,   434,   430,   126,   123,   433,   391,
     115,   116,   117,   118,     5,   440,   132,   442,   112,   113,
     450,   115,   116,   117,   118,    67,    68,    69,    70,    71,
      72,    73,    74,   415,   124,   125,   471,   419,   122,   124,
     124,   126,    16,   364,   426,   123,   123,   125,   125,   370,
     123,   123,   125,   125,   124,   485,   486,   769,   123,   126,
     125,     4,   492,   123,   123,   125,   125,    28,    29,    30,
      31,    32,    33,    34,   126,    18,    19,    20,   123,   509,
     125,    24,    25,    26,   545,   515,   516,   123,     5,   125,
     520,   125,   522,   553,   123,   123,   125,   125,   123,   122,
     125,   813,    45,   219,   220,   123,   123,   125,   125,   124,
     431,   536,     5,   538,   496,   231,   122,   375,   234,    80,
      81,   123,    83,   125,    57,   241,    59,   385,   244,    90,
      91,    92,    57,   391,    59,   122,   252,   567,   122,    82,
     101,   102,   103,   104,   105,   106,   122,   108,   109,   110,
     111,   112,   113,   122,   115,   116,   117,   118,   124,   125,
     542,   419,   544,    57,   546,    59,   123,   549,   125,   599,
     131,   123,     5,   125,   124,   125,   124,   125,   124,   125,
       5,   611,   124,   125,   124,   125,   125,   126,   124,   125,
     620,   651,   652,   124,   125,   124,   125,   124,   125,   122,
     124,   125,   124,   125,   124,   125,   609,   610,   633,   634,
     635,   124,   637,   638,   122,   536,   126,   538,   539,   540,
     541,   124,     5,   653,   606,   607,   130,   126,   124,     5,
     612,   122,   614,   663,   122,   122,   126,   558,     5,   125,
     670,   126,   358,   126,   126,   124,   362,   124,   124,   124,
     124,     5,     5,   124,   124,     5,   124,     5,   124,   375,
     642,     5,   124,   645,   122,   750,   126,   383,   124,   385,
     124,   124,    11,   124,    59,   391,   128,   127,   124,   704,
       5,   706,   126,   124,   124,   770,   544,   129,   546,   124,
     122,   549,   717,   129,   124,   123,    57,   124,   124,   415,
     124,   124,   124,   419,   124,   124,   124,    59,     5,   769,
     426,   632,   128,   124,     4,   124,   637,   699,    30,    31,
      32,    33,    34,   124,   124,    39,    52,   102,   124,   124,
     124,     5,   124,   124,   655,    57,    39,   719,   720,   764,
     765,     5,   128,   124,   131,   124,    52,    52,   606,   607,
      52,   124,     5,   813,   612,   124,   614,   739,   740,    57,
     124,   124,    57,   745,   124,    59,     5,   122,   750,   751,
      57,    83,    57,   124,     4,   805,    59,   124,   124,   761,
     496,    57,   703,   437,   642,   767,   135,   645,   770,    30,
      31,    32,    33,    34,   208,   483,   717,   718,   110,   111,
     112,   113,   405,   115,   116,   117,   118,   197,   591,   585,
     150,   793,   620,   422,   118,   362,   462,   162,    -1,    -1,
      -1,    -1,    -1,    -1,   806,    -1,   542,    -1,   544,    -1,
     546,    -1,    -1,   549,    -1,    -1,    -1,     4,     5,    -1,
      -1,   699,    83,   764,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    18,    19,    20,    -1,    -1,    -1,    24,    25,    26,
      -1,   719,   720,    -1,    -1,   106,    -1,   108,   109,   110,
     111,   112,   113,    -1,   115,   116,   117,   118,    45,    -1,
      -1,   739,   740,    -1,    -1,    -1,    -1,   745,    -1,    -1,
     606,   607,    -1,   751,    -1,    -1,   612,    -1,   614,    66,
      -1,    -1,    -1,   761,    -1,    -1,    -1,    -1,    -1,   767,
      -1,    -1,    -1,    -1,    -1,    82,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    91,    92,   642,    -1,    -1,   645,
      -1,    -1,    -1,    -1,    -1,   793,   103,   104,   105,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   113,    -1,   806,    -1,
      -1,    -1,    -1,    -1,    -1,   122,   123,    -1,    -1,    -1,
     127,    -1,   129,    -1,    -1,    -1,   133,   134,    -1,    -1,
       4,     5,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   699,    18,    19,    20,    -1,    -1,    -1,
      24,    25,    26,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   719,   720,    -1,    -1,    -1,    -1,    -1,
      -1,    45,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   739,   740,    -1,    -1,    -1,    -1,   745,
      -1,    -1,    66,    -1,   750,   751,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   761,     4,     5,    82,    -1,
      -1,   767,    -1,    -1,   770,    -1,    90,    91,    92,    -1,
      18,    19,    20,    -1,    -1,    -1,    24,    25,    26,   103,
     104,   105,    -1,    -1,    -1,    -1,    -1,   793,    -1,   113,
      -1,    -1,    40,    41,    -1,    -1,    -1,    45,   122,   123,
     806,    -1,    -1,   127,    -1,   129,    -1,    -1,    -1,   133,
     134,     4,     5,    -1,    -1,    -1,    -1,    -1,    66,    -1,
      -1,    -1,    -1,    -1,    -1,    18,    19,    20,    -1,    -1,
      -1,    24,    25,    26,    82,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    45,    -1,    -1,   103,   104,   105,    -1,    52,
      53,    -1,    -1,    -1,    -1,   113,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    66,   122,    -1,    -1,    -1,    -1,   127,
      -1,    -1,    -1,    -1,    -1,   133,   134,     4,     5,    82,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,
      -1,    18,    19,    20,    -1,    -1,    -1,    24,    25,    26,
     103,   104,   105,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     113,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    45,   122,
      -1,    -1,    -1,    -1,   127,    52,    53,    -1,    -1,    -1,
     133,   134,     4,     5,    -1,    -1,    -1,    -1,    -1,    66,
      -1,    -1,    -1,    -1,    -1,    -1,    18,    19,    20,    -1,
      -1,    -1,    24,    25,    26,    82,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    45,    -1,    -1,   103,   104,   105,    -1,
      52,    53,     4,     5,    -1,    -1,   113,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    66,   122,    18,    19,    20,    -1,
     127,    -1,    24,    25,    26,    -1,   133,   134,    -1,    -1,
      82,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,
      92,    -1,    -1,    45,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   103,   104,   105,    -1,    -1,    -1,     4,     5,    -1,
      -1,   113,    -1,    -1,    66,    -1,    -1,    -1,    -1,    -1,
     122,    18,    19,    20,    -1,   127,    -1,    24,    25,    26,
      82,   133,   134,    -1,    -1,    -1,    -1,    -1,    90,    91,
      92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    45,    -1,
      -1,   103,   104,   105,    -1,    -1,    -1,   109,    -1,    -1,
      -1,   113,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    66,
     122,    -1,    -1,    -1,    -1,   127,     4,     5,    -1,    -1,
      -1,   133,   134,    -1,    -1,    82,    -1,    -1,    -1,    -1,
      18,    19,    20,    90,    91,    92,    24,    25,    26,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   103,   104,   105,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   113,    45,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   122,   123,    -1,    -1,    -1,
     127,    -1,    -1,    -1,    -1,    -1,   133,   134,    66,    -1,
      -1,    -1,    -1,    -1,    -1,     4,     5,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    82,    -1,    -1,    -1,    -1,    18,
      19,    20,    90,    91,    92,    24,    25,    26,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   103,   104,   105,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   113,    45,    -1,    -1,    -1,
      -1,    -1,    -1,   121,   122,    -1,    -1,    -1,    -1,   127,
       4,     5,    -1,    -1,    -1,   133,   134,    66,    -1,    -1,
      -1,    -1,    -1,    -1,    18,    19,    20,    -1,    -1,    -1,
      24,    25,    26,    82,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    45,    -1,    -1,   103,   104,   105,    -1,    -1,    53,
      -1,    -1,    -1,    -1,   113,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    66,   122,    -1,    -1,    -1,    -1,   127,    -1,
     129,    -1,    -1,    -1,   133,   134,     4,     5,    82,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,
      18,    19,    20,    -1,    -1,    -1,    24,    25,    26,   103,
     104,   105,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   113,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    45,   122,    -1,
      -1,    -1,    -1,   127,    -1,     4,     5,    -1,    -1,   133,
     134,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    66,    18,
      19,    20,    -1,    -1,    -1,    24,    25,    26,    -1,    -1,
      -1,    -1,    -1,    -1,    82,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    90,    91,    92,    -1,    45,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   103,   104,   105,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   113,    -1,    66,    -1,    -1,
      -1,    -1,    -1,    -1,   122,   123,    -1,    -1,    -1,   127,
      -1,    -1,    -1,    82,    -1,   133,   134,    -1,    -1,    -1,
      -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   103,   104,   105,    -1,    -1,    -1,
      -1,    -1,    -1,     5,   113,     7,    -1,    -1,    -1,    11,
      -1,    -1,    -1,   122,    -1,    -1,    -1,    -1,   127,    21,
      -1,    -1,    -1,    -1,   133,   134,    28,    29,    30,    31,
      32,    33,    34,    -1,    36,    -1,    38,    -1,    -1,    -1,
      -1,    43,    44,    -1,    -1,    -1,    -1,    49,    50,    51,
      -1,    -1,    -1,    55,    -1,    -1,    -1,    -1,    60,    61,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    75,    -1,    77,    78,    -1,    -1,    -1,
      -1,    83,    -1,    -1,    -1,    -1,    88,    89,    90,    91,
      92,    93,    -1,    -1,    -1,    97,    -1,    -1,    -1,   101,
      -1,   103,   104,   105,   106,    -1,   108,   109,   110,   111,
     112,   113,    -1,   115,   116,   117,   118,    -1,    -1,   121,
      -1,    -1,   124,    -1,    -1,   127,    -1,    -1,    -1,     5,
     132,     7,     8,     9,    -1,    11,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    21,    22,    23,    -1,    -1,
       5,    -1,     7,    -1,    -1,    -1,    11,    -1,    -1,    -1,
      36,    -1,    38,    -1,    -1,    -1,    21,    43,    44,    -1,
      -1,    -1,    -1,    49,    50,    51,    -1,    -1,    -1,    55,
      -1,    36,    37,    38,    60,    61,    -1,    -1,    43,    44,
      -1,    -1,    -1,    -1,    49,    50,    51,    -1,    -1,    75,
      55,    77,    78,    -1,    -1,    60,    61,    -1,    -1,    -1,
      -1,    -1,    88,    89,    -1,    -1,    -1,    93,    -1,    -1,
      75,    97,    77,    78,     5,    -1,     7,    -1,    -1,    -1,
      11,    -1,    -1,    88,    89,    -1,    -1,    -1,    93,    -1,
      21,    -1,    97,    -1,    -1,   121,    -1,   102,    -1,    -1,
      -1,   127,    -1,    -1,    -1,    36,   132,    38,    -1,    -1,
      -1,    -1,    43,    44,    -1,    -1,   121,    -1,    49,    50,
      51,    -1,   127,    -1,    55,    -1,    -1,   132,    -1,    60,
      61,    -1,     5,    -1,     7,    -1,    -1,    -1,    11,    -1,
      -1,    -1,    -1,    -1,    75,    -1,    77,    78,    21,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    88,    89,    -1,
      -1,    -1,    93,    36,    37,    38,    97,    -1,    -1,    -1,
      43,    44,    -1,    -1,    -1,    -1,    49,    50,    51,    -1,
      -1,    -1,    55,    -1,    -1,    -1,    -1,    60,    61,    -1,
     121,    -1,    -1,   124,    -1,    -1,   127,     5,    -1,     7,
      -1,   132,    75,    11,    77,    78,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    21,    -1,    88,    89,    -1,    -1,    -1,
      93,    -1,    -1,    -1,    97,    -1,    -1,    -1,    36,    -1,
      38,    -1,    -1,    -1,    -1,    43,    44,    -1,    -1,    -1,
      -1,    49,    50,    51,    -1,    -1,    -1,    55,   121,    -1,
      -1,    -1,    60,    61,   127,     5,    -1,     7,    -1,   132,
      -1,    11,    -1,    -1,    -1,    -1,    -1,    75,    76,    77,
      78,    21,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      88,    89,    -1,    -1,    -1,    93,    36,    -1,    38,    97,
      -1,    -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,
      50,    51,    -1,    -1,    -1,    55,    -1,    57,    -1,    -1,
      60,    61,    -1,   121,    -1,    -1,    -1,    -1,    -1,   127,
       5,    -1,     7,    -1,   132,    75,    11,    77,    78,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    21,    -1,    88,    89,
      -1,    -1,    -1,    93,    -1,    -1,    -1,    97,    -1,    -1,
      -1,    36,    37,    38,    -1,    -1,    -1,    -1,    43,    44,
      -1,    -1,    -1,    -1,    49,    50,    51,    -1,    -1,    -1,
      55,   121,    -1,    -1,    -1,    60,    61,   127,     5,    -1,
       7,    -1,   132,    -1,    11,    -1,    -1,    -1,    -1,    -1,
      75,    -1,    77,    78,    21,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    88,    89,    -1,    -1,    -1,    93,    36,
      -1,    38,    97,    -1,    -1,    -1,    43,    44,    -1,    -1,
      -1,    -1,    49,    50,    51,    -1,    -1,    -1,    55,    -1,
      57,    -1,    -1,    60,    61,    -1,   121,    -1,    -1,    -1,
      -1,    -1,   127,     5,    -1,     7,    -1,   132,    75,    11,
      77,    78,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    21,
      -1,    88,    89,    -1,    -1,    -1,    93,    -1,    -1,    -1,
      97,    -1,    -1,    -1,    36,    -1,    38,    -1,    -1,    -1,
      -1,    43,    44,    -1,    -1,    -1,    -1,    49,    50,    51,
      -1,    -1,    -1,    55,   121,    -1,    -1,    -1,    60,    61,
     127,     5,    -1,     7,    -1,   132,    -1,    11,    -1,    -1,
      -1,    -1,    -1,    75,    -1,    77,    78,    21,    -1,    -1,
      -1,    -1,     5,    -1,     7,    -1,    88,    89,    11,    -1,
      -1,    93,    36,    -1,    38,    97,    -1,    -1,    21,    43,
      44,    -1,    -1,    -1,    -1,    49,    50,    51,    -1,    -1,
      -1,    55,    -1,    36,    -1,    38,    60,    61,    -1,   121,
      43,    44,   124,    -1,    -1,   127,    49,    50,    51,    -1,
     132,    75,    55,    77,    78,    -1,    -1,    60,    61,    -1,
      -1,    -1,    -1,    -1,    88,    89,    -1,    -1,    -1,    93,
      -1,    -1,    75,    97,    77,    78,    28,    29,    30,    31,
      32,    33,    34,    -1,    -1,    88,    89,    -1,    -1,    -1,
      93,    -1,    -1,    -1,    97,    -1,    -1,   121,    -1,    -1,
     124,    -1,    -1,   127,    -1,    -1,    -1,    -1,   132,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   121,    -1,
      -1,    -1,    -1,    -1,   127,    -1,    -1,    -1,    -1,   132,
      -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,
      92,    28,    29,    30,    31,    32,    33,    34,    -1,   101,
      -1,   103,   104,   105,   106,    -1,   108,   109,   110,   111,
     112,   113,    -1,   115,   116,   117,   118,    -1,    -1,    -1,
      -1,    -1,    28,    29,    30,    31,    32,    33,    34,   131,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   101,    -1,   103,   104,   105,   106,
      -1,   108,   109,   110,   111,   112,   113,    83,   115,   116,
     117,   118,    -1,    -1,    90,    91,    92,    28,    29,    30,
      31,    32,    33,    34,   131,   101,    -1,   103,   104,   105,
     106,    -1,   108,   109,   110,   111,   112,   113,    -1,   115,
     116,   117,   118,    -1,    -1,    -1,    -1,    -1,    28,    29,
      30,    31,    32,    33,    34,   131,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     101,    -1,   103,   104,   105,   106,    -1,   108,   109,   110,
     111,   112,   113,    83,   115,   116,   117,   118,    -1,    -1,
      90,    91,    92,    -1,    -1,    -1,   127,    -1,    -1,    -1,
      -1,   101,    -1,   103,   104,   105,   106,    -1,   108,   109,
     110,   111,   112,   113,    -1,   115,   116,   117,   118,    -1,
      -1,    -1,    -1,    -1,    -1,     5,   126,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    16,    17,    -1,    -1,
      -1,    21,    22,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    35,    36,    -1,    38,    -1,
      -1,    -1,    42,    -1,    -1,    -1,    46,    47,    48,    -1,
      -1,    -1,    -1,    -1,    54,    -1,    -1,    -1,    -1,    -1,
      60,    28,    29,    30,    31,    32,    33,    34,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    78,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    87,    -1,    -1,
      -1,    -1,    -1,    -1,    94,    95,    -1,    -1,    98,    -1,
     100,    -1,   102,    28,    29,    30,    31,    32,    33,    34,
      -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   101,    -1,   103,   104,   105,   106,
      -1,   108,   109,   110,   111,   112,   113,    -1,   115,   116,
     117,   118,    -1,    -1,    -1,    -1,    -1,   124,    83,    -1,
      -1,    -1,    -1,    -1,    -1,    90,    91,    92,    28,    29,
      30,    31,    32,    33,    34,    -1,   101,    -1,   103,   104,
     105,   106,    -1,   108,   109,   110,   111,   112,   113,    -1,
     115,   116,   117,   118,    -1,    -1,    -1,    -1,    -1,   124,
      -1,    -1,    -1,    -1,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   101,    -1,   103,   104,   105,   106,    -1,   108,   109,
     110,   111,   112,   113,    -1,   115,   116,   117,   118,    83,
      -1,    -1,    -1,    -1,   124,    -1,    90,    91,    92,    28,
      29,    30,    31,    32,    33,    34,    -1,   101,    -1,   103,
     104,   105,   106,    -1,   108,   109,   110,   111,   112,   113,
      -1,   115,   116,   117,   118,    -1,    -1,    -1,    -1,    -1,
     124,    -1,    -1,    -1,    -1,    28,    29,    30,    31,    32,
      33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,
      -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   101,    -1,   103,   104,   105,   106,    -1,   108,
     109,   110,   111,   112,   113,    -1,   115,   116,   117,   118,
      83,    -1,    -1,    -1,    -1,   124,    -1,    90,    91,    92,
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
      -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   101,    -1,   103,   104,   105,   106,    -1,   108,
     109,   110,   111,   112,   113,    -1,   115,   116,   117,   118,
      -1,    -1,    -1,    -1,     5,   124,     7,     8,     9,    10,
      11,    12,    13,    14,    15,    16,    17,    -1,    -1,    -1,
      21,    22,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    35,    -1,    -1,    -1,    -1,    -1,
      -1,    42,    -1,    -1,    -1,    46,    47,    48,    -1,    -1,
      -1,    -1,    -1,    54,    -1,    56,    -1,    58,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    66,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    78,    -1,    -1,
      -1,    -1,    -1,    -1,    85,    -1,    87,    -1,    -1,    -1,
      -1,    -1,    -1,    94,    95,    96,    -1,    98,     5,   100,
       7,     8,     9,    10,    11,    12,    13,    14,    15,    16,
      17,    -1,    -1,    -1,    21,    22,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    35,    36,
      -1,    38,    -1,    -1,    -1,    42,    -1,    -1,    -1,    46,
      47,    48,    -1,    -1,    -1,    -1,    -1,    54,    -1,    -1,
      -1,    -1,    -1,    60,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    78,    28,    -1,    30,    31,    32,    33,    34,    86,
      87,    -1,    -1,    -1,    -1,    -1,    -1,    94,    95,    -1,
      -1,    98,     5,   100,     7,     8,     9,    10,    11,    12,
      13,    14,    15,    16,    17,    -1,    -1,    -1,    21,    22,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    35,    36,    37,    38,    -1,    83,    -1,    42,
      -1,    -1,    -1,    46,    47,    48,    -1,    -1,    -1,    -1,
      -1,    54,    -1,    -1,    -1,    -1,    -1,    60,    -1,   105,
     106,    -1,   108,   109,   110,   111,   112,   113,    -1,   115,
     116,   117,   118,    -1,    -1,    78,    28,    -1,    30,    31,
      32,    33,    34,    -1,    87,    -1,    -1,    -1,    -1,    -1,
      -1,    94,    95,    -1,    -1,    98,     5,   100,     7,     8,
       9,    10,    11,    12,    13,    14,    15,    16,    17,    -1,
      -1,    -1,    21,    22,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    35,    36,    37,    38,
      -1,    83,    -1,    42,    -1,    -1,    -1,    46,    47,    48,
      -1,    -1,    -1,    -1,    -1,    54,    -1,    -1,    -1,    -1,
      -1,    60,    -1,    -1,   106,    -1,   108,   109,   110,   111,
     112,   113,    -1,   115,   116,   117,   118,    -1,    -1,    78,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    87,    -1,
      -1,    -1,    -1,    -1,    -1,    94,    95,    -1,    -1,    98,
       5,   100,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    -1,    -1,    -1,    21,    22,    -1,    -1,
      -1,    28,    29,    30,    31,    32,    33,    34,    -1,    -1,
      35,    36,    -1,    38,    -1,    -1,    -1,    42,    -1,    -1,
      -1,    46,    47,    48,    -1,    -1,    -1,    -1,    -1,    54,
      -1,    -1,    -1,    -1,    -1,    60,    -1,    28,    29,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    78,    -1,    -1,    83,    -1,    -1,    -1,
      -1,    -1,    87,    90,    91,    92,    -1,    -1,    -1,    94,
      95,    -1,    -1,    98,   101,   100,   103,   104,   105,   106,
      -1,   108,   109,   110,   111,   112,   113,    -1,   115,   116,
     117,   118,    83,    -1,    -1,    -1,   123,    -1,    -1,    90,
      91,    92,    28,    29,    30,    31,    32,    33,    34,    -1,
     101,    -1,   103,   104,   105,   106,    -1,   108,   109,   110,
     111,   112,   113,    -1,   115,   116,   117,   118,    -1,    -1,
      -1,    -1,   123,    -1,    -1,    -1,    -1,    -1,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,
      -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   101,    -1,   103,   104,   105,
     106,    -1,   108,   109,   110,   111,   112,   113,    -1,   115,
     116,   117,   118,    83,    -1,    -1,    -1,   123,    -1,    -1,
      90,    91,    92,    28,    29,    30,    31,    32,    33,    34,
      -1,   101,    -1,   103,   104,   105,   106,    -1,   108,   109,
     110,   111,   112,   113,    -1,   115,   116,   117,   118,    -1,
      -1,    -1,    -1,   123,    -1,    -1,    -1,    -1,    -1,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,
      -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   101,    -1,   103,   104,
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
      -1,    -1,    -1,    -1,    -1,    -1,    28,    29,    30,    31,
      32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     101,    -1,   103,   104,   105,   106,    -1,   108,   109,   110,
     111,   112,   113,    -1,   115,   116,   117,   118,    80,    81,
      -1,    83,   123,    -1,    -1,    -1,    -1,    -1,    90,    91,
      92,    28,    29,    30,    31,    32,    33,    34,    -1,   101,
     102,   103,   104,   105,   106,    -1,   108,   109,   110,   111,
     112,   113,    -1,   115,   116,   117,   118,    -1,    -1,    -1,
      -1,    -1,    28,    29,    30,    31,    32,    33,    34,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   101,   102,   103,   104,   105,   106,
      -1,   108,   109,   110,   111,   112,   113,    83,   115,   116,
     117,   118,    -1,    -1,    90,    91,    92,    28,    29,    30,
      31,    32,    33,    34,    -1,   101,    -1,   103,   104,   105,
     106,    -1,   108,   109,   110,   111,   112,   113,    -1,   115,
     116,   117,   118,    -1,    -1,    -1,    -1,    -1,    28,    -1,
      30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   104,   105,   106,    -1,   108,   109,   110,
     111,   112,   113,    83,   115,   116,   117,   118,    -1,    -1,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   104,   105,   106,    -1,   108,   109,
     110,   111,   112,   113,    -1,   115,   116,   117,   118
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
      13,   127,   124,   197,   126,   198,   124,   125,     5,   197,
       5,   149,   198,   207,   207,   207,   207,   207,   207,   207,
     126,   207,     4,    18,    19,    20,    24,    25,    26,    45,
      82,   206,   126,   198,     5,   198,   123,   129,   167,   168,
     194,   122,   123,   129,   170,   171,   194,   123,   122,   198,
     198,   199,   194,   125,   196,   126,   126,   190,   207,   197,
     123,   194,   126,   124,   197,   124,     5,    37,   182,   207,
     124,   124,   207,   207,   207,   189,   207,    76,   124,   126,
     124,   207,   124,   124,   182,    40,    41,   180,   181,   207,
     169,   207,   169,   207,   167,   194,   123,   207,   163,   124,
     162,   124,   162,   124,   162,   142,     8,     9,    11,    21,
      22,    23,   157,   158,   195,   122,   124,     5,   142,   157,
     182,   207,   184,     5,    37,   207,   189,   124,   127,   198,
     197,   124,   198,   207,   124,     5,   148,   126,   124,   198,
     124,     5,   149,   198,   123,   131,   131,   131,   207,   206,
       5,   124,     5,   116,   123,   125,   123,   167,   194,     5,
     123,   125,   123,   124,   123,   167,   122,   123,   153,   126,
     207,   207,   124,   123,   207,   124,   195,   123,   123,   123,
     123,   124,   123,   207,   123,   207,   207,    42,   123,   125,
     179,   207,   124,   207,   124,   123,   123,   124,   124,   124,
     124,   123,    21,   197,   198,    11,   197,   198,   197,   197,
     197,   158,   195,    57,   142,   157,   182,   124,   123,   182,
      59,   175,   123,   124,   197,   127,   128,   124,   207,   124,
     124,   124,     5,   122,   130,   124,   168,   124,   123,   123,
     122,   171,   124,   123,   167,   123,   207,   124,   124,   124,
     124,    37,   182,    53,   191,   192,   193,   194,   191,   191,
     207,   182,   124,   182,   181,   124,   124,   124,   124,   124,
     197,   124,   198,   198,   198,   124,     5,   197,   198,   124,
     198,   124,   124,    57,   123,   182,    57,    11,    21,   157,
     124,    59,    37,   176,   207,   128,   197,     5,   124,   124,
     123,   207,     4,   124,   124,   207,   124,   123,   124,    39,
     102,    52,   192,   193,    52,   102,    52,   193,    52,   193,
     124,   157,   182,   124,   124,   197,   198,   198,   124,     5,
     124,   124,    57,   197,   198,   197,   182,   157,   182,    39,
     124,     5,   128,   124,   123,   131,   123,   124,   182,   124,
     182,    52,   124,   182,    52,    52,   189,   182,    57,   124,
       5,   124,   124,   157,   182,   124,   197,   124,    57,   182,
      59,   176,   189,   124,     5,   122,   123,    57,   124,   182,
      57,   124,    59,   123,   124,   207,   182,    57,   176,   123
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
#line 3090 "y.tab.c"
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


#line 393 "yaccs/verilog.yacc"


