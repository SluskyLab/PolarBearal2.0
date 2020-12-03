from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3D5K.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 88-99 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 110-126 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 299-310 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 322-335 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Bstrand4", "resi 88-99 & chain B ")
cmd.color ("yellow", "Bstrand4")


cmd.select("Bstrand5", "resi 110-126 & chain B ")
cmd.color ("blue", "Bstrand5")


cmd.select("Bstrand6", "resi 299-310 & chain B ")
cmd.color ("red", "Bstrand6")


cmd.select("Bstrand7", "resi 322-335 & chain B ")
cmd.color ("green", "Bstrand7")


cmd.select("Cstrand8", "resi 88-99 & chain C ")
cmd.color ("orange", "Cstrand8")


cmd.select("Cstrand9", "resi 110-126 & chain C ")
cmd.color ("teal", "Cstrand9")


cmd.select("Cstrand10", "resi 299-310 & chain C ")
cmd.color ("yellow", "Cstrand10")


cmd.select("Cstrand11", "resi 322-335 & chain C ")
cmd.color ("blue", "Cstrand11")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
