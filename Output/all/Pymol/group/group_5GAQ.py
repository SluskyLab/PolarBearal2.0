from pymol import cmd, stored
x = r"C:\Users\rikdh\Dropbox (Slusky Lab)\Rik\Projects_Rik\Barrel Comparison\Git_polar_bearal/DB/PDBs/5GAQ.pdb"
cmd.load(x)
cmd.hide("everything", "all")
cmd.color("wheat","all")
cmd.select("Group0", "(resi 11-28 & chain A, resi 111-122 & chain A, resi 128-138 & chain A, resi 148-156 & chain A, resi 11-28 & chain B, resi 111-122 & chain B, resi 128-138 & chain B, resi 148-156 & chain B, resi 11-28 & chain C, resi 111-122 & chain C, resi 128-138 & chain C, resi 148-156 & chain C, resi 11-28 & chain D, resi 111-122 & chain D, resi 128-138 & chain D, resi 148-156 & chain D, resi 11-28 & chain E, resi 111-122 & chain E, resi 128-138 & chain E, resi 148-156 & chain E, resi 11-28 & chain F, resi 111-122 & chain F, resi 128-138 & chain F, resi 148-156 & chain F, resi 11-28 & chain G, resi 111-122 & chain G, resi 128-138 & chain G, resi 148-156 & chain G, resi 11-28 & chain H, resi 111-122 & chain H, resi 128-138 & chain H, resi 148-156 & chain H, resi 11-28 & chain I, resi 111-122 & chain I, resi 128-138 & chain I, resi 148-156 & chain I, )")
cmd.color ("white", "Group0")


cmd.pseudoatom ("Centroid0", pos=[160.15946222941082,160.1596068827311,189.78125823974608])
cmd.color ("white", "Centroid0")


cmd.select("Group1", "(resi 34-66 & chain A, resi 74-107 & chain A, resi 34-66 & chain B, resi 74-107 & chain B, resi 34-66 & chain C, resi 74-107 & chain C, resi 34-66 & chain D, resi 74-107 & chain D, resi 34-66 & chain E, resi 74-107 & chain E, resi 34-66 & chain F, resi 74-107 & chain F, resi 34-66 & chain G, resi 74-107 & chain G, resi 34-66 & chain H, resi 74-107 & chain H, resi 34-66 & chain I, resi 74-107 & chain I, )")
cmd.color ("red", "Group1")


cmd.pseudoatom ("Centroid1", pos=[160.15936332436937,160.15945095486111,159.1345509518043])
cmd.color ("red", "Centroid1")


cmd.select("Group2", "(resi 168-172 & chain A, resi 178-184 & chain A, resi 187-193 & chain A, resi 232-235 & chain A, resi 223-226 & chain A, resi 209-213 & chain A, resi 200-204 & chain A, resi 281-285 & chain A, resi 269-273 & chain A, resi 291-295 & chain A, resi 257-259 & chain A, )")
cmd.color ("orange", "Group2")


cmd.pseudoatom ("Centroid2", pos=[120.03280001553622,175.0995996648615,163.28385481400923])
cmd.color ("orange", "Centroid2")


cmd.select("Group3", "(resi 168-172 & chain B, resi 178-184 & chain B, resi 187-193 & chain B, resi 232-235 & chain B, resi 223-226 & chain B, resi 209-213 & chain B, resi 200-204 & chain B, resi 281-285 & chain B, resi 269-273 & chain B, resi 291-295 & chain B, resi 257-259 & chain B, )")
cmd.color ("purple", "Group3")


cmd.pseudoatom ("Centroid3", pos=[139.0242904663086,197.39714521928266,163.28345447887074])
cmd.color ("purple", "Centroid3")


cmd.select("Group4", "(resi 168-172 & chain C, resi 178-184 & chain C, resi 187-193 & chain C, resi 232-235 & chain C, resi 223-226 & chain C, resi 209-213 & chain C, resi 200-204 & chain C, resi 281-285 & chain C, resi 269-273 & chain C, resi 291-295 & chain C, resi 257-259 & chain C, )")
cmd.color ("yellow", "Group4")


