from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2QO4.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 4+5+6+7+8+9+10+11+12 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 46+47+48+49+50+51+52+53 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 56+57+58+59+60+61+62+63 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 67+68+69+70+71 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 77+78+79+80+81+82+83+84+85 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 88+89+90+91+92 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 97+98+99+100+101+102+103 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 37+38+39+40+41+42+43 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 106+107+108+109+110+111+112+113 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 116+117+118+119+120+121+122+123+124 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
