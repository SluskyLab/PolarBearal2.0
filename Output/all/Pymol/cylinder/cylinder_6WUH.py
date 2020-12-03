from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6WUH.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 273+273+274+275+276+277+290+291+292+293+294+295+296+297+310+311+312+313+314+315+316+336+337+338+339+340+341+342+343+344+395+396+397+398+399+400+401+402+420+421+422+423+426+427+428+469+470+471+472+473+474+475+476+477+486+487+488+489 & chain B")
cmd.load_cgo( [9.0, 85.30783,60.712475,100.896065, 78.663376, 105.74025, 90.54772, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
