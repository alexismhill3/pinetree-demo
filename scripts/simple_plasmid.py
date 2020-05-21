# Derived from the Pinetree documentation site
# source: https://pinetree.readthedocs.io/en/latest/intro.html

import pinetree as pt

if __name__ == "__main__":
    
    # Initialize Model and Genome objects
    # These are the only objects needed to run a simulation
    model = pt.Model(cell_volume=8e-16)
    plasmid = pt.Genome(name="myplasmid", 
                        length=410, 
                        transcript_degradation_rate_ext=1e-2,
                        transcript_degradation_rate=1e-2,
                        rnase_speed=20,
                        rnase_footprint=10)

    # Add some features to our genome
    plasmid.add_gene(name="rnapol", start=26, stop=225,
                    rbs_start=11, rbs_stop=26, rbs_strength=1e7)
    plasmid.add_gene(name="proteinX", start=241, stop=280,
                    rbs_start=226, rbs_stop=241, rbs_strength=1e7)
    plasmid.add_gene(name="proteinY", start=306, stop=390, 
                    rbs_start=291, rbs_stop=306, rbs_strength=1e7)
    
    plasmid.add_promoter(name="phi1", start=1, stop=10,
                        interactions={"rnapol": 2e8})
    plasmid.add_rnase_site(start=281, stop=290)
    plasmid.add_terminator(name="t1", start=409, stop=410,
                        efficiency={"rnapol": 1.0})

    # Add our genome to the simulation
    model.register_genome(plasmid)

    # Add some more species to the simulation
    model.add_polymerase(name="rnapol", speed=40, footprint=10, copy_number=10)
    model.add_ribosome(speed=30, footprint=10, copy_number=100)
    model.add_species(name="rnapol-X", copy_number=0)
    model.add_species(name="proteinY", copy_number=0)

    # Define a reaction between proteinX and rnapol
    model.add_reaction(reactants=['proteinX', 'rnapol'],
                    products=['rnapol-X'],
                    rate_constant=1e3)

    model.seed(3)

    # Run the simulation!
    model.simulate(time_limit=180, time_step=1, output="../data/simple_plasmid.tsv")
