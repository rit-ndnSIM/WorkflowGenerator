#!/usr/bin/env python3

if __name__ == '__main__':
    import pipeline
    import fmri
    import protein
    
    # DAX files
    pipeline.main("-D", "pipeline.xml")
    fmri.main("-D", "fmri.xml")
    protein.main("-D", "protein.xml")
    
    # JSON files
    pipeline.main("-j", "pipeline.json")
    fmri.main("-j", "fmri.json")
    protein.main("-j", "protein.json")
    
    # DOT files
    pipeline.main("-d", "pipeline.dot")
    fmri.main("-d", "fmri.dot")
    protein.main("-d", "protein.dot")
