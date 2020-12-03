from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2FIM.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 252+253+254+255+256+257+258+259 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 270+271+272+273+274+275 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 451+452+453+454+455+456+457 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 281+282+283+284+285+286+287+288 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 296+297+298+299+300 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 313+314+315+316+317+318+319 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 325+326+327+328+329 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 349+350+351+352+353+354+355 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 368+369+370+371+372+373 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 405+406+407+408+409+410 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 438+439+440+441 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 460+461+462+463+464+465 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
