from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4I3B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 7+7+8+9+10+11+12+13+14+15+40+41+42+43+44+45+46+50+51+52+53+54+55+56+64+65+66+67+68+69+70+128+129+130+131+132+133+134+135+118+119+120+121+122+123+124+125+106+107+108+109+110+111+112+113+114+115+96+97+98+99+100+101+102+103+86+87+88+89+90+91+92+93+75+76+77 & chain A")
cmd.load_cgo( [9.0, -1.9568665,-21.647436,50.52866, -7.125187, 16.829435, 59.90254, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
