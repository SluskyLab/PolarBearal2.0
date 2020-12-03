from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5DL5.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 14+15+16+17+18+19+20+21+22+23+24+25+26+27+28 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 401+402+403+404+405+406+407+408+409+410+411+412+413+414 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 379+380+381+382+383+384+385+386+387+388+389 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 354+355+356+357+358+359+360+361+362+363+364+365+366+367+368+369 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 336+337+338+339+340+341+342+343+344+345+346+347+348+349+350 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 317+318+319+320+321+322+323+324+325+326 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 274+275+276+277+278+279+280+281+282+283+284+285 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 258+259+260+261+262+263+264+265+266+267+268+269+270+271 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 218+219+220+221+222+223+224+225+226+227+228+229+230+231 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 201+202+203+204+205+206+207+208+209+210+211+212+213+214 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 188+189+190+191+192+193+194+195+196+197 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 175+176+177+178+179+180+181+182+183+184+185 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 145+146+147+148+149+150+151+152+153+154+155+156 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 131+132+133+134+135+136+137+138+139+140+141+142 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 106+107+108+109+110+111+112+113 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 91+92+93+94+95+96+97+98+99+100+101+102+103 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 55+56+57+58+59+60+61+62+63+64+65+66+67+68 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 35+36+37+38+39+40+41+42+43+44+45+46+47 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
