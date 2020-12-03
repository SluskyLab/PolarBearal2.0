from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2XST.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 35+35+36+37+38+39+40+41+42+43+44+59+60+61+62+63+64+65+71+72+73+74+75+76+85+86+87+88+89+90+91+92+98+99+100+101+106+107+108+109+110+111+112+113+114+119+120+121+122+123+124+125+126+127+128+131+132+133+134+135+136+137+138+139+140 & chain A")
cmd.load_cgo( [9.0, 33.51338,-12.369133,25.133076, 22.747341, 24.635197, 12.393425, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
