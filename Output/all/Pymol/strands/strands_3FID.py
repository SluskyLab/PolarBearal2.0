from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3FID.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 2-9 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 33-44 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 49-60 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 80-94 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 97-108 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 140-151 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 154-157 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 160-173 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 176-188 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 215-231 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 251-263 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 266-275 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 285-295 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Bstrand13", "resi 2-9 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 33-46 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 49-60 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 80-94 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 97-108 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 140-151 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 154-157 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 160-173 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 176-188 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 215-231 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 251-263 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 266-275 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 285-295 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
