from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SYB.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 150+149+148+147+146+145+90+144+43+89+143+88+44+45+142+141+87+86+46+47+140+85+48+139+84+49+426+138+83+427+50+428+51+137+82+429+52+430+81+53+80+431+432+54+79+55+434+78+433+435+436+56+77 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 153+154+155+98+156+99+100+101+157+102+160+103+158+159+104+105+106+457+107+455+456+454+453+108+109+452+451+110+450+449+111+448+447+445+446 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 178+179+180+181+182+183+184+185+186+187+188+189 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 192+193+194+195+196+197+198+199+200+201+202+203 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 227+228+229+230+231+232+233+234+235+236+237 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 240+241+242+243+244+245+246+247+248+249 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 253+254+255+256+257+258+259+260+261+262+263+264 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 272+273+274+275+276+277+278+279+280+281+282+283+284 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 294+295+296+297+298+299+300+301+302+303+304+305+306 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 309+310+311+312+313+314+315+316+317+318+319 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 349+350+351+352+353+354+355+356+357+358 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 367+368+369+370+371+372+373+374+375+376+377+378+379+380 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 402+403+404+405+406+407+408+409+410+411+412+413+414+415+416 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
