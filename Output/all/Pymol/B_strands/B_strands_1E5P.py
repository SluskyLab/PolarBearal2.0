from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1E5P.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Bstrand0", "resi 7+8+9+10+11+12+13+14+15+16+17+18+19 & chain B ")
cmd.color ("red", "Bstrand0")


cmd.select("Bstrand1", "resi 44+45+46+47+48+49+50+51+52+53 & chain B ")
cmd.color ("green", "Bstrand1")


cmd.select("Bstrand2", "resi 35+36+37+38+39 & chain B ")
cmd.color ("orange", "Bstrand2")


cmd.select("Bstrand3", "resi 56+57+58+59+60+61+62+63+64+65+66+67 & chain B ")
cmd.color ("teal", "Bstrand3")


cmd.select("Bstrand4", "resi 71+72+73+74+75+76 & chain B ")
cmd.color ("yellow", "Bstrand4")


cmd.select("Bstrand5", "resi 79+80+81+82+83 & chain B ")
cmd.color ("blue", "Bstrand5")


cmd.select("Bstrand6", "resi 91+92+93+94+95+96+97+98+99+100 & chain B ")
cmd.color ("red", "Bstrand6")


cmd.select("Bstrand7", "resi 105+106+107+108+109+110+111+112+113 & chain B ")
cmd.color ("green", "Bstrand7")


cmd.select("barrel", "Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
