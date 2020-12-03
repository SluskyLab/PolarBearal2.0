from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2RD7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Cstrand0", "resi 29-38 & chain C ")
cmd.color ("red", "Cstrand0")


cmd.select("Cstrand1", "resi 54-58 & chain C ")
cmd.color ("green", "Cstrand1")


cmd.select("Cstrand2", "resi 65-72 & chain C ")
cmd.color ("orange", "Cstrand2")


cmd.select("Cstrand3", "resi 75-82 & chain C ")
cmd.color ("teal", "Cstrand3")


cmd.select("Cstrand4", "resi 91-94 & chain C ")
cmd.color ("yellow", "Cstrand4")


cmd.select("Cstrand5", "resi 103-110 & chain C ")
cmd.color ("blue", "Cstrand5")


cmd.select("Cstrand6", "resi 115-121 & chain C ")
cmd.color ("red", "Cstrand6")


cmd.select("Cstrand7", "resi 127-132 & chain C ")
cmd.color ("green", "Cstrand7")


cmd.select("Cstrand8", "resi 159-161 & chain C ")
cmd.color ("orange", "Cstrand8")


cmd.select("Cstrand9", "resi 176-178 & chain C ")
cmd.color ("teal", "Cstrand9")


cmd.select("barrel", "Cstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
