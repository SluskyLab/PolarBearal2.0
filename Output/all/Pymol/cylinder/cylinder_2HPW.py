from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2HPW.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 15+15+16+17+18+19+20+21+22+23+24+25+28+29+30+31+32+33+34+35+36+37+38+39+44+45+46+47+48+49+50+51+119+120+121+122+123+124+125+126+127+128+129+106+107+108+109+110+111+112+113+114+115+116+93+94+95+96+97+98+99+100+101+177+178+179+180+181+182+183+184+185+186+187+188+161+162+163+164+165+166+167+168+169+170+171+149+150+151+152+153+154+155+156+200+201+202+203+204+205+206+207+208+209+219+220+221+222+223+224+225+226+227+228+229 & chain A")
cmd.load_cgo( [9.0, -3.66752,-15.342332,-57.604946, 10.853556, -15.342406, -15.88953, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")