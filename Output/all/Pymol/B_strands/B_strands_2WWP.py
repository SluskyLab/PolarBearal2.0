from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2WWP.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 41+42+43+44+45+46+47+48+49+50 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 144+145+146+147+148+149+150 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 77+78+79+80+81+82+83+84+85 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 128+129+130+131+132+133+134+135+136+137 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 88+89+90+91+92+93+94+95+96+97+98 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 104+105+106+107+108+109 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 114+115+116+117+118+119+120+121+122+123 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 65+66+67+68+69+70+71 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
