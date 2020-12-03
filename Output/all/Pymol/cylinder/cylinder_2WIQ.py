from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2WIQ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 12+12+13+14+15+16+17+18+19+20+21+22+25+26+27+28+29+30+31+32+33+34+35+41+42+43+44+45+46+47+48+116+117+118+119+120+121+122+123+124+125+126+103+104+105+106+107+108+109+110+111+112+113+90+91+92+93+94+95+96+97+98+172+173+174+175+176+177+178+179+180+181+182+183+156+157+158+159+160+161+162+163+164+165+166+167+139+140+141+142+145+146+147+148+149+150+151+195+196+197+198+199+200+201+202+203+204+205+213+214+215+216+217+218+219+220+221+222+223 & chain A")
cmd.load_cgo( [9.0, 37.617214,12.068465,9.48206, -6.909588, 12.068381, 9.482144, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
