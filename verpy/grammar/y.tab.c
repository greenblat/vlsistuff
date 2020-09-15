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
     tri0 = 268,
     tri1 = 269,
     signed = 270,
     event = 271,
     bin = 272,
     hex = 273,
     dig = 274,
     integer = 275,
     real = 276,
     wreal = 277,
     ubin = 278,
     uhex = 279,
     udig = 280,
     domino = 281,
     and_and = 282,
     or_or = 283,
     eq3 = 284,
     eq_eq = 285,
     not_eq = 286,
     gr_eq = 287,
     sm_eq = 288,
     always = 289,
     begin = 290,
     end = 291,
     if = 292,
     else = 293,
     posedge = 294,
     negedge = 295,
     or = 296,
     wait = 297,
     emit = 298,
     string = 299,
     defparam = 300,
     parameter = 301,
     localparam = 302,
     case = 303,
     casez = 304,
     casex = 305,
     endcase = 306,
     default = 307,
     initial = 308,
     forever = 309,
     function = 310,
     endfunction = 311,
     task = 312,
     endtask = 313,
     for = 314,
     while = 315,
     backtick_define = 316,
     backtick_include = 317,
     backtick_timescale = 318,
     backtick_undef = 319,
     define = 320,
     strong1 = 321,
     strong0 = 322,
     pull1 = 323,
     pull0 = 324,
     weak1 = 325,
     weak0 = 326,
     highz1 = 327,
     highz0 = 328,
     fork = 329,
     join = 330,
     disable = 331,
     pragma = 332,
     plus_range = 333,
     minus_range = 334,
     floating = 335,
     power = 336,
     star = 337,
     generate = 338,
     endgenerate = 339,
     genvar = 340,
     force = 341,
     release = 342,
     xnor = 343,
     nand = 344,
     nor = 345,
     repeat = 346,
     supply0 = 347,
     supply1 = 348,
     newver = 349,
     return = 350,
     arith_shift_right = 351,
     SignedLeft = 352,
     shift_right = 353,
     shift_left = 354,
     Veryequal = 355,
     noteqeq = 356,
     StarStar = 357,
     UNARY_PREC = 358
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
#define tri0 268
#define tri1 269
#define signed 270
#define event 271
#define bin 272
#define hex 273
#define dig 274
#define integer 275
#define real 276
#define wreal 277
#define ubin 278
#define uhex 279
#define udig 280
#define domino 281
#define and_and 282
#define or_or 283
#define eq3 284
#define eq_eq 285
#define not_eq 286
#define gr_eq 287
#define sm_eq 288
#define always 289
#define begin 290
#define end 291
#define if 292
#define else 293
#define posedge 294
#define negedge 295
#define or 296
#define wait 297
#define emit 298
#define string 299
#define defparam 300
#define parameter 301
#define localparam 302
#define case 303
#define casez 304
#define casex 305
#define endcase 306
#define default 307
#define initial 308
#define forever 309
#define function 310
#define endfunction 311
#define task 312
#define endtask 313
#define for 314
#define while 315
#define backtick_define 316
#define backtick_include 317
#define backtick_timescale 318
#define backtick_undef 319
#define define 320
#define strong1 321
#define strong0 322
#define pull1 323
#define pull0 324
#define weak1 325
#define weak0 326
#define highz1 327
#define highz0 328
#define fork 329
#define join 330
#define disable 331
#define pragma 332
#define plus_range 333
#define minus_range 334
#define floating 335
#define power 336
#define star 337
#define generate 338
#define endgenerate 339
#define genvar 340
#define force 341
#define release 342
#define xnor 343
#define nand 344
#define nor 345
#define repeat 346
#define supply0 347
#define supply1 348
#define newver 349
#define return 350
#define arith_shift_right 351
#define SignedLeft 352
#define shift_right 353
#define shift_left 354
#define Veryequal 355
#define noteqeq 356
#define StarStar 357
#define UNARY_PREC 358




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
#line 313 "y.tab.c"

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
#define YYLAST   5281

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  130
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  70
/* YYNRULES -- Number of rules.  */
#define YYNRULES  348
/* YYNRULES -- Number of states.  */
#define YYNSTATES  776

/* YYTRANSLATE(YYLEX) -- Bison symbol number corresponding to YYLEX.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   358

#define YYTRANSLATE(YYX)						\
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[YYLEX] -- Bison symbol number corresponding to YYLEX.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   128,     2,   116,     2,   113,   100,     2,
     117,   118,   111,   107,   120,   108,   122,   112,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,    97,   119,
     105,   121,   106,    96,   123,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,   124,     2,   125,    99,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   126,    98,   127,   129,     2,     2,     2,
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
      95,   101,   102,   103,   104,   109,   110,   114,   115
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
     579,   586,   594,   603,   611,   615,   617,   620,   626,   631,
     636,   639,   642,   645,   649,   651,   657,   660,   665,   668,
     671,   674,   679,   683,   686,   690,   694,   697,   699,   703,
     709,   713,   715,   717,   719,   721,   723,   725,   727,   729,
     731,   737,   745,   755,   758,   761,   764,   769,   771,   773,
     777,   779,   782,   785,   787,   791,   794,   797,   803,   807,
     812,   818,   823,   829,   835,   843,   847,   851,   855,   860,
     864,   870,   873,   877,   881,   886,   892,   899,   907,   914,
     921,   929,   936,   944,   948,   952,   955,   957,   959,   961,
     964,   966,   972,   976,   986,   992,   998,  1002,  1004,  1008,
    1011,  1013,  1017,  1021,  1025,  1029,  1033,  1035,  1038,  1040,
    1042,  1045,  1049,  1053,  1056,  1058,  1060,  1064,  1066,  1072,
    1078,  1084,  1088,  1090,  1092,  1094,  1097,  1100,  1103,  1106,
    1109,  1112,  1116,  1118,  1120,  1122,  1124,  1126,  1129,  1132,
    1134,  1136,  1138,  1140,  1142,  1146,  1150,  1152,  1155,  1157,
    1160,  1164,  1168,  1173,  1178,  1185,  1187,  1189,  1191,  1193,
    1195,  1197,  1199,  1201,  1203,  1205,  1207,  1209,  1211,  1213,
    1215,  1220,  1222,  1224,  1226,  1228,  1230,  1232,  1235,  1239,
    1243,  1246,  1252,  1256,  1260,  1264,  1268,  1272,  1276,  1280,
    1284,  1288,  1292,  1296,  1300,  1304,  1308,  1312,  1316,  1320,
    1324,  1328,  1332,  1336,  1340,  1344,  1348,  1352,  1357,  1361,
    1363,  1366,  1369,  1372,  1375,  1378,  1381,  1384,  1387
};

/* YYRHS -- A `-1'-separated list of the rules' RHS.  */
static const yytype_int16 yyrhs[] =
{
     131,     0,    -1,   132,    -1,   132,   133,    -1,   133,    -1,
     134,    -1,   141,    -1,     3,     5,   135,   136,   139,     6,
      -1,   116,   117,   159,   118,    -1,   116,   117,   118,    -1,
      -1,   119,    -1,   117,   137,   118,   119,    -1,   117,   118,
     119,    -1,   137,   120,   138,    -1,   138,    -1,   192,     5,
      -1,   192,   190,     5,    -1,   192,    20,     5,    -1,   192,
     190,     5,   190,    -1,   192,   190,   190,     5,    -1,     5,
      -1,   192,     5,   121,   198,    -1,   192,   190,     5,   121,
     198,    -1,   140,   139,    -1,    -1,   143,    -1,   144,    -1,
     161,    -1,   168,    -1,   169,    -1,   152,    -1,   153,    -1,
     154,    -1,   142,    -1,   148,    -1,   149,    -1,   141,    -1,
      77,    -1,    94,    -1,    65,    44,    -1,    65,     5,    -1,
      65,     5,   199,    -1,    65,     4,     5,   112,     4,     5,
      -1,    53,   177,    -1,   192,   189,   119,    -1,    16,   189,
     119,    -1,   193,   189,   119,    -1,   193,   189,   121,   199,
     119,    -1,   192,   190,   189,   119,    -1,   192,   190,   189,
     190,   119,    -1,   193,   190,   189,   119,    -1,   193,   190,
       5,   121,   199,   119,    -1,   193,   190,     5,   190,   119,
      -1,   193,   190,   190,   189,   119,    -1,   193,   190,   190,
       5,   121,   199,   119,    -1,   193,     5,   190,   119,    -1,
     193,   167,   189,   119,    -1,   193,   167,     5,   121,   199,
     119,    -1,     5,    26,     5,     5,   119,    -1,     7,   181,
     119,    -1,     7,   164,   188,   121,   199,   119,    -1,     7,
     145,   164,   188,   121,   199,   119,    -1,     7,   145,   188,
     121,   199,   119,    -1,   117,   146,   120,   146,   118,    -1,
      66,    -1,    67,    -1,    68,    -1,    69,    -1,    70,    -1,
      71,    -1,    72,    -1,    73,    -1,   190,    -1,    20,    -1,
      55,     5,   119,   150,   187,    56,    -1,    55,     5,   119,
     187,    56,    -1,    55,   190,   190,     5,   119,   150,   177,
      56,    -1,    55,   147,     5,   119,   150,   177,    56,    -1,
      55,   147,     5,   119,   177,    56,    -1,    55,     5,   117,
     137,   118,   119,   177,    56,    -1,    55,     5,   117,   137,
     118,   119,   150,   177,    56,    -1,    55,   147,     5,   117,
     137,   118,   119,   177,    56,    -1,    55,   147,     5,   117,
     137,   118,   119,   150,   177,    56,    -1,    57,     5,   119,
     150,   177,    58,    -1,    57,     5,   119,   177,    58,    -1,
      57,     5,   117,   137,   118,   119,   177,    58,    -1,    57,
       5,   117,   137,   118,   119,   150,   177,    58,    -1,   150,
     151,    -1,   151,    -1,    11,   189,   119,    -1,    21,   189,
     119,    -1,    22,   189,   119,    -1,    11,   190,   189,   119,
      -1,    11,   190,     5,   190,   119,    -1,    11,   190,   190,
       5,   119,    -1,     9,    11,   190,   190,     5,   119,    -1,
       8,   189,   119,    -1,     8,   189,   190,   119,    -1,     8,
     190,   190,   189,   119,    -1,     8,    20,   189,   119,    -1,
      20,   189,   119,    -1,    20,   189,   190,   119,    -1,    46,
     157,   119,    -1,    46,    15,   157,   119,    -1,    46,   190,
     157,   119,    -1,    46,   190,   190,   157,   119,    -1,    46,
      15,   190,   157,   119,    -1,    47,   157,   119,    -1,    47,
     190,   157,   119,    -1,    47,   190,   190,   157,   119,    -1,
      45,   156,   119,    -1,   197,   121,   199,    -1,   156,   120,
     155,    -1,   155,    -1,   157,   120,   158,    -1,   158,    -1,
       5,   121,   199,    -1,   159,   120,   160,    -1,   160,    -1,
      46,     5,   121,   199,    -1,    46,   190,     5,   121,   199,
      -1,     5,   121,   199,    -1,     5,     5,   117,   118,   119,
      -1,     5,   167,     5,   117,   118,   119,    -1,     5,     5,
     119,    -1,    41,   117,   186,   118,   119,    -1,    41,     5,
     117,   186,   118,   119,    -1,     5,     5,   117,   162,   118,
     119,    -1,    41,     5,   117,   162,   118,   119,    -1,     5,
       5,   117,   186,   118,   119,    -1,     5,   167,     5,   117,
     162,   118,   119,    -1,     5,   167,     5,   190,   117,   162,
     118,   119,    -1,     5,     5,   190,   117,   162,   118,   119,
      -1,   162,   120,   163,    -1,   163,    -1,   122,   111,    -1,
     122,     5,   117,   199,   118,    -1,   122,     5,   117,   118,
      -1,   116,   117,   186,   118,    -1,   116,     4,    -1,   116,
       5,    -1,   116,    80,    -1,   165,   120,   166,    -1,   166,
      -1,   122,     5,   117,   199,   118,    -1,   122,     5,    -1,
     116,   117,   186,   118,    -1,   116,     4,    -1,   116,    80,
      -1,   116,     5,    -1,   116,   117,   165,   118,    -1,   116,
     117,   118,    -1,    34,   177,    -1,    34,   173,   177,    -1,
      83,   170,    84,    -1,   170,   171,    -1,   171,    -1,    35,
     170,    36,    -1,    35,    97,     5,   170,    36,    -1,    85,
       5,   119,    -1,   143,    -1,   144,    -1,   152,    -1,   153,
      -1,   154,    -1,   161,    -1,   172,    -1,   168,    -1,   142,
      -1,    37,   117,   199,   118,   171,    -1,    37,   117,   199,
     118,   171,    38,   171,    -1,    59,   117,   181,   119,   199,
     119,   181,   118,   171,    -1,   123,   111,    -1,   123,    82,
      -1,   123,     5,    -1,   123,   117,   175,   118,    -1,    41,
      -1,   120,    -1,   175,   174,   176,    -1,   176,    -1,    39,
     199,    -1,    40,   199,    -1,   199,    -1,    35,   187,    36,
      -1,    35,    36,    -1,    54,   177,    -1,    35,    97,     5,
     187,    36,    -1,    74,   187,    75,    -1,   188,   121,   199,
     119,    -1,   188,   121,   164,   199,   119,    -1,   188,    33,
     199,   119,    -1,   188,    33,   164,   199,   119,    -1,    37,
     117,   199,   118,   177,    -1,    37,   117,   199,   118,   177,
      38,   177,    -1,    42,   199,   119,    -1,    20,   189,   119,
      -1,    11,   189,   119,    -1,    11,   190,   189,   119,    -1,
      87,   199,   119,    -1,    86,   199,   121,   199,   119,    -1,
     173,   119,    -1,    43,     5,   119,    -1,    76,     5,   119,
      -1,     5,   117,   118,   119,    -1,     5,   117,   186,   118,
     119,    -1,    48,   117,   199,   118,   183,    51,    -1,    48,
     117,   199,   118,   183,   185,    51,    -1,    48,   117,   199,
     118,   185,    51,    -1,    49,   117,   199,   118,   183,    51,
      -1,    49,   117,   199,   118,   183,   185,    51,    -1,    50,
     117,   199,   118,   183,    51,    -1,    50,   117,   199,   118,
     183,   185,    51,    -1,   116,   199,   119,    -1,   116,   199,
     177,    -1,     5,   119,    -1,   178,    -1,   179,    -1,   180,
      -1,   197,   119,    -1,    77,    -1,     7,   188,   121,   199,
     119,    -1,    95,     5,   119,    -1,    59,   117,   181,   119,
     199,   119,   181,   118,   177,    -1,    91,   117,   199,   118,
     177,    -1,    60,   117,   199,   118,   177,    -1,   181,   120,
     182,    -1,   182,    -1,   188,   121,   199,    -1,   183,   184,
      -1,   184,    -1,   186,    97,   177,    -1,   186,    97,   119,
      -1,    52,    97,   177,    -1,    52,    97,   119,    -1,   186,
     120,   199,    -1,   199,    -1,   187,   177,    -1,   177,    -1,
       5,    -1,     5,   190,    -1,     5,   191,   190,    -1,     5,
     191,   191,    -1,     5,   191,    -1,   197,    -1,   194,    -1,
       5,   120,   189,    -1,     5,    -1,   124,   199,    97,   199,
     125,    -1,   124,   199,    78,   199,   125,    -1,   124,   199,
      79,   199,   125,    -1,   124,   199,   125,    -1,     8,    -1,
       9,    -1,    10,    -1,     9,    11,    -1,     8,    12,    -1,
       9,    12,    -1,    10,    12,    -1,     8,    15,    -1,     9,
      15,    -1,     9,    11,    15,    -1,    11,    -1,    12,    -1,
      15,    -1,    20,    -1,    21,    -1,    11,    15,    -1,    12,
      15,    -1,    85,    -1,    92,    -1,    93,    -1,    13,    -1,
      14,    -1,   126,   195,   127,    -1,   195,   120,   196,    -1,
     196,    -1,   199,   194,    -1,   199,    -1,   104,   194,    -1,
       5,   122,   197,    -1,     5,   122,     5,    -1,     5,   122,
       5,   190,    -1,     5,   122,     5,   191,    -1,     5,   122,
       5,   117,   199,   118,    -1,     4,    -1,    80,    -1,    44,
      -1,    17,    -1,    18,    -1,    19,    -1,    23,    -1,    24,
      -1,    25,    -1,     5,    -1,   197,    -1,     4,    -1,    80,
      -1,    44,    -1,    65,    -1,    65,   117,   199,   118,    -1,
      17,    -1,    18,    -1,    19,    -1,    23,    -1,    24,    -1,
      25,    -1,     5,   190,    -1,     5,   191,   190,    -1,     5,
     191,   191,    -1,     5,   191,    -1,   199,    96,   199,    97,
     199,    -1,   199,   107,   199,    -1,   199,   111,   199,    -1,
     199,   108,   199,    -1,   199,   112,   199,    -1,   199,   113,
     199,    -1,   199,    99,   199,    -1,   199,    98,   199,    -1,
     199,   100,   199,    -1,   199,   105,   199,    -1,   199,   106,
     199,    -1,   199,    81,   199,    -1,   199,    27,   199,    -1,
     199,    28,   199,    -1,   199,    88,   199,    -1,   199,    89,
     199,    -1,   199,    90,   199,    -1,   199,    30,   199,    -1,
     199,    29,   199,    -1,   199,    31,   199,    -1,   199,   110,
     199,    -1,   199,    32,   199,    -1,   199,    33,   199,    -1,
     199,   104,   199,    -1,   199,   103,   199,    -1,   199,   101,
     199,    -1,     5,   117,   186,   118,    -1,   117,   199,   118,
      -1,   194,    -1,   108,   199,    -1,    98,   199,    -1,   100,
     199,    -1,    99,   199,    -1,    88,   199,    -1,    90,   199,
      -1,    89,   199,    -1,   128,   199,    -1,   129,   199,    -1
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
     172,   173,   174,   175,   183,   183,   184,   184,   184,   186,
     186,   186,   186,   187,   187,   188,   188,   189,   189,   189,
     189,   189,   189,   192,   192,   195,   197,   197,   200,   201,
     202,   203,   204,   205,   206,   207,   208,   209,   210,   211,
     212,   213,   218,   223,   223,   223,   223,   224,   224,   225,
     225,   226,   226,   226,   231,   232,   233,   234,   235,   236,
     237,   238,   239,   240,   241,   242,   243,   244,   245,   246,
     247,   248,   249,   250,   251,   252,   253,   254,   255,   256,
     257,   258,   259,   260,   261,   262,   263,   264,   265,   266,
     267,   268,   269,   272,   273,   274,   275,   275,   276,   277,
     277,   278,   278,   279,   279,   281,   281,   282,   282,   285,
     285,   285,   285,   285,   285,   285,   287,   287,   289,   289,
     289,   290,   292,   292,   292,   292,   292,   292,   292,   292,
     292,   292,   294,   294,   294,   294,   294,   294,   294,   294,
     294,   294,   294,   294,   296,   297,   297,   299,   300,   301,
     305,   306,   307,   308,   309,   313,   314,   315,   316,   316,
     316,   316,   316,   316,   320,   321,   322,   323,   324,   325,
     326,   327,   327,   327,   327,   327,   327,   328,   329,   330,
     331,   332,   333,   334,   335,   336,   337,   338,   339,   340,
     341,   342,   343,   344,   345,   346,   347,   348,   349,   350,
     351,   352,   353,   354,   355,   356,   357,   358,   359,   360,
     361,   362,   363,   364,   365,   366,   367,   368,   369
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || YYTOKEN_TABLE
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "module", "number", "token", "endmodule",
  "assign", "input", "output", "inout", "reg", "wire", "tri0", "tri1",
  "signed", "event", "bin", "hex", "dig", "integer", "real", "wreal",
  "ubin", "uhex", "udig", "domino", "and_and", "or_or", "eq3", "eq_eq",
  "not_eq", "gr_eq", "sm_eq", "always", "begin", "end", "if", "else",
  "posedge", "negedge", "or", "wait", "emit", "string", "defparam",
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
     345,   346,   347,   348,   349,   350,    63,    58,   124,    94,
      38,   351,   352,   353,   354,    60,    62,    43,    45,   355,
     356,    42,    47,    37,   357,   358,    35,    40,    41,    59,
      44,    61,    46,    64,    91,    93,   123,   125,    33,   126
};
# endif

/* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint8 yyr1[] =
{
       0,   130,   131,   132,   132,   133,   133,   134,   135,   135,
     135,   136,   136,   136,   137,   137,   138,   138,   138,   138,
     138,   138,   138,   138,   139,   139,   140,   140,   140,   140,
     140,   140,   140,   140,   140,   140,   140,   140,   140,   140,
     141,   141,   141,   141,   142,   143,   143,   143,   143,   143,
     143,   143,   143,   143,   143,   143,   143,   143,   143,   143,
     144,   144,   144,   144,   145,   146,   146,   146,   146,   146,
     146,   146,   146,   147,   147,   148,   148,   148,   148,   148,
     148,   148,   148,   148,   149,   149,   149,   149,   150,   150,
     151,   151,   151,   151,   151,   151,   151,   151,   151,   151,
     151,   151,   151,   152,   152,   152,   152,   152,   153,   153,
     153,   154,   155,   156,   156,   157,   157,   158,   159,   159,
     160,   160,   160,   161,   161,   161,   161,   161,   161,   161,
     161,   161,   161,   161,   162,   162,   163,   163,   163,   164,
     164,   164,   164,   165,   165,   166,   166,   167,   167,   167,
     167,   167,   167,   168,   168,   169,   170,   170,   171,   171,
     171,   171,   171,   171,   171,   171,   171,   171,   171,   171,
     171,   171,   172,   173,   173,   173,   173,   174,   174,   175,
     175,   176,   176,   176,   177,   177,   177,   177,   177,   177,
     177,   177,   177,   177,   177,   177,   177,   177,   177,   177,
     177,   177,   177,   177,   177,   177,   177,   177,   177,   177,
     177,   177,   177,   177,   177,   177,   177,   177,   177,   177,
     177,   177,   177,   178,   179,   180,   181,   181,   182,   183,
     183,   184,   184,   185,   185,   186,   186,   187,   187,   188,
     188,   188,   188,   188,   188,   188,   189,   189,   190,   190,
     190,   191,   192,   192,   192,   192,   192,   192,   192,   192,
     192,   192,   193,   193,   193,   193,   193,   193,   193,   193,
     193,   193,   193,   193,   194,   195,   195,   196,   196,   196,
     197,   197,   197,   197,   197,   198,   198,   198,   198,   198,
     198,   198,   198,   198,   199,   199,   199,   199,   199,   199,
     199,   199,   199,   199,   199,   199,   199,   199,   199,   199,
     199,   199,   199,   199,   199,   199,   199,   199,   199,   199,
     199,   199,   199,   199,   199,   199,   199,   199,   199,   199,
     199,   199,   199,   199,   199,   199,   199,   199,   199,   199,
     199,   199,   199,   199,   199,   199,   199,   199,   199
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
       6,     7,     8,     7,     3,     1,     2,     5,     4,     4,
       2,     2,     2,     3,     1,     5,     2,     4,     2,     2,
       2,     4,     3,     2,     3,     3,     2,     1,     3,     5,
       3,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       5,     7,     9,     2,     2,     2,     4,     1,     1,     3,
       1,     2,     2,     1,     3,     2,     2,     5,     3,     4,
       5,     4,     5,     5,     7,     3,     3,     3,     4,     3,
       5,     2,     3,     3,     4,     5,     6,     7,     6,     6,
       7,     6,     7,     3,     3,     2,     1,     1,     1,     2,
       1,     5,     3,     9,     5,     5,     3,     1,     3,     2,
       1,     3,     3,     3,     3,     3,     1,     2,     1,     1,
       2,     3,     3,     2,     1,     1,     3,     1,     5,     5,
       5,     3,     1,     1,     1,     2,     2,     2,     2,     2,
       2,     3,     1,     1,     1,     1,     1,     2,     2,     1,
       1,     1,     1,     1,     3,     3,     1,     2,     1,     2,
       3,     3,     4,     4,     6,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       4,     1,     1,     1,     1,     1,     1,     2,     3,     3,
       2,     5,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     4,     3,     1,
       2,     2,     2,     2,     2,     2,     2,     2,     2
};

/* YYDEFACT[STATE-NAME] -- Default rule to reduce with in state
   STATE-NUM when YYTABLE doesn't specify something else to do.  Zero
   means the default is an error.  */
