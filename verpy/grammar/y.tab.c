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
     arith_shift_right = 350,
     SignedLeft = 351,
     shift_right = 352,
     shift_left = 353,
     Veryequal = 354,
     noteqeq = 355,
     StarStar = 356,
     UNARY_PREC = 357
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
#define arith_shift_right 350
#define SignedLeft 351
#define shift_right 352
#define shift_left 353
#define Veryequal 354
#define noteqeq 355
#define StarStar 356
#define UNARY_PREC 357




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
#line 311 "y.tab.c"

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
#define YYLAST   4821

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  129
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  67
/* YYNRULES -- Number of rules.  */
#define YYNRULES  318
/* YYNRULES -- Number of states.  */
#define YYNSTATES  701

/* YYTRANSLATE(YYLEX) -- Bison symbol number corresponding to YYLEX.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   357

#define YYTRANSLATE(YYX)						\
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[YYLEX] -- Bison symbol number corresponding to YYLEX.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   127,     2,   115,     2,   112,    99,     2,
     116,   117,   110,   106,   119,   107,   121,   111,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,    96,   118,
     104,   120,   105,    95,   122,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,   123,     2,   124,    98,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   125,    97,   126,   128,     2,     2,     2,
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
     100,   101,   102,   103,   108,   109,   113,   114
};

#if YYDEBUG
/* YYPRHS[YYN] -- Index of the first RHS symbol of rule number YYN in
   YYRHS.  */
static const yytype_uint16 yyprhs[] =
{
       0,     0,     3,     5,     8,    10,    12,    14,    21,    26,
      30,    31,    33,    38,    42,    46,    48,    51,    55,    59,
      64,    66,    69,    70,    72,    74,    76,    78,    80,    82,
      84,    86,    88,    90,    92,    94,    96,    98,   101,   104,
     108,   115,   118,   122,   126,   130,   136,   141,   147,   152,
     159,   165,   170,   175,   181,   187,   194,   202,   209,   215,
     217,   219,   221,   223,   225,   227,   229,   231,   233,   235,
     242,   248,   256,   263,   272,   282,   292,   303,   310,   316,
     325,   335,   338,   340,   344,   348,   352,   357,   363,   367,
     372,   377,   382,   386,   391,   395,   400,   405,   411,   415,
     420,   426,   430,   432,   436,   440,   442,   447,   451,   457,
     464,   468,   474,   481,   488,   495,   503,   512,   520,   524,
     526,   529,   535,   540,   545,   548,   551,   554,   558,   560,
     566,   569,   574,   577,   580,   585,   589,   592,   596,   600,
     603,   605,   609,   615,   619,   621,   623,   625,   627,   629,
     631,   633,   635,   641,   649,   659,   662,   665,   668,   673,
     675,   677,   681,   683,   686,   689,   691,   695,   698,   701,
     707,   711,   716,   722,   727,   733,   739,   747,   751,   755,
     759,   764,   768,   774,   777,   781,   785,   790,   796,   803,
     811,   818,   825,   833,   840,   848,   852,   856,   859,   861,
     863,   865,   868,   870,   876,   886,   892,   898,   902,   904,
     908,   911,   913,   917,   921,   925,   929,   933,   935,   938,
     940,   942,   945,   949,   953,   956,   958,   960,   964,   966,
     972,   978,   984,   988,   990,   992,   994,   997,  1000,  1003,
    1006,  1009,  1012,  1016,  1018,  1020,  1022,  1024,  1026,  1029,
    1032,  1034,  1036,  1038,  1040,  1042,  1046,  1050,  1052,  1055,
    1057,  1061,  1065,  1070,  1075,  1082,  1084,  1086,  1088,  1090,
    1092,  1094,  1099,  1101,  1103,  1105,  1107,  1109,  1111,  1114,
    1118,  1122,  1125,  1131,  1135,  1139,  1143,  1147,  1151,  1155,
    1159,  1163,  1167,  1171,  1175,  1179,  1183,  1187,  1191,  1195,
    1199,  1203,  1207,  1211,  1215,  1219,  1223,  1227,  1231,  1236,
    1240,  1242,  1245,  1248,  1251,  1254,  1257,  1260,  1263
};

/* YYRHS -- A `-1'-separated list of the rules' RHS.  */
static const yytype_int16 yyrhs[] =
{
     130,     0,    -1,   131,    -1,   131,   132,    -1,   132,    -1,
     133,    -1,   140,    -1,     3,     5,   134,   135,   138,     6,
      -1,   115,   116,   156,   117,    -1,   115,   116,   117,    -1,
      -1,   118,    -1,   116,   136,   117,   118,    -1,   116,   117,
     118,    -1,   136,   119,   137,    -1,   137,    -1,   189,     5,
      -1,   189,   187,     5,    -1,   189,    20,     5,    -1,   189,
     187,     5,   187,    -1,     5,    -1,   139,   138,    -1,    -1,
     142,    -1,   143,    -1,   158,    -1,   165,    -1,   166,    -1,
     151,    -1,   152,    -1,   153,    -1,   141,    -1,   147,    -1,
     148,    -1,   140,    -1,    77,    -1,    94,    -1,    65,    44,
      -1,    65,     5,    -1,    65,     5,   195,    -1,    65,     4,
       5,   111,     4,     5,    -1,    53,   174,    -1,   189,   186,
     118,    -1,    16,   186,   118,    -1,   190,   186,   118,    -1,
     190,   186,   120,   195,   118,    -1,   189,   187,   186,   118,
      -1,   189,   187,   186,   187,   118,    -1,   190,   187,   186,
     118,    -1,   190,   187,   186,   120,   195,   118,    -1,   190,
     187,     5,   187,   118,    -1,   190,     5,   187,   118,    -1,
     190,   164,   186,   118,    -1,     5,    26,     5,     5,   118,
      -1,     7,   185,   120,   195,   118,    -1,     7,   161,   185,
     120,   195,   118,    -1,     7,   144,   161,   185,   120,   195,
     118,    -1,     7,   144,   185,   120,   195,   118,    -1,   116,
     145,   119,   145,   117,    -1,    66,    -1,    67,    -1,    68,
      -1,    69,    -1,    70,    -1,    71,    -1,    72,    -1,    73,
      -1,   187,    -1,    20,    -1,    55,     5,   118,   149,   184,
      56,    -1,    55,     5,   118,   184,    56,    -1,    55,   146,
       5,   118,   149,   174,    56,    -1,    55,   146,     5,   118,
     174,    56,    -1,    55,     5,   116,   136,   117,   118,   174,
      56,    -1,    55,     5,   116,   136,   117,   118,   149,   174,
      56,    -1,    55,   146,     5,   116,   136,   117,   118,   174,
      56,    -1,    55,   146,     5,   116,   136,   117,   118,   149,
     174,    56,    -1,    57,     5,   118,   149,   174,    58,    -1,
      57,     5,   118,   174,    58,    -1,    57,     5,   116,   136,
     117,   118,   174,    58,    -1,    57,     5,   116,   136,   117,
     118,   149,   174,    58,    -1,   149,   150,    -1,   150,    -1,
      11,   186,   118,    -1,    21,   186,   118,    -1,    22,   186,
     118,    -1,    11,   187,   186,   118,    -1,    11,   187,     5,
     187,   118,    -1,     8,   186,   118,    -1,     8,   186,   187,
     118,    -1,     8,   187,   186,   118,    -1,     8,    20,   186,
     118,    -1,    20,   186,   118,    -1,    20,   186,   187,   118,
      -1,    46,   154,   118,    -1,    46,    15,   154,   118,    -1,
      46,   187,   154,   118,    -1,    46,    15,   187,   154,   118,
      -1,    47,   154,   118,    -1,    47,   187,   154,   118,    -1,
      45,   194,   120,   195,   118,    -1,   154,   119,   155,    -1,
     155,    -1,     5,   120,   195,    -1,   156,   119,   157,    -1,
     157,    -1,    46,     5,   120,   195,    -1,     5,   120,   195,
      -1,     5,     5,   116,   117,   118,    -1,     5,   164,     5,
     116,   117,   118,    -1,     5,     5,   118,    -1,    41,   116,
     183,   117,   118,    -1,    41,     5,   116,   159,   117,   118,
      -1,     5,     5,   116,   159,   117,   118,    -1,     5,     5,
     116,   183,   117,   118,    -1,     5,   164,     5,   116,   159,
     117,   118,    -1,     5,   164,     5,   187,   116,   159,   117,
     118,    -1,     5,     5,   187,   116,   159,   117,   118,    -1,
     159,   119,   160,    -1,   160,    -1,   121,   110,    -1,   121,
       5,   116,   195,   117,    -1,   121,     5,   116,   117,    -1,
     115,   116,   183,   117,    -1,   115,     4,    -1,   115,     5,
      -1,   115,    80,    -1,   162,   119,   163,    -1,   163,    -1,
     121,     5,   116,   195,   117,    -1,   121,     5,    -1,   115,
     116,   183,   117,    -1,   115,     4,    -1,   115,     5,    -1,
     115,   116,   162,   117,    -1,   115,   116,   117,    -1,    34,
     174,    -1,    34,   170,   174,    -1,    83,   167,    84,    -1,
     167,   168,    -1,   168,    -1,    35,   167,    36,    -1,    35,
      96,     5,   167,    36,    -1,    85,     5,   118,    -1,   142,
      -1,   143,    -1,   151,    -1,   153,    -1,   158,    -1,   169,
      -1,   165,    -1,   141,    -1,    37,   116,   195,   117,   168,
      -1,    37,   116,   195,   117,   168,    38,   168,    -1,    59,
     116,   178,   118,   195,   118,   178,   117,   168,    -1,   122,
     110,    -1,   122,    82,    -1,   122,     5,    -1,   122,   116,
     172,   117,    -1,    41,    -1,   119,    -1,   172,   171,   173,
      -1,   173,    -1,    39,   195,    -1,    40,   195,    -1,   195,
      -1,    35,   184,    36,    -1,    35,    36,    -1,    54,   174,
      -1,    35,    96,     5,   184,    36,    -1,    74,   184,    75,
      -1,   185,   120,   195,   118,    -1,   185,   120,   161,   195,
     118,    -1,   185,    33,   195,   118,    -1,   185,    33,   161,
     195,   118,    -1,    37,   116,   195,   117,   174,    -1,    37,
     116,   195,   117,   174,    38,   174,    -1,    42,   195,   118,
      -1,    20,   186,   118,    -1,    11,   186,   118,    -1,    11,
     187,   186,   118,    -1,    87,   195,   118,    -1,    86,   195,
     120,   195,   118,    -1,   170,   118,    -1,    43,     5,   118,
      -1,    76,     5,   118,    -1,     5,   116,   117,   118,    -1,
       5,   116,   183,   117,   118,    -1,    48,   116,   195,   117,
     180,    51,    -1,    48,   116,   195,   117,   180,   182,    51,
      -1,    48,   116,   195,   117,   182,    51,    -1,    49,   116,
     195,   117,   180,    51,    -1,    49,   116,   195,   117,   180,
     182,    51,    -1,    50,   116,   195,   117,   180,    51,    -1,
      50,   116,   195,   117,   180,   182,    51,    -1,   115,   195,
     118,    -1,   115,   195,   174,    -1,     5,   118,    -1,   175,
      -1,   176,    -1,   177,    -1,   194,   118,    -1,    77,    -1,
       7,   185,   120,   195,   118,    -1,    59,   116,   178,   118,
     195,   118,   178,   117,   174,    -1,    91,   116,   195,   117,
     174,    -1,    60,   116,   195,   117,   174,    -1,   178,   119,
     179,    -1,   179,    -1,   185,   120,   195,    -1,   180,   181,
      -1,   181,    -1,   183,    96,   174,    -1,   183,    96,   118,
      -1,    52,    96,   174,    -1,    52,    96,   118,    -1,   183,
     119,   195,    -1,   195,    -1,   184,   174,    -1,   174,    -1,
       5,    -1,     5,   187,    -1,     5,   188,   187,    -1,     5,
     188,   188,    -1,     5,   188,    -1,   194,    -1,   191,    -1,
       5,   119,   186,    -1,     5,    -1,   123,   195,    96,   195,
     124,    -1,   123,   195,    78,   195,   124,    -1,   123,   195,
      79,   195,   124,    -1,   123,   195,   124,    -1,     8,    -1,
       9,    -1,    10,    -1,     9,    11,    -1,     8,    12,    -1,
       9,    12,    -1,    10,    12,    -1,     8,    15,    -1,     9,
      15,    -1,     9,    11,    15,    -1,    11,    -1,    12,    -1,
      15,    -1,    20,    -1,    21,    -1,    11,    15,    -1,    12,
      15,    -1,    85,    -1,    92,    -1,    93,    -1,    13,    -1,
      14,    -1,   125,   192,   126,    -1,   192,   119,   193,    -1,
     193,    -1,   195,   191,    -1,   195,    -1,     5,   121,   194,
      -1,     5,   121,     5,    -1,     5,   121,     5,   187,    -1,
       5,   121,     5,   188,    -1,     5,   121,     5,   116,   195,
     117,    -1,     5,    -1,   194,    -1,     4,    -1,    80,    -1,
      44,    -1,    65,    -1,    65,   116,   195,   117,    -1,    17,
      -1,    18,    -1,    19,    -1,    23,    -1,    24,    -1,    25,
      -1,     5,   187,    -1,     5,   188,   187,    -1,     5,   188,
     188,    -1,     5,   188,    -1,   195,    95,   195,    96,   195,
      -1,   195,   106,   195,    -1,   195,   110,   195,    -1,   195,
     107,   195,    -1,   195,   111,   195,    -1,   195,   112,   195,
      -1,   195,    98,   195,    -1,   195,    97,   195,    -1,   195,
      99,   195,    -1,   195,   104,   195,    -1,   195,   105,   195,
      -1,   195,    81,   195,    -1,   195,    27,   195,    -1,   195,
      28,   195,    -1,   195,    88,   195,    -1,   195,    89,   195,
      -1,   195,    90,   195,    -1,   195,    30,   195,    -1,   195,
      29,   195,    -1,   195,    31,   195,    -1,   195,   109,   195,
      -1,   195,    32,   195,    -1,   195,    33,   195,    -1,   195,
     103,   195,    -1,   195,   102,   195,    -1,   195,   100,   195,
      -1,     5,   116,   183,   117,    -1,   116,   195,   117,    -1,
     191,    -1,   107,   195,    -1,    97,   195,    -1,    99,   195,
      -1,    98,   195,    -1,    88,   195,    -1,    90,   195,    -1,
     127,   195,    -1,   128,   195,    -1
};

