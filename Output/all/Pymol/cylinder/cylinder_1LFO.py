from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1LFO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 6+6+7+8+35+36+37+38+39+40+41+42+43+44+47+48+49+50+51+52+53+54+57+58+59+60+61+62+63+64+67+68+70+71+72+73+78+79+80+81+82+83+84+85+86+90+91+92+93+94+95+98+99+100+101+102+103+104+105+108+109+110+111+112+113+114+115+118+119+120+121+122+123+124+125+11+12+13 & chain A")
cmd.load_cgo( [9.0, 45.567547,21.658297,35.088573, 7.3663483, 24.177755, 35.08865, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
