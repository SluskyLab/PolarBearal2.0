from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2FIM.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 252+252+253+254+255+256+257+258+259+270+271+272+273+274+275+281+282+283+284+285+286+287+288+296+297+298+299+300+313+314+315+316+317+318+319+325+326+327+328+329+349+350+351+352+353+354+355+368+369+370+371+372+373+405+406+407+408+409+410+438+439+440+441+451+452+453+454+455+456+457+460+461+462+463+464+465 & chain A")
cmd.load_cgo( [9.0, 78.41457,14.146196,18.87719, 97.684715, -18.303476, 33.14217, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