/* YYRLINE[YYN] -- source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,    42,    42,    43,    43,    44,    44,    45,    47,    47,
      47,    48,    48,    48,    49,    49,    51,    51,    51,    51,
      51,    54,    54,    57,    58,    59,    60,    61,    62,    63,
      64,    65,    66,    67,    68,    69,    70,    74,    74,    74,
      74,    75,    77,    78,    79,    80,    81,    82,    83,    84,
      85,    86,    87,    88,    92,    93,    94,    95,    98,    99,
      99,    99,    99,    99,    99,    99,    99,   100,   100,   102,
     103,   104,   105,   106,   107,   108,   109,   112,   113,   114,
     115,   118,   118,   120,   121,   122,   123,   124,   125,   126,
     127,   128,   129,   130,   134,   135,   136,   137,   139,   139,
     140,   141,   141,   142,   144,   144,   146,   147,   151,   152,
     153,   154,   155,   156,   157,   158,   159,   160,   168,   168,
     169,   169,   169,   171,   171,   171,   171,   172,   172,   173,
     173,   174,   174,   174,   174,   174,   177,   177,   180,   182,
     182,   185,   186,   187,   188,   189,   190,   191,   192,   193,
     194,   195,   196,   197,   202,   207,   207,   207,   207,   208,
     208,   209,   209,   210,   210,   210,   215,   216,   217,   218,
     219,   220,   221,   222,   223,   224,   225,   226,   227,   228,
     229,   230,   231,   232,   233,   234,   235,   236,   237,   238,
     239,   240,   241,   242,   243,   244,   245,   246,   247,   248,
     249,   250,   251,   252,   255,   256,   257,   258,   258,   259,
     260,   260,   261,   261,   262,   262,   264,   264,   265,   265,
     268,   268,   268,   268,   268,   268,   268,   270,   270,   272,
     272,   272,   273,   275,   275,   275,   275,   275,   275,   275,
     275,   275,   275,   277,   277,   277,   277,   277,   277,   277,
     277,   277,   277,   277,   277,   279,   280,   280,   281,   281,
     284,   285,   286,   287,   288,   291,   292,   293,   294,   295,
     296,   297,   298,   298,   298,   298,   298,   298,   299,   300,
     301,   302,   303,   304,   305,   306,   307,   308,   309,   310,
     311,   312,   313,   314,   315,   316,   317,   318,   319,   320,
     321,   322,   323,   324,   325,   326,   327,   328,   329,   330,
     331,   332,   333,   334,   335,   336,   337,   338,   339
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
  "nand", "nor", "repeat", "supply0", "supply1", "newver", "'?'", "':'",
  "'|'", "'^'", "'&'", "arith_shift_right", "SignedLeft", "shift_right",
  "shift_left", "'<'", "'>'", "'+'", "'-'", "Veryequal", "noteqeq", "'*'",
  "'/'", "'%'", "StarStar", "UNARY_PREC", "'#'", "'('", "')'", "';'",
  "','", "'='", "'.'", "'@'", "'['", "']'", "'{'", "'}'", "'!'", "'~'",
  "$accept", "Main", "Mains", "MainItem", "Module", "Hparams", "Header",
  "Header_list", "Header_item", "Module_stuffs", "Mstuff", "Define",
  "Initial", "Definition", "Assign", "StrengthDef", "Strength", "WidthInt",
  "Function", "Task", "Mem_defs", "Mem_def", "Parameter", "Localparam",
  "Defparam", "Pairs", "Pair", "head_params", "head_param", "Instance",
  "Conns_list", "Connection", "AssignParams", "Prms_list", "PrmAssign",
  "InstParams", "Always", "Generate", "GenStatements", "GenStatement",
  "GenFor_statement", "When", "Or_coma", "When_items", "When_item",
  "Statement", "For_statement", "Repeat_statement", "While_statement",
  "Soft_assigns", "Soft_assign", "Cases", "Case", "Default", "Exprs",
  "Statements", "LSH", "Tokens_list", "Width", "BusBit", "ExtDir",
  "IntDir", "CurlyList", "CurlyItems", "CurlyItem", "Dotted", "Expr", 0
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
     345,   346,   347,   348,   349,    63,    58,   124,    94,    38,
     350,   351,   352,   353,    60,    62,    43,    45,   354,   355,
      42,    47,    37,   356,   357,    35,    40,    41,    59,    44,
      61,    46,    64,    91,    93,   123,   125,    33,   126
};
# endif

/* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint8 yyr1[] =
{
       0,   129,   130,   131,   131,   132,   132,   133,   134,   134,
     134,   135,   135,   135,   136,   136,   137,   137,   137,   137,
     137,   138,   138,   139,   139,   139,   139,   139,   139,   139,
     139,   139,   139,   139,   139,   139,   139,   140,   140,   140,
     140,   141,   142,   142,   142,   142,   142,   142,   142,   142,
     142,   142,   142,   142,   143,   143,   143,   143,   144,   145,
     145,   145,   145,   145,   145,   145,   145,   146,   146,   147,
     147,   147,   147,   147,   147,   147,   147,   148,   148,   148,
     148,   149,   149,   150,   150,   150,   150,   150,   150,   150,
     150,   150,   150,   150,   151,   151,   151,   151,   152,   152,
     153,   154,   154,   155,   156,   156,   157,   157,   158,   158,
     158,   158,   158,   158,   158,   158,   158,   158,   159,   159,
     160,   160,   160,   161,   161,   161,   161,   162,   162,   163,
     163,   164,   164,   164,   164,   164,   165,   165,   166,   167,
     167,   168,   168,   168,   168,   168,   168,   168,   168,   168,
     168,   168,   168,   168,   169,   170,   170,   170,   170,   171,
     171,   172,   172,   173,   173,   173,   174,   174,   174,   174,
     174,   174,   174,   174,   174,   174,   174,   174,   174,   174,
     174,   174,   174,   174,   174,   174,   174,   174,   174,   174,
     174,   174,   174,   174,   174,   174,   174,   174,   174,   174,
     174,   174,   174,   174,   175,   176,   177,   178,   178,   179,
     180,   180,   181,   181,   182,   182,   183,   183,   184,   184,
     185,   185,   185,   185,   185,   185,   185,   186,   186,   187,
     187,   187,   188,   189,   189,   189,   189,   189,   189,   189,
     189,   189,   189,   190,   190,   190,   190,   190,   190,   190,
     190,   190,   190,   190,   190,   191,   192,   192,   193,   193,
     194,   194,   194,   194,   194,   195,   195,   195,   195,   195,
     195,   195,   195,   195,   195,   195,   195,   195,   195,   195,
     195,   195,   195,   195,   195,   195,   195,   195,   195,   195,
     195,   195,   195,   195,   195,   195,   195,   195,   195,   195,
     195,   195,   195,   195,   195,   195,   195,   195,   195,   195,
     195,   195,   195,   195,   195,   195,   195,   195,   195
};

/* YYR2[YYN] -- Number of symbols composing right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     1,     2,     1,     1,     1,     6,     4,     3,
       0,     1,     4,     3,     3,     1,     2,     3,     3,     4,
       1,     2,     0,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     2,     2,     3,
       6,     2,     3,     3,     3,     5,     4,     5,     4,     6,
       5,     4,     4,     5,     5,     6,     7,     6,     5,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     6,
       5,     7,     6,     8,     9,     9,    10,     6,     5,     8,
       9,     2,     1,     3,     3,     3,     4,     5,     3,     4,
       4,     4,     3,     4,     3,     4,     4,     5,     3,     4,
       5,     3,     1,     3,     3,     1,     4,     3,     5,     6,
       3,     5,     6,     6,     6,     7,     8,     7,     3,     1,
       2,     5,     4,     4,     2,     2,     2,     3,     1,     5,
       2,     4,     2,     2,     4,     3,     2,     3,     3,     2,
       1,     3,     5,     3,     1,     1,     1,     1,     1,     1,
       1,     1,     5,     7,     9,     2,     2,     2,     4,     1,
       1,     3,     1,     2,     2,     1,     3,     2,     2,     5,
       3,     4,     5,     4,     5,     5,     7,     3,     3,     3,
       4,     3,     5,     2,     3,     3,     4,     5,     6,     7,
       6,     6,     7,     6,     7,     3,     3,     2,     1,     1,
       1,     2,     1,     5,     9,     5,     5,     3,     1,     3,
       2,     1,     3,     3,     3,     3,     3,     1,     2,     1,
       1,     2,     3,     3,     2,     1,     1,     3,     1,     5,
       5,     5,     3,     1,     1,     1,     2,     2,     2,     2,
       2,     2,     3,     1,     1,     1,     1,     1,     2,     2,
       1,     1,     1,     1,     1,     3,     3,     1,     2,     1,
       3,     3,     4,     4,     6,     1,     1,     1,     1,     1,
       1,     4,     1,     1,     1,     1,     1,     1,     2,     3,
       3,     2,     5,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     4,     3,
       1,     2,     2,     2,     2,     2,     2,     2,     2
};

/* YYDEFACT[STATE-NAME] -- Default rule to reduce with in state
   STATE-NUM when YYTABLE doesn't specify something else to do.  Zero
   means the default is an error.  */
