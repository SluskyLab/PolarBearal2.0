from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3CSL.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 243+244+245+246+247+248+249+250+251+252 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 258+259+260+261+262+263+264+265+266 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 271+272+273+274+275+276+277+278+279+280+281+282 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 322+323+324+325+326+327+328+329+330+331+332+333+334+335 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 339+340+341+342+343+344+345+346+347+348+349+350+351+352+353+354+355 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 373+374+375+376+377+378+379+380+381+382+383+384+385+386+387+388+389+390 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 400+401+402+403+404+405+406+407+408+409+410+411+412+413+414+415 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 426+427+428+429+430+431+432+433+434+435+436+437+438+439+440+441+442+443+444+445+446+447+448 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 451+452+453+454+455+456+457+458+459+460+461+462+463+464+465+466+467+468+469+470 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 482+483+484+485+486+487+488+489+490+491+492+493+494+495+496+497 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 501+502+503+504+505+506+507+508+509+510+511+512+513+514+515+516+517+518 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 554+555+556+557+558+559+560+561+562+563+564+565+566+567+568+569+570+571 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 578+579+580+581+582+583+584+585+586+587+588+589 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 617+618+619+620+621+622+623+624+625+626+627+628+629+630+631 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 639+640+641+642+643+644+645+646+647+648+649+650+651+652 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 682+683+684+685+686+687+688+689+690+691+692+693+694+695 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("Astrand16", "resi 699+700+701+702+703+704+705+706+707+708+709 & chain A ")
cmd.color ("yellow", "Astrand16")


cmd.select("Astrand17", "resi 766+767+768+769+770+771+772+773 & chain A ")
cmd.color ("blue", "Astrand17")


cmd.select("Astrand18", "resi 782+783+784+785+786+787+788+789 & chain A ")
cmd.color ("red", "Astrand18")


cmd.select("Astrand19", "resi 810+811+812+813+814+815+816+817+818+819+820 & chain A ")
cmd.color ("green", "Astrand19")


cmd.select("Astrand20", "resi 825+826+827+828+829+830+831 & chain A ")
cmd.color ("orange", "Astrand20")


cmd.select("Astrand21", "resi 857+858+859+860+861+862+863+864 & chain A ")
cmd.color ("teal", "Astrand21")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
