from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4AIP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 185+186+187+188+189+190+191+192+193+194 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 733+734+735+736+737+738+739+740+741 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 702+703+704+705+648+649+706+650+651+707+652+708+600+653+601+709+654+602+603+655+656+604+605+657+606+658+607+608+609 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 582+583+584+585+586+587+588+589+590+635+591+636+685+592+637+686+687+593+638+688+594+639+689+595+640+690+691+641+596+692+693+642+597+643+694+695+644 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 548+549+550+551+552+553+554+555+556+557+558+559+560 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 532+533+534+535+536+537+538+539+540+541+542+543+544 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 495+496+497+498+499+500+501+502+503+504+505+506 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 475+476+477+478+479+480+481+482+483+484+485+486+487+488+489+490+491+492 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 455+456+457+458+459+460+461+462+463+464+465+466+467+468+469 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 438+439+440+441+442+443+444+445+446+447+448+449+450+451+452 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 376+377+378+379+324+323+380+325+326+381+327+382+328+383+329+384+330+385+331+386+332+333+387+334+388+335+389+336+390+337+338+339 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 302+303+304+305+355+306+356+357+307+358+308+359+309+360+310+361+311+362+312+363+313+364+314+365+315+366+316+367+368+317+369+318+370+371+372+373 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 264+265+266+267+268+269+270+271+272+273+274+275+276+277+278+279 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 246+247+248+249+250+251+252+253+254+255+256+257+258+259 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 212+213+214+215+216+217+218+219+220+221+222+223 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 198+199+200+201+202+203+204+205+206+207+208+209 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
