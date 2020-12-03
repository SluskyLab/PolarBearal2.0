from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3PDF.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 14+14+15+16+17+18+19+20+36+37+38+39+40+41+42+43+44+45+49+50+51+52+57+58+59+60+61+62+63+67+68+69+70+71+72+75+76+77+78+79+80+100+101+102+103+109+110+111+112+113+114+115+116 & chain A")
cmd.load_cgo( [9.0, 63.257294,28.120123,18.429258, 40.360825, 3.4195309, 18.429281, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
