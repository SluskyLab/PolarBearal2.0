from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2Y32.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 2-8 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 14-20 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 26-32 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 45-53 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 58-66 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 71-78 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 85-93 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 102-113 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Bstrand8", "resi 2-8 & chain B ")
cmd.color ("orange", "Bstrand8")


cmd.select("Bstrand9", "resi 14-20 & chain B ")
cmd.color ("teal", "Bstrand9")


cmd.select("Bstrand10", "resi 26-32 & chain B ")
cmd.color ("yellow", "Bstrand10")


cmd.select("Bstrand11", "resi 45-53 & chain B ")
cmd.color ("blue", "Bstrand11")


cmd.select("Bstrand12", "resi 58-66 & chain B ")
cmd.color ("red", "Bstrand12")


cmd.select("Bstrand13", "resi 71-78 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 85-93 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 102-113 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Cstrand16", "resi 6-8 & chain C ")
cmd.color ("yellow", "Cstrand16")


cmd.select("Cstrand17", "resi 14-20 & chain C ")
cmd.color ("blue", "Cstrand17")


cmd.select("Cstrand18", "resi 26-32 & chain C ")
cmd.color ("red", "Cstrand18")


cmd.select("Cstrand19", "resi 45-53 & chain C ")
cmd.color ("green", "Cstrand19")


cmd.select("Cstrand20", "resi 58-66 & chain C ")
cmd.color ("orange", "Cstrand20")


cmd.select("Cstrand21", "resi 71-78 & chain C ")
cmd.color ("teal", "Cstrand21")


cmd.select("Cstrand22", "resi 85-93 & chain C ")
cmd.color ("yellow", "Cstrand22")


cmd.select("Cstrand23", "resi 102-113 & chain C ")
cmd.color ("blue", "Cstrand23")


cmd.select("Dstrand24", "resi 2-8 & chain D ")
cmd.color ("red", "Dstrand24")


cmd.select("Dstrand25", "resi 14-20 & chain D ")
cmd.color ("green", "Dstrand25")


cmd.select("Dstrand26", "resi 26-32 & chain D ")
cmd.color ("orange", "Dstrand26")


cmd.select("Dstrand27", "resi 44-53 & chain D ")
cmd.color ("teal", "Dstrand27")


cmd.select("Dstrand28", "resi 58-66 & chain D ")
cmd.color ("yellow", "Dstrand28")


cmd.select("Dstrand29", "resi 71-78 & chain D ")
cmd.color ("blue", "Dstrand29")


cmd.select("Dstrand30", "resi 85-93 & chain D ")
cmd.color ("red", "Dstrand30")


cmd.select("Dstrand31", "resi 102-113 & chain D ")
cmd.color ("green", "Dstrand31")


cmd.select("barrel", "Astrand* or Bstrand* or Cstrand* or Dstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
