from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1XQB.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 10+10+11+12+13+33+34+35+36+37+38+116+117+118+119+120+121+122+123+100+101+102+103+104+105+106+107+108+109+110+111+112+113+56+57+58+59+60+61+62+131+132+133+134+135+136+137 & chain A")
cmd.load_cgo( [9.0, 34.817635,15.224341,2.2401066, 14.762281, 18.480831, 32.792328, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
