from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2FR2.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 17+17+18+19+20+21+22+23+24+25+33+34+35+36+37+38+39+40+41+42+43+48+49+50+51+52+53+54+55+56+57+63+64+65+66+67+68+69+70+71+72+73+78+79+80+81+82+83+84+85+89+90+91+92+93+94+95+96+97+98+99+100+103+104+105+106+107+108+109+115+116+117+118+125+126+127+128+129+130+131+132+133+134+135+138+139+140+141+142+143+144+145+146+147+150+151+152+153+154+155+156+157+158+159+160+161+162 & chain A")
cmd.load_cgo( [9.0, 24.843887,38.15378,15.26758, -12.35466, 13.472711, 18.44206, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
