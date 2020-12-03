from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4GGR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 11+11+12+13+14+20+21+22+23+24+25+30+31+32+33+34+35+36+48+49+50+51+52+53+54+55+56+59+60+61+62+63+64+65+66+71+72+73+74+75+76+77+83+84+85+86+87+88+89+90+91+92+93+99+100+101+102+103+104+105+106+107+108+109+110+111 & chain A")
cmd.load_cgo( [9.0, 21.9043,-8.681815,9.482131, 4.614376, 13.358062, -25.373116, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
