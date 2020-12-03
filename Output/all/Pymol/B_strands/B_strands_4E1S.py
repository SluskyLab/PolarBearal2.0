from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4E1S.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 212+213+214+215+216+217+218+219 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 398+399+400+401+402+403+404+405+406+407+408+409+410 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 385+386+387+388+389+390+391+392+393+394 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 371+372+373+374+375+376+377+378+379+380+381+382 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 286+287+288+289+290+291+292+293+294+295+296+297 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 300+301+302+303+304+305+306+307+308+309 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 329+330+331+332+333+334+335+336+337+338 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 271+272+273+274+275+276+277+278+279+280+281 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 341+342+343+344+345+346+347+348+349+350+351+352+353 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 254+255+256+257+258+259+260+261+262+263+264+265+266 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 240+241+242+243+244+245+246+247+248+249+250+251 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 225+226+227+228+229+230+231+232+233+234+235+236 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
