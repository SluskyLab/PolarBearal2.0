from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2Q03.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 7+7+8+9+10+11+12+14+15+16+17+18+19+20+21+22+23+24+25+26+32+33+34+35+36+37+38+39+40+41+42+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+63+64+65+66+67+68+69+70+71+72+73+74+75+76+79+80+81+82+83+84+85+86+87+88+89+90+91+92+95+96+97+98+99+100+101+102+114+115+116+117+118+119+120+121+122+127+128+129+130+131+132+133+134+135+136 & chain A")
cmd.load_cgo( [9.0, 54.72145,41.166267,4.166143, 64.143585, -10.196129, 4.166137, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
