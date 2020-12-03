from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/4H6B.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 12+13+14+15+16+17+18+19 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 141+142+143+144+145+146+147+148+149 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 128+129+130+131+132+133+134+135+136+137 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 113+114+115+116+117+118+119+120 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 84+85+86+87+88+89+90+91+92+93+94 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 65+66+67+68+69+70+71+72+73+74+75+76+77+78+79 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 100+101+102+103+104+105+106+107+108 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 50+51+52+53+56+57+58+59 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
