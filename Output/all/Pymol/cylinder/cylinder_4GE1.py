from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4GE1.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 22+22+23+24+25+26+27+28+29+30+42+43+44+45+46+47+48+49+54+55+56+57+58+59+60+61+62+63+68+69+70+71+72+73+74+75+76+77+87+88+89+90+91+92+93+94+95+101+102+103+104+105+106+107+108+109+110+111+112+113+114+119+120+121+122+123+124+125+126+129+130+131+132+133+134+135+136+137+138+139 & chain A")
cmd.load_cgo( [9.0, 23.720268,9.9364395,47.880913, -14.427054, -2.741022, 47.88096, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
