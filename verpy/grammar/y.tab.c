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
#define YYLAST   4784

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  129
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  67
/* YYNRULES -- Number of rules.  */
#define YYNRULES  317
/* YYNRULES -- Number of states.  */
#define YYNSTATES  696

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
     464,   468,   474,   481,   488,   496,   505,   513,   517,   519,
     522,   528,   533,   538,   541,   544,   547,   551,   553,   559,
     562,   567,   570,   573,   578,   582,   585,   589,   593,   596,
     598,   602,   608,   612,   614,   616,   618,   620,   622,   624,
     626,   628,   634,   642,   652,   655,   658,   661,   666,   668,
     670,   674,   676,   679,   682,   684,   688,   691,   694,   700,
     704,   709,   715,   720,   726,   732,   740,   744,   748,   752,
     757,   761,   767,   770,   774,   778,   783,   789,   796,   804,
     811,   818,   826,   833,   841,   845,   849,   852,   854,   856,
     858,   861,   863,   869,   879,   885,   891,   895,   897,   901,
     904,   906,   910,   914,   918,   922,   926,   928,   931,   933,
     935,   938,   942,   946,   949,   951,   953,   957,   959,   965,
     971,   977,   981,   983,   985,   987,   990,   993,   996,   999,
    1002,  1005,  1009,  1011,  1013,  1015,  1017,  1019,  1022,  1025,
    1027,  1029,  1031,  1033,  1035,  1039,  1043,  1045,  1048,  1050,
    1054,  1058,  1063,  1068,  1075,  1077,  1079,  1081,  1083,  1085,
    1087,  1092,  1094,  1096,  1098,  1100,  1102,  1104,  1107,  1111,
    1115,  1118,  1124,  1128,  1132,  1136,  1140,  1144,  1148,  1152,
    1156,  1160,  1164,  1168,  1172,  1176,  1180,  1184,  1188,  1192,
    1196,  1200,  1204,  1208,  1212,  1216,  1220,  1224,  1229,  1233,
    1235,  1238,  1241,  1244,  1247,  1250,  1253,  1256
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
     183,   117,   118,    -1,     5,     5,   116,   159,   117,   118,
      -1,     5,     5,   116,   183,   117,   118,    -1,     5,   164,
       5,   116,   159,   117,   118,    -1,     5,   164,     5,   187,
     116,   159,   117,   118,    -1,     5,     5,   187,   116,   159,
     117,   118,    -1,   159,   119,   160,    -1,   160,    -1,   121,
     110,    -1,   121,     5,   116,   195,   117,    -1,   121,     5,
     116,   117,    -1,   115,   116,   183,   117,    -1,   115,     4,
      -1,   115,     5,    -1,   115,    80,    -1,   162,   119,   163,
      -1,   163,    -1,   121,     5,   116,   195,   117,    -1,   121,
       5,    -1,   115,   116,   183,   117,    -1,   115,     4,    -1,
     115,     5,    -1,   115,   116,   162,   117,    -1,   115,   116,
     117,    -1,    34,   174,    -1,    34,   170,   174,    -1,    83,
     167,    84,    -1,   167,   168,    -1,   168,    -1,    35,   167,
      36,    -1,    35,    96,     5,   167,    36,    -1,    85,     5,
     118,    -1,   142,    -1,   143,    -1,   151,    -1,   153,    -1,
     158,    -1,   169,    -1,   165,    -1,   141,    -1,    37,   116,
     195,   117,   168,    -1,    37,   116,   195,   117,   168,    38,
     168,    -1,    59,   116,   178,   118,   195,   118,   178,   117,
     168,    -1,   122,   110,    -1,   122,    82,    -1,   122,     5,
      -1,   122,   116,   172,   117,    -1,    41,    -1,   119,    -1,
     172,   171,   173,    -1,   173,    -1,    39,   195,    -1,    40,
     195,    -1,   195,    -1,    35,   184,    36,    -1,    35,    36,
      -1,    54,   174,    -1,    35,    96,     5,   184,    36,    -1,
      74,   184,    75,    -1,   185,   120,   195,   118,    -1,   185,
     120,   161,   195,   118,    -1,   185,    33,   195,   118,    -1,
     185,    33,   161,   195,   118,    -1,    37,   116,   195,   117,
     174,    -1,    37,   116,   195,   117,   174,    38,   174,    -1,
      42,   195,   118,    -1,    20,   186,   118,    -1,    11,   186,
     118,    -1,    11,   187,   186,   118,    -1,    87,   195,   118,
      -1,    86,   195,   120,   195,   118,    -1,   170,   118,    -1,
      43,     5,   118,    -1,    76,     5,   118,    -1,     5,   116,
     117,   118,    -1,     5,   116,   183,   117,   118,    -1,    48,
     116,   195,   117,   180,    51,    -1,    48,   116,   195,   117,
     180,   182,    51,    -1,    48,   116,   195,   117,   182,    51,
      -1,    49,   116,   195,   117,   180,    51,    -1,    49,   116,
     195,   117,   180,   182,    51,    -1,    50,   116,   195,   117,
     180,    51,    -1,    50,   116,   195,   117,   180,   182,    51,
      -1,   115,   195,   118,    -1,   115,   195,   174,    -1,     5,
     118,    -1,   175,    -1,   176,    -1,   177,    -1,   194,   118,
      -1,    77,    -1,     7,   185,   120,   195,   118,    -1,    59,
     116,   178,   118,   195,   118,   178,   117,   174,    -1,    91,
     116,   195,   117,   174,    -1,    60,   116,   195,   117,   174,
      -1,   178,   119,   179,    -1,   179,    -1,   185,   120,   195,
      -1,   180,   181,    -1,   181,    -1,   183,    96,   174,    -1,
     183,    96,   118,    -1,    52,    96,   174,    -1,    52,    96,
     118,    -1,   183,   119,   195,    -1,   195,    -1,   184,   174,
      -1,   174,    -1,     5,    -1,     5,   187,    -1,     5,   188,
     187,    -1,     5,   188,   188,    -1,     5,   188,    -1,   194,
      -1,   191,    -1,     5,   119,   186,    -1,     5,    -1,   123,
     195,    96,   195,   124,    -1,   123,   195,    78,   195,   124,
      -1,   123,   195,    79,   195,   124,    -1,   123,   195,   124,
      -1,     8,    -1,     9,    -1,    10,    -1,     9,    11,    -1,
       8,    12,    -1,     9,    12,    -1,    10,    12,    -1,     8,
      15,    -1,     9,    15,    -1,     9,    11,    15,    -1,    11,
      -1,    12,    -1,    15,    -1,    20,    -1,    21,    -1,    11,
      15,    -1,    12,    15,    -1,    85,    -1,    92,    -1,    93,
      -1,    13,    -1,    14,    -1,   125,   192,   126,    -1,   192,
     119,   193,    -1,   193,    -1,   195,   191,    -1,   195,    -1,
       5,   121,   194,    -1,     5,   121,     5,    -1,     5,   121,
       5,   187,    -1,     5,   121,     5,   188,    -1,     5,   121,
       5,   116,   195,   117,    -1,     5,    -1,   194,    -1,     4,
      -1,    80,    -1,    44,    -1,    65,    -1,    65,   116,   195,
     117,    -1,    17,    -1,    18,    -1,    19,    -1,    23,    -1,
      24,    -1,    25,    -1,     5,   187,    -1,     5,   188,   187,
      -1,     5,   188,   188,    -1,     5,   188,    -1,   195,    95,
     195,    96,   195,    -1,   195,   106,   195,    -1,   195,   110,
     195,    -1,   195,   107,   195,    -1,   195,   111,   195,    -1,
     195,   112,   195,    -1,   195,    98,   195,    -1,   195,    97,
     195,    -1,   195,    99,   195,    -1,   195,   104,   195,    -1,
     195,   105,   195,    -1,   195,    81,   195,    -1,   195,    27,
     195,    -1,   195,    28,   195,    -1,   195,    88,   195,    -1,
     195,    89,   195,    -1,   195,    90,   195,    -1,   195,    30,
     195,    -1,   195,    29,   195,    -1,   195,    31,   195,    -1,
     195,   109,   195,    -1,   195,    32,   195,    -1,   195,    33,
     195,    -1,   195,   103,   195,    -1,   195,   102,   195,    -1,
     195,   100,   195,    -1,     5,   116,   183,   117,    -1,   116,
     195,   117,    -1,   191,    -1,   107,   195,    -1,    97,   195,
      -1,    99,   195,    -1,    98,   195,    -1,    88,   195,    -1,
      90,   195,    -1,   127,   195,    -1,   128,   195,    -1
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
     153,   154,   155,   156,   157,   158,   159,   167,   167,   168,
     168,   168,   170,   170,   170,   170,   171,   171,   172,   172,
     173,   173,   173,   173,   173,   176,   176,   179,   181,   181,
     184,   185,   186,   187,   188,   189,   190,   191,   192,   193,
     194,   195,   196,   201,   206,   206,   206,   206,   207,   207,
     208,   208,   209,   209,   209,   214,   215,   216,   217,   218,
     219,   220,   221,   222,   223,   224,   225,   226,   227,   228,
     229,   230,   231,   232,   233,   234,   235,   236,   237,   238,
     239,   240,   241,   242,   243,   244,   245,   246,   247,   248,
     249,   250,   251,   254,   255,   256,   257,   257,   258,   259,
     259,   260,   260,   261,   261,   263,   263,   264,   264,   267,
     267,   267,   267,   267,   267,   267,   269,   269,   271,   271,
     271,   272,   274,   274,   274,   274,   274,   274,   274,   274,
     274,   274,   276,   276,   276,   276,   276,   276,   276,   276,
     276,   276,   276,   276,   278,   279,   279,   280,   280,   283,
     284,   285,   286,   287,   290,   291,   292,   293,   294,   295,
     296,   297,   297,   297,   297,   297,   297,   298,   299,   300,
     301,   302,   303,   304,   305,   306,   307,   308,   309,   310,
     311,   312,   313,   314,   315,   316,   317,   318,   319,   320,
     321,   322,   323,   324,   325,   326,   327,   328,   329,   330,
     331,   332,   333,   334,   335,   336,   337,   338
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
     158,   158,   158,   158,   158,   158,   158,   159,   159,   160,
     160,   160,   161,   161,   161,   161,   162,   162,   163,   163,
     164,   164,   164,   164,   164,   165,   165,   166,   167,   167,
     168,   168,   168,   168,   168,   168,   168,   168,   168,   168,
     168,   168,   168,   169,   170,   170,   170,   170,   171,   171,
     172,   172,   173,   173,   173,   174,   174,   174,   174,   174,
     174,   174,   174,   174,   174,   174,   174,   174,   174,   174,
     174,   174,   174,   174,   174,   174,   174,   174,   174,   174,
     174,   174,   174,   174,   174,   174,   174,   174,   174,   174,
     174,   174,   174,   175,   176,   177,   178,   178,   179,   180,
     180,   181,   181,   182,   182,   183,   183,   184,   184,   185,
     185,   185,   185,   185,   185,   185,   186,   186,   187,   187,
     187,   188,   189,   189,   189,   189,   189,   189,   189,   189,
     189,   189,   190,   190,   190,   190,   190,   190,   190,   190,
     190,   190,   190,   190,   191,   192,   192,   193,   193,   194,
     194,   194,   194,   194,   195,   195,   195,   195,   195,   195,
     195,   195,   195,   195,   195,   195,   195,   195,   195,   195,
     195,   195,   195,   195,   195,   195,   195,   195,   195,   195,
     195,   195,   195,   195,   195,   195,   195,   195,   195,   195,
     195,   195,   195,   195,   195,   195,   195,   195,   195,   195,
     195,   195,   195,   195,   195,   195,   195,   195
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
       3,     5,     6,     6,     7,     8,     7,     3,     1,     2,
       5,     4,     4,     2,     2,     2,     3,     1,     5,     2,
       4,     2,     2,     4,     3,     2,     3,     3,     2,     1,
       3,     5,     3,     1,     1,     1,     1,     1,     1,     1,
       1,     5,     7,     9,     2,     2,     2,     4,     1,     1,
       3,     1,     2,     2,     1,     3,     2,     2,     5,     3,
       4,     5,     4,     5,     5,     7,     3,     3,     3,     4,
       3,     5,     2,     3,     3,     4,     5,     6,     7,     6,
       6,     7,     6,     7,     3,     3,     2,     1,     1,     1,
       2,     1,     5,     9,     5,     5,     3,     1,     3,     2,
       1,     3,     3,     3,     3,     3,     1,     2,     1,     1,
       2,     3,     3,     2,     1,     1,     3,     1,     5,     5,
       5,     3,     1,     1,     1,     2,     2,     2,     2,     2,
       2,     3,     1,     1,     1,     1,     1,     2,     2,     1,
       1,     1,     1,     1,     3,     3,     1,     2,     1,     3,
       3,     4,     4,     6,     1,     1,     1,     1,     1,     1,
       4,     1,     1,     1,     1,     1,     1,     2,     3,     3,
       2,     5,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     4,     3,     1,
       2,     2,     2,     2,     2,     2,     2,     2
};

