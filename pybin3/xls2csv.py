#! /usr/bin/env python3
import os,sys
import xlrd

Lines=[]
def main():
    if len(sys.argv)==1:
        print('activation:   xls2csv.py <xlsfile> [more xlsfiles]')
        return
    workOnAll(sys.argv[1:])


def workOnAll(CsvsNames):
    global Lines
    Lines=[]
    for Fname in CsvsNames:
        workon(Fname)
    Fname = CsvsNames[0]
    BaseName = get_file_basename(Fname)
    Foutname = '%s.csv'%BaseName
    Fout = open(Foutname,'w')
    print('opening csv file %s'%Foutname)
    li=0
    for line in Lines:
        line.encode('ascii','replace')
        Fout.write('%s\n'%(line.encode('ascii','replace')))
        li+=1
    Fout.close()
    print('%d lines written to %s file, max len is %d fields'%(li,Foutname,mlen))

def get_file_basename(Fname):
    ww0 = Fname.split('/')
    Base0 = ww0[-1]
    ww = Base0.split('.')
    Base1=ww[0]
    return Base1

mlen=0
def workon(Fname):
    global mlen
    try:
        book = xlrd.open_workbook(Fname)
    except:
        print('cannot open %s'%Fname)
        return
    print("The number of worksheets is", book.nsheets)
    SheetNames = book.sheet_names()
    SheetVisi = book._sheet_visibility
    for Ind in range(book.nsheets):
        sh = book.sheet_by_index(Ind)
        Lines.append('sheet,ilia,%d,%s,%s'%(Ind,SheetNames[Ind],SheetVisi[Ind]))
        for rx in range(sh.nrows):
            line=[]
            Li = sh.row(rx)
            for Cell in Li:
                if Cell.ctype==0:
                    Val = ''
                elif Cell.ctype==1:
                    Val = Cell.value
                elif Cell.ctype==2:
                    Val = str(int(Cell.value))
                elif Cell.ctype==3:
                    Val = str(float(Cell.value))
                elif Cell.ctype in[4,5]:
                    Val = str(Cell.value)
                else:
                    print('ilia ctype=%s %s'%(Cell.ctype,Cell.value))
                    Val = str(Cell.value)
                if ('\n' in Val):
                    Val = Val.replace('\n','\\n')
                if (',' in Val):
                    Val = Val.replace(',','^^')
                line.append(Val)
            Line = ','.join(line)
            Lines.append(Line)
            mlen=max(mlen,len(line))
    return Lines

if __name__=='__main__':
    main()



