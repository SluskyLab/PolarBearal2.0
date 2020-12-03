from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1JSG.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 8-10 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 17-22 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 25-28 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 34-42 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 46-53 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 75-78 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 84-86 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 91-100 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 103-111 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
