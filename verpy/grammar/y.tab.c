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
#define YYLAST   5114

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  135
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  75
/* YYNRULES -- Number of rules.  */
#define YYNRULES  362
/* YYNRULES -- Number of states.  */
#define YYNSTATES  804

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
     110,   126,   111,   101,   130,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,   131,     2,   132,   104,     2,     2,     2,     2,     2,
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
     474,   479,   485,   489,   493,   497,   499,   503,   505,   509,
     513,   515,   520,   525,   531,   535,   541,   548,   552,   558,
     565,   572,   579,   586,   592,   600,   609,   617,   625,   629,
     631,   634,   640,   645,   650,   653,   656,   659,   663,   665,
     671,   674,   679,   682,   685,   688,   693,   697,   700,   703,
     707,   711,   714,   716,   720,   726,   730,   732,   734,   736,
     738,   740,   742,   744,   746,   748,   750,   756,   764,   774,
     777,   780,   783,   788,   790,   792,   796,   798,   801,   804,
     806,   810,   813,   816,   822,   826,   831,   837,   842,   848,
     854,   862,   866,   870,   874,   879,   883,   889,   892,   896,
     900,   905,   911,   918,   926,   933,   940,   948,   955,   963,
     967,   971,   974,   976,   978,   980,   983,   985,   991,   995,
     999,  1001,  1005,  1007,  1011,  1021,  1027,  1033,  1037,  1039,
    1043,  1046,  1048,  1052,  1056,  1060,  1064,  1068,  1070,  1073,
    1075,  1077,  1080,  1084,  1088,  1091,  1093,  1095,  1099,  1101,
    1107,  1113,  1119,  1123,  1125,  1127,  1129,  1132,  1135,  1138,
    1141,  1144,  1147,  1151,  1154,  1157,  1159,  1161,  1163,  1165,
    1167,  1169,  1172,  1175,  1177,  1179,  1181,  1183,  1185,  1189,
    1193,  1195,  1198,  1200,  1203,  1207,  1211,  1216,  1221,  1228,
    1230,  1232,  1234,  1236,  1238,  1240,  1242,  1244,  1246,  1248,
    1250,  1252,  1254,  1256,  1258,  1263,  1265,  1267,  1269,  1271,
    1273,  1275,  1278,  1282,  1286,  1289,  1295,  1299,  1303,  1307,
    1311,  1315,  1319,  1323,  1327,  1331,  1335,  1339,  1343,  1347,
    1351,  1355,  1359,  1363,  1367,  1371,  1375,  1379,  1383,  1387,
    1391,  1395,  1400,  1404,  1406,  1409,  1412,  1415,  1418,  1421,
    1424,  1427,  1430
};

