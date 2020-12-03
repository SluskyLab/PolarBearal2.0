from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4FSO.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 7+8+9+10+11+12+13+14+15+16+17+18+19+20 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 35+36+37+38+39+40+41+42+43+44+45+116+115+46+114+47+113+112+111+110+109 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 134+135+136+99+62+97+98+64+137+63+100+61+101+96+138+95+65+60+139+66+102+59+94+103+67+140+141+58+104+57+105+142+56+106 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 148+149+150+151+152+153+154+155+156+157+158+159 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 187+188+189+190+191+192+193+194+195+196+197 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 200+201+202+203+204+205+206+207+208+209 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 213+214+215+216+217+218+219+220+221+222+223+224+225 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 230+231+232+233+234+235+236+237+238+239+240+241+242 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 252+253+254+255+256+257+258+259+260+261+262+263+264 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 267+268+269+270+271+272+273+274+275+276+277 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 307+308+309+310+311+312+313+314+315+316 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 325+326+327+328+329+330+331+332+333+334+335+336+337+338 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 344+345+346+347+348+349+350+351+352+353+354+355+356+357 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 367+368+369+370+371+372+373+374+375+376+377 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 386+387+388+389+390+391+392+393+394+395+396+397+398 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
