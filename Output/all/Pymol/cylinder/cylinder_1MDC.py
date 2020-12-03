from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1MDC.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 7+7+8+9+10+11+12+13+37+38+39+40+41+42+43+48+49+50+51+52+53+58+59+60+61+62+63+124+125+126+127+128+129+130+112+113+114+115+116+117+100+101+102+103+104+105+106+107+90+91+92+93+94+95+77+78+79+80+81+82+83+84+85+68+69+70+71+72 & chain A")
cmd.load_cgo( [9.0, 30.80841,30.765274,2.9982393, -0.81417084, 13.692158, 2.998268, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
