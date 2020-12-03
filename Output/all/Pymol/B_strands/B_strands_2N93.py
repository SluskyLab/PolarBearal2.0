from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2N93.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 6+7+8+9+10+11+12+13 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 40+41+42+43+44 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 49+50+51+52+53 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 59+60+61+62 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 103+104+105+106 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 88+89+90+91+92+93+94 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 76+77+78+79+80+81+82+83+84 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 66+67+68+69+70+71 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 112+113+114+115+116+117+118 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 121+122+123+124+125+126+127+128+129 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
