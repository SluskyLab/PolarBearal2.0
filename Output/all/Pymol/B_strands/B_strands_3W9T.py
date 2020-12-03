from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/3W9T.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 304+305+306+307+308+309+310+311+312+313+314+315+316+317+318+319+320+321+322+323+324+325+326+327+328+329+330+331+332 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 337+338+339+340+341+342+343+344+345+346+347+348+349+350+351+352+353+354+355+356+357+358+359+360+361+362+363+364+365+366 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Gstrand2", "resi 304+305+306+307+308+309+310+311+312+313+314+315+316+317+318+319+320+321+322+323+324+325+326+327+328+329+330+331+332 & chain G ")
cmd.color ("orange", "Gstrand2")


cmd.select("Gstrand3", "resi 337+338+339+340+341+342+343+344+345+346+347+348+349+350+351+352+353+354+355+356+357+358+359+360+361+362+363+364+365+366 & chain G ")
cmd.color ("teal", "Gstrand3")


cmd.select("Fstrand4", "resi 304+305+306+307+308+309+310+311+312+313+314+315+316+317+318+319+320+321+322+323+324+325+326+327+328+329+330+331+332 & chain F ")
cmd.color ("yellow", "Fstrand4")


cmd.select("Fstrand5", "resi 337+338+339+340+341+342+343+344+345+346+347+348+349+350+351+352+353+354+355+356+357+358+359+360+361+362+363+364+365+366 & chain F ")
cmd.color ("blue", "Fstrand5")


cmd.select("Estrand6", "resi 304+305+306+307+308+309+310+311+312+313+314+315+316+317+318+319+320+321+322+323+324+325+326+327+328+329+330+331+332 & chain E ")
cmd.color ("red", "Estrand6")


cmd.select("Estrand7", "resi 337+338+339+340+341+342+343+344+345+346+347+348+349+350+351+352+353+354+355+356+357+358+359+360+361+362+363+364+365+366 & chain E ")
cmd.color ("green", "Estrand7")


cmd.select("Dstrand8", "resi 304+305+306+307+308+309+310+311+312+313+314+315+316+317+318+319+320+321+322+323+324+325+326+327+328+329+330+331+332 & chain D ")
cmd.color ("orange", "Dstrand8")


cmd.select("Dstrand9", "resi 337+338+339+340+341+342+343+344+345+346+347+348+349+350+351+352+353+354+355+356+357+358+359+360+361+362+363+364+365+366 & chain D ")
cmd.color ("teal", "Dstrand9")


cmd.select("Cstrand10", "resi 304+305+306+307+308+309+310+311+312+313+314+315+316+317+318+319+320+321+322+323+324+325 & chain C ")
cmd.color ("yellow", "Cstrand10")


cmd.select("Cstrand11", "resi 337+338+339+340+341+342+343+344+345+346+347+348+349+350+351+352+353+354+355+356+357+358+359+360+361+362+363+364+365+366 & chain C ")
cmd.color ("blue", "Cstrand11")


cmd.select("Cstrand12", "resi 328+329+330+331+332 & chain C ")
cmd.color ("red", "Cstrand12")


cmd.select("Bstrand13", "resi 304+305+306+307+308+309+310+311+312+313+314+315+316+317+318+319+320+321+322+323+324+325+326+327+328+329+330+331+332 & chain B ")
cmd.color ("green", "Bstrand13")


cmd.select("Bstrand14", "resi 337+338+339+340+341+342+343+344+345+346+347+348+349+350+351+352+353+354+355+356+357+358+359+360+361+362+363+364+365+366 & chain B ")
cmd.color ("orange", "Bstrand14")


cmd.select("barrel", "Astrand* or Gstrand* or Fstrand* or Estrand* or Dstrand* or Cstrand* or Bstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
