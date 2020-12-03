from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2FGR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 3+4+5+6+7+8+9+10+11+12+13+14+15+16+17 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 320+321+322+323+324+325+326+327+328+329+330+331 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 286+287+288+289+290+291+292+293+294+295+296+297 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 269+270+271+272+273+274+275+276+277+278+279+280+281 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 253+254+255+256+257+258+259+260+261+262+263+264 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 235+236+237+238+239+240+241+242+243+244+245+246+247+248+249 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 218+219+220+221+222+223+224+225+226+227+228+229+230 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 199+200+201+202+203+204+205+206+207+208+209+210+211+212+213 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 183+184+185+186+187+188+189+190+191+192+193+194+195+196 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 171+172+173+174+175+176+177+178+179 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 148+149+150+151+152+153+154+155 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 137+138+139+140+141 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 86+87+88+89+90 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 76+77+78+79+80+81+82+83 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 51+52+53+54+55+56+57+58+59+60 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 26+27+28+29+30+31+38+39+40+41+42+43+44+45+46+47+48 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
