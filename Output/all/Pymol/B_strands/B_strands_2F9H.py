from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2F9H.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 4+5+6+7+8+9+10+11+12 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 118+119+120+121+122 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 57+58+59+60 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 63+64+65+66+67+68+69+70 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 102+103+104+105+106 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 84+85+86+87 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 23+24+25+26+27 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 40+41+42+43 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
