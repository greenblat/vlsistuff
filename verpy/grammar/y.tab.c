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
#define YYLAST   5223

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  133
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  75
/* YYNRULES -- Number of rules.  */
#define YYNRULES  361
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
     114,   117,   120,   124,   131,   134,   136,   140,   144,   146,
     150,   155,   161,   165,   169,   174,   180,   186,   191,   196,
     203,   207,   214,   222,   229,   235,   237,   239,   241,   243,
     245,   247,   249,   251,   253,   255,   262,   268,   277,   285,
     292,   301,   311,   321,   332,   339,   345,   354,   364,   367,
     369,   373,   377,   381,   386,   392,   398,   405,   409,   414,
     420,   425,   429,   434,   438,   443,   448,   454,   460,   464,
     469,   475,   479,   483,   487,   489,   493,   495,   499,   503,
     505,   510,   515,   521,   525,   531,   538,   542,   548,   555,
     562,   569,   576,   582,   590,   599,   607,   615,   619,   621,
     624,   630,   635,   640,   643,   646,   649,   653,   655,   661,
     664,   669,   672,   675,   678,   683,   687,   690,   693,   697,
     701,   704,   706,   710,   716,   720,   722,   724,   726,   728,
     730,   732,   734,   736,   738,   740,   746,   754,   764,   767,
     770,   773,   778,   780,   782,   786,   788,   791,   794,   796,
     800,   803,   806,   812,   816,   821,   827,   832,   838,   844,
     852,   856,   860,   864,   869,   873,   879,   882,   886,   890,
     895,   901,   908,   916,   923,   930,   938,   945,   953,   957,
     961,   964,   966,   968,   970,   973,   975,   981,   985,   989,
     991,   995,   997,  1001,  1011,  1017,  1023,  1027,  1029,  1033,
    1036,  1038,  1042,  1046,  1050,  1054,  1058,  1060,  1063,  1065,
    1067,  1070,  1074,  1078,  1081,  1083,  1085,  1089,  1091,  1097,
    1103,  1109,  1113,  1115,  1117,  1119,  1122,  1125,  1128,  1131,
    1134,  1137,  1141,  1144,  1147,  1149,  1151,  1153,  1155,  1157,
    1159,  1162,  1165,  1167,  1169,  1171,  1173,  1175,  1179,  1183,
    1185,  1188,  1190,  1193,  1197,  1201,  1206,  1211,  1218,  1220,
    1222,  1224,  1226,  1228,  1230,  1232,  1234,  1236,  1238,  1240,
    1242,  1244,  1246,  1248,  1253,  1255,  1257,  1259,  1261,  1263,
    1265,  1268,  1272,  1276,  1279,  1285,  1289,  1293,  1297,  1301,
    1305,  1309,  1313,  1317,  1321,  1325,  1329,  1333,  1337,  1341,
    1345,  1349,  1353,  1357,  1361,  1365,  1369,  1373,  1377,  1381,
    1385,  1390,  1394,  1396,  1399,  1402,  1405,  1408,  1411,  1414,
    1417,  1420
};

/* YYRHS -- A `-1'-separated list of the rules' RHS.  */
static const yytype_int16 yyrhs[] =
{
     134,     0,    -1,   135,    -1,   135,   136,    -1,   136,    -1,
     137,    -1,   144,    -1,     3,     5,   138,   139,   142,     6,
      -1,   119,   120,   164,   121,    -1,   119,   120,   121,    -1,
      -1,   122,    -1,   120,   140,   121,   122,    -1,   120,   121,
     122,    -1,   140,   123,   141,    -1,   141,    -1,   200,     5,
      -1,   200,   198,     5,    -1,   200,    21,     5,    -1,   200,
     198,     5,   198,    -1,   200,   198,   198,     5,    -1,     5,
      -1,   200,     5,   124,   206,    -1,   200,   198,     5,   124,
     206,    -1,   143,   142,    -1,    -1,   148,    -1,   149,    -1,
     166,    -1,   173,    -1,   174,    -1,   157,    -1,   158,    -1,
     159,    -1,   145,    -1,   153,    -1,   154,    -1,   144,    -1,
     185,    -1,    96,    -1,    66,    45,    -1,    66,     5,    -1,
      66,     5,   207,    -1,    66,     4,     5,   115,     4,     5,
      -1,    54,   182,    -1,     5,    -1,     5,   124,   207,    -1,
     147,   123,   146,    -1,   146,    -1,   200,   197,   122,    -1,
     200,   198,   197,   122,    -1,   200,   198,   197,   198,   122,
      -1,    17,   197,   122,    -1,   201,   147,   122,    -1,   201,
     198,   147,   122,    -1,   201,   198,   198,   147,   122,    -1,
     201,   198,     5,   198,   122,    -1,   201,     5,   198,   122,
      -1,   201,   172,   197,   122,    -1,   201,   172,     5,   124,
     207,   122,    -1,     7,   189,   122,    -1,     7,   169,   196,
     124,   207,   122,    -1,     7,   150,   169,   196,   124,   207,
     122,    -1,     7,   150,   196,   124,   207,   122,    -1,   120,
     151,   123,   151,   121,    -1,    67,    -1,    68,    -1,    69,
      -1,    70,    -1,    71,    -1,    72,    -1,    73,    -1,    74,
      -1,   198,    -1,    21,    -1,    56,     5,   122,   155,   195,
      57,    -1,    56,     5,   122,   195,    57,    -1,    56,   198,
     198,     5,   122,   155,   182,    57,    -1,    56,   152,     5,
     122,   155,   182,    57,    -1,    56,   152,     5,   122,   182,
      57,    -1,    56,     5,   120,   140,   121,   122,   182,    57,
      -1,    56,     5,   120,   140,   121,   122,   155,   182,    57,
      -1,    56,   152,     5,   120,   140,   121,   122,   182,    57,
      -1,    56,   152,     5,   120,   140,   121,   122,   155,   182,
      57,    -1,    58,     5,   122,   155,   182,    59,    -1,    58,
       5,   122,   182,    59,    -1,    58,     5,   120,   140,   121,
     122,   182,    59,    -1,    58,     5,   120,   140,   121,   122,
     155,   182,    59,    -1,   155,   156,    -1,   156,    -1,    11,
     197,   122,    -1,    22,   197,   122,    -1,    23,   197,   122,
      -1,    11,   198,   197,   122,    -1,    11,   198,     5,   198,
     122,    -1,    11,   198,   198,     5,   122,    -1,     9,    11,
     198,   198,     5,   122,    -1,     8,   197,   122,    -1,     8,
     197,   198,   122,    -1,     8,   198,   198,   197,   122,    -1,
       8,    21,   197,   122,    -1,    21,   197,   122,    -1,    21,
     197,   198,   122,    -1,    47,   162,   122,    -1,    47,    16,
     162,   122,    -1,    47,   198,   162,   122,    -1,    47,   198,
     198,   162,   122,    -1,    47,    16,   198,   162,   122,    -1,
      48,   162,   122,    -1,    48,   198,   162,   122,    -1,    48,
     198,   198,   162,   122,    -1,    46,   161,   122,    -1,   205,
     124,   207,    -1,   161,   123,   160,    -1,   160,    -1,   162,
     123,   163,    -1,   163,    -1,     5,   124,   207,    -1,   164,
     123,   165,    -1,   165,    -1,    48,     5,   124,   207,    -1,
      47,     5,   124,   207,    -1,    47,   198,     5,   124,   207,
      -1,     5,   124,   207,    -1,     5,     5,   120,   121,   122,
      -1,     5,   172,     5,   120,   121,   122,    -1,     5,     5,
     122,    -1,    42,   120,   194,   121,   122,    -1,    42,     5,
     120,   194,   121,   122,    -1,     5,     5,   120,   167,   121,
     122,    -1,    42,     5,   120,   167,   121,   122,    -1,     5,
       5,   120,   194,   121,   122,    -1,     5,   120,   194,   121,
     122,    -1,     5,   172,     5,   120,   167,   121,   122,    -1,
       5,   172,     5,   198,   120,   167,   121,   122,    -1,     5,
       5,   198,   120,   167,   121,   122,    -1,     5,     5,   198,
     120,   194,   121,   122,    -1,   167,   123,   168,    -1,   168,
      -1,   125,   114,    -1,   125,     5,   120,   207,   121,    -1,
     125,     5,   120,   121,    -1,   119,   120,   194,   121,    -1,
     119,     4,    -1,   119,     5,    -1,   119,    82,    -1,   170,
     123,   171,    -1,   171,    -1,   125,     5,   120,   207,   121,
      -1,   125,     5,    -1,   119,   120,   194,   121,    -1,   119,
       4,    -1,   119,    82,    -1,   119,     5,    -1,   119,   120,
     170,   121,    -1,   119,   120,   121,    -1,    98,   182,    -1,
      35,   182,    -1,    35,   178,   182,    -1,    85,   175,    86,
      -1,   175,   176,    -1,   176,    -1,    36,   175,    37,    -1,
      36,   100,     5,   175,    37,    -1,    87,   197,   122,    -1,
     148,    -1,   149,    -1,   157,    -1,   158,    -1,   159,    -1,
     166,    -1,   177,    -1,   173,    -1,   145,    -1,   185,    -1,
      38,   120,   207,   121,   176,    -1,    38,   120,   207,   121,
     176,    39,   176,    -1,    60,   120,   189,   122,   207,   122,
     189,   121,   176,    -1,   126,   114,    -1,   126,    84,    -1,
     126,     5,    -1,   126,   120,   180,   121,    -1,    42,    -1,
     123,    -1,   180,   179,   181,    -1,   181,    -1,    40,   207,
      -1,    41,   207,    -1,   207,    -1,    36,   195,    37,    -1,
      36,    37,    -1,    55,   182,    -1,    36,   100,     5,   195,
      37,    -1,    75,   195,    76,    -1,   196,   124,   207,   122,
      -1,   196,   124,   169,   207,   122,    -1,   196,    34,   207,
     122,    -1,   196,    34,   169,   207,   122,    -1,    38,   120,
     207,   121,   182,    -1,    38,   120,   207,   121,   182,    39,
     182,    -1,    43,   207,   122,    -1,    21,   197,   122,    -1,
      11,   197,   122,    -1,    11,   198,   197,   122,    -1,    89,
     207,   122,    -1,    88,   207,   124,   207,   122,    -1,   178,
     122,    -1,    44,     5,   122,    -1,    77,     5,   122,    -1,
       5,   120,   121,   122,    -1,     5,   120,   194,   121,   122,
      -1,    49,   120,   207,   121,   191,    52,    -1,    49,   120,
     207,   121,   191,   193,    52,    -1,    49,   120,   207,   121,
     193,    52,    -1,    50,   120,   207,   121,   191,    52,    -1,
      50,   120,   207,   121,   191,   193,    52,    -1,    51,   120,
     207,   121,   191,    52,    -1,    51,   120,   207,   121,   191,
     193,    52,    -1,   119,   207,   122,    -1,   119,   207,   182,
      -1,     5,   122,    -1,   186,    -1,   187,    -1,   188,    -1,
     205,   122,    -1,   185,    -1,     7,   196,   124,   207,   122,
      -1,    97,     5,   122,    -1,   183,   123,   184,    -1,   184,
      -1,     5,   124,   207,    -1,    45,    -1,    78,   183,    79,
      -1,    60,   120,   189,   122,   207,   122,   189,   121,   182,
      -1,    93,   120,   207,   121,   182,    -1,    61,   120,   207,
     121,   182,    -1,   189,   123,   190,    -1,   190,    -1,   196,
     124,   207,    -1,   191,   192,    -1,   192,    -1,   194,   100,
     182,    -1,   194,   100,   122,    -1,    53,   100,   182,    -1,
      53,   100,   122,    -1,   194,   123,   207,    -1,   207,    -1,
     195,   182,    -1,   182,    -1,     5,    -1,     5,   198,    -1,
       5,   199,   198,    -1,     5,   199,   199,    -1,     5,   199,
      -1,   205,    -1,   202,    -1,     5,   123,   197,    -1,     5,
      -1,   127,   207,   100,   207,   128,    -1,   127,   207,    80,
     207,   128,    -1,   127,   207,    81,   207,   128,    -1,   127,
     207,   128,    -1,     8,    -1,     9,    -1,    10,    -1,     9,
      11,    -1,     8,    12,    -1,     9,    12,    -1,    10,    12,
      -1,     8,    16,    -1,     9,    16,    -1,     9,    11,    16,
      -1,     9,    13,    -1,     8,    13,    -1,    13,    -1,    11,
      -1,    12,    -1,    16,    -1,    21,    -1,    22,    -1,    11,
      16,    -1,    12,    16,    -1,    87,    -1,    94,    -1,    95,
      -1,    14,    -1,    15,    -1,   129,   203,   130,    -1,   203,
     123,   204,    -1,   204,    -1,   207,   202,    -1,   207,    -1,
     107,   202,    -1,     5,   125,   205,    -1,     5,   125,     5,
      -1,     5,   125,     5,   198,    -1,     5,   125,     5,   199,
      -1,     5,   125,     5,   120,   207,   121,    -1,     4,    -1,
      82,    -1,    45,    -1,    18,    -1,    19,    -1,    20,    -1,
      24,    -1,    25,    -1,    26,    -1,     5,    -1,   205,    -1,
       4,    -1,    82,    -1,    45,    -1,    66,    -1,    66,   120,
     207,   121,    -1,    18,    -1,    19,    -1,    20,    -1,    24,
      -1,    25,    -1,    26,    -1,     5,   198,    -1,     5,   199,
     198,    -1,     5,   199,   199,    -1,     5,   199,    -1,   207,
      99,   207,   100,   207,    -1,   207,   110,   207,    -1,   207,
     114,   207,    -1,   207,   111,   207,    -1,   207,   115,   207,
      -1,   207,   116,   207,    -1,   207,   102,   207,    -1,   207,
     101,   207,    -1,   207,   103,   207,    -1,   207,   108,   207,
      -1,   207,   109,   207,    -1,   207,    83,   207,    -1,   207,
      28,   207,    -1,   207,    29,   207,    -1,   207,    90,   207,
      -1,   207,    91,   207,    -1,   207,    92,   207,    -1,   207,
      31,   207,    -1,   207,    30,   207,    -1,   207,    32,   207,
      -1,   207,   113,   207,    -1,   207,    33,   207,    -1,   207,
      34,   207,    -1,   207,   107,   207,    -1,   207,   106,   207,
      -1,   207,   104,   207,    -1,     5,   120,   194,   121,    -1,
     120,   207,   121,    -1,   202,    -1,   111,   207,    -1,   101,
     207,    -1,   103,   207,    -1,   102,   207,    -1,    90,   207,
      -1,    92,   207,    -1,    91,   207,    -1,   131,   207,    -1,
     132,   207,    -1
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
     102,   103,   104,   105,   108,   109,   109,   109,   109,   109,
     109,   109,   109,   110,   110,   112,   113,   114,   115,   116,
     117,   118,   119,   120,   123,   124,   125,   126,   129,   129,
     131,   132,   133,   134,   135,   136,   137,   138,   139,   140,
     141,   142,   143,   147,   148,   149,   150,   151,   153,   153,
     153,   154,   155,   156,   156,   158,   158,   159,   161,   161,
     163,   164,   165,   166,   170,   171,   172,   173,   174,   175,
     176,   177,   178,   179,   180,   181,   182,   190,   190,   191,
     191,   191,   193,   193,   193,   193,   194,   194,   195,   195,
     196,   196,   196,   196,   196,   196,   199,   199,   199,   202,
     204,   204,   207,   208,   209,   210,   211,   212,   213,   214,
     215,   216,   217,   218,   219,   220,   221,   226,   231,   231,
     231,   231,   232,   232,   233,   233,   234,   234,   234,   239,
     240,   241,   242,   243,   244,   245,   246,   247,   248,   249,
     250,   251,   252,   253,   254,   255,   256,   257,   258,   259,
     260,   261,   262,   263,   264,   265,   266,   267,   268,   269,
     270,   271,   272,   273,   274,   275,   276,   277,   281,   281,
     282,   282,   284,   286,   287,   288,   289,   289,   290,   291,
     291,   292,   292,   293,   293,   295,   295,   296,   296,   299,
     299,   299,   299,   299,   299,   299,   301,   301,   303,   303,
     303,   304,   306,   306,   306,   306,   306,   306,   306,   306,
     306,   306,   306,   306,   308,   308,   308,   308,   308,   308,
     308,   308,   308,   308,   308,   308,   308,   310,   311,   311,
     313,   314,   315,   319,   320,   321,   322,   323,   327,   328,
     329,   330,   330,   330,   330,   330,   330,   334,   335,   336,
     337,   338,   339,   340,   341,   341,   341,   341,   341,   341,
     342,   343,   344,   345,   346,   347,   348,   349,   350,   351,
     352,   353,   354,   355,   356,   357,   358,   359,   360,   361,
     362,   363,   364,   365,   366,   367,   368,   369,   370,   371,
     372,   373,   374,   375,   376,   377,   378,   379,   380,   381,
     382,   383
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
     144,   144,   144,   144,   145,   146,   146,   147,   147,   148,
     148,   148,   148,   148,   148,   148,   148,   148,   148,   148,
     149,   149,   149,   149,   150,   151,   151,   151,   151,   151,
     151,   151,   151,   152,   152,   153,   153,   153,   153,   153,
     153,   153,   153,   153,   154,   154,   154,   154,   155,   155,
     156,   156,   156,   156,   156,   156,   156,   156,   156,   156,
     156,   156,   156,   157,   157,   157,   157,   157,   158,   158,
     158,   159,   160,   161,   161,   162,   162,   163,   164,   164,
     165,   165,   165,   165,   166,   166,   166,   166,   166,   166,
     166,   166,   166,   166,   166,   166,   166,   167,   167,   168,
     168,   168,   169,   169,   169,   169,   170,   170,   171,   171,
     172,   172,   172,   172,   172,   172,   173,   173,   173,   174,
     175,   175,   176,   176,   176,   176,   176,   176,   176,   176,
     176,   176,   176,   176,   176,   176,   176,   177,   178,   178,
     178,   178,   179,   179,   180,   180,   181,   181,   181,   182,
     182,   182,   182,   182,   182,   182,   182,   182,   182,   182,
     182,   182,   182,   182,   182,   182,   182,   182,   182,   182,
     182,   182,   182,   182,   182,   182,   182,   182,   182,   182,
     182,   182,   182,   182,   182,   182,   182,   182,   183,   183,
     184,   184,   185,   186,   187,   188,   189,   189,   190,   191,
     191,   192,   192,   193,   193,   194,   194,   195,   195,   196,
     196,   196,   196,   196,   196,   196,   197,   197,   198,   198,
     198,   199,   200,   200,   200,   200,   200,   200,   200,   200,
     200,   200,   200,   200,   201,   201,   201,   201,   201,   201,
     201,   201,   201,   201,   201,   201,   201,   202,   203,   203,
     204,   204,   204,   205,   205,   205,   205,   205,   206,   206,
     206,   206,   206,   206,   206,   206,   206,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207
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
       1,     1,     1,     1,     1,     5,     7,     9,     2,     2,
       2,     4,     1,     1,     3,     1,     2,     2,     1,     3,
       2,     2,     5,     3,     4,     5,     4,     5,     5,     7,
       3,     3,     3,     4,     3,     5,     2,     3,     3,     4,
       5,     6,     7,     6,     6,     7,     6,     7,     3,     3,
       2,     1,     1,     1,     2,     1,     5,     3,     3,     1,
       3,     1,     3,     9,     5,     5,     3,     1,     3,     2,
       1,     3,     3,     3,     3,     3,     1,     2,     1,     1,
       2,     3,     3,     2,     1,     1,     3,     1,     5,     5,
       5,     3,     1,     1,     1,     2,     2,     2,     2,     2,
       2,     3,     2,     2,     1,     1,     1,     1,     1,     1,
       2,     2,     1,     1,     1,     1,     1,     3,     3,     1,
       2,     1,     2,     3,     3,     4,     4,     6,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     4,     1,     1,     1,     1,     1,     1,
       2,     3,     3,     2,     5,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       4,     3,     1,     2,     2,     2,     2,     2,     2,     2,
       2,     2
};

