from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5LDV.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 13+14+15+16+17+18+19+20+21+22+23+24+25+26+27+28 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 395+396+397+398+399+400+401+402+403+404+405+406+407 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 374+375+376+377+378+379+380+381+382+383+384+385 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 357+358+359+360+361+362+363+364+365+366+367+368+369 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 335+336+337+338+339+340+341+342+343+344+345+346+347 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 316+317+318+319+320+321+322+323+324+325+326+327+328+329+330+331 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 270+271+272+273+274+275+276+277+278+279+280+281+282+283+284+285+286 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 256+257+258+259+260+261+262+263+264+265+266+267 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 231+232+233+234+235+236+237+238+239+240+241+242+243 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 213+214+215+216+217+218+219+220+221+222+223+224 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 198+199+200+201+202+203+204+205+206+207+208+209 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 184+185+186+187+188+189+190+191+192+193+194 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 140+141+142+143+144+145+146+147+148+149+150 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 126+127+128+129+130+131+132+133+134 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 104+105+106+107+108+109+110+111+112 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 89+90+91+92+93+94+95+96+97+98+99 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 61+62+63+64+65+66+67+68+69+70+71+72+73 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
