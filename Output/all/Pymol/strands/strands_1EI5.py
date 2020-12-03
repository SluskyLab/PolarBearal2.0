from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1EI5.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 24-31 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 34-45 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 50-51 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 58-59 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 191-192 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 205-208 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 212-215 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 228-230 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 270-271 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 274-279 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 282-291 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 294-301 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 306-312 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 348-351 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 358-363 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 368-372 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 378-384 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 387-389 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 394-398 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 401-406 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 411-417 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 428-432 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 437-444 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 447-454 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 457-458 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 462-468 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 471-476 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 486-494 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 500-507 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 510-517 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
