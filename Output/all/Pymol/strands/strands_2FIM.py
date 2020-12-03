from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2FIM.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 252-259 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 270-275 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 281-288 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 296-300 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 313-319 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 325-329 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 349-355 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 368-373 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 405-410 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 414-416 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 421-423 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 438-441 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 451-457 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 460-465 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Bstrand14", "resi 252-259 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("Bstrand15", "resi 270-275 & chain B ")
cmd.color ("teal", "Bstrand15")


cmd.select("Bstrand16", "resi 282-288 & chain B ")
cmd.color ("yellow", "Bstrand16")


cmd.select("Bstrand17", "resi 296-300 & chain B ")
cmd.color ("blue", "Bstrand17")


cmd.select("Bstrand18", "resi 315-319 & chain B ")
cmd.color ("red", "Bstrand18")


cmd.select("Bstrand19", "resi 325-330 & chain B ")
cmd.color ("green", "Bstrand19")


cmd.select("Bstrand20", "resi 349-357 & chain B ")
cmd.color ("orange", "Bstrand20")


cmd.select("Bstrand21", "resi 366-373 & chain B ")
cmd.color ("teal", "Bstrand21")


cmd.select("Bstrand22", "resi 405-410 & chain B ")
cmd.color ("yellow", "Bstrand22")


cmd.select("Bstrand23", "resi 414-415 & chain B ")
cmd.color ("blue", "Bstrand23")


cmd.select("Bstrand24", "resi 422-423 & chain B ")
cmd.color ("red", "Bstrand24")


cmd.select("Bstrand25", "resi 438-441 & chain B ")
cmd.color ("green", "Bstrand25")


cmd.select("Bstrand26", "resi 451-457 & chain B ")
cmd.color ("orange", "Bstrand26")


cmd.select("Bstrand27", "resi 460-465 & chain B ")
cmd.color ("teal", "Bstrand27")


cmd.select("barrel", "Astrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
