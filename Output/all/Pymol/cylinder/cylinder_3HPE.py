from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3HPE.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 28+28+29+30+31+32+33+34+35+39+40+41+42+43+44+167+168+169+170+171+172+173+174+175+176+177+178+179+180+141+142+143+144+145+146+147+148+149+150+151+152+119+120+121+122+123+124+125+126+127+128+129+130+131+132+133+134+109+110+111+112+113+114+115+116+97+98+99+100+101+102+103+104+105+106+60+61+62+63+64+65+66+67+68+69+48+49+50+51+52+53+54+55 & chain A")
cmd.load_cgo( [9.0, 15.861593,-25.901293,45.656353, -11.091223, 5.3198357, 17.598232, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
