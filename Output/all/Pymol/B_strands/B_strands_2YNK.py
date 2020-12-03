from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2YNK.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 92+93+94+95+96+97+98+99 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 130+131+132+133+134+135+136+137+138+139+140+141+142 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 446+447+448+449+450+451+452+453+454+455+456 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 429+430+431+432+433+434+435+436+437+438+439+440+441+442+443 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 404+405+406+407+408+409+410+411+412+413+414 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 249+250+251+252+253+254+255+256+257+258+259 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 289+290+291+292+293+294+295+296+297+298+299 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 308+309+310+311+312+313+314+315+316+317+318+319+320 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 323+324+325+326+327+328+329+330+331+332+333+334+335+336+337+338 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 235+236+237+238+239+240+241+242+243+244+245+246 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 343+344+345+346+347+348+349+350+351+352 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 216+217+218+219+220+221+222+223+224 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 389+390+391+392+393+394+395+396+397+398 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 193+194+195+196+197+198+199 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 164+165+166+167+168+169+170 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 156+157+158+159+160+161 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 115+116+117+118+119+120+121+122+123+124+125+126+127 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 465+466+467+468+469+470+471+472+473+474+475 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
