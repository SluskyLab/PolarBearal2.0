from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2QO4.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 4+4+5+6+7+8+9+10+11+12+37+38+39+40+41+42+43+46+47+48+49+50+51+52+53+56+57+58+59+60+61+62+63+116+117+118+119+120+121+122+123+124+106+107+108+109+110+111+112+113+97+98+99+100+101+102+103+88+89+90+91+92+77+78+79+80+81+82+83+84+85+67+68+69+70+71 & chain A")
cmd.load_cgo( [9.0, -6.601837,11.619436,-19.372152, -13.211069, 25.511366, 17.026926, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
