from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1UUN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 2+2+3+4+5+6+7+8+9+15+16+17+18+19+20+21+22+23+24+25+26+27+28+38+39+40+41+42+43+44+45+46+47+48+49+50+51+139+140+141+142+143+144+145+146+147+148+149+150+151+173+174+175+176+177+159+160+161+162+163+164+165+166+167+168+59+60+61+62+63+64+65+66+67+68+69+126+127+128+129+130+131+132+133+134+135+136 & chain B")
cmd.load_cgo( [9.0, 52.531075,26.482698,42.992813, -7.958214, 16.214605, 42.99288, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