/* YYRHS -- A `-1'-separated list of the rules' RHS.  */
static const yytype_int16 yyrhs[] =
{
     136,     0,    -1,   137,    -1,   137,   138,    -1,   138,    -1,
     139,    -1,   146,    -1,     3,     5,   140,   141,   144,     6,
      -1,   121,   122,   166,   123,    -1,   121,   122,   123,    -1,
      -1,   124,    -1,   122,   142,   123,   124,    -1,   122,   123,
     124,    -1,   142,   125,   143,    -1,   143,    -1,   202,     5,
      -1,   202,   200,     5,    -1,   202,    21,     5,    -1,   202,
     200,     5,   200,    -1,   202,   200,   200,     5,    -1,     5,
      -1,   202,     5,   126,   208,    -1,   202,   200,     5,   126,
     208,    -1,   145,   144,    -1,    -1,   150,    -1,   151,    -1,
     168,    -1,   175,    -1,   176,    -1,   159,    -1,   160,    -1,
     161,    -1,   147,    -1,   155,    -1,   156,    -1,   146,    -1,
     187,    -1,    96,    -1,    66,    45,    -1,    66,     5,    -1,
      66,     5,   209,    -1,    66,     4,     5,   117,     4,     5,
      -1,    54,   184,    -1,     5,    -1,     5,   126,   209,    -1,
     149,   125,   148,    -1,   148,    -1,   202,   199,   124,    -1,
     202,   200,   199,   124,    -1,   202,   200,   199,   200,   124,
      -1,    17,   199,   124,    -1,   203,   149,   124,    -1,   203,
     200,   149,   124,    -1,   203,   200,   200,   149,   124,    -1,
     203,   200,     5,   200,   124,    -1,   203,     5,   200,   124,
      -1,   203,   174,   199,   124,    -1,   203,   174,     5,   126,
     209,   124,    -1,   100,    99,    13,   200,   127,   199,   128,
       5,   124,    -1,     7,   191,   124,    -1,     7,   171,   198,
     126,   209,   124,    -1,     7,   152,   171,   198,   126,   209,
     124,    -1,     7,   152,   198,   126,   209,   124,    -1,   122,
     153,   125,   153,   123,    -1,    67,    -1,    68,    -1,    69,
      -1,    70,    -1,    71,    -1,    72,    -1,    73,    -1,    74,
      -1,   200,    -1,    21,    -1,    56,     5,   124,   157,   197,
      57,    -1,    56,     5,   124,   197,    57,    -1,    56,   200,
     200,     5,   124,   157,   184,    57,    -1,    56,   154,     5,
     124,   157,   184,    57,    -1,    56,   154,     5,   124,   184,
      57,    -1,    56,     5,   122,   142,   123,   124,   184,    57,
      -1,    56,     5,   122,   142,   123,   124,   157,   184,    57,
      -1,    56,   154,     5,   122,   142,   123,   124,   184,    57,
      -1,    56,   154,     5,   122,   142,   123,   124,   157,   184,
      57,    -1,    58,     5,   124,   157,   184,    59,    -1,    58,
       5,   124,   184,    59,    -1,    58,     5,   122,   142,   123,
     124,   184,    59,    -1,    58,     5,   122,   142,   123,   124,
     157,   184,    59,    -1,   157,   158,    -1,   158,    -1,    11,
     199,   124,    -1,    22,   199,   124,    -1,    23,   199,   124,
      -1,    11,   200,   199,   124,    -1,    11,   200,     5,   200,
     124,    -1,    11,   200,   200,     5,   124,    -1,     9,    11,
     200,   200,     5,   124,    -1,     8,   199,   124,    -1,     8,
     199,   200,   124,    -1,     8,   200,   200,   199,   124,    -1,
       8,    21,   199,   124,    -1,    21,   199,   124,    -1,    21,
     199,   200,   124,    -1,    47,   164,   124,    -1,    47,    16,
     164,   124,    -1,    47,   200,   164,   124,    -1,    47,   200,
     200,   164,   124,    -1,    47,    16,   200,   164,   124,    -1,
      48,   164,   124,    -1,    48,   200,   164,   124,    -1,    48,
     200,   200,   164,   124,    -1,    46,   163,   124,    -1,   207,
     126,   209,    -1,   163,   125,   162,    -1,   162,    -1,   164,
     125,   165,    -1,   165,    -1,     5,   126,   209,    -1,   166,
     125,   167,    -1,   167,    -1,    48,     5,   126,   209,    -1,
      47,     5,   126,   209,    -1,    47,   200,     5,   126,   209,
      -1,     5,   126,   209,    -1,     5,     5,   122,   123,   124,
      -1,     5,   174,     5,   122,   123,   124,    -1,     5,     5,
     124,    -1,    42,   122,   196,   123,   124,    -1,    42,     5,
     122,   196,   123,   124,    -1,     5,     5,   122,   169,   123,
     124,    -1,    42,     5,   122,   169,   123,   124,    -1,     5,
       5,   122,   196,   123,   124,    -1,     5,   122,   196,   123,
     124,    -1,     5,   174,     5,   122,   169,   123,   124,    -1,
       5,   174,     5,   200,   122,   169,   123,   124,    -1,     5,
       5,   200,   122,   169,   123,   124,    -1,     5,     5,   200,
     122,   196,   123,   124,    -1,   169,   125,   170,    -1,   170,
      -1,   129,   116,    -1,   129,     5,   122,   209,   123,    -1,
     129,     5,   122,   123,    -1,   121,   122,   196,   123,    -1,
     121,     4,    -1,   121,     5,    -1,   121,    82,    -1,   172,
     125,   173,    -1,   173,    -1,   129,     5,   122,   209,   123,
      -1,   129,     5,    -1,   121,   122,   196,   123,    -1,   121,
       4,    -1,   121,    82,    -1,   121,     5,    -1,   121,   122,
     172,   123,    -1,   121,   122,   123,    -1,    98,   184,    -1,
      35,   184,    -1,    35,   180,   184,    -1,    85,   177,    86,
      -1,   177,   178,    -1,   178,    -1,    36,   177,    37,    -1,
      36,   102,     5,   177,    37,    -1,    87,   199,   124,    -1,
     150,    -1,   151,    -1,   159,    -1,   160,    -1,   161,    -1,
     168,    -1,   179,    -1,   175,    -1,   147,    -1,   187,    -1,
      38,   122,   209,   123,   178,    -1,    38,   122,   209,   123,
     178,    39,   178,    -1,    60,   122,   191,   124,   209,   124,
     191,   123,   178,    -1,   130,   116,    -1,   130,    84,    -1,
     130,     5,    -1,   130,   122,   182,   123,    -1,    42,    -1,
     125,    -1,   182,   181,   183,    -1,   183,    -1,    40,   209,
      -1,    41,   209,    -1,   209,    -1,    36,   197,    37,    -1,
      36,    37,    -1,    55,   184,    -1,    36,   102,     5,   197,
      37,    -1,    75,   197,    76,    -1,   198,   126,   209,   124,
      -1,   198,   126,   171,   209,   124,    -1,   198,    34,   209,
     124,    -1,   198,    34,   171,   209,   124,    -1,    38,   122,
     209,   123,   184,    -1,    38,   122,   209,   123,   184,    39,
     184,    -1,    43,   209,   124,    -1,    21,   199,   124,    -1,
      11,   199,   124,    -1,    11,   200,   199,   124,    -1,    89,
     209,   124,    -1,    88,   209,   126,   209,   124,    -1,   180,
     124,    -1,    44,     5,   124,    -1,    77,     5,   124,    -1,
       5,   122,   123,   124,    -1,     5,   122,   196,   123,   124,
      -1,    49,   122,   209,   123,   193,    52,    -1,    49,   122,
     209,   123,   193,   195,    52,    -1,    49,   122,   209,   123,
     195,    52,    -1,    50,   122,   209,   123,   193,    52,    -1,
      50,   122,   209,   123,   193,   195,    52,    -1,    51,   122,
     209,   123,   193,    52,    -1,    51,   122,   209,   123,   193,
     195,    52,    -1,   121,   209,   124,    -1,   121,   209,   184,
      -1,     5,   124,    -1,   188,    -1,   189,    -1,   190,    -1,
     207,   124,    -1,   187,    -1,     7,   198,   126,   209,   124,
      -1,    97,     5,   124,    -1,   185,   125,   186,    -1,   186,
      -1,     5,   126,   209,    -1,    45,    -1,    78,   185,    79,
      -1,    60,   122,   191,   124,   209,   124,   191,   123,   184,
      -1,    93,   122,   209,   123,   184,    -1,    61,   122,   209,
     123,   184,    -1,   191,   125,   192,    -1,   192,    -1,   198,
     126,   209,    -1,   193,   194,    -1,   194,    -1,   196,   102,
     184,    -1,   196,   102,   124,    -1,    53,   102,   184,    -1,
      53,   102,   124,    -1,   196,   125,   209,    -1,   209,    -1,
     197,   184,    -1,   184,    -1,     5,    -1,     5,   200,    -1,
       5,   201,   200,    -1,     5,   201,   201,    -1,     5,   201,
      -1,   207,    -1,   204,    -1,     5,   125,   199,    -1,     5,
      -1,   131,   209,   102,   209,   132,    -1,   131,   209,    80,
     209,   132,    -1,   131,   209,    81,   209,   132,    -1,   131,
     209,   132,    -1,     8,    -1,     9,    -1,    10,    -1,     9,
      11,    -1,     8,    12,    -1,     9,    12,    -1,    10,    12,
      -1,     8,    16,    -1,     9,    16,    -1,     9,    11,    16,
      -1,     9,    13,    -1,     8,    13,    -1,    13,    -1,    11,
      -1,    12,    -1,    16,    -1,    21,    -1,    22,    -1,    11,
      16,    -1,    12,    16,    -1,    87,    -1,    94,    -1,    95,
      -1,    14,    -1,    15,    -1,   127,   205,   128,    -1,   205,
     125,   206,    -1,   206,    -1,   209,   204,    -1,   209,    -1,
     109,   204,    -1,     5,   129,   207,    -1,     5,   129,     5,
      -1,     5,   129,     5,   200,    -1,     5,   129,     5,   201,
      -1,     5,   129,     5,   122,   209,   123,    -1,     4,    -1,
      82,    -1,    45,    -1,    18,    -1,    19,    -1,    20,    -1,
      24,    -1,    25,    -1,    26,    -1,     5,    -1,   207,    -1,
       4,    -1,    82,    -1,    45,    -1,    66,    -1,    66,   122,
     209,   123,    -1,    18,    -1,    19,    -1,    20,    -1,    24,
      -1,    25,    -1,    26,    -1,     5,   200,    -1,     5,   201,
     200,    -1,     5,   201,   201,    -1,     5,   201,    -1,   209,
     101,   209,   102,   209,    -1,   209,   112,   209,    -1,   209,
     116,   209,    -1,   209,   113,   209,    -1,   209,   117,   209,
      -1,   209,   118,   209,    -1,   209,   104,   209,    -1,   209,
     103,   209,    -1,   209,   105,   209,    -1,   209,   110,   209,
      -1,   209,   111,   209,    -1,   209,    83,   209,    -1,   209,
      28,   209,    -1,   209,    29,   209,    -1,   209,    90,   209,
      -1,   209,    91,   209,    -1,   209,    92,   209,    -1,   209,
      31,   209,    -1,   209,    30,   209,    -1,   209,    32,   209,
      -1,   209,   115,   209,    -1,   209,    33,   209,    -1,   209,
      34,   209,    -1,   209,   109,   209,    -1,   209,   108,   209,
      -1,   209,   106,   209,    -1,     5,   122,   196,   123,    -1,
     122,   209,   123,    -1,   204,    -1,   113,   209,    -1,   103,
     209,    -1,   105,   209,    -1,   104,   209,    -1,    90,   209,
      -1,    92,   209,    -1,    91,   209,    -1,   133,   209,    -1,
     134,   209,    -1
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
     154,   154,   155,   156,   157,   157,   159,   159,   160,   162,
     162,   164,   165,   166,   167,   171,   172,   173,   174,   175,
     176,   177,   178,   179,   180,   181,   182,   183,   191,   191,
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
  "'{'", "'}'", "'.'", "'@'", "'['", "']'", "'!'", "'~'", "$accept",
  "Main", "Mains", "MainItem", "Module", "Hparams", "Header",
  "Header_list", "Header_item", "Module_stuffs", "Mstuff", "Define",
  "Initial", "OneDef", "ManyDefs", "Definition", "Assign", "StrengthDef",
  "Strength", "WidthInt", "Function", "Task", "Mem_defs", "Mem_def",
  "Parameter", "Localparam", "Defparam", "DottedPair", "DottedPairs",
  "Pairs", "Pair", "head_params", "head_param", "Instance", "Conns_list",
  "Connection", "AssignParams", "Prms_list", "PrmAssign", "InstParams",
  "Always", "Generate", "GenStatements", "GenStatement",
  "GenFor_statement", "When", "Or_coma", "When_items", "When_item",
  "Statement", "pragma_stuffs", "pragma_item", "Pragma", "For_statement",
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
     345,   346,   347,   348,   349,   350,   351,   352,   353,   354,
     355,    63,    58,   124,    94,    38,   356,   357,   358,   359,
      60,    62,    43,    45,   360,   361,    42,    47,    37,   362,
     363,    35,    40,    41,    59,    44,    61,   123,   125,    46,
      64,    91,    93,    33,   126
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
     160,   160,   161,   162,   163,   163,   164,   164,   165,   166,
     166,   167,   167,   167,   167,   168,   168,   168,   168,   168,
     168,   168,   168,   168,   168,   168,   168,   168,   169,   169,
     170,   170,   170,   171,   171,   171,   171,   172,   172,   173,
     173,   174,   174,   174,   174,   174,   174,   175,   175,   175,
     176,   177,   177,   178,   178,   178,   178,   178,   178,   178,
     178,   178,   178,   178,   178,   178,   178,   178,   179,   180,
     180,   180,   180,   181,   181,   182,   182,   183,   183,   183,
     184,   184,   184,   184,   184,   184,   184,   184,   184,   184,
     184,   184,   184,   184,   184,   184,   184,   184,   184,   184,
     184,   184,   184,   184,   184,   184,   184,   184,   184,   184,
     184,   184,   184,   184,   184,   184,   184,   184,   184,   185,
     185,   186,   186,   187,   188,   189,   190,   191,   191,   192,
     193,   193,   194,   194,   195,   195,   196,   196,   197,   197,
     198,   198,   198,   198,   198,   198,   198,   199,   199,   200,
     200,   200,   201,   202,   202,   202,   202,   202,   202,   202,
     202,   202,   202,   202,   202,   203,   203,   203,   203,   203,
     203,   203,   203,   203,   203,   203,   203,   203,   204,   205,
     205,   206,   206,   206,   207,   207,   207,   207,   207,   208,
     208,   208,   208,   208,   208,   208,   208,   208,   209,   209,
     209,   209,   209,   209,   209,   209,   209,   209,   209,   209,
     209,   209,   209,   209,   209,   209,   209,   209,   209,   209,
     209,   209,   209,   209,   209,   209,   209,   209,   209,   209,
     209,   209,   209,   209,   209,   209,   209,   209,   209,   209,
     209,   209,   209,   209,   209,   209,   209,   209,   209,   209,
     209,   209,   209
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
       4,     5,     3,     3,     3,     1,     3,     1,     3,     3,
       1,     4,     4,     5,     3,     5,     6,     3,     5,     6,
       6,     6,     6,     5,     7,     8,     7,     7,     3,     1,
       2,     5,     4,     4,     2,     2,     2,     3,     1,     5,
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
       0,     0,     0,     0,     0,     0,     9,     0,   120,    21,
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
       0,     0,     0,   115,     0,     0,     0,     0,     0,   117,
       0,     0,     0,     0,    44,     0,    75,     0,    74,     0,
       0,   232,     0,   230,     0,     0,     0,   283,   174,   166,
     167,   168,   169,   170,   171,   173,     0,   162,   172,   175,
     157,     0,     7,    24,     0,     0,    45,    48,     0,     0,
       0,    43,   351,     0,     0,   296,   297,     0,     0,     0,
     262,   314,   289,     0,   124,     0,     0,     0,     0,   119,
     272,    12,    14,     0,    18,    17,     0,     0,   127,     0,
     152,   154,   153,     0,     0,     0,   251,   254,   144,   145,
     146,     0,    66,    67,    68,    69,    70,    71,    72,    73,
       0,     0,     0,     0,    61,     0,     0,     0,    52,     0,
     221,     0,     0,     0,     0,   191,     0,   249,     0,     0,
       0,     0,     0,     0,     0,   192,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   181,   180,   179,     0,   207,
     159,     0,     0,   225,     0,     0,   112,     0,     0,     0,
       0,     0,   104,     0,     0,     0,   109,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   233,     0,     0,     0,
       0,     0,     0,   160,   161,     0,    49,     0,     0,     0,
      53,     0,   258,     0,    45,     0,     0,   246,     0,     0,
       0,     0,   325,   122,     0,   121,   299,   302,   303,   304,
     305,   306,   307,   301,   300,    22,     0,    19,    20,     0,
       0,     0,   139,     0,     0,   156,     0,     0,   148,     0,
       0,     0,     0,   252,   253,     0,     0,     0,     0,     0,
     237,   239,   257,     0,     0,     0,   203,     0,   202,     0,
     190,   248,     0,   201,   208,     0,     0,     0,     0,     0,
     194,   209,     0,   205,     0,   228,   219,   220,     0,     0,
       0,   186,   189,     0,     0,     0,     0,     0,     0,     0,
     114,   113,   118,   105,     0,   116,   106,     0,   110,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    90,     0,
       0,     0,     0,     0,     0,     0,   231,   229,     0,   163,
       0,     0,   165,     0,    50,     0,    46,    57,    45,    47,
       0,    58,     0,    54,     0,   298,   260,   261,   259,   123,
      23,   125,     0,   140,     0,     0,     0,     0,     0,   150,
     155,     0,   151,   133,     0,     0,     0,   143,     0,     0,
       0,     0,   210,     0,     0,   204,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   187,   188,   183,   182,   184,
       0,     0,   197,     0,   195,     0,     0,   128,   108,   107,
     111,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    89,     0,    77,     0,     0,     0,     0,     0,     0,
      86,     0,     0,     0,     0,    51,     0,    56,    55,     0,
     130,   138,   132,     0,     0,     0,   147,   126,     0,     0,
      65,     0,    64,    62,   211,   227,   193,   199,     0,     0,
     241,     0,     0,     0,     0,     0,   236,   206,   235,   185,
     198,   196,   131,   129,     0,     0,    98,     0,     0,     0,
      91,   258,     0,     0,   102,     0,    92,    93,    76,     0,
       0,    80,     0,     0,     0,     0,    85,   164,   176,     0,
       0,    59,   142,     0,   136,   137,     0,   134,     0,    63,
       0,     0,   212,   240,     0,   214,     0,   215,     0,   217,
       0,     0,     0,     0,   101,    99,     0,     0,     0,    94,
       0,   103,     0,    79,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   141,   149,   135,   200,   245,   244,   213,
     243,   242,   216,   218,     0,     0,    81,   100,     0,    95,
      96,     0,     0,    91,     0,   102,    78,     0,    87,   177,
       0,     0,     0,    82,    97,     0,    83,    94,    88,     0,
      60,   234,    84,   178
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,     3,     4,     5,     6,    15,    45,   104,   105,   134,
     135,     7,   288,   307,   308,   289,   290,   219,   360,   277,
     140,   141,   547,   548,   291,   292,   293,   263,   264,   268,
     269,    97,    98,   294,   471,   472,   220,   477,   478,   215,
     295,   147,   296,   297,   298,   273,   620,   520,   521,   377,
     282,   283,   254,   255,   256,   257,   221,   222,   679,   680,
     681,   682,   378,   258,   229,   346,   347,   149,   150,    39,
      62,    63,    40,   465,   153
};

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
#define YYPACT_NINF -534
static const yytype_int16 yypact[] =
{
      42,   131,    79,    71,    42,  -534,  -534,  -534,    72,   167,
    1777,  -534,  -534,  -534,    60,   -52,   101,  -534,   -31,  -534,
    -534,  -534,  -534,  -534,  -534,  -534,   104,  -534,  1777,  1777,
    1777,  1777,  1777,  1777,  1777,  1777,  1401,  1777,  1777,  -534,
    -534,  4900,    47,    39,  -534,  3824,   228,  1777,   244,  1777,
    -534,   121,  1777,  -534,  -534,  -534,  -534,  -534,  -534,  -534,
    4198,   141,   -32,  -534,  2814,  -534,  -534,  1777,  1777,  1777,
    1777,  1777,  1777,  1777,  1777,  1777,  1777,  1777,  1777,  1777,
    1777,  1777,  1777,  1777,  1777,  1777,  1777,  1777,  1777,  1777,
    1777,  1777,  1777,   153,    24,   285,  -534,   117,  -534,  -534,
     253,   246,   290,   184,   157,  -534,    15,    64,    38,   332,
     346,  -534,  -534,  -534,  -534,   314,  -534,  -534,  2617,    25,
     354,    17,    26,  2617,    20,   368,    82,  4200,  -534,  -534,
    -534,  -534,  2617,   213,   310,  3824,  -534,  -534,  -534,  -534,
    -534,  -534,  -534,  -534,  -534,  -534,  -534,  -534,  -534,    30,
      23,   389,   182,  4900,    -6,  -534,   380,  -534,  -534,  4234,
    -534,  -534,  1401,  -534,  -534,  2868,  4996,   129,   129,   129,
     334,   334,  -534,  3969,  3969,  3969,  4835,  4931,  3969,  4063,
     514,   514,   514,   334,   334,   254,   254,   129,  -534,  -534,
    -534,  1777,   259,  1777,   430,   318,  -534,    62,  -534,  -534,
    -534,   432,  -534,  -534,  -534,  -534,  -534,   329,   266,   347,
     453,    32,    99,    46,  1777,   482,   191,    49,   284,    52,
      12,   -64,  -534,   378,  -534,  -534,  -534,  -534,   369,   382,
     -56,    12,    30,   314,  2029,   401,  1777,   506,   410,   413,
     414,  2617,   415,   416,  2617,   520,  1777,  1777,   417,   535,
    1777,    19,  2103,  -534,  -534,  -534,  -534,  -534,    -7,   395,
     420,  1777,   421,  -534,    80,   426,   427,    26,   171,  -534,
      26,   214,    26,   431,  -534,   205,  -534,   549,   425,   221,
     433,  -534,   -47,  -534,  3025,   435,   436,   314,  -534,  -534,
    -534,  -534,  -534,  -534,  -534,  -534,  3918,  -534,  -534,  -534,
    -534,   547,  -534,  -534,   437,   314,    91,  -534,   281,   559,
      33,  -534,  -534,  1777,  1777,  -534,  -534,  1777,  1777,  1777,
    -534,  -534,  -534,  1777,  4900,  1777,  4804,   439,  1777,  -534,
    -534,  -534,  -534,   209,  -534,   146,   561,   754,  -534,   445,
    -534,  -534,  -534,   980,   208,   -66,  -534,   121,  -534,  -534,
    -534,  1777,  -534,  -534,  -534,  -534,  -534,  -534,  -534,  -534,
     444,    12,   446,   447,  -534,    12,  1777,   314,  -534,  1493,
    -534,   448,   452,   314,   454,  -534,   566,  -534,  2161,  1777,
    3058,   456,  1777,  1777,  1777,  -534,    12,  1777,  2224,   457,
    2905,  3100,  1777,   458,  1884,  -534,  -534,  -534,   983,  -534,
    -534,  1527,  1527,  -534,  1617,   224,  -534,   354,  1777,  1777,
     291,   572,  -534,   572,   353,   572,  -534,   355,   572,   266,
    2008,   255,   578,   266,  2008,  1777,  -534,    82,   579,  4012,
    1777,    12,   461,  -534,  -534,   425,  -534,   -69,  1777,   463,
    -534,   583,    -8,   465,    91,   375,   583,  4900,  4299,  2651,
    2687,  2778,  4900,  4900,  1777,  4900,  -534,  -534,  -534,  -534,
    -534,  -534,  -534,  -534,  -534,  -534,   209,  -534,  -534,   466,
       6,   258,  -534,   267,  1617,  -534,   586,   268,  -534,   272,
     468,    11,   471,  -534,  -534,   275,   284,   470,  1777,  1777,
    -534,  4900,  -534,   475,   278,  1777,  -534,   479,  -534,  2617,
    -534,  -534,  4335,  -534,  -534,  4400,  4436,  4501,   377,  4537,
    -534,  -534,  1777,  -534,  4602,  -534,  -534,  -534,  1777,  1777,
      55,  -534,  4900,  1777,  3165,  1777,  3201,   279,   296,   480,
    -534,  4900,  4900,  -534,   390,  -534,  -534,   393,  -534,   397,
     299,    21,   597,    30,   314,   314,   314,  2008,  -534,  2282,
     266,  2008,   487,   300,  2008,   553,  4900,  -534,  4200,  -534,
    4638,   403,  -534,   467,  -534,   489,  4900,  -534,   488,  -534,
    1777,  -534,   491,  -534,   406,  -534,  -534,  -534,  -534,  4900,
    -534,  -534,   497,  -534,   498,   494,   504,   303,   307,   511,
    -534,   505,  -534,  -534,   513,   308,   494,  -534,   512,  1777,
    3266,  3302,  -534,   515,  3367,  -534,  2345,  2617,  1651,  1777,
    1777,  1777,  2617,  3403,  2617,  4900,  4900,  -534,  -534,  -534,
     983,  3468,  -534,  3504,  -534,   516,   517,  -534,  -534,  -534,
    -534,   518,   314,   107,   425,   425,   519,    35,   112,   521,
     522,  -534,  2403,  -534,   311,  2008,   581,   302,   523,   585,
    -534,  4106,  4200,  1777,   314,  -534,  3569,  -534,  -534,  1743,
    -534,  -534,  -534,   524,   525,  1777,  -534,  -534,   527,   331,
    -534,  3605,  -534,  -534,  -534,  -534,  -534,   614,   557,  1129,
    -534,   603,   -39,  1241,  1347,  3670,  -534,  -534,  -534,  -534,
    -534,  -534,  -534,  -534,  2008,   536,  -534,   537,   314,   425,
     400,    89,   538,   659,   405,   542,  -534,  -534,  -534,   543,
     611,  -534,    30,   314,  2008,  2008,  -534,  -534,   630,  3706,
     544,  -534,  -534,  4703,  -534,  -534,  4739,  -534,   550,  -534,
    2617,  2466,  -534,  -534,   621,  -534,  2524,  -534,   623,  -534,
     624,    12,  2008,   620,  -534,  -534,   554,   674,   556,   408,
     564,  -534,  2008,  -534,   565,    35,   113,   626,  2008,   622,
    4200,    12,   680,  -534,  -534,  -534,  -534,  -534,  -534,  -534,
    -534,  -534,  -534,  -534,   343,   633,  -534,  -534,   567,  -534,
    -534,  2008,   637,  -534,   575,  -534,  -534,   641,  -534,  -534,
     351,   577,  2617,  -534,  -534,   646,  -534,  -534,  -534,  4200,
    -534,  -534,  -534,  -534
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -534,  -534,  -534,   701,  -534,  -534,  -534,  -400,   499,   576,
    -534,    14,    54,   269,  -303,    56,    57,  -534,   226,  -534,
    -534,  -534,  -406,  -533,    61,    66,    68,   306,  -534,  -114,
     305,  -534,   526,    75,  -389,   134,  -203,  -534,   125,   570,
      76,  -534,  -275,  -291,  -534,   604,  -534,  -534,   105,    51,
    -534,   294,   -45,  -534,  -534,  -534,  -373,   359,  -529,  -385,
    -343,   -37,  -232,  -105,  -103,   -17,   -12,   -41,  -534,   155,
    -534,   568,   -44,   260,   889
};

