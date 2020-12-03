from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4R0B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 17+18+19+20+21+22+23+24+25+26 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 102+103+104+105+106+107+108+109 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 89+90+91+92+93+94+95+96+97 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 81+82+83+84+85+86 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 66+67+68+69+70+71+72+73+74+75 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 54+55+56+57+58+59+60+61 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 116+117+118+119+120+121+122+123 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 149+150+151+152+42+43+44+45+46+47+48 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
