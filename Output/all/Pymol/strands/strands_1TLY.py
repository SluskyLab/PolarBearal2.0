from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1TLY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 13-23 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 35-45 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 48-57 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 77-85 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 99-111 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 120-131 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 138-151 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 159-176 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 179-191 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 213-223 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 227-237 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 247-249 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 254-256 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 261-272 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Bstrand14", "resi 14-23 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 35-45 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 48-57 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 77-85 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 99-115 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 118-131 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 138-151 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 159-176 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 179-191 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 213-223 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 227-237 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 247-248 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 255-256 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 261-271 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
