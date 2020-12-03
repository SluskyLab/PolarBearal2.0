from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4XMC.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 25-32 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 41-50 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 53-62 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 67-76 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 83-91 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 97-99 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 105-115 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 118-127 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 130-140 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 166-167 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
