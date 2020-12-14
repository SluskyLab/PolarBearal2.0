from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3NSG.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 13+14+15+16+17+18+19+20+21+22+23+24 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 332+333+334+335+336+337+338+339+340 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 36+37+38+39+40+41+42+43+44+45 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 52+53+54+55+56+57+58+59+60+61+62 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 74+75+76+77+78+79+80+81+82+83+84+85 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 89+90+91+92+93+94+95+96+97 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 149+150+151+152+153+154+155+156 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 172+173+174+175+176+177+178+179+180+181 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 184+185+186+187+188+189+190+191+192+193 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 209+210+211+212+213+214+215+216+217+218+219+220 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 223+224+225+226+227+228+229+230+231+232 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 130+131+132+133+134+135+136+137+138+139 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 251+252+253+254+255+256+257+258+259+260+261 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 269+270+271+272+273+274+275+276+277+278+279 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 288+289+290+291+292+293+294+295+296+297+298+299+300 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 306+307+308+309+310+311+312+313+314+315 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
