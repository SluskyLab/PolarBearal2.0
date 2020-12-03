from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4RDR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 148+149+150+151+152+153+154+155+156+157 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 725+726+727+728+729+730+731+732+733 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 694+695+696+697+698+699+700+701+702 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 677+678+679+680+681+682+683+684+685+686+687+688+689 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 653+654+655+656+657+658+659+660+661 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 496+497+498+499+639+640+641+642+643+644+645+646+647 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 593+594+595+596+531+532+597+533+598+534+599+535+475+600+476+536+477+601+537+478+602+538+479+418+480+603+419+539+420+481+604+540+421+482+422+605+423+541+483+484+542+424+606+425+486+545+485+543+607+547+546+548+426+544+427+504+549+506+550+428+429+505+507+430+431+432 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 397+398+399+400+401+402+570+571+569+456+568+403+572+567+457+404+458+573+515+459+405+460+574+406+516+575+576+517+461+462+407+577+578+408+518+519+463+579+409+464+580+520+410+521+465+581+582+466+411+522+583+523+412+467+584+468+524+525+413+585+469+414+526+586+470+527+415+587+528+588+589+590 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 369+370+371+372+373+374+375+376+377+378+379+380+381+382+383+384+385+386 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 345+346+347+348+349+350+351+352+353+354+355+356+357+358+359+360+361+362+363 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 324+325+326+327+328+329+330+331+332+333+334+335+336+337+338+339+340+341+342 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 302+303+304+305+306+307+308+309+310+311+312+313+314+315+316+317 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 223+224+225+226+227+228+229+230+231+232+233+234+235+236+237 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 207+208+209+210+211+212+213+214+215+216+217+218 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 177+178+179+180+181+182+183+184+185+186+187+188 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 163+164+165+166+167+168+169+170+171+172 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
