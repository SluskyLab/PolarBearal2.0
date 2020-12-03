from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1UUN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Bstrand0", "resi 2-9 & chain B ")
cmd.color ("red", "Bstrand0")


cmd.select("Bstrand1", "resi 15-28 & chain B ")
cmd.color ("green", "Bstrand1")


cmd.select("Bstrand2", "resi 38-51 & chain B ")
cmd.color ("orange", "Bstrand2")


cmd.select("Bstrand3", "resi 59-69 & chain B ")
cmd.color ("teal", "Bstrand3")


cmd.select("Bstrand4", "resi 72-81 & chain B ")
cmd.color ("yellow", "Bstrand4")


cmd.select("Bstrand5", "resi 88-89 & chain B ")
cmd.color ("blue", "Bstrand5")


cmd.select("Bstrand6", "resi 104-105 & chain B ")
cmd.color ("red", "Bstrand6")


cmd.select("Bstrand7", "resi 112-121 & chain B ")
cmd.color ("green", "Bstrand7")


cmd.select("Bstrand8", "resi 126-136 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Bstrand9", "resi 139-151 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 154-155 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 159-168 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 173-177 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 181-182 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 2-9 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 15-28 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 38-51 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 59-69 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 72-81 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 88-89 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 104-105 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 112-121 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 126-136 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 139-151 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 154-155 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 159-168 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 173-177 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 181-182 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("barrel", "Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