/* YYDEFACT[STATE-NAME] -- Default rule to reduce with in state
   STATE-NUM when YYTABLE doesn't specify something else to do.  Zero
   means the default is an error.  */
static const yytype_uint16 yydefact[] =
{
       0,     0,     0,     0,     2,     4,     5,     6,    10,     0,
      41,    40,     1,     3,     0,     0,     0,   309,   307,   314,
     315,   316,   317,   318,   319,   311,   312,   310,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   352,
     308,    42,     0,     0,    11,    25,     0,     0,     0,     0,
     320,   323,     0,   357,   359,   358,   354,   356,   355,   353,
       0,     0,     0,   289,   291,   360,   361,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     9,     0,   119,    21,
     262,   263,   264,     0,     0,    15,     0,     0,     0,   275,
     276,   274,   285,   286,   277,     0,   278,   279,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   282,   283,
     284,    39,     0,     0,    25,    37,    34,    26,    27,    35,
      36,    31,    32,    33,    28,    29,    30,    38,     0,     0,
       0,     0,   246,   294,   293,     0,   321,   322,     0,   351,
     292,     0,   287,   290,   336,   337,   342,   341,   343,   345,
     346,   335,   338,   339,   340,     0,   331,   330,   332,   349,
     348,   347,   333,   334,   325,   327,   344,   326,   328,   329,
       0,     0,     0,     0,     0,     8,     0,   266,   273,   269,
     265,   267,   272,   270,   268,    13,     0,     0,    16,     0,
       0,     0,     0,     0,     0,   249,     0,     0,     0,     0,
       0,   237,     0,   255,   254,   280,   281,   257,     0,   249,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   157,   225,   221,   222,   223,     0,   254,     0,
       0,     0,   114,     0,     0,     0,     0,     0,   116,     0,
       0,     0,     0,    44,     0,    74,     0,    73,     0,     0,
     231,     0,   229,     0,     0,     0,   282,   173,   165,   166,
     167,   168,   169,   170,   172,     0,   161,   171,   174,   156,
       7,    24,     0,     0,    45,    48,     0,     0,     0,    43,
     350,     0,     0,   295,   296,     0,     0,     0,   261,   313,
     288,     0,   123,     0,     0,     0,     0,   118,   271,    12,
      14,     0,    18,    17,     0,     0,   126,     0,   151,   153,
     152,     0,     0,     0,   250,   253,   143,   144,   145,     0,
      65,    66,    67,    68,    69,    70,    71,    72,     0,     0,
       0,     0,    60,     0,     0,     0,    52,     0,   220,     0,
       0,     0,     0,   190,     0,   248,     0,     0,     0,     0,
       0,     0,     0,   191,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   180,   179,   178,     0,   206,   158,     0,
       0,   224,     0,     0,   111,     0,     0,     0,     0,     0,
     103,     0,     0,     0,   108,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   232,     0,     0,     0,     0,     0,
       0,   159,   160,    49,     0,     0,     0,    53,     0,   257,
       0,    45,     0,     0,   245,     0,     0,     0,     0,   324,
     121,     0,   120,   298,   301,   302,   303,   304,   305,   306,
     300,   299,    22,     0,    19,    20,     0,     0,     0,   138,
       0,     0,   155,     0,     0,   147,     0,     0,     0,     0,
     251,   252,     0,     0,     0,     0,     0,   236,   238,   256,
       0,     0,     0,   202,     0,   201,     0,   189,   247,     0,
     200,   207,     0,     0,     0,     0,     0,   193,   208,     0,
     204,     0,   227,   218,   219,     0,     0,     0,   185,   188,
       0,     0,     0,     0,     0,     0,     0,   113,   112,   117,
     104,     0,   115,   105,     0,   109,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    89,     0,     0,     0,     0,
       0,     0,     0,   230,   228,     0,   162,     0,     0,   164,
      50,     0,    46,    57,    45,    47,     0,    58,     0,    54,
       0,   297,   259,   260,   258,   122,    23,   124,     0,   139,
       0,     0,     0,     0,     0,   149,   154,     0,   150,   132,
       0,     0,     0,   142,     0,     0,     0,     0,   209,     0,
       0,   203,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   186,   187,   182,   181,   183,     0,     0,   196,     0,
     194,     0,     0,   127,   107,   106,   110,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    88,     0,    76,
       0,     0,     0,     0,     0,     0,    85,     0,     0,     0,
      51,     0,    56,    55,     0,   129,   137,   131,     0,     0,
       0,   146,   125,     0,     0,    64,     0,    63,    61,   210,
     226,   192,   198,     0,     0,   240,     0,     0,     0,     0,
       0,   235,   205,   234,   184,   197,   195,   130,   128,     0,
       0,    97,     0,     0,     0,    90,   257,     0,     0,   101,
       0,    91,    92,    75,     0,     0,    79,     0,     0,     0,
       0,    84,   163,   175,     0,    59,   141,     0,   135,   136,
       0,   133,     0,    62,     0,     0,   211,   239,     0,   213,
       0,   214,     0,   216,     0,     0,     0,     0,   100,    98,
       0,     0,     0,    93,     0,   102,     0,    78,     0,     0,
       0,     0,     0,     0,     0,     0,   140,   148,   134,   199,
     244,   243,   212,   242,   241,   215,   217,     0,     0,    80,
      99,     0,    94,    95,     0,     0,    90,     0,   101,    77,
       0,    86,   176,     0,     0,    81,    96,     0,    82,    93,
      87,     0,   233,    83,   177
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,     3,     4,     5,     6,    15,    45,   104,   105,   133,
     134,     7,   287,   305,   306,   288,   289,   218,   358,   276,
     139,   140,   544,   545,   290,   291,   292,   262,   263,   267,
     268,    97,    98,   293,   468,   469,   219,   474,   475,   214,
     294,   146,   295,   296,   297,   272,   616,   517,   518,   375,
     281,   282,   253,   254,   255,   256,   220,   221,   674,   675,
     676,   677,   376,   257,   228,   344,   345,   148,   149,    39,
      62,    63,    40,   462,   152
};

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
#define YYPACT_NINF -627
static const yytype_int16 yypact[] =
{
      28,    65,    81,    62,    28,  -627,  -627,  -627,   -24,   102,
    1788,  -627,  -627,  -627,    -8,   -39,    33,  -627,   124,  -627,
    -627,  -627,  -627,  -627,  -627,  -627,    75,  -627,  1788,  1788,
    1788,  1788,  1788,  1788,  1788,  1788,  1443,  1788,  1788,  -627,
    -627,  5013,    73,    50,  -627,  3874,   163,  1788,   168,  1788,
    -627,    82,  1788,  -627,  -627,  -627,  -627,  -627,  -627,  -627,
    4126,    89,   -69,  -627,  2650,  -627,  -627,  1788,  1788,  1788,
    1788,  1788,  1788,  1788,  1788,  1788,  1788,  1788,  1788,  1788,
    1788,  1788,  1788,  1788,  1788,  1788,  1788,  1788,  1788,  1788,
    1788,  1788,  1788,    99,    30,   222,  -627,    67,  -627,  -627,
     279,   242,   224,   125,   188,  -627,    12,    64,    16,   241,
     267,  -627,  -627,  -627,  -627,   289,  -627,  -627,  2599,    17,
     299,    22,    32,  2599,    24,   312,    27,  4128,  -627,  -627,
    -627,  -627,  2599,   273,  3874,  -627,  -627,  -627,  -627,  -627,
    -627,  -627,  -627,  -627,  -627,  -627,  -627,  -627,    34,    35,
     326,   204,  5013,   148,  -627,  2739,  -627,  -627,  4161,  -627,
    -627,  1443,  -627,  -627,  1851,  5107,   114,   114,   114,   254,
     254,  -627,  2679,  2679,  2679,  4924,  5042,  2679,   440,   952,
     952,   952,   254,   254,   275,   275,   114,  -627,  -627,  -627,
    1788,   165,  1788,   339,   200,  -627,    20,  -627,  -627,  -627,
     343,  -627,  -627,  -627,  -627,  -627,   253,   313,   248,   378,
      36,   -47,    61,  1788,   382,   214,    86,   344,    11,    18,
     -73,  -627,   268,  -627,  -627,  -627,  -627,   280,   303,   115,
      18,    34,   289,  2030,   381,  1788,   424,   383,   385,   393,
    2599,   394,   395,  2599,   443,  1788,  1788,   396,   453,  1788,
      96,  2126,  -627,  -627,  -627,  -627,  -627,    -6,   341,   397,
    1788,   399,  -627,     5,   402,   403,    32,   190,  -627,    32,
     212,    32,   406,  -627,   223,  -627,   513,   392,   227,   408,
    -627,   -23,  -627,  1815,   401,   409,   289,  -627,  -627,  -627,
    -627,  -627,  -627,  -627,  -627,  3966,  -627,  -627,  -627,  -627,
    -627,  -627,   412,   289,   154,  -627,   229,   525,    37,  -627,
    -627,  1788,  1788,  -627,  -627,  1788,  1788,  1788,  -627,  -627,
    -627,  1788,  5013,  1788,  4895,   411,  1788,  -627,  -627,  -627,
    -627,   375,  -627,   175,   531,   867,  -627,   417,  -627,  -627,
    -627,   927,   250,   -11,  -627,    82,  -627,  -627,  -627,  1788,
    -627,  -627,  -627,  -627,  -627,  -627,  -627,  -627,   415,    18,
     416,   428,  -627,    18,  1788,   289,  -627,  1475,  -627,   433,
     419,   289,   420,  -627,   534,  -627,  2147,  1788,  2985,   423,
    1788,  1788,  1788,  -627,    18,  1788,  2236,   438,  2896,  3014,
    1788,   439,  1893,  -627,  -627,  -627,  1103,  -627,  -627,  1498,
    1498,  -627,  1615,   263,  -627,   299,  1788,  1788,   233,   557,
    -627,   557,   240,   557,  -627,   286,   557,   313,  2009,   282,
     558,   313,  2009,  1788,  -627,    27,   560,  4020,  1788,    18,
     445,  -627,  -627,  -627,    90,  1788,   446,  -627,   564,   274,
     448,   154,   367,   564,  5013,  4255,   807,  2773,  2862,  5013,
    5013,  1788,  5013,  -627,  -627,  -627,  -627,  -627,  -627,  -627,
    -627,  -627,  -627,   375,  -627,  -627,   449,    58,   284,  -627,
     298,  1615,  -627,   567,   301,  -627,   305,   452,     4,   455,
    -627,  -627,   309,   344,   456,  1788,  1788,  -627,  5013,  -627,
     457,   314,  1788,  -627,   459,  -627,  2599,  -627,  -627,  4289,
    -627,  -627,  4383,  4417,  4511,   369,  4545,  -627,  -627,  1788,
    -627,  4639,  -627,  -627,  -627,  1788,  1788,   -18,  -627,  5013,
    1788,  3109,  1788,  3138,   315,   319,   461,  -627,  5013,  5013,
    -627,   371,  -627,  -627,   373,  -627,   376,   320,    25,   574,
      34,   289,   289,   289,  2009,  -627,  2296,   313,  2009,   464,
     323,  2009,   528,  5013,  -627,  4128,  -627,  4673,   386,  -627,
    -627,   466,  5013,  -627,   465,  -627,  1788,  -627,   468,  -627,
     389,  -627,  -627,  -627,  -627,  5013,  -627,  -627,   472,  -627,
     474,   475,   477,   324,   328,   481,  -627,   479,  -627,  -627,
     483,   332,   475,  -627,   485,  1788,  3233,  3262,  -627,   486,
    3357,  -627,  2359,  2599,  1647,  1788,  1788,  1788,  2599,  3386,
    2599,  5013,  5013,  -627,  -627,  -627,  1103,  3481,  -627,  3510,
    -627,   487,   488,  -627,  -627,  -627,  -627,   489,   289,   134,
     392,   392,   491,    42,   147,   492,   494,  -627,  2419,  -627,
     333,  2009,   550,   211,   495,   559,  -627,  4074,  4128,  1788,
    -627,  3605,  -627,  -627,  1670,  -627,  -627,  -627,   497,   498,
    1788,  -627,  -627,   499,   338,  -627,  3634,  -627,  -627,  -627,
    -627,  -627,   586,   529,  1220,  -627,   576,   -66,  1310,  1354,
    3729,  -627,  -627,  -627,  -627,  -627,  -627,  -627,  -627,  2009,
     508,  -627,   509,   289,   392,   405,    88,   510,   628,   418,
     512,  -627,  -627,  -627,   514,   578,  -627,    34,   289,  2009,
    2009,  -627,  -627,   598,  3758,  -627,  -627,  4767,  -627,  -627,
    4801,  -627,   518,  -627,  2599,  2479,  -627,  -627,   589,  -627,
    2539,  -627,   590,  -627,   591,    18,  2009,   587,  -627,  -627,
     524,   642,   526,   421,   532,  -627,  2009,  -627,   536,    42,
     149,   594,  2009,   597,  4128,    18,  -627,  -627,  -627,  -627,
    -627,  -627,  -627,  -627,  -627,  -627,  -627,   358,   603,  -627,
    -627,   539,  -627,  -627,  2009,   605,  -627,   542,  -627,  -627,
     608,  -627,  -627,   361,  2599,  -627,  -627,   611,  -627,  -627,
    -627,  4128,  -627,  -627,  -627
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -627,  -627,  -627,   665,  -627,  -627,  -627,  -403,   463,   537,
    -627,    -2,    26,   234,  -293,    51,    53,  -627,   191,  -627,
    -627,  -627,  -417,  -531,    57,    59,    68,   270,  -627,  -113,
     262,  -627,   480,    74,  -394,    97,  -199,  -627,    92,   533,
      79,  -627,  -273,  -294,  -627,   572,  -627,  -627,    77,   -26,
    -627,   252,   -45,  -627,  -627,  -627,  -378,   334,  -139,  -626,
    -433,   -21,  -236,   -96,   -55,    -7,   -15,   -41,  -627,    47,
    -627,   535,   -44,   232,   775
};

