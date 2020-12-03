from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6EHD.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 304+305+306+307+318+308+320+319+317+309+316+321+322+310+311+315+314+323+324+312+313+2+3+4+5+6 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 281+282+283+284+285+286+287+288+289+290+291+292+293+294+295+296+297+298+299 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 184+185+186+187+188+189+190+191+192+193+194+195+196+197+198+199+200+201+202+203+204+205 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 160+161+162+163+164+165+166+167+168+169+170+171+172+173+174+175+176+177+178+179+180+181 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 208+209+210+211+212+213+214+215+216+217+218+219+220+221 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 147+148+149+150+151+152+153+154+155+156+157 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 131+132+133+134+135+136+137+138 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 117+118+119+120+121+122+123+124+125+126+127+128 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 80+81+82+83+84+85+86+87+88 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 67+68+69+70+71+72+73+74+75+76+77 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 50+51+52+53+54+55+56+57+58+59 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 37+38+39+40+41+42+43+44+45+46+47 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 227+228+229+230+231+232+233+234+235+236+237+238+239+240+241+242 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 245+246+247+248+249+250+251+252+253+254+255+256+257+258 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 263+264+265+266+267+268+269+270+271+272+273+274+275+276+277+278 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 9+10+11+12+13+14+15+16+17+18+19+20+21+22+23+24 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
