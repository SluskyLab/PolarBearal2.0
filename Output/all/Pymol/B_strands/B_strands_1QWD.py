from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1QWD.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 85+86+87+88+89+90+91+92+93+94+95+14+17+16+15 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 72+73+74+75+76+77+78+79+80 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 58+59+60+61+62+63+64+65+66 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 41+42+43+44+45+46+47+48 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 138+139+140+141+142 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 127+128+129+130+131 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 112+113+114+115+116+117+118+119+120+121 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 109+108+107+106+105+104+103+30+28+31+29 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
