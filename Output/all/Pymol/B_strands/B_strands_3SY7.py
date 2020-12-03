from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SY7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 18+19+51+50+20+49+21+48+22+47+46+23+24+45+387+25+44+388+26+389+43+27+390+42+391+28+41+392+29+40+393+30+39+394+31+38+395+396+397 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 96+97+98+99+100+101+102+103+104+105+106+107+108 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 137+138+139+140+141+142+143+144 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 150+151+152+153+154+155+156+157+158+159+171+172+173+174 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 179+180+181+182+183+184+185+186+187+188+189+190+191+192+193+194 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 197+198+199+200+201+202+203+204+205+206 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 210+211+212+213+214+215+216+217+218+219+220+221+222+223+224 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 227+228+229+230+231+232+233+234+235+236+237+238+239+240 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 250+251+252+253+254+255+256+257+258+259+260+261+262 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 265+266+267+268+269+270+271+272+273+274+275+276 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 111+112+113+114+115+116+117+118 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 314+315+316+317+318+319+320+321+322+323 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 332+333+334+335+336+337+338+339+340+341+342+343+344 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 365+366+367+368+369+370+371+372+373+374+375+376+377 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 60+61+62+63+64+65+66+67+68+416+69+415+414+70+413+412+71+72+411+410+73+409+74+408+75+407+406 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
