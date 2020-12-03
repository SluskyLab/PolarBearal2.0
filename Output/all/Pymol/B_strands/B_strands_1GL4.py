from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1GL4.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 400+401+402+403+404+405+406+407+408+409+410+411+412+413+414 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 515+516+517+518+519+520+521+522+523+524+525 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 485+486+487+488+489+490+491+492+493+494 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 618+619+620+621+622+623+624+625+626+627+628 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 600+601+602+603+604+605+606+607+608+609+610+611+612+613 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 534+535+536+537+538+539+540+541+542+543+544+545+546+547 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 550+551+552+553+554+555+556+557+558+559+560+561+562 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 573+574+575+576+577+578+579+580+581+582+583+584 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 500+501+502+503+504+505+506+507 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 438+439+440+441+442+443+444+445+446 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 419+420+421+422+423+424+425+426+427+428+429+430+431+432+433 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
