from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1QFT.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 30+30+31+32+33+34+133+134+135+136+137+138+119+120+121+122+123+124+107+108+109+110+111+112+113+114+115+116+97+98+99+100+101+102+78+79+80+81+82+83+84+85+86+87+62+63+64+65+66+67+68+69+50+51+52+53+54 & chain A")
cmd.load_cgo( [9.0, 68.09546,26.514542,24.231522, 69.76494, 61.528496, 17.054619, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
