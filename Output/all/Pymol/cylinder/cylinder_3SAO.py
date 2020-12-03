from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SAO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 10+10+11+12+13+14+15+16+17+18+34+35+36+37+38+39+40+41+45+46+47+48+49+50+51+52+59+60+61+62+63+64+65+66+74+75+76+77+82+83+84+85+86+87+88+89+94+95+96+97+98+99+100+101+102+103+106+107+108+109+110+111+112+113+114+115+142+143+144 & chain A")
cmd.load_cgo( [9.0, -25.04977,17.247784,-31.598, -2.8844366, -7.22243, -6.0226183, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
