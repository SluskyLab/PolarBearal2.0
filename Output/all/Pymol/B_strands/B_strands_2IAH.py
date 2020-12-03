from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2IAH.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 278+279+280+281+282+283+284+285+286 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 806+807+808+809+810+811+812 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 776+777+778+779+780+781+782 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 760+761+762+763+764+765+766+767+768+769+770 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 728+729+730+731+732+733+734+735+736+737 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 711+712+713+714+715+716+717+718+719+720 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 685+686+687+688+689+690+691+692+693 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 664+665+666+667+668+669+670+671+672+673+674+675+676+677+678+679+680+681+682 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 611+612+613+614+615+616+617+618+619+620+621+622+623+624 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 629+630+631+632+633+634+635+636+637+638+639+640+641+642+643+644+645 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 583+584+585+586+587+588+589+590+591+592+593+594 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 563+564+565+566+567+568+569+570+571+572+573+574+575+576+577+578 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 543+544+545+546+547+548+549+550+551+552+553+554+555+556+557+558 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 520+521+522+523+524+525+526+527+528+529+530+531+532+533+534+535+536+537 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 471+472+473+474+475+476+477+478+479+480+481+482+483+484+485+486+487+488+489+490 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 441+442+443+444+445+446+447+448+449+450+451+452+453+454+455+456+457+458+459+460+461+462+463+464+465+466 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 411+412+413+414+415+416+417+418+419+420+421+422+423+424+425+426+427+428+429+430 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 392+393+394+395+396+397+398+399+400+401+402+403+404+405 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 344+345+346+347+348+349+350+351+352+353+354+355+356+357+358 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 326+327+328+329+330+331+332+333+334+335+336+337+338+339+340+341 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 307+308+309+310+311+312+313+314+315+316+317+318+319 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 290+291+292+293+294+295+296+297+298+299+300 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
