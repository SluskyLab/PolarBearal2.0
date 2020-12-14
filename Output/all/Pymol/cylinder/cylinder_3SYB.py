from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3SYB.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 43+43+44+45+46+47+48+49+50+51+52+53+54+55+56+77+78+79+80+81+82+83+84+85+86+87+88+89+90+98+99+100+101+102+103+104+105+106+107+108+109+110+111+137+138+139+140+141+142+143+144+145+146+147+148+149+150+153+154+155+156+157+158+159+160+178+179+180+181+182+183+184+185+186+187+188+189+192+193+194+195+196+197+198+199+200+201+202+203+227+228+229+230+231+232+233+234+235+236+237+240+241+242+243+244+245+246+247+248+249+253+254+255+256+257+258+259+260+261+262+263+264+272+273+274+275+276+277+278+279+280+281+282+283+284+294+295+296+297+298+299+300+301+302+303+304+305+306+309+310+311+312+313+314+315+316+317+318+319+349+350+351+352+353+354+355+356+357+358+367+368+369+370+371+372+373+374+375+376+377+378+379+380+402+403+404+405+406+407+408+409+410+411+412+413+414+415+416+426+427+428+429+430+431+432+433+434+435+436+445+446+447+448+449+450+451+452+453+454+455+456+457 & chain A")
cmd.load_cgo( [9.0, 18.109634,50.127525,20.59311, 40.055214, 4.282467, -21.49339, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")