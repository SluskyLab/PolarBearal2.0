from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2LME.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 52-63 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 66-77 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 84-90 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 94-104 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Bstrand4", "resi 52-63 & chain B ")
cmd.color ("yellow", "Bstrand4")


cmd.select("Bstrand5", "resi 66-77 & chain B ")
cmd.color ("blue", "Bstrand5")


cmd.select("Bstrand6", "resi 84-90 & chain B ")
cmd.color ("red", "Bstrand6")


cmd.select("Bstrand7", "resi 94-104 & chain B ")
cmd.color ("green", "Bstrand7")


cmd.select("Cstrand8", "resi 52-63 & chain C ")
cmd.color ("orange", "Cstrand8")


cmd.select("Cstrand9", "resi 66-77 & chain C ")
cmd.color ("teal", "Cstrand9")


cmd.select("Cstrand10", "resi 84-90 & chain C ")
cmd.color ("yellow", "Cstrand10")


cmd.select("Cstrand11", "resi 94-104 & chain C ")
cmd.color ("blue", "Cstrand11")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
