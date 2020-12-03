from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6UWR.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Hstrand0", "resi 300+301+302+303+304+305+306+307+308+309+310 & chain H ")
cmd.color ("red", "Hstrand0")


cmd.select("Hstrand1", "resi 322+323+324+325+326+327+328+329+330 & chain H ")
cmd.color ("green", "Hstrand1")


cmd.select("Hstrand2", "resi 362+363+364+365+366+367 & chain H ")
cmd.color ("orange", "Hstrand2")


cmd.select("Hstrand3", "resi 477+478+479+480+481+482+483+484+485+486 & chain H ")
cmd.color ("teal", "Hstrand3")


cmd.select("Hstrand4", "resi 404+405+406+407+408+409+410+411+412+413 & chain H ")
cmd.color ("yellow", "Hstrand4")


cmd.select("Hstrand5", "resi 418+419+420+421+422+423 & chain H ")
cmd.color ("blue", "Hstrand5")


cmd.select("Hstrand6", "resi 460+461+462 & chain H ")
cmd.color ("red", "Hstrand6")


cmd.select("Hstrand7", "resi 387+388+389+390+391+392+393+394+395+396+397 & chain H ")
cmd.color ("green", "Hstrand7")


cmd.select("barrel", "Hstrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
