from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2ZO6.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 8-18 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 21-32 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 37-46 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 87-95 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 100-110 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 113-123 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 135-138 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 141-148 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 151-162 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 167-178 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 189-200 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 203-213 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
