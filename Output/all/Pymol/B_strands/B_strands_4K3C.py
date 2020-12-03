from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4K3C.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 421+422+423+424+425+426+427+428+429+430 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 434+435+436+437+438+439+440+441+442+443+444+445+446 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 451+452+453+454+455+456+457+458+459 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 463+464+465+466+467+468+469+470+471+472+473+474+475 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 481+482+483+484+485+486+487+488+489+490+491+492 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 503+504+505+506+507+508+509+510+511+512+513+514+515 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 521+522+523+524+525+526+527+528+529+530+531+532+533+534+535 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 569+570+571+572+573+574+575+576+577+578 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 589+590+591+592+593+594+595+596+597+598+599 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 627+628+629+630+631+632+633+634+635+636+637+638+639 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 607+608+609+610+611+612+613+614+615+616+617+618+619 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 691+692+693+694+695+696+697+698+699+700+701 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 714+715+716+717+718+719+720+721+722+723+724+725+726 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 750+751+752+753+754+755+756+757+758+759+760+761 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 764+765+766+767+768+769+770+771+772+773+774+775 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 782+783+784+785+786+787+788+789+790+791+792 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
