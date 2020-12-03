from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3A2S.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Xstrand0", "resi 2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19 & chain X ")
cmd.color ("red", "Xstrand0")


cmd.select("Xstrand1", "resi 30+31+32+33+34+35+36+37+42+43+44+45+46+47+48+49 & chain X ")
cmd.color ("green", "Xstrand1")


cmd.select("Xstrand2", "resi 55+56+57+58+59+60+61+62+63+64+65+66 & chain X ")
cmd.color ("orange", "Xstrand2")


cmd.select("Xstrand3", "resi 77+78+79+80+81+82+83+84+85 & chain X ")
cmd.color ("teal", "Xstrand3")


cmd.select("Xstrand4", "resi 89+90+91+92+93+94+95 & chain X ")
cmd.color ("yellow", "Xstrand4")


cmd.select("Xstrand5", "resi 128+129+130+131+132+133+134+135+136+137 & chain X ")
cmd.color ("blue", "Xstrand5")


cmd.select("Xstrand6", "resi 144+145+146+147+148+149+150+151 & chain X ")
cmd.color ("red", "Xstrand6")


cmd.select("Xstrand7", "resi 184+185+186+187+188+189+190+191+192+193+194+195+196+197+198 & chain X ")
cmd.color ("green", "Xstrand7")


cmd.select("Xstrand8", "resi 171+172+173+174+175+176+177+178+179+180 & chain X ")
cmd.color ("orange", "Xstrand8")


cmd.select("Xstrand9", "resi 212+213+214+215+216+217+218+219+220+221+222+223+224+225+226+227+228 & chain X ")
cmd.color ("teal", "Xstrand9")


cmd.select("Xstrand10", "resi 231+232+233+234+235+236+237+238+239+240+241+242+243 & chain X ")
cmd.color ("yellow", "Xstrand10")


cmd.select("Xstrand11", "resi 254+255+256+257+258+259+260+261+262+263+264+265+266+267+268 & chain X ")
cmd.color ("blue", "Xstrand11")


cmd.select("Xstrand12", "resi 271+272+273+274+275+276+277+278+279+280 & chain X ")
cmd.color ("red", "Xstrand12")


cmd.select("Xstrand13", "resi 295+296+297+298+299+300+301+302+303+304+305+306+307 & chain X ")
cmd.color ("green", "Xstrand13")


cmd.select("Xstrand14", "resi 310+311+312+313+314+315+316+317+318+319+320+321+322+323 & chain X ")
cmd.color ("orange", "Xstrand14")


cmd.select("Xstrand15", "resi 328+329+330+331+332+333+334+335+336+337+338+339+340 & chain X ")
cmd.color ("teal", "Xstrand15")


cmd.select("barrel", "Xstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
