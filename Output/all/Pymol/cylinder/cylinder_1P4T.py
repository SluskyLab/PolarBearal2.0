from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1P4T.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 4+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+23+24+25+26+27+40+41+42+43+44+45+46+47+48+49+50+51+30+31+32+33+34+35+36+37+60+61+62+63+64+65+66+67+68+69+70+71+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+98+99+100+101+105+106+107+108+109+110+111+112+113+114+115+116+117+118+119+122+123+124+125+126+127+128+129+130+131+132+133+134+135+136+139+140+141+142+143+144+145+146+147+148+149+150+151+152+153+154 & chain A")
cmd.load_cgo( [9.0, 8.30695,16.932535,29.549078, 66.036194, 16.932615, 35.702225, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")