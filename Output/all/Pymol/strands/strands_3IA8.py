from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3IA8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 18-22 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 26-30 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 33-45 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 51-59 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 66-76 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 82-89 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 93-102 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 105-115 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 124-133 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 139-147 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 150-163 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Bstrand11", "resi 18-22 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 26-30 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 33-45 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 51-59 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 66-76 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 82-89 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 93-102 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 105-115 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 124-133 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 139-147 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 153-163 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
