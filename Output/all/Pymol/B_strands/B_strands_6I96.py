from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6I96.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 291+292+293+294+295+296+297+298+299 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 811+812+813+814+815+816+817+818+819 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 780+781+782+783+784+785+786+787 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 761+762+763+764+765+766+767+768+769+770+771 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 736+737+738+739+740+741+742+743+744+745 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 718+719+720+721+722+723+724+725+726+727 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 687+688+689+690+691+692+693+694+695+696+697+698+699+700+701+702 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 665+666+667+668+669+670+671+672+673+674+675+676+677+678+679+680+681+682+683 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 622+623+624+625+626+627+628+629+630+631+632+633 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 596+597+598+599+600+601+602+603+604+605+606+607 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 641+642+643+644+645+646+647+648+649+650+651+652+653+654+655+656 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 574+575+576+577+578+579+580+581+582+583+584+585+586+587+588+589+590 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 551+552+553+554+555+556+557+558+559+560+561+562+563+564+565+566+567+568 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 529+530+531+532+533+534+535+536+537+538+539+540+541+542+543+544+545+546+547+548 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 484+485+486+487+488+489+490+491+492+493+494+495+496+497+498+499+500+501+502+503+504+505+506+507+508+509+510+511+512 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 454+455+456+457+458+459+460+461+462+463+464+465+466+467+468+469+470+471+472+473+474+475+476+477+478+479+480+481 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 424+425+426+427+428+429+430+431+432+433+434+435+436+437+438+439+440+441+442+443+444+445+446+447 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 404+405+406+407+408+409+410+411+412+413+414+415+416+417+418+419 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 357+358+359+360+361+362+363+364+365+366+367+368+369+370+371 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 339+340+341+342+343+344+345+346+347+348+349+350+351+352+353+354 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 320+321+322+323+324+325+326+327+328+329+330+331+332 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 304+305+306+307+308+309+310+311+312+313 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
