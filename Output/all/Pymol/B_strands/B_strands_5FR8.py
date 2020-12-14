from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5FR8.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 362+363+364+365+366+305+367+306+307+368+308+369+309+247+370+248+525+310+527+523+526+524+529+528+249+371+530+531+250+311+522+532+372+312+533+251+596+594+252+534+198+598+199+595+597+373+313+201+200+593+599+592+535+600+536+253+314+601+374+602+603+164+254+202+591+203+537+604+605+315+165+375+166+255+637+639+316+635+204+638+256+636+538+640+641+633+376+205+634+167+168+691+257+317+632+693+690+258+692+206+207+169+377+318+170+697+695+694+696+498+171+259+208+209+172+319+260+497+320+173+261+174+496+545+495+546+547+548+549+550 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 561+562+563+564+565+481+566+482+480+479+567+568+569+570+340+571+572+342+341+343+573+287+344+506+574+288+345+575+289+507+346+290+576+508+291+347+229+230+577+292+348+509+231+293+232+510+578+349+233+294+234+579+350+511+618+295+182+619+235+675+512+236+580+351+183+296+676+184+581+677+620+721+352+297+237+621+513+185+186+238+582+678+723+722+298+353+514+679+187+583+622+239+188+299+724+725+354+623+240+515+680+189+584+300+726+516+681+355+241+190+727+624+585+301+242+728+356+243+625+517+191+682+683+302+193+357+586+192+244+518+358+684+626+587+194+627+588 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 456+457+458+459+460+461+462+463+464+465+466+467 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 439+440+441+442+443+444+445+446+447+448+449+450+451 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 424+425+426+427+428+429+430+431+432+433+434+435 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 404+405+406+407+408+409+410+411+412+413+414+415+416+417+418+419 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")