/* YYTABLE[YYPACT[STATE-NUM]].  What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule which
   number is the opposite.  If zero, do what YYDEFACT says.
   If YYTABLE_NINF, syntax error.  */
#define YYTABLE_NINF -205
static const yytype_int16 yytable[] =
{
     148,    50,   106,   223,   155,   434,    51,   445,   271,   429,
     152,   582,   388,   508,   641,   527,   361,   216,   554,   540,
     209,   641,   266,   553,   395,   275,   228,   401,   306,   192,
     260,   266,   426,   267,   157,   228,   210,   335,   444,   158,
     701,   276,   632,   216,    99,     1,   304,   100,   101,   102,
     340,   341,    93,   348,   349,   564,   481,   216,   561,   136,
     364,   365,   193,   736,   225,   193,   369,    93,   370,   212,
      43,    12,    44,    48,   259,    49,   265,   194,   427,   259,
     683,   684,   299,     9,    10,   587,   313,   280,   259,   211,
     148,    47,   595,   162,    94,    95,   163,   617,    48,   137,
      49,   138,   139,   396,   270,   272,   142,   278,     2,    94,
      95,   143,   641,   144,   362,   363,   314,   367,   570,   402,
     145,   146,   583,    48,    11,    49,   371,   281,   342,   372,
     374,   350,   305,   310,   594,   397,     8,   315,   434,    36,
     470,   398,   316,   574,   213,   645,   193,   261,   193,   136,
     644,   193,   193,   410,   193,   193,   414,   193,   417,   217,
     218,   193,   103,   193,   193,    36,   193,   106,   343,   253,
      96,   351,    16,   217,   274,   225,   225,   344,   618,    36,
     619,   641,    42,   300,   432,   213,   214,   225,   549,   137,
     259,   138,   139,    14,   336,   339,   142,   259,   523,   525,
     259,   143,   437,   144,   406,   407,   443,   669,   259,   641,
     145,   146,    74,   456,   367,   373,   161,   438,    46,   164,
     193,   337,   193,   338,   405,   641,    52,   457,   458,   459,
     193,   696,   151,   460,   461,   462,   704,   785,   193,   299,
     196,   714,   197,   193,   193,    90,    91,    92,   641,   154,
     411,   299,    49,   415,   463,   418,   487,   201,   202,   203,
     223,   422,   204,   224,   492,   198,   199,   606,    36,   200,
     497,    99,   466,   224,   100,   101,   102,   193,   224,   191,
     207,   223,   208,   651,    69,    70,    71,   224,   742,   439,
     195,   464,   385,   446,   733,   412,   413,   534,   733,   733,
     473,   537,   205,   400,   539,   312,   479,   313,   206,   758,
     541,   542,   301,   712,   485,   642,   302,   225,   467,   228,
      48,   225,    49,   713,   545,   546,   223,   419,   482,   420,
     483,   480,   494,   313,   259,   484,   734,    74,   416,   413,
     738,   740,   225,   423,   259,   424,   781,   529,   226,   313,
     259,   352,   353,   354,   355,   356,   357,   358,   359,   262,
     434,   718,   227,   265,    69,    70,    71,   528,   774,    89,
      90,    91,    92,   279,   224,   224,   259,   550,   106,   551,
     259,   584,   106,   585,   299,   325,   224,   225,   790,   224,
     586,   590,   313,   591,   311,   592,   224,   313,   597,   224,
     313,   603,   625,   313,   585,   440,   441,   224,    67,    68,
      69,    70,    71,    72,    73,   533,   413,    74,   563,   626,
     565,   313,   631,   648,   208,   208,   663,   572,   585,   501,
     664,   668,   313,   585,   709,   327,   208,   588,   633,   501,
     636,   638,   639,   640,   328,   517,    87,    88,   330,    89,
      90,    91,    92,   331,   728,   259,   585,  -203,   334,  -203,
     317,   318,  -202,    74,  -202,  -204,   792,  -204,   365,   789,
      75,    76,    77,   333,   799,   555,   365,   536,   413,   538,
     413,    78,   319,    79,    80,    81,    82,   345,    83,    84,
      85,    86,    87,    88,   367,    89,    90,    91,    92,   573,
     441,   611,   365,   259,   366,   259,   368,   259,   803,   106,
     259,   381,   320,   299,   628,   413,   224,   629,   413,   403,
     224,   630,   413,   379,   634,   389,   637,   653,   365,   695,
     658,   441,   382,   224,   702,   383,   384,   386,   387,   392,
     393,   224,   404,   224,    69,    70,    71,    72,    73,   224,
      48,   720,   408,   409,   421,   399,   193,   430,   431,   425,
     435,   436,   259,   259,   442,   454,   468,   474,   259,   486,
     259,   499,   488,   489,   495,   224,   496,   266,   498,   224,
     504,   511,   515,   552,   558,   562,   224,   567,   568,   571,
     581,   589,   593,   596,   654,   746,   599,    74,   259,   602,
     501,   259,   646,   605,   627,   649,   299,   299,   635,   754,
     756,   647,   650,   655,   438,   657,   697,   698,   699,   659,
     703,   705,   660,   470,    85,    86,    87,    88,   662,    89,
      90,    91,    92,   665,   476,   670,   223,   667,   711,   674,
     692,   693,   694,   700,   716,   706,   707,   715,   724,   725,
     259,   727,   784,   730,   224,   735,   223,   501,   677,   731,
     744,   745,   749,   686,   750,   688,   751,   752,   753,   760,
     259,   259,   762,   769,   765,   772,   773,   776,   777,   778,
     779,   788,   747,   786,   748,   791,   259,   259,   780,   783,
     793,   794,   259,   501,   796,   755,   710,   225,   259,   797,
     798,   800,   224,   802,   224,    13,   224,   332,   259,   224,
     569,   303,   598,   530,   259,   299,   666,   225,   535,   661,
     309,   557,   252,   329,   490,   689,   580,     0,     0,     0,
     322,     0,     0,     0,     0,     0,     0,   259,   703,   705,
       0,     0,     0,     0,     0,   743,     0,     0,   259,     0,
       0,     0,     0,     0,   299,     0,     0,     0,    17,    18,
       0,   224,   224,     0,     0,   757,   759,   224,     0,   224,
       0,     0,    19,    20,    21,     0,     0,     0,    22,    23,
      24,   766,   768,     0,     0,     0,     0,   771,     0,     0,
       0,     0,     0,   775,     0,     0,     0,   224,     0,    25,
     224,     0,     0,   782,     0,     0,     0,     0,     0,   787,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      26,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   795,     0,     0,     0,    27,     0,     0,     0,
       0,     0,     0,   801,    28,    29,    30,     0,     0,   224,
       0,     0,     0,     0,     0,     0,     0,    31,    32,    33,
       0,     0,     0,     0,     0,     0,     0,    34,     0,   224,
     224,     0,     0,     0,     0,     0,    35,   469,     0,     0,
       0,    36,     0,   470,     0,   224,   224,    37,    38,     0,
       0,   224,     0,     0,     0,     0,   224,   224,     0,    41,
       0,     0,     0,     0,     0,     0,     0,   224,     0,     0,
       0,     0,     0,   224,     0,     0,   224,    53,    54,    55,
      56,    57,    58,    59,    60,    64,    65,    66,     0,     0,
       0,     0,     0,     0,     0,     0,   224,     0,   156,     0,
       0,   159,     0,     0,     0,     0,     0,   224,     0,     0,
       0,     0,     0,     0,     0,     0,   165,   166,   167,   168,
     169,   170,   171,   172,   173,   174,   175,   176,   177,   178,
     179,   180,   181,   182,   183,   184,   185,   186,   187,   188,
     189,   190,     0,     0,    17,    18,     0,    17,    18,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    19,    20,
      21,    19,    20,    21,    22,    23,    24,    22,    23,    24,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   518,   519,    25,     0,     0,    25,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    26,     0,     0,    26,
       0,    64,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    27,     0,     0,    27,     0,     0,     0,     0,
      28,    29,    30,    28,    29,    30,     0,     0,     0,     0,
     324,     0,   326,    31,    32,    33,    31,    32,    33,     0,
       0,     0,     0,    34,     0,     0,    34,     0,     0,     0,
       0,     0,    35,   475,     0,    35,     0,    36,     0,   476,
      36,     0,     0,    37,    38,     0,    37,    38,     0,     0,
       0,     0,     0,     0,     0,   380,     0,     0,     0,     0,
       0,     0,     0,    17,    18,   390,   391,     0,     0,   394,
       0,     0,     0,     0,     0,     0,     0,    19,    20,    21,
       0,     0,     0,    22,    23,    24,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    25,     0,     0,     0,     0,     0,
       0,   732,   678,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    26,     0,     0,     0,     0,
       0,     0,   447,   448,     0,     0,   449,   450,   451,     0,
       0,    27,   452,     0,   453,     0,     0,   455,     0,    28,
      29,    30,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    31,    32,    33,     0,     0,     0,     0,     0,
       0,     0,    34,     0,     0,    17,    18,     0,     0,     0,
       0,    35,     0,     0,     0,   491,    36,     0,     0,    19,
      20,    21,    37,    38,     0,    22,    23,    24,   502,     0,
       0,   505,   506,   507,     0,     0,   509,     0,     0,     0,
       0,   514,     0,     0,     0,     0,    25,   522,     0,     0,
     524,   526,     0,   737,   678,     0,     0,   531,   532,     0,
       0,     0,     0,     0,     0,     0,     0,    26,     0,     0,
       0,     0,     0,     0,   556,     0,     0,     0,     0,   560,
       0,     0,     0,    27,     0,     0,     0,   566,     0,     0,
       0,    28,    29,    30,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   579,    31,    32,    33,     0,     0,     0,
       0,    17,    18,     0,    34,     0,     0,     0,     0,     0,
       0,     0,     0,    35,     0,    19,    20,    21,    36,     0,
       0,    22,    23,    24,    37,    38,     0,   600,   601,     0,
       0,     0,     0,     0,   604,     0,     0,     0,     0,     0,
       0,     0,    25,     0,     0,     0,     0,     0,     0,   739,
     678,   613,     0,     0,     0,    17,    18,   615,   616,     0,
       0,     0,   621,    26,   623,     0,     0,     0,     0,    19,
      20,    21,     0,     0,     0,    22,    23,    24,     0,    27,
       0,     0,     0,     0,     0,     0,     0,    28,    29,    30,
       0,     0,     0,     0,     0,     0,    25,     0,     0,     0,
      31,    32,    33,     0,     0,     0,     0,     0,     0,   656,
      34,     0,     0,     0,     0,     0,     0,    26,     0,    35,
       0,     0,     0,     0,    36,     0,     0,     0,     0,     0,
      37,    38,     0,    27,     0,     0,     0,     0,   671,     0,
       0,    28,    29,    30,     0,     0,     0,    17,    18,     0,
     685,     0,     0,     0,    31,    32,    33,     0,     0,   522,
      61,    19,    20,    21,    34,     0,     0,    22,    23,    24,
       0,     0,     0,    35,     0,     0,     0,     0,    36,     0,
       0,    17,    18,     0,    37,    38,     0,     0,    25,     0,
       0,     0,   719,     0,     0,    19,    20,    21,   723,     0,
       0,    22,    23,    24,   726,     0,     0,     0,     0,    26,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    25,     0,     0,    27,     0,     0,     0,     0,
       0,     0,     0,    28,    29,    30,     0,     0,     0,     0,
       0,     0,     0,    26,     0,     0,    31,    32,    33,     0,
       0,     0,     0,     0,     0,     0,    34,     0,     0,    27,
       0,     0,     0,     0,     0,    35,   493,    28,    29,    30,
      36,    17,    18,     0,     0,     0,    37,    38,     0,     0,
      31,    32,    33,     0,     0,    19,    20,    21,     0,     0,
      34,    22,    23,    24,     0,     0,     0,     0,   217,    35,
       0,     0,     0,     0,    36,    17,    18,     0,     0,     0,
      37,    38,    25,     0,     0,     0,     0,     0,     0,    19,
      20,    21,     0,     0,     0,    22,    23,    24,     0,     0,
       0,     0,     0,    26,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    25,     0,     0,    27,
       0,     0,     0,     0,   678,     0,     0,    28,    29,    30,
       0,     0,     0,     0,     0,     0,     0,    26,     0,     0,
      31,    32,    33,     0,     0,     0,     0,     0,     0,     0,
      34,     0,     0,    27,     0,     0,     0,     0,     0,    35,
       0,    28,    29,    30,    36,     0,   470,    17,    18,     0,
      37,    38,     0,     0,    31,    32,    33,     0,     0,     0,
       0,    19,    20,    21,    34,     0,     0,    22,    23,    24,
       0,     0,     0,    35,     0,     0,     0,     0,    36,     0,
       0,    17,    18,     0,    37,    38,     0,     0,    25,     0,
       0,     0,     0,     0,     0,    19,    20,    21,     0,     0,
       0,    22,    23,    24,     0,     0,     0,     0,     0,    26,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    25,     0,     0,    27,     0,     0,     0,     0,
       0,     0,     0,    28,    29,    30,     0,     0,     0,     0,
       0,     0,     0,    26,     0,     0,    31,    32,    33,     0,
       0,     0,     0,     0,     0,     0,    34,     0,     0,    27,
       0,     0,     0,     0,     0,    35,   722,    28,    29,    30,
      36,     0,     0,     0,     0,     0,    37,    38,     0,     0,
      31,    32,    33,     0,     0,     0,     0,     0,     0,   230,
      34,   231,     0,     0,     0,   232,     0,     0,     0,    35,
       0,     0,     0,     0,    36,   233,     0,     0,     0,     0,
      37,    38,    67,    68,    69,    70,    71,    72,    73,     0,
     234,     0,   235,     0,     0,     0,     0,   236,   237,     0,
       0,     0,     0,   238,   239,   240,     0,     0,     0,   241,
       0,     0,     0,     0,   242,   243,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   244,
       0,   245,   126,     0,     0,     0,     0,    74,     0,     0,
       0,     0,   246,   247,    75,    76,    77,   248,     0,     0,
       0,   249,     0,     0,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,     0,     0,   250,     0,     0,   516,     0,
       0,    36,     0,   230,   251,   231,   541,   542,     0,   543,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   544,
     545,   546,     0,     0,   230,     0,   231,     0,     0,     0,
     232,     0,     0,     0,   234,     0,   235,     0,     0,     0,
     233,   236,   237,     0,     0,     0,     0,   238,   239,   240,
       0,     0,     0,   241,     0,   234,   375,   235,   242,   243,
       0,     0,   236,   237,     0,     0,     0,     0,   238,   239,
     240,     0,     0,   244,   241,   245,   126,     0,     0,   242,
     243,     0,     0,     0,     0,     0,   246,   247,     0,     0,
       0,   248,     0,     0,   244,   249,   245,   126,   230,     0,
     231,     0,     0,     0,   232,     0,     0,   246,   247,     0,
       0,     0,   248,     0,   233,     0,   249,     0,     0,   250,
       0,   376,     0,     0,     0,    36,     0,     0,   251,   234,
       0,   235,     0,     0,     0,     0,   236,   237,     0,     0,
     250,     0,   238,   239,   240,     0,    36,     0,   241,   251,
       0,     0,     0,   242,   243,     0,   230,     0,   231,     0,
       0,     0,   232,     0,     0,     0,     0,     0,   244,     0,
     245,   126,   233,     0,     0,     0,     0,     0,     0,     0,
       0,   246,   247,     0,     0,     0,   248,   234,   500,   235,
     249,     0,     0,     0,   236,   237,     0,     0,     0,     0,
     238,   239,   240,     0,     0,     0,   241,     0,     0,     0,
       0,   242,   243,     0,   250,     0,     0,   399,     0,   230,
      36,   231,     0,   251,     0,   232,   244,     0,   245,   126,
       0,     0,     0,     0,     0,   233,     0,     0,     0,   246,
     247,     0,     0,     0,   248,     0,     0,     0,   249,     0,
     234,     0,   235,     0,     0,     0,     0,   236,   237,     0,
       0,     0,     0,   238,   239,   240,     0,     0,     0,   241,
       0,     0,   250,     0,   242,   243,     0,   230,    36,   231,
       0,   251,     0,   232,     0,     0,     0,     0,     0,   244,
     510,   245,   126,   233,     0,     0,     0,     0,     0,     0,
       0,     0,   246,   247,     0,     0,     0,   248,   234,     0,
     235,   249,     0,     0,     0,   236,   237,     0,     0,     0,
       0,   238,   239,   240,     0,     0,     0,   241,     0,   643,
       0,     0,   242,   243,     0,   250,     0,     0,     0,     0,
     230,    36,   231,     0,   251,     0,   232,   244,     0,   245,
     126,     0,     0,     0,     0,     0,   233,     0,     0,     0,
     246,   247,     0,     0,     0,   248,     0,     0,     0,   249,
       0,   234,   676,   235,     0,     0,     0,     0,   236,   237,
       0,     0,     0,     0,   238,   239,   240,     0,     0,     0,
     241,     0,     0,   250,     0,   242,   243,     0,   230,    36,
     231,     0,   251,     0,   232,     0,     0,     0,     0,     0,
     244,     0,   245,   126,   233,     0,     0,     0,     0,     0,
       0,     0,     0,   246,   247,     0,     0,     0,   248,   234,
       0,   235,   249,     0,     0,     0,   236,   237,     0,     0,
       0,     0,   238,   239,   240,     0,     0,     0,   241,     0,
     708,     0,     0,   242,   243,     0,   250,     0,     0,     0,
       0,   230,    36,   231,     0,   251,     0,   232,   244,     0,
     245,   126,     0,     0,     0,     0,     0,   233,     0,     0,
       0,   246,   247,     0,     0,     0,   248,     0,     0,     0,
     249,     0,   234,     0,   235,     0,     0,     0,     0,   236,
     237,     0,     0,     0,     0,   238,   239,   240,     0,     0,
       0,   241,     0,     0,   250,     0,   242,   243,     0,   230,
      36,   231,     0,   251,     0,   232,     0,     0,     0,     0,
       0,   244,     0,   245,   126,   233,     0,     0,     0,     0,
       0,     0,     0,     0,   246,   247,     0,     0,     0,   248,
     234,     0,   235,   249,     0,     0,     0,   236,   237,     0,
       0,     0,     0,   238,   239,   240,     0,     0,     0,   241,
       0,     0,     0,     0,   242,   243,     0,   250,     0,     0,
     767,     0,     0,    36,     0,     0,   251,     0,     0,   244,
       0,   245,   126,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   246,   247,     0,     0,     0,   248,     0,     0,
       0,   249,   230,     0,   231,     0,     0,     0,   232,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   233,     0,
       0,     0,     0,     0,     0,   250,     0,     0,   770,     0,
       0,    36,     0,   234,   251,   235,     0,     0,     0,     0,
     236,   237,     0,     0,     0,     0,   238,   239,   240,     0,
       0,     0,   241,     0,     0,     0,     0,   242,   243,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,   244,     0,   245,   126,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   246,   247,     0,     0,     0,
     248,     0,     0,     0,   249,    67,    68,    69,    70,    71,
      72,    73,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    74,     0,     0,     0,   250,     0,
       0,    75,    76,    77,    36,     0,     0,   251,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
      74,     0,     0,     0,     0,     0,     0,    75,    76,    77,
       0,     0,     0,   576,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,   577,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    74,     0,     0,     0,     0,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,     0,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,    74,    69,    70,
      71,    72,    73,     0,    75,    76,    77,     0,     0,     0,
     578,     0,     0,     0,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,    67,    68,    69,    70,    71,    72,    73,
       0,    36,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    74,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,     0,     0,
     107,   512,   108,   100,   101,   102,   109,   110,   111,   112,
     113,   114,   115,     0,     0,     0,   116,   117,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     118,   284,     0,   285,     0,     0,     0,   119,     0,     0,
       0,   120,   121,   122,     0,     0,     0,     0,     0,   123,
       0,     0,     0,     0,     0,   286,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   126,     0,     0,     0,     0,     0,     0,
       0,     0,   287,     0,     0,     0,     0,     0,     0,   129,
     130,     0,     0,   132,     0,   133,     0,   428,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,    74,     0,     0,     0,     0,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,     0,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,     0,
       0,     0,   503,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,    67,    68,    69,    70,    71,    72,    73,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,     0,   513,     0,     0,     0,     0,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,    74,     0,     0,     0,     0,   622,
       0,    75,    76,    77,    67,    68,    69,    70,    71,    72,
      73,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
       0,     0,     0,     0,     0,   624,     0,     0,     0,     0,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    74,
       0,     0,     0,     0,     0,     0,    75,    76,    77,     0,
       0,     0,     0,     0,     0,     0,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,    74,     0,     0,     0,     0,
     672,     0,    75,    76,    77,    67,    68,    69,    70,    71,
      72,    73,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,     0,     0,     0,     0,     0,   673,     0,     0,     0,
       0,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      74,     0,     0,     0,     0,     0,     0,    75,    76,    77,
       0,     0,     0,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,    74,     0,     0,     0,
       0,   675,     0,    75,    76,    77,    67,    68,    69,    70,
      71,    72,    73,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,     0,     0,     0,     0,     0,   687,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    74,     0,     0,     0,     0,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,     0,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,    74,     0,     0,
       0,     0,   690,     0,    75,    76,    77,    67,    68,    69,
      70,    71,    72,    73,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,     0,     0,     0,     0,     0,   691,     0,
       0,     0,     0,    67,    68,    69,    70,    71,    72,    73,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    74,     0,     0,     0,     0,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,     0,     0,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,    74,     0,
       0,     0,     0,   721,     0,    75,    76,    77,    67,    68,
      69,    70,    71,    72,    73,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,     0,   729,
       0,     0,     0,     0,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,    74,
       0,     0,     0,     0,   741,     0,    75,    76,    77,     0,
       0,     0,     0,     0,     0,     0,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,     0,     0,     0,     0,   107,
     761,   108,   100,   101,   102,   109,   110,   111,   112,   113,
     114,   115,     0,     0,     0,   116,   117,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   118,
       0,     0,     0,     0,     0,     0,   119,     0,     0,     0,
     120,   121,   122,     0,     0,     0,     0,     0,   123,     0,
     124,     0,   125,     0,     0,     0,     0,     0,     0,     0,
       2,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   126,     0,     0,     0,     0,     0,     0,   127,
       0,   128,     0,     0,     0,     0,     0,     0,   129,   130,
     131,     0,   132,   107,   133,   108,   100,   101,   102,   109,
     110,   111,   112,   113,   114,   115,     0,     0,     0,   116,
     117,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   118,   284,     0,   285,     0,     0,     0,
     119,     0,     0,     0,   120,   121,   122,     0,     0,     0,
       0,     0,   123,     0,     0,     0,     0,     0,   286,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   126,    67,     0,    69,
      70,    71,    72,    73,   433,   287,     0,     0,     0,     0,
       0,     0,   129,   130,     0,     0,   132,   107,   133,   108,
     100,   101,   102,   109,   110,   111,   112,   113,   114,   115,
       0,     0,     0,   116,   117,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   118,   284,   559,
     285,     0,    74,     0,   119,     0,     0,     0,   120,   121,
     122,     0,     0,     0,     0,     0,   123,     0,     0,     0,
       0,     0,   286,     0,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,     0,     0,
     126,    67,     0,    69,    70,    71,    72,    73,     0,   287,
       0,     0,     0,     0,     0,     0,   129,   130,     0,     0,
     132,   107,   133,   108,   100,   101,   102,   109,   110,   111,
     112,   113,   114,   115,     0,     0,     0,   116,   117,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   118,   284,   717,   285,     0,    74,     0,   119,     0,
       0,     0,   120,   121,   122,     0,     0,     0,     0,     0,
     123,     0,     0,     0,     0,     0,   286,     0,     0,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,     0,     0,   126,     0,     0,     0,     0,     0,
       0,     0,     0,   287,     0,     0,     0,     0,     0,     0,
     129,   130,     0,     0,   132,   107,   133,   108,   100,   101,
     102,   109,   110,   111,   112,   113,   114,   115,     0,     0,
       0,   116,   117,     0,     0,     0,    67,    68,    69,    70,
      71,    72,    73,     0,     0,   118,   284,     0,   285,     0,
       0,     0,   119,     0,     0,     0,   120,   121,   122,     0,
       0,     0,     0,     0,   123,     0,     0,     0,     0,     0,
     286,     0,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   126,     0,
       0,    74,     0,     0,     0,     0,     0,   287,    75,    76,
      77,     0,     0,     0,   129,   130,     0,     0,   132,    78,
     133,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,    74,     0,     0,
       0,   160,     0,     0,    75,    76,    77,    67,    68,    69,
      70,    71,    72,    73,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,     0,     0,     0,     0,   321,     0,     0,
       0,     0,     0,    67,    68,    69,    70,    71,    72,    73,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    74,     0,     0,     0,     0,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,     0,     0,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,    74,     0,
       0,     0,   575,     0,     0,    75,    76,    77,    67,    68,
      69,    70,    71,    72,    73,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,   607,     0,
       0,     0,     0,     0,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,    74,
       0,     0,     0,   608,     0,     0,    75,    76,    77,    67,
      68,    69,    70,    71,    72,    73,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,     0,     0,     0,     0,   609,
       0,     0,     0,     0,     0,    67,    68,    69,    70,    71,
      72,    73,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    74,     0,     0,     0,     0,     0,
       0,    75,    76,    77,     0,     0,     0,     0,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
      74,     0,     0,     0,   610,     0,     0,    75,    76,    77,
      67,    68,    69,    70,    71,    72,    73,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,     0,     0,     0,     0,
     612,     0,     0,     0,     0,     0,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    74,     0,     0,     0,     0,
       0,     0,    75,    76,    77,     0,     0,     0,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,    74,     0,     0,     0,   614,     0,     0,    75,    76,
      77,    67,    68,    69,    70,    71,    72,    73,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,     0,
       0,   652,     0,     0,     0,     0,     0,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    74,     0,     0,     0,
       0,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,    74,     0,     0,     0,   763,     0,     0,    75,
      76,    77,    67,    68,    69,    70,    71,    72,    73,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,     0,     0,
       0,     0,   764,    67,    68,    69,    70,    71,    72,    73,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   317,   318,     0,    74,     0,     0,
       0,     0,     0,     0,    75,    76,    77,     0,     0,     0,
       0,     0,     0,     0,     0,    78,   319,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,    74,    89,
      90,    91,    92,     0,     0,    75,    76,    77,    67,    68,
      69,    70,    71,    72,    73,     0,    78,   323,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,     0,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,    74,    89,    90,    91,    92,     0,
       0,    75,    76,    77,    67,     0,    69,    70,    71,    72,
      73,     0,     0,     0,     0,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    74,
       0,     0,     0,     0,     0,     0,    75,    76,    77,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92
};

