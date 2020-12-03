from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2FHL.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 8+9+10+11+12 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 111+112+113+114+115+116+117+118+119+120 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 89+90+91+92+93+94+95+96+97+98 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 61+62+63+64+65+66+67 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 74+75+76+77+78+79+80+81+82+83 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 47+48+49+50+51+52+53 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 28+29+30+31+32+33+34 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 17+18+19+20 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
