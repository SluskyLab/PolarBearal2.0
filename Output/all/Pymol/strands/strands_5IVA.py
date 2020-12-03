from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5IVA.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 51-54 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 60-63 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 66-68 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 74-83 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 89-98 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 101-111 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 126-136 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 142-151 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 171-181 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 185-196 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 206-216 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 225-236 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 244-245 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 251-253 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 267-278 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 281-282 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 286-302 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 321-343 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 346-361 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 399-412 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 416-428 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 463-471 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 475-484 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 489-499 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 508-516 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 520-522 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 529-531 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 538-548 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 553-562 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 567-578 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 583-596 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 602-615 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Bstrand32", "resi 8-9 & chain B ")
cmd.color ("orange", "Bstrand32")


cmd.select("Bstrand33", "resi 23-26 & chain B ")
cmd.color ("teal", "Bstrand33")


cmd.select("Bstrand34", "resi 55-70 & chain B ")
cmd.color ("yellow", "Bstrand34")


cmd.select("Bstrand35", "resi 76-90 & chain B ")
cmd.color ("blue", "Bstrand35")


cmd.select("Bstrand36", "resi 96-109 & chain B ")
cmd.color ("red", "Bstrand36")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
