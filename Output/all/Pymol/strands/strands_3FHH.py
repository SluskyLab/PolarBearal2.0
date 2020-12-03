from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3FHH.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 4-5 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 11-13 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 18-26 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 37-37 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 45-45 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 48-53 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 60-63 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 66-67 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 71-75 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 78-78 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 82-83 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 89-93 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 97-104 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 115-115 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 118-126 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 129-129 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 135-146 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 151-162 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 165-181 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 185-202 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 205-205 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 208-223 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 226-226 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 229-229 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 232-233 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 237-237 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("Astrand26", "resi 240-256 & chain A ")
cmd.color ("orange", "Astrand26")


cmd.select("Astrand27", "resi 260-260 & chain A ")
cmd.color ("teal", "Astrand27")


cmd.select("Astrand28", "resi 263-278 & chain A ")
cmd.color ("yellow", "Astrand28")


cmd.select("Astrand29", "resi 287-303 & chain A ")
cmd.color ("blue", "Astrand29")


cmd.select("Astrand30", "resi 307-326 & chain A ")
cmd.color ("red", "Astrand30")


cmd.select("Astrand31", "resi 341-359 & chain A ")
cmd.color ("green", "Astrand31")


cmd.select("Astrand32", "resi 362-379 & chain A ")
cmd.color ("orange", "Astrand32")


cmd.select("Astrand33", "resi 382-382 & chain A ")
cmd.color ("teal", "Astrand33")


cmd.select("Astrand34", "resi 385-401 & chain A ")
cmd.color ("yellow", "Astrand34")


cmd.select("Astrand35", "resi 404-415 & chain A ")
cmd.color ("blue", "Astrand35")


cmd.select("Astrand36", "resi 429-432 & chain A ")
cmd.color ("red", "Astrand36")


cmd.select("Astrand37", "resi 435-442 & chain A ")
cmd.color ("green", "Astrand37")


cmd.select("Astrand38", "resi 446-464 & chain A ")
cmd.color ("orange", "Astrand38")


cmd.select("Astrand39", "resi 467-467 & chain A ")
cmd.color ("teal", "Astrand39")


cmd.select("Astrand40", "resi 470-483 & chain A ")
cmd.color ("yellow", "Astrand40")


cmd.select("Astrand41", "resi 487-491 & chain A ")
cmd.color ("blue", "Astrand41")


cmd.select("Astrand42", "resi 496-518 & chain A ")
cmd.color ("red", "Astrand42")


cmd.select("Astrand43", "resi 521-533 & chain A ")
cmd.color ("green", "Astrand43")


cmd.select("Astrand44", "resi 539-545 & chain A ")
cmd.color ("orange", "Astrand44")


cmd.select("Astrand45", "resi 548-557 & chain A ")
cmd.color ("teal", "Astrand45")


cmd.select("Astrand46", "resi 562-571 & chain A ")
cmd.color ("yellow", "Astrand46")


cmd.select("Astrand47", "resi 574-584 & chain A ")
cmd.color ("blue", "Astrand47")


cmd.select("Astrand48", "resi 587-599 & chain A ")
cmd.color ("red", "Astrand48")


cmd.select("Astrand49", "resi 605-612 & chain A ")
cmd.color ("green", "Astrand49")


cmd.select("Astrand50", "resi 618-620 & chain A ")
cmd.color ("orange", "Astrand50")


cmd.select("Astrand51", "resi 625-627 & chain A ")
cmd.color ("teal", "Astrand51")


cmd.select("Astrand52", "resi 630-639 & chain A ")
cmd.color ("yellow", "Astrand52")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
