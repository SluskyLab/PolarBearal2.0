from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3QLB.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 162+163+164+165+166+167+168+169+170 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 689+690+691+692+693+694+695+696+697 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 659+660+661+662+663+664+665+666 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 638+639+640+641+642+643+644+645+646+647+648 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 613+614+615+616+617+618+619+620+621+622 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 595+596+597+598+599+600+601+602+603+604 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 563+564+565+566+567+568+569+570+571+572+573+574+575+576+577 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 540+541+542+543+544+545+546+547+548+549+550+551+552+553+554+555+556+557+558 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 497+498+499+500+501+502+503+504+505+506+507+508 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 471+472+473+474+475+476+477+478+479+480+481+482 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 515+516+517+518+519+520+521+522+523+524+525+526+527+528+529+530+531+532 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 448+449+450+451+452+453+454+455+456+457+458+459+460+461+462+463+464+465 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 426+427+428+429+430+431+432+433+434+435+436+437+438+439+440+441+442+443 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 401+402+403+404+405+406+407+408+409+410+411+412+413+414+415+416+417+418+419+420+421+422 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 353+354+355+356+357+358+359+360+361+362+363+364+365+366+367+368+369+370+371+372+373+374+375+376+377+378+379+380+381 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 323+324+325+326+327+328+329+330+331+332+333+334+335+336+337+338+339+340+341+342+343+344+345+346 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 294+295+296+297+298+299+300+301+302+303+304+305+306+307+308+309+310+311+312+313+314+315+316+317 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 275+276+277+278+279+280+281+282+283+284+285+286+287+288+289 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 228+229+230+231+232+233+234+235+236+237+238+239+240 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 212+213+214+215+216+217+218+219+220+221+222 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 191+192+193+194+195+196+197+198+199+200+201 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 174+175+176+177+178+179+180+181+182+183+184 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
