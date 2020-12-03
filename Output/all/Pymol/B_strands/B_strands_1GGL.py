from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1GGL.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 6+7+8+9+10+11+12+13+14 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 39+40+41+42+43+44 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 105+106+107+108+109+110+111 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 48+49+50+51+52+53+54 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 60+61+62+63+64+65 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 81+82+83+84+85+86+87+88 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 93+94+95+96+97+98 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 70+71+72+73 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 114+115+116+117+118+119+120+121 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 124+125+126+127+128+129+130+131+132 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
