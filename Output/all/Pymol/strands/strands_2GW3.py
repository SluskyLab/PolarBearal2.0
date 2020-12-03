from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2GW3.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 8-18 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 21-32 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 37-46 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 87-95 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 100-110 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 113-123 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 136-139 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 142-149 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 152-163 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 167-179 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 190-201 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 207-217 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Bstrand12", "resi 8-18 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 21-32 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 37-46 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 87-95 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 100-110 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 113-123 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 136-139 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 142-149 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 152-163 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 167-179 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 190-201 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 207-217 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
