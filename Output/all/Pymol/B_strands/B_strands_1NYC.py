from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1NYC.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 2+3+4+5+6+7+8+9+10 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 38+39+40+41+42+43+44+45 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 29+30+31+32+33 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 52+53+54+55+56+57+58+59 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 64+65+66+67+68+69 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 72+73+74+75+76+77+78+79+80+81+82+83 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 86+87+88+89+90+91+92+93 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 103+104+105+106+107 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
