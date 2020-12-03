from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2MAF.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 7+7+8+9+10+11+12+13+14+15+55+56+57+58+59+60+61+62+65+66+67+68+69+70+71+115+116+117+118+119+120+121+122+123+124+131+132+133+134+135+136+137+138+139+140+141+142+191+192+193+194+195+196+197+198+199+200+201+206+207+208+209+210+211+212+230+231+232+233+234+235+236+237 & chain A")
cmd.load_cgo( [9.0, 47.191788,68.76225,24.831547, 67.75404, 51.895794, 57.91595, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
