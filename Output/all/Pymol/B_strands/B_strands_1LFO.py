from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1LFO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 35+36+37+38+39+40+41+42+43+44 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 98+99+100+101+102+103+104+105 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 78+79+80+81+82+83+84+85+86 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 90+91+92+93+94+95 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 108+109+110+111+112+113+114+115 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 67+68+70+71+72+73 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 118+119+120+121+122+123+124+125 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 11+12+13 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 57+58+59+60+61+62+63+64 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 47+48+49+50+51+52+53+54 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")