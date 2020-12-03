from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4AZP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 9+10+11+12+13+14+15+16+17 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 125+126+127+128+129+130+131+132+133 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 115+116+117+118+119+120+121+122 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 103+104+105+106+107+108+109+110+111+112 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 93+94+95+96+97+98+99+100 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 82+83+84+85+86+87+88+89+90 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 73+74+75+76 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 62+63+64+65+66+67+68 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 51+52+53+54+55+56+57 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 42+43+44+45+46+47+48 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
