from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2L5P.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 51-60 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 75-80 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 86-94 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 97-107 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 113-116 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 128-136 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 140-148 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 153-161 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 188-189 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
