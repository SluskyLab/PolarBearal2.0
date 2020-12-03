from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4GE1.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 22+23+24+25+26+27+28+29+30 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 129+130+131+132+133+134+135+136+137+138+139 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 119+120+121+122+123+124+125+126 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 101+102+103+104+105+106+107+108+109+110+111+112+113+114 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 87+88+89+90+91+92+93+94+95 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 68+69+70+71+72+73+74+75+76+77 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 54+55+56+57+58+59+60+61+62+63 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 42+43+44+45+46+47+48+49 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
