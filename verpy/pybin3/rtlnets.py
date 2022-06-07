



def help_main(Env):
    Mod = Env.Current
    Fout = open('%s.html' % Mod.Module,'w')
    Fout.write(HEAD0)
    Mod.buildNetTable()
    Nets = list(Mod.netTable.keys())
    Nets.sort()
    for Net in Nets:
        Dir,Wid = Mod.nets[Net]
        H = Wid
        if type(Wid) is tuple:
            if len(Wid) == 2:
                H = Wid[0]
                if type(H) is  int: H = H+1

        Fout.write('<tr>\n')
        Fout.write('<td> %s </td>\n' % Net)
        Fout.write('<td> %s </td>\n' % Dir)
        Fout.write('<td> %s </td>\n' % str(H))
        List = Mod.netTable[Net]
        for (A,B,C) in List:
            Fout.write('<td>%s @%s <a target="_blank" href="file:%s.html">%s</a></td>\n' % (C,A,B,B))
        Fout.write('</tr>\n')
    Fout.write('</table> </center> </body> </html>\n')
    Fout.close()


HEAD0 = '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <title>MODULE</title>
  </head>

  <body>
    <center>

      <h1>set</h1>

      <table border>
      <tr>
        <td align="center"><b>net</b></td>
        <td align="center"><b>dir</b></td>
        <td align="center"><b>wid</b></td>
        <td colspan=16 align="center"><b>conns bits</b></td>
      </tr>
'''
