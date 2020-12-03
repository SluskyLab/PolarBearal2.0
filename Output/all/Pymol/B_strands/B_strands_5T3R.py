from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5T3R.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Dstrand0", "resi 212+213+214+215+216+217+218+219+220+221+222+223+224 & chain D ")
cmd.color ("red", "Dstrand0")


cmd.select("Dstrand1", "resi 1006+1007+1008+1009+1010+1011+1012+1013+1014+1015 & chain D ")
cmd.color ("green", "Dstrand1")


cmd.select("Dstrand2", "resi 972+973+974+975+976+977+978+979+980 & chain D ")
cmd.color ("orange", "Dstrand2")


cmd.select("Dstrand3", "resi 948+949+950+951+952+953+954+955+956+957+958+959 & chain D ")
cmd.color ("teal", "Dstrand3")


cmd.select("Dstrand4", "resi 872+873+874+875+876+877+878+879+880+881+882 & chain D ")
cmd.color ("yellow", "Dstrand4")


cmd.select("Dstrand5", "resi 859+860+861+862+863+864+865+866+867+868+869 & chain D ")
cmd.color ("blue", "Dstrand5")


cmd.select("Dstrand6", "resi 761+762+763+764+765+766+767+768+769+770+771+772+773+774+775+776+777 & chain D ")
cmd.color ("red", "Dstrand6")


cmd.select("Dstrand7", "resi 740+741+742+743+744+745+746+747+748+749+750+751+752+753+754 & chain D ")
cmd.color ("green", "Dstrand7")


cmd.select("Dstrand8", "resi 704+705+706+707+708+709+710+711+712+713+714+715+716 & chain D ")
cmd.color ("orange", "Dstrand8")


cmd.select("Dstrand9", "resi 591+592+593+594+595+596+597+598+599 & chain D ")
cmd.color ("teal", "Dstrand9")


cmd.select("Dstrand10", "resi 686+687+688+689+690+691+692+693 & chain D ")
cmd.color ("yellow", "Dstrand10")


cmd.select("Dstrand11", "resi 620+621+622+623+624+625+626+627 & chain D ")
cmd.color ("blue", "Dstrand11")


cmd.select("Dstrand12", "resi 569+570+571+572+573+574+575+576+577+578+579+580 & chain D ")
cmd.color ("red", "Dstrand12")


cmd.select("Dstrand13", "resi 543+544+545+546+547+548+549+550+551+552+553+554+555+556+557+558+559+560+561+562+563+564 & chain D ")
cmd.color ("green", "Dstrand13")


cmd.select("Dstrand14", "resi 502+503+504+505+506+507+508+509+510+511+512+513+514+515+516+517+518+519+520+521+522+523+524 & chain D ")
cmd.color ("orange", "Dstrand14")


cmd.select("Dstrand15", "resi 475+476+477+478+479+480+481+482+483+484+485+486+487+488+489+490+491+492+493+494 & chain D ")
cmd.color ("teal", "Dstrand15")


cmd.select("Dstrand16", "resi 441+442+443+444+445+446+447+448+449+450+451+452+453+454+455+456+457+458+459+460 & chain D ")
cmd.color ("yellow", "Dstrand16")


cmd.select("Dstrand17", "resi 421+422+423+424+425+426+427+428+429+430+431+432+433+434+435 & chain D ")
cmd.color ("blue", "Dstrand17")


cmd.select("Dstrand18", "resi 357+358+359+360+361+362+363+364+365+366+367+368+369+370+371 & chain D ")
cmd.color ("red", "Dstrand18")


cmd.select("Dstrand19", "resi 339+340+341+342+343+344+345+346+347+348+349+350+351+352+353 & chain D ")
cmd.color ("green", "Dstrand19")


cmd.select("Dstrand20", "resi 319+320+321+322+323+324+325+326+327+328+329+330+331 & chain D ")
cmd.color ("orange", "Dstrand20")


cmd.select("Dstrand21", "resi 303+304+305+306+307+308+309+310+311+312+313+314+315 & chain D ")
cmd.color ("teal", "Dstrand21")


cmd.select("barrel", "Dstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
