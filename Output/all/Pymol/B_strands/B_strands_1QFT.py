from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1QFT.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 30+31+32+33+34 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 50+51+52+53+54 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 62+63+64+65+66+67+68+69 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 78+79+80+81+82+83+84+85+86+87 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 97+98+99+100+101+102 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 107+108+109+110+111+112+113+114+115+116 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 119+120+121+122+123+124 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 133+134+135+136+137+138 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
