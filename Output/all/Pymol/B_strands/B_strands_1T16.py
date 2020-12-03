from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1T16.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 402+403+404+405+406+407+408+409+410+411+412+413+414+415+416+417+418+419+420 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 381+382+383+384+385+386+387+388+389+390+391+392+395+396+397+399+398 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 313+314+315+316+317+318+324+325+326+327+328+329+330+331+332+333 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 140+141+142+143+144+145+146+147+148+149+150+151+152+153+154+155+156+157+158 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 287+288+289+290+291+292+293+294+295+296+303+304+305+306+307 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 196+197+198+199+200+201+202+203+204+205+206+207+208+209+210+211+212+213+214+215+216+217+218 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 221+222+223+224+225+226+227+228+231+232+233+234+235+236+237+238+239+240 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 263+264+265+266+267+268+269+270+271+274+275+276+277+278+279+280+281+282+283+284 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 120+121+122+123+124+125+126+127+128+129+130+131+132+133+134 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 92+93+94+95+96+97+98+99+104+105+106+107 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 77+78+79+80+81+82+83+84+85+86+87 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 339+340+341+342+343+344+345+346+347+348 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 366+367+368+369+370+371+372+373+374+375+376 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
