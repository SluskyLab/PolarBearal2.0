from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5EZ2.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 138+139+140+141+142+143+144+145+146+147 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 43+44+45+46+47+48+49+50 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 59+60+61+62+63+64+65+66+67 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 73+74+75+76+77+78+79+80 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 86+87+88+89+90+91+92+93+94 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 103+104+105+106+107+108 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 114+115+116+117+118+119+120+121 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 126+127+128+129+130+131+132+133+134+135 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