/* YYTABLE[YYPACT[STATE-NUM]].  What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule which
   number is the opposite.  If zero, do what YYDEFACT says.
   If YYTABLE_NINF, syntax error.  */
#define YYTABLE_NINF -204
static const yytype_int16 yytable[] =
{
     147,   432,   106,    51,   154,   551,   505,   386,   524,   270,
     427,    50,   222,   637,   537,   442,   215,   208,   550,   359,
     637,   215,   259,   215,   613,    93,   151,   265,   399,   274,
     227,     1,   279,   209,   730,   191,   157,   265,   266,   227,
     304,   333,   441,   135,   156,   275,   628,   696,   727,   362,
     363,   558,   727,   727,   161,    99,   424,   311,   100,   101,
     102,   162,    12,   578,   224,   338,   339,    94,    95,   211,
       8,   136,   280,   335,   258,   336,   264,   583,    93,   258,
     192,    43,   298,    44,   591,     9,    10,   193,   258,   147,
     346,   347,   252,   302,     2,    14,   137,   273,   138,   210,
     425,   393,   141,   614,   142,   615,   299,    16,   160,   478,
     637,   163,    42,   143,   269,   271,   192,   277,   400,   144,
      94,    95,   360,   361,   145,   590,    11,   404,   405,   467,
     216,   641,   135,   432,   369,   216,   217,   260,   314,   192,
      36,   303,   308,   340,   640,    36,   313,    36,    46,   192,
     570,   192,   192,   408,   212,   223,   412,   192,   415,   192,
     136,   192,   192,   192,   192,   223,   106,   150,   348,   192,
     223,   103,   579,   153,   224,   224,   370,   372,   637,   223,
     394,   341,   546,   212,   213,   137,   224,   138,   195,   258,
     196,   141,   342,   142,    96,    52,   258,    74,   664,   258,
     520,   522,   143,   334,   337,   637,   349,   258,   144,    49,
     395,   365,   560,   145,   383,   192,   396,   192,    36,   538,
     539,   637,   707,   190,   371,   398,   709,   194,    90,    91,
      92,   430,   708,   542,   543,   367,   204,   368,   298,   403,
      48,   728,    49,   637,    47,   732,   734,   205,   434,    48,
     298,    49,   440,   200,   201,   202,   691,   225,   203,   409,
     602,   192,   413,   484,   416,   223,   223,   222,   312,   699,
     420,   778,   736,    48,   192,    49,   192,   223,   435,   300,
     223,   192,   647,   226,    69,    70,    71,   223,   222,   323,
     223,   197,   198,   752,   227,   199,   531,   436,   223,   463,
     534,   443,   192,   536,   261,    69,    70,    71,   638,   206,
     489,   207,   410,   411,   470,   224,   494,   278,    99,   224,
     476,   100,   101,   102,   326,   310,   464,   311,   482,   774,
     481,   309,   258,   222,   414,   411,   479,    74,   480,    48,
     224,    49,   258,   417,   325,   418,   491,   421,   258,   422,
     498,   437,   438,   432,   713,   530,   411,   767,    74,   328,
     498,   264,   533,   411,    87,    88,   514,    89,    90,    91,
      92,   477,   331,   311,   258,   329,   106,   783,   258,   453,
     106,   525,   298,   332,   526,   224,   311,   343,    89,    90,
      91,    92,   364,   454,   455,   456,   552,   365,   566,   457,
     458,   459,   547,   365,   548,   580,   223,   581,   535,   411,
     223,   350,   351,   352,   353,   354,   355,   356,   357,   582,
     460,   311,   586,   223,   587,   366,   588,   561,   311,   379,
     593,   223,   311,   223,   568,   599,   621,   311,   581,   223,
     622,   627,   311,   207,   644,   658,   207,   581,   387,   659,
     584,   311,   258,   663,   704,   581,   207,   461,   391,   722,
     782,   581,  -202,   401,  -202,   223,   678,   679,    67,   223,
      69,    70,    71,    72,    73,  -201,   223,  -201,  -203,   784,
    -203,   363,   791,   629,   363,   632,   634,   635,   636,   569,
     438,   607,   363,   624,   411,   625,   411,   794,   626,   411,
     258,   377,   258,   380,   258,   381,   106,   258,   649,   363,
     298,   653,   438,   382,   384,   385,   390,   402,   419,   192,
     498,   428,   642,    74,    48,   645,   406,   407,   397,   429,
     439,   630,   423,   633,   433,   451,   465,   471,   483,   496,
     485,   493,   495,   223,    82,   501,    83,    84,    85,    86,
      87,    88,   486,    89,    90,    91,    92,   492,   258,   258,
     508,   512,   265,   549,   258,   555,   258,   559,   563,   564,
     567,   577,   585,   690,   589,   592,   498,   672,   697,   598,
     595,   601,   681,   623,   683,   631,   643,   646,   650,   435,
     652,   223,   654,   223,   258,   223,   655,   258,   223,   657,
     467,   660,   298,   298,   473,   662,   665,   706,   669,   687,
     688,   689,   498,   695,   701,   705,   702,   710,   711,   718,
     719,   721,   692,   693,   694,   724,   698,   700,   729,   725,
     738,   739,   743,   744,   745,   747,   746,   754,   740,   222,
     758,   762,   765,   766,   769,   258,   770,   771,   772,   223,
     223,   779,   748,   750,   773,   223,   781,   223,   776,   222,
     785,   786,   788,   737,   789,   258,   258,   790,   793,    13,
     330,   301,   565,   532,   594,   527,   327,   554,   656,   661,
     258,   258,   307,   751,   753,   223,   258,   741,   223,   742,
     251,   224,   258,   684,   777,   576,   320,   487,   759,   761,
     749,     0,   258,     0,   764,     0,     0,     0,   258,   298,
     768,   224,     0,     0,     0,     0,     0,     0,     0,     0,
     775,     0,     0,     0,     0,     0,   780,     0,     0,     0,
     258,     0,     0,     0,     0,     0,   223,     0,     0,     0,
     258,     0,   698,   700,     0,     0,   298,     0,   787,     0,
       0,     0,     0,     0,     0,     0,   223,   223,   792,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   223,   223,     0,     0,     0,     0,   223,     0,     0,
       0,     0,   223,   223,     0,    41,     0,     0,     0,     0,
       0,     0,     0,   223,     0,     0,     0,     0,     0,   223,
       0,     0,   223,    53,    54,    55,    56,    57,    58,    59,
      60,    64,    65,    66,     0,     0,     0,     0,     0,     0,
       0,   223,     0,     0,   155,     0,     0,   158,     0,     0,
       0,   223,     0,     0,     0,    67,    68,    69,    70,    71,
      72,    73,   164,   165,   166,   167,   168,   169,   170,   171,
     172,   173,   174,   175,   176,   177,   178,   179,   180,   181,
     182,   183,   184,   185,   186,   187,   188,   189,     0,     0,
       0,    17,    18,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    19,    20,    21,     0,     0,
      74,    22,    23,    24,     0,     0,     0,    75,    76,    77,
       0,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,    25,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,     0,     0,
       0,    17,    18,    26,     0,   572,    64,     0,     0,     0,
       0,     0,     0,     0,     0,    19,    20,    21,     0,    27,
       0,    22,    23,    24,     0,     0,     0,    28,    29,    30,
       0,     0,     0,     0,     0,   322,     0,   324,    31,    32,
      33,     0,    25,     0,     0,     0,     0,     0,    34,     0,
       0,     0,    69,    70,    71,    72,    73,    35,   466,     0,
       0,     0,   467,    26,     0,     0,    36,     0,    37,    38,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    27,
     378,     0,     0,     0,     0,     0,     0,    28,    29,    30,
     388,   389,     0,     0,   392,     0,     0,     0,    31,    32,
      33,     0,     0,     0,     0,    74,     0,     0,    34,     0,
       0,     0,     0,     0,     0,     0,     0,    35,   472,     0,
       0,     0,   473,     0,     0,     0,    36,     0,    37,    38,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   444,   445,     0,     0,
     446,   447,   448,     0,     0,     0,   449,     0,   450,     0,
       0,   452,     0,     0,     0,     0,     0,    17,    18,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    19,    20,    21,     0,     0,     0,    22,    23,    24,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   488,
       0,     0,     0,   515,   516,     0,     0,     0,    25,     0,
       0,     0,   499,     0,     0,   502,   503,   504,     0,     0,
     506,     0,     0,     0,     0,   511,     0,     0,     0,    26,
       0,   519,     0,     0,   521,   523,     0,     0,     0,     0,
       0,   528,   529,     0,     0,    27,     0,     0,     0,     0,
       0,     0,     0,    28,    29,    30,     0,     0,   553,     0,
       0,     0,     0,   557,    31,    32,    33,     0,     0,     0,
     562,     0,     0,     0,    34,     0,     0,     0,     0,     0,
       0,     0,     0,    35,    17,    18,   575,     0,     0,     0,
       0,     0,    36,     0,    37,    38,     0,     0,    19,    20,
      21,     0,     0,     0,    22,    23,    24,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     596,   597,     0,     0,     0,    25,     0,   600,     0,     0,
       0,     0,   726,   673,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   609,     0,    26,     0,     0,     0,
     611,   612,     0,     0,     0,   617,     0,   619,     0,     0,
       0,     0,    27,     0,     0,     0,     0,     0,     0,     0,
      28,    29,    30,     0,    17,    18,     0,     0,     0,     0,
       0,    31,    32,    33,     0,     0,     0,     0,    19,    20,
      21,    34,     0,     0,    22,    23,    24,     0,     0,     0,
      35,   651,     0,     0,     0,     0,     0,     0,     0,    36,
       0,    37,    38,     0,     0,    25,     0,     0,    17,    18,
       0,     0,   731,   673,     0,     0,     0,     0,     0,     0,
     666,     0,    19,    20,    21,     0,    26,     0,    22,    23,
      24,     0,   680,     0,     0,     0,     0,     0,     0,     0,
       0,   519,    27,     0,     0,     0,     0,     0,     0,    25,
      28,    29,    30,     0,     0,     0,   733,   673,     0,     0,
       0,    31,    32,    33,     0,     0,     0,     0,     0,     0,
      26,    34,     0,     0,   714,     0,     0,     0,     0,   717,
      35,     0,     0,     0,     0,   720,    27,     0,     0,    36,
       0,    37,    38,     0,    28,    29,    30,    17,    18,     0,
       0,     0,     0,     0,     0,    31,    32,    33,     0,     0,
       0,    19,    20,    21,     0,    34,     0,    22,    23,    24,
       0,     0,     0,     0,    35,     0,     0,     0,     0,    17,
      18,     0,     0,    36,     0,    37,    38,     0,    25,     0,
       0,     0,     0,    19,    20,    21,     0,     0,     0,    22,
      23,    24,    17,    18,     0,     0,     0,     0,     0,    26,
       0,     0,     0,     0,     0,     0,    19,    20,    21,     0,
      25,     0,    22,    23,    24,    27,     0,     0,     0,     0,
       0,     0,     0,    28,    29,    30,     0,     0,     0,     0,
       0,    26,     0,    25,    31,    32,    33,     0,     0,     0,
      61,     0,     0,     0,    34,     0,     0,    27,     0,     0,
       0,     0,     0,    35,    26,    28,    29,    30,     0,     0,
       0,     0,    36,     0,    37,    38,    31,    32,    33,     0,
      27,     0,     0,     0,     0,     0,    34,     0,    28,    29,
      30,     0,     0,     0,     0,    35,   490,     0,     0,    31,
      32,    33,     0,     0,    36,     0,    37,    38,     0,    34,
       0,     0,     0,     0,     0,     0,     0,   216,    35,    17,
      18,     0,     0,     0,     0,     0,     0,    36,     0,    37,
      38,     0,     0,    19,    20,    21,     0,     0,     0,    22,
      23,    24,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    17,    18,     0,     0,     0,     0,     0,     0,     0,
      25,     0,     0,     0,     0,    19,    20,    21,     0,     0,
       0,    22,    23,    24,    17,    18,     0,     0,     0,     0,
       0,    26,     0,     0,     0,     0,     0,     0,    19,    20,
      21,     0,    25,     0,    22,    23,    24,    27,     0,     0,
     673,     0,     0,     0,     0,    28,    29,    30,     0,     0,
       0,     0,     0,    26,     0,    25,    31,    32,    33,     0,
       0,     0,     0,     0,     0,     0,    34,     0,     0,    27,
       0,     0,     0,     0,     0,    35,    26,    28,    29,    30,
     467,     0,     0,     0,    36,     0,    37,    38,    31,    32,
      33,     0,    27,     0,     0,     0,     0,     0,    34,     0,
      28,    29,    30,     0,     0,     0,     0,    35,     0,     0,
       0,    31,    32,    33,     0,     0,    36,     0,    37,    38,
       0,    34,     0,     0,     0,     0,     0,     0,     0,     0,
      35,   716,    17,    18,     0,     0,     0,     0,     0,    36,
       0,    37,    38,     0,     0,     0,    19,    20,    21,     0,
       0,     0,    22,    23,    24,     0,     0,     0,     0,     0,
     107,     0,   108,   100,   101,   102,   109,   110,   111,   112,
     113,   114,   115,    25,     0,     0,   116,   117,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     118,   283,     0,   284,    26,     0,     0,   119,     0,     0,
       0,   120,   121,   122,     0,     0,     0,     0,     0,   123,
      27,     0,     0,     0,     0,   285,     0,     0,    28,    29,
      30,    69,    70,    71,    72,    73,     0,     0,     0,    31,
      32,    33,     0,   126,     0,     0,     0,     0,   229,    34,
     230,     0,   286,     0,   231,     0,     0,     0,    35,   129,
     130,     0,     0,   132,   232,   426,     0,    36,     0,    37,
      38,    67,    68,    69,    70,    71,    72,    73,     0,   233,
       0,   234,     0,     0,    74,     0,   235,   236,     0,     0,
       0,     0,   237,   238,   239,     0,     0,     0,   240,     0,
       0,     0,     0,   241,   242,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,   243,     0,
     244,   126,     0,     0,     0,     0,    74,     0,     0,     0,
       0,   245,   246,    75,    76,    77,   247,     0,     0,     0,
     248,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
       0,     0,   249,     0,   229,   513,   230,   538,   539,   250,
     540,     0,    36,     0,     0,     0,     0,     0,     0,     0,
     541,   542,   543,     0,     0,   229,     0,   230,     0,     0,
       0,   231,     0,     0,     0,   233,     0,   234,     0,     0,
       0,   232,   235,   236,     0,     0,     0,     0,   237,   238,
     239,     0,     0,     0,   240,     0,   233,   373,   234,   241,
     242,     0,     0,   235,   236,     0,     0,     0,     0,   237,
     238,   239,     0,     0,   243,   240,   244,   126,     0,     0,
     241,   242,     0,     0,     0,     0,     0,   245,   246,     0,
       0,     0,   247,     0,     0,   243,   248,   244,   126,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   245,   246,
       0,     0,     0,   247,     0,     0,     0,   248,   249,     0,
     374,   229,     0,   230,     0,   250,     0,   231,    36,     0,
       0,     0,     0,     0,     0,     0,     0,   232,     0,   249,
       0,     0,   229,     0,   230,     0,   250,     0,   231,    36,
       0,     0,   233,     0,   234,     0,     0,     0,   232,   235,
     236,     0,     0,     0,     0,   237,   238,   239,     0,     0,
       0,   240,     0,   233,   497,   234,   241,   242,     0,     0,
     235,   236,     0,     0,     0,     0,   237,   238,   239,     0,
       0,   243,   240,   244,   126,     0,     0,   241,   242,     0,
       0,     0,     0,     0,   245,   246,     0,     0,     0,   247,
       0,     0,   243,   248,   244,   126,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   245,   246,     0,     0,     0,
     247,   229,     0,   230,   248,   249,     0,   231,   397,     0,
       0,     0,   250,     0,     0,    36,     0,   232,     0,     0,
       0,     0,     0,     0,     0,     0,   249,     0,     0,     0,
       0,     0,   233,   250,   234,     0,    36,     0,     0,   235,
     236,     0,     0,     0,     0,   237,   238,   239,     0,     0,
       0,   240,     0,     0,     0,     0,   241,   242,     0,     0,
       0,   229,     0,   230,     0,     0,     0,   231,     0,     0,
       0,   243,   507,   244,   126,     0,     0,   232,     0,     0,
       0,     0,     0,     0,   245,   246,     0,     0,     0,   247,
       0,     0,   233,   248,   234,     0,     0,     0,     0,   235,
     236,     0,     0,     0,     0,   237,   238,   239,     0,     0,
       0,   240,     0,   639,     0,   249,   241,   242,     0,     0,
       0,     0,   250,     0,   229,    36,   230,     0,     0,     0,
     231,   243,     0,   244,   126,     0,     0,     0,     0,     0,
     232,     0,     0,     0,   245,   246,     0,     0,     0,   247,
       0,     0,     0,   248,     0,   233,   671,   234,     0,     0,
       0,     0,   235,   236,     0,     0,     0,     0,   237,   238,
     239,     0,     0,     0,   240,   249,     0,     0,     0,   241,
     242,     0,   250,     0,   229,    36,   230,     0,     0,     0,
     231,     0,     0,     0,   243,     0,   244,   126,     0,     0,
     232,     0,     0,     0,     0,     0,     0,   245,   246,     0,
       0,     0,   247,     0,     0,   233,   248,   234,     0,     0,
       0,     0,   235,   236,     0,     0,     0,     0,   237,   238,
     239,     0,     0,     0,   240,     0,   703,     0,   249,   241,
     242,     0,     0,     0,   229,   250,   230,     0,    36,     0,
     231,     0,     0,     0,   243,     0,   244,   126,     0,     0,
     232,     0,     0,     0,     0,     0,     0,   245,   246,     0,
       0,     0,   247,     0,     0,   233,   248,   234,     0,     0,
       0,     0,   235,   236,     0,     0,     0,     0,   237,   238,
     239,     0,     0,     0,   240,     0,     0,     0,   249,   241,
     242,     0,     0,     0,   229,   250,   230,     0,    36,     0,
     231,     0,     0,     0,   243,     0,   244,   126,     0,     0,
     232,     0,     0,     0,     0,     0,     0,   245,   246,     0,
       0,     0,   247,     0,     0,   233,   248,   234,     0,     0,
       0,     0,   235,   236,     0,     0,     0,     0,   237,   238,
     239,     0,     0,     0,   240,     0,     0,     0,   249,   241,
     242,   760,     0,     0,   229,   250,   230,     0,    36,     0,
     231,     0,     0,     0,   243,     0,   244,   126,     0,     0,
     232,     0,     0,     0,     0,     0,     0,   245,   246,     0,
       0,     0,   247,     0,     0,   233,   248,   234,     0,     0,
       0,     0,   235,   236,     0,     0,     0,     0,   237,   238,
     239,     0,     0,     0,   240,     0,     0,     0,   249,   241,
     242,   763,     0,     0,     0,   250,     0,     0,    36,     0,
       0,     0,     0,     0,   243,     0,   244,   126,    67,    68,
      69,    70,    71,    72,    73,     0,     0,   245,   246,     0,
       0,     0,   247,     0,     0,     0,   248,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    67,     0,    69,
      70,    71,    72,    73,     0,     0,     0,     0,   249,     0,
       0,     0,     0,     0,     0,   250,     0,     0,    36,     0,
       0,     0,     0,    74,     0,     0,     0,     0,     0,     0,
      75,    76,    77,     0,     0,     0,     0,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,    74,    89,    90,    91,    92,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,    36,
       0,     0,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,     0,     0,     0,     0,
       0,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   315,
     316,     0,    74,     0,     0,     0,     0,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,     0,    78,   317,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,    74,     0,     0,     0,
       0,     0,     0,    75,    76,    77,     0,   318,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,   573,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    74,     0,     0,     0,     0,
       0,     0,    75,    76,    77,     0,     0,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,    74,
       0,     0,     0,     0,     0,     0,    75,    76,    77,     0,
     574,     0,     0,     0,     0,    78,     0,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,    67,    68,    69,    70,    71,    72,    73,
     509,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,    74,    89,    90,
      91,    92,     0,     0,    75,    76,    77,   500,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,     0,     0,     0,     0,     0,   510,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    74,     0,     0,     0,     0,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,    74,    89,    90,    91,    92,     0,     0,    75,    76,
      77,   618,     0,     0,     0,     0,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,     0,     0,     0,     0,     0,
     620,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    74,     0,     0,     0,
       0,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,    74,    89,    90,    91,    92,
       0,     0,    75,    76,    77,   667,     0,     0,     0,     0,
       0,    78,     0,    79,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,     0,   668,    67,    68,    69,    70,    71,
      72,    73,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    67,    68,    69,    70,    71,    72,
      73,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      74,     0,     0,     0,     0,     0,     0,    75,    76,    77,
       0,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,    74,
      89,    90,    91,    92,     0,     0,    75,    76,    77,   670,
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
      75,    76,    77,   685,     0,     0,     0,     0,     0,    78,
       0,    79,    80,    81,    82,     0,    83,    84,    85,    86,
      87,    88,     0,    89,    90,    91,    92,     0,     0,     0,
       0,     0,   686,    67,    68,    69,    70,    71,    72,    73,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,    74,    89,    90,
      91,    92,     0,     0,    75,    76,    77,   715,     0,     0,
       0,     0,     0,    78,     0,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,     0,     0,     0,     0,     0,   723,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    67,    68,    69,    70,
      71,    72,    73,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    74,     0,     0,     0,     0,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,    74,    89,    90,    91,    92,     0,     0,    75,    76,
      77,   735,     0,     0,     0,     0,     0,    78,     0,    79,
      80,    81,    82,     0,    83,    84,    85,    86,    87,    88,
       0,    89,    90,    91,    92,     0,     0,     0,     0,   107,
     755,   108,   100,   101,   102,   109,   110,   111,   112,   113,
     114,   115,     0,     0,     0,   116,   117,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   118,
       0,     0,     0,     0,     0,     0,   119,     0,     0,     0,
     120,   121,   122,     0,     0,     0,     0,     0,   123,     0,
     124,     0,   125,     0,     0,     0,     0,     0,     0,     0,
       2,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   126,     0,     0,     0,     0,     0,     0,   127,
       0,   128,     0,     0,     0,     0,     0,     0,   129,   130,
     131,   107,   132,   108,   100,   101,   102,   109,   110,   111,
     112,   113,   114,   115,     0,     0,     0,   116,   117,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   118,   283,     0,   284,     0,     0,     0,   119,     0,
       0,     0,   120,   121,   122,     0,     0,     0,     0,     0,
     123,     0,     0,     0,     0,   107,   285,   108,   100,   101,
     102,   109,   110,   111,   112,   113,   114,   115,     0,     0,
       0,   116,   117,     0,   126,     0,     0,     0,     0,     0,
       0,     0,   431,   286,     0,   118,   283,   556,   284,     0,
     129,   130,   119,     0,   132,     0,   120,   121,   122,     0,
       0,     0,     0,     0,   123,     0,     0,     0,     0,   107,
     285,   108,   100,   101,   102,   109,   110,   111,   112,   113,
     114,   115,     0,     0,     0,   116,   117,     0,   126,     0,
       0,     0,     0,     0,     0,     0,     0,   286,     0,   118,
     283,   712,   284,     0,   129,   130,   119,     0,   132,     0,
     120,   121,   122,     0,     0,     0,     0,     0,   123,     0,
       0,     0,     0,   107,   285,   108,   100,   101,   102,   109,
     110,   111,   112,   113,   114,   115,     0,     0,     0,   116,
     117,     0,   126,     0,    67,    68,    69,    70,    71,    72,
      73,   286,     0,   118,   283,     0,   284,     0,   129,   130,
     119,     0,   132,     0,   120,   121,   122,     0,     0,     0,
       0,     0,   123,     0,     0,     0,     0,     0,   285,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   126,     0,     0,    74,
       0,     0,     0,     0,     0,   286,    75,    76,    77,     0,
       0,     0,   129,   130,     0,    78,   132,    79,    80,    81,
      82,     0,    83,    84,    85,    86,    87,    88,     0,    89,
      90,    91,    92,     0,    74,     0,     0,   159,     0,     0,
       0,    75,    76,    77,     0,     0,     0,     0,     0,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,     0,     0,
       0,     0,   319,    67,    68,    69,    70,    71,    72,    73,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,    74,     0,     0,     0,   571,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,     0,     0,     0,     0,
     603,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    67,    68,    69,    70,    71,
      72,    73,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    74,     0,     0,     0,
       0,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
      74,     0,     0,     0,   604,     0,     0,    75,    76,    77,
       0,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,     0,     0,     0,     0,   605,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    67,    68,    69,    70,    71,    72,    73,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    74,     0,     0,     0,     0,     0,
       0,    75,    76,    77,     0,     0,     0,     0,     0,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,    74,     0,
       0,     0,   606,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,     0,    78,     0,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,     0,    89,    90,
      91,    92,     0,     0,     0,     0,   608,    67,    68,    69,
      70,    71,    72,    73,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    74,     0,     0,     0,     0,     0,     0,    75,
      76,    77,     0,     0,     0,     0,     0,     0,    78,     0,
      79,    80,    81,    82,     0,    83,    84,    85,    86,    87,
      88,     0,    89,    90,    91,    92,    74,     0,     0,     0,
     610,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,     0,    89,    90,    91,    92,
       0,     0,     0,     0,   648,    67,    68,    69,    70,    71,
      72,    73,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    67,
      68,    69,    70,    71,    72,    73,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      74,     0,     0,     0,     0,     0,     0,    75,    76,    77,
       0,     0,     0,     0,     0,     0,    78,     0,    79,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92,    74,     0,     0,     0,   756,     0,
       0,    75,    76,    77,     0,     0,     0,     0,     0,     0,
      78,     0,    79,    80,    81,    82,     0,    83,    84,    85,
      86,    87,    88,     0,    89,    90,    91,    92,     0,     0,
       0,     0,   757,    67,    68,    69,    70,    71,    72,    73,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    67,    68,    69,    70,    71,    72,    73,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   315,   316,     0,    74,     0,
       0,     0,     0,     0,     0,    75,    76,    77,     0,     0,
       0,     0,     0,     0,    78,   317,    79,    80,    81,    82,
       0,    83,    84,    85,    86,    87,    88,    74,    89,    90,
      91,    92,     0,     0,    75,    76,    77,     0,     0,     0,
       0,     0,     0,    78,   321,    79,    80,    81,    82,     0,
      83,    84,    85,    86,    87,    88,     0,    89,    90,    91,
      92,    67,    68,    69,    70,    71,    72,    73,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      67,    68,    69,    70,    71,    72,    73,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    74,     0,     0,     0,
       0,     0,     0,    75,    76,    77,     0,     0,     0,     0,
       0,     0,    78,     0,    79,    80,    81,    82,     0,    83,
      84,    85,    86,    87,    88,    74,    89,    90,    91,    92,
       0,     0,    75,    76,    77,    67,     0,    69,    70,    71,
      72,    73,     0,     0,    80,    81,    82,     0,    83,    84,
      85,    86,    87,    88,     0,    89,    90,    91,    92,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      74,     0,     0,     0,     0,     0,     0,    75,    76,    77,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    80,
      81,    82,     0,    83,    84,    85,    86,    87,    88,     0,
      89,    90,    91,    92
};

