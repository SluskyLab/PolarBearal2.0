from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4N75.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 427+428+429+430+431+432+433 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 799+800+801+802+803+804+805+806+807+808+809 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 781+782+783+784+785+786+787+788+789+790+791+792 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 767+768+769+770+771+772+773+774+775+776+777+778 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 733+734+735+736+737+738+739+740+741+742+743+744+745 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 710+711+712+713+714+715+716+717+718+719+720 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 628+629+630+631+632+633+634+635+636+637+638+639+640 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 608+609+610+611+612+613+614+615+616+617+618+619+620 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 590+591+592+593+594+595+596+597+598+599+600 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 564+565+566+567+568+569+570+571+572+573+574+575+576+577+578+579 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 523+524+525+526+527+528+529+530+531+532+533+534+535+536+537 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 505+506+507+508+509+510+511+512+513+514+515+516+517+518+519+520 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 484+485+486+487+488+489+490+491+492+493+494+495 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 466+467+468+469+470+471+472+473+474+475 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 455+456+457+458+459+460+461+462 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 437+438+439+440+441+442+443+444+445+446 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
