from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2Y0L.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 21+22+23+24+25+26+27+28+29+30+31+32+33 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 388+389+390+391+392+393+394+395+396+397+398+399+400 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 372+373+374+375+376+377+378+379+380+381+382 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 352+353+354+355+356+357+358+359+360+361+362 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 329+330+331+332+333+334+335+336+337+338+339 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 311+312+313+314+315+316+317+318+319+320 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 271+272+273+274+275+276+277+278+279+280+281 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 256+257+258+259+260+261+262+263+264+265+266+267+268 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 234+235+236+237+238+239+240+241+242+243+244+245+246 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 217+218+219+220+221+222+223+224+225+226+227+228+229 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 204+205+206+207+208+209+210+211+212+213 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 191+192+193+194+195+196+197+198 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 153+154+155+156+157+158+159+160+161+162+163+164 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 62+63+111+110+64+109+65+108+107+66+147+145+146+67+106+144+143+105+68+142+104+141+69+140+103+70+139+102+71+101+72+100+73+99+74+75+98+97+76+77+78 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 42+43+44+45+46+47+48+49+50+51+121+52+120+119+118+117+116+115+114 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
