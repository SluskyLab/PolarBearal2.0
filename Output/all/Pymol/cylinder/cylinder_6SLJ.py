from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6SLJ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 239+239+240+241+242+243+244+245+246+247+248+249+250+329+330+331+332+333+334+335+336+337+338+339+340+345+346+347+348+349+350+351+352+353+354+355+356+357+365+366+367+368+369+370+371+372+373+374+375+376+377+378+383+384+385+386+387+388+389+390+391+392+393+394+395+396+397+455+456+457+458+459+460+461+462+463+464+465+466+467+468+469+470+476+477+478+479+480+481+482+483+484+485+486+487+488+489+490+491+492+493+494+495+507+508+509+510+511+512+513+514+515+516+517+520+521+522+523+524+525+526+527+528+529+530+535+536+537+538+539+540+541+542+543+544+545+546+547+548+549+550+551+552+553+554+555+556+557+558+559+560+581+582+583+584+585+586+587+588+589+590+591+592+593+594+595+596+597+598+599+600+604+605+606+607+608+609+610+611+612+613+614+615+624+625+626+627+628+629+630+631+632+633+634+647+648+649+650+651+652+653+654+655+656+657+658+659+660+661+698+699+700+701+702+703+704+705+706+707+708+709+710+711+716+717+718+719+720+721+722+723+724+725+726+727+728+751+752+753+754+755+756+757+758+759+760+761+762+763+764+774+775+776+777+778+779+780+781+782+783+784+785+786+787+788+864+865+866+867+868+869+870+871+872+873+877+878+879+880+881+882+883+884+885+886+887+946+947+948+949+950+951+952+953+954+955+956+957+971+972+973+974+975+976+977+978+979+983+984+985+1006+1007+1008+1009+1010+1011+1012+1013+1014+1015+1016 & chain A")
cmd.load_cgo( [9.0, 75.137985,80.21973,40.164062, -18.48608, 80.219574, 13.166608, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
