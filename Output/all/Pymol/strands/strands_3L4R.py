from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3L4R.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 17-26 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 41-48 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 51-59 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 64-73 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 79-83 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 87-96 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 100-109 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 112-121 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 148-150 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
