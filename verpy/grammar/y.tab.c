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
#define YYLAST   5008

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  135
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  73
/* YYNRULES -- Number of rules.  */
#define YYNRULES  362
/* YYNRULES -- Number of states.  */
#define YYNSTATES  813

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
     203,   213,   222,   230,   234,   241,   249,   256,   262,   264,
     266,   268,   270,   272,   274,   276,   278,   280,   282,   289,
     295,   304,   312,   319,   328,   338,   348,   359,   366,   372,
     381,   391,   394,   396,   400,   404,   408,   413,   419,   425,
     432,   436,   441,   447,   452,   456,   461,   465,   470,   475,
     481,   487,   491,   496,   502,   506,   510,   512,   516,   520,
     522,   527,   532,   538,   542,   548,   555,   559,   565,   572,
     579,   586,   593,   599,   607,   616,   624,   632,   636,   638,
     641,   647,   652,   661,   666,   669,   672,   675,   679,   681,
     687,   690,   695,   698,   701,   704,   709,   713,   716,   719,
     723,   727,   730,   732,   736,   742,   746,   748,   750,   752,
     754,   756,   758,   760,   762,   764,   766,   772,   780,   790,
     793,   796,   799,   804,   806,   808,   812,   814,   817,   820,
     822,   826,   829,   832,   838,   842,   847,   853,   858,   864,
     870,   878,   882,   886,   890,   895,   899,   905,   908,   912,
     916,   921,   927,   934,   942,   949,   956,   964,   971,   979,
     983,   987,   990,   992,   994,   996,   999,  1001,  1007,  1011,
    1015,  1017,  1021,  1023,  1027,  1037,  1043,  1049,  1053,  1055,
    1059,  1062,  1064,  1068,  1072,  1076,  1080,  1084,  1086,  1089,
    1091,  1093,  1096,  1100,  1104,  1107,  1109,  1111,  1115,  1117,
    1123,  1129,  1135,  1139,  1141,  1143,  1145,  1148,  1151,  1154,
    1157,  1160,  1163,  1167,  1170,  1173,  1175,  1177,  1179,  1181,
    1183,  1185,  1188,  1191,  1193,  1195,  1197,  1199,  1201,  1205,
    1209,  1211,  1214,  1216,  1219,  1223,  1227,  1232,  1237,  1244,
    1246,  1248,  1250,  1252,  1254,  1256,  1258,  1260,  1262,  1264,
    1266,  1268,  1270,  1272,  1274,  1279,  1281,  1283,  1285,  1287,
    1289,  1291,  1294,  1298,  1302,  1305,  1311,  1315,  1319,  1323,
    1327,  1331,  1335,  1339,  1343,  1347,  1351,  1355,  1359,  1363,
    1367,  1371,  1375,  1379,  1383,  1387,  1391,  1395,  1399,  1403,
    1407,  1411,  1416,  1420,  1422,  1425,  1428,  1431,  1434,  1437,
    1440,  1443,  1446
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
       5,   124,    -1,   100,    99,    13,   127,   197,   128,     5,
     124,    -1,   100,    99,   127,   197,   128,     5,   124,    -1,
       7,   189,   124,    -1,     7,   169,   196,   126,   207,   124,
      -1,     7,   152,   169,   196,   126,   207,   124,    -1,     7,
     152,   196,   126,   207,   124,    -1,   122,   153,   125,   153,
     123,    -1,    67,    -1,    68,    -1,    69,    -1,    70,    -1,
      71,    -1,    72,    -1,    73,    -1,    74,    -1,   198,    -1,
      21,    -1,    56,     5,   124,   157,   195,    57,    -1,    56,
       5,   124,   195,    57,    -1,    56,   198,   198,     5,   124,
     157,   182,    57,    -1,    56,   154,     5,   124,   157,   182,
      57,    -1,    56,   154,     5,   124,   182,    57,    -1,    56,
       5,   122,   142,   123,   124,   182,    57,    -1,    56,     5,
     122,   142,   123,   124,   157,   182,    57,    -1,    56,   154,
       5,   122,   142,   123,   124,   182,    57,    -1,    56,   154,
       5,   122,   142,   123,   124,   157,   182,    57,    -1,    58,
       5,   124,   157,   182,    59,    -1,    58,     5,   124,   182,
      59,    -1,    58,     5,   122,   142,   123,   124,   182,    59,
      -1,    58,     5,   122,   142,   123,   124,   157,   182,    59,
      -1,   157,   158,    -1,   158,    -1,    11,   197,   124,    -1,
      22,   197,   124,    -1,    23,   197,   124,    -1,    11,   198,
     197,   124,    -1,    11,   198,     5,   198,   124,    -1,    11,
     198,   198,     5,   124,    -1,     9,    11,   198,   198,     5,
     124,    -1,     8,   197,   124,    -1,     8,   197,   198,   124,
      -1,     8,   198,   198,   197,   124,    -1,     8,    21,   197,
     124,    -1,    21,   197,   124,    -1,    21,   197,   198,   124,
      -1,    47,   162,   124,    -1,    47,    16,   162,   124,    -1,
      47,   198,   162,   124,    -1,    47,   198,   198,   162,   124,
      -1,    47,    16,   198,   162,   124,    -1,    48,   162,   124,
      -1,    48,   198,   162,   124,    -1,    48,   198,   198,   162,
     124,    -1,    46,   162,   124,    -1,   162,   125,   163,    -1,
     163,    -1,     5,   126,   207,    -1,   164,   125,   165,    -1,
     165,    -1,    48,     5,   126,   207,    -1,    47,     5,   126,
     207,    -1,    47,   198,     5,   126,   207,    -1,     5,   126,
     207,    -1,     5,     5,   122,   123,   124,    -1,     5,   172,
       5,   122,   123,   124,    -1,     5,     5,   124,    -1,    42,
     122,   194,   123,   124,    -1,    42,     5,   122,   194,   123,
     124,    -1,     5,     5,   122,   167,   123,   124,    -1,    42,
       5,   122,   167,   123,   124,    -1,     5,     5,   122,   194,
     123,   124,    -1,     5,   122,   194,   123,   124,    -1,     5,
     172,     5,   122,   167,   123,   124,    -1,     5,   172,     5,
     198,   122,   167,   123,   124,    -1,     5,     5,   198,   122,
     167,   123,   124,    -1,     5,     5,   198,   122,   194,   123,
     124,    -1,   167,   125,   168,    -1,   168,    -1,   129,   116,
      -1,   129,     5,   122,   207,   123,    -1,   129,     5,   122,
     123,    -1,   129,     5,   130,     4,   131,   122,   207,   123,
      -1,   121,   122,   194,   123,    -1,   121,     4,    -1,   121,
       5,    -1,   121,    82,    -1,   170,   125,   171,    -1,   171,
      -1,   129,     5,   122,   207,   123,    -1,   129,     5,    -1,
     121,   122,   194,   123,    -1,   121,     4,    -1,   121,    82,
      -1,   121,     5,    -1,   121,   122,   170,   123,    -1,   121,
     122,   123,    -1,    98,   182,    -1,    35,   182,    -1,    35,
     178,   182,    -1,    85,   175,    86,    -1,   175,   176,    -1,
     176,    -1,    36,   175,    37,    -1,    36,   102,     5,   175,
      37,    -1,    87,   197,   124,    -1,   150,    -1,   151,    -1,
     159,    -1,   160,    -1,   161,    -1,   166,    -1,   177,    -1,
     173,    -1,   147,    -1,   185,    -1,    38,   122,   207,   123,
     176,    -1,    38,   122,   207,   123,   176,    39,   176,    -1,
      60,   122,   189,   124,   207,   124,   189,   123,   176,    -1,
     132,   116,    -1,   132,    84,    -1,   132,     5,    -1,   132,
     122,   180,   123,    -1,    42,    -1,   125,    -1,   180,   179,
     181,    -1,   181,    -1,    40,   207,    -1,    41,   207,    -1,
     207,    -1,    36,   195,    37,    -1,    36,    37,    -1,    55,
     182,    -1,    36,   102,     5,   195,    37,    -1,    75,   195,
      76,    -1,   196,   126,   207,   124,    -1,   196,   126,   169,
     207,   124,    -1,   196,    34,   207,   124,    -1,   196,    34,
     169,   207,   124,    -1,    38,   122,   207,   123,   182,    -1,
      38,   122,   207,   123,   182,    39,   182,    -1,    43,   207,
     124,    -1,    21,   197,   124,    -1,    11,   197,   124,    -1,
      11,   198,   197,   124,    -1,    89,   207,   124,    -1,    88,
     207,   126,   207,   124,    -1,   178,   124,    -1,    44,     5,
     124,    -1,    77,     5,   124,    -1,     5,   122,   123,   124,
      -1,     5,   122,   194,   123,   124,    -1,    49,   122,   207,
     123,   191,    52,    -1,    49,   122,   207,   123,   191,   193,
      52,    -1,    49,   122,   207,   123,   193,    52,    -1,    50,
     122,   207,   123,   191,    52,    -1,    50,   122,   207,   123,
     191,   193,    52,    -1,    51,   122,   207,   123,   191,    52,
      -1,    51,   122,   207,   123,   191,   193,    52,    -1,   121,
     207,   124,    -1,   121,   207,   182,    -1,     5,   124,    -1,
     186,    -1,   187,    -1,   188,    -1,   205,   124,    -1,   185,
      -1,     7,   196,   126,   207,   124,    -1,    97,     5,   124,
      -1,   183,   125,   184,    -1,   184,    -1,     5,   126,   207,
      -1,    45,    -1,    78,   183,    79,    -1,    60,   122,   189,
     124,   207,   124,   189,   123,   182,    -1,    93,   122,   207,
     123,   182,    -1,    61,   122,   207,   123,   182,    -1,   189,
     125,   190,    -1,   190,    -1,   196,   126,   207,    -1,   191,
     192,    -1,   192,    -1,   194,   102,   182,    -1,   194,   102,
     124,    -1,    53,   102,   182,    -1,    53,   102,   124,    -1,
     194,   125,   207,    -1,   207,    -1,   195,   182,    -1,   182,
      -1,     5,    -1,     5,   198,    -1,     5,   199,   198,    -1,
       5,   199,   199,    -1,     5,   199,    -1,   205,    -1,   202,
      -1,     5,   125,   197,    -1,     5,    -1,   130,   207,   102,
     207,   131,    -1,   130,   207,    80,   207,   131,    -1,   130,
     207,    81,   207,   131,    -1,   130,   207,   131,    -1,     8,
      -1,     9,    -1,    10,    -1,     9,    11,    -1,     8,    12,
      -1,     9,    12,    -1,    10,    12,    -1,     8,    16,    -1,
       9,    16,    -1,     9,    11,    16,    -1,     9,    13,    -1,
       8,    13,    -1,    13,    -1,    11,    -1,    12,    -1,    16,
      -1,    21,    -1,    22,    -1,    11,    16,    -1,    12,    16,
      -1,    87,    -1,    94,    -1,    95,    -1,    14,    -1,    15,
      -1,   127,   203,   128,    -1,   203,   125,   204,    -1,   204,
      -1,   207,   202,    -1,   207,    -1,   109,   202,    -1,     5,
     129,   205,    -1,     5,   129,     5,    -1,     5,   129,     5,
     198,    -1,     5,   129,     5,   199,    -1,     5,   129,     5,
     122,   207,   123,    -1,     4,    -1,    82,    -1,    45,    -1,
      18,    -1,    19,    -1,    20,    -1,    24,    -1,    25,    -1,
      26,    -1,     5,    -1,   205,    -1,     4,    -1,    82,    -1,
      45,    -1,    66,    -1,    66,   122,   207,   123,    -1,    18,
      -1,    19,    -1,    20,    -1,    24,    -1,    25,    -1,    26,
      -1,     5,   198,    -1,     5,   199,   198,    -1,     5,   199,
     199,    -1,     5,   199,    -1,   207,   101,   207,   102,   207,
      -1,   207,   112,   207,    -1,   207,   116,   207,    -1,   207,
     113,   207,    -1,   207,   117,   207,    -1,   207,   118,   207,
      -1,   207,   104,   207,    -1,   207,   103,   207,    -1,   207,
     105,   207,    -1,   207,   110,   207,    -1,   207,   111,   207,
      -1,   207,    83,   207,    -1,   207,    28,   207,    -1,   207,
      29,   207,    -1,   207,    90,   207,    -1,   207,    91,   207,
      -1,   207,    92,   207,    -1,   207,    31,   207,    -1,   207,
      30,   207,    -1,   207,    32,   207,    -1,   207,   115,   207,
      -1,   207,    33,   207,    -1,   207,    34,   207,    -1,   207,
     109,   207,    -1,   207,   108,   207,    -1,   207,   106,   207,
      -1,     5,   122,   194,   123,    -1,   122,   207,   123,    -1,
     202,    -1,   113,   207,    -1,   103,   207,    -1,   105,   207,
      -1,   104,   207,    -1,    90,   207,    -1,    92,   207,    -1,
      91,   207,    -1,   133,   207,    -1,   134,   207,    -1
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
      98,    99,   100,   105,   106,   107,   108,   111,   112,   112,
     112,   112,   112,   112,   112,   112,   113,   113,   115,   116,
     117,   118,   119,   120,   121,   122,   123,   126,   127,   128,
     129,   132,   132,   134,   135,   136,   137,   138,   139,   140,
     141,   142,   143,   144,   145,   146,   150,   151,   152,   153,
     154,   156,   156,   156,   157,   159,   159,   160,   162,   162,
     164,   165,   166,   167,   171,   172,   173,   174,   175,   176,
     177,   178,   179,   180,   181,   182,   183,   191,   191,   192,
     192,   192,   192,   194,   194,   194,   194,   195,   195,   196,
     196,   197,   197,   197,   197,   197,   197,   200,   200,   200,
     203,   205,   205,   208,   209,   210,   211,   212,   213,   214,
     215,   216,   217,   218,   219,   220,   221,   222,   227,   232,
     232,   232,   232,   233,   233,   234,   234,   235,   235,   235,
     240,   241,   242,   243,   244,   245,   246,   247,   248,   249,
     250,   251,   252,   253,   254,   255,   256,   257,   258,   259,
     260,   261,   262,   263,   264,   265,   266,   267,   268,   269,
     270,   271,   272,   273,   274,   275,   276,   277,   278,   282,
     282,   283,   283,   285,   287,   288,   289,   290,   290,   291,
     292,   292,   293,   293,   294,   294,   296,   296,   297,   297,
     300,   300,   300,   300,   300,   300,   300,   302,   302,   304,
     304,   304,   305,   307,   307,   307,   307,   307,   307,   307,
     307,   307,   307,   307,   307,   309,   309,   309,   309,   309,
     309,   309,   309,   309,   309,   309,   309,   309,   311,   312,
     312,   314,   315,   316,   320,   321,   322,   323,   324,   328,
     329,   330,   331,   331,   331,   331,   331,   331,   335,   336,
     337,   338,   339,   340,   341,   342,   342,   342,   342,   342,
     342,   343,   344,   345,   346,   347,   348,   349,   350,   351,
     352,   353,   354,   355,   356,   357,   358,   359,   360,   361,
     362,   363,   364,   365,   366,   367,   368,   369,   370,   371,
     372,   373,   374,   375,   376,   377,   378,   379,   380,   381,
     382,   383,   384
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
     150,   150,   150,   151,   151,   151,   151,   152,   153,   153,
     153,   153,   153,   153,   153,   153,   154,   154,   155,   155,
     155,   155,   155,   155,   155,   155,   155,   156,   156,   156,
     156,   157,   157,   158,   158,   158,   158,   158,   158,   158,
     158,   158,   158,   158,   158,   158,   159,   159,   159,   159,
     159,   160,   160,   160,   161,   162,   162,   163,   164,   164,
     165,   165,   165,   165,   166,   166,   166,   166,   166,   166,
     166,   166,   166,   166,   166,   166,   166,   167,   167,   168,
     168,   168,   168,   169,   169,   169,   169,   170,   170,   171,
     171,   172,   172,   172,   172,   172,   172,   173,   173,   173,
     174,   175,   175,   176,   176,   176,   176,   176,   176,   176,
     176,   176,   176,   176,   176,   176,   176,   176,   177,   178,
     178,   178,   178,   179,   179,   180,   180,   181,   181,   181,
     182,   182,   182,   182,   182,   182,   182,   182,   182,   182,
     182,   182,   182,   182,   182,   182,   182,   182,   182,   182,
     182,   182,   182,   182,   182,   182,   182,   182,   182,   182,
     182,   182,   182,   182,   182,   182,   182,   182,   182,   183,
     183,   184,   184,   185,   186,   187,   188,   189,   189,   190,
     191,   191,   192,   192,   193,   193,   194,   194,   195,   195,
     196,   196,   196,   196,   196,   196,   196,   197,   197,   198,
     198,   198,   199,   200,   200,   200,   200,   200,   200,   200,
     200,   200,   200,   200,   200,   201,   201,   201,   201,   201,
     201,   201,   201,   201,   201,   201,   201,   201,   202,   203,
     203,   204,   204,   204,   205,   205,   205,   205,   205,   206,
     206,   206,   206,   206,   206,   206,   206,   206,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   207
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
       9,     8,     7,     3,     6,     7,     6,     5,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     6,     5,
       8,     7,     6,     8,     9,     9,    10,     6,     5,     8,
       9,     2,     1,     3,     3,     3,     4,     5,     5,     6,
       3,     4,     5,     4,     3,     4,     3,     4,     4,     5,
       5,     3,     4,     5,     3,     3,     1,     3,     3,     1,
       4,     4,     5,     3,     5,     6,     3,     5,     6,     6,
       6,     6,     5,     7,     8,     7,     7,     3,     1,     2,
       5,     4,     8,     4,     2,     2,     2,     3,     1,     5,
       2,     4,     2,     2,     2,     4,     3,     2,     2,     3,
       3,     2,     1,     3,     5,     3,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     5,     7,     9,     2,
       2,     2,     4,     1,     1,     3,     1,     2,     2,     1,
       3,     2,     2,     5,     3,     4,     5,     4,     5,     5,
       7,     3,     3,     3,     4,     3,     5,     2,     3,     3,
       4,     5,     6,     7,     6,     6,     7,     6,     7,     3,
       3,     2,     1,     1,     1,     2,     1,     5,     3,     3,
       1,     3,     1,     3,     9,     5,     5,     3,     1,     3,
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
      41,    40,     1,     3,     0,     0,     0,   310,   308,   315,
     316,   317,   318,   319,   320,   312,   313,   311,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   353,
     309,    42,     0,     0,    11,    25,     0,     0,     0,     0,
     321,   324,     0,   358,   360,   359,   355,   357,   356,   354,
       0,     0,     0,   290,   292,   361,   362,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     9,     0,   119,    21,
     263,   264,   265,     0,     0,    15,     0,     0,     0,   276,
     277,   275,   286,   287,   278,     0,   279,   280,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   283,   284,
     285,    39,     0,     0,     0,    25,    37,    34,    26,    27,
      35,    36,    31,    32,    33,    28,    29,    30,    38,     0,
       0,     0,     0,   247,   295,   294,     0,   322,   323,     0,
     352,   293,     0,   288,   291,   337,   338,   343,   342,   344,
     346,   347,   336,   339,   340,   341,     0,   332,   331,   333,
     350,   349,   348,   334,   335,   326,   328,   345,   327,   329,
     330,     0,     0,     0,     0,     0,     8,     0,   267,   274,
     270,   266,   268,   273,   271,   269,    13,     0,     0,    16,
       0,     0,     0,     0,     0,     0,   250,     0,     0,     0,
       0,     0,   238,     0,   256,   255,   281,   282,   258,     0,
     250,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   158,   226,   222,   223,   224,     0,   255,
       0,     0,     0,     0,   116,     0,     0,     0,     0,     0,
       0,    44,     0,    77,     0,    76,     0,     0,   232,     0,
     230,     0,     0,     0,   283,   174,   166,   167,   168,   169,
     170,   171,   173,     0,   162,   172,   175,   157,     0,     7,
      24,     0,     0,    45,    48,     0,     0,     0,    43,   351,
       0,     0,   296,   297,     0,     0,     0,   262,   314,   289,
       0,   123,     0,     0,     0,     0,   118,   272,    12,    14,
       0,    18,    17,     0,     0,   126,     0,   152,   154,   153,
       0,     0,     0,   251,   254,   144,   145,   146,     0,    68,
      69,    70,    71,    72,    73,    74,    75,     0,     0,     0,
       0,    63,     0,     0,     0,    52,     0,   221,     0,     0,
       0,     0,   191,     0,   249,     0,     0,     0,     0,     0,
       0,     0,   192,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   181,   180,   179,     0,   207,   159,     0,     0,
     225,     0,     0,     0,   114,     0,     0,     0,   106,     0,
       0,   111,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   233,     0,     0,     0,     0,     0,     0,   160,   161,
       0,     0,    49,     0,     0,     0,    53,     0,   258,     0,
      45,     0,     0,   246,     0,     0,     0,     0,   325,   121,
       0,   120,   299,   302,   303,   304,   305,   306,   307,   301,
     300,    22,     0,    19,    20,     0,     0,     0,   138,     0,
       0,   156,     0,     0,   148,     0,     0,     0,     0,   252,
     253,     0,     0,     0,     0,     0,   237,   239,   257,     0,
       0,     0,   203,     0,   202,     0,   190,   248,     0,   201,
     208,     0,     0,     0,     0,     0,   194,   209,     0,   205,
       0,   228,   219,   220,     0,     0,     0,   186,   189,     0,
       0,     0,     0,     0,     0,     0,   117,   115,   107,     0,
     108,     0,   112,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    92,     0,     0,     0,     0,     0,     0,     0,
     231,   229,     0,   163,     0,     0,   165,     0,     0,     0,
      50,     0,    46,    57,    45,    47,     0,    58,     0,    54,
       0,   298,   260,   261,   259,   122,    23,   124,     0,   139,
       0,     0,     0,     0,     0,   150,   155,     0,   151,   132,
       0,     0,     0,   143,     0,     0,     0,     0,   210,     0,
       0,   204,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   187,   188,   183,   182,   184,     0,     0,   197,     0,
     195,     0,     0,   127,   110,   109,   113,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    91,     0,    79,
       0,     0,     0,     0,     0,     0,    88,     0,     0,     0,
       0,     0,     0,    51,     0,    56,    55,     0,     0,   129,
     137,   131,     0,     0,     0,   147,   125,     0,     0,    67,
       0,    66,    64,   211,   227,   193,   199,     0,     0,   241,
       0,     0,     0,     0,     0,   236,   206,   235,   185,   198,
     196,   130,   128,     0,     0,   100,     0,     0,     0,    93,
     258,     0,     0,   104,     0,    94,    95,    78,     0,     0,
      82,     0,     0,     0,     0,    87,   164,   176,     0,     0,
       0,     0,    59,   141,     0,     0,   135,   136,     0,   133,
       0,    65,     0,     0,   212,   240,     0,   214,     0,   215,
       0,   217,     0,     0,     0,     0,   103,   101,     0,     0,
       0,    96,     0,   105,     0,    81,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    62,   140,     0,   149,
     134,   200,   245,   244,   213,   243,   242,   216,   218,     0,
       0,    83,   102,     0,    97,    98,     0,     0,    93,     0,
     104,    80,     0,    89,   177,     0,    61,     0,     0,     0,
      84,    99,     0,    85,    96,    90,     0,    60,     0,   234,
      86,   178,   142
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,     3,     4,     5,     6,    15,    45,   104,   105,   134,
     135,     7,   285,   304,   305,   286,   287,   219,   357,   274,
     140,   141,   541,   542,   288,   289,   290,   263,   264,    97,
      98,   291,   467,   468,   220,   473,   474,   215,   292,   147,
     293,   294,   295,   270,   616,   516,   517,   374,   279,   280,
     254,   255,   256,   257,   221,   222,   678,   679,   680,   681,
     375,   258,   229,   343,   344,   149,   150,    39,    62,    63,
      40,   461,   153
};

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
#define YYPACT_NINF -513
static const yytype_int16 yypact[] =
{
      49,   149,   105,   173,    49,  -513,  -513,  -513,   152,   230,
    1708,  -513,  -513,  -513,   174,   -18,   110,  -513,    92,  -513,
    -513,  -513,  -513,  -513,  -513,  -513,   177,  -513,  1708,  1708,
    1708,  1708,  1708,  1708,  1708,  1708,  1332,  1708,  1708,  -513,
    -513,  4794,    51,    83,  -513,  3679,   323,  1708,   350,  1708,
    -513,   228,  1708,  -513,  -513,  -513,  -513,  -513,  -513,  -513,
    4053,   180,   155,  -513,  2729,  -513,  -513,  1708,  1708,  1708,
    1708,  1708,  1708,  1708,  1708,  1708,  1708,  1708,  1708,  1708,
    1708,  1708,  1708,  1708,  1708,  1708,  1708,  1708,  1708,  1708,
    1708,  1708,  1708,   224,     8,   357,  -513,    11,  -513,  -513,
     282,   273,   356,   256,    95,  -513,    29,    89,    10,   392,
     415,  -513,  -513,  -513,  -513,   386,  -513,  -513,  2484,    40,
     438,    25,    28,  2484,    30,   475,   106,  4055,  -513,  -513,
    -513,  -513,  2484,   299,   388,  3679,  -513,  -513,  -513,  -513,
    -513,  -513,  -513,  -513,  -513,  -513,  -513,  -513,  -513,    39,
      27,   481,   129,  4794,   101,  -513,  2537,  -513,  -513,  4089,
    -513,  -513,  1332,  -513,  -513,  3729,  4890,   150,   150,   150,
     329,   329,  -513,   631,   631,   631,  4763,  4859,   631,  3824,
     372,   372,   372,   329,   329,   420,   420,   150,  -513,  -513,
    -513,  1708,   365,  1708,   488,   369,  -513,   181,  -513,  -513,
    -513,   485,  -513,  -513,  -513,  -513,  -513,   373,   111,   384,
     534,    48,    67,    97,  1708,   535,   113,   103,   453,    26,
      12,   193,  -513,   416,  -513,  -513,  -513,  -513,   418,   417,
     141,    12,    39,   386,  1962,   422,  1708,   543,   427,   428,
     429,  2484,   430,   431,  2484,   549,  1708,  1708,   435,   553,
    1708,    91,  2036,  -513,  -513,  -513,  -513,  -513,     9,   436,
     440,  1708,   439,   207,  -513,    28,   222,    28,   248,    28,
     442,  -513,   200,  -513,   559,   437,   201,   444,  -513,    18,
    -513,  2880,   446,   450,   386,  -513,  -513,  -513,  -513,  -513,
    -513,  -513,  -513,  3773,  -513,  -513,  -513,  -513,    72,  -513,
    -513,   451,   386,   183,  -513,   262,   569,    50,  -513,  -513,
    1708,  1708,  -513,  -513,  1708,  1708,  1708,  -513,  -513,  -513,
    1708,  4794,  1708,  4698,   456,  1708,  -513,  -513,  -513,  -513,
     576,  -513,   190,   571,   886,  -513,   462,  -513,  -513,  -513,
    1017,   203,    19,  -513,   228,  -513,  -513,  -513,  1708,  -513,
    -513,  -513,  -513,  -513,  -513,  -513,  -513,   452,    12,   464,
     465,  -513,    12,  1708,   386,  -513,  1424,  -513,   466,   469,
     386,   479,  -513,   583,  -513,  2094,  1708,  2913,   480,  1708,
    1708,  1708,  -513,    12,  1708,  2159,   486,  2760,  2955,  1708,
     487,  1815,  -513,  -513,  -513,  1155,  -513,  -513,  1458,  1458,
    -513,  1548,   213,  1708,  -513,   438,   324,   438,  -513,   337,
     438,  -513,   345,   438,   111,  1941,   217,   594,   111,  1941,
    1708,  -513,   106,   600,  3867,  1708,    12,   489,  -513,  -513,
      37,   386,  -513,    -7,  1708,   490,  -513,   604,   347,   491,
     183,   352,   604,  4794,  4154,  2568,  2633,  2664,  4794,  4794,
    1708,  4794,  -513,  -513,  -513,  -513,  -513,  -513,  -513,  -513,
    -513,  -513,   576,  -513,  -513,   493,    84,   219,  -513,   220,
    1548,  -513,   607,   229,  -513,   242,   494,    42,   497,  -513,
    -513,   267,   453,   496,  1708,  1708,  -513,  4794,  -513,   499,
     272,  1708,  -513,   500,  -513,  2484,  -513,  -513,  4190,  -513,
    -513,  4255,  4291,  4356,   354,  4392,  -513,  -513,  1708,  -513,
    4457,  -513,  -513,  -513,  1708,  1708,     5,  -513,  4794,  1708,
    3020,  1708,  3056,   276,   284,   501,  4794,  -513,  -513,   375,
    -513,   382,  -513,   389,   291,    33,   615,    39,   386,   386,
     386,  1941,  -513,  2217,   111,  1941,   503,   294,  1941,   570,
    4794,  -513,  4055,  -513,  4493,   393,  -513,   386,   504,   502,
    -513,   508,  4794,  -513,   507,  -513,  1708,  -513,   510,  -513,
     404,  -513,  -513,  -513,  -513,  4794,  -513,  -513,    54,  -513,
     511,   509,   513,   295,   302,   506,  -513,   514,  -513,  -513,
     518,   303,   509,  -513,   521,  1708,  3121,  3157,  -513,   525,
    3222,  -513,  2282,  2484,  1582,  1708,  1708,  1708,  2484,  3258,
    2484,  4794,  4794,  -513,  -513,  -513,  1155,  3323,  -513,  3359,
    -513,   526,   527,  -513,  -513,  -513,  -513,   528,   386,   114,
     437,   437,   529,    79,   126,   531,   542,  -513,  2340,  -513,
     307,  1941,   588,   238,   544,   610,  -513,  3961,  4055,  1708,
     545,   386,   665,  -513,  3424,  -513,  -513,  1674,   667,  -513,
    -513,  -513,   548,   556,  1708,  -513,  -513,   557,   311,  -513,
    3460,  -513,  -513,  -513,  -513,  -513,   638,   580,  1158,  -513,
     633,    43,  1279,  1282,  3525,  -513,  -513,  -513,  -513,  -513,
    -513,  -513,  -513,  1941,   563,  -513,   564,   386,   437,   378,
     109,   566,   678,   397,   567,  -513,  -513,  -513,   568,   636,
    -513,    39,   386,  1941,  1941,  -513,  -513,   655,  3561,   690,
     572,   573,  -513,  -513,  4558,   574,  -513,  -513,  4594,  -513,
     577,  -513,  2484,  2405,  -513,  -513,   646,  -513,  2463,  -513,
     650,  -513,   651,    12,  1941,   647,  -513,  -513,   582,   703,
     585,   401,   586,  -513,  1941,  -513,   587,    79,   151,   659,
    1941,   653,  4055,    12,   593,   714,  -513,  -513,   598,  -513,
    -513,  -513,  -513,  -513,  -513,  -513,  -513,  -513,  -513,   342,
     664,  -513,  -513,   599,  -513,  -513,  1941,   668,  -513,   602,
    -513,  -513,   669,  -513,  -513,   343,  -513,   603,  1708,  2484,
    -513,  -513,   672,  -513,  -513,  -513,  4055,  -513,  4659,  -513,
    -513,  -513,  -513
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -513,  -513,  -513,   720,  -513,  -513,  -513,  -402,   522,   597,
    -513,    55,    58,   296,  -298,    60,    69,  -513,   252,  -513,
    -513,  -513,  -379,  -512,    73,    77,    80,   -73,   330,  -513,
     541,    81,  -387,   169,  -211,  -513,   166,   605,    82,  -513,
    -275,  -291,  -513,   639,  -513,  -513,   138,   170,  -513,   334,
     -40,  -513,  -513,  -513,  -380,   396,   -74,  -480,  -391,   -37,
    -233,  -107,   314,   227,   -14,   -36,  -513,   455,  -513,   601,
      38,   297,   -10
};

