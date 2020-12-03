from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2F9H.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 4+4+5+6+7+8+9+10+11+12+40+41+42+43+23+24+25+26+27+84+85+86+87+102+103+104+105+106+63+64+65+66+67+68+69+70+57+58+59+60+118+119+120+121+122 & chain A")
cmd.load_cgo( [9.0, -12.67328,26.745577,10.420785, -27.222267, 40.44156, 36.016895, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
