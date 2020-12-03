from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2X55.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 14+15+16+17+18+19+20+21+22+23+24+25+26+27+28+29+30+31+32 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 275+276+277+278+279+280+281+282+283+284+285+286+287+288+289+290+291+292 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 239+240+241+242+243+244+245+246+247+248+249+250 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 65+66+67+68+69+70+71+72+73+74 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 126+127+128+129+130+131+132+133+134+135+136+137+138+139+140+141+142+143+144 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 164+165+166+167+168+169+170+171+172+173+174+175+176+177+178+179+180+181+182+183+184+185 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 188+189+190+191+192+193+194+195+196+197+198+199+200+201+202+203+204+205+206+207+208 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 213+214+215+216+217+218+219+220+221+222+223+224+225+226+227+228+229+230+231+232+233+234+235+236 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 97+98+99+100+101+102+103+104+105+106+107+108+109+110+111+112+113+114+115+116+117+118+119+120+121+122 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 39+40+41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
