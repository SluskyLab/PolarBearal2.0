from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2WIQ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 12-22 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 25-35 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 41-48 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 90-98 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 103-113 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 116-126 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 139-142 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 145-151 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 156-167 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 172-183 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 195-205 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 213-223 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Bstrand12", "resi 12-22 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 25-35 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 41-48 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 90-98 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 103-113 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 116-126 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 139-142 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 145-151 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 156-167 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 172-183 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 195-204 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 213-223 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