static const yytype_uint16 yydefact[] =
{
       0,     0,     0,     0,     2,     4,     5,     6,    10,     0,
      38,    37,     1,     3,     0,     0,     0,   267,   265,   272,
     273,   274,   275,   276,   277,   269,   270,   268,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   310,   266,
      39,     0,     0,    11,    22,     0,     0,     0,     0,   278,
     281,     0,   315,   316,   312,   314,   313,   311,     0,     0,
     257,   259,   317,   318,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     9,     0,   105,    20,   233,   234,   235,     0,
       0,    15,     0,     0,     0,   243,   244,   253,   254,   245,
       0,   246,   247,     0,     0,     0,     0,     0,     0,     0,
       0,    35,     0,   250,   251,   252,    36,     0,    22,    34,
      31,    23,    24,    32,    33,    28,    29,    30,    25,    26,
      27,     0,     0,     0,     0,   217,   261,   260,     0,   279,
     280,     0,   309,     0,   255,   258,   294,   295,   300,   299,
     301,   303,   304,   293,   296,   297,   298,     0,   289,   288,
     290,   307,   306,   305,   291,   292,   283,   285,   302,   284,
     286,   287,     0,     0,     8,     0,   237,   240,   236,   238,
     241,   239,    13,     0,     0,    16,     0,     0,     0,     0,
       0,     0,     0,   220,     0,     0,     0,     0,     0,   226,
     225,   248,   249,   228,     0,   220,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   202,     0,     0,     0,     0,     0,     0,   136,   198,
     199,   200,     0,   225,     0,     0,     0,     0,     0,     0,
       0,   102,     0,     0,     0,     0,    41,     0,    68,     0,
      67,     0,     0,     0,     0,   250,   151,   144,   145,   146,
     147,   148,   150,     0,   140,   149,     7,    21,     0,     0,
     228,     0,     0,     0,    40,   308,     0,     0,   262,   263,
       0,     0,     0,   232,   271,   256,     0,   107,     0,   104,
     242,    12,    14,    18,     0,    17,     0,   110,     0,     0,
     132,   133,     0,     0,   221,   224,   124,   125,   126,     0,
      59,    60,    61,    62,    63,    64,    65,    66,     0,     0,
       0,     0,     0,     0,    43,     0,   197,     0,     0,     0,
       0,   167,     0,   219,     0,     0,     0,     0,     0,     0,
       0,   168,     0,     0,     0,     0,     0,     0,     0,     0,
     157,   156,   155,     0,   183,   137,     0,     0,   201,     0,
       0,     0,     0,     0,     0,    94,     0,     0,    98,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     138,   139,    42,     0,     0,     0,    44,     0,   228,     0,
     216,     0,     0,     0,     0,   282,   106,    19,     0,     0,
       0,   119,     0,     0,     0,   135,     0,     0,   128,     0,
       0,     0,   222,   223,     0,     0,     0,     0,     0,     0,
     227,     0,     0,     0,   179,     0,   178,     0,   166,   218,
       0,   177,   184,     0,     0,     0,     0,   208,     0,     0,
     170,   185,     0,   181,     0,   195,   196,     0,     0,     0,
     162,   165,     0,     0,     0,     0,     0,     0,     0,   103,
      95,     0,   101,    96,    99,     0,     0,     0,     0,     0,
       0,     0,    82,     0,     0,     0,     0,     0,     0,     0,
     141,     0,     0,   143,    46,     0,    51,    52,     0,     0,
      48,     0,   264,   230,   231,   229,   108,     0,   120,     0,
       0,     0,     0,    53,   130,   134,     0,   131,     0,     0,
       0,   123,     0,     0,     0,     0,    54,   186,     0,     0,
     180,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   163,   164,   159,   158,   160,     0,     0,   173,
       0,   171,     0,   111,   100,    97,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    81,     0,    70,     0,     0,
       0,     0,     0,    78,     0,     0,     0,    47,    45,    50,
       0,     0,   113,   118,   114,     0,     0,   127,   109,     0,
       0,    58,     0,    57,    55,   187,   203,   169,   175,     0,
       0,   211,     0,     0,     0,     0,     0,   207,   209,   206,
     182,   205,   161,   174,   172,   112,     0,     0,    88,     0,
       0,    83,   228,     0,    92,     0,    84,    85,    69,     0,
       0,    72,     0,    77,   142,   152,     0,    49,   122,     0,
     117,     0,   115,     0,    56,     0,     0,   188,   210,     0,
     190,     0,   191,     0,   193,     0,     0,     0,     0,    91,
      89,    90,     0,    86,    93,     0,    71,     0,     0,     0,
       0,   121,   129,   116,   176,   215,   214,   189,   213,   212,
     192,   194,     0,     0,    73,    87,     0,     0,     0,    79,
     153,     0,     0,    74,     0,    75,    80,     0,   204,    76,
     154
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,     3,     4,     5,     6,    15,    44,   100,   101,   127,
     128,     7,   266,   267,   268,   206,   328,   259,   133,   134,
     481,   482,   269,   136,   270,   250,   251,    93,    94,   271,
     410,   411,   207,   417,   418,   202,   272,   140,   273,   274,
     275,   255,   547,   459,   460,   343,   239,   240,   241,   446,
     447,   600,   601,   602,   603,   344,   242,   214,   314,   315,
     141,   142,    38,    59,    60,    39,   145
};

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
#define YYPACT_NINF -473
static const yytype_int16 yypact[] =
{
      27,    23,    49,    55,    27,  -473,  -473,  -473,   -51,    84,
    1456,  -473,  -473,  -473,    33,   -39,    56,  -473,   -60,  -473,
    -473,  -473,  -473,  -473,  -473,  -473,    64,  -473,  1456,  1456,
    1456,  1456,  1456,  1456,  1456,  1456,  1456,  1456,  -473,  -473,
    4682,    44,    37,  -473,  4485,   104,  1456,   127,  1456,  -473,
      48,  1456,  -473,  -473,  -473,  -473,  -473,  -473,  3727,   -59,
    -473,  2313,  -473,  -473,  1456,  1456,  1456,  1456,  1456,  1456,
    1456,  1456,  1456,  1456,  1456,  1456,  1456,  1456,  1456,  1456,
    1456,  1456,  1456,  1456,  1456,  1456,  1456,  1456,  1456,  1456,
      63,   195,  -473,   -14,  -473,  -473,    98,   242,   185,   138,
     121,  -473,    12,    43,    13,   248,   255,  -473,  -473,  -473,
     272,  -473,  -473,  2274,    34,   276,    14,    21,  2274,    16,
     291,  -473,  4006,  -473,  -473,  -473,  -473,   295,  4485,  -473,
    -473,  -473,  -473,  -473,  -473,  -473,  -473,  -473,  -473,  -473,
    -473,    22,    19,   305,   122,  4682,    71,  -473,  2351,  -473,
    -473,  3759,  -473,  1456,  -473,  -473,  4709,   467,    10,    10,
      10,   254,   254,  -473,   364,   364,   364,  4596,  2523,   364,
     648,   485,   485,   485,   254,   254,   263,   263,    10,  -473,
    -473,  -473,  1456,   236,  -473,    35,  -473,  -473,   347,  -473,
    -473,  -473,  -473,   202,   216,  -473,   366,  1456,   371,   -38,
     376,    46,   384,    89,    39,   177,    15,    11,   271,  -473,
    -473,  -473,  -473,   284,   286,    85,    11,    22,   272,  1689,
     289,  1456,   401,   292,   293,   299,  2274,   300,   302,  2274,
     412,  -473,  1456,  1456,   303,  1456,    65,  1781,  -473,  -473,
    -473,  -473,    -8,   304,   307,  1456,   306,   308,   309,    21,
       5,  -473,   415,   100,   415,   313,  -473,   143,  -473,   416,
    -473,   144,  3657,   314,   316,   419,  -473,  -473,  -473,  -473,
    -473,  -473,  -473,  4502,  -473,  -473,  -473,  -473,   315,   272,
     -24,   272,   151,   420,  -473,  -473,  1456,  1456,  -473,  -473,
    1456,  1456,  1456,  -473,  -473,  -473,  1456,  4682,  1456,  -473,
    -473,  -473,  -473,  -473,  4569,   318,   722,  -473,   319,   434,
    -473,  -473,   790,    75,  -473,    48,  -473,  -473,  -473,  1456,
    -473,  -473,  -473,  -473,  -473,  -473,  -473,  -473,   323,    11,
     324,   326,  1456,   272,  -473,  1202,  -473,   327,   330,   272,
     331,  -473,   445,  -473,  1802,  1456,  2673,   334,  1456,  1456,
    1456,  -473,    11,  1456,  1893,   336,  2587,  2700,  1456,  1559,
    -473,  -473,  -473,   931,  -473,  -473,  1316,  1316,  -473,   335,
     157,  1456,  1456,   112,   415,  -473,   415,   168,  -473,   234,
     216,  1668,   162,   216,  1668,   453,  3760,  1456,    11,   341,
    -473,  -473,  -473,    70,   342,   354,  -473,  1456,   -24,   188,
    4682,  3850,  2437,  2469,  2555,  4682,  4682,  -473,   359,    47,
     192,  -473,   196,   335,   360,  -473,   460,   199,  -473,   200,
     134,   370,  -473,  -473,   204,   177,   362,  1456,  1456,  2792,
    -473,   369,   208,  1456,  -473,   385,  -473,  2274,  -473,  -473,
    3882,  -473,  -473,  3973,  4005,  4096,   267,  -473,   368,  4128,
    -473,  -473,  1456,  -473,  4219,  -473,  -473,  1456,  1456,   -19,
    -473,  4682,  1456,  2819,  1456,  2911,   209,   386,  2938,  4682,
    -473,   269,  -473,  -473,  -473,   213,    18,    22,   272,   272,
     272,  1668,  -473,  1951,   216,  1668,   214,  1668,   422,  4006,
    -473,  4251,   281,  -473,  -473,   387,  -473,  -473,  3030,   388,
    -473,  1456,  -473,  -473,  -473,  -473,  -473,   373,  -473,   390,
     335,   392,   219,  -473,   396,  -473,   399,  -473,   403,   226,
     335,  -473,   406,  1456,  3057,  3149,  -473,  -473,   407,  3176,
    -473,  2009,  2274,  1338,  1456,  1456,  1456,    11,  1456,  2274,
    3268,  2274,  4682,  4682,  -473,  -473,  -473,   931,  3295,  -473,
    3387,  -473,   408,  -473,  -473,  -473,   411,   272,    86,   272,
     413,   519,    93,   414,   423,  -473,  2067,  -473,   229,  1668,
     474,   424,   475,  -473,  3883,  4006,  1456,  -473,  -473,  -473,
    3414,  1434,  -473,  -473,  -473,   426,  1456,  -473,  -473,   427,
     230,  -473,  3506,  -473,  -473,  -473,  -473,  -473,   496,   442,
    1027,  -473,   489,   -23,  1143,  1186,  3533,  -473,  4682,  -473,
    -473,  -473,  -473,  -473,  -473,  -473,  1668,   428,  -473,   431,
     432,   301,   -24,   433,   311,   435,  -473,  -473,  -473,   436,
     499,  -473,  1668,  -473,  -473,   514,  3625,  -473,  -473,  4342,
    -473,  4374,  -473,   439,  -473,  2274,  2125,  -473,  -473,   507,
    -473,  2214,  -473,   508,  -473,   509,    11,  1668,   505,  -473,
    -473,  -473,   446,   312,  -473,  1668,  -473,  1668,   510,  4006,
      11,  -473,  -473,  -473,  -473,  -473,  -473,  -473,  -473,  -473,
    -473,  -473,   260,   511,  -473,  -473,  1668,   524,   517,  -473,
    -473,   265,  2274,  -473,   525,  -473,  -473,  4006,  -473,  -473,
    -473
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -473,  -473,  -473,   559,  -473,  -473,  -473,  -321,   389,   454,
    -473,   -11,   -10,    -3,    28,  -473,   159,  -473,  -473,  -473,
    -374,  -472,    38,  -473,    40,  -106,   211,  -473,   418,    42,
    -355,    78,  -193,  -473,    77,   458,    50,  -473,  -254,  -271,
    -473,   488,  -473,  -473,    58,    -4,  -473,  -473,  -473,  -381,
      69,  -133,  -377,  -368,   -40,  -217,  -100,   -66,   -15,   -13,
     -41,  -473,   -30,  -473,   455,   -47,   636
};

/* YYTABLE[YYPACT[STATE-NUM]].  What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule which
   number is the opposite.  If zero, do what YYDEFACT says.
   If YYTABLE_NINF, syntax error.  */
