from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4ALO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 34+34+35+36+37+38+39+40+41+42+43+53+54+55+56+57+58+62+63+64+65+66+67+68+69+70+48+49+50+75+76+77+78+79+80+81+82+83+84+92+93+94+95+96+97+100+101+102+103+104+105+106+107+108+109+110+115+116+117+118+119+120+121+122+123+124+128+129+130+131+132+133+134+135+136+137+138+139+140+141+142+165+166+167+168+169 & chain A")
cmd.load_cgo( [9.0, -15.346137,3.1417344,18.787184, 19.741642, 3.48683, -15.833818, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