static const yytype_int16 yycheck[] =
{
      45,   295,    43,    18,    48,   422,   384,   243,   402,   122,
     283,    18,   108,   544,   417,   308,     5,     5,   421,   218,
     551,     5,     5,     5,    42,     5,    47,     5,    34,     5,
       5,     3,     5,    21,   100,     5,    51,     5,    16,     5,
       5,     5,     5,    45,    51,    21,    21,     5,   674,   122,
     123,   429,   678,   679,   123,     5,    79,   123,     8,     9,
      10,   130,     0,     5,   108,     4,     5,    47,    48,     5,
       5,    45,    45,   120,   118,   122,   120,   471,     5,   123,
     127,   120,   127,   122,   478,     4,     5,    94,   132,   134,
       4,     5,   118,   148,    66,   119,    45,   123,    45,   106,
     123,     5,    45,   121,    45,   123,   132,     5,    61,   120,
     641,    64,   120,    45,   121,   122,   127,   124,   124,    45,
      47,    48,   218,   219,    45,   121,    45,   122,   123,   125,
     119,   548,   134,   427,   230,   119,   120,   120,   153,   127,
     129,   148,   149,    82,   547,   129,   153,   129,   115,   127,
     443,   127,   127,   266,   119,   108,   269,   127,   271,   127,
     134,   127,   127,   127,   127,   118,   207,     4,    82,   127,
     123,   121,   114,     5,   218,   219,   231,   232,   709,   132,
      84,   120,   418,   119,   120,   134,   230,   134,   121,   233,
     123,   134,   213,   134,   121,   120,   240,    83,   592,   243,
     399,   400,   134,   210,   211,   736,   120,   251,   134,   127,
     114,   123,   122,   134,   240,   127,   120,   127,   129,     8,
       9,   752,    11,   124,   231,   251,   643,     5,   114,   115,
     116,   286,    21,    22,    23,   120,    12,   122,   283,   260,
     125,   674,   127,   774,   120,   678,   679,   122,   303,   125,
     295,   127,   307,    11,    12,    13,   122,    16,    16,   266,
     496,   127,   269,   359,   271,   218,   219,   363,   120,   122,
     277,   122,   689,   125,   127,   127,   127,   230,   124,     6,
     233,   127,   555,    16,    30,    31,    32,   240,   384,   124,
     243,    12,    13,   710,     5,    16,   409,   304,   251,   124,
     413,   308,   127,   416,     5,    30,    31,    32,   544,   121,
     365,   123,   122,   123,   335,   359,   371,     5,     5,   363,
     341,     8,     9,    10,   124,   121,   333,   123,   349,   746,
     345,     5,   376,   429,   122,   123,   343,    83,   345,   125,
     384,   127,   386,   120,     5,   122,   367,   120,   392,   122,
     376,   122,   123,   647,   648,   122,   123,   735,    83,    16,
     386,   405,   122,   123,   110,   111,   392,   113,   114,   115,
     116,   121,   124,   123,   418,   122,   417,   755,   422,     4,
     421,   402,   427,     5,   121,   429,   123,     5,   113,   114,
     115,   116,   124,    18,    19,    20,   422,   123,   124,    24,
      25,    26,   120,   123,   122,   121,   359,   123,   122,   123,
     363,    67,    68,    69,    70,    71,    72,    73,    74,   121,
      45,   123,   121,   376,   123,   122,   121,   434,   123,     5,
     121,   384,   123,   386,   441,   121,   121,   123,   123,   392,
     121,   121,   123,   123,   121,   121,   123,   123,     5,   121,
     471,   123,   496,   121,   121,   123,   123,    82,     5,   121,
     754,   123,    57,   122,    59,   418,   605,   606,    28,   422,
      30,    31,    32,    33,    34,    57,   429,    59,    57,   121,
      59,   123,   121,   538,   123,   540,   541,   542,   543,   122,
     123,   122,   123,   122,   123,   122,   123,   791,   122,   123,
     544,   120,   546,   120,   548,   120,   547,   551,   122,   123,
     555,   122,   123,   120,   120,   120,   120,   120,     5,   127,
     546,   120,   548,    83,   125,   551,   124,   124,   122,   120,
       5,   538,   124,   540,   122,   124,     5,   120,   123,     5,
     124,   122,   122,   496,   104,   122,   106,   107,   108,   109,
     110,   111,   124,   113,   114,   115,   116,   124,   602,   603,
     122,   122,     5,     5,   608,     5,   610,   122,   122,     5,
     122,   122,     5,   628,   122,   120,   602,   603,   633,   122,
     124,   122,   608,   122,   610,    11,   122,    59,   122,   124,
     122,   544,   120,   546,   638,   548,   122,   641,   551,   122,
     125,   120,   647,   648,   125,   122,   121,    57,   122,   122,
     122,   122,   638,   122,   122,   641,   122,   122,    59,   122,
     122,   122,   629,   630,   631,    39,   633,   634,    52,   100,
     122,   122,   122,     5,   122,    57,   122,    39,   693,   735,
     122,    52,    52,    52,    57,   689,   122,     5,   122,   602,
     603,    57,   707,   708,   122,   608,    59,   610,   122,   755,
      57,   122,    57,   689,   122,   709,   710,    59,    57,     4,
     207,   134,   438,   411,   483,   405,   196,   425,   581,   587,
     724,   725,   149,   709,   710,   638,   730,   694,   641,   696,
     118,   735,   736,   616,   749,   463,   161,   363,   724,   725,
     707,    -1,   746,    -1,   730,    -1,    -1,    -1,   752,   754,
     736,   755,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     746,    -1,    -1,    -1,    -1,    -1,   752,    -1,    -1,    -1,
     774,    -1,    -1,    -1,    -1,    -1,   689,    -1,    -1,    -1,
     784,    -1,   749,   750,    -1,    -1,   791,    -1,   774,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   709,   710,   784,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   724,   725,    -1,    -1,    -1,    -1,   730,    -1,    -1,
      -1,    -1,   735,   736,    -1,    10,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   746,    -1,    -1,    -1,    -1,    -1,   752,
      -1,    -1,   755,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   774,    -1,    -1,    49,    -1,    -1,    52,    -1,    -1,
      -1,   784,    -1,    -1,    -1,    28,    29,    30,    31,    32,
      33,    34,    67,    68,    69,    70,    71,    72,    73,    74,
      75,    76,    77,    78,    79,    80,    81,    82,    83,    84,
      85,    86,    87,    88,    89,    90,    91,    92,    -1,    -1,
      -1,     4,     5,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    18,    19,    20,    -1,    -1,
      83,    24,    25,    26,    -1,    -1,    -1,    90,    91,    92,
      -1,    -1,    -1,    -1,    -1,    -1,    99,    -1,   101,   102,
     103,   104,    45,   106,   107,   108,   109,   110,   111,    -1,
     113,   114,   115,   116,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,     4,     5,    66,    -1,   128,   161,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    18,    19,    20,    -1,    82,
      -1,    24,    25,    26,    -1,    -1,    -1,    90,    91,    92,
      -1,    -1,    -1,    -1,    -1,   190,    -1,   192,   101,   102,
     103,    -1,    45,    -1,    -1,    -1,    -1,    -1,   111,    -1,
      -1,    -1,    30,    31,    32,    33,    34,   120,   121,    -1,
      -1,    -1,   125,    66,    -1,    -1,   129,    -1,   131,   132,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    82,
     235,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,
     245,   246,    -1,    -1,   249,    -1,    -1,    -1,   101,   102,
     103,    -1,    -1,    -1,    -1,    83,    -1,    -1,   111,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   120,   121,    -1,
      -1,    -1,   125,    -1,    -1,    -1,   129,    -1,   131,   132,
     108,   109,   110,   111,    -1,   113,   114,   115,   116,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   311,   312,    -1,    -1,
     315,   316,   317,    -1,    -1,    -1,   321,    -1,   323,    -1,
      -1,   326,    -1,    -1,    -1,    -1,    -1,     4,     5,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    18,    19,    20,    -1,    -1,    -1,    24,    25,    26,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   364,
      -1,    -1,    -1,    40,    41,    -1,    -1,    -1,    45,    -1,
      -1,    -1,   377,    -1,    -1,   380,   381,   382,    -1,    -1,
     385,    -1,    -1,    -1,    -1,   390,    -1,    -1,    -1,    66,
      -1,   396,    -1,    -1,   399,   400,    -1,    -1,    -1,    -1,
      -1,   406,   407,    -1,    -1,    82,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    91,    92,    -1,    -1,   423,    -1,
      -1,    -1,    -1,   428,   101,   102,   103,    -1,    -1,    -1,
     435,    -1,    -1,    -1,   111,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   120,     4,     5,   451,    -1,    -1,    -1,
      -1,    -1,   129,    -1,   131,   132,    -1,    -1,    18,    19,
      20,    -1,    -1,    -1,    24,    25,    26,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     485,   486,    -1,    -1,    -1,    45,    -1,   492,    -1,    -1,
      -1,    -1,    52,    53,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   509,    -1,    66,    -1,    -1,    -1,
     515,   516,    -1,    -1,    -1,   520,    -1,   522,    -1,    -1,
      -1,    -1,    82,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      90,    91,    92,    -1,     4,     5,    -1,    -1,    -1,    -1,
      -1,   101,   102,   103,    -1,    -1,    -1,    -1,    18,    19,
      20,   111,    -1,    -1,    24,    25,    26,    -1,    -1,    -1,
     120,   566,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   129,
      -1,   131,   132,    -1,    -1,    45,    -1,    -1,     4,     5,
      -1,    -1,    52,    53,    -1,    -1,    -1,    -1,    -1,    -1,
     595,    -1,    18,    19,    20,    -1,    66,    -1,    24,    25,
      26,    -1,   607,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   616,    82,    -1,    -1,    -1,    -1,    -1,    -1,    45,
      90,    91,    92,    -1,    -1,    -1,    52,    53,    -1,    -1,
      -1,   101,   102,   103,    -1,    -1,    -1,    -1,    -1,    -1,
      66,   111,    -1,    -1,   649,    -1,    -1,    -1,    -1,   654,
     120,    -1,    -1,    -1,    -1,   660,    82,    -1,    -1,   129,
      -1,   131,   132,    -1,    90,    91,    92,     4,     5,    -1,
      -1,    -1,    -1,    -1,    -1,   101,   102,   103,    -1,    -1,
      -1,    18,    19,    20,    -1,   111,    -1,    24,    25,    26,
      -1,    -1,    -1,    -1,   120,    -1,    -1,    -1,    -1,     4,
       5,    -1,    -1,   129,    -1,   131,   132,    -1,    45,    -1,
      -1,    -1,    -1,    18,    19,    20,    -1,    -1,    -1,    24,
      25,    26,     4,     5,    -1,    -1,    -1,    -1,    -1,    66,
      -1,    -1,    -1,    -1,    -1,    -1,    18,    19,    20,    -1,
      45,    -1,    24,    25,    26,    82,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    66,    -1,    45,   101,   102,   103,    -1,    -1,    -1,
     107,    -1,    -1,    -1,   111,    -1,    -1,    82,    -1,    -1,
      -1,    -1,    -1,   120,    66,    90,    91,    92,    -1,    -1,
      -1,    -1,   129,    -1,   131,   132,   101,   102,   103,    -1,
      82,    -1,    -1,    -1,    -1,    -1,   111,    -1,    90,    91,
      92,    -1,    -1,    -1,    -1,   120,   121,    -1,    -1,   101,
     102,   103,    -1,    -1,   129,    -1,   131,   132,    -1,   111,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   119,   120,     4,
       5,    -1,    -1,    -1,    -1,    -1,    -1,   129,    -1,   131,
     132,    -1,    -1,    18,    19,    20,    -1,    -1,    -1,    24,
      25,    26,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,     4,     5,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      45,    -1,    -1,    -1,    -1,    18,    19,    20,    -1,    -1,
      -1,    24,    25,    26,     4,     5,    -1,    -1,    -1,    -1,
      -1,    66,    -1,    -1,    -1,    -1,    -1,    -1,    18,    19,
      20,    -1,    45,    -1,    24,    25,    26,    82,    -1,    -1,
      53,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,
      -1,    -1,    -1,    66,    -1,    45,   101,   102,   103,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   111,    -1,    -1,    82,
      -1,    -1,    -1,    -1,    -1,   120,    66,    90,    91,    92,
     125,    -1,    -1,    -1,   129,    -1,   131,   132,   101,   102,
     103,    -1,    82,    -1,    -1,    -1,    -1,    -1,   111,    -1,
      90,    91,    92,    -1,    -1,    -1,    -1,   120,    -1,    -1,
      -1,   101,   102,   103,    -1,    -1,   129,    -1,   131,   132,
      -1,   111,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     120,   121,     4,     5,    -1,    -1,    -1,    -1,    -1,   129,
      -1,   131,   132,    -1,    -1,    -1,    18,    19,    20,    -1,
      -1,    -1,    24,    25,    26,    -1,    -1,    -1,    -1,    -1,
       5,    -1,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    45,    -1,    -1,    21,    22,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      35,    36,    -1,    38,    66,    -1,    -1,    42,    -1,    -1,
      -1,    46,    47,    48,    -1,    -1,    -1,    -1,    -1,    54,
      82,    -1,    -1,    -1,    -1,    60,    -1,    -1,    90,    91,
      92,    30,    31,    32,    33,    34,    -1,    -1,    -1,   101,
     102,   103,    -1,    78,    -1,    -1,    -1,    -1,     5,   111,
       7,    -1,    87,    -1,    11,    -1,    -1,    -1,   120,    94,
      95,    -1,    -1,    98,    21,   100,    -1,   129,    -1,   131,
     132,    28,    29,    30,    31,    32,    33,    34,    -1,    36,
      -1,    38,    -1,    -1,    83,    -1,    43,    44,    -1,    -1,
      -1,    -1,    49,    50,    51,    -1,    -1,    -1,    55,    -1,
      -1,    -1,    -1,    60,    61,   104,    -1,   106,   107,   108,
     109,   110,   111,    -1,   113,   114,   115,   116,    75,    -1,
      77,    78,    -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,
      -1,    88,    89,    90,    91,    92,    93,    -1,    -1,    -1,
      97,    -1,    99,    -1,   101,   102,   103,   104,    -1,   106,
     107,   108,   109,   110,   111,    -1,   113,   114,   115,   116,
      -1,    -1,   119,    -1,     5,   122,     7,     8,     9,   126,
      11,    -1,   129,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      21,    22,    23,    -1,    -1,     5,    -1,     7,    -1,    -1,
      -1,    11,    -1,    -1,    -1,    36,    -1,    38,    -1,    -1,
      -1,    21,    43,    44,    -1,    -1,    -1,    -1,    49,    50,
      51,    -1,    -1,    -1,    55,    -1,    36,    37,    38,    60,
      61,    -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,
      50,    51,    -1,    -1,    75,    55,    77,    78,    -1,    -1,
      60,    61,    -1,    -1,    -1,    -1,    -1,    88,    89,    -1,
      -1,    -1,    93,    -1,    -1,    75,    97,    77,    78,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    88,    89,
      -1,    -1,    -1,    93,    -1,    -1,    -1,    97,   119,    -1,
     100,     5,    -1,     7,    -1,   126,    -1,    11,   129,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    21,    -1,   119,
      -1,    -1,     5,    -1,     7,    -1,   126,    -1,    11,   129,
      -1,    -1,    36,    -1,    38,    -1,    -1,    -1,    21,    43,
      44,    -1,    -1,    -1,    -1,    49,    50,    51,    -1,    -1,
      -1,    55,    -1,    36,    37,    38,    60,    61,    -1,    -1,
      43,    44,    -1,    -1,    -1,    -1,    49,    50,    51,    -1,
      -1,    75,    55,    77,    78,    -1,    -1,    60,    61,    -1,
      -1,    -1,    -1,    -1,    88,    89,    -1,    -1,    -1,    93,
      -1,    -1,    75,    97,    77,    78,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    88,    89,    -1,    -1,    -1,
      93,     5,    -1,     7,    97,   119,    -1,    11,   122,    -1,
      -1,    -1,   126,    -1,    -1,   129,    -1,    21,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   119,    -1,    -1,    -1,
      -1,    -1,    36,   126,    38,    -1,   129,    -1,    -1,    43,
      44,    -1,    -1,    -1,    -1,    49,    50,    51,    -1,    -1,
      -1,    55,    -1,    -1,    -1,    -1,    60,    61,    -1,    -1,
      -1,     5,    -1,     7,    -1,    -1,    -1,    11,    -1,    -1,
      -1,    75,    76,    77,    78,    -1,    -1,    21,    -1,    -1,
      -1,    -1,    -1,    -1,    88,    89,    -1,    -1,    -1,    93,
      -1,    -1,    36,    97,    38,    -1,    -1,    -1,    -1,    43,
      44,    -1,    -1,    -1,    -1,    49,    50,    51,    -1,    -1,
      -1,    55,    -1,    57,    -1,   119,    60,    61,    -1,    -1,
      -1,    -1,   126,    -1,     5,   129,     7,    -1,    -1,    -1,
      11,    75,    -1,    77,    78,    -1,    -1,    -1,    -1,    -1,
      21,    -1,    -1,    -1,    88,    89,    -1,    -1,    -1,    93,
      -1,    -1,    -1,    97,    -1,    36,    37,    38,    -1,    -1,
      -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,    50,
      51,    -1,    -1,    -1,    55,   119,    -1,    -1,    -1,    60,
      61,    -1,   126,    -1,     5,   129,     7,    -1,    -1,    -1,
      11,    -1,    -1,    -1,    75,    -1,    77,    78,    -1,    -1,
      21,    -1,    -1,    -1,    -1,    -1,    -1,    88,    89,    -1,
      -1,    -1,    93,    -1,    -1,    36,    97,    38,    -1,    -1,
      -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,    50,
      51,    -1,    -1,    -1,    55,    -1,    57,    -1,   119,    60,
      61,    -1,    -1,    -1,     5,   126,     7,    -1,   129,    -1,
      11,    -1,    -1,    -1,    75,    -1,    77,    78,    -1,    -1,
      21,    -1,    -1,    -1,    -1,    -1,    -1,    88,    89,    -1,
      -1,    -1,    93,    -1,    -1,    36,    97,    38,    -1,    -1,
      -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,    50,
      51,    -1,    -1,    -1,    55,    -1,    -1,    -1,   119,    60,
      61,    -1,    -1,    -1,     5,   126,     7,    -1,   129,    -1,
      11,    -1,    -1,    -1,    75,    -1,    77,    78,    -1,    -1,
      21,    -1,    -1,    -1,    -1,    -1,    -1,    88,    89,    -1,
      -1,    -1,    93,    -1,    -1,    36,    97,    38,    -1,    -1,
      -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,    50,
      51,    -1,    -1,    -1,    55,    -1,    -1,    -1,   119,    60,
      61,   122,    -1,    -1,     5,   126,     7,    -1,   129,    -1,
      11,    -1,    -1,    -1,    75,    -1,    77,    78,    -1,    -1,
      21,    -1,    -1,    -1,    -1,    -1,    -1,    88,    89,    -1,
      -1,    -1,    93,    -1,    -1,    36,    97,    38,    -1,    -1,
      -1,    -1,    43,    44,    -1,    -1,    -1,    -1,    49,    50,
      51,    -1,    -1,    -1,    55,    -1,    -1,    -1,   119,    60,
      61,   122,    -1,    -1,    -1,   126,    -1,    -1,   129,    -1,
      -1,    -1,    -1,    -1,    75,    -1,    77,    78,    28,    29,
      30,    31,    32,    33,    34,    -1,    -1,    88,    89,    -1,
      -1,    -1,    93,    -1,    -1,    -1,    97,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,    -1,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,   119,    -1,
      -1,    -1,    -1,    -1,    -1,   126,    -1,    -1,   129,    -1,
      -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,
      90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    99,
      -1,   101,   102,   103,   104,    -1,   106,   107,   108,   109,
     110,   111,    83,   113,   114,   115,   116,    28,    29,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,   129,
      -1,    -1,   103,   104,    -1,   106,   107,   108,   109,   110,
     111,    -1,   113,   114,   115,   116,    -1,    -1,    -1,    -1,
      -1,    28,    29,    30,    31,    32,    33,    34,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    80,
      81,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    99,   100,
     101,   102,   103,   104,    -1,   106,   107,   108,   109,   110,
     111,    -1,   113,   114,   115,   116,    83,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    91,    92,    -1,   128,    -1,    -1,
      -1,    -1,    99,    -1,   101,   102,   103,   104,    -1,   106,
     107,   108,   109,   110,   111,    -1,   113,   114,   115,   116,
      28,    29,    30,    31,    32,    33,    34,    -1,    -1,    -1,
      -1,   128,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    28,    29,    30,    31,    32,    33,
      34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,
      -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,
      -1,    99,    -1,   101,   102,   103,   104,    -1,   106,   107,
     108,   109,   110,   111,    -1,   113,   114,   115,   116,    83,
      -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,
     128,    -1,    -1,    -1,    -1,    99,    -1,   101,   102,   103,
     104,    -1,   106,   107,   108,   109,   110,   111,    -1,   113,
     114,   115,   116,    28,    29,    30,    31,    32,    33,    34,
     124,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
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
      -1,   113,   114,   115,   116,    -1,    -1,    -1,    -1,     5,
     122,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      16,    17,    -1,    -1,    -1,    21,    22,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    35,
      -1,    -1,    -1,    -1,    -1,    -1,    42,    -1,    -1,    -1,
      46,    47,    48,    -1,    -1,    -1,    -1,    -1,    54,    -1,
      56,    -1,    58,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      66,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    78,    -1,    -1,    -1,    -1,    -1,    -1,    85,
      -1,    87,    -1,    -1,    -1,    -1,    -1,    -1,    94,    95,
      96,     5,    98,     7,     8,     9,    10,    11,    12,    13,
      14,    15,    16,    17,    -1,    -1,    -1,    21,    22,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    35,    36,    -1,    38,    -1,    -1,    -1,    42,    -1,
      -1,    -1,    46,    47,    48,    -1,    -1,    -1,    -1,    -1,
      54,    -1,    -1,    -1,    -1,     5,    60,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    16,    17,    -1,    -1,
      -1,    21,    22,    -1,    78,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    86,    87,    -1,    35,    36,    37,    38,    -1,
      94,    95,    42,    -1,    98,    -1,    46,    47,    48,    -1,
      -1,    -1,    -1,    -1,    54,    -1,    -1,    -1,    -1,     5,
      60,     7,     8,     9,    10,    11,    12,    13,    14,    15,
      16,    17,    -1,    -1,    -1,    21,    22,    -1,    78,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    87,    -1,    35,
      36,    37,    38,    -1,    94,    95,    42,    -1,    98,    -1,
      46,    47,    48,    -1,    -1,    -1,    -1,    -1,    54,    -1,
      -1,    -1,    -1,     5,    60,     7,     8,     9,    10,    11,
      12,    13,    14,    15,    16,    17,    -1,    -1,    -1,    21,
      22,    -1,    78,    -1,    28,    29,    30,    31,    32,    33,
      34,    87,    -1,    35,    36,    -1,    38,    -1,    94,    95,
      42,    -1,    98,    -1,    46,    47,    48,    -1,    -1,    -1,
      -1,    -1,    54,    -1,    -1,    -1,    -1,    -1,    60,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    78,    -1,    -1,    83,
      -1,    -1,    -1,    -1,    -1,    87,    90,    91,    92,    -1,
      -1,    -1,    94,    95,    -1,    99,    98,   101,   102,   103,
     104,    -1,   106,   107,   108,   109,   110,   111,    -1,   113,
     114,   115,   116,    -1,    83,    -1,    -1,   121,    -1,    -1,
      -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,
      99,    -1,   101,   102,   103,   104,    -1,   106,   107,   108,
     109,   110,   111,    -1,   113,   114,   115,   116,    -1,    -1,
      -1,    -1,   121,    28,    29,    30,    31,    32,    33,    34,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,    29,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,
      -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,
      -1,    -1,    -1,    -1,    99,    -1,   101,   102,   103,   104,
      -1,   106,   107,   108,   109,   110,   111,    -1,   113,   114,
     115,   116,    83,    -1,    -1,    -1,   121,    -1,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    99,    -1,
     101,   102,   103,   104,    -1,   106,   107,   108,   109,   110,
     111,    -1,   113,   114,   115,   116,    -1,    -1,    -1,    -1,
     121,    28,    29,    30,    31,    32,    33,    34,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    28,    29,    30,    31,    32,
      33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    -1,    99,    -1,   101,   102,   103,   104,    -1,   106,
     107,   108,   109,   110,   111,    -1,   113,   114,   115,   116,
      83,    -1,    -1,    -1,   121,    -1,    -1,    90,    91,    92,
      -1,    -1,    -1,    -1,    -1,    -1,    99,    -1,   101,   102,
     103,   104,    -1,   106,   107,   108,   109,   110,   111,    -1,
     113,   114,   115,   116,    -1,    -1,    -1,    -1,   121,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    28,    29,    30,    31,    32,    33,    34,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,
      -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,
      99,    -1,   101,   102,   103,   104,    -1,   106,   107,   108,
     109,   110,   111,    -1,   113,   114,   115,   116,    83,    -1,
      -1,    -1,   121,    -1,    -1,    90,    91,    92,    -1,    -1,
      -1,    -1,    -1,    -1,    99,    -1,   101,   102,   103,   104,
      -1,   106,   107,   108,   109,   110,   111,    -1,   113,   114,
     115,   116,    -1,    -1,    -1,    -1,   121,    28,    29,    30,
      31,    32,    33,    34,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    28,    29,    30,    31,    32,    33,    34,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    90,
      91,    92,    -1,    -1,    -1,    -1,    -1,    -1,    99,    -1,
     101,   102,   103,   104,    -1,   106,   107,   108,   109,   110,
     111,    -1,   113,   114,   115,   116,    83,    -1,    -1,    -1,
     121,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    -1,    99,    -1,   101,   102,   103,   104,    -1,   106,
     107,   108,   109,   110,   111,    -1,   113,   114,   115,   116,
      -1,    -1,    -1,    -1,   121,    28,    29,    30,    31,    32,
      33,    34,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,
      29,    30,    31,    32,    33,    34,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,
      -1,    -1,    -1,    -1,    -1,    -1,    99,    -1,   101,   102,
     103,   104,    -1,   106,   107,   108,   109,   110,   111,    -1,
     113,   114,   115,   116,    83,    -1,    -1,    -1,   121,    -1,
      -1,    90,    91,    92,    -1,    -1,    -1,    -1,    -1,    -1,
      99,    -1,   101,   102,   103,   104,    -1,   106,   107,   108,
     109,   110,   111,    -1,   113,   114,   115,   116,    -1,    -1,
      -1,    -1,   121,    28,    29,    30,    31,    32,    33,    34,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    28,    29,    30,    31,    32,    33,    34,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    80,    81,    -1,    83,    -1,
      -1,    -1,    -1,    -1,    -1,    90,    91,    92,    -1,    -1,
      -1,    -1,    -1,    -1,    99,   100,   101,   102,   103,   104,
      -1,   106,   107,   108,   109,   110,   111,    83,   113,   114,
     115,   116,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,
      -1,    -1,    -1,    99,   100,   101,   102,   103,   104,    -1,
     106,   107,   108,   109,   110,   111,    -1,   113,   114,   115,
     116,    28,    29,    30,    31,    32,    33,    34,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      28,    29,    30,    31,    32,    33,    34,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    83,    -1,    -1,    -1,
      -1,    -1,    -1,    90,    91,    92,    -1,    -1,    -1,    -1,
      -1,    -1,    99,    -1,   101,   102,   103,   104,    -1,   106,
     107,   108,   109,   110,   111,    83,   113,   114,   115,   116,
      -1,    -1,    90,    91,    92,    28,    -1,    30,    31,    32,
      33,    34,    -1,    -1,   102,   103,   104,    -1,   106,   107,
     108,   109,   110,   111,    -1,   113,   114,   115,   116,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      83,    -1,    -1,    -1,    -1,    -1,    -1,    90,    91,    92,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   102,
     103,   104,    -1,   106,   107,   108,   109,   110,   111,    -1,
     113,   114,   115,   116
};

/* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
   symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,     3,    66,   134,   135,   136,   137,   144,     5,     4,
       5,    45,     0,   136,   119,   138,     5,     4,     5,    18,
      19,    20,    24,    25,    26,    45,    66,    82,    90,    91,
      92,   101,   102,   103,   111,   120,   129,   131,   132,   202,
     205,   207,   120,   120,   122,   139,   115,   120,   125,   127,
     198,   199,   120,   207,   207,   207,   207,   207,   207,   207,
     207,   107,   203,   204,   207,   207,   207,    28,    29,    30,
      31,    32,    33,    34,    83,    90,    91,    92,    99,   101,
     102,   103,   104,   106,   107,   108,   109,   110,   111,   113,
     114,   115,   116,     5,    47,    48,   121,   164,   165,     5,
       8,     9,    10,   121,   140,   141,   200,     5,     7,    11,
      12,    13,    14,    15,    16,    17,    21,    22,    35,    42,
      46,    47,    48,    54,    56,    58,    78,    85,    87,    94,
      95,    96,    98,   142,   143,   144,   145,   148,   149,   153,
     154,   157,   158,   159,   166,   173,   174,   185,   200,   201,
       4,   194,   207,     5,   205,   207,   198,   199,   207,   121,
     202,   123,   130,   202,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     124,     5,   127,   198,     5,   121,   123,    12,    13,    16,
      11,    12,    13,    16,    12,   122,   121,   123,     5,    21,
     198,     5,   119,   120,   172,     5,   119,   120,   150,   169,
     189,   190,   196,   202,   205,    16,    16,     5,   197,     5,
       7,    11,    21,    36,    38,    43,    44,    49,    50,    51,
      55,    60,    61,    75,    77,    88,    89,    93,    97,   119,
     126,   178,   182,   185,   186,   187,   188,   196,   205,     5,
     120,     5,   160,   161,   205,     5,    16,   162,   163,   198,
     162,   198,   178,   182,     5,    21,   152,   198,     5,     5,
      45,   183,   184,    36,    38,    60,    87,   145,   148,   149,
     157,   158,   159,   166,   173,   175,   176,   177,   185,   182,
       6,   142,   197,   198,     5,   146,   147,   172,   198,     5,
     121,   123,   120,   198,   199,    80,    81,   100,   128,   121,
     204,   100,   207,   124,   207,     5,   124,   165,    16,   122,
     141,   124,     5,     5,   198,   120,   122,   198,     4,     5,
      82,   120,   194,     5,   198,   199,     4,     5,    82,   120,
      67,    68,    69,    70,    71,    72,    73,    74,   151,   169,
     196,   196,   122,   123,   124,   123,   122,   120,   122,   196,
     197,   198,   197,    37,   100,   182,   195,   120,   207,     5,
     120,   120,   120,   182,   120,   120,   195,     5,   207,   207,
     120,     5,   207,     5,    84,   114,   120,   122,   182,    34,
     124,   122,   120,   194,   122,   123,   124,   124,   162,   198,
     122,   123,   162,   198,   122,   162,   198,   120,   122,     5,
     198,   120,   122,   124,    79,   123,   100,   175,   120,   120,
     197,    86,   176,   122,   197,   124,   198,   122,   123,     5,
     197,     5,   147,   198,   207,   207,   207,   207,   207,   207,
     207,   124,   207,     4,    18,    19,    20,    24,    25,    26,
      45,    82,   206,   124,   198,     5,   121,   125,   167,   168,
     194,   120,   121,   125,   170,   171,   194,   121,   120,   198,
     198,   199,   194,   123,   196,   124,   124,   190,   207,   197,
     121,   194,   124,   122,   197,   122,     5,    37,   182,   207,
     122,   122,   207,   207,   207,   189,   207,    76,   122,   124,
     122,   207,   122,   122,   182,    40,    41,   180,   181,   207,
     169,   207,   169,   207,   167,   194,   121,   160,   207,   207,
     122,   162,   163,   122,   162,   122,   162,   140,     8,     9,
      11,    21,    22,    23,   155,   156,   195,   120,   122,     5,
     140,   155,   182,   207,   184,     5,    37,   207,   189,   122,
     122,   198,   207,   122,     5,   146,   124,   122,   198,   122,
     147,   121,   128,   128,   128,   207,   206,   122,     5,   114,
     121,   123,   121,   167,   194,     5,   121,   123,   121,   122,
     121,   167,   120,   121,   151,   124,   207,   207,   122,   121,
     207,   122,   195,   121,   121,   121,   121,   122,   121,   207,
     121,   207,   207,    42,   121,   123,   179,   207,   122,   207,
     122,   121,   121,   122,   122,   122,   122,   121,    21,   197,
     198,    11,   197,   198,   197,   197,   197,   156,   195,    57,
     140,   155,   182,   122,   121,   182,    59,   175,   121,   122,
     122,   207,   122,   122,   120,   122,   168,   122,   121,   121,
     120,   171,   122,   121,   167,   121,   207,   122,   122,   122,
     122,    37,   182,    53,   191,   192,   193,   194,   191,   191,
     207,   182,   122,   182,   181,   122,   122,   122,   122,   122,
     197,   122,   198,   198,   198,   122,     5,   197,   198,   122,
     198,   122,   122,    57,   121,   182,    57,    11,    21,   155,
     122,    59,    37,   176,   207,   122,   121,   207,   122,   122,
     207,   122,   121,   122,    39,   100,    52,   192,   193,    52,
     100,    52,   193,    52,   193,   122,   155,   182,   122,   122,
     197,   198,   198,   122,     5,   122,   122,    57,   197,   198,
     197,   182,   155,   182,    39,   122,   121,   121,   122,   182,
     122,   182,    52,   122,   182,    52,    52,   189,   182,    57,
     122,     5,   122,   122,   155,   182,   122,   197,   122,    57,
     182,    59,   176,   189,   121,    57,   122,   182,    57,   122,
      59,   121,   182,    57,   176
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
#line 3134 "y.tab.c"
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


#line 387 "yaccs/verilog.yacc"


