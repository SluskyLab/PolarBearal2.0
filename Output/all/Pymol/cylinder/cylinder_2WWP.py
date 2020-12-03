from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2WWP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 41+41+42+43+44+45+46+47+48+49+50+65+66+67+68+69+70+71+77+78+79+80+81+82+83+84+85+88+89+90+91+92+93+94+95+96+97+98+104+105+106+107+108+109+114+115+116+117+118+119+120+121+122+123+128+129+130+131+132+133+134+135+136+137+144+145+146+147+148+149+150+177+178+179 & chain A")
cmd.load_cgo( [9.0, 26.182804,-32.530624,6.2354856, 7.5134706, 10.483965, 4.1965966, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
