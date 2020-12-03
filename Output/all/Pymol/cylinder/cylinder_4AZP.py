from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4AZP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 9+9+10+11+12+13+14+15+16+17+42+43+44+45+46+47+48+51+52+53+54+55+56+57+62+63+64+65+66+67+68+125+126+127+128+129+130+131+132+133+115+116+117+118+119+120+121+122+103+104+105+106+107+108+109+110+111+112+93+94+95+96+97+98+99+100+82+83+84+85+86+87+88+89+90+73+74+75+76 & chain A")
cmd.load_cgo( [9.0, 26.184551,29.649708,-5.5222282, 31.2053, 0.11652374, 19.917511, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
