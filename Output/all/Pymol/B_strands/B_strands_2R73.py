from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2R73.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 29+30+31+32+33+34+35 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 50+51+52+53+54+55+56+57 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 60+61+62+63+64+65+66+67+68+69 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 72+73+74+75+76+77+78+79+80+81+82 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 88+89+90+91+92 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 96+97+98+99+100+101+102 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 109+110+111+112+113+114+115+116+117+118 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 121+122+123+124+125+126+127+128+129+130 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
