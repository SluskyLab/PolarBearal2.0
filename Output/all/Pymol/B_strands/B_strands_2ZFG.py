from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2ZFG.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 331+332+333+334+335+336+337+338+339+2+3+4+5+6 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 307+308+309+310+311+312+313+314+315+316 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 287+288+289+290+291+292+293+294+295+296+297+298+299+300+301+302+303+304 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 269+270+271+272+273+274+275+276+277+278+279+280+281+282+283 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 253+254+255+256+257+258+259+260+261+262+263 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 225+226+227+228+229+230+231+232+233+234+235 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 210+211+212+213+214+215+216+217+218+219+220+221+222 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 185+186+187+188+189+190+191+192+193+194+195 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 173+174+175+176+177+178+179+180+181+182 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 151+152+153+154+155+156+157+158 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 132+133+134+135+136+137+138+139+140+141 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 94+95+96+97+98+99+100+101+102 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 80+81+82+83+84+85+86+87+88+89+90 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 55+56+57+58+59+60+61+62+63+64+65+66 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 40+41+42+43+44+45+46+47+48+49+50 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 9+10+11+12+13+14+15+16+17+18+19+20+21+22+23 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