/* YYTABLE[YYPACT[STATE-NUM]].  What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule which
   number is the opposite.  If zero, do what YYDEFACT says.
   If YYTABLE_NINF, syntax error.  */
#define YYTABLE_NINF -205
static const yytype_int16 yytable[] =
{
      41,   223,   429,   504,    51,   148,   424,   106,   358,   441,
     152,   385,   534,   192,   523,   216,   547,   216,    53,    54,
      55,    56,    57,    58,    59,    60,    64,    65,    66,   637,
     262,   216,   303,   262,   209,   272,   637,   158,   228,   156,
     548,   265,   159,   398,   228,   260,   555,   613,   266,   268,
     210,   273,     1,   332,   628,   440,    93,   165,   166,   167,
     168,   169,   170,   171,   172,   173,   174,   175,   176,   177,
     178,   179,   180,   181,   182,   183,   184,   185,   186,   187,
     188,   189,   190,   583,   700,   430,   155,   296,    99,   578,
     591,   100,   101,   102,   212,   148,   392,   421,    94,    95,
     136,   337,   338,   137,    43,   138,    44,   345,   346,     9,
      10,   277,   359,   360,   139,     2,    99,   560,   142,   100,
     101,   102,   143,   193,   368,   144,   145,   146,   614,   637,
     615,   217,   218,   429,   196,   399,   197,    36,   193,    36,
     313,   477,   640,   422,   570,   738,   225,   217,   213,   193,
      11,   278,    64,    36,     8,   193,   259,   193,   193,   193,
     193,   259,   261,   193,   557,   590,   641,   193,   310,   193,
     259,   466,   106,    12,    96,   393,   657,   341,   193,   339,
     193,   321,   543,   323,   658,   347,    93,   519,   521,   334,
     136,   335,   406,   137,   409,   138,   412,   193,   735,   431,
     579,   637,   735,   735,   139,   668,   103,   394,   142,   193,
     213,   214,   143,   395,    47,   144,   145,   146,   207,   340,
     208,    48,    49,   311,   402,   348,   377,    46,    94,    95,
      48,    49,   637,    74,   364,    16,   387,   388,   695,   193,
     391,   296,    48,    49,   193,    50,   535,   536,   637,   711,
     703,   483,   309,   296,   310,   223,   193,   225,   225,   712,
     539,   540,   602,   366,   713,   367,    90,    91,    92,   225,
      48,    49,   259,    14,   637,   790,   223,   647,   157,   259,
     162,   193,   259,   163,   201,   202,   203,   736,   253,   204,
     259,   740,   742,   271,   198,   199,    42,   469,   200,    52,
     443,   444,   297,   475,   445,   446,   447,    36,   638,   434,
     448,   481,   449,   193,   744,   451,   462,   361,   362,   223,
     193,   194,   414,   418,   415,   419,   476,   151,   310,   490,
     480,   404,   405,   211,   529,   760,   525,   531,   310,   544,
     533,   545,   580,   582,   581,   310,   408,   405,   267,   269,
     191,   275,   586,   487,   587,   154,   429,   717,    49,    69,
      70,    71,   195,   779,   524,   588,   498,   310,   205,   501,
     502,   503,   411,   405,   505,   786,   302,   307,   106,   510,
     206,   312,   106,   795,   296,   518,   436,   437,   520,   522,
     593,   228,   310,   526,   299,   599,   225,   310,   298,   621,
     225,   581,    69,    70,    71,    72,    73,   622,   226,   310,
     550,   382,    74,   259,   627,   554,   208,   644,   662,   208,
     581,   225,   397,   259,   562,   663,   667,   310,   581,   259,
     708,   227,   208,   584,   730,  -203,   581,  -203,   333,   336,
     575,    87,    88,   262,    89,    90,    91,    92,   528,   405,
      69,    70,    71,   259,  -202,    74,  -202,   259,  -204,   370,
    -204,   530,   405,   301,   225,   799,   806,   362,   362,   532,
     405,   794,   364,   566,   596,   597,   569,   437,   607,   362,
     276,   600,    85,    86,    87,    88,   308,    89,    90,    91,
      92,   322,   407,   324,   410,   325,   413,   328,   609,   624,
     405,   327,   417,    74,   611,   612,   625,   405,   106,   617,
     330,   619,   296,   626,   405,   811,   161,   649,   362,   164,
     349,   350,   351,   352,   353,   354,   355,   356,   656,   437,
     435,   682,   683,   259,   442,    89,    90,    91,    92,   331,
     342,   365,   363,   364,   376,   497,   369,   371,   378,   379,
     380,   381,   383,   384,   386,   497,   654,   389,   390,   463,
     400,   513,   401,   224,   416,   403,   396,   193,   425,   478,
     420,   479,   426,   224,   438,   432,   464,   482,   224,   259,
     452,   259,   450,   259,   470,   670,   259,   224,   495,   549,
     484,   485,   491,   492,   453,   454,   455,   684,   427,   546,
     456,   457,   458,   494,   500,   552,   518,   296,   296,   564,
     507,   511,   585,   556,   563,   567,   433,   577,   589,   592,
     439,   459,   595,   598,   601,   623,   631,   643,   664,   646,
     652,   651,   653,   434,   655,   659,   223,   661,   466,   718,
     259,   259,   666,   472,   669,   710,   259,   724,   259,   673,
     691,   692,   693,   699,   728,   705,   223,   558,   460,    67,
     561,    69,    70,    71,    72,    73,   706,   568,   714,   715,
     721,   725,   726,   719,   224,   224,   259,   732,   488,   259,
     727,   729,   733,   752,   493,   737,   224,   746,   747,   224,
     751,   753,   754,   755,   762,   764,   224,   766,   774,   224,
     765,   770,   777,   778,   781,   768,   782,   224,   783,   784,
     785,   788,   793,   497,    74,   642,   791,   796,   645,   797,
     798,   800,   296,   801,    13,   803,   804,   807,   805,   810,
     329,   259,   300,   565,   594,   527,    81,    82,   326,    83,
      84,    85,    86,    87,    88,   559,    89,    90,    91,    92,
     660,   259,   259,   665,   688,   306,   551,   252,   486,   576,
       0,     0,   630,   319,   633,     0,   296,     0,     0,     0,
     259,   259,   497,   676,     0,     0,   259,     0,   685,     0,
     687,   225,   259,     0,     0,     0,     0,     0,   808,     0,
       0,     0,   259,     0,     0,     0,     0,     0,   259,     0,
       0,   225,     0,     0,     0,     0,     0,     0,   497,     0,
       0,   709,     0,   224,     0,     0,     0,   224,     0,     0,
       0,     0,     0,     0,   259,     0,     0,     0,     0,     0,
     224,     0,     0,     0,     0,     0,     0,   259,   224,     0,
     224,     0,     0,     0,     0,     0,   224,     0,     0,   629,
       0,   632,   634,   635,   636,     0,   696,   697,   698,     0,
     702,   704,     0,   745,     0,     0,     0,     0,     0,     0,
     224,   650,     0,     0,   224,     0,     0,     0,     0,     0,
       0,   224,     0,   759,   761,     0,     0,     0,     0,     0,
      17,    18,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   771,   773,    19,    20,    21,     0,   776,     0,
      22,    23,    24,     0,   780,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   787,   749,     0,   750,     0,     0,
     792,    25,     0,     0,     0,     0,     0,     0,   757,     0,
       0,     0,   694,     0,     0,     0,     0,   701,     0,     0,
     224,     0,    26,     0,     0,     0,   802,     0,     0,     0,
       0,     0,     0,     0,     0,   720,     0,     0,    27,   809,
       0,     0,     0,     0,     0,     0,    28,    29,    30,     0,
       0,     0,     0,     0,   702,   704,     0,     0,     0,    31,
      32,    33,     0,     0,     0,     0,   224,     0,   224,    34,
     224,     0,     0,   224,     0,     0,     0,     0,    35,   465,
       0,   748,     0,    36,     0,   466,     0,     0,     0,    37,
      38,    17,    18,     0,     0,   756,   758,     0,     0,     0,
       0,     0,     0,     0,     0,    19,    20,    21,     0,     0,
       0,    22,    23,    24,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   224,   224,     0,
       0,     0,    25,   224,     0,   224,     0,     0,     0,     0,
       0,   789,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    26,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   224,     0,     0,   224,     0,     0,    27,
       0,     0,     0,     0,     0,     0,     0,    28,    29,    30,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      31,    32,    33,     0,     0,     0,     0,     0,     0,     0,
      34,     0,     0,     0,     0,     0,     0,     0,     0,    35,
     471,     0,     0,     0,    36,     0,   472,     0,   224,     0,
      37,    38,     0,     0,     0,     0,     0,     0,     0,    17,
      18,     0,    17,    18,     0,     0,     0,     0,   224,   224,
       0,     0,     0,    19,    20,    21,    19,    20,    21,    22,
      23,    24,    22,    23,    24,     0,     0,   224,   224,     0,
       0,     0,     0,   224,     0,   514,   515,     0,   224,   224,
      25,     0,     0,    25,     0,     0,     0,     0,     0,   224,
     734,   677,     0,     0,     0,   224,     0,     0,   224,     0,
       0,    26,     0,     0,    26,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    27,     0,     0,
      27,   224,     0,     0,     0,    28,    29,    30,    28,    29,
      30,     0,     0,     0,   224,     0,     0,     0,    31,    32,
      33,    31,    32,    33,     0,     0,     0,     0,    34,     0,
       0,    34,     0,     0,     0,     0,     0,    35,     0,     0,
      35,     0,    36,    17,    18,    36,    17,    18,    37,    38,
       0,    37,    38,     0,     0,     0,     0,    19,    20,    21,
      19,    20,    21,    22,    23,    24,    22,    23,    24,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    25,     0,     0,    25,     0,     0,
       0,   739,   677,     0,   741,   677,    17,    18,     0,     0,
       0,     0,     0,     0,     0,    26,     0,     0,    26,     0,
      19,    20,    21,     0,     0,     0,    22,    23,    24,     0,
       0,    27,     0,     0,    27,     0,     0,     0,     0,    28,
      29,    30,    28,    29,    30,     0,     0,    25,     0,     0,
       0,     0,    31,    32,    33,    31,    32,    33,     0,     0,
       0,     0,    34,     0,     0,    34,     0,     0,    26,     0,
       0,    35,     0,     0,    35,     0,    36,     0,     0,    36,
       0,     0,    37,    38,    27,    37,    38,     0,     0,     0,
       0,     0,    28,    29,    30,     0,     0,     0,    17,    18,
       0,     0,     0,     0,     0,    31,    32,    33,     0,     0,
       0,    61,    19,    20,    21,    34,     0,     0,    22,    23,
      24,     0,     0,     0,    35,     0,     0,     0,     0,    36,
       0,     0,    17,    18,     0,    37,    38,     0,     0,    25,
       0,     0,     0,     0,     0,     0,    19,    20,    21,     0,
       0,     0,    22,    23,    24,     0,     0,     0,     0,     0,
      26,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    25,     0,     0,    27,     0,     0,     0,
       0,     0,     0,     0,    28,    29,    30,     0,     0,     0,
       0,     0,     0,     0,    26,     0,     0,    31,    32,    33,
       0,     0,     0,     0,     0,     0,     0,    34,     0,     0,
      27,     0,     0,     0,     0,     0,    35,   489,    28,    29,
      30,    36,    17,    18,     0,     0,     0,    37,    38,     0,
       0,    31,    32,    33,     0,     0,    19,    20,    21,     0,
       0,    34,    22,    23,    24,     0,     0,     0,     0,   217,
      35,     0,     0,     0,     0,    36,    17,    18,     0,     0,
       0,    37,    38,    25,     0,     0,     0,     0,     0,     0,
      19,    20,    21,     0,     0,     0,    22,    23,    24,     0,
       0,     0,     0,     0,    26,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    25,     0,     0,
      27,     0,     0,     0,     0,   677,     0,     0,    28,    29,
      30,     0,     0,     0,     0,     0,     0,     0,    26,     0,
       0,    31,    32,    33,     0,     0,     0,     0,     0,     0,
       0,    34,     0,     0,    27,     0,     0,     0,     0,     0,
      35,     0,    28,    29,    30,    36,     0,   466,    17,    18,
       0,    37,    38,     0,     0,    31,    32,    33,     0,     0,
       0,     0,    19,    20,    21,    34,     0,     0,    22,    23,
      24,     0,     0,     0,    35,     0,     0,     0,     0,    36,
       0,     0,    17,    18,     0,    37,    38,     0,     0,    25,
       0,     0,     0,     0,     0,     0,    19,    20,    21,     0,
       0,     0,    22,    23,    24,     0,     0,     0,     0,     0,
      26,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    25,     0,     0,    27,     0,     0,     0,
       0,     0,     0,     0,    28,    29,    30,     0,     0,     0,
       0,     0,     0,     0,    26,     0,     0,    31,    32,    33,
       0,     0,     0,     0,     0,     0,     0,    34,     0,     0,
      27,     0,     0,     0,     0,     0,    35,   723,    28,    29,
      30,    36,     0,     0,     0,     0,     0,    37,    38,     0,
       0,    31,    32,    33,     0,     0,     0,     0,     0,     0,
     230,    34,   231,     0,     0,     0,   232,     0,     0,     0,
      35,     0,     0,     0,     0,    36,   233,     0,     0,     0,
       0,    37,    38,    67,    68,    69,    70,    71,    72,    73,
       0,   234,     0,   235,     0,     0,     0,     0,   236,   237,
       0,     0,     0,     0,   238,   239,   240,     0,     0,     0,
     241,     0,     0,     0,     0,   242,   243,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     244,     0,   245,   126,     0,     0,     0,     0,    74,     0,
       0,     0,     0,   246,   247,    75,    76,    77,   248,     0,
       0,     0,   249,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,   250,     0,     0,   512,
       0,     0,    36,     0,     0,     0,   230,   251,   231,   535,
     536,     0,   537,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   538,   539,   540,     0,     0,   230,     0,   231,
       0,     0,     0,   232,     0,     0,     0,   234,     0,   235,
       0,     0,     0,   233,   236,   237,     0,     0,     0,     0,
     238,   239,   240,     0,     0,     0,   241,     0,   234,   372,
     235,   242,   243,     0,     0,   236,   237,     0,     0,     0,
       0,   238,   239,   240,     0,     0,   244,   241,   245,   126,
       0,     0,   242,   243,     0,     0,     0,     0,     0,   246,
     247,     0,     0,     0,   248,     0,     0,   244,   249,   245,
     126,   230,     0,   231,     0,     0,     0,   232,     0,     0,
     246,   247,     0,     0,     0,   248,     0,   233,     0,   249,
       0,     0,   250,     0,   373,     0,     0,     0,    36,     0,
       0,     0,   234,   251,   235,     0,     0,     0,     0,   236,
     237,     0,     0,   250,     0,   238,   239,   240,     0,    36,
       0,   241,     0,     0,   251,     0,   242,   243,     0,   230,
       0,   231,     0,     0,     0,   232,     0,     0,     0,     0,
       0,   244,     0,   245,   126,   233,     0,     0,     0,     0,
       0,     0,     0,     0,   246,   247,     0,     0,     0,   248,
     234,   496,   235,   249,     0,     0,     0,   236,   237,     0,
       0,     0,     0,   238,   239,   240,     0,     0,     0,   241,
       0,     0,     0,     0,   242,   243,     0,   250,     0,     0,
     396,     0,     0,    36,   230,     0,   231,     0,   251,   244,
     232,   245,   126,     0,     0,     0,     0,     0,     0,     0,
     233,     0,   246,   247,     0,     0,     0,   248,     0,     0,
       0,   249,     0,     0,     0,   234,     0,   235,     0,     0,
       0,     0,   236,   237,     0,     0,     0,     0,   238,   239,
     240,     0,     0,     0,   241,   250,     0,     0,     0,   242,
     243,    36,   230,     0,   231,     0,   251,     0,   232,     0,
       0,     0,     0,     0,   244,   506,   245,   126,   233,     0,
       0,     0,     0,     0,     0,     0,     0,   246,   247,     0,
       0,     0,   248,   234,     0,   235,   249,     0,     0,     0,
     236,   237,     0,     0,     0,     0,   238,   239,   240,     0,
       0,     0,   241,     0,   639,     0,     0,   242,   243,     0,
     250,     0,     0,     0,     0,     0,    36,   230,     0,   231,
       0,   251,   244,   232,   245,   126,     0,     0,     0,     0,
       0,     0,     0,   233,     0,   246,   247,     0,     0,     0,
     248,     0,     0,     0,   249,     0,     0,     0,   234,   675,
     235,     0,     0,     0,     0,   236,   237,     0,     0,     0,
       0,   238,   239,   240,     0,     0,     0,   241,   250,     0,
       0,     0,   242,   243,    36,   230,     0,   231,     0,   251,
       0,   232,     0,     0,     0,     0,     0,   244,     0,   245,
     126,   233,     0,     0,     0,     0,     0,     0,     0,     0,
     246,   247,     0,     0,     0,   248,   234,     0,   235,   249,
       0,     0,     0,   236,   237,     0,     0,     0,     0,   238,
     239,   240,     0,     0,     0,   241,     0,   707,     0,     0,
     242,   243,     0,   250,     0,     0,     0,     0,     0,    36,
     230,     0,   231,     0,   251,   244,   232,   245,   126,     0,
       0,     0,     0,     0,     0,     0,   233,     0,   246,   247,
       0,     0,     0,   248,     0,     0,     0,   249,     0,     0,
       0,   234,     0,   235,     0,     0,     0,     0,   236,   237,
       0,     0,     0,     0,   238,   239,   240,     0,     0,     0,
     241,   250,     0,     0,     0,   242,   243,    36,   230,     0,
     231,     0,   251,     0,   232,     0,     0,     0,     0,     0,
     244,     0,   245,   126,   233,     0,     0,     0,     0,   230,
       0,   231,     0,   246,   247,   232,     0,     0,   248,   234,
       0,   235,   249,     0,     0,   233,   236,   237,     0,     0,
       0,     0,   238,   239,   240,     0,     0,     0,   241,     0,
     234,     0,   235,   242,   243,     0,   250,   236,   237,   772,
       0,     0,    36,   238,   239,   240,     0,   251,   244,   241,
     245,   126,     0,     0,   242,   243,     0,     0,     0,     0,
       0,   246,   247,     0,     0,     0,   248,     0,     0,   244,
     249,   245,   126,     0,     0,    67,    68,    69,    70,    71,
      72,    73,   246,   247,     0,     0,     0,   248,     0,     0,
       0,   249,     0,     0,   250,     0,     0,   775,     0,     0,
      36,     0,     0,     0,     0,   251,    67,    68,    69,    70,
      71,    72,    73,     0,     0,   250,     0,     0,     0,     0,
       0,    36,     0,     0,     0,     0,   251,   314,   315,     0,
      74,     0,     0,     0,     0,     0,     0,    75,    76,    77,
       0,     0,     0,     0,     0,     0,     0,     0,    78,   316,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,    74,    89,    90,    91,    92,     0,     0,    75,    76,
      77,    67,    68,    69,    70,    71,    72,    73,   317,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,   572,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    74,     0,     0,     0,
       0,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,    74,    89,    90,
      91,    92,     0,     0,    75,    76,    77,    67,    68,    69,
      70,    71,    72,    73,   573,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,     0,     0,     0,     0,     0,    67,    68,
      69,    70,    71,    72,    73,   574,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    74,     0,     0,     0,     0,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,     0,     0,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,    74,    89,    90,    91,    92,     0,     0,
      75,    76,    77,     0,     0,     0,    36,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,     0,     0,   107,   508,   108,   100,   101,
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
      91,    92,     0,     0,     0,     0,     0,   499,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,    67,    68,
      69,    70,    71,    72,    73,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,     0,   509,
       0,     0,     0,     0,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,    74,
       0,     0,     0,     0,   618,     0,    75,    76,    77,    67,
      68,    69,    70,    71,    72,    73,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,     0,     0,     0,     0,     0,
     620,     0,     0,     0,     0,    67,    68,    69,    70,    71,
      72,    73,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    74,     0,     0,     0,     0,     0,
       0,    75,    76,    77,     0,     0,     0,     0,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
      74,     0,     0,     0,     0,   671,     0,    75,    76,    77,
      67,    68,    69,    70,    71,    72,    73,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,     0,     0,     0,     0,
       0,   672,     0,     0,     0,     0,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    74,     0,     0,     0,     0,
       0,     0,    75,    76,    77,     0,     0,     0,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,    74,     0,     0,     0,     0,   674,     0,    75,    76,
      77,    67,    68,    69,    70,    71,    72,    73,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,     0,
       0,     0,   686,     0,     0,     0,     0,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    74,     0,     0,     0,
       0,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,    74,     0,     0,     0,     0,   689,     0,    75,
      76,    77,    67,    68,    69,    70,    71,    72,    73,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,     0,     0,
       0,     0,     0,   690,     0,     0,     0,     0,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    74,     0,     0,
       0,     0,     0,     0,    75,    76,    77,     0,     0,     0,
       0,     0,     0,     0,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,    74,     0,     0,     0,     0,   722,     0,
      75,    76,    77,    67,    68,    69,    70,    71,    72,    73,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,     0,   731,     0,     0,     0,     0,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,    74,     0,     0,     0,     0,   743,
       0,    75,    76,    77,     0,     0,     0,     0,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
       0,     0,     0,     0,   107,   763,   108,   100,   101,   102,
     109,   110,   111,   112,   113,   114,   115,     0,     0,     0,
     116,   117,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   118,     0,     0,     0,     0,     0,
       0,   119,     0,     0,     0,   120,   121,   122,     0,     0,
       0,     0,     0,   123,     0,   124,     0,   125,     0,     0,
       0,     0,     0,     0,     0,     2,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   126,     0,    69,
      70,    71,    72,    73,   127,     0,   128,     0,     0,     0,
       0,     0,     0,   129,   130,   131,     0,   132,   107,   133,
     108,   100,   101,   102,   109,   110,   111,   112,   113,   114,
     115,     0,     0,     0,   116,   117,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   118,   281,
       0,   282,    74,     0,     0,   119,     0,     0,     0,   120,
     121,   122,     0,     0,     0,     0,     0,   123,     0,     0,
       0,     0,     0,   283,     0,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,     0,     0,
       0,   126,    67,     0,    69,    70,    71,    72,    73,   428,
     284,     0,     0,     0,     0,     0,     0,   129,   130,     0,
       0,   132,   107,   133,   108,   100,   101,   102,   109,   110,
     111,   112,   113,   114,   115,     0,     0,     0,   116,   117,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   118,   281,   553,   282,     0,    74,     0,   119,
       0,     0,     0,   120,   121,   122,     0,     0,     0,     0,
       0,   123,     0,     0,     0,     0,     0,   283,     0,     0,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,     0,     0,   126,     0,     0,     0,     0,
       0,     0,     0,     0,   284,     0,     0,     0,     0,     0,
       0,   129,   130,     0,     0,   132,   107,   133,   108,   100,
     101,   102,   109,   110,   111,   112,   113,   114,   115,     0,
       0,     0,   116,   117,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   118,   281,   716,   282,
       0,     0,     0,   119,     0,     0,     0,   120,   121,   122,
       0,     0,     0,     0,     0,   123,     0,     0,     0,     0,
       0,   283,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   126,
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
      90,    91,    92,    74,     0,     0,     0,   571,     0,     0,
      75,    76,    77,    67,    68,    69,    70,    71,    72,    73,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,   603,     0,     0,     0,     0,     0,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,    74,     0,     0,     0,   604,     0,
       0,    75,    76,    77,    67,    68,    69,    70,    71,    72,
      73,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
       0,     0,     0,     0,   605,     0,     0,     0,     0,     0,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    74,
       0,     0,     0,     0,     0,     0,    75,    76,    77,     0,
       0,     0,     0,     0,     0,     0,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,    74,     0,     0,     0,   606,
       0,     0,    75,    76,    77,    67,    68,    69,    70,    71,
      72,    73,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,     0,     0,     0,     0,   608,     0,     0,     0,     0,
       0,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      74,     0,     0,     0,     0,     0,     0,    75,    76,    77,
       0,     0,     0,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,    74,     0,     0,     0,
     610,     0,     0,    75,    76,    77,    67,    68,    69,    70,
      71,    72,    73,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,     0,     0,     0,     0,   648,     0,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    74,     0,     0,     0,     0,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,     0,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,    74,     0,     0,
       0,   767,     0,     0,    75,    76,    77,    67,    68,    69,
      70,    71,    72,    73,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,     0,     0,     0,     0,   769,     0,     0,
       0,     0,     0,     0,     0,     0,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    74,     0,     0,     0,     0,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,     0,     0,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,   314,   315,
       0,    74,   812,     0,     0,     0,     0,     0,    75,    76,
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
      10,   108,   293,   383,    18,    45,   281,    43,   219,   307,
      47,   244,   414,     5,   401,     5,   418,     5,    28,    29,
      30,    31,    32,    33,    34,    35,    36,    37,    38,   541,
       5,     5,     5,     5,     5,     5,   548,    51,     5,    49,
     419,    16,    52,    34,     5,     5,   426,    42,   121,   122,
      21,    21,     3,     5,    21,     5,     5,    67,    68,    69,
      70,    71,    72,    73,    74,    75,    76,    77,    78,    79,
      80,    81,    82,    83,    84,    85,    86,    87,    88,    89,
      90,    91,    92,   470,     5,    13,    48,   127,     5,     5,
     477,     8,     9,    10,     5,   135,     5,    79,    47,    48,
      45,     4,     5,    45,   122,    45,   124,     4,     5,     4,
       5,     5,   219,   220,    45,    66,     5,   124,    45,     8,
       9,    10,    45,   130,   231,    45,    45,    45,   123,   641,
     125,   121,   122,   424,   123,   126,   125,   127,   130,   127,
     154,   122,   544,   125,   442,   102,   108,   121,   121,   130,
      45,    45,   162,   127,     5,   130,   118,   130,   130,   130,
     130,   123,   122,   130,   127,   123,   545,   130,   125,   130,
     132,   129,   208,     0,   123,    84,   122,   214,   130,    82,
     130,   191,   415,   193,   130,    82,     5,   398,   399,   122,
     135,   124,   265,   135,   267,   135,   269,   130,   678,   127,
     116,   713,   682,   683,   135,   592,   123,   116,   135,   130,
     121,   122,   135,   122,   122,   135,   135,   135,   123,   122,
     125,   129,   130,   122,   261,   122,   236,   117,    47,    48,
     129,   130,   744,    83,   125,     5,   246,   247,   124,   130,
     250,   281,   129,   130,   130,    18,     8,     9,   760,    11,
     124,   358,   123,   293,   125,   362,   130,   219,   220,    21,
      22,    23,   495,   122,   643,   124,   116,   117,   118,   231,
     129,   130,   234,   121,   786,   124,   383,   552,    51,   241,
     125,   130,   244,   128,    11,    12,    13,   678,   118,    16,
     252,   682,   683,   123,    12,    13,   122,   334,    16,   122,
     310,   311,   132,   340,   314,   315,   316,   127,   541,   126,
     320,   348,   322,   130,   693,   325,   126,   124,   125,   426,
     130,    94,   122,   122,   124,   124,   123,     4,   125,   366,
     344,   124,   125,   106,   407,   714,   123,   410,   125,   122,
     413,   124,   123,   123,   125,   125,   124,   125,   121,   122,
     126,   124,   123,   363,   125,     5,   647,   648,   130,    30,
      31,    32,     5,   743,   401,   123,   376,   125,    12,   379,
     380,   381,   124,   125,   384,   754,   149,   150,   414,   389,
     124,   154,   418,   763,   424,   395,   124,   125,   398,   399,
     123,     5,   125,   403,     6,   123,   358,   125,    99,   123,
     362,   125,    30,    31,    32,    33,    34,   123,    16,   125,
     420,   241,    83,   375,   123,   425,   125,   123,   123,   125,
     125,   383,   252,   385,   434,   123,   123,   125,   125,   391,
     123,    16,   125,   470,   123,    57,   125,    59,   211,   212,
     450,   112,   113,     5,   115,   116,   117,   118,   124,   125,
      30,    31,    32,   415,    57,    83,    59,   419,    57,   232,
      59,   124,   125,   149,   426,   123,   123,   125,   125,   124,
     125,   762,   125,   126,   484,   485,   124,   125,   124,   125,
       5,   491,   110,   111,   112,   113,     5,   115,   116,   117,
     118,   126,   265,     5,   267,   126,   269,   124,   508,   124,
     125,    16,   275,    83,   514,   515,   124,   125,   544,   519,
     126,   521,   552,   124,   125,   806,    61,   124,   125,    64,
      67,    68,    69,    70,    71,    72,    73,    74,   124,   125,
     303,   605,   606,   495,   307,   115,   116,   117,   118,     5,
       5,   124,   126,   125,   122,   375,   232,   233,     5,   122,
     122,   122,   122,   122,     5,   385,   566,   122,     5,   332,
     124,   391,   122,   108,     5,   126,   124,   130,   122,   342,
     126,   344,   122,   118,     5,   124,     5,   125,   123,   541,
       4,   543,   126,   545,   122,   595,   548,   132,     5,   419,
     126,   126,   126,   124,    18,    19,    20,   607,   284,     5,
      24,    25,    26,   124,   124,     5,   616,   647,   648,     5,
     124,   124,     5,   124,   124,   124,   302,   124,   124,   122,
     306,    45,   126,   124,   124,   124,    11,   124,   122,    59,
     128,   127,   124,   126,   124,   124,   743,   124,   129,   649,
     602,   603,   124,   129,   123,    57,   608,   657,   610,   124,
     124,   124,   124,   124,   664,   124,   763,   430,    82,    28,
     433,    30,    31,    32,    33,    34,   124,   440,   124,    59,
       5,     4,   124,   128,   219,   220,   638,    39,   364,   641,
     124,   124,   102,     5,   370,    52,   231,   124,   124,   234,
     124,   124,   124,    57,    39,     5,   241,   124,    52,   244,
     128,   124,    52,    52,    57,   131,   124,   252,     5,   124,
     124,   124,    59,   543,    83,   545,    57,   124,   548,     5,
     122,    57,   762,   124,     4,    57,   124,   124,    59,    57,
     208,   693,   135,   437,   482,   405,   105,   106,   197,   108,
     109,   110,   111,   112,   113,   431,   115,   116,   117,   118,
     581,   713,   714,   587,   616,   150,   422,   118,   362,   462,
      -1,    -1,   535,   162,   537,    -1,   806,    -1,    -1,    -1,
     732,   733,   602,   603,    -1,    -1,   738,    -1,   608,    -1,
     610,   743,   744,    -1,    -1,    -1,    -1,    -1,   798,    -1,
      -1,    -1,   754,    -1,    -1,    -1,    -1,    -1,   760,    -1,
      -1,   763,    -1,    -1,    -1,    -1,    -1,    -1,   638,    -1,
      -1,   641,    -1,   358,    -1,    -1,    -1,   362,    -1,    -1,
      -1,    -1,    -1,    -1,   786,    -1,    -1,    -1,    -1,    -1,
     375,    -1,    -1,    -1,    -1,    -1,    -1,   799,   383,    -1,
     385,    -1,    -1,    -1,    -1,    -1,   391,    -1,    -1,   535,
      -1,   537,   538,   539,   540,    -1,   629,   630,   631,    -1,
     633,   634,    -1,   693,    -1,    -1,    -1,    -1,    -1,    -1,
     415,   557,    -1,    -1,   419,    -1,    -1,    -1,    -1,    -1,
      -1,   426,    -1,   713,   714,    -1,    -1,    -1,    -1,    -1,
       4,     5,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   732,   733,    18,    19,    20,    -1,   738,    -1,
      24,    25,    26,    -1,   744,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   754,   698,    -1,   700,    -1,    -1,
     760,    45,    -1,    -1,    -1,    -1,    -1,    -1,   711,    -1,
      -1,    -1,   628,    -1,    -1,    -1,    -1,   633,    -1,    -1,
     495,    -1,    66,    -1,    -1,    -1,   786,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   651,    -1,    -1,    82,   799,
      -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,
      -1,    -1,    -1,    -1,   757,   758,    -1,    -1,    -1,   103,
     104,   105,    -1,    -1,    -1,    -1,   541,    -1,   543,   113,
     545,    -1,    -1,   548,    -1,    -1,    -1,    -1,   122,   123,
      -1,   697,    -1,   127,    -1,   129,    -1,    -1,    -1,   133,
     134,     4,     5,    -1,    -1,   711,   712,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    18,    19,    20,    -1,    -1,
      -1,    24,    25,    26,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   602,   603,    -1,
      -1,    -1,    45,   608,    -1,   610,    -1,    -1,    -1,    -1,
      -1,   757,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    66,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   638,    -1,    -1,   641,    -1,    -1,    82,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     103,   104,   105,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     113,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   122,
     123,    -1,    -1,    -1,   127,    -1,   129,    -1,   693,    -1,
     133,   134,    -1,    -1,    -1,    -1,    -1,    -1,    -1,     4,
       5,    -1,     4,     5,    -1,    -1,    -1,    -1,   713,   714,
      -1,    -1,    -1,    18,    19,    20,    18,    19,    20,    24,
      25,    26,    24,    25,    26,    -1,    -1,   732,   733,    -1,
      -1,    -1,    -1,   738,    -1,    40,    41,    -1,   743,   744,
      45,    -1,    -1,    45,    -1,    -1,    -1,    -1,    -1,   754,
      52,    53,    -1,    -1,    -1,   760,    -1,    -1,   763,    -1,
      -1,    66,    -1,    -1,    66,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    82,    -1,    -1,
      82,   786,    -1,    -1,    -1,    90,    91,    92,    90,    91,
      92,    -1,    -1,    -1,   799,    -1,    -1,    -1,   103,   104,
     105,   103,   104,   105,    -1,    -1,    -1,    -1,   113,    -1,
      -1,   113,    -1,    -1,    -1,    -1,    -1,   122,    -1,    -1,
     122,    -1,   127,     4,     5,   127,     4,     5,   133,   134,
      -1,   133,   134,    -1,    -1,    -1,    -1,    18,    19,    20,
      18,    19,    20,    24,    25,    26,    24,    25,    26,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    45,    -1,    -1,    45,    -1,    -1,
      -1,    52,    53,    -1,    52,    53,     4,     5,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    66,    -1,    -1,    66,    -1,
      18,    19,    20,    -1,    -1,    -1,    24,    25,    26,    -1,
      -1,    82,    -1,    -1,    82,    -1,    -1,    -1,    -1,    90,
      91,    92,    90,    91,    92,    -1,    -1,    45,    -1,    -1,
      -1,    -1,   103,   104,   105,   103,   104,   105,    -1,    -1,
      -1,    -1,   113,    -1,    -1,   113,    -1,    -1,    66,    -1,
      -1,   122,    -1,    -1,   122,    -1,   127,    -1,    -1,   127,
      -1,    -1,   133,   134,    82,   133,   134,    -1,    -1,    -1,
      -1,    -1,    90,    91,    92,    -1,    -1,    -1,     4,     5,
      -1,    -1,    -1,    -1,    -1,   103,   104,   105,    -1,    -1,
      -1,   109,    18,    19,    20,   113,    -1,    -1,    24,    25,
      26,    -1,    -1,    -1,   122,    -1,    -1,    -1,    -1,   127,
      -1,    -1,     4,     5,    -1,   133,   134,    -1,    -1,    45,
      -1,    -1,    -1,    -1,    -1,    -1,    18,    19,    20,    -1,
      -1,    -1,    24,    25,    26,    -1,    -1,    -1,    -1,    -1,
      66,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    45,    -1,    -1,    82,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    66,    -1,    -1,   103,   104,   105,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   113,    -1,    -1,
      82,    -1,    -1,    -1,    -1,    -1,   122,   123,    90,    91,
      92,   127,     4,     5,    -1,    -1,    -1,   133,   134,    -1,
      -1,   103,   104,   105,    -1,    -1,    18,    19,    20,    -1,
      -1,   113,    24,    25,    26,    -1,    -1,    -1,    -1,   121,
     122,    -1,    -1,    -1,    -1,   127,     4,     5,    -1,    -1,
      -1,   133,   134,    45,    -1,    -1,    -1,    -1,    -1,    -1,
      18,    19,    20,    -1,    -1,    -1,    24,    25,    26,    -1,
      -1,    -1,    -1,    -1,    66,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    45,    -1,    -1,
      82,    -1,    -1,    -1,    -1,    53,    -1,    -1,    90,    91,
      92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    66,    -1,
      -1,   103,   104,   105,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   113,    -1,    -1,    82,    -1,    -1,    -1,    -1,    -1,
     122,    -1,    90,    91,    92,   127,    -1,   129,     4,     5,
      -1,   133,   134,    -1,    -1,   103,   104,   105,    -1,    -1,
      -1,    -1,    18,    19,    20,   113,    -1,    -1,    24,    25,
      26,    -1,    -1,    -1,   122,    -1,    -1,    -1,    -1,   127,
      -1,    -1,     4,     5,    -1,   133,   134,    -1,    -1,    45,
      -1,    -1,    -1,    -1,    -1,    -1,    18,    19,    20,    -1,
      -1,    -1,    24,    25,    26,    -1,    -1,    -1,    -1,    -1,
      66,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    45,    -1,    -1,    82,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    66,    -1,    -1,   103,   104,   105,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   113,    -1,    -1,
      82,    -1,    -1,    -1,    -1,    -1,   122,   123,    90,    91,
      92,   127,    -1,    -1,    -1,    -1,    -1,   133,   134,    -1,
      -1,   103,   104,   105,    -1,    -1,    -1,    -1,    -1,    -1,
       5,   113,     7,    -1,    -1,    -1,    11,    -1,    -1,    -1,
     122,    -1,    -1,    -1,    -1,   127,    21,    -1,    -1,    -1,
      -1,   133,   134,    28,    29,    30,    31,    32,    33,    34,
      -1,    36,    -1,    38,    -1,    -1,    -1,    -1,    43,    44,
      -1,    -1,    -1,    -1,    49,    50,    51,    -1,    -1,    -1,
      55,    -1,    -1,    -1,    -1,    60,    61,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      75,    -1,    77,    78,    -1,    -1,    -1,    -1,    83,    -1,
      -1,    -1,    -1,    88,    89,    90,    91,    92,    93,    -1,
      -1,    -1,    97,    -1,    -1,    -1,   101,    -1,   103,   104,
     105,   106,    -1,   108,   109,   110,   111,   112,   113,    -1,
     115,   116,   117,   118,    -1,    -1,   121,    -1,    -1,   124,
      -1,    -1,   127,    -1,    -1,    -1,     5,   132,     7,     8,
       9,    -1,    11,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    21,    22,    23,    -1,    -1,     5,    -1,     7,
      -1,    -1,    -1,    11,    -1,    -1,    -1,    36,    -1,    38,
      -1,    -1,    -1,    21,    43,    44,    -1,    -1,    -1,    -1,
      49,    50,    51,    -1,    -1,    -1,    55,    -1,    36,    37,
      38,    60,    61,    -1,    -1,    43,    44,    -1,    -1,    -1,
      -1,    49,    50,    51,    -1,    -1,    75,    55,    77,    78,
      -1,    -1,    60,    61,    -1,    -1,    -1,    -1,    -1,    88,
      89,    -1,    -1,    -1,    93,    -1,    -1,    75,    97,    77,
      78,     5,    -1,     7,    -1,    -1,    -1,    11,    -1,    -1,
      88,    89,    -1,    -1,    -1,    93,    -1,    21,    -1,    97,
      -1,    -1,   121,    -1,   102,    -1,    -1,    -1,   127,    -1,
      -1,    -1,    36,   132,    38,    -1,    -1,    -1,    -1,    43,
      44,    -1,    -1,   121,    -1,    49,    50,    51,    -1,   127,
      -1,    55,    -1,    -1,   132,    -1,    60,    61,    -1,     5,
      -1,     7,    -1,    -1,    -1,    11,    -1,    -1,    -1,    -1,
      -1,    75,    -1,    77,    78,    21,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    88,    89,    -1,    -1,    -1,    93,
      36,    37,    38,    97,    -1,    -1,    -1,    43,    44,    -1,
      -1,    -1,    -1,    49,    50,    51,    -1,    -1,    -1,    55,
      -1,    -1,    -1,    -1,    60,    61,    -1,   121,    -1,    -1,
     124,    -1,    -1,   127,     5,    -1,     7,    -1,   132,    75,
      11,    77,    78,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      21,    -1,    88,    89,    -1,    -1,    -1,    93,    -1,    -1,
      -1,    97,    -1,    -1,    -1,    36,    -1,    38,    -1,    -1,
      -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,    50,
      51,    -1,    -1,    -1,    55,   121,    -1,    -1,    -1,    60,
      61,   127,     5,    -1,     7,    -1,   132,    -1,    11,    -1,
      -1,    -1,    -1,    -1,    75,    76,    77,    78,    21,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    88,    89,    -1,
      -1,    -1,    93,    36,    -1,    38,    97,    -1,    -1,    -1,
      43,    44,    -1,    -1,    -1,    -1,    49,    50,    51,    -1,
      -1,    -1,    55,    -1,    57,    -1,    -1,    60,    61,    -1,
     121,    -1,    -1,    -1,    -1,    -1,   127,     5,    -1,     7,
      -1,   132,    75,    11,    77,    78,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    21,    -1,    88,    89,    -1,    -1,    -1,
      93,    -1,    -1,    -1,    97,    -1,    -1,    -1,    36,    37,
      38,    -1,    -1,    -1,    -1,    43,    44,    -1,    -1,    -1,
      -1,    49,    50,    51,    -1,    -1,    -1,    55,   121,    -1,
      -1,    -1,    60,    61,   127,     5,    -1,     7,    -1,   132,
      -1,    11,    -1,    -1,    -1,    -1,    -1,    75,    -1,    77,
      78,    21,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      88,    89,    -1,    -1,    -1,    93,    36,    -1,    38,    97,
      -1,    -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,
      50,    51,    -1,    -1,    -1,    55,    -1,    57,    -1,    -1,
      60,    61,    -1,   121,    -1,    -1,    -1,    -1,    -1,   127,
       5,    -1,     7,    -1,   132,    75,    11,    77,    78,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    21,    -1,    88,    89,
      -1,    -1,    -1,    93,    -1,    -1,    -1,    97,    -1,    -1,
      -1,    36,    -1,    38,    -1,    -1,    -1,    -1,    43,    44,
      -1,    -1,    -1,    -1,    49,    50,    51,    -1,    -1,    -1,
      55,   121,    -1,    -1,    -1,    60,    61,   127,     5,    -1,
       7,    -1,   132,    -1,    11,    -1,    -1,    -1,    -1,    -1,
      75,    -1,    77,    78,    21,    -1,    -1,    -1,    -1,     5,
      -1,     7,    -1,    88,    89,    11,    -1,    -1,    93,    36,
      -1,    38,    97,    -1,    -1,    21,    43,    44,    -1,    -1,
      -1,    -1,    49,    50,    51,    -1,    -1,    -1,    55,    -1,
      36,    -1,    38,    60,    61,    -1,   121,    43,    44,   124,
      -1,    -1,   127,    49,    50,    51,    -1,   132,    75,    55,
      77,    78,    -1,    -1,    60,    61,    -1,    -1,    -1,    -1,
      -1,    88,    89,    -1,    -1,    -1,    93,    -1,    -1,    75,
      97,    77,    78,    -1,    -1,    28,    29,    30,    31,    32,
      33,    34,    88,    89,    -1,    -1,    -1,    93,    -1,    -1,
      -1,    97,    -1,    -1,   121,    -1,    -1,   124,    -1,    -1,
     127,    -1,    -1,    -1,    -1,   132,    28,    29,    30,    31,
      32,    33,    34,    -1,    -1,   121,    -1,    -1,    -1,    -1,
      -1,   127,    -1,    -1,    -1,    -1,   132,    80,    81,    -1,
      83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   101,   102,
     103,   104,   105,   106,    -1,   108,   109,   110,   111,   112,
     113,    83,   115,   116,   117,   118,    -1,    -1,    90,    91,
      92,    28,    29,    30,    31,    32,    33,    34,   131,   101,
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
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    78,    -1,    30,
      31,    32,    33,    34,    85,    -1,    87,    -1,    -1,    -1,
      -1,    -1,    -1,    94,    95,    96,    -1,    98,     5,   100,
       7,     8,     9,    10,    11,    12,    13,    14,    15,    16,
      17,    -1,    -1,    -1,    21,    22,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    35,    36,
      -1,    38,    83,    -1,    -1,    42,    -1,    -1,    -1,    46,
      47,    48,    -1,    -1,    -1,    -1,    -1,    54,    -1,    -1,
      -1,    -1,    -1,    60,    -1,   106,    -1,   108,   109,   110,
     111,   112,   113,    -1,   115,   116,   117,   118,    -1,    -1,
      -1,    78,    28,    -1,    30,    31,    32,    33,    34,    86,
      87,    -1,    -1,    -1,    -1,    -1,    -1,    94,    95,    -1,
      -1,    98,     5,   100,     7,     8,     9,    10,    11,    12,
      13,    14,    15,    16,    17,    -1,    -1,    -1,    21,    22,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    35,    36,    37,    38,    -1,    83,    -1,    42,
      -1,    -1,    -1,    46,    47,    48,    -1,    -1,    -1,    -1,
      -1,    54,    -1,    -1,    -1,    -1,    -1,    60,    -1,    -1,
     106,    -1,   108,   109,   110,   111,   112,   113,    -1,   115,
     116,   117,   118,    -1,    -1,    78,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    87,    -1,    -1,    -1,    -1,    -1,
      -1,    94,    95,    -1,    -1,    98,     5,   100,     7,     8,
       9,    10,    11,    12,    13,    14,    15,    16,    17,    -1,
      -1,    -1,    21,    22,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    35,    36,    37,    38,
      -1,    -1,    -1,    42,    -1,    -1,    -1,    46,    47,    48,
      -1,    -1,    -1,    -1,    -1,    54,    -1,    -1,    -1,    -1,
      -1,    60,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    78,
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
      82,   206,   126,   198,     5,   123,   129,   167,   168,   194,
     122,   123,   129,   170,   171,   194,   123,   122,   198,   198,
     199,   194,   125,   196,   126,   126,   190,   207,   197,   123,
     194,   126,   124,   197,   124,     5,    37,   182,   207,   124,
     124,   207,   207,   207,   189,   207,    76,   124,   126,   124,
     207,   124,   124,   182,    40,    41,   180,   181,   207,   169,
     207,   169,   207,   167,   194,   123,   207,   163,   124,   162,
     124,   162,   124,   162,   142,     8,     9,    11,    21,    22,
      23,   157,   158,   195,   122,   124,     5,   142,   157,   182,
     207,   184,     5,    37,   207,   189,   124,   127,   198,   197,
     124,   198,   207,   124,     5,   148,   126,   124,   198,   124,
     149,   123,   131,   131,   131,   207,   206,   124,     5,   116,
     123,   125,   123,   167,   194,     5,   123,   125,   123,   124,
     123,   167,   122,   123,   153,   126,   207,   207,   124,   123,
     207,   124,   195,   123,   123,   123,   123,   124,   123,   207,
     123,   207,   207,    42,   123,   125,   179,   207,   124,   207,
     124,   123,   123,   124,   124,   124,   124,   123,    21,   197,
     198,    11,   197,   198,   197,   197,   197,   158,   195,    57,
     142,   157,   182,   124,   123,   182,    59,   175,   123,   124,
     197,   127,   128,   124,   207,   124,   124,   122,   130,   124,
     168,   124,   123,   123,   122,   171,   124,   123,   167,   123,
     207,   124,   124,   124,   124,    37,   182,    53,   191,   192,
     193,   194,   191,   191,   207,   182,   124,   182,   181,   124,
     124,   124,   124,   124,   197,   124,   198,   198,   198,   124,
       5,   197,   198,   124,   198,   124,   124,    57,   123,   182,
      57,    11,    21,   157,   124,    59,    37,   176,   207,   128,
     197,     5,   124,   123,   207,     4,   124,   124,   207,   124,
     123,   124,    39,   102,    52,   192,   193,    52,   102,    52,
     193,    52,   193,   124,   157,   182,   124,   124,   197,   198,
     198,   124,     5,   124,   124,    57,   197,   198,   197,   182,
     157,   182,    39,   124,     5,   128,   124,   123,   131,   123,
     124,   182,   124,   182,    52,   124,   182,    52,    52,   189,
     182,    57,   124,     5,   124,   124,   157,   182,   124,   197,
     124,    57,   182,    59,   176,   189,   124,     5,   122,   123,
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
#line 3102 "y.tab.c"
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


#line 388 "yaccs/verilog.yacc"


