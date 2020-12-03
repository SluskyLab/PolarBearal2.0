from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4GEY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 27+28+29+30+31+32+33+34+35+36+37+38+39+40+41+42 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 51+52+53+54+55+56+57+58+59+60+61+62+63+64 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 74+75+76+77+78+79+80+81+82+83+84+85 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 114+115+116+117+118+119+120+121+122+123+124+125 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 130+131+132+133+134+135+136+137 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 175+176+177+178+179+180+181+182+183+184+185 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 188+189+190+191+192+193+194+195+196+197 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 217+218+219+220+221+222+223+224+225+226 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 233+234+235+236+237+238+239+240+241+242+243+244 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 273+274+275+276+277+278+279+280+281+282+283 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 294+295+296+297+298+299+300+301+302+303+304 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 311+312+313+314+315+316+317+318+319+320+321+322 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 332+333+334+335+336+337+338+339+340+341+342 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 373+374+375+376+377+378+379+380+381+382+383+384 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 389+390+391+392+393+394+395+396+397+398+399 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 410+411+412+413+414+415+416+417+418+419+420 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
