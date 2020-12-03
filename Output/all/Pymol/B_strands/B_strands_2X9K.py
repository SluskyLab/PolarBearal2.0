from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2X9K.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7+8+9+10+11+12+13+14+15+16+17+18+19+20+21 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 268+269+270+271+272+273+274+275+276+277+278+279 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 248+249+250+251+252+253+254+255+256+257+258+259 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 233+234+235+236+237+238+239+240+241+242+243 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 204+205+206+207+208+209+210+211+212+213+214+215+216+217+218 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 188+189+190+191+192+193+194+195+196 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 166+167+168+169+170+171+172+173+174+175+176+177 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 149+150+151+152+153+154+155+156+157+158+159+160 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 126+127+128+129+130+131+132+133+134+135+136+137+138 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 106+107+108+109+110+111+112+113+114+115+116+117+118+119+120+121 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 83+84+85+86+87+88+89+90+91+92+93+94+95+96+97 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 65+66+67+68+69+70+71+72+73+74+75+76+77+78+79 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 43+44+45+46+47+48+49+50+51+52+53+54 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 24+25+26+27+28+29+30+31+32+33+34+35+36+37+38+39 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
