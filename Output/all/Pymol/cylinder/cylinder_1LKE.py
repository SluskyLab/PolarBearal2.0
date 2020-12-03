from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1LKE.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 24+24+25+26+27+28+29+30+31+41+42+43+44+45+46+47+48+49+50+53+54+55+56+57+58+59+60+61+62+65+66+67+68+69+70+71+72+73+74+75+83+84+85+86+87+88+89+90+93+94+95+96+97+98+99+100+101+102+103+104+109+110+111+112+113+114+115+116+125+126+127+128+129+130+131+132 & chain A")
cmd.load_cgo( [9.0, 32.81139,-22.41791,37.244778, -7.9300575, -22.179903, 37.244854, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
