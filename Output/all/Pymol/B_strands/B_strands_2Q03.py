from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2Q03.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7+8+9+10+11+12+14+15+16+17+18+19+20+21+22+23+24+25+26 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 127+128+129+130+131+132+133+134+135+136 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 114+115+116+117+118+119+120+121+122 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 79+80+81+82+83+84+85+86+87+88+89+90+91+92 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 95+96+97+98+99+100+101+102 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 63+64+65+66+67+68+69+70+71+72+73+74+75+76 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 46+47+48+49+50+51+52+53+54+55+56+57+58+59+60 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 32+33+34+35+36+37+38+39+40+41+42 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")