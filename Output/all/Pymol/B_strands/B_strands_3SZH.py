from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SZH.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 11+12+13+14 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 111+112+113+114+115+116+117+118+119 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 92+93+94+95+96+97+98+99+100+101 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 73+74+75+76+77+78+79+80+81+82+83+84+85 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 60+61+62+63+64+65+66+67+68 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 50+51+52+53+54+55+56+57 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 31+32+33+34+35+36+37 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 20+21+22+23+24+25+26 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
