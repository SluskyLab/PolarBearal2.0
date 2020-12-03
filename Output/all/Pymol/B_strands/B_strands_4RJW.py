from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RJW.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 10+11+12+13+380+381+382+383+384+385+386+387+388+389+390+391+392 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 402+403+404+405+406+407+408+409+410+411+412+413+18+19+20+21+22 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 28+29+30+31+32+33+34+35+36+37+38+39+40+41+42 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 53+54+55+56+57+58+59+60+61+62+63+64+65+66+67+68+69 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 73+74+75+76+77+78+79+80 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 93+94+95+96+97+98+99+100 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 107+108+109+110+111+112 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 150+151+152+153+154+155+156+157+158 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 162+163+164+165+166+167+168+169+170+171+172+173+174 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 180+181+182+183+184+185+186+187+188+189+190+191+192+193+194+195 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 198+199+200+201+202+203+204+205+206+207+208+209+210 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 257+258+259+260+261+262+263+264+265+266+267+268+269+270+271 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 274+275+276+277+278+279+280+281+282+283+284+285+286+287 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 295+296+297+298+299+300+301+302+303+304+305+306+307 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 334+335+336+337+338+339+340+341+342+343+344+345+346+347+348 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 363+364+365+366+367+368+369+370+371+372+373+374+375 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
