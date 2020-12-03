from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4DKN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 6-15 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 18-28 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 35-41 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 66-67 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 70-71 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 84-92 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 97-107 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 110-120 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 133-136 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 139-146 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 150-161 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 166-177 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 191-201 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 205-215 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Bstrand14", "resi 6-15 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 18-29 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 34-41 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 66-67 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 70-71 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 84-92 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 97-107 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 110-120 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 133-136 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 139-146 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 150-161 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 166-177 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 191-201 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 205-215 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
