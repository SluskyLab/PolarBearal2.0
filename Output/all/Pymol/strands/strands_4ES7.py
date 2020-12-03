from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4ES7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 16-25 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 40-46 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 52-61 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 64-74 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 80-85 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 90-99 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 104-113 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 119-126 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 153-155 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
