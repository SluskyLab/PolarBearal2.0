from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4Y25.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 518-530 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 540-547 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 555-565 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 575-586 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 589-599 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 604-615 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 620-628 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 644-654 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 659-670 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 675-689 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 693-697 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 700-705 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 718-735 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 738-753 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 757-772 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 776-788 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 793-807 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
