from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4K3C.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 318-321 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 336-339 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 345-352 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 372-373 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 392-397 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 408-417 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 421-430 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 434-446 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 451-459 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 463-475 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 481-492 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 503-515 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 521-535 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 564-566 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 569-578 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 589-599 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 607-619 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 627-639 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 661-662 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 670-673 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 681-686 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 691-701 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 714-726 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 750-761 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 764-775 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 782-792 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
