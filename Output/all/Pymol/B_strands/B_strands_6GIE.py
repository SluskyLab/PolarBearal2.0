from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6GIE.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 0+1+2+3+4+5+6+7+8+9+10+11+12+13 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 263+264+265+266+267+268+269+270+271+272+273 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 244+245+246+247+248+249+250+251+252+253+254 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 230+231+232+233+234+235+236+237+238+239+240+241 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 212+213+214+215+216+217+218+219+220 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 198+199+200+201+202+203+204+205+206+207+208+209 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 185+186+187+188+189+190+191+192+193+194 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 168+169+170+116+171+115+117+114+118+172+95+113+119+94+96+93+97+112+120+173+92+98+99+91+174+121+90+100+122+175+123+176+124+177+178 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 72+73+74+75+76+77+135+78+134+79+133+80+132+131+81+130+129+82+128+127+83 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 52+53+54+55+56+57+58+59+60+61 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 21+22+23+24+25+26+27+28+29+30+31+32+33+34+35 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
