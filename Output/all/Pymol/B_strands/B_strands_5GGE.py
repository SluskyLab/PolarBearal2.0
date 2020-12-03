from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5GGE.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7+8+9+10+11+12+13+14 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 39+40+41+42+43+44+45 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 48+49+50+51+52+53+54 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 59+60+61+62+63+64 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 79+80+81+82+83+84+85+86+87 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 70+71+72+73 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 90+91+92+93+94+95 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 101+102+103+104+105+106+107+108 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 111+112+113+114+115+116+117+118 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 121+122+123+124+125+126+127+128+129 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
