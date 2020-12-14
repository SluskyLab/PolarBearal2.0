from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3WI4.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 300+301+302+303+304+305+306+307+308+309+310+311+312 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 282+283+284+285+286+287+288+289+290+291+292+293 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 267+268+269+270+271+272+273+274+275+276+277 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 247+248+249+250+251+252+253 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 227+228+229+230+231+232+233+234+235+236+237+238 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 207+208+209+210+211+212+213+214+215+216+217+218+219+220 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 190+191+192+193+194+195+196+197+198+199+200+201+202+203+204 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 158+159+160+161+162+163+164+165+166+167 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 170+171+172+173+174+175+176+177+178+179+180+181 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 139+140+141+142+143+144+145+146 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 125+126+127+128+129+130+131+132 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 87+88+89+90+91+92+93+94+95 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 78+79+80+81+82+83+84 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 54+55+56+57+58+59+60+61+62+63 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 32+33+34+29+35+36+28+37+27+26+41+42+43+44+45+46+47+48+49+50+51 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
