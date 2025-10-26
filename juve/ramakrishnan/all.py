#!/usr/bin/env python3

if __name__ == '__main__':
    import leadmm
    import leadadas
    import leaddm
    import scoop
    import floodplain
    import glimmer
    import gene2life
    import motif
    import mememast
    import molsci
    import avianflu
    import cadsr
    import psload
    import psmerge
    import mcstas
    
    # DAX files
    leadmm.main("-D", "leadmm.xml")
    leadadas.main("-D", "leadadas.xml")
    leaddm.main("-D", "leaddm.xml")
    floodplain.main("-D", "floodplain.xml")
    glimmer.main("-D", "glimmer.xml")
    gene2life.main("-D", "gene2life.xml")
    mememast.main("-D", "mememast.xml")
    molsci.main("-D", "molsci.xml")
    cadsr.main("-D", "cadsr.xml")
    mcstas.main("-D", "mcstas.xml")
    motif.main("-D", "motif_small.xml", "-N", "10")
    motif.main("-D", "motif_medium.xml", "-N", "135")
    motif.main("-D", "motif_large.xml", "-N", "500")
    psload.main("-D", "psload_small.xml", "-N", "1", "-n", "5")
    psload.main("-D", "psload_medium.xml", "-N", "100", "-n", "5")
    psload.main("-D", "psload_large.xml", "-N", "1000", "-n", "5")
    psmerge.main("-D", "psmerge_small.xml", "-N", "1", "-L", "50", "-H", "100")
    psmerge.main("-D", "psmerge_medium.xml", "-N", "5", "-L", "100", "-H", "200")
    psmerge.main("-D", "psmerge_large.xml", "-N", "16", "-L", "300", "-H", "600")
    scoop.main("-D", "scoop_small.xml", "-N", "5")
    scoop.main("-D", "scoop_medium.xml", "-N", "50")
    scoop.main("-D", "scoop_large.xml", "-N", "100")
    avianflu.main("-D", "avianflu_small.xml", "-N", "100")
    avianflu.main("-D", "avianflu_medium.xml", "-N", "1000")
    avianflu.main("-D", "avianflu_large.xml", "-N", "2000")

    # JSON files
    leadmm.main("-j", "leadmm.json")
    leadadas.main("-j", "leadadas.json")
    leaddm.main("-j", "leaddm.json")
    floodplain.main("-j", "floodplain.json")
    glimmer.main("-j", "glimmer.json")
    gene2life.main("-j", "gene2life.json")
    mememast.main("-j", "mememast.json")
    molsci.main("-j", "molsci.json")
    cadsr.main("-j", "cadsr.json")
    mcstas.main("-j", "mcstas.json")
    motif.main("-j", "motif_small.json", "-N", "10")
    motif.main("-j", "motif_medium.json", "-N", "135")
    motif.main("-j", "motif_large.json", "-N", "500")
    psload.main("-j", "psload_small.json", "-N", "1", "-n", "5")
    psload.main("-j", "psload_medium.json", "-N", "100", "-n", "5")
    psload.main("-j", "psload_large.json", "-N", "1000", "-n", "5")
    psmerge.main("-j", "psmerge_small.json", "-N", "1", "-L", "50", "-H", "100")
    psmerge.main("-j", "psmerge_medium.json", "-N", "5", "-L", "100", "-H", "200")
    psmerge.main("-j", "psmerge_large.json", "-N", "16", "-L", "300", "-H", "600")
    scoop.main("-j", "scoop_small.json", "-N", "5")
    scoop.main("-j", "scoop_medium.json", "-N", "50")
    scoop.main("-j", "scoop_large.json", "-N", "100")
    avianflu.main("-j", "avianflu_small.json", "-N", "100")
    avianflu.main("-j", "avianflu_medium.json", "-N", "1000")
    avianflu.main("-j", "avianflu_large.json", "-N", "2000")
    
    # DOT files
    leadmm.main("-d", "leadmm.dot")
    leadadas.main("-d", "leadadas.dot")
    leaddm.main("-d", "leaddm.dot")
    floodplain.main("-d", "floodplain.dot")
    glimmer.main("-d", "glimmer.dot")
    gene2life.main("-d", "gene2life.dot")
    mememast.main("-d", "mememast.dot")
    molsci.main("-d", "molsci.dot")
    cadsr.main("-d", "cadsr.dot")
    mcstas.main("-d", "mcstas.dot")
    motif.main("-d", "motif.dot", "-N", "3")
    psload.main("-d", "psload.dot", "-N", "2", "-n", "3")
    psmerge.main("-d", "psmerge.dot", "-N", "2", "-L", "3", "-H", "3")
    scoop.main("-d", "scoop.dot", "-N", "3")
    avianflu.main("-d", "avianflu.dot", "-N", "3")
