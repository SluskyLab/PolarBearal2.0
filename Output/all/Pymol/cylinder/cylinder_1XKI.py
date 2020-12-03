from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1XKI.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 15+15+16+17+18+19+20+21+22+23+24+39+40+41+42+43+49+50+51+52+53+54+55+62+63+64+65+66+67+68+69+70+76+77+78+79+84+85+86+87+88+89+90+96+97+98+99+100+101+102+103+110+111+112+113+114+115+116+117+143+144+145 & chain A")
cmd.load_cgo( [9.0, 16.759594,55.12872,6.252901, 28.310078, 16.413181, -1.1075895, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