/* YYDEFACT[STATE-NAME] -- Default rule to reduce with in state
   STATE-NUM when YYTABLE doesn't specify something else to do.  Zero
   means the default is an error.  */
static const yytype_uint16 yydefact[] =
{
       0,     0,     0,     0,     2,     4,     5,     6,    10,     0,
      38,    37,     1,     3,     0,     0,     0,   266,   264,   271,
     272,   273,   274,   275,   276,   268,   269,   267,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   309,   265,
      39,     0,     0,    11,    22,     0,     0,     0,     0,   277,
     280,     0,   314,   315,   311,   313,   312,   310,     0,     0,
     256,   258,   316,   317,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     9,     0,   105,    20,   232,   233,   234,     0,
       0,    15,     0,     0,     0,   242,   243,   252,   253,   244,
       0,   245,   246,     0,     0,     0,     0,     0,     0,     0,
       0,    35,     0,   249,   250,   251,    36,     0,    22,    34,
      31,    23,    24,    32,    33,    28,    29,    30,    25,    26,
      27,     0,     0,     0,     0,   216,   260,   259,     0,   278,
     279,     0,   308,     0,   254,   257,   293,   294,   299,   298,
     300,   302,   303,   292,   295,   296,   297,     0,   288,   287,
     289,   306,   305,   304,   290,   291,   282,   284,   301,   283,
     285,   286,     0,     0,     8,     0,   236,   239,   235,   237,
     240,   238,    13,     0,     0,    16,     0,     0,     0,     0,
       0,     0,     0,   219,     0,     0,     0,     0,     0,   225,
     224,   247,   248,   227,     0,   219,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   201,     0,     0,     0,     0,     0,     0,   135,   197,
     198,   199,     0,   224,     0,     0,     0,     0,     0,     0,
     102,     0,     0,     0,     0,    41,     0,    68,     0,    67,
       0,     0,     0,     0,   249,   150,   143,   144,   145,   146,
     147,   149,     0,   139,   148,     7,    21,     0,     0,   227,
       0,     0,     0,    40,   307,     0,     0,   261,   262,     0,
       0,     0,   231,   270,   255,     0,   107,     0,   104,   241,
      12,    14,    18,     0,    17,     0,   110,     0,     0,   131,
     132,     0,     0,   220,   223,   123,   124,   125,     0,    59,
      60,    61,    62,    63,    64,    65,    66,     0,     0,     0,
       0,     0,     0,    43,     0,   196,     0,     0,     0,     0,
     166,     0,   218,     0,     0,     0,     0,     0,     0,     0,
     167,     0,     0,     0,     0,     0,     0,     0,     0,   156,
     155,   154,     0,   182,   136,     0,     0,   200,     0,     0,
       0,     0,     0,    94,     0,     0,    98,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   137,   138,
      42,     0,     0,     0,    44,     0,   227,     0,   215,     0,
       0,     0,     0,   281,   106,    19,     0,     0,     0,   118,
       0,     0,     0,   134,     0,     0,   127,     0,     0,     0,
     221,   222,     0,     0,     0,     0,     0,     0,   226,     0,
       0,     0,   178,     0,   177,     0,   165,   217,     0,   176,
     183,     0,     0,     0,     0,   207,     0,     0,   169,   184,
       0,   180,     0,   194,   195,     0,     0,     0,   161,   164,
       0,     0,     0,     0,     0,     0,   103,    95,     0,   101,
      96,    99,     0,     0,     0,     0,     0,     0,     0,    82,
       0,     0,     0,     0,     0,     0,     0,   140,     0,     0,
     142,    46,     0,    51,    52,     0,     0,    48,     0,   263,
     229,   230,   228,   108,     0,   119,     0,     0,     0,     0,
      53,   129,   133,     0,   130,     0,     0,     0,   122,     0,
       0,     0,     0,    54,   185,     0,     0,   179,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   162,
     163,   158,   157,   159,     0,     0,   172,     0,   170,   111,
     100,    97,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    81,     0,    70,     0,     0,     0,     0,     0,    78,
       0,     0,     0,    47,    45,    50,     0,     0,   112,   117,
     113,     0,     0,   126,   109,     0,     0,    58,     0,    57,
      55,   186,   202,   168,   174,     0,     0,   210,     0,     0,
       0,     0,     0,   206,   208,   205,   181,   204,   160,   173,
     171,     0,     0,    88,     0,     0,    83,   227,     0,    92,
       0,    84,    85,    69,     0,     0,    72,     0,    77,   141,
     151,     0,    49,   121,     0,   116,     0,   114,     0,    56,
       0,     0,   187,   209,     0,   189,     0,   190,     0,   192,
       0,     0,     0,     0,    91,    89,    90,     0,    86,    93,
       0,    71,     0,     0,     0,     0,   120,   128,   115,   175,
     214,   213,   188,   212,   211,   191,   193,     0,     0,    73,
      87,     0,     0,     0,    79,   152,     0,     0,    74,     0,
      75,    80,     0,   203,    76,   153
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,     3,     4,     5,     6,    15,    44,   100,   101,   127,
     128,     7,   265,   266,   267,   206,   327,   258,   133,   134,
     478,   479,   268,   136,   269,   249,   250,    93,    94,   270,
     408,   409,   207,   415,   416,   202,   271,   140,   272,   273,
     274,   254,   544,   457,   458,   342,   239,   240,   241,   444,
     445,   596,   597,   598,   599,   343,   242,   214,   313,   314,
     141,   142,    38,    59,    60,    39,   145
};

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
#define YYPACT_NINF -504
static const yytype_int16 yypact[] =
{
      49,    18,    51,    29,    49,  -504,  -504,  -504,   -73,    65,
    1468,  -504,  -504,  -504,    -5,    40,   -25,  -504,   -31,  -504,
    -504,  -504,  -504,  -504,  -504,  -504,    67,  -504,  1468,  1468,
    1468,  1468,  1468,  1468,  1468,  1468,  1468,  1468,  -504,  -504,
    4645,     5,    38,  -504,  4448,    95,  1468,   189,  1468,  -504,
      44,  1468,  -504,  -504,  -504,  -504,  -504,  -504,  3685,   -37,
    -504,   314,  -504,  -504,  1468,  1468,  1468,  1468,  1468,  1468,
    1468,  1468,  1468,  1468,  1468,  1468,  1468,  1468,  1468,  1468,
    1468,  1468,  1468,  1468,  1468,  1468,  1468,  1468,  1468,  1468,
      88,   220,  -504,   125,  -504,  -504,   194,   228,   238,   135,
     128,  -504,    16,    34,    13,   261,   264,  -504,  -504,  -504,
     254,  -504,  -504,  2286,   168,   283,    23,    27,  2286,    20,
     287,  -504,  4092,  -504,  -504,  -504,  -504,   289,  4448,  -504,
    -504,  -504,  -504,  -504,  -504,  -504,  -504,  -504,  -504,  -504,
    -504,    28,    39,   304,   129,  4645,    -8,  -504,  2325,  -504,
    -504,  3722,  -504,  1468,  -504,  -504,  4672,   360,   100,   100,
     100,   414,   414,  -504,  2529,  2529,  2529,  4559,  2411,  2529,
    1177,   538,   538,   538,   414,   414,   480,   480,   100,  -504,
    -504,  -504,  1468,   199,  -504,    17,  -504,  -504,   311,  -504,
    -504,  -504,  -504,   215,   221,  -504,   325,  1468,   333,    75,
     349,    45,   357,   131,    72,   151,    19,    10,   260,  -504,
    -504,  -504,  -504,   245,   257,   -43,    10,    28,   254,  1701,
     263,  1468,   377,   267,   268,   269,  2286,   270,   271,  2286,
     401,  -504,  1468,  1468,   291,  1468,    54,  1793,  -504,  -504,
    -504,  -504,   -17,   290,  1468,   294,   302,   307,    27,    96,
    -504,   405,   116,   405,   310,  -504,   142,  -504,   425,  -504,
     152,  3652,   316,   320,   433,  -504,  -504,  -504,  -504,  -504,
    -504,  -504,  4465,  -504,  -504,  -504,  -504,   324,   254,   -65,
     254,   149,   441,  -504,  -504,  1468,  1468,  -504,  -504,  1468,
    1468,  1468,  -504,  -504,  -504,  1468,  4645,  1468,  -504,  -504,
    -504,  -504,  -504,  4532,   326,   735,  -504,   331,   446,  -504,
    -504,   803,    69,  -504,    44,  -504,  -504,  -504,  1468,  -504,
    -504,  -504,  -504,  -504,  -504,  -504,  -504,   334,    10,   335,
     336,  1468,   254,  -504,  1232,  -504,   337,   342,   254,   343,
    -504,   457,  -504,  1814,  1468,  2588,   345,  1468,  1468,  1468,
    -504,    10,  1468,  1905,   350,  2561,  2680,  1468,  1571,  -504,
    -504,  -504,   943,  -504,  -504,  1328,  1328,  -504,   155,  1468,
    1468,   144,   405,  -504,   405,   248,  -504,   250,   221,  1680,
     159,   221,  1680,   468,  3846,  1468,    10,   356,  -504,  -504,
    -504,   -51,   359,   361,  -504,  1468,   -65,   162,  4645,  3813,
    2357,  2443,  2475,  4645,  4645,  -504,   365,    22,   166,  -504,
     174,   354,   366,  -504,   481,   183,  -504,   186,   -12,   369,
    -504,  -504,   193,   151,   368,  1468,  1468,  2707,  -504,   372,
     197,  1468,  -504,   375,  -504,  2286,  -504,  -504,  3845,  -504,
    -504,  3936,  3968,  4059,   253,  -504,   380,  4091,  -504,  -504,
    1468,  -504,  4182,  -504,  -504,  1468,  1468,     0,  -504,  4645,
    1468,  2799,  1468,  2826,   379,  2918,  4645,  -504,   255,  -504,
    -504,  -504,   198,    25,    28,   254,   254,   254,  1680,  -504,
    1963,   221,  1680,   201,  1680,   443,  4092,  -504,  4214,   259,
    -504,  -504,   384,  -504,  -504,  2945,   385,  -504,  1468,  -504,
    -504,  -504,  -504,  -504,   389,  -504,   394,   354,   395,   205,
    -504,   391,  -504,   393,  -504,   398,   208,   354,  -504,   400,
    1468,  3037,  3064,  -504,  -504,   404,  3156,  -504,  2021,  2286,
    1350,  1468,  1468,  1468,    10,  1468,  2286,  3183,  2286,  4645,
    4645,  -504,  -504,  -504,   943,  3275,  -504,  3302,  -504,  -504,
    -504,  -504,   409,   254,    48,   254,   410,   514,    77,   411,
     412,  -504,  2079,  -504,   212,  1680,   475,   415,   476,  -504,
    3969,  4092,  1468,  -504,  -504,  -504,  3394,  1446,  -504,  -504,
    -504,   418,  1468,  -504,  -504,   419,   217,  -504,  3421,  -504,
    -504,  -504,  -504,  -504,   500,   448,  1073,  -504,   491,   -35,
    1097,  1210,  3513,  -504,  4645,  -504,  -504,  -504,  -504,  -504,
    -504,  1680,   427,  -504,   428,   429,   292,   -65,   431,   295,
     434,  -504,  -504,  -504,   435,   498,  -504,  1680,  -504,  -504,
     517,  3540,  -504,  -504,  4305,  -504,  4337,  -504,   438,  -504,
    2286,  2137,  -504,  -504,   506,  -504,  2226,  -504,   507,  -504,
     508,    10,  1680,   504,  -504,  -504,  -504,   444,   301,  -504,
    1680,  -504,  1680,   505,  4092,    10,  -504,  -504,  -504,  -504,
    -504,  -504,  -504,  -504,  -504,  -504,  -504,   241,   516,  -504,
    -504,  1680,   519,   515,  -504,  -504,   244,  2286,  -504,   520,
    -504,  -504,  4092,  -504,  -504,  -504
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -504,  -504,  -504,   574,  -504,  -504,  -504,  -361,   388,   451,
    -504,   -18,   -10,     9,    35,  -504,   160,  -504,  -504,  -504,
    -370,  -465,    37,  -504,    47,  -106,   210,  -504,   402,    50,
    -349,    78,  -192,  -504,    73,   453,    52,  -504,  -259,  -263,
    -504,   483,  -504,  -504,    56,    12,  -504,  -504,  -504,  -378,
      64,  -408,  -503,  -364,   -40,  -222,  -100,   -77,   -15,   -13,
     -41,  -504,   -30,  -504,   450,   -47,   649
};

