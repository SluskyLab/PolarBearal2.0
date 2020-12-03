from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3S26.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 29+29+30+31+32+33+34+35+36+37+38+53+54+55+56+57+58+64+65+66+67+68+69+70+79+80+81+82+83+84+85+86+87+93+94+95+96+105+106+107+108+109+110+111+112+113+114+115+120+121+122+123+124+125+126+127+128+129+132+133+134+135+136+137+138+139+140+141+168+169+170+171+172 & chain A")
cmd.load_cgo( [9.0, 2.034608,-2.4093428,10.137962, 3.8681145, -2.4092684, -31.19585, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