cmd.pseudoatom ("Centroid4", pos=[167.90452658913352,202.27056218927558,163.28387256969106])
cmd.color ("yellow", "Centroid4")


cmd.select("Group5", "(resi 168-172 & chain D, resi 178-184 & chain D, resi 187-193 & chain D, resi 232-235 & chain D, resi 223-226 & chain D, resi 209-213 & chain D, resi 200-204 & chain D, resi 281-285 & chain D, resi 269-273 & chain D, resi 291-295 & chain D, resi 257-259 & chain D, )")
cmd.color ("green", "Group5")


cmd.pseudoatom ("Centroid5", pos=[193.16090836958452,187.43989174582742,163.28398076837712])
cmd.color ("green", "Centroid5")


cmd.select("Group6", "(resi 168-172 & chain E, resi 178-184 & chain E, resi 187-193 & chain E, resi 232-235 & chain E, resi 223-226 & chain E, resi 209-213 & chain E, resi 200-204 & chain E, resi 281-285 & chain E, resi 269-273 & chain E, resi 291-295 & chain E, resi 257-259 & chain E, )")
cmd.color ("cyan", "Group6")


cmd.pseudoatom ("Centroid6", pos=[202.9760722767223,159.8444003018466,163.28394581187854])
cmd.color ("cyan", "Centroid6")


cmd.select("Group7", "(resi 168-172 & chain F, resi 178-184 & chain F, resi 187-193 & chain F, resi 232-235 & chain F, resi 223-226 & chain F, resi 209-213 & chain F, resi 200-204 & chain F, resi 281-285 & chain F, resi 269-273 & chain F, resi 291-295 & chain F, resi 257-259 & chain F, )")
cmd.color ("blue", "Group7")


cmd.pseudoatom ("Centroid7", pos=[192.7562364058061,132.3966180974787,163.2839277787642])
cmd.color ("blue", "Centroid7")


cmd.select("Group8", "(resi 168-172 & chain G, resi 178-184 & chain G, resi 187-193 & chain G, resi 232-235 & chain G, resi 223-226 & chain G, resi 209-213 & chain G, resi 200-204 & chain G, resi 281-285 & chain G, resi 269-273 & chain G, resi 291-295 & chain G, resi 257-259 & chain G, )")
cmd.color ("purple", "Group8")


cmd.pseudoatom ("Centroid8", pos=[167.2844365900213,117.93883666992187,163.28410866477273])
cmd.color ("purple", "Centroid8")


cmd.select("Group9", "(resi 168-172 & chain H, resi 178-184 & chain H, resi 187-193 & chain H, resi 232-235 & chain H, resi 223-226 & chain H, resi 209-213 & chain H, resi 200-204 & chain H, resi 281-285 & chain H, resi 269-273 & chain H, resi 291-295 & chain H, resi 257-259 & chain H, )")
cmd.color ("red", "Group9")


cmd.pseudoatom ("Centroid9", pos=[138.47885409268466,123.23647336092863,163.2838359485973])
cmd.color ("red", "Centroid9")


cmd.select("Group10", "(resi 168-172 & chain I, resi 178-184 & chain I, resi 187-193 & chain I, resi 232-235 & chain I, resi 223-226 & chain I, resi 209-213 & chain I, resi 200-204 & chain I, resi 281-285 & chain I, resi 269-273 & chain I, resi 291-295 & chain I, resi 257-259 & chain I, )")
cmd.color ("orange", "Group10")


cmd.pseudoatom ("Centroid10", pos=[119.81754608154297,145.8108359596946,163.28381791548296])
cmd.color ("orange", "Centroid10")


cmd.select("barrel", "Group*")
cmd.show("cartoon", "barrel")
cmd.show("sphere", "Centroid*")
cmd.zoom("barrel")
