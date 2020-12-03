from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1QJP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 6+6+7+8+9+10+11+12+13+14+15+16+34+35+36+37+38+39+40+41+42+43+44+45+46+49+50+51+52+53+54+55+56+57+58+59+60+72+73+74+75+76+77+78+79+80+81+82+83+84+85+86+91+92+93+94+95+96+97+98+99+100+101+102+103+104+105+106+107+113+114+115+116+117+118+119+120+121+122+123+124+125+126+127+128+129+130+131+132+135+136+137+138+139+140+141+142+143+144+161+162+163+164+165+166+167+168+169 & chain A")
cmd.load_cgo( [9.0, 32.209873,13.865134,8.817089, 22.894257, 26.116867, 64.44142, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
