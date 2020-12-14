from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4ZGV.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 211+211+212+213+214+215+216+217+218+219+248+249+250+251+252+253+254+255+256+257+258+259+264+265+266+267+268+269+270+271+272+273+274+275+276+277+278+279+280+281+286+287+288+289+290+291+292+293+294+295+296+297+298+299+300+301+302+303+304+310+311+312+313+314+315+316+317+320+321+322+323+324+325+333+334+335+336+337+338+339+340+341+342+343+344+345+346+347+348+354+355+356+357+358+359+360+361+362+363+364+365+366+367+368+369+370+371+411+412+413+414+415+416+417+418+419+420+421+422+423+424+425+426+427+436+437+438+439+440+441+442+443+444+445+446+447+448+449+450+451+452+453+454+500+501+502+503+504+505+506+507+508+509+510+511+512+513+514+515+516+517+518+522+523+524+525+526+527+528+529+530+531+532+533+538+539+540+541+542+543+544+545+546+547+548+549+550+557+558+559+560+561+562+563+564+565+566+567+615+616+617+618+619+620+621+622+623+624+625+626+630+631+632+633+634+635+636+637+638+639+640+641+642+666+667+668+669+670+671+672+673+674+675+676+677+687+688+689+690+691+692+693+694+695+696+697+698+699+700+701+738+739+740+741+742+743+744+745+746+747+748+753+754+755+756+757+758+759+760+761+762+805+806+807+808+809+810+811+812+813+814+815+816+817+823+824+825+826+827+828+829+830+859+860+861+862+863+864+865+866 & chain A")
cmd.load_cgo( [9.0, 53.216793,56.648415,47.084297, 3.9115372, -11.750069, 41.287476, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")