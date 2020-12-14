from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6I96.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 291+291+292+293+294+295+296+297+298+299+304+305+306+307+308+309+310+311+312+313+320+321+322+323+324+325+326+327+328+329+330+331+332+339+340+341+342+343+344+345+346+347+348+349+350+351+352+353+354+357+358+359+360+361+362+363+364+365+366+367+368+369+370+371+404+405+406+407+408+409+410+411+412+413+414+415+416+417+418+419+424+425+426+427+428+429+430+431+432+433+434+435+436+437+438+439+440+441+442+443+444+445+446+447+454+455+456+457+458+459+460+461+462+463+464+465+466+467+468+469+470+471+472+473+474+475+476+477+478+479+480+481+484+485+486+487+488+489+490+491+492+493+494+495+496+497+498+499+500+501+502+503+504+505+506+507+508+509+510+511+512+529+530+531+532+533+534+535+536+537+538+539+540+541+542+543+544+545+546+547+548+551+552+553+554+555+556+557+558+559+560+561+562+563+564+565+566+567+568+574+575+576+577+578+579+580+581+582+583+584+585+586+587+588+589+590+596+597+598+599+600+601+602+603+604+605+606+607+622+623+624+625+626+627+628+629+630+631+632+633+641+642+643+644+645+646+647+648+649+650+651+652+653+654+655+656+665+666+667+668+669+670+671+672+673+674+675+676+677+678+679+680+681+682+683+687+688+689+690+691+692+693+694+695+696+697+698+699+700+701+702+718+719+720+721+722+723+724+725+726+727+736+737+738+739+740+741+742+743+744+745+761+762+763+764+765+766+767+768+769+770+771+780+781+782+783+784+785+786+787+811+812+813+814+815+816+817+818+819 & chain A")
cmd.load_cgo( [9.0, -16.118881,19.392776,56.99115, -6.943509, 51.731926, -16.536142, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")