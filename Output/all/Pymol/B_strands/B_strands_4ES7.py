from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4ES7.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 16+17+18+19+20+21+22+23+24+25 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 40+41+42+43+44+45+46 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 104+105+106+107+108+109+110+111+112+113 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 90+91+92+93+94+95+96+97+98+99 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 80+81+82+83+84+85 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 64+65+66+67+68+69+70+71+72+73+74 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 52+53+54+55+56+57+58+59+60+61 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 119+120+121+122+123+124+125+126 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
