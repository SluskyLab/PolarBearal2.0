from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4GGR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 11-14 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 20-25 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 30-36 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 48-56 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 59-66 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 71-77 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 83-93 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 99-111 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
