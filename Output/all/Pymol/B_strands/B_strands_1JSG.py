from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1JSG.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 91+92+93+94+95+96+97+98+99+100 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 75+76+77+78 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 25+26+27+28 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 17+18+19+20+21+22 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 34+35+36+37+38+39+40+41+42 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 46+47+48+49+50+51+52+53 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 84+85+86 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 103+104+105+106+107+108+109+110+111 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
