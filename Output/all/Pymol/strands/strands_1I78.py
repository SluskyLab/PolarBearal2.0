from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1I78.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 12-31 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 37-58 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 64-73 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 77-85 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 97-122 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 126-144 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 147-149 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 169-189 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 192-213 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 219-242 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 245-267 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 272-296 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Bstrand12", "resi 12-30 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 38-59 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 64-73 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 77-85 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 97-100 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 104-123 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 126-143 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 147-150 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 159-162 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 170-189 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 192-212 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 219-240 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 245-267 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 272-296 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
