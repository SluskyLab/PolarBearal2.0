from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3KZA.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 17+17+18+19+20+21+22+23+24+25+26+42+43+44+45+46+47+48+54+55+56+57+58+59+69+70+71+72+73+74+75+81+82+83+84+85+86+89+90+91+92+93+94+95+96+97+102+103+104+105+106+107+108+118+119+120+121+122+123+147+148+149+150 & chain A")
cmd.load_cgo( [9.0, 18.285572,-25.676468,12.660846, 51.92143, -42.91198, 12.660865, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
