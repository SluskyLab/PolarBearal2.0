from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1O8V.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7+8+9+10+11+12+13+14 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 123+124+125+126+127+128+129+130 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 113+114+115+116+117+118+119+120 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 101+102+103+104+105+106+107+108+109+110 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 91+92+93+94+95+96+97+98 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 82+83+84+85+86+87+88 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 69+70+71+72+73+74+75 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 60+61+62+64 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 49+50+51+52+53+54+55+56 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 36+37+38+39+40+41+42+43+44+45 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