#define YYTABLE_NINF -181
static const yytype_int16 yytable[] =
{
     147,   102,   391,    49,   208,    50,   144,   492,   386,   565,
     487,   253,   354,   329,   466,   565,   203,   195,   203,   248,
     203,   257,   544,   213,   280,   366,   248,   213,     8,   249,
       1,   155,   196,   129,   130,   149,   258,   150,   557,   244,
      90,   131,    95,   316,   317,    96,    97,    98,   199,    90,
     310,   311,   507,     9,    10,    12,    46,   210,   512,   475,
     153,    47,   486,    48,    14,   519,   243,   154,   247,   200,
     360,   243,   132,   651,   209,   278,   282,    42,   306,    43,
     307,    91,   135,   209,   137,   197,   138,   198,   209,    16,
      91,    71,     2,    11,   139,   333,   286,   565,   545,   197,
     546,   252,   254,   184,   260,   185,   330,   331,   143,   238,
     186,   569,   367,   187,   256,   391,   337,   129,   130,   318,
      87,    88,    89,   375,   376,   131,   279,   283,   204,   205,
     204,   288,   146,   289,   201,   197,    35,   197,    35,   197,
      35,   197,   197,   373,   197,   197,   377,   361,   379,    41,
     245,   338,   340,   102,    99,   319,   132,   508,   201,   210,
     210,    92,   312,   568,   483,   590,   135,    45,   137,   210,
     138,    48,   243,   462,   464,   362,   209,   209,   139,   243,
      51,   363,   243,   182,   308,   565,   209,   287,   494,   209,
     243,   420,    47,   197,    48,   565,   209,   191,   197,   209,
     183,   335,   339,   336,   618,   370,    47,   209,    48,   197,
      47,   624,    48,   393,   565,   395,   197,   399,   378,   376,
     531,    95,   351,   648,    96,    97,    98,   648,   648,   426,
     470,   376,   649,   365,   374,   574,   653,   655,   193,   285,
     194,   286,   657,   320,   321,   322,   323,   324,   325,   326,
     327,   518,   448,   188,   189,   409,   192,   190,   667,   380,
     383,   381,   384,   211,   566,   394,   412,   430,   471,   396,
     212,   397,   419,   435,   467,   682,   286,   213,   484,   424,
     485,   246,   210,    66,    67,    68,   473,   376,   448,   691,
     407,   686,    66,    67,    68,   432,   261,   243,   421,   209,
     422,   276,   423,   391,   635,   210,   500,   243,   501,   509,
     284,   510,   243,   511,   209,   286,   515,   517,   516,   286,
     301,   521,   209,   286,   209,   528,   552,   286,   510,   209,
     556,   571,   194,   194,   243,    71,   585,   243,   510,   102,
     439,   210,   102,   589,    71,   510,   629,   643,   194,   510,
     439,   209,   474,   376,   209,   456,   298,  -179,   209,  -179,
      84,    85,   300,    86,    87,    88,    89,  -178,  -180,  -178,
    -180,   303,    86,    87,    88,    89,   305,   692,   495,   537,
     488,   309,   697,   499,   537,   536,   537,   555,   376,   313,
     243,   332,    65,    66,    67,    68,    69,    70,   690,   576,
     537,   604,   605,   333,   334,   345,   347,   209,   348,   349,
     558,   560,   562,   563,   564,   350,   352,   355,   353,   358,
     248,   382,   368,   369,   389,   398,   700,    47,   371,   372,
     387,   364,   388,   392,   243,   413,   243,   448,   243,   414,
     243,   197,   425,   102,   427,    71,   428,   433,   434,   436,
     437,   209,   442,   209,   451,   209,   409,   209,   489,   493,
     496,   559,   561,    78,    79,   514,    80,    81,    82,    83,
      84,    85,   497,    86,    87,    88,    89,   506,   513,   439,
     573,   570,   523,   572,   243,   243,   520,   527,   538,   581,
     210,   617,   243,   620,   243,   623,    66,    67,    68,    69,
      70,   209,   209,   530,   553,   577,   579,   209,   582,   209,
     584,   209,   586,    65,    66,    67,    68,    69,    70,   243,
     416,   588,   243,   591,   622,   595,   615,   439,   598,   616,
     631,   621,   626,   633,   645,   609,   209,   611,   646,   209,
     650,   627,   632,   619,   640,   642,   659,   625,    71,   660,
     661,   663,   669,   664,   665,   666,   448,   673,   677,   680,
     681,   684,   439,    13,   685,   630,    71,   693,   689,   243,
     448,    82,    83,    84,    85,   696,    86,    87,    88,    89,
     695,   699,   277,   302,   522,   243,   209,   472,   583,    82,
      83,    84,    85,   587,    86,    87,    88,    89,   243,   243,
     281,   237,   209,   299,   243,   612,   607,   662,   295,   210,
     243,     0,   658,     0,     0,   209,   209,     0,   243,     0,
     243,   209,     0,   210,     0,     0,   209,   209,   668,     0,
       0,     0,     0,     0,     0,   209,     0,   209,     0,   243,
     209,   674,   676,     0,     0,   243,    40,   679,     0,     0,
       0,     0,     0,   683,     0,     0,   209,     0,     0,     0,
       0,   687,   209,   688,    52,    53,    54,    55,    56,    57,
      58,    61,    62,    63,     0,     0,    65,    66,    67,    68,
      69,    70,   694,     0,   148,     0,     0,   151,   698,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     156,   157,   158,   159,   160,   161,   162,   163,   164,   165,
     166,   167,   168,   169,   170,   171,   172,   173,   174,   175,
     176,   177,   178,   179,   180,   181,    17,    18,     0,    71,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    19,
      20,    21,     0,     0,     0,    22,    23,    24,    79,     0,
      80,    81,    82,    83,    84,    85,     0,    86,    87,    88,
      89,     0,     0,     0,     0,     0,    25,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    26,     0,    61,
       0,     0,     0,     0,    17,    18,     0,     0,     0,     0,
       0,     0,    27,     0,     0,     0,     0,    19,    20,    21,
      28,     0,    29,    22,    23,    24,     0,     0,   297,    30,
      31,    32,     0,     0,     0,     0,     0,     0,     0,    33,
       0,     0,     0,   304,    25,     0,     0,     0,    34,   408,
       0,     0,     0,   409,     0,     0,     0,    35,     0,    36,
      37,     0,     0,     0,     0,    26,     0,   346,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   356,   357,
      27,   359,     0,     0,     0,     0,     0,     0,    28,     0,
      29,     0,     0,     0,     0,     0,     0,    30,    31,    32,
       0,     0,     0,     0,     0,     0,     0,    33,     0,     0,
       0,     0,     0,     0,     0,     0,    34,   415,     0,     0,
       0,   416,     0,     0,     0,    35,     0,    36,    37,     0,
       0,     0,   400,   401,     0,     0,   402,   403,   404,     0,
       0,     0,   405,     0,   406,    17,    18,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    19,    20,
      21,     0,     0,     0,    22,    23,    24,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   429,     0,
     457,   458,     0,     0,     0,    25,     0,     0,     0,     0,
       0,   440,     0,     0,   443,   444,   445,     0,     0,   449,
       0,     0,     0,     0,   454,     0,    26,     0,     0,   461,
       0,     0,   463,   465,     0,     0,     0,   468,   469,     0,
       0,    27,     0,     0,     0,     0,     0,     0,     0,    28,
       0,    29,     0,   491,     0,     0,     0,     0,    30,    31,
      32,    17,    18,   498,     0,     0,     0,     0,    33,     0,
       0,     0,     0,     0,    19,    20,    21,    34,     0,     0,
      22,    23,    24,     0,     0,     0,    35,     0,    36,    37,
       0,     0,     0,   524,   525,     0,     0,     0,     0,   529,
       0,    25,     0,     0,     0,     0,     0,     0,   647,   599,
       0,     0,     0,     0,     0,     0,     0,     0,   540,     0,
       0,     0,    26,   542,   543,     0,     0,     0,   548,     0,
     550,     0,     0,     0,     0,     0,     0,    27,     0,     0,
       0,     0,     0,     0,     0,    28,     0,    29,     0,     0,
       0,     0,     0,     0,    30,    31,    32,     0,     0,     0,
       0,     0,     0,     0,    33,     0,     0,   580,     0,     0,
       0,     0,     0,    34,     0,     0,     0,    17,    18,     0,
       0,     0,    35,     0,    36,    37,     0,     0,     0,   592,
      19,    20,    21,     0,     0,     0,    22,    23,    24,     0,
       0,     0,   606,     0,   608,     0,     0,     0,     0,     0,
       0,     0,     0,   461,     0,     0,     0,    25,     0,     0,
      17,    18,     0,     0,   652,   599,     0,     0,     0,     0,
       0,     0,     0,    19,    20,    21,    17,    18,    26,    22,
      23,    24,   636,     0,     0,     0,     0,   639,     0,    19,
      20,    21,   641,    27,     0,    22,    23,    24,     0,     0,
      25,    28,     0,    29,     0,     0,     0,   654,   599,     0,
      30,    31,    32,     0,     0,     0,    25,     0,     0,     0,
      33,    26,     0,     0,     0,     0,     0,     0,     0,    34,
       0,     0,     0,     0,     0,     0,    27,    26,    35,     0,
      36,    37,     0,     0,    28,     0,    29,     0,     0,     0,
       0,     0,    27,    30,    31,    32,     0,     0,     0,     0,
      28,     0,    29,    33,     0,     0,     0,     0,     0,    30,
      31,    32,    34,     0,     0,     0,     0,     0,     0,    33,
       0,    35,     0,    36,    37,     0,     0,     0,    34,   431,
      17,    18,     0,     0,     0,     0,     0,    35,     0,    36,
      37,     0,     0,    19,    20,    21,     0,     0,     0,    22,
      23,    24,    17,    18,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    19,    20,    21,     0,     0,
      25,    22,    23,    24,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    26,    25,     0,     0,     0,     0,     0,     0,     0,
     599,     0,     0,     0,     0,     0,    27,     0,     0,     0,
       0,     0,     0,    26,    28,     0,    29,     0,     0,     0,
       0,     0,     0,    30,    31,    32,     0,     0,    27,     0,
       0,     0,     0,    33,     0,     0,    28,     0,    29,     0,
       0,   204,    34,     0,     0,    30,    31,    32,    17,    18,
       0,    35,     0,    36,    37,    33,     0,     0,     0,     0,
       0,    19,    20,    21,    34,     0,     0,    22,    23,    24,
      17,    18,     0,    35,     0,    36,    37,     0,     0,     0,
       0,     0,     0,    19,    20,    21,     0,     0,    25,    22,
      23,    24,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    26,
      25,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    27,     0,     0,     0,     0,     0,
       0,    26,    28,     0,    29,     0,     0,     0,     0,     0,
       0,    30,    31,    32,     0,     0,    27,     0,     0,     0,
       0,    33,     0,     0,    28,     0,    29,     0,     0,     0,
      34,   638,     0,    30,    31,    32,     0,     0,     0,    35,
       0,    36,    37,    33,   215,     0,   216,     0,     0,     0,
     217,     0,    34,     0,     0,     0,     0,     0,     0,   218,
       0,    35,     0,    36,    37,     0,    64,    65,    66,    67,
      68,    69,    70,     0,   219,     0,   220,     0,     0,     0,
       0,   221,   222,     0,     0,     0,     0,   223,   224,   225,
       0,     0,     0,   226,     0,     0,     0,     0,   227,   228,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   229,     0,   230,   231,     0,     0,     0,
      71,     0,     0,     0,     0,   232,   233,    72,    73,    74,
     234,     0,     0,     0,    75,     0,    76,    77,    78,    79,
       0,    80,    81,    82,    83,    84,    85,     0,    86,    87,
      88,    89,     0,   215,   235,   216,   476,   455,     0,   477,
       0,   236,     0,     0,    35,     0,     0,     0,   478,   479,
     480,     0,     0,     0,   215,     0,   216,     0,     0,     0,
     217,     0,     0,   219,     0,   220,     0,     0,     0,   218,
     221,   222,     0,     0,     0,     0,   223,   224,   225,     0,
       0,     0,   226,     0,   219,   341,   220,   227,   228,     0,
       0,   221,   222,     0,     0,     0,     0,   223,   224,   225,
       0,     0,   229,   226,   230,   231,     0,     0,   227,   228,
       0,     0,     0,     0,   232,   233,     0,     0,     0,   234,
       0,     0,     0,   229,     0,   230,   231,     0,     0,     0,
       0,     0,     0,     0,     0,   232,   233,     0,     0,     0,
     234,     0,     0,   235,     0,   342,   215,     0,   216,     0,
     236,     0,   217,    35,     0,     0,     0,     0,     0,     0,
       0,   218,     0,     0,   235,     0,     0,   215,     0,   216,
       0,   236,     0,   217,    35,     0,   219,     0,   220,     0,
       0,     0,   218,   221,   222,     0,     0,     0,     0,   223,
     224,   225,     0,     0,     0,   226,     0,   219,   438,   220,
     227,   228,     0,     0,   221,   222,     0,     0,     0,     0,
     223,   224,   225,     0,     0,   229,   226,   230,   231,     0,
       0,   227,   228,     0,     0,     0,     0,   232,   233,     0,
       0,     0,   234,     0,     0,     0,   229,     0,   230,   231,
       0,     0,     0,     0,     0,     0,     0,     0,   232,   233,
       0,     0,     0,   234,     0,     0,   235,     0,   215,   364,
     216,     0,     0,   236,   217,     0,    35,     0,     0,     0,
       0,     0,     0,   218,     0,     0,     0,   235,     0,     0,
       0,     0,     0,     0,   236,     0,     0,    35,   219,     0,
     220,     0,     0,     0,     0,   221,   222,     0,     0,     0,
       0,   223,   224,   225,     0,     0,     0,   226,     0,     0,
       0,     0,   227,   228,     0,     0,   215,     0,   216,     0,
       0,     0,   217,     0,     0,     0,     0,   229,   450,   230,
     231,   218,     0,     0,     0,     0,     0,     0,     0,   232,
     233,     0,     0,     0,   234,     0,   219,     0,   220,     0,
       0,     0,     0,   221,   222,     0,     0,     0,     0,   223,
     224,   225,     0,     0,     0,   226,     0,   567,   235,     0,
     227,   228,     0,     0,   215,   236,   216,     0,    35,     0,
     217,     0,     0,     0,     0,   229,     0,   230,   231,   218,
       0,     0,     0,     0,     0,     0,     0,   232,   233,     0,
       0,     0,   234,     0,   219,   597,   220,     0,     0,     0,
       0,   221,   222,     0,     0,     0,     0,   223,   224,   225,
       0,     0,     0,   226,     0,     0,   235,     0,   227,   228,
       0,     0,   215,   236,   216,     0,    35,     0,   217,     0,
       0,     0,     0,   229,     0,   230,   231,   218,     0,     0,
       0,     0,     0,     0,     0,   232,   233,     0,     0,     0,
     234,     0,   219,     0,   220,     0,     0,     0,     0,   221,
     222,     0,     0,     0,     0,   223,   224,   225,     0,     0,
       0,   226,     0,   628,   235,     0,   227,   228,     0,     0,
     215,   236,   216,     0,    35,     0,   217,     0,     0,     0,
       0,   229,     0,   230,   231,   218,     0,     0,     0,     0,
       0,     0,     0,   232,   233,     0,     0,     0,   234,     0,
     219,     0,   220,     0,     0,     0,     0,   221,   222,     0,
       0,     0,     0,   223,   224,   225,     0,     0,     0,   226,
       0,     0,   235,     0,   227,   228,     0,     0,     0,   236,
       0,     0,    35,     0,     0,     0,     0,     0,     0,   229,
       0,   230,   231,     0,     0,     0,     0,     0,     0,     0,
       0,   232,   233,     0,     0,     0,   234,     0,     0,   215,
       0,   216,     0,     0,     0,   217,     0,     0,     0,     0,
       0,     0,     0,     0,   218,     0,     0,     0,     0,     0,
     235,     0,     0,   675,     0,     0,     0,   236,     0,   219,
      35,   220,     0,     0,     0,     0,   221,   222,     0,     0,
       0,     0,   223,   224,   225,     0,     0,     0,   226,     0,
       0,     0,     0,   227,   228,     0,     0,     0,     0,   215,
       0,   216,     0,     0,     0,   217,     0,     0,   229,     0,
     230,   231,     0,     0,   218,     0,     0,     0,     0,     0,
     232,   233,     0,     0,     0,   234,     0,     0,     0,   219,
       0,   220,     0,     0,     0,     0,   221,   222,     0,     0,
       0,     0,   223,   224,   225,     0,     0,     0,   226,   235,
       0,     0,   678,   227,   228,     0,   236,     0,     0,    35,
      64,    65,    66,    67,    68,    69,    70,     0,   229,     0,
     230,   231,     0,     0,     0,     0,     0,     0,     0,     0,
     232,   233,     0,     0,     0,   234,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    64,    65,
      66,    67,    68,    69,    70,     0,     0,     0,     0,   235,
       0,     0,     0,     0,    71,     0,   236,     0,     0,    35,
       0,    72,    73,    74,     0,     0,     0,     0,    75,     0,
      76,    77,    78,    79,     0,    80,    81,    82,    83,    84,
      85,     0,    86,    87,    88,    89,     0,     0,     0,   290,
     291,     0,    71,     0,     0,     0,     0,     0,    35,    72,
      73,    74,     0,     0,     0,     0,    75,   292,    76,    77,
      78,    79,     0,    80,    81,    82,    83,    84,    85,     0,
      86,    87,    88,    89,    64,    65,    66,    67,    68,    69,
      70,     0,     0,     0,     0,   293,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    64,    65,    66,    67,
      68,    69,    70,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    71,     0,
       0,     0,     0,     0,     0,    72,    73,    74,     0,     0,
       0,     0,    75,     0,    76,    77,    78,    79,     0,    80,
      81,    82,    83,    84,    85,     0,    86,    87,    88,    89,
      71,    65,    66,    67,    68,    69,    70,    72,    73,    74,
       0,   503,     0,     0,    75,     0,    76,    77,    78,    79,
       0,    80,    81,    82,    83,    84,    85,     0,    86,    87,
      88,    89,    64,    65,    66,    67,    68,    69,    70,     0,
       0,     0,     0,   504,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    71,     0,     0,     0,     0,     0,
       0,    72,    73,    74,    64,    65,    66,    67,    68,    69,
      70,    77,    78,    79,     0,    80,    81,    82,    83,    84,
      85,     0,    86,    87,    88,    89,    71,     0,     0,     0,
       0,     0,     0,    72,    73,    74,     0,     0,     0,     0,
      75,     0,    76,    77,    78,    79,     0,    80,    81,    82,
      83,    84,    85,     0,    86,    87,    88,    89,    71,     0,
       0,     0,     0,     0,     0,    72,    73,    74,     0,   505,
       0,     0,    75,     0,    76,    77,    78,    79,     0,    80,
      81,    82,    83,    84,    85,     0,    86,    87,    88,    89,
      64,    65,    66,    67,    68,    69,    70,   452,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    64,    65,    66,
      67,    68,    69,    70,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    71,     0,     0,     0,     0,     0,
       0,    72,    73,    74,     0,     0,     0,     0,    75,     0,
      76,    77,    78,    79,     0,    80,    81,    82,    83,    84,
      85,    71,    86,    87,    88,    89,     0,     0,    72,    73,
      74,   441,     0,     0,     0,    75,     0,    76,    77,    78,
      79,     0,    80,    81,    82,    83,    84,    85,     0,    86,
      87,    88,    89,     0,     0,     0,     0,     0,   453,    64,
      65,    66,    67,    68,    69,    70,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    64,    65,    66,    67,
      68,    69,    70,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    71,     0,     0,     0,     0,     0,     0,
      72,    73,    74,     0,     0,     0,     0,    75,     0,    76,
      77,    78,    79,     0,    80,    81,    82,    83,    84,    85,
      71,    86,    87,    88,    89,     0,     0,    72,    73,    74,
     526,     0,     0,     0,    75,     0,    76,    77,    78,    79,
       0,    80,    81,    82,    83,    84,    85,     0,    86,    87,
      88,    89,     0,     0,     0,     0,     0,   549,    64,    65,
      66,    67,    68,    69,    70,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    64,    65,    66,    67,    68,
      69,    70,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    71,     0,     0,     0,     0,     0,     0,    72,
      73,    74,     0,     0,     0,     0,    75,     0,    76,    77,
      78,    79,     0,    80,    81,    82,    83,    84,    85,    71,
      86,    87,    88,    89,     0,     0,    72,    73,    74,   551,
       0,     0,     0,    75,     0,    76,    77,    78,    79,     0,
      80,    81,    82,    83,    84,    85,     0,    86,    87,    88,
      89,     0,     0,     0,     0,     0,   554,    64,    65,    66,
      67,    68,    69,    70,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    64,    65,    66,    67,    68,    69,
      70,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    71,     0,     0,     0,     0,     0,     0,    72,    73,
      74,     0,     0,     0,     0,    75,     0,    76,    77,    78,
      79,     0,    80,    81,    82,    83,    84,    85,    71,    86,
      87,    88,    89,     0,     0,    72,    73,    74,   578,     0,
       0,     0,    75,     0,    76,    77,    78,    79,     0,    80,
      81,    82,    83,    84,    85,     0,    86,    87,    88,    89,
       0,     0,     0,     0,     0,   593,    64,    65,    66,    67,
      68,    69,    70,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    64,    65,    66,    67,    68,    69,    70,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      71,     0,     0,     0,     0,     0,     0,    72,    73,    74,
       0,     0,     0,     0,    75,     0,    76,    77,    78,    79,
       0,    80,    81,    82,    83,    84,    85,    71,    86,    87,
      88,    89,     0,     0,    72,    73,    74,   594,     0,     0,
       0,    75,     0,    76,    77,    78,    79,     0,    80,    81,
      82,    83,    84,    85,     0,    86,    87,    88,    89,     0,
       0,     0,     0,     0,   596,    64,    65,    66,    67,    68,
      69,    70,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    64,    65,    66,    67,    68,    69,    70,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    71,
       0,     0,     0,     0,     0,     0,    72,    73,    74,     0,
       0,     0,     0,    75,     0,    76,    77,    78,    79,     0,
      80,    81,    82,    83,    84,    85,    71,    86,    87,    88,
      89,     0,     0,    72,    73,    74,   610,     0,     0,     0,
      75,     0,    76,    77,    78,    79,     0,    80,    81,    82,
      83,    84,    85,     0,    86,    87,    88,    89,     0,     0,
       0,     0,     0,   613,    64,    65,    66,    67,    68,    69,
      70,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    64,    65,    66,    67,    68,    69,    70,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    71,     0,
       0,     0,     0,     0,     0,    72,    73,    74,     0,     0,
       0,     0,    75,     0,    76,    77,    78,    79,     0,    80,
      81,    82,    83,    84,    85,    71,    86,    87,    88,    89,
       0,     0,    72,    73,    74,   614,     0,     0,     0,    75,
       0,    76,    77,    78,    79,     0,    80,    81,    82,    83,
      84,    85,     0,    86,    87,    88,    89,     0,     0,     0,
       0,     0,   637,    64,    65,    66,    67,    68,    69,    70,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      64,    65,    66,    67,    68,    69,    70,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    71,     0,     0,
       0,     0,     0,     0,    72,    73,    74,     0,     0,     0,
       0,    75,     0,    76,    77,    78,    79,     0,    80,    81,
      82,    83,    84,    85,    71,    86,    87,    88,    89,     0,
       0,    72,    73,    74,   644,     0,     0,     0,    75,     0,
      76,    77,    78,    79,     0,    80,    81,    82,    83,    84,
      85,     0,    86,    87,    88,    89,     0,     0,     0,     0,
       0,   656,    64,    65,    66,    67,    68,    69,    70,     0,
       0,     0,   103,     0,   104,    96,    97,    98,   105,   106,
     107,   108,   109,   110,     0,     0,     0,   111,   112,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   113,   262,     0,   263,     0,     0,     0,   114,     0,
       0,     0,   115,   116,     0,     0,    71,     0,     0,     0,
     118,     0,     0,    72,    73,    74,   264,     0,     0,     0,
      75,     0,    76,    77,    78,    79,     0,    80,    81,    82,
      83,    84,    85,     0,    86,    87,    88,    89,     0,     0,
       0,     0,   265,   670,     0,     0,     0,     0,     0,   124,
     125,     0,     0,   385,    64,    65,    66,    67,    68,    69,
      70,     0,     0,     0,     0,   103,     0,   104,    96,    97,
      98,   105,   106,   107,   108,   109,   110,     0,     0,     0,
     111,   112,     0,     0,     0,     0,    64,    65,    66,    67,
      68,    69,    70,     0,   113,   262,   490,   263,     0,     0,
       0,   114,     0,     0,     0,   115,   116,     0,    71,     0,
       0,     0,     0,   118,     0,    72,    73,    74,     0,   264,
       0,     0,    75,     0,    76,    77,    78,    79,     0,    80,
      81,    82,    83,    84,    85,     0,    86,    87,    88,    89,
      71,     0,     0,     0,   152,   265,     0,    72,    73,    74,
       0,     0,   124,   125,    75,     0,    76,    77,    78,    79,
       0,    80,    81,    82,    83,    84,    85,     0,    86,    87,
      88,    89,     0,     0,     0,     0,   294,    64,    65,    66,
      67,    68,    69,    70,     0,     0,     0,     0,   103,     0,
     104,    96,    97,    98,   105,   106,   107,   108,   109,   110,
       0,     0,     0,   111,   112,     0,     0,     0,     0,    64,
      65,    66,    67,    68,    69,    70,     0,   113,   262,   634,
     263,     0,     0,     0,   114,     0,     0,     0,   115,   116,
       0,    71,     0,     0,     0,     0,   118,     0,    72,    73,
      74,     0,   264,     0,     0,    75,     0,    76,    77,    78,
      79,     0,    80,    81,    82,    83,    84,    85,     0,    86,
      87,    88,    89,    71,     0,     0,     0,   502,   265,     0,
      72,    73,    74,     0,     0,   124,   125,    75,     0,    76,
      77,    78,    79,     0,    80,    81,    82,    83,    84,    85,
       0,    86,    87,    88,    89,     0,     0,     0,     0,   532,
      64,    65,    66,    67,    68,    69,    70,     0,     0,     0,
       0,   103,     0,   104,    96,    97,    98,   105,   106,   107,
     108,   109,   110,     0,     0,     0,   111,   112,     0,     0,
       0,     0,    64,    65,    66,    67,    68,    69,    70,     0,
     113,   262,     0,   263,     0,     0,     0,   114,     0,     0,
       0,   115,   116,     0,    71,     0,     0,     0,     0,   118,
       0,    72,    73,    74,     0,   264,     0,     0,    75,     0,
      76,    77,    78,    79,     0,    80,    81,    82,    83,    84,
      85,     0,    86,    87,    88,    89,    71,     0,     0,     0,
     533,   265,     0,    72,    73,    74,     0,     0,   124,   125,
      75,     0,    76,    77,    78,    79,     0,    80,    81,    82,
      83,    84,    85,     0,    86,    87,    88,    89,     0,     0,
       0,     0,   534,    64,    65,    66,    67,    68,    69,    70,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    64,    65,    66,    67,    68,
      69,    70,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    71,     0,     0,
       0,     0,     0,     0,    72,    73,    74,     0,     0,     0,
       0,    75,     0,    76,    77,    78,    79,     0,    80,    81,
      82,    83,    84,    85,     0,    86,    87,    88,    89,    71,
       0,     0,     0,   535,     0,     0,    72,    73,    74,     0,
       0,     0,     0,    75,     0,    76,    77,    78,    79,     0,
      80,    81,    82,    83,    84,    85,     0,    86,    87,    88,
      89,     0,     0,     0,     0,   539,    64,    65,    66,    67,
      68,    69,    70,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    64,    65,
      66,    67,    68,    69,    70,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      71,     0,     0,     0,     0,     0,     0,    72,    73,    74,
       0,     0,     0,     0,    75,     0,    76,    77,    78,    79,
       0,    80,    81,    82,    83,    84,    85,     0,    86,    87,
      88,    89,    71,     0,     0,     0,   541,     0,     0,    72,
      73,    74,     0,     0,     0,     0,    75,     0,    76,    77,
      78,    79,     0,    80,    81,    82,    83,    84,    85,     0,
      86,    87,    88,    89,     0,     0,     0,     0,   575,    64,
      65,    66,    67,    68,    69,    70,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    64,    65,    66,    67,    68,    69,    70,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    71,     0,     0,     0,     0,     0,     0,
      72,    73,    74,     0,     0,     0,     0,    75,     0,    76,
      77,    78,    79,     0,    80,    81,    82,    83,    84,    85,
       0,    86,    87,    88,    89,    71,     0,     0,     0,   671,
       0,     0,    72,    73,    74,     0,     0,     0,     0,    75,
       0,    76,    77,    78,    79,     0,    80,    81,    82,    83,
      84,    85,     0,    86,    87,    88,    89,     0,     0,     0,
     103,   672,   104,    96,    97,    98,   105,   106,   107,   108,
     109,   110,     0,     0,     0,   111,   112,   103,     0,   104,
      96,    97,    98,   105,   106,   107,   108,   109,   110,   113,
       0,     0,   111,   112,     0,     0,   114,     0,     0,     0,
     115,   116,   117,     0,     0,     0,   113,   262,   118,   263,
     119,     0,   120,   114,     0,     0,     0,   115,   116,     0,
       2,     0,     0,     0,     0,   118,     0,     0,     0,     0,
       0,   264,   121,     0,     0,     0,     0,     0,   122,     0,
     123,     0,     0,     0,     0,     0,     0,   124,   125,   126,
       0,     0,     0,     0,     0,     0,   390,   265,     0,     0,
       0,     0,     0,     0,   124,   125,    64,    65,    66,    67,
      68,    69,    70,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    64,    65,    66,    67,    68,    69,    70,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   290,   291,     0,
      71,     0,     0,     0,     0,     0,     0,    72,    73,    74,
       0,     0,     0,     0,    75,   292,    76,    77,    78,    79,
       0,    80,    81,    82,    83,    84,    85,    71,    86,    87,
      88,    89,     0,     0,    72,    73,    74,     0,     0,     0,
       0,    75,   296,    76,    77,    78,    79,     0,    80,    81,
      82,    83,    84,    85,     0,    86,    87,    88,    89,    64,
      65,    66,    67,    68,    69,    70,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    65,    66,    67,
      68,    69,    70,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    71,     0,     0,     0,     0,     0,     0,
      72,    73,    74,     0,     0,     0,     0,    75,     0,    76,
      77,    78,    79,     0,    80,    81,    82,    83,    84,    85,
      71,    86,    87,    88,    89,     0,     0,    72,    73,    74,
       0,     0,     0,     0,     0,     0,    76,    77,    78,    79,
       0,    80,    81,    82,    83,    84,    85,     0,    86,    87,
      88,    89
};

