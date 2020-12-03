from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SZV.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7+8+9+10+11+12+13+14+15+16+17+18+19+20+21 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 370+371+372+373+374+375+376+377+378+379+380+381+382+383 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 354+355+356+357+358+359+360+361+362+363+364 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 329+330+331+332+333+334+335+336+337+338+339+340+341+342+343+344 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 312+313+314+315+316+317+318+319+320+321+322+323+324+325+326 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 294+295+296+297+298+299+300+301+302+303 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 254+255+256+257+258+259+260+261+262+263+264 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 239+240+241+242+243+244+245+246+247+248+249+250+251 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 219+220+221+222+223+224+225+226+227+228+229+230+231 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 201+202+203+204+205+206+207+208+209+210+211+212+213 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 188+189+190+191+192+193+194+195+196+197 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 175+176+177+178+179+180+181+182+183 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 142+143+144+145+146+147+148+149+150+151+152+153 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 128+129+130+131+132+133+134+135+136+137+138+139 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 103+104+105+106+107+108+109+110 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 89+90+91+92+93+94+95+96+97+98+99+100 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 50+51+52+53+54+55+56+57+58+59+60+61+62+63+64 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 32+33+34+35+36+37+38+39+40+41+42 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
