from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RLC.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 6+6+7+8+9+10+11+12+13+14+15+27+28+29+30+31+32+33+34+35+36+41+42+43+44+45+46+47+48+49+50+51+65+66+67+68+69+70+71+72+73+74+75+76+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100+105+106+107+108+109+110+111+112+113+114+115+116+117+118+119+120+121+122+127+128+129+130+131+132+133+134+135+136+137+138+149+150+151+152+153+154+155+156+157+158+159 & chain A")
cmd.load_cgo( [9.0, -18.043308,-8.210648,17.934948, 37.3477, 7.0134516, 24.639385, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
