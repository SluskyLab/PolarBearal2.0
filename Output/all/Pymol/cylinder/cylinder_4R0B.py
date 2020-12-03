from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4R0B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 17+17+18+19+20+21+22+23+24+25+26+42+43+44+45+46+47+48+54+55+56+57+58+59+60+61+66+67+68+69+70+71+72+73+74+75+81+82+83+84+85+86+89+90+91+92+93+94+95+96+97+102+103+104+105+106+107+108+109+116+117+118+119+120+121+122+123+149+150+151+152 & chain A")
cmd.load_cgo( [9.0, -7.4611425,39.940704,-2.1408312, -16.2168, 3.6576138, -7.318055, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