/* YYTABLE[YYPACT[STATE-NUM]].  What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule which
   number is the opposite.  If zero, do what YYDEFACT says.
   If YYTABLE_NINF, syntax error.  */
#define YYTABLE_NINF -180
static const yytype_int16 yytable[] =
{
     147,   102,   384,    49,   208,    50,   144,   353,   489,   389,
      90,   252,   484,   561,   328,   203,   365,   472,   203,   561,
     483,   195,    90,     8,   203,   256,   129,   504,   247,    12,
     213,   155,   247,   213,   130,   149,   196,   150,   248,   199,
     257,   541,    14,    95,   279,   553,    96,    97,    98,   309,
     310,    91,     1,   131,   332,     9,    10,   210,   197,   359,
     200,   646,   509,    91,   277,   281,   243,   491,   246,   516,
      16,   243,   197,   334,   209,   335,   315,   316,    47,   132,
      48,   135,   153,   209,   285,    46,    45,   198,   209,   154,
      47,   137,    48,   643,   138,    11,   139,   643,   643,   143,
     561,   251,   253,   366,   259,   515,   329,   330,   286,   407,
     129,    41,   565,    47,     2,    48,   336,   542,   130,   543,
     564,   389,    92,   600,   601,   238,   278,   282,   204,   205,
     255,   287,   505,   288,   204,    35,   360,   131,    35,   197,
     337,   339,   371,   197,    35,   375,   197,   377,   197,   201,
     197,   197,   317,   102,   201,    99,    42,   480,    43,   210,
     210,   311,   197,   132,   361,   135,   613,    48,   586,   210,
     362,   197,   243,   460,   462,   137,   209,   209,   138,   243,
     139,    71,   243,    51,   307,   418,   209,   561,   318,   209,
     243,   305,   197,   306,   146,   619,   209,   561,   197,   209,
     197,   391,   338,   393,   368,   397,   186,   209,   182,   187,
      87,    88,    89,   528,   373,   374,   561,   319,   320,   321,
     322,   323,   324,   325,   326,   183,    95,   570,   424,    96,
      97,    98,   644,   372,   376,   374,   648,   650,   350,   188,
     189,   652,   184,   190,   185,   193,   284,   194,   285,   364,
     191,   446,    47,   192,    48,   428,   562,   662,   378,   213,
     379,   433,   467,   374,   392,   410,   468,   394,   381,   395,
     382,   417,   464,   677,   285,   481,   211,   482,   422,   212,
     497,   210,   498,   506,   244,   507,   446,   686,   245,   405,
     681,   508,   260,   285,   430,   275,   243,   419,   209,   420,
     512,   421,   513,   514,   210,   285,   243,   389,   630,   283,
     518,   243,   285,   209,   525,   552,   285,   194,   567,   297,
     194,   209,   581,   209,   507,   585,   299,   507,   209,   624,
     302,   194,   243,   300,   638,   243,   507,   102,   304,   210,
     102,    64,    65,    66,    67,    68,    69,    70,  -178,   209,
    -178,  -177,   209,  -177,   308,   437,   209,  -179,   687,  -179,
     534,   692,   312,   534,   332,   437,   470,   374,   471,   374,
     454,   533,   534,   551,   374,   333,   492,   572,   534,   344,
     331,   496,   346,   347,   348,   349,   351,   352,   243,    66,
      67,    68,    69,    70,   485,    71,   554,   556,   558,   559,
     560,   685,    72,    73,    74,   209,   354,   357,   367,    75,
     247,    76,    77,    78,    79,    47,    80,    81,    82,    83,
      84,    85,   369,    86,    87,    88,    89,   370,   363,   695,
     380,   243,   385,   243,   446,   243,   386,   243,   387,    35,
     102,    71,   390,    66,    67,    68,   396,   411,   209,   197,
     209,   412,   209,   423,   209,   425,   426,   431,   555,   557,
     432,   434,   435,   440,    82,    83,    84,    85,   449,    86,
      87,    88,    89,   486,   490,   407,   612,   493,   615,   494,
     618,   243,   243,   503,   510,   517,   511,   210,   520,   243,
     524,   243,   437,   527,   566,    71,   568,   549,   209,   209,
     535,   569,   573,   575,   209,   577,   209,   582,   209,    66,
      67,    68,   578,   580,   414,   243,   584,   587,   243,   617,
      84,    85,   591,    86,    87,    88,    89,   611,   616,   621,
     622,   626,   209,   627,   628,   209,   635,   637,   640,   614,
     437,   594,   645,   620,   641,   654,   655,   656,   605,   658,
     607,   446,   659,   660,   661,   664,   668,   672,   675,   676,
     679,    71,   680,   684,   243,   446,    65,    66,    67,    68,
      69,    70,   688,   691,   437,   690,   694,   625,    13,   276,
     243,   209,   301,   519,   469,   579,   583,   298,     0,    86,
      87,    88,    89,   243,   243,   280,   237,   209,   603,   243,
     608,     0,   657,   294,   210,   243,     0,     0,     0,     0,
     209,   209,     0,   243,     0,   243,   209,     0,   210,    71,
       0,   209,   209,   653,     0,     0,     0,     0,     0,     0,
     209,     0,   209,     0,   243,   209,     0,     0,     0,   663,
     243,     0,    82,    83,    84,    85,     0,    86,    87,    88,
      89,   209,   669,   671,     0,     0,     0,   209,   674,    40,
       0,     0,     0,     0,   678,     0,     0,     0,     0,     0,
       0,     0,   682,     0,   683,     0,     0,    52,    53,    54,
      55,    56,    57,    58,    61,    62,    63,     0,     0,     0,
       0,     0,     0,   689,     0,     0,     0,   148,     0,   693,
     151,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   156,   157,   158,   159,   160,   161,   162,
     163,   164,   165,   166,   167,   168,   169,   170,   171,   172,
     173,   174,   175,   176,   177,   178,   179,   180,   181,    17,
      18,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    19,    20,    21,     0,     0,     0,    22,    23,
      24,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    25,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      26,     0,    61,     0,     0,     0,     0,    17,    18,     0,
       0,     0,     0,     0,     0,    27,     0,     0,     0,     0,
      19,    20,    21,    28,     0,    29,    22,    23,    24,     0,
       0,   296,    30,    31,    32,     0,     0,     0,     0,     0,
       0,     0,    33,     0,     0,     0,   303,    25,     0,     0,
       0,    34,   406,     0,     0,     0,   407,     0,     0,     0,
      35,     0,    36,    37,     0,     0,     0,     0,    26,     0,
     345,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   355,   356,    27,   358,     0,     0,     0,     0,     0,
       0,    28,     0,    29,     0,     0,     0,     0,     0,     0,
      30,    31,    32,     0,     0,     0,     0,     0,     0,     0,
      33,     0,     0,     0,     0,     0,     0,     0,     0,    34,
     413,     0,     0,     0,   414,     0,     0,     0,    35,     0,
      36,    37,     0,     0,   398,   399,     0,     0,   400,   401,
     402,     0,     0,     0,   403,     0,   404,    17,    18,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      19,    20,    21,     0,     0,     0,    22,    23,    24,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     427,     0,   455,   456,     0,     0,     0,    25,     0,     0,
       0,     0,     0,   438,     0,     0,   441,   442,   443,     0,
       0,   447,     0,     0,     0,     0,   452,     0,    26,     0,
       0,   459,     0,     0,   461,   463,     0,     0,   465,   466,
       0,     0,     0,    27,     0,     0,     0,     0,     0,     0,
       0,    28,     0,    29,   488,     0,     0,     0,     0,     0,
      30,    31,    32,     0,   495,     0,     0,     0,     0,     0,
      33,     0,     0,     0,     0,     0,     0,     0,     0,    34,
       0,     0,     0,     0,     0,     0,     0,     0,    35,     0,
      36,    37,     0,     0,   521,   522,     0,    17,    18,     0,
     526,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      19,    20,    21,     0,     0,     0,    22,    23,    24,   537,
       0,    17,    18,     0,   539,   540,     0,     0,     0,   545,
       0,   547,     0,     0,    19,    20,    21,    25,     0,     0,
      22,    23,    24,     0,   642,   595,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    26,     0,
       0,    25,     0,     0,     0,     0,     0,   576,   647,   595,
       0,     0,     0,    27,     0,     0,     0,     0,     0,     0,
       0,    28,    26,    29,     0,     0,     0,     0,     0,   588,
      30,    31,    32,     0,     0,     0,     0,    27,     0,     0,
      33,     0,   602,     0,   604,    28,     0,    29,     0,    34,
       0,     0,     0,   459,    30,    31,    32,     0,    35,     0,
      36,    37,     0,     0,    33,    65,    66,    67,    68,    69,
      70,     0,     0,    34,    17,    18,     0,     0,     0,     0,
       0,   631,    35,     0,    36,    37,   634,    19,    20,    21,
       0,   636,     0,    22,    23,    24,    17,    18,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    19,
      20,    21,     0,     0,    25,    22,    23,    24,    71,     0,
       0,   649,   595,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    26,    25,    79,     0,    80,
      81,    82,    83,    84,    85,     0,    86,    87,    88,    89,
      27,     0,     0,     0,     0,     0,     0,    26,    28,     0,
      29,     0,     0,     0,     0,     0,     0,    30,    31,    32,
       0,     0,    27,     0,     0,     0,     0,    33,     0,     0,
      28,     0,    29,     0,     0,     0,    34,     0,     0,    30,
      31,    32,    17,    18,     0,    35,     0,    36,    37,    33,
       0,     0,     0,     0,     0,    19,    20,    21,    34,   429,
       0,    22,    23,    24,    17,    18,     0,    35,     0,    36,
      37,     0,     0,     0,     0,     0,     0,    19,    20,    21,
       0,     0,    25,    22,    23,    24,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    26,    25,     0,     0,     0,     0,     0,
       0,     0,   595,     0,     0,     0,     0,     0,    27,     0,
       0,     0,     0,     0,     0,    26,    28,     0,    29,     0,
       0,     0,     0,     0,     0,    30,    31,    32,     0,     0,
      27,     0,     0,     0,     0,    33,     0,     0,    28,     0,
      29,     0,     0,   204,    34,     0,     0,    30,    31,    32,
      17,    18,     0,    35,     0,    36,    37,    33,     0,     0,
       0,     0,     0,    19,    20,    21,    34,     0,     0,    22,
      23,    24,    17,    18,     0,    35,     0,    36,    37,     0,
       0,     0,     0,     0,     0,    19,    20,    21,     0,     0,
      25,    22,    23,    24,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    26,    25,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    27,     0,     0,     0,
       0,     0,     0,    26,    28,     0,    29,     0,     0,     0,
       0,     0,     0,    30,    31,    32,     0,     0,    27,     0,
       0,     0,     0,    33,     0,     0,    28,     0,    29,     0,
       0,     0,    34,   633,     0,    30,    31,    32,     0,     0,
       0,    35,     0,    36,    37,    33,   215,     0,   216,     0,
       0,     0,   217,     0,    34,     0,     0,     0,     0,     0,
       0,   218,     0,    35,     0,    36,    37,     0,    64,    65,
      66,    67,    68,    69,    70,     0,   219,     0,   220,     0,
       0,     0,     0,   221,   222,     0,     0,     0,     0,   223,
     224,   225,     0,     0,     0,   226,     0,     0,     0,     0,
     227,   228,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   229,     0,   230,   231,     0,
       0,     0,    71,     0,     0,     0,     0,   232,   233,    72,
      73,    74,   234,     0,     0,     0,    75,     0,    76,    77,
      78,    79,     0,    80,    81,    82,    83,    84,    85,     0,
      86,    87,    88,    89,     0,   215,   235,   216,   473,   453,
       0,   474,     0,   236,     0,     0,    35,     0,     0,     0,
     475,   476,   477,     0,     0,     0,   215,     0,   216,     0,
       0,     0,   217,     0,     0,   219,     0,   220,     0,     0,
       0,   218,   221,   222,     0,     0,     0,     0,   223,   224,
     225,     0,     0,     0,   226,     0,   219,   340,   220,   227,
     228,     0,     0,   221,   222,     0,     0,     0,     0,   223,
     224,   225,     0,     0,   229,   226,   230,   231,     0,     0,
     227,   228,     0,     0,     0,     0,   232,   233,     0,     0,
       0,   234,     0,     0,     0,   229,     0,   230,   231,     0,
       0,     0,     0,     0,     0,     0,     0,   232,   233,     0,
       0,     0,   234,     0,     0,   235,     0,   341,   215,     0,
     216,     0,   236,     0,   217,    35,     0,     0,     0,     0,
       0,     0,     0,   218,     0,     0,   235,     0,     0,   215,
       0,   216,     0,   236,     0,   217,    35,     0,   219,     0,
     220,     0,     0,     0,   218,   221,   222,     0,     0,     0,
       0,   223,   224,   225,     0,     0,     0,   226,     0,   219,
     436,   220,   227,   228,     0,     0,   221,   222,     0,     0,
       0,     0,   223,   224,   225,     0,     0,   229,   226,   230,
     231,     0,     0,   227,   228,     0,     0,     0,     0,   232,
     233,     0,     0,     0,   234,     0,     0,     0,   229,     0,
     230,   231,     0,     0,     0,     0,     0,     0,     0,     0,
     232,   233,     0,     0,     0,   234,     0,     0,   235,     0,
     215,   363,   216,     0,     0,   236,   217,     0,    35,     0,
       0,     0,     0,     0,     0,   218,     0,     0,     0,   235,
       0,     0,     0,     0,     0,     0,   236,     0,     0,    35,
     219,     0,   220,     0,     0,     0,     0,   221,   222,     0,
       0,     0,     0,   223,   224,   225,     0,     0,     0,   226,
       0,     0,     0,     0,   227,   228,     0,     0,   215,     0,
     216,     0,     0,     0,   217,     0,     0,     0,     0,   229,
     448,   230,   231,   218,     0,     0,     0,     0,     0,     0,
       0,   232,   233,     0,     0,     0,   234,     0,   219,     0,
     220,     0,     0,     0,     0,   221,   222,     0,     0,     0,
       0,   223,   224,   225,     0,     0,     0,   226,     0,   563,
     235,     0,   227,   228,     0,     0,   215,   236,   216,     0,
      35,     0,   217,     0,     0,     0,     0,   229,     0,   230,
     231,   218,     0,     0,     0,     0,     0,     0,     0,   232,
     233,     0,     0,     0,   234,     0,   219,   593,   220,     0,
       0,     0,     0,   221,   222,     0,     0,     0,     0,   223,
     224,   225,     0,     0,     0,   226,     0,     0,   235,     0,
     227,   228,     0,     0,   215,   236,   216,     0,    35,     0,
     217,     0,     0,     0,     0,   229,     0,   230,   231,   218,
       0,     0,     0,     0,     0,     0,     0,   232,   233,     0,
       0,     0,   234,     0,   219,     0,   220,     0,     0,     0,
       0,   221,   222,     0,     0,     0,     0,   223,   224,   225,
       0,     0,     0,   226,     0,   623,   235,     0,   227,   228,
       0,     0,   215,   236,   216,     0,    35,     0,   217,     0,
       0,     0,     0,   229,     0,   230,   231,   218,     0,     0,
       0,     0,     0,     0,     0,   232,   233,     0,     0,     0,
     234,     0,   219,     0,   220,     0,     0,     0,     0,   221,
     222,     0,     0,     0,     0,   223,   224,   225,     0,     0,
       0,   226,     0,     0,   235,     0,   227,   228,     0,     0,
       0,   236,     0,     0,    35,     0,     0,     0,     0,     0,
       0,   229,     0,   230,   231,     0,     0,     0,     0,     0,
       0,     0,     0,   232,   233,     0,     0,     0,   234,     0,
       0,   215,     0,   216,     0,     0,     0,   217,     0,     0,
       0,     0,     0,     0,     0,     0,   218,     0,     0,     0,
       0,     0,   235,     0,     0,   670,     0,     0,     0,   236,
       0,   219,    35,   220,     0,     0,     0,     0,   221,   222,
       0,     0,     0,     0,   223,   224,   225,     0,     0,     0,
     226,     0,     0,     0,     0,   227,   228,     0,     0,     0,
       0,   215,     0,   216,     0,     0,     0,   217,     0,     0,
     229,     0,   230,   231,     0,     0,   218,     0,     0,     0,
       0,     0,   232,   233,     0,     0,     0,   234,     0,     0,
       0,   219,     0,   220,     0,     0,     0,     0,   221,   222,
       0,     0,     0,     0,   223,   224,   225,     0,     0,     0,
     226,   235,     0,     0,   673,   227,   228,     0,   236,     0,
       0,    35,    64,    65,    66,    67,    68,    69,    70,     0,
     229,     0,   230,   231,     0,     0,     0,     0,     0,     0,
       0,     0,   232,   233,     0,     0,     0,   234,     0,     0,
       0,     0,     0,     0,    64,    65,    66,    67,    68,    69,
      70,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   235,     0,   289,   290,     0,    71,     0,   236,     0,
       0,    35,     0,    72,    73,    74,     0,     0,     0,     0,
      75,   291,    76,    77,    78,    79,     0,    80,    81,    82,
      83,    84,    85,     0,    86,    87,    88,    89,    71,    65,
      66,    67,    68,    69,    70,    72,    73,    74,     0,   292,
       0,     0,    75,     0,    76,    77,    78,    79,     0,    80,
      81,    82,    83,    84,    85,     0,    86,    87,    88,    89,
      64,    65,    66,    67,    68,    69,    70,     0,     0,     0,
       0,   500,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    71,     0,     0,     0,     0,     0,     0,    72,
      73,    74,    64,    65,    66,    67,    68,    69,    70,    77,
      78,    79,     0,    80,    81,    82,    83,    84,    85,     0,
      86,    87,    88,    89,    71,     0,     0,     0,     0,     0,
       0,    72,    73,    74,     0,     0,     0,     0,    75,     0,
      76,    77,    78,    79,     0,    80,    81,    82,    83,    84,
      85,     0,    86,    87,    88,    89,    71,    65,    66,    67,
      68,    69,    70,    72,    73,    74,     0,   501,     0,     0,
      75,     0,    76,    77,    78,    79,     0,    80,    81,    82,
      83,    84,    85,     0,    86,    87,    88,    89,    64,    65,
      66,    67,    68,    69,    70,     0,     0,     0,     0,   502,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      71,     0,     0,     0,     0,    64,    65,    66,    67,    68,
      69,    70,     0,     0,     0,     0,     0,     0,    78,    79,
       0,    80,    81,    82,    83,    84,    85,     0,    86,    87,
      88,    89,    71,     0,     0,     0,     0,     0,     0,    72,
      73,    74,     0,     0,     0,     0,    75,     0,    76,    77,
      78,    79,     0,    80,    81,    82,    83,    84,    85,    71,
      86,    87,    88,    89,     0,     0,    72,    73,    74,     0,
       0,   450,     0,    75,     0,    76,    77,    78,    79,     0,
      80,    81,    82,    83,    84,    85,     0,    86,    87,    88,
      89,     0,     0,     0,     0,     0,   439,    64,    65,    66,
      67,    68,    69,    70,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    64,    65,    66,    67,    68,    69,
      70,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    71,     0,     0,     0,     0,     0,     0,    72,    73,
      74,     0,     0,     0,     0,    75,     0,    76,    77,    78,
      79,     0,    80,    81,    82,    83,    84,    85,    71,    86,
      87,    88,    89,     0,     0,    72,    73,    74,   451,     0,
       0,     0,    75,     0,    76,    77,    78,    79,     0,    80,
      81,    82,    83,    84,    85,     0,    86,    87,    88,    89,
       0,     0,     0,     0,     0,   523,    64,    65,    66,    67,
      68,    69,    70,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    64,    65,    66,    67,    68,    69,    70,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      71,     0,     0,     0,     0,     0,     0,    72,    73,    74,
       0,     0,     0,     0,    75,     0,    76,    77,    78,    79,
       0,    80,    81,    82,    83,    84,    85,    71,    86,    87,
      88,    89,     0,     0,    72,    73,    74,   546,     0,     0,
       0,    75,     0,    76,    77,    78,    79,     0,    80,    81,
      82,    83,    84,    85,     0,    86,    87,    88,    89,     0,
       0,     0,     0,     0,   548,    64,    65,    66,    67,    68,
      69,    70,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    64,    65,    66,    67,    68,    69,    70,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    71,
       0,     0,     0,     0,     0,     0,    72,    73,    74,     0,
       0,     0,     0,    75,     0,    76,    77,    78,    79,     0,
      80,    81,    82,    83,    84,    85,    71,    86,    87,    88,
      89,     0,     0,    72,    73,    74,   550,     0,     0,     0,
      75,     0,    76,    77,    78,    79,     0,    80,    81,    82,
      83,    84,    85,     0,    86,    87,    88,    89,     0,     0,
       0,     0,     0,   574,    64,    65,    66,    67,    68,    69,
      70,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    64,    65,    66,    67,    68,    69,    70,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    71,     0,
       0,     0,     0,     0,     0,    72,    73,    74,     0,     0,
       0,     0,    75,     0,    76,    77,    78,    79,     0,    80,
      81,    82,    83,    84,    85,    71,    86,    87,    88,    89,
       0,     0,    72,    73,    74,   589,     0,     0,     0,    75,
       0,    76,    77,    78,    79,     0,    80,    81,    82,    83,
      84,    85,     0,    86,    87,    88,    89,     0,     0,     0,
       0,     0,   590,    64,    65,    66,    67,    68,    69,    70,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      64,    65,    66,    67,    68,    69,    70,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    71,     0,     0,
       0,     0,     0,     0,    72,    73,    74,     0,     0,     0,
       0,    75,     0,    76,    77,    78,    79,     0,    80,    81,
      82,    83,    84,    85,    71,    86,    87,    88,    89,     0,
       0,    72,    73,    74,   592,     0,     0,     0,    75,     0,
      76,    77,    78,    79,     0,    80,    81,    82,    83,    84,
      85,     0,    86,    87,    88,    89,     0,     0,     0,     0,
       0,   606,    64,    65,    66,    67,    68,    69,    70,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    64,
      65,    66,    67,    68,    69,    70,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    71,     0,     0,     0,
       0,     0,     0,    72,    73,    74,     0,     0,     0,     0,
      75,     0,    76,    77,    78,    79,     0,    80,    81,    82,
      83,    84,    85,    71,    86,    87,    88,    89,     0,     0,
      72,    73,    74,   609,     0,     0,     0,    75,     0,    76,
      77,    78,    79,     0,    80,    81,    82,    83,    84,    85,
       0,    86,    87,    88,    89,     0,     0,     0,     0,     0,
     610,    64,    65,    66,    67,    68,    69,    70,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    64,    65,
      66,    67,    68,    69,    70,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    71,     0,     0,     0,     0,
       0,     0,    72,    73,    74,     0,     0,     0,     0,    75,
       0,    76,    77,    78,    79,     0,    80,    81,    82,    83,
      84,    85,    71,    86,    87,    88,    89,     0,     0,    72,
      73,    74,   632,     0,     0,     0,    75,     0,    76,    77,
      78,    79,     0,    80,    81,    82,    83,    84,    85,     0,
      86,    87,    88,    89,     0,     0,     0,     0,     0,   639,
      64,    65,    66,    67,    68,    69,    70,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    64,    65,    66,
      67,    68,    69,    70,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    71,     0,     0,     0,     0,     0,
       0,    72,    73,    74,     0,     0,     0,     0,    75,     0,
      76,    77,    78,    79,     0,    80,    81,    82,    83,    84,
      85,    71,    86,    87,    88,    89,     0,     0,    72,    73,
      74,   651,     0,     0,     0,    75,     0,    76,    77,    78,
      79,     0,    80,    81,    82,    83,    84,    85,     0,    86,
      87,    88,    89,     0,     0,     0,     0,   103,   665,   104,
      96,    97,    98,   105,   106,   107,   108,   109,   110,     0,
       0,     0,   111,   112,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   113,   261,     0,   262,
       0,     0,     0,   114,     0,     0,     0,   115,   116,     0,
       0,     0,     0,     0,     0,   118,     0,     0,     0,     0,
       0,   263,    64,    65,    66,    67,    68,    69,    70,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   264,     0,     0,
       0,     0,     0,     0,   124,   125,     0,     0,   383,    64,
      65,    66,    67,    68,    69,    70,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    71,     0,     0,     0,
       0,     0,     0,    72,    73,    74,     0,     0,     0,     0,
      75,     0,    76,    77,    78,    79,     0,    80,    81,    82,
      83,    84,    85,     0,    86,    87,    88,    89,     0,     0,
       0,     0,   152,    71,     0,     0,     0,     0,     0,     0,
      72,    73,    74,     0,     0,     0,     0,    75,     0,    76,
      77,    78,    79,     0,    80,    81,    82,    83,    84,    85,
       0,    86,    87,    88,    89,     0,     0,     0,     0,   293,
      64,    65,    66,    67,    68,    69,    70,     0,     0,     0,
       0,   103,     0,   104,    96,    97,    98,   105,   106,   107,
     108,   109,   110,     0,     0,     0,   111,   112,     0,     0,
       0,     0,    64,    65,    66,    67,    68,    69,    70,     0,
     113,   261,   487,   262,     0,     0,     0,   114,     0,     0,
       0,   115,   116,     0,    71,     0,     0,     0,     0,   118,
       0,    72,    73,    74,     0,   263,     0,     0,    75,     0,
      76,    77,    78,    79,     0,    80,    81,    82,    83,    84,
      85,     0,    86,    87,    88,    89,    71,     0,     0,     0,
     499,   264,     0,    72,    73,    74,     0,     0,   124,   125,
      75,     0,    76,    77,    78,    79,     0,    80,    81,    82,
      83,    84,    85,     0,    86,    87,    88,    89,     0,     0,
       0,     0,   529,    64,    65,    66,    67,    68,    69,    70,
       0,     0,     0,     0,   103,     0,   104,    96,    97,    98,
     105,   106,   107,   108,   109,   110,     0,     0,     0,   111,
     112,     0,     0,     0,     0,    64,    65,    66,    67,    68,
      69,    70,     0,   113,   261,   629,   262,     0,     0,     0,
     114,     0,     0,     0,   115,   116,     0,    71,     0,     0,
       0,     0,   118,     0,    72,    73,    74,     0,   263,     0,
       0,    75,     0,    76,    77,    78,    79,     0,    80,    81,
      82,    83,    84,    85,     0,    86,    87,    88,    89,    71,
       0,     0,     0,   530,   264,     0,    72,    73,    74,     0,
       0,   124,   125,    75,     0,    76,    77,    78,    79,     0,
      80,    81,    82,    83,    84,    85,     0,    86,    87,    88,
      89,     0,     0,     0,     0,   531,    64,    65,    66,    67,
      68,    69,    70,     0,     0,     0,     0,   103,     0,   104,
      96,    97,    98,   105,   106,   107,   108,   109,   110,     0,
       0,     0,   111,   112,     0,     0,     0,     0,    64,    65,
      66,    67,    68,    69,    70,     0,   113,   261,     0,   262,
       0,     0,     0,   114,     0,     0,     0,   115,   116,     0,
      71,     0,     0,     0,     0,   118,     0,    72,    73,    74,
       0,   263,     0,     0,    75,     0,    76,    77,    78,    79,
       0,    80,    81,    82,    83,    84,    85,     0,    86,    87,
      88,    89,    71,     0,     0,     0,   532,   264,     0,    72,
      73,    74,     0,     0,   124,   125,    75,     0,    76,    77,
      78,    79,     0,    80,    81,    82,    83,    84,    85,     0,
      86,    87,    88,    89,     0,     0,     0,     0,   536,    64,
      65,    66,    67,    68,    69,    70,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    64,    65,    66,    67,    68,    69,    70,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    71,     0,     0,     0,     0,     0,     0,
      72,    73,    74,     0,     0,     0,     0,    75,     0,    76,
      77,    78,    79,     0,    80,    81,    82,    83,    84,    85,
       0,    86,    87,    88,    89,    71,     0,     0,     0,   538,
       0,     0,    72,    73,    74,     0,     0,     0,     0,    75,
       0,    76,    77,    78,    79,     0,    80,    81,    82,    83,
      84,    85,     0,    86,    87,    88,    89,     0,     0,     0,
       0,   571,    64,    65,    66,    67,    68,    69,    70,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    64,    65,    66,    67,    68,    69,
      70,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    71,     0,     0,     0,
       0,     0,     0,    72,    73,    74,     0,     0,     0,     0,
      75,     0,    76,    77,    78,    79,     0,    80,    81,    82,
      83,    84,    85,     0,    86,    87,    88,    89,    71,     0,
       0,     0,   666,     0,     0,    72,    73,    74,     0,     0,
       0,     0,    75,     0,    76,    77,    78,    79,     0,    80,
      81,    82,    83,    84,    85,     0,    86,    87,    88,    89,
       0,     0,     0,   103,   667,   104,    96,    97,    98,   105,
     106,   107,   108,   109,   110,     0,     0,     0,   111,   112,
     103,     0,   104,    96,    97,    98,   105,   106,   107,   108,
     109,   110,   113,     0,     0,   111,   112,     0,     0,   114,
       0,     0,     0,   115,   116,   117,     0,     0,     0,   113,
     261,   118,   262,   119,     0,   120,   114,     0,     0,     0,
     115,   116,     0,     2,     0,     0,     0,     0,   118,     0,
       0,     0,     0,     0,   263,   121,     0,     0,     0,     0,
       0,   122,     0,   123,     0,     0,     0,     0,     0,     0,
     124,   125,   126,     0,     0,     0,     0,     0,     0,   388,
     264,     0,     0,     0,     0,     0,     0,   124,   125,    64,
      65,    66,    67,    68,    69,    70,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    64,    65,    66,    67,
      68,    69,    70,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     289,   290,     0,    71,     0,     0,     0,     0,     0,     0,
      72,    73,    74,     0,     0,     0,     0,    75,   291,    76,
      77,    78,    79,     0,    80,    81,    82,    83,    84,    85,
      71,    86,    87,    88,    89,     0,     0,    72,    73,    74,
       0,     0,     0,     0,    75,   295,    76,    77,    78,    79,
       0,    80,    81,    82,    83,    84,    85,     0,    86,    87,
      88,    89,    64,    65,    66,    67,    68,    69,    70,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      65,    66,    67,    68,    69,    70,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    71,     0,     0,     0,
       0,     0,     0,    72,    73,    74,     0,     0,     0,     0,
      75,     0,    76,    77,    78,    79,     0,    80,    81,    82,
      83,    84,    85,    71,    86,    87,    88,    89,     0,     0,
      72,    73,    74,     0,     0,     0,     0,     0,     0,    76,
      77,    78,    79,     0,    80,    81,    82,    83,    84,    85,
       0,    86,    87,    88,    89
};

