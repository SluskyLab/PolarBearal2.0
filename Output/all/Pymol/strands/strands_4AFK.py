from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4AFK.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 42-54 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 66-81 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 84-95 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 124-135 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 144-154 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 162-173 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 177-185 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 204-216 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 219-230 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 248-261 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 272-292 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 297-319 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 324-333 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 353-354 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 363-364 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 377-388 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 392-403 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 425-437 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 457-467 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 479-489 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
