from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4Q35.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 230+230+231+232+233+234+235+236+242+243+244+245+246+247+248+249+250+251+252+255+256+257+258+259+260+261+262+263+264+269+270+271+272+273+274+275+276+277+278+279+280+284+285+286+287+288+289+290+291+292+293+294+295+310+311+312+313+314+315+316+317+318+319+320+321+326+327+328+329+330+331+332+333+334+335+336+354+355+356+357+358+359+360+361+362+363+364+365+368+369+370+371+372+373+374+375+376+377+378+379+387+388+389+390+391+392+393+394+395+396+397+398+399+400+406+407+408+409+410+411+412+413+414+415+416+417+418+419+424+425+426+427+428+429+430+431+432+433+434+435+436+437+438+439+440+441+442+445+446+447+448+449+450+451+452+453+454+455+456+457+458+459+460+461+470+471+472+473+474+475+476+477+478+479+480+481+482+483+484+485+486+487+488+489+490+491+492+493+494+495+496+497+505+506+507+508+509+510+511+512+513+514+515+516+517+518+519+520+555+556+557+558+559+560+561+562+563+564+565+566+567+568+575+576+577+578+579+580+581+582+583+584+585+586+587+588+589+603+604+605+606+607+608+609+610+611+612+613+614+615+616+617+620+621+622+623+624+625+626+627+628+629+637+638+639+640+641+642+643+644+645+646+647+650+651+652+653+654+655+656+657+658+659+682+683+684+685+686+687+688+689+690+691+692+693+697+698+699+700+701+702+703+704+705+706+714+715+716+717+718+719+720+721+722+723+726+727+728+729+730+731+732+733+734+735+745+746+747+748+749+750+751+752+753+754+755+756+757+758+759+738+739+740 & chain A")
cmd.load_cgo( [9.0, 81.79397,17.497322,52.49591, 36.026688, 42.809723, -9.193596, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
