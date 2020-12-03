from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/6SCN.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("group", "resi 276+276+277+278+374+375+376 & chain a or resi 276+276+277+278+374+375+376 & chain b or resi 276+276+277+278+374+375+376 & chain c or resi 276+276+277+278+374+375+376 & chain d or resi 276+276+277+278+374+375+376 & chain e or resi 276+276+277+278+374+375+376 & chain f or resi 276+276+277+278+374+375+376 & chain g or resi 276+276+277+278+374+375+376 & chain A or resi 276+276+277+278+374+375+376 & chain B or resi 276+276+277+278+374+375+376 & chain C or resi 276+276+277+278+374+375+376 & chain D or resi 276+276+277+278+374+375+376 & chain E or resi 276+276+277+278+374+375+376 & chain F or resi 276+276+277+278+374+375+376 & chain G or resi 276+276+277+278+374+375+376 & chain H or resi 276+276+277+278+374+375+376 & chain I or resi 276+276+277+278+374+375+376 & chain J or resi 276+276+277+278+374+375+376 & chain K or resi 276+276+277+278+374+375+376 & chain L or resi 276+276+277+278+374+375+376 & chain M or resi 276+276+277+278+374+375+376 & chain N or resi 276+276+277+278+374+375+376 & chain O or resi 276+276+277+278+374+375+376 & chain P or resi 276+276+277+278+374+375+376 & chain Q or resi 276+276+277+278+374+375+376 & chain R or resi 276+276+277+278+374+375+376 & chain S or resi 276+276+277+278+374+375+376 & chain T or resi 276+276+277+278+374+375+376 & chain U or resi 276+276+277+278+374+375+376 & chain V or resi 276+276+277+278+374+375+376 & chain W or resi 276+276+277+278+374+375+376 & chain X or resi 276+276+277+278+374+375+376 & chain Y or resi 276+276+277+278+374+375+376 & chain Z")
cmd.load_cgo( [9.0, 169.0261,193.96649,207.54086, 186.07535, 161.1391, 82.70957, 2.5, 1,1,0,1,1,0], "cylinder2" )
cmd.color ("red", "Group")


cmd.show("cartoon", "group")
