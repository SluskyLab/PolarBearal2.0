from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4Q35.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 230+231+232+233+234+235+236 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 726+727+728+729+730+731+732+733+734+735 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 255+256+257+258+259+260+261+262+263+264 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 242+243+244+245+246+247+248+249+250+251+252 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 714+715+716+717+718+719+720+721+722+723 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 269+270+271+272+273+274+275+276+277+278+279+280 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 310+311+312+313+314+315+316+317+318+319+320+321 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 326+327+328+329+330+331+332+333+334+335+336 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 637+638+639+640+641+642+643+644+645+646+647 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 354+355+356+357+358+359+360+361+362+363+364+365 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 368+369+370+371+372+373+374+375+376+377+378+379 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 387+388+389+390+391+392+393+394+395+396+397+398+399+400 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 406+407+408+409+410+411+412+413+414+415+416+417+418+419 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 555+556+557+558+559+560+561+562+563+564+565+566+567+568 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 424+425+426+427+428+429+430+431+432+433+434+435+436+437+438+439+440+441+442 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 505+506+507+508+509+510+511+512+513+514+515+516+517+518+519+520 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 470+471+472+473+474+475+476+477+478+479+480+481+482+483+484+485+486+487+488+489+490+491+492+493+494+495+496+497 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 445+446+447+448+449+450+451+452+453+454+455+456+457+458+459+460+461 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 575+576+577+578+579+580+581+582+583+584+585+586+587+588+589 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 603+604+605+606+607+608+609+610+611+612+613+614+615+616+617 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 620+621+622+623+624+625+626+627+628+629 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 650+651+652+653+654+655+656+657+658+659 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("Astrand22", "resi 682+683+684+685+686+687+688+689+690+691+692+693 & chain A ")
cmd.color ("yellow", "Astrand22")


cmd.select("Astrand23", "resi 697+698+699+700+701+702+703+704+705+706 & chain A ")
cmd.color ("blue", "Astrand23")


cmd.select("Astrand24", "resi 284+285+286+287+288+289+290+291+292+293+294+295 & chain A ")
cmd.color ("red", "Astrand24")


cmd.select("Astrand25", "resi 745+746+747+748+749+750+751+752+753+754+755+756+757+758+759 & chain A ")
cmd.color ("green", "Astrand25")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
