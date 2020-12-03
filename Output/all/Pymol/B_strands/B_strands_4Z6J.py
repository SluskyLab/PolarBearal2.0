from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4Z6J.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 18+19+20+21+22 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 27+28+29+30+31+32+33+34 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 41+42+43+44+45+46+47+48+49 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 61+62+63+64+65+66+67+68+69 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 74+75+76+77+78+79+80+81+82 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 87+88+89+90+91+92+93+94+95+96+97+98+99 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 106+107+108+109+110+111+112+113+114+115+116+117 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 120+121+122+123+124+125+126+127+128+129+130+131+132 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
