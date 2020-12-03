from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2LHF.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 4+4+5+6+7+8+9+10+11+41+42+43+44+45+46+47+48+49+50+53+54+55+56+57+58+59+60+73+74+75+76+77+78+79+80+81+93+94+95+96+97+98+99+100+101+102+103+104+119+120+121+122+123+124+125+126+127+128+129+130+136+137+138+139+140+141+142+143+144+145+170+171+172+173+174+175+176+177+178 & chain A")
cmd.load_cgo( [9.0, -20.707165,-0.1903019,6.0731864, 20.529243, -14.3392105, -3.6434941, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
