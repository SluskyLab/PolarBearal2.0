from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5EZ2.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 22+22+23+24+138+139+140+141+142+143+144+145+146+147+43+44+45+46+47+48+49+50+59+60+61+62+63+64+65+66+67+73+74+75+76+77+78+79+80+86+87+88+89+90+91+92+93+94+103+104+105+106+107+108+114+115+116+117+118+119+120+121+126+127+128+129+130+131+132+133+134+135 & chain A")
cmd.load_cgo( [9.0, 59.560104,102.01131,11.547914, 33.004288, 66.013565, 31.343918, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
