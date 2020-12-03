from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1QJ8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 2+2+3+4+5+6+7+8+9+10+11+12+13+14+21+22+23+24+25+26+27+28+29+30+31+37+38+39+40+41+42+43+44+45+46+47+48+49+50+51+57+58+59+60+61+62+63+64+65+66+67+68+69+70+71+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+98+99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114+115+121+122+123+124+125+126+127+128+129+130+131+132+135+136+137+138+139+140+141+142+143+144+145+146+147 & chain A")
cmd.load_cgo( [9.0, 28.49672,14.613681,65.91403, 82.70521, 14.613866, 29.388147, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