static const yytype_int16 yycheck[] =
{
      45,    18,    43,   108,    48,   296,    18,   310,   122,   284,
      47,     5,   244,   386,   547,   404,   219,     5,   424,   419,
       5,   554,     5,   423,     5,     5,     5,    34,     5,     5,
       5,     5,    79,    16,    51,     5,    21,     5,     5,    51,
       5,    21,    21,     5,     5,     3,   149,     8,     9,    10,
       4,     5,     5,     4,     5,   124,   122,     5,   431,    45,
     124,   125,   131,   102,   108,   131,   122,     5,   124,     5,
     122,     0,   124,   129,   118,   131,   120,    94,   125,   123,
     609,   610,   127,     4,     5,   474,   125,     5,   132,   106,
     135,   122,   481,   125,    47,    48,   128,    42,   129,    45,
     131,    45,    45,    84,   121,   122,    45,   124,    66,    47,
      48,    45,   645,    45,   219,   220,   122,   125,   126,   126,
      45,    45,   116,   129,    45,   131,   231,    45,    82,   232,
     233,    82,   149,   150,   123,   116,     5,   154,   429,   127,
     129,   122,   154,   446,   121,   551,   131,   122,   131,   135,
     550,   131,   131,   267,   131,   131,   270,   131,   272,   121,
     122,   131,   123,   131,   131,   127,   131,   208,   122,   118,
     123,   122,     5,   121,   123,   219,   220,   214,   123,   127,
     125,   714,   122,   132,   287,   121,   122,   231,   420,   135,
     234,   135,   135,   121,   211,   212,   135,   241,   401,   402,
     244,   135,   305,   135,   124,   125,   309,   596,   252,   742,
     135,   135,    83,     4,   125,   232,    61,   126,   117,    64,
     131,   122,   131,   124,   261,   758,   122,    18,    19,    20,
     131,   124,     4,    24,    25,    26,   124,   124,   131,   284,
     123,   647,   125,   131,   131,   116,   117,   118,   781,     5,
     267,   296,   131,   270,    45,   272,   361,    11,    12,    13,
     365,   278,    16,   108,   367,    12,    13,   499,   127,    16,
     373,     5,   126,   118,     8,     9,    10,   131,   123,   126,
     123,   386,   125,   558,    30,    31,    32,   132,   694,   306,
       5,    82,   241,   310,   679,   124,   125,   411,   683,   684,
     337,   415,    12,   252,   418,   123,   343,   125,   124,   715,
       8,     9,    99,    11,   351,   547,     6,   361,   335,     5,
     129,   365,   131,    21,    22,    23,   431,   122,   345,   124,
     347,   123,   369,   125,   378,   347,   679,    83,   124,   125,
     683,   684,   386,   122,   388,   124,   752,   123,    16,   125,
     394,    67,    68,    69,    70,    71,    72,    73,    74,     5,
     651,   652,    16,   407,    30,    31,    32,   404,   741,   115,
     116,   117,   118,     5,   219,   220,   420,   122,   419,   124,
     424,   123,   423,   125,   429,   126,   231,   431,   761,   234,
     123,   123,   125,   125,     5,   123,   241,   125,   123,   244,
     125,   123,   123,   125,   125,   124,   125,   252,    28,    29,
      30,    31,    32,    33,    34,   124,   125,    83,   435,   123,
     437,   125,   123,   123,   125,   125,   123,   444,   125,   378,
     123,   123,   125,   125,   123,     5,   125,   474,   541,   388,
     543,   544,   545,   546,   126,   394,   112,   113,    16,   115,
     116,   117,   118,   124,   123,   499,   125,    57,     5,    59,
      80,    81,    57,    83,    59,    57,   123,    59,   125,   760,
      90,    91,    92,   126,   123,   424,   125,   124,   125,   124,
     125,   101,   102,   103,   104,   105,   106,     5,   108,   109,
     110,   111,   112,   113,   125,   115,   116,   117,   118,   124,
     125,   124,   125,   547,   126,   549,   124,   551,   799,   550,
     554,     5,   132,   558,   124,   125,   361,   124,   125,   124,
     365,   124,   125,   122,   541,     5,   543,   124,   125,   632,
     124,   125,   122,   378,   637,   122,   122,   122,   122,   122,
       5,   386,   122,   388,    30,    31,    32,    33,    34,   394,
     129,   654,   126,   126,     5,   124,   131,   122,   122,   126,
      13,   124,   606,   607,     5,   126,     5,   122,   612,   125,
     614,     5,   126,   126,   126,   420,   124,     5,   124,   424,
     124,   124,   124,     5,     5,   124,   431,   124,     5,   124,
     124,     5,   124,   122,   127,   698,   126,    83,   642,   124,
     549,   645,   551,   124,   124,   554,   651,   652,    11,   712,
     713,   124,    59,   124,   126,   124,   633,   634,   635,   122,
     637,   638,   124,   129,   110,   111,   112,   113,   124,   115,
     116,   117,   118,   122,   129,   123,   741,   124,    57,   124,
     124,   124,   124,   124,    59,   124,   124,   124,   124,   124,
     694,   124,   755,    39,   499,    52,   761,   606,   607,   102,
     124,   124,   124,   612,     5,   614,   124,   124,    57,    39,
     714,   715,   128,    52,   124,    52,    52,    57,   124,     5,
     124,    59,   699,    57,   701,     5,   730,   731,   124,   124,
      57,   124,   736,   642,    57,   712,   645,   741,   742,   124,
      59,   124,   547,    57,   549,     4,   551,   208,   752,   554,
     441,   135,   486,   407,   758,   760,   591,   761,   413,   585,
     150,   427,   118,   197,   365,   620,   466,    -1,    -1,    -1,
     162,    -1,    -1,    -1,    -1,    -1,    -1,   781,   755,   756,
      -1,    -1,    -1,    -1,    -1,   694,    -1,    -1,   792,    -1,
      -1,    -1,    -1,    -1,   799,    -1,    -1,    -1,     4,     5,
      -1,   606,   607,    -1,    -1,   714,   715,   612,    -1,   614,
      -1,    -1,    18,    19,    20,    -1,    -1,    -1,    24,    25,
      26,   730,   731,    -1,    -1,    -1,    -1,   736,    -1,    -1,
      -1,    -1,    -1,   742,    -1,    -1,    -1,   642,    -1,    45,
     645,    -1,    -1,   752,    -1,    -1,    -1,    -1,    -1,   758,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      66,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   781,    -1,    -1,    -1,    82,    -1,    -1,    -1,
      -1,    -1,    -1,   792,    90,    91,    92,    -1,    -1,   694,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   103,   104,   105,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   113,    -1,   714,
     715,    -1,    -1,    -1,    -1,    -1,   122,   123,    -1,    -1,
      -1,   127,    -1,   129,    -1,   730,   731,   133,   134,    -1,
      -1,   736,    -1,    -1,    -1,    -1,   741,   742,    -1,    10,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   752,    -1,    -1,
      -1,    -1,    -1,   758,    -1,    -1,   761,    28,    29,    30,
      31,    32,    33,    34,    35,    36,    37,    38,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   781,    -1,    49,    -1,
      -1,    52,    -1,    -1,    -1,    -1,    -1,   792,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    67,    68,    69,    70,
      71,    72,    73,    74,    75,    76,    77,    78,    79,    80,
      81,    82,    83,    84,    85,    86,    87,    88,    89,    90,
      91,    92,    -1,    -1,     4,     5,    -1,     4,     5,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    18,    19,
      20,    18,    19,    20,    24,    25,    26,    24,    25,    26,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    40,    41,    45,    -1,    -1,    45,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    66,    -1,    -1,    66,
      -1,   162,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    82,    -1,    -1,    82,    -1,    -1,    -1,    -1,
      90,    91,    92,    90,    91,    92,    -1,    -1,    -1,    -1,
     191,    -1,   193,   103,   104,   105,   103,   104,   105,    -1,
      -1,    -1,    -1,   113,    -1,    -1,   113,    -1,    -1,    -1,
      -1,    -1,   122,   123,    -1,   122,    -1,   127,    -1,   129,
     127,    -1,    -1,   133,   134,    -1,   133,   134,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   236,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,     4,     5,   246,   247,    -1,    -1,   250,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    18,    19,    20,
      -1,    -1,    -1,    24,    25,    26,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    45,    -1,    -1,    -1,    -1,    -1,
      -1,    52,    53,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    66,    -1,    -1,    -1,    -1,
      -1,    -1,   313,   314,    -1,    -1,   317,   318,   319,    -1,
      -1,    82,   323,    -1,   325,    -1,    -1,   328,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   103,   104,   105,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   113,    -1,    -1,     4,     5,    -1,    -1,    -1,
      -1,   122,    -1,    -1,    -1,   366,   127,    -1,    -1,    18,
      19,    20,   133,   134,    -1,    24,    25,    26,   379,    -1,
      -1,   382,   383,   384,    -1,    -1,   387,    -1,    -1,    -1,
      -1,   392,    -1,    -1,    -1,    -1,    45,   398,    -1,    -1,
     401,   402,    -1,    52,    53,    -1,    -1,   408,   409,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    66,    -1,    -1,
      -1,    -1,    -1,    -1,   425,    -1,    -1,    -1,    -1,   430,
      -1,    -1,    -1,    82,    -1,    -1,    -1,   438,    -1,    -1,
      -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   454,   103,   104,   105,    -1,    -1,    -1,
      -1,     4,     5,    -1,   113,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   122,    -1,    18,    19,    20,   127,    -1,
      -1,    24,    25,    26,   133,   134,    -1,   488,   489,    -1,
      -1,    -1,    -1,    -1,   495,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    45,    -1,    -1,    -1,    -1,    -1,    -1,    52,
      53,   512,    -1,    -1,    -1,     4,     5,   518,   519,    -1,
      -1,    -1,   523,    66,   525,    -1,    -1,    -1,    -1,    18,
      19,    20,    -1,    -1,    -1,    24,    25,    26,    -1,    82,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,
      -1,    -1,    -1,    -1,    -1,    -1,    45,    -1,    -1,    -1,
     103,   104,   105,    -1,    -1,    -1,    -1,    -1,    -1,   570,
     113,    -1,    -1,    -1,    -1,    -1,    -1,    66,    -1,   122,
      -1,    -1,    -1,    -1,   127,    -1,    -1,    -1,    -1,    -1,
     133,   134,    -1,    82,    -1,    -1,    -1,    -1,   599,    -1,
      -1,    90,    91,    92,    -1,    -1,    -1,     4,     5,    -1,
     611,    -1,    -1,    -1,   103,   104,   105,    -1,    -1,   620,
     109,    18,    19,    20,   113,    -1,    -1,    24,    25,    26,
      -1,    -1,    -1,   122,    -1,    -1,    -1,    -1,   127,    -1,
      -1,     4,     5,    -1,   133,   134,    -1,    -1,    45,    -1,
      -1,    -1,   653,    -1,    -1,    18,    19,    20,   659,    -1,
      -1,    24,    25,    26,   665,    -1,    -1,    -1,    -1,    66,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    45,    -1,    -1,    82,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    66,    -1,    -1,   103,   104,   105,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   113,    -1,    -1,    82,
      -1,    -1,    -1,    -1,    -1,   122,   123,    90,    91,    92,
     127,     4,     5,    -1,    -1,    -1,   133,   134,    -1,    -1,
     103,   104,   105,    -1,    -1,    18,    19,    20,    -1,    -1,
     113,    24,    25,    26,    -1,    -1,    -1,    -1,   121,   122,
      -1,    -1,    -1,    -1,   127,     4,     5,    -1,    -1,    -1,
     133,   134,    45,    -1,    -1,    -1,    -1,    -1,    -1,    18,
      19,    20,    -1,    -1,    -1,    24,    25,    26,    -1,    -1,
      -1,    -1,    -1,    66,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    45,    -1,    -1,    82,
      -1,    -1,    -1,    -1,    53,    -1,    -1,    90,    91,    92,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    66,    -1,    -1,
     103,   104,   105,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     113,    -1,    -1,    82,    -1,    -1,    -1,    -1,    -1,   122,
      -1,    90,    91,    92,   127,    -1,   129,     4,     5,    -1,
     133,   134,    -1,    -1,   103,   104,   105,    -1,    -1,    -1,
      -1,    18,    19,    20,   113,    -1,    -1,    24,    25,    26,
      -1,    -1,    -1,   122,    -1,    -1,    -1,    -1,   127,    -1,
      -1,     4,     5,    -1,   133,   134,    -1,    -1,    45,    -1,
      -1,    -1,    -1,    -1,    -1,    18,    19,    20,    -1,    -1,
      -1,    24,    25,    26,    -1,    -1,    -1,    -1,    -1,    66,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    45,    -1,    -1,    82,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    66,    -1,    -1,   103,   104,   105,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   113,    -1,    -1,    82,
      -1,    -1,    -1,    -1,    -1,   122,   123,    90,    91,    92,
     127,    -1,    -1,    -1,    -1,    -1,   133,   134,    -1,    -1,
     103,   104,   105,    -1,    -1,    -1,    -1,    -1,    -1,     5,
     113,     7,    -1,    -1,    -1,    11,    -1,    -1,    -1,   122,
      -1,    -1,    -1,    -1,   127,    21,    -1,    -1,    -1,    -1,
     133,   134,    28,    29,    30,    31,    32,    33,    34,    -1,
      36,    -1,    38,    -1,    -1,    -1,    -1,    43,    44,    -1,
      -1,    -1,    -1,    49,    50,    51,    -1,    -1,    -1,    55,
      -1,    -1,    -1,    -1,    60,    61,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    75,
      -1,    77,    78,    -1,    -1,    -1,    -1,    83,    -1,    -1,
      -1,    -1,    88,    89,    90,    91,    92,    93,    -1,    -1,
      -1,    97,    -1,    -1,    -1,   101,    -1,   103,   104,   105,
     106,    -1,   108,   109,   110,   111,   112,   113,    -1,   115,
     116,   117,   118,    -1,    -1,   121,    -1,    -1,   124,    -1,
      -1,   127,    -1,     5,   130,     7,     8,     9,    -1,    11,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    21,
      22,    23,    -1,    -1,     5,    -1,     7,    -1,    -1,    -1,
      11,    -1,    -1,    -1,    36,    -1,    38,    -1,    -1,    -1,
      21,    43,    44,    -1,    -1,    -1,    -1,    49,    50,    51,
      -1,    -1,    -1,    55,    -1,    36,    37,    38,    60,    61,
      -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,    50,
      51,    -1,    -1,    75,    55,    77,    78,    -1,    -1,    60,
      61,    -1,    -1,    -1,    -1,    -1,    88,    89,    -1,    -1,
      -1,    93,    -1,    -1,    75,    97,    77,    78,     5,    -1,
       7,    -1,    -1,    -1,    11,    -1,    -1,    88,    89,    -1,
      -1,    -1,    93,    -1,    21,    -1,    97,    -1,    -1,   121,
      -1,   102,    -1,    -1,    -1,   127,    -1,    -1,   130,    36,
      -1,    38,    -1,    -1,    -1,    -1,    43,    44,    -1,    -1,
     121,    -1,    49,    50,    51,    -1,   127,    -1,    55,   130,
      -1,    -1,    -1,    60,    61,    -1,     5,    -1,     7,    -1,
      -1,    -1,    11,    -1,    -1,    -1,    -1,    -1,    75,    -1,
      77,    78,    21,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    88,    89,    -1,    -1,    -1,    93,    36,    37,    38,
      97,    -1,    -1,    -1,    43,    44,    -1,    -1,    -1,    -1,
      49,    50,    51,    -1,    -1,    -1,    55,    -1,    -1,    -1,
      -1,    60,    61,    -1,   121,    -1,    -1,   124,    -1,     5,
     127,     7,    -1,   130,    -1,    11,    75,    -1,    77,    78,
      -1,    -1,    -1,    -1,    -1,    21,    -1,    -1,    -1,    88,
      89,    -1,    -1,    -1,    93,    -1,    -1,    -1,    97,    -1,
      36,    -1,    38,    -1,    -1,    -1,    -1,    43,    44,    -1,
      -1,    -1,    -1,    49,    50,    51,    -1,    -1,    -1,    55,
      -1,    -1,   121,    -1,    60,    61,    -1,     5,   127,     7,
      -1,   130,    -1,    11,    -1,    -1,    -1,    -1,    -1,    75,
      76,    77,    78,    21,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    88,    89,    -1,    -1,    -1,    93,    36,    -1,
      38,    97,    -1,    -1,    -1,    43,    44,    -1,    -1,    -1,
      -1,    49,    50,    51,    -1,    -1,    -1,    55,    -1,    57,
      -1,    -1,    60,    61,    -1,   121,    -1,    -1,    -1,    -1,
       5,   127,     7,    -1,   130,    -1,    11,    75,    -1,    77,
      78,    -1,    -1,    -1,    -1,    -1,    21,    -1,    -1,    -1,
      88,    89,    -1,    -1,    -1,    93,    -1,    -1,    -1,    97,
      -1,    36,    37,    38,    -1,    -1,    -1,    -1,    43,    44,
      -1,    -1,    -1,    -1,    49,    50,    51,    -1,    -1,    -1,
      55,    -1,    -1,   121,    -1,    60,    61,    -1,     5,   127,
       7,    -1,   130,    -1,    11,    -1,    -1,    -1,    -1,    -1,
      75,    -1,    77,    78,    21,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    88,    89,    -1,    -1,    -1,    93,    36,
      -1,    38,    97,    -1,    -1,    -1,    43,    44,    -1,    -1,
      -1,    -1,    49,    50,    51,    -1,    -1,    -1,    55,    -1,
      57,    -1,    -1,    60,    61,    -1,   121,    -1,    -1,    -1,
      -1,     5,   127,     7,    -1,   130,    -1,    11,    75,    -1,
      77,    78,    -1,    -1,    -1,    -1,    -1,    21,    -1,    -1,
      -1,    88,    89,    -1,    -1,    -1,    93,    -1,    -1,    -1,
      97,    -1,    36,    -1,    38,    -1,    -1,    -1,    -1,    43,
      44,    -1,    -1,    -1,    -1,    49,    50,    51,    -1,    -1,
      -1,    55,    -1,    -1,   121,    -1,    60,    61,    -1,     5,
     127,     7,    -1,   130,    -1,    11,    -1,    -1,    -1,    -1,
      -1,    75,    -1,    77,    78,    21,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    88,    89,    -1,    -1,    -1,    93,
      36,    -1,    38,    97,    -1,    -1,    -1,    43,    44,    -1,
      -1,    -1,    -1,    49,    50,    51,    -1,    -1,    -1,    55,
      -1,    -1,    -1,    -1,    60,    61,    -1,   121,    -1,    -1,
     124,    -1,    -1,   127,    -1,    -1,   130,    -1,    -1,    75,
      -1,    77,    78,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    88,    89,    -1,    -1,    -1,    93,    -1,    -1,
      -1,    97,     5,    -1,     7,    -1,    -1,    -1,    11,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    21,    -1,
      -1,    -1,    -1,    -1,    -1,   121,    -1,    -1,   124,    -1,
      -1,   127,    -1,    36,   130,    38,    -1,    -1,    -1,    -1,
      43,    44,    -1,    -1,    -1,    -1,    49,    50,    51,    -1,
      -1,    -1,    55,    -1,    -1,    -1,    -1,    60,    61,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
      -1,    -1,    75,    -1,    77,    78,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    88,    89,    -1,    -1,    -1,
      93,    -1,    -1,    -1,    97,    28,    29,    30,    31,    32,
      33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,   121,    -1,
      -1,    90,    91,    92,   127,    -1,    -1,   130,    -1,    -1,
      -1,    -1,   101,    -1,   103,   104,   105,   106,    -1,   108,
     109,   110,   111,   112,   113,    -1,   115,   116,   117,   118,
      83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,
      -1,    -1,    -1,   132,    -1,    -1,    -1,    -1,   101,    -1,
     103,   104,   105,   106,    -1,   108,   109,   110,   111,   112,
     113,    -1,   115,   116,   117,   118,    28,    29,    30,    31,
      32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,   132,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    28,    29,    30,    31,    32,    33,    34,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,
      92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   101,
      -1,   103,   104,   105,   106,    -1,   108,   109,   110,   111,
     112,   113,    -1,   115,   116,   117,   118,    83,    30,    31,
      32,    33,    34,    -1,    90,    91,    92,    -1,    -1,    -1,
     132,    -1,    -1,    -1,    -1,   101,    -1,   103,   104,   105,
     106,    -1,   108,   109,   110,   111,   112,   113,    -1,   115,
     116,   117,   118,    28,    29,    30,    31,    32,    33,    34,
      -1,   127,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   106,    -1,   108,   109,   110,   111,
     112,   113,    -1,   115,   116,   117,   118,    -1,    83,    -1,
      -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   101,    -1,   103,   104,
     105,   106,    -1,   108,   109,   110,   111,   112,   113,    -1,
     115,   116,   117,   118,    -1,    -1,    -1,    -1,    -1,    -1,
       5,   126,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    -1,    -1,    -1,    21,    22,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      35,    36,    -1,    38,    -1,    -1,    -1,    42,    -1,    -1,
      -1,    46,    47,    48,    -1,    -1,    -1,    -1,    -1,    54,
      -1,    -1,    -1,    -1,    -1,    60,    28,    29,    30,    31,
      32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    78,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    87,    -1,    -1,    -1,    -1,    -1,    -1,    94,
      95,    -1,    -1,    98,    -1,   100,    -1,   102,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,
      -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,
      92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   101,
      -1,   103,   104,   105,   106,    -1,   108,   109,   110,   111,
     112,   113,    -1,   115,   116,   117,   118,    -1,    -1,    -1,
      -1,    -1,   124,    83,    -1,    -1,    -1,    -1,    -1,    -1,
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
      -1,   124,    -1,    90,    91,    92,    28,    29,    30,    31,
      32,    33,    34,    -1,   101,    -1,   103,   104,   105,   106,
      -1,   108,   109,   110,   111,   112,   113,    -1,   115,   116,
     117,   118,    -1,    -1,    -1,    -1,    -1,   124,    -1,    -1,
      -1,    -1,    28,    29,    30,    31,    32,    33,    34,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,
      92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   101,
      -1,   103,   104,   105,   106,    -1,   108,   109,   110,   111,
     112,   113,    -1,   115,   116,   117,   118,    83,    -1,    -1,
      -1,    -1,   124,    -1,    90,    91,    92,    28,    29,    30,
      31,    32,    33,    34,    -1,   101,    -1,   103,   104,   105,
     106,    -1,   108,   109,   110,   111,   112,   113,    -1,   115,
     116,   117,   118,    -1,    -1,    -1,    -1,    -1,   124,    -1,
      -1,    -1,    -1,    28,    29,    30,    31,    32,    33,    34,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     101,    -1,   103,   104,   105,   106,    -1,   108,   109,   110,
     111,   112,   113,    -1,   115,   116,   117,   118,    83,    -1,
      -1,    -1,    -1,   124,    -1,    90,    91,    92,    28,    29,
      30,    31,    32,    33,    34,    -1,   101,    -1,   103,   104,
     105,   106,    -1,   108,   109,   110,   111,   112,   113,    -1,
     115,   116,   117,   118,    -1,    -1,    -1,    -1,    -1,   124,
      -1,    -1,    -1,    -1,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   101,    -1,   103,   104,   105,   106,    -1,   108,   109,
     110,   111,   112,   113,    -1,   115,   116,   117,   118,    83,
      -1,    -1,    -1,    -1,   124,    -1,    90,    91,    92,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   101,    -1,   103,
     104,   105,   106,    -1,   108,   109,   110,   111,   112,   113,
      -1,   115,   116,   117,   118,    -1,    -1,    -1,    -1,     5,
     124,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      16,    17,    -1,    -1,    -1,    21,    22,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    35,
      -1,    -1,    -1,    -1,    -1,    -1,    42,    -1,    -1,    -1,
      46,    47,    48,    -1,    -1,    -1,    -1,    -1,    54,    -1,
      56,    -1,    58,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      66,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    78,    -1,    -1,    -1,    -1,    -1,    -1,    85,
      -1,    87,    -1,    -1,    -1,    -1,    -1,    -1,    94,    95,
      96,    -1,    98,     5,   100,     7,     8,     9,    10,    11,
      12,    13,    14,    15,    16,    17,    -1,    -1,    -1,    21,
      22,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    35,    36,    -1,    38,    -1,    -1,    -1,
      42,    -1,    -1,    -1,    46,    47,    48,    -1,    -1,    -1,
      -1,    -1,    54,    -1,    -1,    -1,    -1,    -1,    60,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    78,    28,    -1,    30,
      31,    32,    33,    34,    86,    87,    -1,    -1,    -1,    -1,
      -1,    -1,    94,    95,    -1,    -1,    98,     5,   100,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    16,    17,
      -1,    -1,    -1,    21,    22,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    35,    36,    37,
      38,    -1,    83,    -1,    42,    -1,    -1,    -1,    46,    47,
      48,    -1,    -1,    -1,    -1,    -1,    54,    -1,    -1,    -1,
      -1,    -1,    60,    -1,   105,   106,    -1,   108,   109,   110,
     111,   112,   113,    -1,   115,   116,   117,   118,    -1,    -1,
      78,    28,    -1,    30,    31,    32,    33,    34,    -1,    87,
      -1,    -1,    -1,    -1,    -1,    -1,    94,    95,    -1,    -1,
      98,     5,   100,     7,     8,     9,    10,    11,    12,    13,
      14,    15,    16,    17,    -1,    -1,    -1,    21,    22,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    35,    36,    37,    38,    -1,    83,    -1,    42,    -1,
      -1,    -1,    46,    47,    48,    -1,    -1,    -1,    -1,    -1,
      54,    -1,    -1,    -1,    -1,    -1,    60,    -1,    -1,   106,
      -1,   108,   109,   110,   111,   112,   113,    -1,   115,   116,
     117,   118,    -1,    -1,    78,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    87,    -1,    -1,    -1,    -1,    -1,    -1,
      94,    95,    -1,    -1,    98,     5,   100,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    16,    17,    -1,    -1,
      -1,    21,    22,    -1,    -1,    -1,    28,    29,    30,    31,
      32,    33,    34,    -1,    -1,    35,    36,    -1,    38,    -1,
      -1,    -1,    42,    -1,    -1,    -1,    46,    47,    48,    -1,
      -1,    -1,    -1,    -1,    54,    -1,    -1,    -1,    -1,    -1,
      60,    -1,    28,    29,    30,    31,    32,    33,    34,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    78,    -1,
      -1,    83,    -1,    -1,    -1,    -1,    -1,    87,    90,    91,
      92,    -1,    -1,    -1,    94,    95,    -1,    -1,    98,   101,
     100,   103,   104,   105,   106,    -1,   108,   109,   110,   111,
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
      -1,    -1,    -1,    -1,    -1,    28,    29,    30,    31,    32,
      33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,
      -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   101,    -1,   103,   104,   105,   106,    -1,   108,
     109,   110,   111,   112,   113,    -1,   115,   116,   117,   118,
      83,    -1,    -1,    -1,   123,    -1,    -1,    90,    91,    92,
      28,    29,    30,    31,    32,    33,    34,    -1,   101,    -1,
     103,   104,   105,   106,    -1,   108,   109,   110,   111,   112,
     113,    -1,   115,   116,   117,   118,    -1,    -1,    -1,    -1,
     123,    -1,    -1,    -1,    -1,    -1,    28,    29,    30,    31,
      32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,
      -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   101,    -1,   103,   104,   105,   106,    -1,
     108,   109,   110,   111,   112,   113,    -1,   115,   116,   117,
     118,    83,    -1,    -1,    -1,   123,    -1,    -1,    90,    91,
      92,    28,    29,    30,    31,    32,    33,    34,    -1,   101,
      -1,   103,   104,   105,   106,    -1,   108,   109,   110,   111,
     112,   113,    -1,   115,   116,   117,   118,    -1,    -1,    -1,
      -1,   123,    -1,    -1,    -1,    -1,    -1,    28,    29,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   101,    -1,   103,   104,   105,   106,
      -1,   108,   109,   110,   111,   112,   113,    -1,   115,   116,
     117,   118,    83,    -1,    -1,    -1,   123,    -1,    -1,    90,
      91,    92,    28,    29,    30,    31,    32,    33,    34,    -1,
     101,    -1,   103,   104,   105,   106,    -1,   108,   109,   110,
     111,   112,   113,    -1,   115,   116,   117,   118,    -1,    -1,
      -1,    -1,   123,    28,    29,    30,    31,    32,    33,    34,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    80,    81,    -1,    83,    -1,    -1,
      -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   101,   102,   103,   104,   105,
     106,    -1,   108,   109,   110,   111,   112,   113,    83,   115,
     116,   117,   118,    -1,    -1,    90,    91,    92,    28,    29,
      30,    31,    32,    33,    34,    -1,   101,   102,   103,   104,
     105,   106,    -1,   108,   109,   110,   111,   112,   113,    -1,
     115,   116,   117,   118,    -1,    -1,    -1,    -1,    -1,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   101,    -1,   103,   104,   105,   106,    -1,   108,   109,
     110,   111,   112,   113,    83,   115,   116,   117,   118,    -1,
      -1,    90,    91,    92,    28,    -1,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,   104,   105,   106,    -1,   108,
     109,   110,   111,   112,   113,    -1,   115,   116,   117,   118,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,
      -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     104,   105,   106,    -1,   108,   109,   110,   111,   112,   113,
      -1,   115,   116,   117,   118
};

/* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
   symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,     3,    66,   136,   137,   138,   139,   146,     5,     4,
       5,    45,     0,   138,   121,   140,     5,     4,     5,    18,
      19,    20,    24,    25,    26,    45,    66,    82,    90,    91,
      92,   103,   104,   105,   113,   122,   127,   133,   134,   204,
     207,   209,   122,   122,   124,   141,   117,   122,   129,   131,
     200,   201,   122,   209,   209,   209,   209,   209,   209,   209,
     209,   109,   205,   206,   209,   209,   209,    28,    29,    30,
      31,    32,    33,    34,    83,    90,    91,    92,   101,   103,
     104,   105,   106,   108,   109,   110,   111,   112,   113,   115,
     116,   117,   118,     5,    47,    48,   123,   166,   167,     5,
       8,     9,    10,   123,   142,   143,   202,     5,     7,    11,
      12,    13,    14,    15,    16,    17,    21,    22,    35,    42,
      46,    47,    48,    54,    56,    58,    78,    85,    87,    94,
      95,    96,    98,   100,   144,   145,   146,   147,   150,   151,
     155,   156,   159,   160,   161,   168,   175,   176,   187,   202,
     203,     4,   196,   209,     5,   207,   209,   200,   201,   209,
     123,   204,   125,   128,   204,   209,   209,   209,   209,   209,
     209,   209,   209,   209,   209,   209,   209,   209,   209,   209,
     209,   209,   209,   209,   209,   209,   209,   209,   209,   209,
     209,   126,     5,   131,   200,     5,   123,   125,    12,    13,
      16,    11,    12,    13,    16,    12,   124,   123,   125,     5,
      21,   200,     5,   121,   122,   174,     5,   121,   122,   152,
     171,   191,   192,   198,   204,   207,    16,    16,     5,   199,
       5,     7,    11,    21,    36,    38,    43,    44,    49,    50,
      51,    55,    60,    61,    75,    77,    88,    89,    93,    97,
     121,   130,   180,   184,   187,   188,   189,   190,   198,   207,
       5,   122,     5,   162,   163,   207,     5,    16,   164,   165,
     200,   164,   200,   180,   184,     5,    21,   154,   200,     5,
       5,    45,   185,   186,    36,    38,    60,    87,   147,   150,
     151,   159,   160,   161,   168,   175,   177,   178,   179,   187,
     184,    99,     6,   144,   199,   200,     5,   148,   149,   174,
     200,     5,   123,   125,   122,   200,   201,    80,    81,   102,
     132,   123,   206,   102,   209,   126,   209,     5,   126,   167,
      16,   124,   143,   126,     5,     5,   200,   122,   124,   200,
       4,     5,    82,   122,   196,     5,   200,   201,     4,     5,
      82,   122,    67,    68,    69,    70,    71,    72,    73,    74,
     153,   171,   198,   198,   124,   125,   126,   125,   124,   122,
     124,   198,   199,   200,   199,    37,   102,   184,   197,   122,
     209,     5,   122,   122,   122,   184,   122,   122,   197,     5,
     209,   209,   122,     5,   209,     5,    84,   116,   122,   124,
     184,    34,   126,   124,   122,   196,   124,   125,   126,   126,
     164,   200,   124,   125,   164,   200,   124,   164,   200,   122,
     124,     5,   200,   122,   124,   126,    79,   125,   102,   177,
     122,   122,   199,    86,   178,    13,   124,   199,   126,   200,
     124,   125,     5,   199,     5,   149,   200,   209,   209,   209,
     209,   209,   209,   209,   126,   209,     4,    18,    19,    20,
      24,    25,    26,    45,    82,   208,   126,   200,     5,   123,
     129,   169,   170,   196,   122,   123,   129,   172,   173,   196,
     123,   122,   200,   200,   201,   196,   125,   198,   126,   126,
     192,   209,   199,   123,   196,   126,   124,   199,   124,     5,
      37,   184,   209,   124,   124,   209,   209,   209,   191,   209,
      76,   124,   126,   124,   209,   124,   124,   184,    40,    41,
     182,   183,   209,   171,   209,   171,   209,   169,   196,   123,
     162,   209,   209,   124,   164,   165,   124,   164,   124,   164,
     142,     8,     9,    11,    21,    22,    23,   157,   158,   197,
     122,   124,     5,   142,   157,   184,   209,   186,     5,    37,
     209,   191,   124,   200,   124,   200,   209,   124,     5,   148,
     126,   124,   200,   124,   149,   123,   132,   132,   132,   209,
     208,   124,     5,   116,   123,   125,   123,   169,   196,     5,
     123,   125,   123,   124,   123,   169,   122,   123,   153,   126,
     209,   209,   124,   123,   209,   124,   197,   123,   123,   123,
     123,   124,   123,   209,   123,   209,   209,    42,   123,   125,
     181,   209,   124,   209,   124,   123,   123,   124,   124,   124,
     124,   123,    21,   199,   200,    11,   199,   200,   199,   199,
     199,   158,   197,    57,   142,   157,   184,   124,   123,   184,
      59,   177,   123,   124,   127,   124,   209,   124,   124,   122,
     124,   170,   124,   123,   123,   122,   173,   124,   123,   169,
     123,   209,   124,   124,   124,   124,    37,   184,    53,   193,
     194,   195,   196,   193,   193,   209,   184,   124,   184,   183,
     124,   124,   124,   124,   124,   199,   124,   200,   200,   200,
     124,     5,   199,   200,   124,   200,   124,   124,    57,   123,
     184,    57,    11,    21,   157,   124,    59,    37,   178,   209,
     199,   124,   123,   209,   124,   124,   209,   124,   123,   124,
      39,   102,    52,   194,   195,    52,   102,    52,   195,    52,
     195,   124,   157,   184,   124,   124,   199,   200,   200,   124,
       5,   124,   124,    57,   199,   200,   199,   184,   157,   184,
      39,   124,   128,   123,   123,   124,   184,   124,   184,    52,
     124,   184,    52,    52,   191,   184,    57,   124,     5,   124,
     124,   157,   184,   124,   199,   124,    57,   184,    59,   178,
     191,     5,   123,    57,   124,   184,    57,   124,    59,   123,
     124,   184,    57,   178
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
#line 3120 "y.tab.c"
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


