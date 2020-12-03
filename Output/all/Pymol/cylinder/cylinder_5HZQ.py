from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5HZQ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 5+5+6+7+8+9+10+11+12+13+40+41+42+43+44+45+46+49+50+51+52+53+54+55+59+60+61+62+63+64+65+66+128+129+130+131+132+133+134+135+136+119+120+121+122+123+124+125+107+108+109+110+111+112+113+92+93+94+95+96+97+98+99+80+81+82+83+84+85+86+87+71+72+73+74 & chain A")
cmd.load_cgo( [9.0, 5.962321,3.2095346,-23.804195, 5.574679, -30.9384, -6.032508, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
