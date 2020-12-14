from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1EW3.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 25+25+26+27+106+107+108+109+110+111+112+113+114+98+99+100+101+102+82+83+84+85+86+87+88+89+90+91+92+71+72+73+74+75+76+77+78+79+59+60+61+62+63+64+65+35+36+37+38+39+40+41+42+43+44+119+120+121+122+123+124+125+126+133+134+135+136+137+138+139+140+167+168+169 & chain A")
cmd.load_cgo( [9.0, 65.76048,7.885988,12.539695, 87.82735, 41.520584, 32.972057, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")