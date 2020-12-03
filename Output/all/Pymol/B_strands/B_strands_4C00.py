from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4C00.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 267+268+269+270+271+272+273+274+275+276 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 568+569+570+571+572+573 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 549+550+551+552+553+554+555+556+557+558 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 535+536+537+538+539+540+541+542+543+544+545+546 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 514+515+516+517+518+519+520+521+522+523+524+525+526 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 497+498+499+500+501+502+503+504+505+506+507+508+509+510+511 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 442+443+444+445+446+447+448+449+450+451+452+453+454+455+456 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 426+427+428+429+430+431+432+433+434+435+436+437+438+439 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("Astrand8", "resi 404+405+406+407+408+409+410+411+412+413+414+415+416 & chain A ")
cmd.color ("orange", "Astrand8")


cmd.select("Astrand9", "resi 379+380+381+382+383+384+385+386+387+388+389+390+391+392+393+394+395+396+397+398 & chain A ")
cmd.color ("teal", "Astrand9")


cmd.select("Astrand10", "resi 361+362+363+364+365+366+367+368+369+370+371+372+373+374+375+376 & chain A ")
cmd.color ("yellow", "Astrand10")


cmd.select("Astrand11", "resi 342+343+344+345+346+347+348+349+350+351+352+353+354+355+356+357 & chain A ")
cmd.color ("blue", "Astrand11")


cmd.select("Astrand12", "resi 326+327+328+329+330+331+332+333+334+335+336+337+338+339 & chain A ")
cmd.color ("red", "Astrand12")


cmd.select("Astrand13", "resi 308+309+310+311+312+313+314+315+316+317+318 & chain A ")
cmd.color ("green", "Astrand13")


cmd.select("Astrand14", "resi 297+298+299+300+301+302+303+304+305 & chain A ")
cmd.color ("orange", "Astrand14")


cmd.select("Astrand15", "resi 280+281+282+283+284+285+286+287+288 & chain A ")
cmd.color ("teal", "Astrand15")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
