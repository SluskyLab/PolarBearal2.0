from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1VKY.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 67+68+69+70 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 78+79+80+81+82+83+84+85+86+87 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 126+127+128+129+130+131 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 113+114+115+116+117+118+119+120 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 90+91+92+93+94+95+96 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 106+107+108+109+110 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
