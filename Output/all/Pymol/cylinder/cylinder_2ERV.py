from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2ERV.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 2+2+3+4+5+6+7+8+9+15+16+17+18+19+20+21+22+23+24+35+36+37+38+39+40+41+42+43+44+45+46+47+48+29+30+31+32+57+58+59+60+61+62+63+64+65+66+67+68+69+70+75+76+77+78+79+80+81+82+83+84+85+86+87+88+102+103+104+105+106+107+108+109+110+111+112+113+114+119+120+121+122+123+124+125+126+127+128+139+140+141+142+143+144+145+146+147+148+149 & chain A")
cmd.load_cgo( [9.0, 37.19153,22.04427,37.838745, -4.816181, 22.044239, 6.4263134, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
