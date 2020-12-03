from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6SLJ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 239+240+241+242+243+244+245+246+247+248+249+250 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 329+330+331+332+333+334+335+336+337+338+339+340 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 345+346+347+348+349+350+351+352+353+354+355+356+357 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 365+366+367+368+369+370+371+372+373+374+375+376+377+378 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 383+384+385+386+387+388+389+390+391+392+393+394+395+396+397 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 455+456+457+458+459+460+461+462+463+464+465+466+467+468+469+470 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 476+477+478+479+480+481+482+483+484+485+486+487+488+489+490+491+492+493+494+495 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 507+508+509+510+511+512+513+514+515+516+517+520+521+522+523+524+525+526+527+528+529+530 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 535+536+537+538+539+540+541+542+543+544+545+546+547+548+549+550+551+552+553+554+555+556+557+558+559+560 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 581+582+583+584+585+586+587+588+589+590+591+592+593+594+595+596+597+598+599+600 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 604+605+606+607+608+609+610+611+612+613+614+615 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 624+625+626+627+628+629+630+631+632+633+634 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 647+648+649+650+651+652+653+654+655+656+657+658+659+660+661 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 698+699+700+701+702+703+704+705+706+707+708+709+710+711 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 716+717+718+719+720+721+722+723+724+725+726+727+728 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 751+752+753+754+755+756+757+758+759+760+761+762+763+764 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 774+775+776+777+778+779+780+781+782+783+784+785+786+787+788 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 864+865+866+867+868+869+870+871+872+873 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 877+878+879+880+881+882+883+884+885+886+887 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 946+947+948+949+950+951+952+953+954+955+956+957 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 971+972+973+974+975+976+977+978+979 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 1006+1007+1008+1009+1010+1011+1012+1013+1014+1015+1016 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
