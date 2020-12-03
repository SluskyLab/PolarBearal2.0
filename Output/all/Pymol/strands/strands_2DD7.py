from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2DD7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 4-14 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 17-28 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 31-38 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 62-63 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 81-89 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 94-104 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 107-117 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 130-133 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 136-143 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 147-158 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 163-174 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 188-198 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 202-212 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Bstrand13", "resi 4-14 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 17-28 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 31-38 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 62-63 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 81-89 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 94-104 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 107-117 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 130-133 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 136-142 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 147-158 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 163-174 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 188-198 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 202-212 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
