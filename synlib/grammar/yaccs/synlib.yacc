
%token library cell pin timing bus
%token token number string floating
%token statetable ff latch test_cell
%token values
%%
libraries : libraries Library | Library ;

Library : library '(' tuken ')' '{' Items '}' ;

Items : Items Item | Item ;

Item : Cell | Pair ;


Token : token ;
String : string ;
Number : number ;
Floating : floating ;


tuken : Token | String ;
Pair :
      Token ':' Expr  ';'
    | Token ':' Number Token ';'
    | Token '(' Expr ')' ';'
    | Token '(' Expr ','  Expr ')' ';'
    | Token '(' Expr ','  Expr ')'
    | Token '(' Expr ','  Expr ',' Expr ')' ';'
    | Token '(' Expr ')'  '{' Pairs '}'
    | Token '(' ')'  '{' Pairs '}'
    | values '(' Values ')' ';'
    | values ':' Values  ';'
    | values '(' Values ')'
    ;


// Struct : Token '(' tuken ')' '{' Pairs '}' ;

Pairs : Pairs Pair | Pair ;
toks : toks ',' Token | Token ;
Exprs : Expr ',' Expr | Expr ;

Value : String | Floating | Number ;
Values : Values  ',' Value | Value ;

Expr : ff | Token | Number | String | Floating | library | cell | pin | timing | Expr '*' Expr | Expr '+' Expr | '-' Floating | Expr '-' Expr | '-' Number | '!' Token | values ;

Cell : cell '(' tuken ')' '{' cell_items '}' ;

cell_items : cell_items cell_item | cell_item ;
cell_item : Pair | Bus | Pin  | Ff | Statetable | Latch | Test_cell ;

test_cell_item : Pin | Ff | Latch ;
test_cell_items : test_cell_items test_cell_item | test_cell_item ;



Pin : pin '(' tuken ')' '{' pin_items '}' | pin '(' Token ',' Token ')' '{' pin_items '}' | pin '(' Token ',' Token ',' Token ')' '{' pin_items '}'  ;

pin_items : pin_items pin_item | pin_item ;
pin_item : Pair |Timing ;

Ff : ff '(' toks ')' '{' Pairs '}' ;
Statetable : statetable '(' Exprs ')' '{' Pairs '}' ;
Latch : latch '(' toks ')' '{' Pairs '}' ;
Test_cell : test_cell '(' ')' '{' test_cell_items '}' ;

Timing : timing  '(' ')' '{' timing_items '}' ;
timing_items : timing_items   timing_item | timing_item ;
timing_item : Pair ;


Bus : bus '(' tuken ')' '{' bus_items '}' ;
bus_items : bus_items bus_item | bus_item ;
bus_item : Pair |Timing | Bpin ;
Bpin : pin '(' tuken '[' Number ':' Number ']' ')' '{' '}' ;

%%


