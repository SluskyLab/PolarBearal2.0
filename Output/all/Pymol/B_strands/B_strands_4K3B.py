from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4K3B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 425+426+427+428+429+430+431+432+433 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 437+438+439+440+441+442+443+444+445+446+447+448+449 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 454+455+456+457+458+459+460+461+462 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 466+467+468+469+470+471+472+473+474+475+476+477+478+479 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 483+484+485+486+487+488+489+490+491+492+493+494 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 507+508+509+510+511+512+513+514+515+516+517+518+519+520 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 626+627+628+629+630+631+632+633+634+635 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 609+610+611+612+613+614+615+616+617+618+619+620 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 591+592+593+594+595+596+597+598+599+600 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 564+565+566+567+568+569+570+571+572+573+574+575+576+577+578+579+580 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 685+686+687+688+689+690+691+692+693+694+695 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 526+527+528+529+530+531+532+533+534+535+536+537+538+539 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 706+707+708+709+710+711+712+713+714+715+716+717+718 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 749+750+751+752+753+754+755+756+757+758+759 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 764+765+766+767+768+769+770+771+772+773 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 784+785+786+787+788+789 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
