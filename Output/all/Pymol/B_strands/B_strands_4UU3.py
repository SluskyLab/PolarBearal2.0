from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4UU3.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 15+16+17+18+19+20+21 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 26+27+28+29+30+31+32+33 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 36+37+38+39+40+41 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 50+51+52+53+54+55+56+57+58+59+60+61+62 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 65+66+67+68+69+70+71 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 77+78+79+80+81+82+83 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 88+89+90+91+92+93+94+95 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 130+131+132+133+134+135+136+137+138+139+140+141+142+143 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