static const yytype_uint16 yydefact[] =
{
       0,     0,     0,     0,     2,     4,     5,     6,    10,     0,
      41,    40,     1,     3,     0,     0,     0,   296,   294,   301,
     302,   303,   304,   305,   306,   298,   299,   297,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   339,
     295,    42,     0,     0,    11,    25,     0,     0,     0,     0,
     307,   310,     0,   344,   346,   345,   341,   343,   342,   340,
       0,     0,     0,   276,   278,   347,   348,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     9,     0,   119,    21,   252,
     253,   254,     0,     0,    15,     0,     0,     0,   262,   263,
     272,   273,   264,     0,   265,   266,     0,     0,     0,     0,
       0,     0,     0,     0,    38,     0,   269,   270,   271,    39,
       0,    25,    37,    34,    26,    27,    35,    36,    31,    32,
      33,    28,    29,    30,     0,     0,     0,     0,   236,   281,
     280,     0,   308,   309,     0,   338,   279,     0,   274,   277,
     323,   324,   329,   328,   330,   332,   333,   322,   325,   326,
     327,     0,   318,   317,   319,   336,   335,   334,   320,   321,
     312,   314,   331,   313,   315,   316,     0,     0,     0,     0,
       8,     0,   256,   259,   255,   257,   260,   258,    13,     0,
       0,    16,     0,     0,     0,     0,     0,     0,   239,     0,
       0,     0,     0,     0,   227,     0,   245,   244,   267,   268,
     247,     0,   239,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   220,     0,
       0,     0,     0,     0,     0,     0,   153,   216,   217,   218,
       0,   244,     0,     0,     0,   114,     0,     0,     0,     0,
       0,   116,     0,     0,     0,     0,    44,     0,    74,     0,
      73,     0,     0,     0,     0,   269,   169,   161,   162,   163,
     164,   165,   166,   168,     0,   157,   167,     7,    24,     0,
       0,   247,     0,     0,     0,    43,   337,     0,     0,   282,
     283,     0,     0,     0,   251,   300,   275,     0,   122,     0,
       0,     0,   118,   261,    12,    14,     0,    18,    17,     0,
       0,   125,     0,     0,   148,   150,   149,     0,     0,   240,
     243,   140,   141,   142,     0,    65,    66,    67,    68,    69,
      70,    71,    72,     0,     0,     0,     0,    60,     0,     0,
       0,    46,     0,   215,     0,     0,     0,     0,   185,     0,
     238,     0,     0,     0,     0,     0,     0,     0,   186,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   175,   174,
     173,     0,   201,   154,     0,     0,   219,     0,     0,   111,
       0,     0,     0,     0,     0,   103,     0,     0,     0,   108,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   155,   156,    45,     0,     0,   247,     0,
      47,     0,   247,     0,     0,   235,     0,     0,     0,     0,
     311,   120,     0,   285,   288,   289,   290,   291,   292,   293,
     287,   286,    22,     0,    19,    20,     0,     0,     0,   135,
       0,     0,     0,   152,     0,     0,   144,     0,     0,     0,
     241,   242,     0,     0,     0,     0,     0,   226,   228,   246,
       0,     0,     0,   197,     0,   196,     0,   184,   237,     0,
     195,   202,     0,     0,     0,     0,     0,   188,   203,     0,
     199,     0,   222,   213,   214,     0,     0,     0,   180,   183,
       0,     0,     0,     0,     0,     0,     0,   113,   112,   117,
     104,     0,   115,   105,     0,   109,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    89,     0,     0,     0,     0,
       0,     0,     0,     0,   158,     0,     0,   160,    49,     0,
      56,     0,    57,     0,     0,     0,    51,   247,     0,   284,
     249,   250,   248,   121,    23,   123,     0,   136,     0,     0,
       0,     0,    59,   146,   151,     0,   147,     0,     0,     0,
     139,     0,     0,     0,     0,   204,     0,     0,   198,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   181,   182,
     177,   176,   178,     0,     0,   191,     0,   189,     0,     0,
     126,   107,   106,   110,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    88,     0,    76,     0,     0,     0,
       0,     0,     0,    85,     0,     0,     0,    50,     0,    48,
       0,    53,     0,    54,     0,   128,   134,   130,     0,     0,
     143,   124,     0,     0,    64,     0,    63,    61,   205,   221,
     187,   193,     0,     0,   230,     0,     0,     0,     0,     0,
     225,   200,   224,   179,   192,   190,   129,   127,     0,     0,
      97,     0,     0,     0,    90,   247,     0,     0,   101,     0,
      91,    92,    75,     0,     0,    79,     0,     0,     0,     0,
      84,   159,   170,     0,    58,    52,     0,   138,     0,   133,
       0,   131,     0,    62,     0,     0,   206,   229,     0,   208,
       0,   209,     0,   211,     0,     0,     0,     0,   100,    98,
       0,     0,     0,    93,     0,   102,     0,    78,     0,     0,
       0,     0,     0,     0,     0,     0,    55,   137,   145,   132,
     194,   234,   233,   207,   232,   231,   210,   212,     0,     0,
      80,    99,     0,    94,    95,     0,     0,    90,     0,   101,
      77,     0,    86,   171,     0,     0,    81,    96,     0,    82,
      93,    87,     0,   223,    83,   172
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,     3,     4,     5,     6,    15,    45,   103,   104,   130,
     131,     7,   276,   277,   278,   211,   343,   269,   136,   137,
     524,   525,   279,   280,   281,   255,   256,   260,   261,    96,
      97,   282,   448,   449,   212,   455,   456,   207,   283,   143,
     284,   285,   286,   265,   593,   497,   498,   360,   247,   248,
     249,   213,   214,   653,   654,   655,   656,   361,   250,   221,
     329,   330,   144,   145,    39,    62,    63,    40,   442,   148
};

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
#define YYPACT_NINF -535
static const yytype_int16 yypact[] =
{
      52,    70,    59,    81,    52,  -535,  -535,  -535,   -28,   116,
    1764,  -535,  -535,  -535,    25,   142,    68,  -535,   -35,  -535,
    -535,  -535,  -535,  -535,  -535,  -535,    84,  -535,  1764,  1764,
    1764,  1764,  1764,  1764,  1764,  1764,  1400,  1764,  1764,  -535,
    -535,  5114,    51,    23,  -535,  4782,   125,  1764,   204,  1764,
    -535,    98,  1764,  -535,  -535,  -535,  -535,  -535,  -535,  -535,
    4007,   105,   -49,  -535,  2624,  -535,  -535,  1764,  1764,  1764,
    1764,  1764,  1764,  1764,  1764,  1764,  1764,  1764,  1764,  1764,
    1764,  1764,  1764,  1764,  1764,  1764,  1764,  1764,  1764,  1764,
    1764,  1764,  1764,   120,    41,  -535,   161,  -535,  -535,   231,
     171,   164,   130,   172,  -535,    33,    40,    17,   240,   245,
    -535,  -535,  -535,   261,  -535,  -535,  2585,    55,   277,    35,
      42,  2585,    37,   289,  -535,  4994,  -535,  -535,  -535,  -535,
     296,  4782,  -535,  -535,  -535,  -535,  -535,  -535,  -535,  -535,
    -535,  -535,  -535,  -535,    43,    44,   306,   181,  5114,    82,
    -535,  2663,  -535,  -535,  4045,  -535,  -535,  1400,  -535,  -535,
    5081,   569,   -19,   -19,   -19,   465,   465,  -535,  1090,  1090,
    1090,  5027,  5168,  1090,   308,   826,   826,   826,   465,   465,
     514,   514,   -19,  -535,  -535,  -535,  1764,   157,  1764,   310,
    -535,    21,  -535,  -535,   303,  -535,  -535,  -535,  -535,   214,
     230,   225,   348,    46,    99,   352,    10,   361,   183,    31,
     305,    20,    12,   155,  -535,   229,  -535,  -535,  -535,  -535,
     249,   288,   -45,    12,    43,   261,  2042,   263,  1764,   405,
     270,   300,   309,  2585,   312,   328,  2585,   418,  -535,  1764,
    1764,   360,   427,  1764,    97,  2101,  -535,  -535,  -535,  -535,
      -9,   365,   371,  1764,   337,  -535,   167,   358,   369,    42,
     208,  -535,    42,   242,    42,   379,  -535,   189,  -535,   500,
     384,   207,  3974,   396,   403,   522,  -535,  -535,  -535,  -535,
    -535,  -535,  -535,  -535,  4799,  -535,  -535,  -535,  -535,   409,
     261,   -55,   524,   213,    47,  -535,  -535,  1764,  1764,  -535,
    -535,  1764,  1764,  1764,  -535,  -535,  -535,  1764,  5114,  1764,
    4992,   413,  -535,  -535,  -535,  -535,   209,  -535,   152,   525,
     885,  -535,   421,   530,  -535,  -535,  -535,   901,    95,  -535,
      98,  -535,  -535,  -535,  1764,  -535,  -535,  -535,  -535,  -535,
    -535,  -535,  -535,   420,    12,   428,   430,  -535,    12,  1764,
     261,  -535,  1468,  -535,   432,   422,   261,   423,  -535,   549,
    -535,  2162,  1764,  2893,   437,  1764,  1764,  1764,  -535,    12,
    1764,  2221,   438,  2865,  2986,  1764,   439,  1868,  -535,  -535,
    -535,  1037,  -535,  -535,  1518,  1518,  -535,  1586,   227,  -535,
     277,  1764,  1764,   317,   554,  -535,   554,   342,   554,  -535,
     345,   554,   230,  1981,   232,   555,   230,  1981,   556,  4888,
    1764,    12,   444,  -535,  -535,  -535,   -20,   445,   347,   446,
    -535,  1764,   147,   447,   563,  5114,  4137,   411,  2750,  2778,
    5114,  5114,  1764,  -535,  -535,  -535,  -535,  -535,  -535,  -535,
    -535,  -535,  -535,   209,  -535,  -535,   450,    11,   234,  -535,
     238,   449,   455,  -535,   574,   247,  -535,   268,   -22,   463,
    -535,  -535,   272,   305,   460,  1764,  1764,  -535,  5114,  -535,
     464,   273,  1764,  -535,   466,  -535,  2585,  -535,  -535,  4170,
    -535,  -535,  4262,  4295,  4387,   350,  4420,  -535,  -535,  1764,
    -535,  4512,  -535,  -535,  -535,  1764,  1764,    -2,  -535,  5114,
    1764,  3014,  1764,  3107,   276,   279,   467,  -535,  5114,  5114,
    -535,   353,  -535,  -535,   355,  -535,   362,   280,    38,   571,
      43,   261,   261,   261,  1981,  -535,  2282,   230,  1981,   468,
     285,  1981,   526,  4994,  -535,  4545,   367,  -535,  -535,   469,
    -535,  1764,  -535,  3135,  1764,   470,  -535,   382,   472,  -535,
    -535,  -535,  -535,  5114,  -535,  -535,   488,  -535,   487,   449,
     489,   286,  -535,   490,  -535,   491,  -535,   496,   304,   449,
    -535,   498,  1764,  3228,  3256,  -535,   499,  3349,  -535,  2343,
    2585,  1636,  1764,  1764,  1764,  2585,  3377,  2585,  5114,  5114,
    -535,  -535,  -535,  1037,  3470,  -535,  3498,  -535,   502,   503,
    -535,  -535,  -535,  -535,   504,   261,    79,   384,   384,   509,
      49,    96,   511,   512,  -535,  2402,  -535,   307,  1981,   576,
     243,   515,   561,  -535,  4941,  4994,  1764,  -535,  3591,  -535,
    3619,  -535,  1764,  -535,  1714,  -535,  -535,  -535,   516,  1764,
    -535,  -535,   517,   315,  -535,  3712,  -535,  -535,  -535,  -535,
    -535,   595,   540,  1213,  -535,   587,   -36,  1263,  1350,  3740,
    -535,  -535,  -535,  -535,  -535,  -535,  -535,  -535,  1981,   527,
    -535,   528,   261,   384,   390,   -55,   529,   638,   393,   532,
    -535,  -535,  -535,   533,   588,  -535,    43,   261,  1981,  1981,
    -535,  -535,   607,  3833,  -535,  -535,  3861,  -535,  4637,  -535,
    4670,  -535,   534,  -535,  2585,  2463,  -535,  -535,   603,  -535,
    2524,  -535,   604,  -535,   609,    12,  1981,   602,  -535,  -535,
     544,   659,   550,   394,   551,  -535,  1981,  -535,   564,    49,
     118,   629,  1981,   628,  4994,    12,  -535,  -535,  -535,  -535,
    -535,  -535,  -535,  -535,  -535,  -535,  -535,  -535,   336,   632,
    -535,  -535,   570,  -535,  -535,  1981,   634,  -535,   572,  -535,
    -535,   635,  -535,  -535,   340,  2585,  -535,  -535,   639,  -535,
    -535,  -535,  4994,  -535,  -535,  -535
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -535,  -535,  -535,   690,  -535,  -535,  -535,  -383,   497,   565,
    -535,   -18,   -16,   -11,    50,  -535,   235,  -535,  -535,  -535,
    -396,  -511,    53,    56,    64,   313,  -535,  -110,   314,  -535,
     508,    65,  -375,   141,  -193,  -535,   137,   560,    69,  -535,
    -263,  -281,  -535,   590,  -535,  -535,   115,    24,  -535,  -535,
    -535,  -367,   363,   -57,  -534,  -428,   -17,  -229,   -86,  -139,
     -14,   -10,   -42,  -535,    86,  -535,   552,   -48,   271,   794
};

/* YYTABLE[YYPACT[STATE-NUM]].  What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule which
   number is the opposite.  If zero, do what YYDEFACT says.
   If YYTABLE_NINF, syntax error.  */
