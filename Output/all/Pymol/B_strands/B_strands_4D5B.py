from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4D5B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 22+23+24+25+26+27+28+29+30+31+32+33+34+35+36+37 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 65+66+67+68+69+70+71+72+73+74+75+76+77+78+79+80 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100+101+102+103 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 106+107+108+109+110+111+112+113+114+115+116+117+118+119+120+121+122 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 127+128+129+130+131+132+133+134+135+136+137+138+139+140+141+142+143+144+145+146 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 151+152+153+154+155+156+157+158+159+160+161+162+163+164+165 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 190+191+192+193+194+195+196+197+198+199+200+201+202+203+204+205+206 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 171+172+173+174+175+176+177+178+179+180+181+182+183+184+185+186+187 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 212+213+214+215+216+217+218+219+220+221+222+223+224+225+226+227+228+229+230 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 236+237+238+239+240+241+242+243+244+245+246+247+248+249+250 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 262+263+264+265+266+267+268+269+270+271+272+273+274+275+276+277+278 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 282+283+284+285+286+287+288+289+290+291+292+293+294+295+296+297 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 309+310+311+312+313+314+315+316+317+318+319+320+321+322+323 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
