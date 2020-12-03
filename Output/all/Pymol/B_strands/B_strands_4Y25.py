from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4Y25.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 518+519+520+521+522+523+524+525+526+527+528+529+530 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 793+794+795+796+797+798+799+800+801+802+803+804+805+806+807 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 776+777+778+779+780+781+782+783+784+785+786+787+788 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 757+758+759+760+761+762+763+764+765+766+767+768+769+770+771+772 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 738+739+740+741+742+743+744+745+746+747+748+749+750+751+752+753 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 718+719+720+721+722+723+724+725+726+727+728+729+730+731+732+733+734+735 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 693+694+695+696+697+700+701+702+703+704+705 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 659+660+661+662+663+664+665+666+667+668+669+670 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 675+676+677+678+679+680+681+682+683+684+685+686+687+688+689 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 644+645+646+647+648+649+650+651+652+653+654 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 620+621+622+623+624+625+626+627+628 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 604+605+606+607+608+609+610+611+612+613+614+615 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 589+590+591+592+593+594+595+596+597+598+599 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 575+576+577+578+579+580+581+582+583+584+585+586 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 555+556+557+558+559+560+561+562+563+564+565 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 540+541+542+543+544+545+546+547 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
