from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3KVN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 347+348+349+350+351+352+353+354+355+356+357+358+359+360 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 369+370+371+372+373+374+375+376+377+378+379+380+381+382+383 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 388+389+390+391+392+393+394+395+396+397+398+399+400+401+402+403 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 408+409+410+411+412+413+414+415+416+417+418+419+420+421+422+423+424+425 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 428+429+430+431+432+433+434+435+436+437+438+439+440+441+442+443+444+445+446+447+448+449+450 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 453+454+455+456+457+458+459+460+461+462+463+464+465+466+467+468+469+470+471+472+473+474 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 484+485+486+487+488+489+490+491+492+493+494+495+496+497+498+499 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 517+518+519+520+521+522+523+524+525+526+527+528+529+530+531+532+533 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 538+539+540+541+542+543+544+545+546+547+548+549 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 579+580+581+582+583+584+585+586+587+588+589+590+591+592 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 595+596+597+598+599+600+601+602+603+604+605+606 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 609+610+611+612+613+614+615+616+617+618+619+620+621 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
