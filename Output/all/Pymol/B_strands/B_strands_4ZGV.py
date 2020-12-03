from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4ZGV.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 211+212+213+214+215+216+217+218+219 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 248+249+250+251+252+253+254+255+256+257+258+259 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 264+265+266+267+268+269+270+271+272+273+274+275+276+277+278+279+280+281 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 286+287+288+289+290+291+292+293+294+295+296+297+298+299+300+301+302+303+304 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 310+311+312+313+314+315+316+317+320+321+322+323+324+325 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 333+334+335+336+337+338+339+340+341+342+343+344+345+346+347+348 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 354+355+356+357+358+359+360+361+362+363+364+365+366+367+368+369+370+371 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 411+412+413+414+415+416+417+418+419+420+421+422+423+424+425+426+427 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 436+437+438+439+440+441+442+443+444+445+446+447+448+449+450+451+452+453+454 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 500+501+502+503+504+505+506+507+508+509+510+511+512+513+514+515+516+517+518 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 522+523+524+525+526+527+528+529+530+531+532+533 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 538+539+540+541+542+543+544+545+546+547+548+549+550 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 557+558+559+560+561+562+563+564+565+566+567 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 615+616+617+618+619+620+621+622+623+624+625+626 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 630+631+632+633+634+635+636+637+638+639+640+641+642 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 666+667+668+669+670+671+672+673+674+675+676+677 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 687+688+689+690+691+692+693+694+695+696+697+698+699+700+701 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 738+739+740+741+742+743+744+745+746+747+748 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 753+754+755+756+757+758+759+760+761+762 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 805+806+807+808+809+810+811+812+813+814+815+816+817 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 823+824+825+826+827+828+829+830 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 859+860+861+862+863+864+865+866 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
