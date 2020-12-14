from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3A2S.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 2+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+30+31+32+33+34+35+36+37+328+329+330+331+332+333+334+335+336+337+338+339+340+310+311+312+313+314+315+316+317+318+319+320+321+322+323+295+296+297+298+299+300+301+302+303+304+305+306+307+271+272+273+274+275+276+277+278+279+280+254+255+256+257+258+259+260+261+262+263+264+265+266+267+268+231+232+233+234+235+236+237+238+239+240+241+242+243+212+213+214+215+216+217+218+219+220+221+222+223+224+225+226+227+228+184+185+186+187+188+189+190+191+192+193+194+195+196+197+198+171+172+173+174+175+176+177+178+179+180+144+145+146+147+148+149+150+151+128+129+130+131+132+133+134+135+136+137+89+90+91+92+93+94+95+77+78+79+80+81+82+83+84+85+55+56+57+58+59+60+61+62+63+64+65+66+42+43+44+45+46+47+48+49+202+203+204 & chain X")
cmd.load_cgo( [9.0, 27.59549,-12.934664,-6.47396, 16.565773, 31.745314, 37.74113, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")