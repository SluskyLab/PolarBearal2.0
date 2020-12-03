from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/1MK5.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 19+20+21+22+23 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 28+29+30+31+32+33 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 38+39+40+41+42+43+44 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 54+55+56+57+58+59+60 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 71+72+73+74+75+76+77+78+79+80 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 85+86+87+88+89+90+91+92+93+94+95+96+97 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 103+104+105+106+107+108+109+110+111+112 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 123+124+125+126+127+128+129+130+131+132+133 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
