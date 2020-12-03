from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4BJ8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 10+11+12+13+14 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 19+20+21+22+23+24+25 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 28+29+30+31+32+33+34 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 49+50+51+52+53+54+55+56 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 63+64+65+66+67+68+69 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 75+76+77+78+79+80+81+82+83+84 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 90+91+92+93+94+95+96+97+98+99 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 112+113+114+115+116+117+118+119+120+121 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
