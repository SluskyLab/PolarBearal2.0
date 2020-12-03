from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3FID.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 2+2+3+4+5+6+7+8+9+33+34+35+36+37+38+39+40+41+42+43+44+49+50+51+52+53+54+55+56+57+58+59+60+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+97+98+99+100+101+102+103+104+105+106+107+108+140+141+142+143+144+145+146+147+148+149+150+151+160+161+162+163+164+165+166+167+168+169+170+171+172+173+154+155+156+157+176+177+178+179+180+181+182+183+184+185+186+187+188+215+216+217+218+219+220+221+222+223+224+225+226+227+228+229+230+231+251+252+253+254+255+256+257+258+259+260+261+262+263+266+267+268+269+270+271+272+273+274+275+285+286+287+288+289+290+291+292+293+294+295 & chain A")
cmd.load_cgo( [9.0, 53.043198,21.751087,-13.199779, 19.84034, 17.552795, 33.079567, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
