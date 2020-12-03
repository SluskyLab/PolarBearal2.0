from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1PRN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 2+3+4+5+6+7+8+9+10+11+12+13+14+15+16 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 25+26+27+28+29+30+31+32+33+34+35+36+37+38+39+40+41 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 45+46+47+48+49+50+51+52+53+54+55+56 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 69+70+71+72+73+74+75 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 78+79+80+81+82+83+84 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 131+132+133+134+135+136+137+138+139 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 142+143+144+145+146+147+148+149+150 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 163+164+165+166+193+194+167+195+168+196+169+222+223+197+170+224+244+245+225+198+243+242+171+199+226+227+241+240+172+200+228+239+238+201+229+237+230+236+231+235+234+232+233 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 261+260+259+258+257+256+255+206+207+254+208+209+253+176+175+210+252+211+177+178+212+179+213+180+181+214+182+183 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 265+266+267+268+269+270+271+272+273+274 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 278+279+280+281+282+283+284+285+286+287+288 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