#define YYTABLE_NINF -199
static const yytype_int16 yytable[] =
{
     150,   105,   485,   414,    50,   289,   293,   371,    51,   409,
     263,   531,   504,   614,   324,   325,   556,   208,   344,   517,
     614,   215,   208,   530,   384,   208,    93,   132,    98,   133,
     147,    99,   100,   101,   134,   331,   332,   152,   201,   590,
     258,   153,   267,   220,   536,   204,   187,   258,   220,   291,
     259,   318,   422,   202,   675,     1,    93,   268,   605,   217,
     252,   710,    74,     9,    10,   350,   205,    94,   251,   188,
     257,   157,   352,   251,   353,     8,   561,    48,   158,    49,
     189,    12,    47,   568,   297,   355,   357,    48,    14,    49,
     326,   203,    90,    91,    92,   135,   567,    94,   138,   538,
     447,   139,   378,    11,   188,   262,   264,   614,   270,   140,
     141,   333,   385,   132,   142,   133,   591,     2,   592,   707,
     134,    16,   557,   707,   707,   345,   346,   327,   414,   146,
     290,   294,   618,   209,   210,   299,   209,   354,    36,   300,
     246,   102,    42,    36,   617,   266,    36,   156,   334,   393,
     159,   416,   397,   419,   400,   423,   206,   188,   105,   188,
     206,   188,   188,   217,   217,   188,   188,   188,   188,    95,
     188,   188,   253,   188,   526,   217,   197,   614,   251,   379,
      46,   135,   194,   195,   138,   251,   196,   139,   251,   319,
     322,   500,   502,   216,   643,   140,   141,   251,   670,   298,
     142,    52,   216,   188,    48,   614,    49,   216,   380,   149,
     356,   469,   458,   433,   381,   678,   320,   474,   321,   188,
     188,   614,    49,   188,   688,   708,   434,   435,   436,   712,
     714,    36,   437,   438,   439,    98,   388,   759,    99,   100,
     101,   186,   188,   192,   614,   394,   193,   579,   398,   198,
     401,   518,   519,   440,   686,   218,   405,   368,   464,    43,
     219,    44,   215,   687,   522,   523,   220,   350,   544,   383,
     624,   188,   716,   443,   347,   348,   188,   417,   309,   190,
     424,   191,   254,   215,   511,   548,   389,   390,   514,   441,
     199,   516,   200,   732,   271,   615,   217,   216,   216,   296,
     217,   297,   287,   450,   444,    48,   402,    49,   403,   216,
     457,   295,   216,   251,   459,   311,   460,   462,   313,   216,
     461,   217,   216,   251,   406,   215,   407,   395,   396,   251,
     755,   216,   420,   314,   421,   471,    68,    69,    70,    71,
      72,    73,   257,   414,   692,   506,   316,   297,   748,   527,
     349,   528,   558,   317,   559,   251,   560,   323,   297,   251,
     105,   399,   396,   217,   105,   564,   328,   565,   764,   350,
     505,   335,   336,   337,   338,   339,   340,   341,   342,   606,
     362,   609,   611,   612,   613,   478,   566,   365,   297,    74,
     570,   576,   297,   297,   598,   478,   559,   599,   604,   297,
     200,   494,   539,   621,   638,   200,   559,   351,   545,    82,
     364,    83,    84,    85,    86,    87,    88,   366,    89,    90,
      91,    92,   642,   372,   559,   683,   367,   200,   251,   369,
     216,   532,   376,   702,   216,   559,   510,   396,    67,    68,
      69,    70,    71,    72,    73,   370,  -197,   216,  -197,  -196,
    -198,  -196,  -198,   763,   765,   216,   348,   216,   772,    48,
     348,   513,   396,   216,   515,   396,   669,   350,   541,   584,
     348,   676,   601,   396,   602,   396,   251,   375,   251,   391,
     251,   603,   396,   251,   386,   105,   626,   348,   387,   216,
     392,   775,    74,   216,    69,    70,    71,   216,   382,    75,
      76,    77,   350,   632,   607,   404,   610,    78,   188,    79,
      80,    81,    82,   410,    83,    84,    85,    86,    87,    88,
     411,    89,    90,    91,    92,   657,   658,   412,   415,   418,
     445,   251,   251,   720,   432,   452,   550,   251,   451,   251,
     463,   473,   475,    69,    70,    71,    74,   728,   730,   465,
     478,   466,   619,   472,   476,   622,   481,   488,   492,   258,
     529,   533,   216,   537,   540,   542,   546,   251,   547,   555,
     251,   447,    87,    88,   562,    89,    90,    91,    92,   563,
     569,   572,   608,   575,   623,   578,   600,   620,   627,   631,
     758,   633,   671,   672,   673,    74,   677,   679,    69,    70,
      71,    72,    73,   478,   651,   634,   635,   639,   637,   660,
     216,   662,   216,   454,   216,   641,   644,   216,   648,   690,
     251,   666,   667,   668,    89,    90,    91,    92,   674,   215,
     680,   681,   685,   704,   689,   699,   701,   705,   709,   478,
     251,   251,   684,   724,   727,   734,   718,   719,   723,   215,
      74,   725,   726,   739,   743,   746,   251,   251,   750,   721,
     747,   722,   251,   751,   752,   216,   216,   217,   251,   753,
     754,   216,   729,   216,    85,    86,    87,    88,   251,    89,
      90,    91,    92,   757,   251,   760,   762,   217,   766,   767,
     769,   770,   717,   771,    13,   774,   288,   315,   571,   312,
     636,   216,   640,   507,   216,   292,   245,   251,   663,   306,
     512,   467,   731,   733,   554,   677,   679,   251,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   740,   742,
       0,     0,     0,     0,   745,     0,     0,     0,     0,     0,
     749,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     756,     0,     0,     0,   216,     0,   761,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   216,   216,     0,     0,     0,   768,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   773,
     216,   216,     0,     0,     0,     0,   216,     0,     0,     0,
       0,   216,   216,     0,    41,     0,     0,     0,     0,     0,
       0,     0,   216,     0,     0,     0,     0,     0,   216,     0,
       0,   216,    53,    54,    55,    56,    57,    58,    59,    60,
      64,    65,    66,     0,     0,     0,     0,     0,     0,     0,
       0,   216,     0,   151,     0,     0,   154,     0,     0,     0,
       0,   216,     0,     0,    68,    69,    70,    71,    72,    73,
       0,   160,   161,   162,   163,   164,   165,   166,   167,   168,
     169,   170,   171,   172,   173,   174,   175,   176,   177,   178,
     179,   180,   181,   182,   183,   184,   185,     0,     0,    17,
      18,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    19,    20,    21,    17,    18,    74,    22,    23,
      24,     0,     0,     0,     0,     0,     0,     0,    19,    20,
      21,     0,     0,     0,    22,    23,    24,     0,     0,    25,
       0,    85,    86,    87,    88,     0,    89,    90,    91,    92,
       0,     0,     0,     0,     0,    25,     0,     0,     0,     0,
      26,    64,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    27,    26,     0,     0,     0,
       0,     0,     0,    28,    29,    30,     0,     0,     0,     0,
     308,    27,   310,    31,    32,    33,     0,     0,     0,    28,
      29,    30,     0,    34,     0,     0,     0,     0,     0,    31,
      32,    33,    35,   446,     0,     0,     0,   447,     0,    34,
       0,    36,     0,    37,    38,     0,     0,     0,    35,   453,
       0,     0,   363,   454,     0,     0,     0,    36,     0,    37,
      38,     0,     0,   373,   374,     0,     0,   377,     0,     0,
       0,    17,    18,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    19,    20,    21,     0,     0,     0,
      22,    23,    24,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   495,   496,     0,     0,
       0,    25,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   425,   426,     0,     0,   427,   428,   429,     0,     0,
       0,   430,    26,   431,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    27,    68,    69,
      70,    71,    72,    73,     0,    28,    29,    30,     0,     0,
       0,     0,     0,     0,     0,    31,    32,    33,     0,     0,
       0,     0,     0,   468,     0,    34,     0,     0,     0,     0,
       0,     0,     0,     0,    35,     0,   479,     0,     0,   482,
     483,   484,     0,    36,   486,    37,    38,     0,     0,   491,
       0,    74,     0,     0,     0,   499,     0,     0,   501,   503,
       0,     0,     0,     0,     0,   508,   509,     0,     0,     0,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,   535,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   543,     0,    17,    18,     0,
       0,     0,     0,     0,     0,     0,   553,     0,     0,     0,
      19,    20,    21,     0,     0,     0,    22,    23,    24,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    25,     0,   573,
     574,     0,     0,     0,   706,   652,   577,    17,    18,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    26,     0,
      19,    20,    21,   586,     0,     0,    22,    23,    24,   588,
     589,     0,     0,    27,   594,     0,   596,     0,     0,     0,
       0,    28,    29,    30,     0,     0,     0,    25,     0,     0,
       0,    31,    32,    33,   711,   652,     0,     0,     0,     0,
       0,    34,     0,     0,     0,     0,     0,     0,    26,     0,
      35,     0,     0,     0,     0,   628,     0,     0,   630,    36,
       0,    37,    38,    27,     0,     0,     0,     0,     0,     0,
       0,    28,    29,    30,    17,    18,     0,     0,     0,     0,
       0,    31,    32,    33,     0,     0,   645,    19,    20,    21,
       0,    34,     0,    22,    23,    24,     0,     0,   659,     0,
      35,     0,     0,     0,     0,     0,     0,   499,     0,    36,
       0,    37,    38,     0,    25,     0,     0,     0,     0,     0,
       0,   713,   652,     0,    17,    18,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    26,     0,    19,    20,    21,
     693,     0,     0,    22,    23,    24,   696,     0,   698,     0,
      27,     0,     0,   700,     0,     0,     0,     0,    28,    29,
      30,     0,     0,     0,    25,     0,     0,     0,    31,    32,
      33,     0,     0,     0,     0,     0,     0,     0,    34,     0,
       0,     0,     0,     0,     0,    26,     0,    35,     0,     0,
       0,     0,    17,    18,     0,     0,    36,     0,    37,    38,
      27,     0,     0,     0,     0,    19,    20,    21,    28,    29,
      30,    22,    23,    24,     0,     0,     0,     0,    31,    32,
      33,     0,     0,     0,    61,     0,     0,     0,    34,     0,
       0,     0,    25,     0,     0,     0,     0,    35,     0,     0,
       0,     0,    17,    18,     0,     0,    36,     0,    37,    38,
       0,     0,     0,    26,     0,    19,    20,    21,     0,     0,
       0,    22,    23,    24,     0,     0,     0,     0,    27,     0,
       0,     0,     0,     0,     0,     0,    28,    29,    30,     0,
       0,     0,    25,     0,     0,     0,    31,    32,    33,     0,
       0,     0,     0,     0,     0,     0,    34,     0,     0,     0,
       0,     0,     0,    26,     0,    35,   470,     0,     0,     0,
      17,    18,     0,     0,    36,     0,    37,    38,    27,     0,
       0,     0,     0,    19,    20,    21,    28,    29,    30,    22,
      23,    24,     0,     0,     0,     0,    31,    32,    33,     0,
       0,     0,     0,     0,     0,     0,    34,     0,     0,     0,
      25,     0,     0,     0,   209,    35,     0,     0,     0,     0,
      17,    18,     0,     0,    36,     0,    37,    38,     0,     0,
       0,    26,     0,    19,    20,    21,     0,     0,     0,    22,
      23,    24,     0,     0,     0,     0,    27,     0,     0,     0,
       0,     0,     0,     0,    28,    29,    30,     0,     0,     0,
      25,     0,     0,     0,    31,    32,    33,     0,   652,     0,
       0,     0,     0,     0,    34,     0,     0,     0,     0,     0,
       0,    26,     0,    35,     0,     0,     0,     0,   447,     0,
       0,     0,    36,     0,    37,    38,    27,     0,    17,    18,
       0,     0,     0,     0,    28,    29,    30,     0,     0,     0,
       0,    19,    20,    21,    31,    32,    33,    22,    23,    24,
       0,     0,     0,     0,    34,     0,     0,     0,     0,     0,
       0,     0,     0,    35,     0,     0,     0,     0,    25,     0,
       0,     0,    36,     0,    37,    38,     0,     0,    17,    18,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    26,
       0,    19,    20,    21,     0,     0,     0,    22,    23,    24,
       0,     0,     0,     0,    27,     0,     0,     0,     0,     0,
       0,     0,    28,    29,    30,     0,     0,     0,    25,     0,
       0,     0,    31,    32,    33,     0,     0,     0,     0,     0,
       0,     0,    34,     0,     0,     0,     0,     0,     0,    26,
       0,    35,   697,     0,     0,     0,     0,     0,     0,     0,
      36,     0,    37,    38,    27,     0,     0,     0,     0,     0,
       0,     0,    28,    29,    30,     0,     0,     0,     0,     0,
       0,     0,    31,    32,    33,     0,     0,     0,     0,     0,
       0,     0,    34,   222,     0,   223,     0,     0,     0,   224,
       0,    35,     0,     0,     0,     0,     0,     0,   225,     0,
      36,     0,    37,    38,     0,    67,    68,    69,    70,    71,
      72,    73,     0,   226,     0,   227,     0,     0,     0,     0,
     228,   229,     0,     0,     0,     0,   230,   231,   232,     0,
       0,     0,   233,     0,     0,     0,     0,   234,   235,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   236,     0,   237,   238,     0,     0,     0,    74,
       0,     0,     0,     0,   239,   240,    75,    76,    77,   241,
       0,     0,     0,   242,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,     0,     0,   243,     0,   222,   493,   223,   518,
     519,   244,   520,     0,    36,     0,     0,     0,     0,     0,
       0,   521,   522,   523,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   226,     0,   227,     0,
       0,     0,     0,   228,   229,     0,     0,     0,     0,   230,
     231,   232,     0,     0,     0,   233,     0,     0,     0,     0,
     234,   235,     0,     0,     0,     0,     0,   222,     0,   223,
       0,     0,     0,   224,     0,   236,     0,   237,   238,     0,
       0,     0,   225,     0,     0,     0,     0,   239,   240,     0,
       0,     0,   241,     0,     0,     0,   242,   226,   358,   227,
       0,     0,     0,     0,   228,   229,     0,     0,     0,     0,
     230,   231,   232,     0,     0,     0,   233,   243,     0,     0,
       0,   234,   235,     0,   244,     0,   222,    36,   223,     0,
       0,     0,   224,     0,     0,     0,   236,     0,   237,   238,
       0,   225,     0,     0,     0,     0,     0,     0,   239,   240,
       0,     0,     0,   241,     0,     0,   226,   242,   227,   359,
       0,     0,     0,   228,   229,     0,     0,     0,     0,   230,
     231,   232,     0,     0,     0,   233,     0,     0,   243,     0,
     234,   235,     0,     0,     0,   244,     0,   222,    36,   223,
       0,     0,     0,   224,     0,   236,     0,   237,   238,     0,
       0,     0,   225,     0,     0,     0,     0,   239,   240,     0,
       0,     0,   241,     0,     0,     0,   242,   226,   477,   227,
       0,     0,     0,     0,   228,   229,     0,     0,     0,     0,
     230,   231,   232,     0,     0,     0,   233,   243,     0,     0,
     382,   234,   235,     0,   244,     0,   222,    36,   223,     0,
       0,     0,   224,     0,     0,     0,   236,     0,   237,   238,
       0,   225,     0,     0,     0,     0,     0,     0,   239,   240,
       0,     0,     0,   241,     0,     0,   226,   242,   227,     0,
       0,     0,     0,   228,   229,     0,     0,     0,     0,   230,
     231,   232,     0,     0,     0,   233,     0,     0,   243,     0,
     234,   235,     0,     0,     0,   244,     0,   222,    36,   223,
       0,     0,     0,   224,     0,   236,   487,   237,   238,     0,
       0,     0,   225,     0,     0,     0,     0,   239,   240,     0,
       0,     0,   241,     0,     0,     0,   242,   226,     0,   227,
       0,     0,     0,     0,   228,   229,     0,     0,     0,     0,
     230,   231,   232,     0,     0,     0,   233,   243,   616,     0,
       0,   234,   235,     0,   244,     0,     0,    36,   222,     0,
     223,     0,     0,     0,   224,     0,   236,     0,   237,   238,
       0,     0,     0,   225,     0,     0,     0,     0,   239,   240,
       0,     0,     0,   241,     0,     0,     0,   242,   226,   650,
     227,     0,     0,     0,     0,   228,   229,     0,     0,     0,
       0,   230,   231,   232,     0,     0,     0,   233,   243,     0,
       0,     0,   234,   235,     0,   244,     0,   222,    36,   223,
       0,     0,     0,   224,     0,     0,     0,   236,     0,   237,
     238,     0,   225,     0,     0,     0,     0,     0,     0,   239,
     240,     0,     0,     0,   241,     0,     0,   226,   242,   227,
       0,     0,     0,     0,   228,   229,     0,     0,     0,     0,
     230,   231,   232,     0,     0,     0,   233,     0,   682,   243,
       0,   234,   235,     0,     0,     0,   244,     0,   222,    36,
     223,     0,     0,     0,   224,     0,   236,     0,   237,   238,
       0,     0,     0,   225,     0,     0,     0,     0,   239,   240,
       0,     0,     0,   241,     0,     0,     0,   242,   226,     0,
     227,     0,     0,     0,     0,   228,   229,     0,     0,     0,
       0,   230,   231,   232,     0,     0,     0,   233,   243,     0,
       0,     0,   234,   235,     0,   244,     0,     0,    36,   222,
       0,   223,     0,     0,     0,   224,     0,   236,     0,   237,
     238,     0,     0,     0,   225,     0,     0,     0,     0,   239,
     240,     0,     0,     0,   241,     0,     0,     0,   242,   226,
       0,   227,     0,     0,     0,     0,   228,   229,     0,     0,
       0,     0,   230,   231,   232,     0,     0,     0,   233,   243,
       0,     0,   741,   234,   235,     0,   244,     0,     0,    36,
     222,     0,   223,     0,     0,     0,   224,     0,   236,     0,
     237,   238,     0,     0,     0,   225,     0,     0,     0,     0,
     239,   240,     0,     0,     0,   241,     0,     0,     0,   242,
     226,     0,   227,     0,     0,     0,     0,   228,   229,     0,
       0,     0,     0,   230,   231,   232,     0,     0,     0,   233,
     243,     0,     0,   744,   234,   235,     0,   244,     0,     0,
      36,    67,    68,    69,    70,    71,    72,    73,     0,   236,
       0,   237,   238,     0,     0,     0,     0,     0,     0,     0,
       0,   239,   240,     0,     0,     0,   241,     0,     0,     0,
     242,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,   243,     0,     0,     0,    74,     0,     0,   244,     0,
       0,    36,    75,    76,    77,     0,     0,     0,     0,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,     0,     0,
       0,   301,   302,     0,    74,     0,     0,     0,     0,     0,
      36,    75,    76,    77,     0,     0,     0,     0,     0,    78,
     303,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,   304,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    67,    68,    69,    70,    71,
      72,    73,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    74,     0,     0,     0,     0,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,    74,
      89,    90,    91,    92,     0,     0,    75,    76,    77,     0,
       0,     0,     0,     0,    78,   551,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,   552,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    74,     0,     0,     0,
       0,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,    74,    89,    90,    91,    92,     0,
       0,    75,    76,    77,     0,     0,   489,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,     0,
       0,     0,   480,    67,    68,    69,    70,    71,    72,    73,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    74,     0,     0,
       0,     0,     0,     0,    75,    76,    77,     0,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,    74,    89,    90,    91,    92,
       0,     0,    75,    76,    77,   490,     0,     0,     0,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,     0,     0,
       0,     0,     0,   595,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,    74,    89,    90,    91,
      92,     0,     0,    75,    76,    77,   597,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,     0,   629,    67,    68,    69,    70,    71,
      72,    73,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    67,    68,    69,    70,    71,    72,    73,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    74,
       0,     0,     0,     0,     0,     0,    75,    76,    77,     0,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,    74,    89,    90,
      91,    92,     0,     0,    75,    76,    77,   646,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
       0,     0,     0,     0,     0,   647,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      74,     0,     0,     0,     0,     0,     0,    75,    76,    77,
       0,     0,     0,     0,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,    74,    89,
      90,    91,    92,     0,     0,    75,    76,    77,   649,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,     0,     0,     0,     0,     0,   661,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    67,    68,    69,    70,    71,
      72,    73,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    74,     0,     0,     0,     0,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,    74,
      89,    90,    91,    92,     0,     0,    75,    76,    77,   664,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,     0,     0,     0,     0,     0,   665,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    74,     0,     0,     0,     0,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
      74,    89,    90,    91,    92,     0,     0,    75,    76,    77,
     694,     0,     0,     0,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,     0,     0,     0,     0,     0,   695,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,    74,    89,    90,    91,    92,     0,     0,    75,    76,
      77,   703,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,     0,   715,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    67,    68,
      69,    70,    71,    72,    73,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    74,     0,     0,     0,     0,     0,
       0,    75,    76,    77,     0,     0,     0,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,    74,    89,    90,    91,    92,     0,     0,    75,
      76,    77,   735,     0,     0,     0,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,     0,     0,     0,     0,   106,
     736,   107,    99,   100,   101,   108,   109,   110,   111,   112,
     113,     0,     0,     0,   114,   115,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   116,   272,
       0,   273,     0,     0,     0,   117,     0,     0,     0,   118,
     119,   120,     0,     0,     0,     0,     0,   121,     0,     0,
       0,     0,     0,   274,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   275,
       0,     0,     0,     0,     0,     0,   127,   128,     0,     0,
       0,   408,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,     0,     0,     0,     0,   155,    74,     0,     0,     0,
       0,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,   305,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,    74,     0,     0,     0,   549,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,   580,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,    74,     0,     0,     0,
     581,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,   582,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,    74,     0,     0,     0,   583,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,   585,    67,
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
       0,     0,     0,   625,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,    74,     0,     0,     0,   737,     0,     0,    75,    76,
      77,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,   106,   738,   107,
      99,   100,   101,   108,   109,   110,   111,   112,   113,     0,
       0,     0,   114,   115,   106,     0,   107,    99,   100,   101,
     108,   109,   110,   111,   112,   113,   116,     0,     0,   114,
     115,     0,     0,   117,     0,     0,     0,   118,   119,   120,
       0,     0,     0,   116,   272,   121,   273,   122,     0,   123,
     117,     0,     0,     0,   118,   119,   120,     2,     0,     0,
       0,     0,   121,     0,     0,     0,     0,     0,   274,   124,
       0,     0,     0,     0,     0,   125,     0,   126,     0,     0,
       0,     0,     0,     0,   127,   128,   129,     0,     0,     0,
       0,     0,     0,   413,   275,     0,     0,     0,     0,     0,
       0,   127,   128,   106,     0,   107,    99,   100,   101,   108,
     109,   110,   111,   112,   113,     0,     0,     0,   114,   115,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   116,   272,   534,   273,     0,     0,     0,   117,
       0,     0,     0,   118,   119,   120,     0,     0,     0,     0,
       0,   121,     0,     0,     0,     0,   106,   274,   107,    99,
     100,   101,   108,   109,   110,   111,   112,   113,     0,     0,
       0,   114,   115,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   275,     0,   116,   272,   691,   273,     0,
     127,   128,   117,     0,     0,     0,   118,   119,   120,     0,
       0,     0,     0,     0,   121,     0,     0,     0,     0,   106,
     274,   107,    99,   100,   101,   108,   109,   110,   111,   112,
     113,     0,     0,     0,   114,   115,     0,     0,     0,    67,
      68,    69,    70,    71,    72,    73,   275,     0,   116,   272,
       0,   273,     0,   127,   128,   117,     0,     0,     0,   118,
     119,   120,     0,     0,     0,     0,     0,   121,     0,     0,
       0,     0,     0,   274,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     301,   302,     0,    74,     0,     0,     0,     0,     0,   275,
      75,    76,    77,     0,     0,     0,   127,   128,    78,   303,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,     0,     0,    74,    68,
      69,    70,    71,    72,    73,    75,    76,    77,     0,     0,
       0,     0,     0,    78,   307,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    74,     0,     0,     0,     0,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,     0,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,    74,    68,    69,    70,    71,
      72,    73,    75,    76,    77,     0,     0,     0,     0,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    74,
       0,     0,     0,     0,     0,     0,    75,    76,    77,     0,
       0,     0,     0,     0,     0,     0,     0,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92
};

