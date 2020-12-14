from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5IV9.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 208+209+210+211+212 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 216+217+218+219+220+223+224+225+226+227+228 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 231+232+233+234+235+236+237+238+239+240 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 245+246+247+248+249+250+251+252+253+254+255+256 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 259+260+261+262+263+264+265+266+267+268 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 286+287+288+289+290+291+292+293+294+295+296+297 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 301+302+303+304+305+306+307+308+309+310 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 330+331+332+333+334+335+336+337+338+339+340 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 344+345+346+347+348+349+350+351+352+353+354+355 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 364+365+366+367+368+369+370+371+372+373+374+375+376+377+378+379 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 382+383+384+385+386+387+388+389+390+391+392+393+394+395 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 402+403+404+405+406+407+408+409+410+411+412+413+414+415+416+417 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 453+454+455+456+457+458+459+460+461+462+463+464+465+466+467+468+469+470+471+472 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 421+422+423+424+425+426+427+428+429+430+431+432+433+434+435+436+437 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 478+479+480+481+482+483+484+485+486+487+488+489 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 529+530+531+532+533+534+535+536+537+538+539+540 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 546+547+548+549+550+551+552+553+554+555+556+557 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 577+578+579+580+581+582+583+584+585+586+587 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 595+596+597+598+599+600+601+602 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 607+608+609+610+611+612+613+614+615+616+617 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 625+626+627+628+629+630+631+632 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 654+655+656+657+658+659+660+661 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 672+673+674+675+676+677+678 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 684+685+686+687+688+689+690+691+692+693+694 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 699+700+701+702+703+704+705+706+707+708+709+710+711+712 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 719+720+721+722+723+724+725+726+727+728+729+730+731 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
