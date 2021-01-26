
import string,os,sys
import logs


header_string = '\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">\n\
<html>\n\
  <head>\n\
    <title>CHIPCHIP regfile </title>\n\
  </head>\n\
\n\
  <body>\n\
\n\
      <h1>CHIPCHIP regfile </h1>\n\
\n\
'

table_header_string = '\
      <tr>\n\
        <td align="center"> <font size="7"><b>regfile</b></font></td>\n\
        <td align="center"> <font size="7"><b>addr</b></font></td>\n\
        <td align="center"> <font size="7"><b>name</b></font></td>\n\
        <td align="center"> <font size="7"><b>access</b></font></td>\n\
        <td align="center"> <font size="7"><b>width</b></font></td>\n\
        <td align="center"> <font size="7"><b>reset</b></font></td>\n\
        <td align="center"> <font size="7"><b>external clk</b></font></td>\n\
        <td colspan=8 align="center"> <font size="7"><b>description</b></font></td>\n\
      </tr>\n\
'
Order = 'access width reset clk description'.split()

tail_string = '</table> </center> </body> </html>\n\n'
def switch_colors():
    global color,othercolor
    x = color
    color=othercolor
    othercolor=x


def getVal(Params,Key):
    if Key in Params:
        Val = Params[Key]
        if type(Val) is int: Val = hex(Val)
        return Val
    return ''

ChipOrder = 'bus reset width  base empty'.split()

def produce_ext_html(Db):
    Faddrs = '%s/%s_base_defs.py'%(Db.DirPath,Db.Module)
    if os.path.exists(Faddrs):
        sys.path.append(Db.DirPath)
        exec('import %s_base_defs as Addrs'%(Db.Module))
    else:
        logs.log_warning('NO prerun addresses file "%s"'%Faddrs)
        logs.log_warning('First run will create the addresses mapping. Run again and the address file will be used')
        Addrs = False

    if Addrs:
        try:
            X = Addrs.ADDR_MAP.keys()
        except:
            Addrs = False


    ofile = open('%s/%s_rgf.html'%(Db.DirPath,Db.Module),'write')
    Str = header_string.replace('CHIPCHIP',Db.Module)
    ofile.write(Str)
    ofile.write('<table border>\n')
    List = [Db.Module]
    for Key in ChipOrder:
        Val = getVal(Db.chip.Params,Key)
        List.append('%s=%s'%(Key,Val))
    oneLine('#d0ffff',List,ofile,7)
    ofile.write(table_header_string)

    for Item in Db.items:
        Addr = 0
        Name = Item.Params['names'][0]
        if Addrs:
            if Name in Addrs.ADDR_MAP:
                Addr = Addrs.ADDR_MAP[Name]
                Addr = hex(Addr)
        if Item.Kind=='gap':
            if 'align' in Item.Params:
                Addr = 'align '+hex(Item.Params['align'])
            elif 'abs' in Item.Params:
                Addr = 'abs '+hex(Item.Params['abs'])
        if Item.Kind=='field': Addr = ''
        List = [Item.Kind,Addr,Name]
        for Key in Order:
            Val = getVal(Item.Params,Key)
            List.append(Val)

        if Item.Kind=='field':
            oneLine('#ffd0ff',List,ofile)
        elif Item.Kind=='reg':
            oneLine('#ffffd0',List,ofile)
        elif Item.Kind=='gap':
            oneLine('#ffd0d0',List,ofile)
        elif Item.Kind=='ram':
            oneLine('#d0ffd0',List,ofile)
    ofile.write(tail_string)
    ofile.close()

def oneLine(Color,LL,ofile,Size=6):
    ofile.write('<tr bgcolor='+Color+'>\n')
    run_on_coding(LL,ofile,Size)
    ofile.write('<td align="center">'+' '+'</td>\n')
    ofile.write('</tr>\n')


def produce_html(Module,Db):
    global color,othercolor
#    return                       # use first one.
    Chip = Db['chip']
    Items = Db['items']
    print(list(Db.keys()))
    Range = Chip.Addr+4
    OpcodeWidth = 16
    ofile = open('%s_rgf.html'%(Module),'w')
    Fcsv = open('%s.csv'%(Module),'w')
    Fcsv.write('kind,access,width,name,reset,addr,desc\n')
    Str = header_string.replace('CHIPCHIP',Module)
    ofile.write(Str)
    ofile.write(table_header_string.replace('OPCODEWIDTH',str(OpcodeWidth)))

    color = '#ffc0ff'
    othercolor = '#ffffc0'
    instruction = 'kind'
    color = '#80ff80'
    othercolor = '#ffffa0'
    color0 = '#c0a0c0'
    color1 = '#a0e0e0'

    Prmx = Db['chip'].Params
    Keys = list(Prmx.keys())
    Keys.sort()
    LL = ['CHIP']
    for Key in Keys:
        if Key != 'names':
            LL.append('%s=%s'%(Key,Prmx[Key]))
    ofile.write('<tr bgcolor='+color0+'>\n')
    run_on_coding(LL,ofile)

    ofile.write('<td align="center">'+' '+'</td>\n')
    ofile.write('</tr>\n')

    origarr = 'kind access width name  reset  addr expl'.split()
    ofile.write('<tr bgcolor='+color1+'>\n')
    run_on_coding(origarr,ofile)
    ofile.write('</tr>\n')

    for Item in Items:
        if 'reset' not in Item.Params: 
            Reset = ' '
        else:
            Reset = hex(Item.Params['reset'])
        if 'access' not in Item.Params: Item.Params['access']=''
        if 'width' not in Item.Params: Item.Params['width']=0
        if 'description' not in Item.Params: Item.Params['description'] = ''
        Desc = Item.Params['description'].replace('.',' ')
        if Item.Kind=='gap':
            Item.Params['names']=['gap']
        Addr = hex(Item.Addr)
        if Item.Addr<0: Addr = ''
        List = [Item.Kind,Item.Params['access'],Item.Params['width'],Item.Params['names'][0],Reset,Addr,Desc]
        Fcsv.write('%s,%s,%s,%s,%s,%s,%s\n'%(List[0],List[1],List[2],List[3],List[4],List[5],List[6]))
        acolor=color
#        ofile.write('<tr bgcolor='+color+'> <td><a target="_blank" href="file:chip_doc.html/#'+Inst+'">'+Inst+'</a></td>\n')
        ofile.write('<tr bgcolor='+color+'>')
        run_on_coding(List,ofile)
        ofile.write('</tr>\n')
        switch_colors()


    ofile.write(tail_string)
    ofile.close()
    Fcsv.close()

def run_on_coding(wrds,ofile,Size=6):
    for word in wrds:
         ofile.write('<td align="left" > <font size="%s"> '%Size+str(word)+' </font> </td>\n')


