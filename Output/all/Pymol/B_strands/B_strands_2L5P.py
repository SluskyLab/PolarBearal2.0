from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/2L5P.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Astrand0", "resi 51+52+53+54+55+56+57+58+59+60 & chain A ")
cmd.color ("red", "Astrand0")


cmd.select("Astrand1", "resi 86+87+88+89+90+91+92+93+94 & chain A ")
cmd.color ("green", "Astrand1")


cmd.select("Astrand2", "resi 75+76+77+78+79+80 & chain A ")
cmd.color ("orange", "Astrand2")


cmd.select("Astrand3", "resi 97+98+99+100+101+102+103+104+105+106+107 & chain A ")
cmd.color ("teal", "Astrand3")


cmd.select("Astrand4", "resi 113+114+115+116 & chain A ")
cmd.color ("yellow", "Astrand4")


cmd.select("Astrand5", "resi 128+129+130+131+132+133+134+135+136 & chain A ")
cmd.color ("blue", "Astrand5")


cmd.select("Astrand6", "resi 140+141+142+143+144+145+146+147+148 & chain A ")
cmd.color ("red", "Astrand6")


cmd.select("Astrand7", "resi 153+154+155+156+157+158+159+160+161 & chain A ")
cmd.color ("green", "Astrand7")


cmd.select("barrel", "Astrand*")
cmd.show("cartoon", "barrel")
cmd.zoom("barrel")
