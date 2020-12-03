from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1QWD.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 14+14+15+16+17+28+29+30+31+112+113+114+115+116+117+118+119+120+121+103+104+105+106+107+108+109+85+86+87+88+89+90+91+92+93+94+95+72+73+74+75+76+77+78+79+80+58+59+60+61+62+63+64+65+66+41+42+43+44+45+46+47+48+127+128+129+130+131+138+139+140+141+142 & chain A")
cmd.load_cgo( [9.0, -9.399707,12.82502,36.310497, 16.546179, 51.79432, 34.116108, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
