from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3FHH.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 135+136+137+138+139+140+141+142+143+144+145+146 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 151+152+153+154+155+156+157+158+159+160+161+162 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 165+166+167+168+169+170+171+172+173+174+175+176+177+178+179+180+181 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 185+186+187+188+189+190+191+192+193+194+195+196+197+198+199+200+201+202 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 208+209+210+211+212+213+214+215+216+217+218+219+220+221+222+223 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 240+241+242+243+244+245+246+247+248+249+250+251+252+253+254+255+256 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 263+264+265+266+267+268+269+270+271+272+273+274+275+276+277+278 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 287+288+289+290+291+292+293+294+295+296+297+298+299+300+301+302+303 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 307+308+309+310+311+312+313+314+315+316+317+318+319+320+321+322+323+324+325+326 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 341+342+343+344+345+346+347+348+349+350+351+352+353+354+355+356+357+358+359 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 432+431+430+429+496+497+498+499+500+501+502+503+504+505+506+507+508+509+510+511+512+513+514+515+516+517+518 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 470+471+472+473+474+475+476+477+478+479+480+481+482+483+442+441+439+440+438+437+436+435 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 385+386+387+388+389+390+391+392+393+394+395+396+397+398+399+400+401 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 404+405+406+407+408+409+410+411+412+413+414+415 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 362+363+364+365+366+367+368+369+370+371+372+373+374+375+376+377+378+379 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 446+447+448+449+450+451+452+453+454+455+456+457+458+459+460+461+462+463+464 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 521+522+523+524+525+526+527+528+529+530+531+532+533+487+488+489+490+491 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 539+540+541+542+543+544+545+548+549+550+551+552+553+554+555+556+557 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 562+563+564+565+566+567+568+569+570+571 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 587+588+589+590+591+592+593+594+595+596+597+598+599 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 605+606+607+608+609+610+611+612 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 630+631+632+633+634+635+636+637+638+639 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
