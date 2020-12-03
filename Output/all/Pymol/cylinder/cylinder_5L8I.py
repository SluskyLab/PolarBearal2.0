from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5L8I.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 5+5+6+7+8+9+10+11+12+13+37+38+39+40+41+42+43+44+47+48+49+50+51+52+53+54+59+60+61+62+63+64+65+118+119+120+121+122+123+124+125+126+108+109+110+111+112+113+114+115+98+99+100+101+102+103+104+90+91+92+93+94+95+80+81+82+83+84+85+86+87+69+70+71+72 & chain A")
cmd.load_cgo( [9.0, 40.977493,9.693275,67.43026, 50.41313, -24.563492, 51.6292, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