static const yytype_int16 yycheck[] =
{
      48,    43,   369,   284,    18,   144,   145,   236,    18,   272,
     120,   407,   387,   524,     4,     5,     5,     5,   211,   402,
     531,   107,     5,   406,    33,     5,     5,    45,     5,    45,
      47,     8,     9,    10,    45,     4,     5,    51,     5,    41,
       5,    51,     5,     5,   411,     5,     5,     5,     5,     5,
      15,     5,     5,    20,     5,     3,     5,    20,    20,   107,
       5,    97,    81,     4,     5,   120,    26,    46,   116,   124,
     118,   120,   117,   121,   119,     5,   451,   122,   127,   124,
      94,     0,   117,   458,   120,   224,   225,   122,   116,   124,
      80,   105,   111,   112,   113,    45,   118,    46,    45,   119,
     122,    45,     5,    44,   124,   119,   120,   618,   122,    45,
      45,    80,   121,   131,    45,   131,   118,    65,   120,   653,
     131,     5,   111,   657,   658,   211,   212,   117,   409,     4,
     144,   145,   528,   116,   117,   149,   116,   223,   126,   149,
     116,   118,   117,   126,   527,   121,   126,    61,   117,   259,
      64,   290,   262,   292,   264,   294,   116,   124,   200,   124,
     116,   124,   124,   211,   212,   124,   124,   124,   124,   118,
     124,   124,   117,   124,   403,   223,    12,   688,   226,    82,
     112,   131,    11,    12,   131,   233,    15,   131,   236,   203,
     204,   384,   385,   107,   569,   131,   131,   245,   119,   117,
     131,   117,   116,   124,   122,   716,   124,   121,   111,     5,
     224,   350,   117,     4,   117,   119,   117,   356,   119,   124,
     124,   732,   124,   124,   620,   653,    17,    18,    19,   657,
     658,   126,    23,    24,    25,     5,   253,   119,     8,     9,
      10,   121,   124,    12,   755,   259,    15,   476,   262,   119,
     264,     8,     9,    44,    11,    15,   270,   233,   344,   117,
      15,   119,   348,    20,    21,    22,     5,   120,   121,   245,
     533,   124,   668,   121,   119,   120,   124,   291,   121,   118,
     294,   120,     5,   369,   394,   424,   119,   120,   398,    80,
     118,   401,   120,   689,     5,   524,   344,   211,   212,   118,
     348,   120,     6,   320,   318,   122,   117,   124,   119,   223,
     327,     5,   226,   361,   328,     5,   330,   334,    15,   233,
     330,   369,   236,   371,   117,   411,   119,   119,   120,   377,
     726,   245,   119,   119,   121,   352,    28,    29,    30,    31,
      32,    33,   390,   624,   625,   118,   121,   120,   715,   117,
     121,   119,   118,     5,   120,   403,   118,     5,   120,   407,
     402,   119,   120,   411,   406,   118,     5,   120,   735,   120,
     387,    66,    67,    68,    69,    70,    71,    72,    73,   518,
     117,   520,   521,   522,   523,   361,   118,   117,   120,    81,
     118,   118,   120,   120,   118,   371,   120,   118,   118,   120,
     120,   377,   416,   118,   118,   120,   120,   119,   422,   101,
       5,   103,   104,   105,   106,   107,   108,   117,   110,   111,
     112,   113,   118,     5,   120,   118,   117,   120,   476,   117,
     344,   407,     5,   118,   348,   120,   119,   120,    27,    28,
      29,    30,    31,    32,    33,   117,    56,   361,    58,    56,
      56,    58,    58,   734,   118,   369,   120,   371,   118,   122,
     120,   119,   120,   377,   119,   120,   605,   120,   121,   119,
     120,   610,   119,   120,   119,   120,   524,   117,   526,   121,
     528,   119,   120,   531,   119,   527,   119,   120,   117,   403,
     121,   772,    81,   407,    29,    30,    31,   411,   119,    88,
      89,    90,   120,   121,   518,     5,   520,    96,   124,    98,
      99,   100,   101,   117,   103,   104,   105,   106,   107,   108,
     117,   110,   111,   112,   113,   582,   583,     5,   119,     5,
       5,   579,   580,   672,   121,     5,   125,   585,   117,   587,
     120,   119,   119,    29,    30,    31,    81,   686,   687,   121,
     526,   121,   528,   121,     5,   531,   119,   119,   119,     5,
       5,     5,   476,   119,   119,   119,   119,   615,     5,   119,
     618,   122,   107,   108,   119,   110,   111,   112,   113,     5,
     117,   121,    11,   119,    58,   119,   119,   119,   119,   119,
     729,   119,   606,   607,   608,    81,   610,   611,    29,    30,
      31,    32,    33,   579,   580,   117,   119,   117,   119,   585,
     524,   587,   526,   122,   528,   119,   118,   531,   119,    58,
     668,   119,   119,   119,   110,   111,   112,   113,   119,   715,
     119,   119,    56,    38,   119,   119,   119,    97,    51,   615,
     688,   689,   618,     5,    56,    38,   119,   119,   119,   735,
      81,   119,   119,   119,    51,    51,   704,   705,    56,   673,
      51,   675,   710,   119,     5,   579,   580,   715,   716,   119,
     119,   585,   686,   587,   105,   106,   107,   108,   726,   110,
     111,   112,   113,   119,   732,    56,    58,   735,    56,   119,
      56,   119,   668,    58,     4,    56,   131,   200,   463,   191,
     559,   615,   565,   390,   618,   145,   116,   755,   593,   157,
     396,   348,   688,   689,   443,   729,   730,   765,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   704,   705,
      -1,    -1,    -1,    -1,   710,    -1,    -1,    -1,    -1,    -1,
     716,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     726,    -1,    -1,    -1,   668,    -1,   732,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   688,   689,    -1,    -1,    -1,   755,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   765,
     704,   705,    -1,    -1,    -1,    -1,   710,    -1,    -1,    -1,
      -1,   715,   716,    -1,    10,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   726,    -1,    -1,    -1,    -1,    -1,   732,    -1,
      -1,   735,    28,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   755,    -1,    49,    -1,    -1,    52,    -1,    -1,    -1,
      -1,   765,    -1,    -1,    28,    29,    30,    31,    32,    33,
      -1,    67,    68,    69,    70,    71,    72,    73,    74,    75,
      76,    77,    78,    79,    80,    81,    82,    83,    84,    85,
      86,    87,    88,    89,    90,    91,    92,    -1,    -1,     4,
       5,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    17,    18,    19,     4,     5,    81,    23,    24,
      25,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    17,    18,
      19,    -1,    -1,    -1,    23,    24,    25,    -1,    -1,    44,
      -1,   105,   106,   107,   108,    -1,   110,   111,   112,   113,
      -1,    -1,    -1,    -1,    -1,    44,    -1,    -1,    -1,    -1,
      65,   157,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    80,    65,    -1,    -1,    -1,
      -1,    -1,    -1,    88,    89,    90,    -1,    -1,    -1,    -1,
     186,    80,   188,    98,    99,   100,    -1,    -1,    -1,    88,
      89,    90,    -1,   108,    -1,    -1,    -1,    -1,    -1,    98,
      99,   100,   117,   118,    -1,    -1,    -1,   122,    -1,   108,
      -1,   126,    -1,   128,   129,    -1,    -1,    -1,   117,   118,
      -1,    -1,   228,   122,    -1,    -1,    -1,   126,    -1,   128,
     129,    -1,    -1,   239,   240,    -1,    -1,   243,    -1,    -1,
      -1,     4,     5,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    17,    18,    19,    -1,    -1,    -1,
      23,    24,    25,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    39,    40,    -1,    -1,
      -1,    44,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   297,   298,    -1,    -1,   301,   302,   303,    -1,    -1,
      -1,   307,    65,   309,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    80,    28,    29,
      30,    31,    32,    33,    -1,    88,    89,    90,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    98,    99,   100,    -1,    -1,
      -1,    -1,    -1,   349,    -1,   108,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   117,    -1,   362,    -1,    -1,   365,
     366,   367,    -1,   126,   370,   128,   129,    -1,    -1,   375,
      -1,    81,    -1,    -1,    -1,   381,    -1,    -1,   384,   385,
      -1,    -1,    -1,    -1,    -1,   391,   392,    -1,    -1,    -1,
     100,   101,    -1,   103,   104,   105,   106,   107,   108,    -1,
     110,   111,   112,   113,   410,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   421,    -1,     4,     5,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   432,    -1,    -1,    -1,
      17,    18,    19,    -1,    -1,    -1,    23,    24,    25,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    44,    -1,   465,
     466,    -1,    -1,    -1,    51,    52,   472,     4,     5,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    65,    -1,
      17,    18,    19,   489,    -1,    -1,    23,    24,    25,   495,
     496,    -1,    -1,    80,   500,    -1,   502,    -1,    -1,    -1,
      -1,    88,    89,    90,    -1,    -1,    -1,    44,    -1,    -1,
      -1,    98,    99,   100,    51,    52,    -1,    -1,    -1,    -1,
      -1,   108,    -1,    -1,    -1,    -1,    -1,    -1,    65,    -1,
     117,    -1,    -1,    -1,    -1,   541,    -1,    -1,   544,   126,
      -1,   128,   129,    80,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    88,    89,    90,     4,     5,    -1,    -1,    -1,    -1,
      -1,    98,    99,   100,    -1,    -1,   572,    17,    18,    19,
      -1,   108,    -1,    23,    24,    25,    -1,    -1,   584,    -1,
     117,    -1,    -1,    -1,    -1,    -1,    -1,   593,    -1,   126,
      -1,   128,   129,    -1,    44,    -1,    -1,    -1,    -1,    -1,
      -1,    51,    52,    -1,     4,     5,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    65,    -1,    17,    18,    19,
     626,    -1,    -1,    23,    24,    25,   632,    -1,   634,    -1,
      80,    -1,    -1,   639,    -1,    -1,    -1,    -1,    88,    89,
      90,    -1,    -1,    -1,    44,    -1,    -1,    -1,    98,    99,
     100,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   108,    -1,
      -1,    -1,    -1,    -1,    -1,    65,    -1,   117,    -1,    -1,
      -1,    -1,     4,     5,    -1,    -1,   126,    -1,   128,   129,
      80,    -1,    -1,    -1,    -1,    17,    18,    19,    88,    89,
      90,    23,    24,    25,    -1,    -1,    -1,    -1,    98,    99,
     100,    -1,    -1,    -1,   104,    -1,    -1,    -1,   108,    -1,
      -1,    -1,    44,    -1,    -1,    -1,    -1,   117,    -1,    -1,
      -1,    -1,     4,     5,    -1,    -1,   126,    -1,   128,   129,
      -1,    -1,    -1,    65,    -1,    17,    18,    19,    -1,    -1,
      -1,    23,    24,    25,    -1,    -1,    -1,    -1,    80,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    88,    89,    90,    -1,
      -1,    -1,    44,    -1,    -1,    -1,    98,    99,   100,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   108,    -1,    -1,    -1,
      -1,    -1,    -1,    65,    -1,   117,   118,    -1,    -1,    -1,
       4,     5,    -1,    -1,   126,    -1,   128,   129,    80,    -1,
      -1,    -1,    -1,    17,    18,    19,    88,    89,    90,    23,
      24,    25,    -1,    -1,    -1,    -1,    98,    99,   100,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   108,    -1,    -1,    -1,
      44,    -1,    -1,    -1,   116,   117,    -1,    -1,    -1,    -1,
       4,     5,    -1,    -1,   126,    -1,   128,   129,    -1,    -1,
      -1,    65,    -1,    17,    18,    19,    -1,    -1,    -1,    23,
      24,    25,    -1,    -1,    -1,    -1,    80,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    88,    89,    90,    -1,    -1,    -1,
      44,    -1,    -1,    -1,    98,    99,   100,    -1,    52,    -1,
      -1,    -1,    -1,    -1,   108,    -1,    -1,    -1,    -1,    -1,
      -1,    65,    -1,   117,    -1,    -1,    -1,    -1,   122,    -1,
      -1,    -1,   126,    -1,   128,   129,    80,    -1,     4,     5,
      -1,    -1,    -1,    -1,    88,    89,    90,    -1,    -1,    -1,
      -1,    17,    18,    19,    98,    99,   100,    23,    24,    25,
      -1,    -1,    -1,    -1,   108,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   117,    -1,    -1,    -1,    -1,    44,    -1,
      -1,    -1,   126,    -1,   128,   129,    -1,    -1,     4,     5,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    65,
      -1,    17,    18,    19,    -1,    -1,    -1,    23,    24,    25,
      -1,    -1,    -1,    -1,    80,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    88,    89,    90,    -1,    -1,    -1,    44,    -1,
      -1,    -1,    98,    99,   100,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   108,    -1,    -1,    -1,    -1,    -1,    -1,    65,
      -1,   117,   118,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     126,    -1,   128,   129,    80,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    88,    89,    90,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    98,    99,   100,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   108,     5,    -1,     7,    -1,    -1,    -1,    11,
      -1,   117,    -1,    -1,    -1,    -1,    -1,    -1,    20,    -1,
     126,    -1,   128,   129,    -1,    27,    28,    29,    30,    31,
      32,    33,    -1,    35,    -1,    37,    -1,    -1,    -1,    -1,
      42,    43,    -1,    -1,    -1,    -1,    48,    49,    50,    -1,
      -1,    -1,    54,    -1,    -1,    -1,    -1,    59,    60,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    74,    -1,    76,    77,    -1,    -1,    -1,    81,
      -1,    -1,    -1,    -1,    86,    87,    88,    89,    90,    91,
      -1,    -1,    -1,    95,    96,    -1,    98,    99,   100,   101,
      -1,   103,   104,   105,   106,   107,   108,    -1,   110,   111,
     112,   113,    -1,    -1,   116,    -1,     5,   119,     7,     8,
       9,   123,    11,    -1,   126,    -1,    -1,    -1,    -1,    -1,
      -1,    20,    21,    22,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    35,    -1,    37,    -1,
      -1,    -1,    -1,    42,    43,    -1,    -1,    -1,    -1,    48,
      49,    50,    -1,    -1,    -1,    54,    -1,    -1,    -1,    -1,
      59,    60,    -1,    -1,    -1,    -1,    -1,     5,    -1,     7,
      -1,    -1,    -1,    11,    -1,    74,    -1,    76,    77,    -1,
      -1,    -1,    20,    -1,    -1,    -1,    -1,    86,    87,    -1,
      -1,    -1,    91,    -1,    -1,    -1,    95,    35,    36,    37,
      -1,    -1,    -1,    -1,    42,    43,    -1,    -1,    -1,    -1,
      48,    49,    50,    -1,    -1,    -1,    54,   116,    -1,    -1,
      -1,    59,    60,    -1,   123,    -1,     5,   126,     7,    -1,
      -1,    -1,    11,    -1,    -1,    -1,    74,    -1,    76,    77,
      -1,    20,    -1,    -1,    -1,    -1,    -1,    -1,    86,    87,
      -1,    -1,    -1,    91,    -1,    -1,    35,    95,    37,    97,
      -1,    -1,    -1,    42,    43,    -1,    -1,    -1,    -1,    48,
      49,    50,    -1,    -1,    -1,    54,    -1,    -1,   116,    -1,
      59,    60,    -1,    -1,    -1,   123,    -1,     5,   126,     7,
      -1,    -1,    -1,    11,    -1,    74,    -1,    76,    77,    -1,
      -1,    -1,    20,    -1,    -1,    -1,    -1,    86,    87,    -1,
      -1,    -1,    91,    -1,    -1,    -1,    95,    35,    36,    37,
      -1,    -1,    -1,    -1,    42,    43,    -1,    -1,    -1,    -1,
      48,    49,    50,    -1,    -1,    -1,    54,   116,    -1,    -1,
     119,    59,    60,    -1,   123,    -1,     5,   126,     7,    -1,
      -1,    -1,    11,    -1,    -1,    -1,    74,    -1,    76,    77,
      -1,    20,    -1,    -1,    -1,    -1,    -1,    -1,    86,    87,
      -1,    -1,    -1,    91,    -1,    -1,    35,    95,    37,    -1,
      -1,    -1,    -1,    42,    43,    -1,    -1,    -1,    -1,    48,
      49,    50,    -1,    -1,    -1,    54,    -1,    -1,   116,    -1,
      59,    60,    -1,    -1,    -1,   123,    -1,     5,   126,     7,
      -1,    -1,    -1,    11,    -1,    74,    75,    76,    77,    -1,
      -1,    -1,    20,    -1,    -1,    -1,    -1,    86,    87,    -1,
      -1,    -1,    91,    -1,    -1,    -1,    95,    35,    -1,    37,
      -1,    -1,    -1,    -1,    42,    43,    -1,    -1,    -1,    -1,
      48,    49,    50,    -1,    -1,    -1,    54,   116,    56,    -1,
      -1,    59,    60,    -1,   123,    -1,    -1,   126,     5,    -1,
       7,    -1,    -1,    -1,    11,    -1,    74,    -1,    76,    77,
      -1,    -1,    -1,    20,    -1,    -1,    -1,    -1,    86,    87,
      -1,    -1,    -1,    91,    -1,    -1,    -1,    95,    35,    36,
      37,    -1,    -1,    -1,    -1,    42,    43,    -1,    -1,    -1,
      -1,    48,    49,    50,    -1,    -1,    -1,    54,   116,    -1,
      -1,    -1,    59,    60,    -1,   123,    -1,     5,   126,     7,
      -1,    -1,    -1,    11,    -1,    -1,    -1,    74,    -1,    76,
      77,    -1,    20,    -1,    -1,    -1,    -1,    -1,    -1,    86,
      87,    -1,    -1,    -1,    91,    -1,    -1,    35,    95,    37,
      -1,    -1,    -1,    -1,    42,    43,    -1,    -1,    -1,    -1,
      48,    49,    50,    -1,    -1,    -1,    54,    -1,    56,   116,
      -1,    59,    60,    -1,    -1,    -1,   123,    -1,     5,   126,
       7,    -1,    -1,    -1,    11,    -1,    74,    -1,    76,    77,
      -1,    -1,    -1,    20,    -1,    -1,    -1,    -1,    86,    87,
      -1,    -1,    -1,    91,    -1,    -1,    -1,    95,    35,    -1,
      37,    -1,    -1,    -1,    -1,    42,    43,    -1,    -1,    -1,
      -1,    48,    49,    50,    -1,    -1,    -1,    54,   116,    -1,
      -1,    -1,    59,    60,    -1,   123,    -1,    -1,   126,     5,
      -1,     7,    -1,    -1,    -1,    11,    -1,    74,    -1,    76,
      77,    -1,    -1,    -1,    20,    -1,    -1,    -1,    -1,    86,
      87,    -1,    -1,    -1,    91,    -1,    -1,    -1,    95,    35,
      -1,    37,    -1,    -1,    -1,    -1,    42,    43,    -1,    -1,
      -1,    -1,    48,    49,    50,    -1,    -1,    -1,    54,   116,
      -1,    -1,   119,    59,    60,    -1,   123,    -1,    -1,   126,
       5,    -1,     7,    -1,    -1,    -1,    11,    -1,    74,    -1,
      76,    77,    -1,    -1,    -1,    20,    -1,    -1,    -1,    -1,
      86,    87,    -1,    -1,    -1,    91,    -1,    -1,    -1,    95,
      35,    -1,    37,    -1,    -1,    -1,    -1,    42,    43,    -1,
      -1,    -1,    -1,    48,    49,    50,    -1,    -1,    -1,    54,
     116,    -1,    -1,   119,    59,    60,    -1,   123,    -1,    -1,
     126,    27,    28,    29,    30,    31,    32,    33,    -1,    74,
      -1,    76,    77,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    86,    87,    -1,    -1,    -1,    91,    -1,    -1,    -1,
      95,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      27,    28,    29,    30,    31,    32,    33,    -1,    -1,    -1,
      -1,   116,    -1,    -1,    -1,    81,    -1,    -1,   123,    -1,
      -1,   126,    88,    89,    90,    -1,    -1,    -1,    -1,    -1,
      96,    -1,    98,    99,   100,   101,    -1,   103,   104,   105,
     106,   107,   108,    -1,   110,   111,   112,   113,    -1,    -1,
      -1,    78,    79,    -1,    81,    -1,    -1,    -1,    -1,    -1,
     126,    88,    89,    90,    -1,    -1,    -1,    -1,    -1,    96,
      97,    98,    99,   100,   101,    -1,   103,   104,   105,   106,
     107,   108,    -1,   110,   111,   112,   113,    27,    28,    29,
      30,    31,    32,    33,    -1,    -1,    -1,    -1,   125,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    27,    28,    29,    30,    31,
      32,    33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    81,    -1,    -1,    -1,    -1,    -1,    -1,    88,    89,
      90,    -1,    -1,    -1,    -1,    -1,    96,    -1,    98,    99,
     100,   101,    -1,   103,   104,   105,   106,   107,   108,    81,
     110,   111,   112,   113,    -1,    -1,    88,    89,    90,    -1,
      -1,    -1,    -1,    -1,    96,   125,    98,    99,   100,   101,
      -1,   103,   104,   105,   106,   107,   108,    -1,   110,   111,
     112,   113,    27,    28,    29,    30,    31,    32,    33,    -1,
      -1,    -1,    -1,   125,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      27,    28,    29,    30,    31,    32,    33,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    81,    -1,    -1,    -1,
      -1,    -1,    -1,    88,    89,    90,    -1,    -1,    -1,    -1,
      -1,    96,    -1,    98,    99,   100,   101,    -1,   103,   104,
     105,   106,   107,   108,    81,   110,   111,   112,   113,    -1,
      -1,    88,    89,    90,    -1,    -1,   121,    -1,    -1,    96,
      -1,    98,    99,   100,   101,    -1,   103,   104,   105,   106,
     107,   108,    -1,   110,   111,   112,   113,    -1,    -1,    -1,
      -1,    -1,   119,    27,    28,    29,    30,    31,    32,    33,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    27,    28,    29,    30,    31,    32,    33,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    81,    -1,    -1,
      -1,    -1,    -1,    -1,    88,    89,    90,    -1,    -1,    -1,
      -1,    -1,    96,    -1,    98,    99,   100,   101,    -1,   103,
     104,   105,   106,   107,   108,    81,   110,   111,   112,   113,
      -1,    -1,    88,    89,    90,   119,    -1,    -1,    -1,    -1,
      96,    -1,    98,    99,   100,   101,    -1,   103,   104,   105,
     106,   107,   108,    -1,   110,   111,   112,   113,    -1,    -1,
      -1,    -1,    -1,   119,    27,    28,    29,    30,    31,    32,
      33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    27,    28,    29,    30,    31,    32,    33,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    81,    -1,
      -1,    -1,    -1,    -1,    -1,    88,    89,    90,    -1,    -1,
      -1,    -1,    -1,    96,    -1,    98,    99,   100,   101,    -1,
     103,   104,   105,   106,   107,   108,    81,   110,   111,   112,
     113,    -1,    -1,    88,    89,    90,   119,    -1,    -1,    -1,
      -1,    96,    -1,    98,    99,   100,   101,    -1,   103,   104,
     105,   106,   107,   108,    -1,   110,   111,   112,   113,    -1,
      -1,    -1,    -1,    -1,   119,    27,    28,    29,    30,    31,
      32,    33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    27,    28,    29,    30,    31,    32,    33,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    81,
      -1,    -1,    -1,    -1,    -1,    -1,    88,    89,    90,    -1,
      -1,    -1,    -1,    -1,    96,    -1,    98,    99,   100,   101,
      -1,   103,   104,   105,   106,   107,   108,    81,   110,   111,
     112,   113,    -1,    -1,    88,    89,    90,   119,    -1,    -1,
      -1,    -1,    96,    -1,    98,    99,   100,   101,    -1,   103,
     104,   105,   106,   107,   108,    -1,   110,   111,   112,   113,
      -1,    -1,    -1,    -1,    -1,   119,    27,    28,    29,    30,
      31,    32,    33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    27,    28,    29,    30,    31,    32,
      33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      81,    -1,    -1,    -1,    -1,    -1,    -1,    88,    89,    90,
      -1,    -1,    -1,    -1,    -1,    96,    -1,    98,    99,   100,
     101,    -1,   103,   104,   105,   106,   107,   108,    81,   110,
     111,   112,   113,    -1,    -1,    88,    89,    90,   119,    -1,
      -1,    -1,    -1,    96,    -1,    98,    99,   100,   101,    -1,
     103,   104,   105,   106,   107,   108,    -1,   110,   111,   112,
     113,    -1,    -1,    -1,    -1,    -1,   119,    27,    28,    29,
      30,    31,    32,    33,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    27,    28,    29,    30,    31,
      32,    33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    81,    -1,    -1,    -1,    -1,    -1,    -1,    88,    89,
      90,    -1,    -1,    -1,    -1,    -1,    96,    -1,    98,    99,
     100,   101,    -1,   103,   104,   105,   106,   107,   108,    81,
     110,   111,   112,   113,    -1,    -1,    88,    89,    90,   119,
      -1,    -1,    -1,    -1,    96,    -1,    98,    99,   100,   101,
      -1,   103,   104,   105,   106,   107,   108,    -1,   110,   111,
     112,   113,    -1,    -1,    -1,    -1,    -1,   119,    27,    28,
      29,    30,    31,    32,    33,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    27,    28,    29,    30,
      31,    32,    33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    81,    -1,    -1,    -1,    -1,    -1,    -1,    88,
      89,    90,    -1,    -1,    -1,    -1,    -1,    96,    -1,    98,
      99,   100,   101,    -1,   103,   104,   105,   106,   107,   108,
      81,   110,   111,   112,   113,    -1,    -1,    88,    89,    90,
     119,    -1,    -1,    -1,    -1,    96,    -1,    98,    99,   100,
     101,    -1,   103,   104,   105,   106,   107,   108,    -1,   110,
     111,   112,   113,    -1,    -1,    -1,    -1,    -1,   119,    27,
      28,    29,    30,    31,    32,    33,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    27,    28,    29,
      30,    31,    32,    33,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    81,    -1,    -1,    -1,    -1,    -1,    -1,
      88,    89,    90,    -1,    -1,    -1,    -1,    -1,    96,    -1,
      98,    99,   100,   101,    -1,   103,   104,   105,   106,   107,
     108,    81,   110,   111,   112,   113,    -1,    -1,    88,    89,
      90,   119,    -1,    -1,    -1,    -1,    96,    -1,    98,    99,
     100,   101,    -1,   103,   104,   105,   106,   107,   108,    -1,
     110,   111,   112,   113,    -1,    -1,    -1,    -1,    -1,   119,
      27,    28,    29,    30,    31,    32,    33,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    27,    28,
      29,    30,    31,    32,    33,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    81,    -1,    -1,    -1,    -1,    -1,
      -1,    88,    89,    90,    -1,    -1,    -1,    -1,    -1,    96,
      -1,    98,    99,   100,   101,    -1,   103,   104,   105,   106,
     107,   108,    81,   110,   111,   112,   113,    -1,    -1,    88,
      89,    90,   119,    -1,    -1,    -1,    -1,    96,    -1,    98,
      99,   100,   101,    -1,   103,   104,   105,   106,   107,   108,
      -1,   110,   111,   112,   113,    -1,    -1,    -1,    -1,     5,
     119,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      16,    -1,    -1,    -1,    20,    21,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    34,    35,
      -1,    37,    -1,    -1,    -1,    41,    -1,    -1,    -1,    45,
      46,    47,    -1,    -1,    -1,    -1,    -1,    53,    -1,    -1,
      -1,    -1,    -1,    59,    27,    28,    29,    30,    31,    32,
      33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    85,
      -1,    -1,    -1,    -1,    -1,    -1,    92,    93,    -1,    -1,
      -1,    97,    27,    28,    29,    30,    31,    32,    33,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    81,    -1,
      -1,    -1,    -1,    -1,    -1,    88,    89,    90,    -1,    -1,
      -1,    -1,    -1,    96,    -1,    98,    99,   100,   101,    -1,
     103,   104,   105,   106,   107,   108,    -1,   110,   111,   112,
     113,    -1,    -1,    -1,    -1,   118,    81,    -1,    -1,    -1,
      -1,    -1,    -1,    88,    89,    90,    -1,    -1,    -1,    -1,
      -1,    96,    -1,    98,    99,   100,   101,    -1,   103,   104,
     105,   106,   107,   108,    -1,   110,   111,   112,   113,    -1,
      -1,    -1,    -1,   118,    27,    28,    29,    30,    31,    32,
      33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    27,    28,    29,
      30,    31,    32,    33,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    81,    -1,
      -1,    -1,    -1,    -1,    -1,    88,    89,    90,    -1,    -1,
      -1,    -1,    -1,    96,    -1,    98,    99,   100,   101,    -1,
     103,   104,   105,   106,   107,   108,    -1,   110,   111,   112,
     113,    81,    -1,    -1,    -1,   118,    -1,    -1,    88,    89,
      90,    -1,    -1,    -1,    -1,    -1,    96,    -1,    98,    99,
     100,   101,    -1,   103,   104,   105,   106,   107,   108,    -1,
     110,   111,   112,   113,    -1,    -1,    -1,    -1,   118,    27,
      28,    29,    30,    31,    32,    33,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    27,    28,    29,    30,    31,    32,    33,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    81,    -1,    -1,    -1,    -1,    -1,    -1,
      88,    89,    90,    -1,    -1,    -1,    -1,    -1,    96,    -1,
      98,    99,   100,   101,    -1,   103,   104,   105,   106,   107,
     108,    -1,   110,   111,   112,   113,    81,    -1,    -1,    -1,
     118,    -1,    -1,    88,    89,    90,    -1,    -1,    -1,    -1,
      -1,    96,    -1,    98,    99,   100,   101,    -1,   103,   104,
     105,   106,   107,   108,    -1,   110,   111,   112,   113,    -1,
      -1,    -1,    -1,   118,    27,    28,    29,    30,    31,    32,
      33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    27,    28,    29,
      30,    31,    32,    33,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    81,    -1,
      -1,    -1,    -1,    -1,    -1,    88,    89,    90,    -1,    -1,
      -1,    -1,    -1,    96,    -1,    98,    99,   100,   101,    -1,
     103,   104,   105,   106,   107,   108,    -1,   110,   111,   112,
     113,    81,    -1,    -1,    -1,   118,    -1,    -1,    88,    89,
      90,    -1,    -1,    -1,    -1,    -1,    96,    -1,    98,    99,
     100,   101,    -1,   103,   104,   105,   106,   107,   108,    -1,
     110,   111,   112,   113,    -1,    -1,    -1,    -1,   118,    27,
      28,    29,    30,    31,    32,    33,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    27,    28,    29,    30,    31,    32,    33,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    81,    -1,    -1,    -1,    -1,    -1,    -1,
      88,    89,    90,    -1,    -1,    -1,    -1,    -1,    96,    -1,
      98,    99,   100,   101,    -1,   103,   104,   105,   106,   107,
     108,    -1,   110,   111,   112,   113,    81,    -1,    -1,    -1,
     118,    -1,    -1,    88,    89,    90,    -1,    -1,    -1,    -1,
      -1,    96,    -1,    98,    99,   100,   101,    -1,   103,   104,
     105,   106,   107,   108,    -1,   110,   111,   112,   113,    -1,
      -1,    -1,    -1,   118,    27,    28,    29,    30,    31,    32,
      33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    27,    28,    29,
      30,    31,    32,    33,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    81,    -1,
      -1,    -1,    -1,    -1,    -1,    88,    89,    90,    -1,    -1,
      -1,    -1,    -1,    96,    -1,    98,    99,   100,   101,    -1,
     103,   104,   105,   106,   107,   108,    -1,   110,   111,   112,
     113,    81,    -1,    -1,    -1,   118,    -1,    -1,    88,    89,
      90,    -1,    -1,    -1,    -1,    -1,    96,    -1,    98,    99,
     100,   101,    -1,   103,   104,   105,   106,   107,   108,    -1,
     110,   111,   112,   113,    -1,    -1,    -1,     5,   118,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    16,    -1,
      -1,    -1,    20,    21,     5,    -1,     7,     8,     9,    10,
      11,    12,    13,    14,    15,    16,    34,    -1,    -1,    20,
      21,    -1,    -1,    41,    -1,    -1,    -1,    45,    46,    47,
      -1,    -1,    -1,    34,    35,    53,    37,    55,    -1,    57,
      41,    -1,    -1,    -1,    45,    46,    47,    65,    -1,    -1,
      -1,    -1,    53,    -1,    -1,    -1,    -1,    -1,    59,    77,
      -1,    -1,    -1,    -1,    -1,    83,    -1,    85,    -1,    -1,
      -1,    -1,    -1,    -1,    92,    93,    94,    -1,    -1,    -1,
      -1,    -1,    -1,    84,    85,    -1,    -1,    -1,    -1,    -1,
      -1,    92,    93,     5,    -1,     7,     8,     9,    10,    11,
      12,    13,    14,    15,    16,    -1,    -1,    -1,    20,    21,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    34,    35,    36,    37,    -1,    -1,    -1,    41,
      -1,    -1,    -1,    45,    46,    47,    -1,    -1,    -1,    -1,
      -1,    53,    -1,    -1,    -1,    -1,     5,    59,     7,     8,
       9,    10,    11,    12,    13,    14,    15,    16,    -1,    -1,
      -1,    20,    21,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    85,    -1,    34,    35,    36,    37,    -1,
      92,    93,    41,    -1,    -1,    -1,    45,    46,    47,    -1,
      -1,    -1,    -1,    -1,    53,    -1,    -1,    -1,    -1,     5,
      59,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      16,    -1,    -1,    -1,    20,    21,    -1,    -1,    -1,    27,
      28,    29,    30,    31,    32,    33,    85,    -1,    34,    35,
      -1,    37,    -1,    92,    93,    41,    -1,    -1,    -1,    45,
      46,    47,    -1,    -1,    -1,    -1,    -1,    53,    -1,    -1,
      -1,    -1,    -1,    59,    27,    28,    29,    30,    31,    32,
      33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      78,    79,    -1,    81,    -1,    -1,    -1,    -1,    -1,    85,
      88,    89,    90,    -1,    -1,    -1,    92,    93,    96,    97,
      98,    99,   100,   101,    -1,   103,   104,   105,   106,   107,
     108,    -1,   110,   111,   112,   113,    -1,    -1,    81,    28,
      29,    30,    31,    32,    33,    88,    89,    90,    -1,    -1,
      -1,    -1,    -1,    96,    97,    98,    99,   100,   101,    -1,
     103,   104,   105,   106,   107,   108,    -1,   110,   111,   112,
     113,    27,    28,    29,    30,    31,    32,    33,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    81,    -1,    -1,    -1,    -1,    -1,    -1,    88,
      89,    90,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    98,
      99,   100,   101,    -1,   103,   104,   105,   106,   107,   108,
      -1,   110,   111,   112,   113,    81,    28,    29,    30,    31,
      32,    33,    88,    89,    90,    -1,    -1,    -1,    -1,    -1,
      96,    -1,    98,    99,   100,   101,    -1,   103,   104,   105,
     106,   107,   108,    -1,   110,   111,   112,   113,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    81,
      -1,    -1,    -1,    -1,    -1,    -1,    88,    89,    90,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    99,   100,   101,
      -1,   103,   104,   105,   106,   107,   108,    -1,   110,   111,
     112,   113
};

/* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
   symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,     3,    65,   131,   132,   133,   134,   141,     5,     4,
       5,    44,     0,   133,   116,   135,     5,     4,     5,    17,
      18,    19,    23,    24,    25,    44,    65,    80,    88,    89,
      90,    98,    99,   100,   108,   117,   126,   128,   129,   194,
     197,   199,   117,   117,   119,   136,   112,   117,   122,   124,
     190,   191,   117,   199,   199,   199,   199,   199,   199,   199,
     199,   104,   195,   196,   199,   199,   199,    27,    28,    29,
      30,    31,    32,    33,    81,    88,    89,    90,    96,    98,
      99,   100,   101,   103,   104,   105,   106,   107,   108,   110,
     111,   112,   113,     5,    46,   118,   159,   160,     5,     8,
       9,    10,   118,   137,   138,   192,     5,     7,    11,    12,
      13,    14,    15,    16,    20,    21,    34,    41,    45,    46,
      47,    53,    55,    57,    77,    83,    85,    92,    93,    94,
     139,   140,   141,   142,   143,   144,   148,   149,   152,   153,
     154,   161,   168,   169,   192,   193,     4,   186,   199,     5,
     197,   199,   190,   191,   199,   118,   194,   120,   127,   194,
     199,   199,   199,   199,   199,   199,   199,   199,   199,   199,
     199,   199,   199,   199,   199,   199,   199,   199,   199,   199,
     199,   199,   199,   199,   199,   199,   121,     5,   124,   190,
     118,   120,    12,    15,    11,    12,    15,    12,   119,   118,
     120,     5,    20,   190,     5,    26,   116,   167,     5,   116,
     117,   145,   164,   181,   182,   188,   194,   197,    15,    15,
       5,   189,     5,     7,    11,    20,    35,    37,    42,    43,
      48,    49,    50,    54,    59,    60,    74,    76,    77,    86,
      87,    91,    95,   116,   123,   173,   177,   178,   179,   180,
     188,   197,     5,   117,     5,   155,   156,   197,     5,    15,
     157,   158,   190,   157,   190,   173,   177,     5,    20,   147,
     190,     5,    35,    37,    59,    85,   142,   143,   144,   152,
     153,   154,   161,   168,   170,   171,   172,     6,   139,   189,
     190,     5,   167,   189,   190,     5,   118,   120,   117,   190,
     191,    78,    79,    97,   125,   118,   196,    97,   199,   121,
     199,     5,   160,    15,   119,   138,   121,     5,     5,   190,
     117,   119,   190,     5,     4,     5,    80,   117,     5,   190,
     191,     4,     5,    80,   117,    66,    67,    68,    69,    70,
      71,    72,    73,   146,   164,   188,   188,   119,   120,   121,
     120,   119,   117,   119,   188,   189,   190,   189,    36,    97,
     177,   187,   117,   199,     5,   117,   117,   117,   177,   117,
     117,   187,     5,   199,   199,   117,     5,   199,     5,    82,
     111,   117,   119,   177,    33,   121,   119,   117,   186,   119,
     120,   121,   121,   157,   190,   119,   120,   157,   190,   119,
     157,   190,   117,   119,     5,   190,   117,   119,    97,   170,
     117,   117,     5,    84,   171,   119,   189,   190,     5,   189,
     119,   121,     5,   189,   190,   199,   199,   199,   199,   199,
     199,   199,   121,     4,    17,    18,    19,    23,    24,    25,
      44,    80,   198,   121,   190,     5,   118,   122,   162,   163,
     186,   117,     5,   118,   122,   165,   166,   186,   117,   190,
     190,   191,   186,   120,   188,   121,   121,   182,   199,   189,
     118,   186,   121,   119,   189,   119,     5,    36,   177,   199,
     119,   119,   199,   199,   199,   181,   199,    75,   119,   121,
     119,   199,   119,   119,   177,    39,    40,   175,   176,   199,
     164,   199,   164,   199,   162,   186,   118,   155,   199,   199,
     119,   157,   158,   119,   157,   119,   157,   137,     8,     9,
      11,    20,    21,    22,   150,   151,   187,   117,   119,     5,
     137,   150,   177,     5,    36,   199,   181,   119,   119,   190,
     119,   121,   119,   199,   121,   190,   119,     5,   189,   118,
     125,   125,   125,   199,   198,   119,     5,   111,   118,   120,
     118,   162,   119,     5,   118,   120,   118,   118,   162,   117,
     118,   146,   121,   199,   199,   119,   118,   199,   119,   187,
     118,   118,   118,   118,   119,   118,   199,   118,   199,   199,
      41,   118,   120,   174,   199,   119,   199,   119,   118,   118,
     119,   119,   119,   119,   118,    20,   189,   190,    11,   189,
     190,   189,   189,   189,   151,   187,    56,   137,   150,   177,
     119,   118,   177,    58,   170,   118,   119,   119,   199,   119,
     199,   119,   121,   119,   117,   119,   163,   119,   118,   117,
     166,   119,   118,   162,   118,   199,   119,   119,   119,   119,
      36,   177,    52,   183,   184,   185,   186,   183,   183,   199,
     177,   119,   177,   176,   119,   119,   119,   119,   119,   189,
     119,   190,   190,   190,   119,     5,   189,   190,   119,   190,
     119,   119,    56,   118,   177,    56,    11,    20,   150,   119,
      58,    36,   171,   199,   119,   119,   199,   118,   199,   119,
     199,   119,   118,   119,    38,    97,    51,   184,   185,    51,
      97,    51,   185,    51,   185,   119,   150,   177,   119,   119,
     189,   190,   190,   119,     5,   119,   119,    56,   189,   190,
     189,   177,   150,   177,    38,   119,   119,   118,   118,   119,
     177,   119,   177,    51,   119,   177,    51,    51,   181,   177,
      56,   119,     5,   119,   119,   150,   177,   119,   189,   119,
      56,   177,    58,   171,   181,   118,    56,   119,   177,    56,
     119,    58,   118,   177,    56,   171
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
#line 3117 "y.tab.c"
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


#line 373 "yaccs/verilog.yacc"


