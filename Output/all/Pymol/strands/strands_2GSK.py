from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2GSK.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 6-11 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 26-30 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 52-56 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 64-68 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 76-80 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 83-84 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 106-111 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 125-130 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 137-145 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 149-161 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 164-178 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 195-209 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 214-228 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 242-257 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 261-277 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 289-305 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 309-322 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 333-348 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 351-362 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 366-380 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 383-394 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 413-426 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 429-441 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 444-447 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 452-455 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 459-472 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 475-488 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 493-494 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 501-511 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 514-523 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 526-530 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 537-541 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 544-554 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 559-566 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Astrand34", "resi 585-593 & chain A ")
cmd.color ("yellow", "Astrand34")


cmd.select("Bstrand35", "resi 155-157 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 174-182 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("Bstrand37", "resi 188-197 & chain B ")
cmd.color ("green", "Bstrand37")


cmd.select("Bstrand38", "resi 214-215 & chain B ")
cmd.color ("orange", "Bstrand38")


cmd.select("Bstrand39", "resi 221-231 & chain B ")
cmd.color ("teal", "Bstrand39")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
