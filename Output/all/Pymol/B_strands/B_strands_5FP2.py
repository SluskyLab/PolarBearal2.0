from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5FP2.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 163+164+165+166+167+168+169+170+171+172+173 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 705+706+707+708+709+710+711+712+713 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 671+672+673+674+675+676+677+678 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 656+657+658+659+660+661+662+663+664+665+666 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 622+623+624+625+626+627+628+629+630+631 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 607+608+609+610+611+612+613+614+615+616 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 581+582+583+584+585+586+587+588+589+590+591+592 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 564+565+566+567+568+569+570+571+572+573+574+575+576+577+578 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 524+525+526+527+528+529+530+531+532+533+534+535 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 508+509+510+511+512+513+514+515+516+517+518+519+520+521 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 457+458+459+460+461+462+463+464+465+466+467+468 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 440+441+442+443+444+445+446+447+448+449+450+451+452 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 425+426+427+428+364+429+365+366+430+367+431+368+306+432+307+369+308+433+309+370+434+371+310+311+249+435+250+372+436+251+373+312+252+313+374+254+253+314+375+315+255+256+376+316+258+257+317+377+259+260+318+319+378+261+320 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 232+233+234+289+235+290+236+291+292+237+342+293+343+238+344+294+345+239+346+295+347+240+296+348+405+406+349+241+407+297+408+298+242+350+409+410+351+299+243+411+300+352+412+353+244+413+414+301+245+354+416+355+415+302+246+418+417+356+303+357+419+420+358+421+422 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 196+197+198+199+200+201+202+203+204+205+206+207 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 181+182+183+184+185+186+187+188+189+190+191 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
