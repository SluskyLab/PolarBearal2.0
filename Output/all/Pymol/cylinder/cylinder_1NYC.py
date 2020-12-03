from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1NYC.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 2+2+3+4+5+6+7+8+9+10+38+39+40+41+42+43+44+45+29+30+31+32+33+103+104+105+106+107+86+87+88+89+90+91+92+93+72+73+74+75+76+77+78+79+80+81+82+83+64+65+66+67+68+69+52+53+54+55+56+57+58+59 & chain A")
cmd.load_cgo( [9.0, -10.114304,13.429864,8.601849, 19.019123, -10.481044, 8.601856, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