static const yytype_int16 yycheck[] =
{
      47,    42,   261,    18,   104,    18,    46,   229,   386,   272,
       5,   117,   382,   478,   206,     5,    33,   378,     5,   484,
     381,     5,     5,     5,     5,     5,    44,     5,     5,     0,
       5,    61,     5,     5,    44,    50,    20,    50,    15,     5,
      20,    41,   115,     5,     5,    20,     8,     9,    10,     4,
       5,    46,     3,    44,   119,     4,     5,   104,   123,     5,
      26,    96,   411,    46,   141,   142,   113,   118,   115,   418,
       5,   118,   123,   116,   104,   118,     4,     5,   121,    44,
     123,    44,   119,   113,   119,   116,   111,   102,   118,   126,
     121,    44,   123,   596,    44,    44,    44,   600,   601,     4,
     565,   116,   117,   120,   119,   117,   206,   207,   116,   121,
     128,   116,   482,   121,    65,   123,   216,   117,   128,   119,
     481,   384,   117,   531,   532,   113,   141,   142,   115,   116,
     118,   146,   110,   146,   115,   125,    82,   128,   125,   123,
     217,   218,   248,   123,   125,   251,   123,   253,   123,   115,
     123,   123,    80,   194,   115,   117,   116,   379,   118,   206,
     207,   116,   123,   128,   110,   128,   118,   123,   517,   216,
     116,   123,   219,   365,   366,   128,   206,   207,   128,   226,
     128,    81,   229,   116,   199,   116,   216,   652,   116,   219,
     237,   116,   123,   118,     5,   118,   226,   662,   123,   229,
     123,   278,   217,   280,   244,   282,    12,   237,   120,    15,
     110,   111,   112,   435,   118,   119,   681,    66,    67,    68,
      69,    70,    71,    72,    73,     5,     5,   486,   328,     8,
       9,    10,   596,   248,   118,   119,   600,   601,   226,    11,
      12,   611,   117,    15,   119,   117,   117,   119,   119,   237,
      12,   351,   121,   118,   123,   332,   478,   627,   116,     5,
     118,   338,   118,   119,   279,   305,   372,   118,   116,   120,
     118,   311,   117,   651,   119,   116,    15,   118,   318,    15,
     118,   328,   120,   117,   116,   119,   386,   665,     5,   304,
     660,   117,     5,   119,   334,     6,   343,   312,   328,   314,
     117,   314,   119,   117,   351,   119,   353,   570,   571,     5,
     117,   358,   119,   343,   117,   117,   119,   119,   117,   120,
     119,   351,   117,   353,   119,   117,    15,   119,   358,   117,
       5,   119,   379,   118,   117,   382,   119,   378,     5,   386,
     381,    27,    28,    29,    30,    31,    32,    33,    56,   379,
      58,    56,   382,    58,     5,   343,   386,    56,   117,    58,
     119,   117,     5,   119,   119,   353,   118,   119,   118,   119,
     358,   118,   119,   118,   119,   118,   391,   118,   119,   116,
     120,   396,     5,   116,   116,   116,   116,   116,   435,    29,
      30,    31,    32,    33,   382,    81,   473,   474,   475,   476,
     477,   664,    88,    89,    90,   435,     5,   116,   118,    95,
       5,    97,    98,    99,   100,   121,   102,   103,   104,   105,
     106,   107,   120,   109,   110,   111,   112,   120,   118,   692,
       5,   478,   116,   480,   534,   482,   116,   484,     5,   125,
     481,    81,   118,    29,    30,    31,     5,   116,   478,   123,
     480,     5,   482,   119,   484,   120,   120,   120,   473,   474,
     118,   118,     5,   118,   104,   105,   106,   107,   118,   109,
     110,   111,   112,     5,   118,   121,   553,   118,   555,   118,
     557,   528,   529,   118,   118,   116,     5,   534,   120,   536,
     118,   538,   480,   118,   482,    81,   484,   118,   528,   529,
     120,    58,   118,   118,   534,   116,   536,   116,   538,    29,
      30,    31,   118,   118,   121,   562,   118,   117,   565,     5,
     106,   107,   118,   109,   110,   111,   112,   118,   118,   118,
     118,    56,   562,   118,    58,   565,   118,   118,    38,   554,
     528,   529,    51,   558,    96,   118,   118,   118,   536,   118,
     538,   651,   118,   118,    56,    38,   118,    51,    51,    51,
      56,    81,   118,    58,   611,   665,    28,    29,    30,    31,
      32,    33,    56,    58,   562,    56,    56,   565,     4,   128,
     627,   611,   194,   423,   374,   507,   513,   185,    -1,   109,
     110,   111,   112,   640,   641,   142,   113,   627,   534,   646,
     544,    -1,   617,   153,   651,   652,    -1,    -1,    -1,    -1,
     640,   641,    -1,   660,    -1,   662,   646,    -1,   665,    81,
      -1,   651,   652,   611,    -1,    -1,    -1,    -1,    -1,    -1,
     660,    -1,   662,    -1,   681,   665,    -1,    -1,    -1,   627,
     687,    -1,   104,   105,   106,   107,    -1,   109,   110,   111,
     112,   681,   640,   641,    -1,    -1,    -1,   687,   646,    10,
      -1,    -1,    -1,    -1,   652,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   660,    -1,   662,    -1,    -1,    28,    29,    30,
      31,    32,    33,    34,    35,    36,    37,    -1,    -1,    -1,
      -1,    -1,    -1,   681,    -1,    -1,    -1,    48,    -1,   687,
      51,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    64,    65,    66,    67,    68,    69,    70,
      71,    72,    73,    74,    75,    76,    77,    78,    79,    80,
      81,    82,    83,    84,    85,    86,    87,    88,    89,     4,
       5,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    17,    18,    19,    -1,    -1,    -1,    23,    24,
      25,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    44,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      65,    -1,   153,    -1,    -1,    -1,    -1,     4,     5,    -1,
      -1,    -1,    -1,    -1,    -1,    80,    -1,    -1,    -1,    -1,
      17,    18,    19,    88,    -1,    90,    23,    24,    25,    -1,
      -1,   182,    97,    98,    99,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   107,    -1,    -1,    -1,   197,    44,    -1,    -1,
      -1,   116,   117,    -1,    -1,    -1,   121,    -1,    -1,    -1,
     125,    -1,   127,   128,    -1,    -1,    -1,    -1,    65,    -1,
     221,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   232,   233,    80,   235,    -1,    -1,    -1,    -1,    -1,
      -1,    88,    -1,    90,    -1,    -1,    -1,    -1,    -1,    -1,
      97,    98,    99,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     107,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   116,
     117,    -1,    -1,    -1,   121,    -1,    -1,    -1,   125,    -1,
     127,   128,    -1,    -1,   285,   286,    -1,    -1,   289,   290,
     291,    -1,    -1,    -1,   295,    -1,   297,     4,     5,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      17,    18,    19,    -1,    -1,    -1,    23,    24,    25,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     331,    -1,    39,    40,    -1,    -1,    -1,    44,    -1,    -1,
      -1,    -1,    -1,   344,    -1,    -1,   347,   348,   349,    -1,
      -1,   352,    -1,    -1,    -1,    -1,   357,    -1,    65,    -1,
      -1,   362,    -1,    -1,   365,   366,    -1,    -1,   369,   370,
      -1,    -1,    -1,    80,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    88,    -1,    90,   385,    -1,    -1,    -1,    -1,    -1,
      97,    98,    99,    -1,   395,    -1,    -1,    -1,    -1,    -1,
     107,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   116,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   125,    -1,
     127,   128,    -1,    -1,   425,   426,    -1,     4,     5,    -1,
     431,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      17,    18,    19,    -1,    -1,    -1,    23,    24,    25,   450,
      -1,     4,     5,    -1,   455,   456,    -1,    -1,    -1,   460,
      -1,   462,    -1,    -1,    17,    18,    19,    44,    -1,    -1,
      23,    24,    25,    -1,    51,    52,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    65,    -1,
      -1,    44,    -1,    -1,    -1,    -1,    -1,   498,    51,    52,
      -1,    -1,    -1,    80,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    88,    65,    90,    -1,    -1,    -1,    -1,    -1,   520,
      97,    98,    99,    -1,    -1,    -1,    -1,    80,    -1,    -1,
     107,    -1,   533,    -1,   535,    88,    -1,    90,    -1,   116,
      -1,    -1,    -1,   544,    97,    98,    99,    -1,   125,    -1,
     127,   128,    -1,    -1,   107,    28,    29,    30,    31,    32,
      33,    -1,    -1,   116,     4,     5,    -1,    -1,    -1,    -1,
      -1,   572,   125,    -1,   127,   128,   577,    17,    18,    19,
      -1,   582,    -1,    23,    24,    25,     4,     5,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    17,
      18,    19,    -1,    -1,    44,    23,    24,    25,    81,    -1,
      -1,    51,    52,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    65,    44,   100,    -1,   102,
     103,   104,   105,   106,   107,    -1,   109,   110,   111,   112,
      80,    -1,    -1,    -1,    -1,    -1,    -1,    65,    88,    -1,
      90,    -1,    -1,    -1,    -1,    -1,    -1,    97,    98,    99,
      -1,    -1,    80,    -1,    -1,    -1,    -1,   107,    -1,    -1,
      88,    -1,    90,    -1,    -1,    -1,   116,    -1,    -1,    97,
      98,    99,     4,     5,    -1,   125,    -1,   127,   128,   107,
      -1,    -1,    -1,    -1,    -1,    17,    18,    19,   116,   117,
      -1,    23,    24,    25,     4,     5,    -1,   125,    -1,   127,
     128,    -1,    -1,    -1,    -1,    -1,    -1,    17,    18,    19,
      -1,    -1,    44,    23,    24,    25,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    65,    44,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    52,    -1,    -1,    -1,    -1,    -1,    80,    -1,
      -1,    -1,    -1,    -1,    -1,    65,    88,    -1,    90,    -1,
      -1,    -1,    -1,    -1,    -1,    97,    98,    99,    -1,    -1,
      80,    -1,    -1,    -1,    -1,   107,    -1,    -1,    88,    -1,
      90,    -1,    -1,   115,   116,    -1,    -1,    97,    98,    99,
       4,     5,    -1,   125,    -1,   127,   128,   107,    -1,    -1,
      -1,    -1,    -1,    17,    18,    19,   116,    -1,    -1,    23,
      24,    25,     4,     5,    -1,   125,    -1,   127,   128,    -1,
      -1,    -1,    -1,    -1,    -1,    17,    18,    19,    -1,    -1,
      44,    23,    24,    25,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    65,    44,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    80,    -1,    -1,    -1,
      -1,    -1,    -1,    65,    88,    -1,    90,    -1,    -1,    -1,
      -1,    -1,    -1,    97,    98,    99,    -1,    -1,    80,    -1,
      -1,    -1,    -1,   107,    -1,    -1,    88,    -1,    90,    -1,
      -1,    -1,   116,   117,    -1,    97,    98,    99,    -1,    -1,
      -1,   125,    -1,   127,   128,   107,     5,    -1,     7,    -1,
      -1,    -1,    11,    -1,   116,    -1,    -1,    -1,    -1,    -1,
      -1,    20,    -1,   125,    -1,   127,   128,    -1,    27,    28,
      29,    30,    31,    32,    33,    -1,    35,    -1,    37,    -1,
      -1,    -1,    -1,    42,    43,    -1,    -1,    -1,    -1,    48,
      49,    50,    -1,    -1,    -1,    54,    -1,    -1,    -1,    -1,
      59,    60,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    74,    -1,    76,    77,    -1,
      -1,    -1,    81,    -1,    -1,    -1,    -1,    86,    87,    88,
      89,    90,    91,    -1,    -1,    -1,    95,    -1,    97,    98,
      99,   100,    -1,   102,   103,   104,   105,   106,   107,    -1,
     109,   110,   111,   112,    -1,     5,   115,     7,     8,   118,
      -1,    11,    -1,   122,    -1,    -1,   125,    -1,    -1,    -1,
      20,    21,    22,    -1,    -1,    -1,     5,    -1,     7,    -1,
      -1,    -1,    11,    -1,    -1,    35,    -1,    37,    -1,    -1,
      -1,    20,    42,    43,    -1,    -1,    -1,    -1,    48,    49,
      50,    -1,    -1,    -1,    54,    -1,    35,    36,    37,    59,
      60,    -1,    -1,    42,    43,    -1,    -1,    -1,    -1,    48,
      49,    50,    -1,    -1,    74,    54,    76,    77,    -1,    -1,
      59,    60,    -1,    -1,    -1,    -1,    86,    87,    -1,    -1,
      -1,    91,    -1,    -1,    -1,    74,    -1,    76,    77,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    86,    87,    -1,
      -1,    -1,    91,    -1,    -1,   115,    -1,    96,     5,    -1,
       7,    -1,   122,    -1,    11,   125,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    20,    -1,    -1,   115,    -1,    -1,     5,
      -1,     7,    -1,   122,    -1,    11,   125,    -1,    35,    -1,
      37,    -1,    -1,    -1,    20,    42,    43,    -1,    -1,    -1,
      -1,    48,    49,    50,    -1,    -1,    -1,    54,    -1,    35,
      36,    37,    59,    60,    -1,    -1,    42,    43,    -1,    -1,
      -1,    -1,    48,    49,    50,    -1,    -1,    74,    54,    76,
      77,    -1,    -1,    59,    60,    -1,    -1,    -1,    -1,    86,
      87,    -1,    -1,    -1,    91,    -1,    -1,    -1,    74,    -1,
      76,    77,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      86,    87,    -1,    -1,    -1,    91,    -1,    -1,   115,    -1,
       5,   118,     7,    -1,    -1,   122,    11,    -1,   125,    -1,
      -1,    -1,    -1,    -1,    -1,    20,    -1,    -1,    -1,   115,
      -1,    -1,    -1,    -1,    -1,    -1,   122,    -1,    -1,   125,
      35,    -1,    37,    -1,    -1,    -1,    -1,    42,    43,    -1,
      -1,    -1,    -1,    48,    49,    50,    -1,    -1,    -1,    54,
      -1,    -1,    -1,    -1,    59,    60,    -1,    -1,     5,    -1,
       7,    -1,    -1,    -1,    11,    -1,    -1,    -1,    -1,    74,
      75,    76,    77,    20,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    86,    87,    -1,    -1,    -1,    91,    -1,    35,    -1,
      37,    -1,    -1,    -1,    -1,    42,    43,    -1,    -1,    -1,
      -1,    48,    49,    50,    -1,    -1,    -1,    54,    -1,    56,
     115,    -1,    59,    60,    -1,    -1,     5,   122,     7,    -1,
     125,    -1,    11,    -1,    -1,    -1,    -1,    74,    -1,    76,
      77,    20,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    86,
      87,    -1,    -1,    -1,    91,    -1,    35,    36,    37,    -1,
      -1,    -1,    -1,    42,    43,    -1,    -1,    -1,    -1,    48,
      49,    50,    -1,    -1,    -1,    54,    -1,    -1,   115,    -1,
      59,    60,    -1,    -1,     5,   122,     7,    -1,   125,    -1,
      11,    -1,    -1,    -1,    -1,    74,    -1,    76,    77,    20,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    86,    87,    -1,
      -1,    -1,    91,    -1,    35,    -1,    37,    -1,    -1,    -1,
      -1,    42,    43,    -1,    -1,    -1,    -1,    48,    49,    50,
      -1,    -1,    -1,    54,    -1,    56,   115,    -1,    59,    60,
      -1,    -1,     5,   122,     7,    -1,   125,    -1,    11,    -1,
      -1,    -1,    -1,    74,    -1,    76,    77,    20,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    86,    87,    -1,    -1,    -1,
      91,    -1,    35,    -1,    37,    -1,    -1,    -1,    -1,    42,
      43,    -1,    -1,    -1,    -1,    48,    49,    50,    -1,    -1,
      -1,    54,    -1,    -1,   115,    -1,    59,    60,    -1,    -1,
      -1,   122,    -1,    -1,   125,    -1,    -1,    -1,    -1,    -1,
      -1,    74,    -1,    76,    77,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    86,    87,    -1,    -1,    -1,    91,    -1,
      -1,     5,    -1,     7,    -1,    -1,    -1,    11,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    20,    -1,    -1,    -1,
      -1,    -1,   115,    -1,    -1,   118,    -1,    -1,    -1,   122,
      -1,    35,   125,    37,    -1,    -1,    -1,    -1,    42,    43,
      -1,    -1,    -1,    -1,    48,    49,    50,    -1,    -1,    -1,
      54,    -1,    -1,    -1,    -1,    59,    60,    -1,    -1,    -1,
      -1,     5,    -1,     7,    -1,    -1,    -1,    11,    -1,    -1,
      74,    -1,    76,    77,    -1,    -1,    20,    -1,    -1,    -1,
      -1,    -1,    86,    87,    -1,    -1,    -1,    91,    -1,    -1,
      -1,    35,    -1,    37,    -1,    -1,    -1,    -1,    42,    43,
      -1,    -1,    -1,    -1,    48,    49,    50,    -1,    -1,    -1,
      54,   115,    -1,    -1,   118,    59,    60,    -1,   122,    -1,
      -1,   125,    27,    28,    29,    30,    31,    32,    33,    -1,
      74,    -1,    76,    77,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    86,    87,    -1,    -1,    -1,    91,    -1,    -1,
      -1,    -1,    -1,    -1,    27,    28,    29,    30,    31,    32,
      33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   115,    -1,    78,    79,    -1,    81,    -1,   122,    -1,
      -1,   125,    -1,    88,    89,    90,    -1,    -1,    -1,    -1,
      95,    96,    97,    98,    99,   100,    -1,   102,   103,   104,
     105,   106,   107,    -1,   109,   110,   111,   112,    81,    28,
      29,    30,    31,    32,    33,    88,    89,    90,    -1,   124,
      -1,    -1,    95,    -1,    97,    98,    99,   100,    -1,   102,
     103,   104,   105,   106,   107,    -1,   109,   110,   111,   112,
      27,    28,    29,    30,    31,    32,    33,    -1,    -1,    -1,
      -1,   124,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    81,    -1,    -1,    -1,    -1,    -1,    -1,    88,
      89,    90,    27,    28,    29,    30,    31,    32,    33,    98,
      99,   100,    -1,   102,   103,   104,   105,   106,   107,    -1,
     109,   110,   111,   112,    81,    -1,    -1,    -1,    -1,    -1,
      -1,    88,    89,    90,    -1,    -1,    -1,    -1,    95,    -1,
      97,    98,    99,   100,    -1,   102,   103,   104,   105,   106,
     107,    -1,   109,   110,   111,   112,    81,    28,    29,    30,
      31,    32,    33,    88,    89,    90,    -1,   124,    -1,    -1,
      95,    -1,    97,    98,    99,   100,    -1,   102,   103,   104,
     105,   106,   107,    -1,   109,   110,   111,   112,    27,    28,
      29,    30,    31,    32,    33,    -1,    -1,    -1,    -1,   124,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      81,    -1,    -1,    -1,    -1,    27,    28,    29,    30,    31,
      32,    33,    -1,    -1,    -1,    -1,    -1,    -1,    99,   100,
      -1,   102,   103,   104,   105,   106,   107,    -1,   109,   110,
     111,   112,    81,    -1,    -1,    -1,    -1,    -1,    -1,    88,
      89,    90,    -1,    -1,    -1,    -1,    95,    -1,    97,    98,
      99,   100,    -1,   102,   103,   104,   105,   106,   107,    81,
     109,   110,   111,   112,    -1,    -1,    88,    89,    90,    -1,
      -1,   120,    -1,    95,    -1,    97,    98,    99,   100,    -1,
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
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    27,
      28,    29,    30,    31,    32,    33,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    81,    -1,    -1,    -1,
      -1,    -1,    -1,    88,    89,    90,    -1,    -1,    -1,    -1,
      95,    -1,    97,    98,    99,   100,    -1,   102,   103,   104,
     105,   106,   107,    81,   109,   110,   111,   112,    -1,    -1,
      88,    89,    90,   118,    -1,    -1,    -1,    95,    -1,    97,
      98,    99,   100,    -1,   102,   103,   104,   105,   106,   107,
      -1,   109,   110,   111,   112,    -1,    -1,    -1,    -1,    -1,
     118,    27,    28,    29,    30,    31,    32,    33,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    27,    28,
      29,    30,    31,    32,    33,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    81,    -1,    -1,    -1,    -1,
      -1,    -1,    88,    89,    90,    -1,    -1,    -1,    -1,    95,
      -1,    97,    98,    99,   100,    -1,   102,   103,   104,   105,
     106,   107,    81,   109,   110,   111,   112,    -1,    -1,    88,
      89,    90,   118,    -1,    -1,    -1,    95,    -1,    97,    98,
      99,   100,    -1,   102,   103,   104,   105,   106,   107,    -1,
     109,   110,   111,   112,    -1,    -1,    -1,    -1,    -1,   118,
      27,    28,    29,    30,    31,    32,    33,    -1,    -1,    -1,
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
     110,   111,   112,    -1,    -1,    -1,    -1,     5,   118,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    16,    -1,
      -1,    -1,    20,    21,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    34,    35,    -1,    37,
      -1,    -1,    -1,    41,    -1,    -1,    -1,    45,    46,    -1,
      -1,    -1,    -1,    -1,    -1,    53,    -1,    -1,    -1,    -1,
      -1,    59,    27,    28,    29,    30,    31,    32,    33,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    85,    -1,    -1,
      -1,    -1,    -1,    -1,    92,    93,    -1,    -1,    96,    27,
      28,    29,    30,    31,    32,    33,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    81,    -1,    -1,    -1,
      -1,    -1,    -1,    88,    89,    90,    -1,    -1,    -1,    -1,
      95,    -1,    97,    98,    99,   100,    -1,   102,   103,   104,
     105,   106,   107,    -1,   109,   110,   111,   112,    -1,    -1,
      -1,    -1,   117,    81,    -1,    -1,    -1,    -1,    -1,    -1,
      88,    89,    90,    -1,    -1,    -1,    -1,    95,    -1,    97,
      98,    99,   100,    -1,   102,   103,   104,   105,   106,   107,
      -1,   109,   110,   111,   112,    -1,    -1,    -1,    -1,   117,
      27,    28,    29,    30,    31,    32,    33,    -1,    -1,    -1,
      -1,     5,    -1,     7,     8,     9,    10,    11,    12,    13,
      14,    15,    16,    -1,    -1,    -1,    20,    21,    -1,    -1,
      -1,    -1,    27,    28,    29,    30,    31,    32,    33,    -1,
      34,    35,    36,    37,    -1,    -1,    -1,    41,    -1,    -1,
      -1,    45,    46,    -1,    81,    -1,    -1,    -1,    -1,    53,
      -1,    88,    89,    90,    -1,    59,    -1,    -1,    95,    -1,
      97,    98,    99,   100,    -1,   102,   103,   104,   105,   106,
     107,    -1,   109,   110,   111,   112,    81,    -1,    -1,    -1,
     117,    85,    -1,    88,    89,    90,    -1,    -1,    92,    93,
      95,    -1,    97,    98,    99,   100,    -1,   102,   103,   104,
     105,   106,   107,    -1,   109,   110,   111,   112,    -1,    -1,
      -1,    -1,   117,    27,    28,    29,    30,    31,    32,    33,
      -1,    -1,    -1,    -1,     5,    -1,     7,     8,     9,    10,
      11,    12,    13,    14,    15,    16,    -1,    -1,    -1,    20,
      21,    -1,    -1,    -1,    -1,    27,    28,    29,    30,    31,
      32,    33,    -1,    34,    35,    36,    37,    -1,    -1,    -1,
      41,    -1,    -1,    -1,    45,    46,    -1,    81,    -1,    -1,
      -1,    -1,    53,    -1,    88,    89,    90,    -1,    59,    -1,
      -1,    95,    -1,    97,    98,    99,   100,    -1,   102,   103,
     104,   105,   106,   107,    -1,   109,   110,   111,   112,    81,
      -1,    -1,    -1,   117,    85,    -1,    88,    89,    90,    -1,
      -1,    92,    93,    95,    -1,    97,    98,    99,   100,    -1,
     102,   103,   104,   105,   106,   107,    -1,   109,   110,   111,
     112,    -1,    -1,    -1,    -1,   117,    27,    28,    29,    30,
      31,    32,    33,    -1,    -1,    -1,    -1,     5,    -1,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    16,    -1,
      -1,    -1,    20,    21,    -1,    -1,    -1,    -1,    27,    28,
      29,    30,    31,    32,    33,    -1,    34,    35,    -1,    37,
      -1,    -1,    -1,    41,    -1,    -1,    -1,    45,    46,    -1,
      81,    -1,    -1,    -1,    -1,    53,    -1,    88,    89,    90,
      -1,    59,    -1,    -1,    95,    -1,    97,    98,    99,   100,
      -1,   102,   103,   104,   105,   106,   107,    -1,   109,   110,
     111,   112,    81,    -1,    -1,    -1,   117,    85,    -1,    88,
      89,    90,    -1,    -1,    92,    93,    95,    -1,    97,    98,
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
      -1,   117,    27,    28,    29,    30,    31,    32,    33,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    27,    28,    29,    30,    31,    32,
      33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    81,    -1,    -1,    -1,
      -1,    -1,    -1,    88,    89,    90,    -1,    -1,    -1,    -1,
      95,    -1,    97,    98,    99,   100,    -1,   102,   103,   104,
     105,   106,   107,    -1,   109,   110,   111,   112,    81,    -1,
      -1,    -1,   117,    -1,    -1,    88,    89,    90,    -1,    -1,
      -1,    -1,    95,    -1,    97,    98,    99,   100,    -1,   102,
     103,   104,   105,   106,   107,    -1,   109,   110,   111,   112,
      -1,    -1,    -1,     5,   117,     7,     8,     9,    10,    11,
      12,    13,    14,    15,    16,    -1,    -1,    -1,    20,    21,
       5,    -1,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    34,    -1,    -1,    20,    21,    -1,    -1,    41,
      -1,    -1,    -1,    45,    46,    47,    -1,    -1,    -1,    34,
      35,    53,    37,    55,    -1,    57,    41,    -1,    -1,    -1,
      45,    46,    -1,    65,    -1,    -1,    -1,    -1,    53,    -1,
      -1,    -1,    -1,    -1,    59,    77,    -1,    -1,    -1,    -1,
      -1,    83,    -1,    85,    -1,    -1,    -1,    -1,    -1,    -1,
      92,    93,    94,    -1,    -1,    -1,    -1,    -1,    -1,    84,
      85,    -1,    -1,    -1,    -1,    -1,    -1,    92,    93,    27,
      28,    29,    30,    31,    32,    33,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    27,    28,    29,    30,
      31,    32,    33,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      78,    79,    -1,    81,    -1,    -1,    -1,    -1,    -1,    -1,
      88,    89,    90,    -1,    -1,    -1,    -1,    95,    96,    97,
      98,    99,   100,    -1,   102,   103,   104,   105,   106,   107,
      81,   109,   110,   111,   112,    -1,    -1,    88,    89,    90,
      -1,    -1,    -1,    -1,    95,    96,    97,    98,    99,   100,
      -1,   102,   103,   104,   105,   106,   107,    -1,   109,   110,
     111,   112,    27,    28,    29,    30,    31,    32,    33,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      28,    29,    30,    31,    32,    33,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    81,    -1,    -1,    -1,
      -1,    -1,    -1,    88,    89,    90,    -1,    -1,    -1,    -1,
      95,    -1,    97,    98,    99,   100,    -1,   102,   103,   104,
     105,   106,   107,    81,   109,   110,   111,   112,    -1,    -1,
      88,    89,    90,    -1,    -1,    -1,    -1,    -1,    -1,    97,
      98,    99,   100,    -1,   102,   103,   104,   105,   106,   107,
      -1,   109,   110,   111,   112
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
     176,   177,   185,   194,   116,     5,   194,     5,    15,   154,
     155,   187,   154,   187,   170,   174,     5,    20,   146,   187,
       5,    35,    37,    59,    85,   141,   142,   143,   151,   153,
     158,   165,   167,   168,   169,     6,   138,   186,   187,     5,
     164,   186,   187,     5,   117,   119,   116,   187,   188,    78,
      79,    96,   124,   117,   193,    96,   195,   120,   157,    15,
     118,   137,     5,   195,     5,   116,   118,   187,     5,     4,
       5,   116,     5,   187,   188,     4,     5,    80,   116,    66,
      67,    68,    69,    70,    71,    72,    73,   145,   161,   185,
     185,   120,   119,   118,   116,   118,   185,   186,   187,   186,
      36,    96,   174,   184,   116,   195,     5,   116,   116,   116,
     174,   116,   116,   184,     5,   195,   195,   116,   195,     5,
      82,   110,   116,   118,   174,    33,   120,   118,   183,   120,
     120,   154,   187,   118,   119,   154,   118,   154,   116,   118,
       5,   116,   118,    96,   167,   116,   116,     5,    84,   168,
     118,   186,   187,   186,   118,   120,     5,   186,   195,   195,
     195,   195,   195,   195,   195,   187,   117,   121,   159,   160,
     183,   116,     5,   117,   121,   162,   163,   183,   116,   187,
     187,   188,   183,   119,   185,   120,   120,   195,   186,   117,
     183,   120,   118,   186,   118,     5,    36,   174,   195,   118,
     118,   195,   195,   195,   178,   179,   185,   195,    75,   118,
     120,   118,   195,   118,   174,    39,    40,   172,   173,   195,
     161,   195,   161,   195,   117,   195,   195,   118,   154,   155,
     118,   118,   136,     8,    11,    20,    21,    22,   149,   150,
     184,   116,   118,   136,   149,   174,     5,    36,   195,   178,
     118,   118,   187,   118,   118,   195,   187,   118,   120,   117,
     124,   124,   124,   118,     5,   110,   117,   119,   117,   159,
     118,     5,   117,   119,   117,   117,   159,   116,   117,   145,
     120,   195,   195,   118,   118,   117,   195,   118,   184,   117,
     117,   117,   117,   118,   119,   120,   117,   195,   117,   195,
     195,    41,   117,   119,   171,   195,   118,   195,   118,   118,
     118,   118,   117,    20,   186,   187,   186,   187,   186,   186,
     186,   150,   184,    56,   136,   149,   174,   117,   174,    58,
     167,   117,   118,   118,   118,   118,   195,   116,   118,   160,
     118,   117,   116,   163,   118,   117,   159,   117,   195,   118,
     118,   118,   118,    36,   174,    52,   180,   181,   182,   183,
     180,   180,   195,   179,   195,   174,   118,   174,   173,   118,
     118,   118,   186,   118,   187,   186,   118,     5,   186,   118,
     187,   118,   118,    56,   117,   174,    56,   118,    58,    36,
     168,   195,   118,   117,   195,   118,   195,   118,   117,   118,
      38,    96,    51,   181,   182,    51,    96,    51,   182,    51,
     182,   118,   149,   174,   118,   118,   118,   187,   118,   118,
     118,    56,   149,   174,    38,   118,   117,   117,   118,   174,
     118,   174,    51,   118,   174,    51,    51,   178,   174,    56,
     118,   149,   174,   174,    58,   168,   178,   117,    56,   174,
      56,    58,   117,   174,    56,   168
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
#line 2964 "y.tab.c"
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


#line 342 "yaccs/verilog.yacc"