static const yytype_int16 yycheck[] =
{
      47,    42,   273,    18,   104,    18,    46,   388,   262,   481,
     384,   117,   229,   206,   369,   487,     5,     5,     5,     5,
       5,     5,    41,     5,     5,    33,     5,     5,     5,    15,
       3,    61,    20,    44,    44,    50,    20,    50,    20,     5,
       5,    44,     5,     4,     5,     8,     9,    10,     5,     5,
       4,     5,     5,     4,     5,     0,   116,   104,   413,   380,
     119,   121,   383,   123,   115,   420,   113,   126,   115,    26,
       5,   118,    44,    96,   104,   141,   142,   116,   116,   118,
     118,    46,    44,   113,    44,   123,    44,   102,   118,     5,
      46,    81,    65,    44,    44,   119,   119,   569,   117,   123,
     119,   116,   117,   117,   119,   119,   206,   207,     4,   113,
      12,   485,   120,    15,   118,   386,   216,   128,   128,    80,
     110,   111,   112,   118,   119,   128,   141,   142,   115,   116,
     115,   146,     5,   146,   115,   123,   125,   123,   125,   123,
     125,   123,   123,   249,   123,   123,   252,    82,   254,   116,
     116,   217,   218,   194,   117,   116,   128,   110,   115,   206,
     207,   117,   116,   484,   381,   520,   128,   111,   128,   216,
     128,   123,   219,   366,   367,   110,   206,   207,   128,   226,
     116,   116,   229,   120,   199,   657,   216,   116,   118,   219,
     237,   116,   121,   123,   123,   667,   226,    12,   123,   229,
       5,   116,   217,   118,   118,   245,   121,   237,   123,   123,
     121,   118,   123,   279,   686,   281,   123,   283,   118,   119,
     437,     5,   226,   600,     8,     9,    10,   604,   605,   329,
     118,   119,   600,   237,   249,   489,   604,   605,   117,   117,
     119,   119,   616,    66,    67,    68,    69,    70,    71,    72,
      73,   117,   352,    11,    12,   121,   118,    15,   632,   116,
     116,   118,   118,    15,   481,   280,   306,   333,   374,   118,
      15,   120,   312,   339,   117,   656,   119,     5,   116,   319,
     118,     5,   329,    29,    30,    31,   118,   119,   388,   670,
     305,   665,    29,    30,    31,   335,     5,   344,   313,   329,
     315,     6,   315,   574,   575,   352,   118,   354,   120,   117,
       5,   119,   359,   117,   344,   119,   117,   117,   119,   119,
     118,   117,   352,   119,   354,   117,   117,   119,   119,   359,
     117,   117,   119,   119,   381,    81,   117,   384,   119,   380,
     344,   388,   383,   117,    81,   119,   117,   117,   119,   119,
     354,   381,   118,   119,   384,   359,   120,    56,   388,    58,
     106,   107,    15,   109,   110,   111,   112,    56,    56,    58,
      58,     5,   109,   110,   111,   112,     5,   117,   393,   119,
     384,     5,   117,   398,   119,   118,   119,   118,   119,     5,
     437,   120,    28,    29,    30,    31,    32,    33,   669,   118,
     119,   534,   535,   119,   118,   116,     5,   437,   116,   116,
     476,   477,   478,   479,   480,   116,   116,     5,   116,   116,
       5,     5,   118,   116,     5,     5,   697,   121,   120,   120,
     116,   118,   116,   118,   481,   116,   483,   537,   485,     5,
     487,   123,   119,   484,   120,    81,   120,   120,   118,   118,
       5,   481,   118,   483,   118,   485,   121,   487,     5,   118,
     118,   476,   477,    99,   100,     5,   102,   103,   104,   105,
     106,   107,   118,   109,   110,   111,   112,   118,   118,   483,
      58,   485,   120,   487,   531,   532,   116,   118,   120,   116,
     537,   557,   539,   559,   541,   561,    29,    30,    31,    32,
      33,   531,   532,   118,   118,   118,   118,   537,   118,   539,
     118,   541,   116,    28,    29,    30,    31,    32,    33,   566,
     121,   118,   569,   117,     5,   118,   118,   531,   532,   118,
      56,   118,   118,    58,    38,   539,   566,   541,    96,   569,
      51,   118,   118,   558,   118,   118,   118,   562,    81,   118,
     118,   118,    38,   118,   118,    56,   656,   118,    51,    51,
      51,    56,   566,     4,   118,   569,    81,    56,    58,   616,
     670,   104,   105,   106,   107,    58,   109,   110,   111,   112,
      56,    56,   128,   194,   425,   632,   616,   376,   510,   104,
     105,   106,   107,   516,   109,   110,   111,   112,   645,   646,
     142,   113,   632,   185,   651,   547,   537,   622,   153,   656,
     657,    -1,   616,    -1,    -1,   645,   646,    -1,   665,    -1,
     667,   651,    -1,   670,    -1,    -1,   656,   657,   632,    -1,
      -1,    -1,    -1,    -1,    -1,   665,    -1,   667,    -1,   686,
     670,   645,   646,    -1,    -1,   692,    10,   651,    -1,    -1,
      -1,    -1,    -1,   657,    -1,    -1,   686,    -1,    -1,    -1,
      -1,   665,   692,   667,    28,    29,    30,    31,    32,    33,
      34,    35,    36,    37,    -1,    -1,    28,    29,    30,    31,
      32,    33,   686,    -1,    48,    -1,    -1,    51,   692,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      64,    65,    66,    67,    68,    69,    70,    71,    72,    73,
      74,    75,    76,    77,    78,    79,    80,    81,    82,    83,
      84,    85,    86,    87,    88,    89,     4,     5,    -1,    81,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    17,
      18,    19,    -1,    -1,    -1,    23,    24,    25,   100,    -1,
     102,   103,   104,   105,   106,   107,    -1,   109,   110,   111,
     112,    -1,    -1,    -1,    -1,    -1,    44,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    65,    -1,   153,
      -1,    -1,    -1,    -1,     4,     5,    -1,    -1,    -1,    -1,
      -1,    -1,    80,    -1,    -1,    -1,    -1,    17,    18,    19,
      88,    -1,    90,    23,    24,    25,    -1,    -1,   182,    97,
      98,    99,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   107,
      -1,    -1,    -1,   197,    44,    -1,    -1,    -1,   116,   117,
      -1,    -1,    -1,   121,    -1,    -1,    -1,   125,    -1,   127,
     128,    -1,    -1,    -1,    -1,    65,    -1,   221,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   232,   233,
      80,   235,    -1,    -1,    -1,    -1,    -1,    -1,    88,    -1,
      90,    -1,    -1,    -1,    -1,    -1,    -1,    97,    98,    99,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   107,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   116,   117,    -1,    -1,
      -1,   121,    -1,    -1,    -1,   125,    -1,   127,   128,    -1,
      -1,    -1,   286,   287,    -1,    -1,   290,   291,   292,    -1,
      -1,    -1,   296,    -1,   298,     4,     5,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    17,    18,
      19,    -1,    -1,    -1,    23,    24,    25,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   332,    -1,
      39,    40,    -1,    -1,    -1,    44,    -1,    -1,    -1,    -1,
      -1,   345,    -1,    -1,   348,   349,   350,    -1,    -1,   353,
      -1,    -1,    -1,    -1,   358,    -1,    65,    -1,    -1,   363,
      -1,    -1,   366,   367,    -1,    -1,    -1,   371,   372,    -1,
      -1,    80,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    88,
      -1,    90,    -1,   387,    -1,    -1,    -1,    -1,    97,    98,
      99,     4,     5,   397,    -1,    -1,    -1,    -1,   107,    -1,
      -1,    -1,    -1,    -1,    17,    18,    19,   116,    -1,    -1,
      23,    24,    25,    -1,    -1,    -1,   125,    -1,   127,   128,
      -1,    -1,    -1,   427,   428,    -1,    -1,    -1,    -1,   433,
      -1,    44,    -1,    -1,    -1,    -1,    -1,    -1,    51,    52,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   452,    -1,
      -1,    -1,    65,   457,   458,    -1,    -1,    -1,   462,    -1,
     464,    -1,    -1,    -1,    -1,    -1,    -1,    80,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    88,    -1,    90,    -1,    -1,
      -1,    -1,    -1,    -1,    97,    98,    99,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   107,    -1,    -1,   501,    -1,    -1,
      -1,    -1,    -1,   116,    -1,    -1,    -1,     4,     5,    -1,
      -1,    -1,   125,    -1,   127,   128,    -1,    -1,    -1,   523,
      17,    18,    19,    -1,    -1,    -1,    23,    24,    25,    -1,
      -1,    -1,   536,    -1,   538,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   547,    -1,    -1,    -1,    44,    -1,    -1,
       4,     5,    -1,    -1,    51,    52,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    17,    18,    19,     4,     5,    65,    23,
      24,    25,   576,    -1,    -1,    -1,    -1,   581,    -1,    17,
      18,    19,   586,    80,    -1,    23,    24,    25,    -1,    -1,
      44,    88,    -1,    90,    -1,    -1,    -1,    51,    52,    -1,
      97,    98,    99,    -1,    -1,    -1,    44,    -1,    -1,    -1,
     107,    65,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   116,
      -1,    -1,    -1,    -1,    -1,    -1,    80,    65,   125,    -1,
     127,   128,    -1,    -1,    88,    -1,    90,    -1,    -1,    -1,
      -1,    -1,    80,    97,    98,    99,    -1,    -1,    -1,    -1,
      88,    -1,    90,   107,    -1,    -1,    -1,    -1,    -1,    97,
      98,    99,   116,    -1,    -1,    -1,    -1,    -1,    -1,   107,
      -1,   125,    -1,   127,   128,    -1,    -1,    -1,   116,   117,
       4,     5,    -1,    -1,    -1,    -1,    -1,   125,    -1,   127,
     128,    -1,    -1,    17,    18,    19,    -1,    -1,    -1,    23,
      24,    25,     4,     5,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    17,    18,    19,    -1,    -1,
      44,    23,    24,    25,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    65,    44,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      52,    -1,    -1,    -1,    -1,    -1,    80,    -1,    -1,    -1,
      -1,    -1,    -1,    65,    88,    -1,    90,    -1,    -1,    -1,
      -1,    -1,    -1,    97,    98,    99,    -1,    -1,    80,    -1,
      -1,    -1,    -1,   107,    -1,    -1,    88,    -1,    90,    -1,
      -1,   115,   116,    -1,    -1,    97,    98,    99,     4,     5,
      -1,   125,    -1,   127,   128,   107,    -1,    -1,    -1,    -1,
      -1,    17,    18,    19,   116,    -1,    -1,    23,    24,    25,
       4,     5,    -1,   125,    -1,   127,   128,    -1,    -1,    -1,
      -1,    -1,    -1,    17,    18,    19,    -1,    -1,    44,    23,
      24,    25,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    65,
      44,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    80,    -1,    -1,    -1,    -1,    -1,
      -1,    65,    88,    -1,    90,    -1,    -1,    -1,    -1,    -1,
      -1,    97,    98,    99,    -1,    -1,    80,    -1,    -1,    -1,
      -1,   107,    -1,    -1,    88,    -1,    90,    -1,    -1,    -1,
     116,   117,    -1,    97,    98,    99,    -1,    -1,    -1,   125,
      -1,   127,   128,   107,     5,    -1,     7,    -1,    -1,    -1,
      11,    -1,   116,    -1,    -1,    -1,    -1,    -1,    -1,    20,
      -1,   125,    -1,   127,   128,    -1,    27,    28,    29,    30,
      31,    32,    33,    -1,    35,    -1,    37,    -1,    -1,    -1,
      -1,    42,    43,    -1,    -1,    -1,    -1,    48,    49,    50,
      -1,    -1,    -1,    54,    -1,    -1,    -1,    -1,    59,    60,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    74,    -1,    76,    77,    -1,    -1,    -1,
      81,    -1,    -1,    -1,    -1,    86,    87,    88,    89,    90,
      91,    -1,    -1,    -1,    95,    -1,    97,    98,    99,   100,
      -1,   102,   103,   104,   105,   106,   107,    -1,   109,   110,
     111,   112,    -1,     5,   115,     7,     8,   118,    -1,    11,
      -1,   122,    -1,    -1,   125,    -1,    -1,    -1,    20,    21,
      22,    -1,    -1,    -1,     5,    -1,     7,    -1,    -1,    -1,
      11,    -1,    -1,    35,    -1,    37,    -1,    -1,    -1,    20,
      42,    43,    -1,    -1,    -1,    -1,    48,    49,    50,    -1,
      -1,    -1,    54,    -1,    35,    36,    37,    59,    60,    -1,
      -1,    42,    43,    -1,    -1,    -1,    -1,    48,    49,    50,
      -1,    -1,    74,    54,    76,    77,    -1,    -1,    59,    60,
      -1,    -1,    -1,    -1,    86,    87,    -1,    -1,    -1,    91,
      -1,    -1,    -1,    74,    -1,    76,    77,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    86,    87,    -1,    -1,    -1,
      91,    -1,    -1,   115,    -1,    96,     5,    -1,     7,    -1,
     122,    -1,    11,   125,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    20,    -1,    -1,   115,    -1,    -1,     5,    -1,     7,
      -1,   122,    -1,    11,   125,    -1,    35,    -1,    37,    -1,
      -1,    -1,    20,    42,    43,    -1,    -1,    -1,    -1,    48,
      49,    50,    -1,    -1,    -1,    54,    -1,    35,    36,    37,
      59,    60,    -1,    -1,    42,    43,    -1,    -1,    -1,    -1,
      48,    49,    50,    -1,    -1,    74,    54,    76,    77,    -1,
      -1,    59,    60,    -1,    -1,    -1,    -1,    86,    87,    -1,
      -1,    -1,    91,    -1,    -1,    -1,    74,    -1,    76,    77,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    86,    87,
      -1,    -1,    -1,    91,    -1,    -1,   115,    -1,     5,   118,
       7,    -1,    -1,   122,    11,    -1,   125,    -1,    -1,    -1,
      -1,    -1,    -1,    20,    -1,    -1,    -1,   115,    -1,    -1,
      -1,    -1,    -1,    -1,   122,    -1,    -1,   125,    35,    -1,
      37,    -1,    -1,    -1,    -1,    42,    43,    -1,    -1,    -1,
      -1,    48,    49,    50,    -1,    -1,    -1,    54,    -1,    -1,
      -1,    -1,    59,    60,    -1,    -1,     5,    -1,     7,    -1,
      -1,    -1,    11,    -1,    -1,    -1,    -1,    74,    75,    76,
      77,    20,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    86,
      87,    -1,    -1,    -1,    91,    -1,    35,    -1,    37,    -1,
      -1,    -1,    -1,    42,    43,    -1,    -1,    -1,    -1,    48,
      49,    50,    -1,    -1,    -1,    54,    -1,    56,   115,    -1,
      59,    60,    -1,    -1,     5,   122,     7,    -1,   125,    -1,
      11,    -1,    -1,    -1,    -1,    74,    -1,    76,    77,    20,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    86,    87,    -1,
      -1,    -1,    91,    -1,    35,    36,    37,    -1,    -1,    -1,
      -1,    42,    43,    -1,    -1,    -1,    -1,    48,    49,    50,
      -1,    -1,    -1,    54,    -1,    -1,   115,    -1,    59,    60,
      -1,    -1,     5,   122,     7,    -1,   125,    -1,    11,    -1,
      -1,    -1,    -1,    74,    -1,    76,    77,    20,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    86,    87,    -1,    -1,    -1,
      91,    -1,    35,    -1,    37,    -1,    -1,    -1,    -1,    42,
      43,    -1,    -1,    -1,    -1,    48,    49,    50,    -1,    -1,
      -1,    54,    -1,    56,   115,    -1,    59,    60,    -1,    -1,
       5,   122,     7,    -1,   125,    -1,    11,    -1,    -1,    -1,
      -1,    74,    -1,    76,    77,    20,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    86,    87,    -1,    -1,    -1,    91,    -1,
      35,    -1,    37,    -1,    -1,    -1,    -1,    42,    43,    -1,
      -1,    -1,    -1,    48,    49,    50,    -1,    -1,    -1,    54,
      -1,    -1,   115,    -1,    59,    60,    -1,    -1,    -1,   122,
      -1,    -1,   125,    -1,    -1,    -1,    -1,    -1,    -1,    74,
      -1,    76,    77,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    86,    87,    -1,    -1,    -1,    91,    -1,    -1,     5,
      -1,     7,    -1,    -1,    -1,    11,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    20,    -1,    -1,    -1,    -1,    -1,
     115,    -1,    -1,   118,    -1,    -1,    -1,   122,    -1,    35,
     125,    37,    -1,    -1,    -1,    -1,    42,    43,    -1,    -1,
      -1,    -1,    48,    49,    50,    -1,    -1,    -1,    54,    -1,
      -1,    -1,    -1,    59,    60,    -1,    -1,    -1,    -1,     5,
      -1,     7,    -1,    -1,    -1,    11,    -1,    -1,    74,    -1,
      76,    77,    -1,    -1,    20,    -1,    -1,    -1,    -1,    -1,
      86,    87,    -1,    -1,    -1,    91,    -1,    -1,    -1,    35,
      -1,    37,    -1,    -1,    -1,    -1,    42,    43,    -1,    -1,
      -1,    -1,    48,    49,    50,    -1,    -1,    -1,    54,   115,
      -1,    -1,   118,    59,    60,    -1,   122,    -1,    -1,   125,
      27,    28,    29,    30,    31,    32,    33,    -1,    74,    -1,
      76,    77,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      86,    87,    -1,    -1,    -1,    91,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    27,    28,
      29,    30,    31,    32,    33,    -1,    -1,    -1,    -1,   115,
      -1,    -1,    -1,    -1,    81,    -1,   122,    -1,    -1,   125,
      -1,    88,    89,    90,    -1,    -1,    -1,    -1,    95,    -1,
      97,    98,    99,   100,    -1,   102,   103,   104,   105,   106,
     107,    -1,   109,   110,   111,   112,    -1,    -1,    -1,    78,
      79,    -1,    81,    -1,    -1,    -1,    -1,    -1,   125,    88,
      89,    90,    -1,    -1,    -1,    -1,    95,    96,    97,    98,
      99,   100,    -1,   102,   103,   104,   105,   106,   107,    -1,
     109,   110,   111,   112,    27,    28,    29,    30,    31,    32,
      33,    -1,    -1,    -1,    -1,   124,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    27,    28,    29,    30,
      31,    32,    33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    81,    -1,
      -1,    -1,    -1,    -1,    -1,    88,    89,    90,    -1,    -1,
      -1,    -1,    95,    -1,    97,    98,    99,   100,    -1,   102,
     103,   104,   105,   106,   107,    -1,   109,   110,   111,   112,
      81,    28,    29,    30,    31,    32,    33,    88,    89,    90,
      -1,   124,    -1,    -1,    95,    -1,    97,    98,    99,   100,
      -1,   102,   103,   104,   105,   106,   107,    -1,   109,   110,
     111,   112,    27,    28,    29,    30,    31,    32,    33,    -1,
      -1,    -1,    -1,   124,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    81,    -1,    -1,    -1,    -1,    -1,
      -1,    88,    89,    90,    27,    28,    29,    30,    31,    32,
      33,    98,    99,   100,    -1,   102,   103,   104,   105,   106,
     107,    -1,   109,   110,   111,   112,    81,    -1,    -1,    -1,
      -1,    -1,    -1,    88,    89,    90,    -1,    -1,    -1,    -1,
      95,    -1,    97,    98,    99,   100,    -1,   102,   103,   104,
     105,   106,   107,    -1,   109,   110,   111,   112,    81,    -1,
      -1,    -1,    -1,    -1,    -1,    88,    89,    90,    -1,   124,
      -1,    -1,    95,    -1,    97,    98,    99,   100,    -1,   102,
     103,   104,   105,   106,   107,    -1,   109,   110,   111,   112,
      27,    28,    29,    30,    31,    32,    33,   120,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    27,    28,    29,
      30,    31,    32,    33,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    81,    -1,    -1,    -1,    -1,    -1,
      -1,    88,    89,    90,    -1,    -1,    -1,    -1,    95,    -1,
      97,    98,    99,   100,    -1,   102,   103,   104,   105,   106,
     107,    81,   109,   110,   111,   112,    -1,    -1,    88,    89,
      90,   118,    -1,    -1,    -1,    95,    -1,    97,    98,    99,
     100,    -1,   102,   103,   104,   105,   106,   107,    -1,   109,
     110,   111,   112,    -1,    -1,    -1,    -1,    -1,   118,    27,
      28,    29,    30,    31,    32,    33,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    27,    28,    29,    30,
      31,    32,    33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    81,    -1,    -1,    -1,    -1,    -1,    -1,
      88,    89,    90,    -1,    -1,    -1,    -1,    95,    -1,    97,
      98,    99,   100,    -1,   102,   103,   104,   105,   106,   107,
      81,   109,   110,   111,   112,    -1,    -1,    88,    89,    90,
     118,    -1,    -1,    -1,    95,    -1,    97,    98,    99,   100,
      -1,   102,   103,   104,   105,   106,   107,    -1,   109,   110,
     111,   112,    -1,    -1,    -1,    -1,    -1,   118,    27,    28,
      29,    30,    31,    32,    33,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    27,    28,    29,    30,    31,
      32,    33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    81,    -1,    -1,    -1,    -1,    -1,    -1,    88,
      89,    90,    -1,    -1,    -1,    -1,    95,    -1,    97,    98,
      99,   100,    -1,   102,   103,   104,   105,   106,   107,    81,
     109,   110,   111,   112,    -1,    -1,    88,    89,    90,   118,
      -1,    -1,    -1,    95,    -1,    97,    98,    99,   100,    -1,
     102,   103,   104,   105,   106,   107,    -1,   109,   110,   111,
     112,    -1,    -1,    -1,    -1,    -1,   118,    27,    28,    29,
      30,    31,    32,    33,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    27,    28,    29,    30,    31,    32,
      33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    81,    -1,    -1,    -1,    -1,    -1,    -1,    88,    89,
      90,    -1,    -1,    -1,    -1,    95,    -1,    97,    98,    99,
     100,    -1,   102,   103,   104,   105,   106,   107,    81,   109,
     110,   111,   112,    -1,    -1,    88,    89,    90,   118,    -1,
      -1,    -1,    95,    -1,    97,    98,    99,   100,    -1,   102,
     103,   104,   105,   106,   107,    -1,   109,   110,   111,   112,
      -1,    -1,    -1,    -1,    -1,   118,    27,    28,    29,    30,
      31,    32,    33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    27,    28,    29,    30,    31,    32,    33,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      81,    -1,    -1,    -1,    -1,    -1,    -1,    88,    89,    90,
      -1,    -1,    -1,    -1,    95,    -1,    97,    98,    99,   100,
      -1,   102,   103,   104,   105,   106,   107,    81,   109,   110,
     111,   112,    -1,    -1,    88,    89,    90,   118,    -1,    -1,
      -1,    95,    -1,    97,    98,    99,   100,    -1,   102,   103,
     104,   105,   106,   107,    -1,   109,   110,   111,   112,    -1,
      -1,    -1,    -1,    -1,   118,    27,    28,    29,    30,    31,
      32,    33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    27,    28,    29,    30,    31,    32,    33,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    81,
      -1,    -1,    -1,    -1,    -1,    -1,    88,    89,    90,    -1,
      -1,    -1,    -1,    95,    -1,    97,    98,    99,   100,    -1,
     102,   103,   104,   105,   106,   107,    81,   109,   110,   111,
     112,    -1,    -1,    88,    89,    90,   118,    -1,    -1,    -1,
      95,    -1,    97,    98,    99,   100,    -1,   102,   103,   104,
     105,   106,   107,    -1,   109,   110,   111,   112,    -1,    -1,
      -1,    -1,    -1,   118,    27,    28,    29,    30,    31,    32,
      33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    27,    28,    29,    30,    31,    32,    33,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    81,    -1,
      -1,    -1,    -1,    -1,    -1,    88,    89,    90,    -1,    -1,
      -1,    -1,    95,    -1,    97,    98,    99,   100,    -1,   102,
     103,   104,   105,   106,   107,    81,   109,   110,   111,   112,
      -1,    -1,    88,    89,    90,   118,    -1,    -1,    -1,    95,
      -1,    97,    98,    99,   100,    -1,   102,   103,   104,   105,
     106,   107,    -1,   109,   110,   111,   112,    -1,    -1,    -1,
      -1,    -1,   118,    27,    28,    29,    30,    31,    32,    33,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      27,    28,    29,    30,    31,    32,    33,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    81,    -1,    -1,
      -1,    -1,    -1,    -1,    88,    89,    90,    -1,    -1,    -1,
      -1,    95,    -1,    97,    98,    99,   100,    -1,   102,   103,
     104,   105,   106,   107,    81,   109,   110,   111,   112,    -1,
      -1,    88,    89,    90,   118,    -1,    -1,    -1,    95,    -1,
      97,    98,    99,   100,    -1,   102,   103,   104,   105,   106,
     107,    -1,   109,   110,   111,   112,    -1,    -1,    -1,    -1,
      -1,   118,    27,    28,    29,    30,    31,    32,    33,    -1,
      -1,    -1,     5,    -1,     7,     8,     9,    10,    11,    12,
      13,    14,    15,    16,    -1,    -1,    -1,    20,    21,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    34,    35,    -1,    37,    -1,    -1,    -1,    41,    -1,
      -1,    -1,    45,    46,    -1,    -1,    81,    -1,    -1,    -1,
      53,    -1,    -1,    88,    89,    90,    59,    -1,    -1,    -1,
      95,    -1,    97,    98,    99,   100,    -1,   102,   103,   104,
     105,   106,   107,    -1,   109,   110,   111,   112,    -1,    -1,
      -1,    -1,    85,   118,    -1,    -1,    -1,    -1,    -1,    92,
      93,    -1,    -1,    96,    27,    28,    29,    30,    31,    32,
      33,    -1,    -1,    -1,    -1,     5,    -1,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    16,    -1,    -1,    -1,
      20,    21,    -1,    -1,    -1,    -1,    27,    28,    29,    30,
      31,    32,    33,    -1,    34,    35,    36,    37,    -1,    -1,
      -1,    41,    -1,    -1,    -1,    45,    46,    -1,    81,    -1,
      -1,    -1,    -1,    53,    -1,    88,    89,    90,    -1,    59,
      -1,    -1,    95,    -1,    97,    98,    99,   100,    -1,   102,
     103,   104,   105,   106,   107,    -1,   109,   110,   111,   112,
      81,    -1,    -1,    -1,   117,    85,    -1,    88,    89,    90,
      -1,    -1,    92,    93,    95,    -1,    97,    98,    99,   100,
      -1,   102,   103,   104,   105,   106,   107,    -1,   109,   110,
     111,   112,    -1,    -1,    -1,    -1,   117,    27,    28,    29,
      30,    31,    32,    33,    -1,    -1,    -1,    -1,     5,    -1,
       7,     8,     9,    10,    11,    12,    13,    14,    15,    16,
      -1,    -1,    -1,    20,    21,    -1,    -1,    -1,    -1,    27,
      28,    29,    30,    31,    32,    33,    -1,    34,    35,    36,
      37,    -1,    -1,    -1,    41,    -1,    -1,    -1,    45,    46,
      -1,    81,    -1,    -1,    -1,    -1,    53,    -1,    88,    89,
      90,    -1,    59,    -1,    -1,    95,    -1,    97,    98,    99,
     100,    -1,   102,   103,   104,   105,   106,   107,    -1,   109,
     110,   111,   112,    81,    -1,    -1,    -1,   117,    85,    -1,
      88,    89,    90,    -1,    -1,    92,    93,    95,    -1,    97,
      98,    99,   100,    -1,   102,   103,   104,   105,   106,   107,
      -1,   109,   110,   111,   112,    -1,    -1,    -1,    -1,   117,
      27,    28,    29,    30,    31,    32,    33,    -1,    -1,    -1,
      -1,     5,    -1,     7,     8,     9,    10,    11,    12,    13,
      14,    15,    16,    -1,    -1,    -1,    20,    21,    -1,    -1,
      -1,    -1,    27,    28,    29,    30,    31,    32,    33,    -1,
      34,    35,    -1,    37,    -1,    -1,    -1,    41,    -1,    -1,
      -1,    45,    46,    -1,    81,    -1,    -1,    -1,    -1,    53,
      -1,    88,    89,    90,    -1,    59,    -1,    -1,    95,    -1,
      97,    98,    99,   100,    -1,   102,   103,   104,   105,   106,
     107,    -1,   109,   110,   111,   112,    81,    -1,    -1,    -1,
     117,    85,    -1,    88,    89,    90,    -1,    -1,    92,    93,
      95,    -1,    97,    98,    99,   100,    -1,   102,   103,   104,
     105,   106,   107,    -1,   109,   110,   111,   112,    -1,    -1,
      -1,    -1,   117,    27,    28,    29,    30,    31,    32,    33,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    27,    28,    29,    30,    31,
      32,    33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    81,    -1,    -1,
      -1,    -1,    -1,    -1,    88,    89,    90,    -1,    -1,    -1,
      -1,    95,    -1,    97,    98,    99,   100,    -1,   102,   103,
     104,   105,   106,   107,    -1,   109,   110,   111,   112,    81,
      -1,    -1,    -1,   117,    -1,    -1,    88,    89,    90,    -1,
      -1,    -1,    -1,    95,    -1,    97,    98,    99,   100,    -1,
     102,   103,   104,   105,   106,   107,    -1,   109,   110,   111,
     112,    -1,    -1,    -1,    -1,   117,    27,    28,    29,    30,
      31,    32,    33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    27,    28,
      29,    30,    31,    32,    33,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      81,    -1,    -1,    -1,    -1,    -1,    -1,    88,    89,    90,
      -1,    -1,    -1,    -1,    95,    -1,    97,    98,    99,   100,
      -1,   102,   103,   104,   105,   106,   107,    -1,   109,   110,
     111,   112,    81,    -1,    -1,    -1,   117,    -1,    -1,    88,
      89,    90,    -1,    -1,    -1,    -1,    95,    -1,    97,    98,
      99,   100,    -1,   102,   103,   104,   105,   106,   107,    -1,
     109,   110,   111,   112,    -1,    -1,    -1,    -1,   117,    27,
      28,    29,    30,    31,    32,    33,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    27,    28,    29,    30,    31,    32,    33,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    81,    -1,    -1,    -1,    -1,    -1,    -1,
      88,    89,    90,    -1,    -1,    -1,    -1,    95,    -1,    97,
      98,    99,   100,    -1,   102,   103,   104,   105,   106,   107,
      -1,   109,   110,   111,   112,    81,    -1,    -1,    -1,   117,
      -1,    -1,    88,    89,    90,    -1,    -1,    -1,    -1,    95,
      -1,    97,    98,    99,   100,    -1,   102,   103,   104,   105,
     106,   107,    -1,   109,   110,   111,   112,    -1,    -1,    -1,
       5,   117,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    -1,    -1,    -1,    20,    21,     5,    -1,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    16,    34,
      -1,    -1,    20,    21,    -1,    -1,    41,    -1,    -1,    -1,
      45,    46,    47,    -1,    -1,    -1,    34,    35,    53,    37,
      55,    -1,    57,    41,    -1,    -1,    -1,    45,    46,    -1,
      65,    -1,    -1,    -1,    -1,    53,    -1,    -1,    -1,    -1,
      -1,    59,    77,    -1,    -1,    -1,    -1,    -1,    83,    -1,
      85,    -1,    -1,    -1,    -1,    -1,    -1,    92,    93,    94,
      -1,    -1,    -1,    -1,    -1,    -1,    84,    85,    -1,    -1,
      -1,    -1,    -1,    -1,    92,    93,    27,    28,    29,    30,
      31,    32,    33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    27,    28,    29,    30,    31,    32,    33,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    78,    79,    -1,
      81,    -1,    -1,    -1,    -1,    -1,    -1,    88,    89,    90,
      -1,    -1,    -1,    -1,    95,    96,    97,    98,    99,   100,
      -1,   102,   103,   104,   105,   106,   107,    81,   109,   110,
     111,   112,    -1,    -1,    88,    89,    90,    -1,    -1,    -1,
      -1,    95,    96,    97,    98,    99,   100,    -1,   102,   103,
     104,   105,   106,   107,    -1,   109,   110,   111,   112,    27,
      28,    29,    30,    31,    32,    33,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,    29,    30,
      31,    32,    33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    81,    -1,    -1,    -1,    -1,    -1,    -1,
      88,    89,    90,    -1,    -1,    -1,    -1,    95,    -1,    97,
      98,    99,   100,    -1,   102,   103,   104,   105,   106,   107,
      81,   109,   110,   111,   112,    -1,    -1,    88,    89,    90,
      -1,    -1,    -1,    -1,    -1,    -1,    97,    98,    99,   100,
      -1,   102,   103,   104,   105,   106,   107,    -1,   109,   110,
     111,   112
};

/* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
   symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,     3,    65,   130,   131,   132,   133,   140,     5,     4,
       5,    44,     0,   132,   115,   134,     5,     4,     5,    17,
      18,    19,    23,    24,    25,    44,    65,    80,    88,    90,
      97,    98,    99,   107,   116,   125,   127,   128,   191,   194,
     195,   116,   116,   118,   135,   111,   116,   121,   123,   187,
     188,   116,   195,   195,   195,   195,   195,   195,   195,   192,
     193,   195,   195,   195,    27,    28,    29,    30,    31,    32,
      33,    81,    88,    89,    90,    95,    97,    98,    99,   100,
     102,   103,   104,   105,   106,   107,   109,   110,   111,   112,
       5,    46,   117,   156,   157,     5,     8,     9,    10,   117,
     136,   137,   189,     5,     7,    11,    12,    13,    14,    15,
      16,    20,    21,    34,    41,    45,    46,    47,    53,    55,
      57,    77,    83,    85,    92,    93,    94,   138,   139,   140,
     141,   142,   143,   147,   148,   151,   152,   153,   158,   165,
     166,   189,   190,     4,   183,   195,     5,   194,   195,   187,
     188,   195,   117,   119,   126,   191,   195,   195,   195,   195,
     195,   195,   195,   195,   195,   195,   195,   195,   195,   195,
     195,   195,   195,   195,   195,   195,   195,   195,   195,   195,
     195,   195,   120,     5,   117,   119,    12,    15,    11,    12,
      15,    12,   118,   117,   119,     5,    20,   123,   187,     5,
      26,   115,   164,     5,   115,   116,   144,   161,   185,   191,
     194,    15,    15,     5,   186,     5,     7,    11,    20,    35,
      37,    42,    43,    48,    49,    50,    54,    59,    60,    74,
      76,    77,    86,    87,    91,   115,   122,   170,   174,   175,
     176,   177,   185,   194,     5,   116,     5,   194,     5,    15,
     154,   155,   187,   154,   187,   170,   174,     5,    20,   146,
     187,     5,    35,    37,    59,    85,   141,   142,   143,   151,
     153,   158,   165,   167,   168,   169,     6,   138,   186,   187,
       5,   164,   186,   187,     5,   117,   119,   116,   187,   188,
      78,    79,    96,   124,   117,   193,    96,   195,   120,   157,
      15,   118,   137,     5,   195,     5,   116,   118,   187,     5,
       4,     5,   116,     5,   187,   188,     4,     5,    80,   116,
      66,    67,    68,    69,    70,    71,    72,    73,   145,   161,
     185,   185,   120,   119,   118,   116,   118,   185,   186,   187,
     186,    36,    96,   174,   184,   116,   195,     5,   116,   116,
     116,   174,   116,   116,   184,     5,   195,   195,   116,   195,
       5,    82,   110,   116,   118,   174,    33,   120,   118,   116,
     183,   120,   120,   154,   187,   118,   119,   154,   118,   154,
     116,   118,     5,   116,   118,    96,   167,   116,   116,     5,
      84,   168,   118,   186,   187,   186,   118,   120,     5,   186,
     195,   195,   195,   195,   195,   195,   195,   187,   117,   121,
     159,   160,   183,   116,     5,   117,   121,   162,   163,   183,
     116,   187,   187,   188,   183,   119,   185,   120,   120,   195,
     186,   117,   183,   120,   118,   186,   118,     5,    36,   174,
     195,   118,   118,   195,   195,   195,   178,   179,   185,   195,
      75,   118,   120,   118,   195,   118,   174,    39,    40,   172,
     173,   195,   161,   195,   161,   195,   159,   117,   195,   195,
     118,   154,   155,   118,   118,   136,     8,    11,    20,    21,
      22,   149,   150,   184,   116,   118,   136,   149,   174,     5,
      36,   195,   178,   118,   118,   187,   118,   118,   195,   187,
     118,   120,   117,   124,   124,   124,   118,     5,   110,   117,
     119,   117,   159,   118,     5,   117,   119,   117,   117,   159,
     116,   117,   145,   120,   195,   195,   118,   118,   117,   195,
     118,   184,   117,   117,   117,   117,   118,   119,   120,   117,
     195,   117,   195,   195,    41,   117,   119,   171,   195,   118,
     195,   118,   117,   118,   118,   118,   117,    20,   186,   187,
     186,   187,   186,   186,   186,   150,   184,    56,   136,   149,
     174,   117,   174,    58,   167,   117,   118,   118,   118,   118,
     195,   116,   118,   160,   118,   117,   116,   163,   118,   117,
     159,   117,   195,   118,   118,   118,   118,    36,   174,    52,
     180,   181,   182,   183,   180,   180,   195,   179,   195,   174,
     118,   174,   173,   118,   118,   118,   118,   186,   118,   187,
     186,   118,     5,   186,   118,   187,   118,   118,    56,   117,
     174,    56,   118,    58,    36,   168,   195,   118,   117,   195,
     118,   195,   118,   117,   118,    38,    96,    51,   181,   182,
      51,    96,    51,   182,    51,   182,   118,   149,   174,   118,
     118,   118,   187,   118,   118,   118,    56,   149,   174,    38,
     118,   117,   117,   118,   174,   118,   174,    51,   118,   174,
      51,    51,   178,   174,    56,   118,   149,   174,   174,    58,
     168,   178,   117,    56,   174,    56,    58,   117,   174,    56,
     168
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
#line 2976 "y.tab.c"
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


#line 343 "yaccs/verilog.yacc"


